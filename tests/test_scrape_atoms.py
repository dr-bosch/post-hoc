import importlib.util
import unittest
from pathlib import Path

from bs4 import BeautifulSoup


SCRIPT = Path(__file__).resolve().parents[1] / "scrape-atoms.py"
SPEC = importlib.util.spec_from_file_location("scrape_atoms", SCRIPT)
scrape_atoms = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scrape_atoms)


class AtomBuildTests(unittest.TestCase):
    def test_root_level_glob_does_not_match_nested_file(self):
        self.assertTrue(scrape_atoms.path_matches("README.md", "*.md"))
        self.assertFalse(
            scrape_atoms.path_matches(".github/copilot-instructions.md", "*.md")
        )

    def test_index_manifest_includes_root_index(self):
        manifest = scrape_atoms.load_manifest()
        parser = manifest["parsers"]["structured_html_atoms"]
        files = scrape_atoms.manifest_files(parser["include"], parser["exclude"])
        paths = {path.relative_to(scrape_atoms.REPO_ROOT).as_posix() for path in files}
        self.assertIn("index.html", paths)

    def test_claude_md_is_excluded_from_atom_input_scope(self):
        manifest = scrape_atoms.load_manifest()
        scope = manifest["input_scope"]
        files = scrape_atoms.manifest_files(scope["include"], scope["exclude"])
        paths = {path.relative_to(scrape_atoms.REPO_ROOT).as_posix() for path in files}
        self.assertNotIn("CLAUDE.md", paths)
        self.assertIn("CLAUDE.md", manifest["build_control_files"])

    def test_sync_wrapper_is_listed_as_a_build_control(self):
        manifest = scrape_atoms.load_manifest()
        self.assertIn("sync-atoms.sh", manifest["build_control_files"])

    def test_changed_input_paths_detect_add_modify_and_delete(self):
        previous = {
            "input_sha256": {
                "corpus/old.md": "old",
                "corpus/edited.md": "before",
            }
        }
        current = {
            "input_sha256": {
                "corpus/edited.md": "after",
                "corpus/new.md": "new",
            }
        }
        changes = scrape_atoms.changed_input_paths(previous, current)
        self.assertEqual(
            changes,
            [
                {"status": "M", "path": "corpus/edited.md", "scope": "input"},
                {"status": "A", "path": "corpus/new.md", "scope": "input"},
                {"status": "D", "path": "corpus/old.md", "scope": "input"},
            ],
        )

    def test_merge_refreshes_changed_pages_and_preserves_other_records(self):
        existing = [
            {"page": "corpus/keep/index.html", "body": "keep"},
            {"page": "corpus/update/index.html", "body": "old"},
            {"page": "corpus/delete/index.html", "body": "remove"},
        ]
        refreshed = [
            {"page": "corpus/update/index.html", "body": "new"},
        ]
        html_files = [
            scrape_atoms.REPO_ROOT / "corpus/keep/index.html",
            scrape_atoms.REPO_ROOT / "corpus/update/index.html",
        ]
        merged = scrape_atoms.merge_refreshed_atoms(
            existing,
            refreshed,
            {"corpus/update/index.html", "corpus/delete/index.html"},
            html_files,
            [],
        )
        self.assertEqual(
            merged,
            [
                {"page": "corpus/keep/index.html", "body": "keep"},
                {"page": "corpus/update/index.html", "body": "new"},
            ],
        )

    def test_atom_block_emits_one_record_per_tagged_paragraph(self):
        soup = BeautifulSoup(
            """
            <div class="atom">
              <p><span class="tag OBS">OBS</span> A source statement.</p>
              <p><span class="tag INT">INT</span> A separate reading.</p>
              <div class="src">source: example</div>
            </div>
            """,
            "html.parser",
        )
        records = scrape_atoms.parse_atom(soup.div, "example/index.html", "Section")
        self.assertEqual([record["type"] for record in records], ["OBS", "INT"])
        self.assertEqual(
            [record["body"] for record in records],
            ["A source statement.", "A separate reading."],
        )
        self.assertTrue(all(record["source"] == "source: example" for record in records))

    def test_untagged_atom_container_is_not_emitted_as_unknown_evidence(self):
        soup = BeautifulSoup('<div class="atom">Diagram labels only</div>', "html.parser")
        self.assertEqual(
            scrape_atoms.parse_atom(soup.div, "example/index.html", "Section"),
            [],
        )

    def test_fsd_panel_is_not_reported_as_a_validated_classification(self):
        soup = BeautifulSoup(
            """
            <div class="fsd-class">
              <div class="fsd-label">FSD classification: fsd:Submission</div>
              <p>A panel assertion.</p>
            </div>
            """,
            "html.parser",
        )
        record = scrape_atoms.parse_fsd_class(
            soup.div, "example/index.html", "Section"
        )
        self.assertEqual(record["type"], "FSD_PANEL")

    def test_legacy_fsd_tag_is_reported_as_a_panel_not_evidence_status(self):
        soup = BeautifulSoup(
            """
            <div class="atom">
              <span class="tag">FSD</span>
              <span class="src">FSD-Ontology-2026.md</span>
              <p class="fsd-label">Determination</p>
              <p>A controlled class label.</p>
            </div>
            """,
            "html.parser",
        )
        records = scrape_atoms.parse_atom(
            soup.div, "example/index.html", "Section"
        )
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["type"], "FSD_PANEL")

    def test_ontology_mentions_are_term_occurrences_not_classes(self):
        concept = {
            "identifier": "Submission",
            "term": "fsd:Submission",
            "label": "Submission",
        }
        source = scrape_atoms.REPO_ROOT / "DETE-letter-Sep-10_clean.md"
        records = scrape_atoms.scrape_concepts(source, [concept])
        self.assertTrue(records)
        self.assertTrue(all(record["type"] == "TERM" for record in records))
        self.assertTrue(
            all("not a classification" in record["source"] for record in records)
        )

    def test_concept_search_does_not_match_partial_identifiers_or_words(self):
        self.assertFalse(
            scrape_atoms.contains_concept_alias(
                "fsd:SubmissionOfNationalUtility", "fsd:Submission"
            )
        )
        self.assertFalse(
            scrape_atoms.contains_concept_alias(
                "Submissions are referenced.", "Submission"
            )
        )
        self.assertTrue(
            scrape_atoms.contains_concept_alias(
                "A `fsd:Submission` is named.", "fsd:Submission"
            )
        )

    def test_new_corpus_source_is_flagged_for_manual_atomization(self):
        manifest = scrape_atoms.load_manifest()
        report = scrape_atoms.status_report(
            manifest,
            None,
            [],
            [],
            [],
            [
                {
                    "status": "A",
                    "path": "corpus/new-source.pdf",
                    "scope": "input",
                }
            ],
            [],
            True,
            {},
            [],
        )
        self.assertEqual(
            report["manual_review_required"],
            [
                {
                    "status": "A",
                    "path": "corpus/new-source.pdf",
                    "scope": "input",
                }
            ],
        )


if __name__ == "__main__":
    unittest.main()
