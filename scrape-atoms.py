"""Build the machine-readable atom exports and timestamped build status."""

import argparse
import csv
from datetime import datetime, timezone
import fnmatch
import hashlib
import json
import re
import subprocess
from pathlib import Path

from bs4 import BeautifulSoup

REPO_ROOT = Path(__file__).resolve().parent
MANIFEST = REPO_ROOT / "atom-build-manifest.json"
ONTOLOGY = REPO_ROOT / "FSD-Ontology-2026.md"
OUTPUT_JSON = REPO_ROOT / "atoms.json"
OUTPUT_CSV = REPO_ROOT / "atoms.csv"
OUTPUT_MD = REPO_ROOT / "atoms.md"
STATUS_JSON = REPO_ROOT / "build" / "atom-build-status.json"
STATUS_MD = REPO_ROOT / "build" / "atom-build-status.md"

STATUS_MAP = {
    "OBS": "OBS",
    "INT": "INT",
    "INF": "INF",
    "HYP": "HYP",
}
CSV_FIELDS = [
    "type",
    "concept",
    "page",
    "section",
    "body",
    "source",
    "gap",
    "see_also",
]


def clean(text: str) -> str:
    """Collapse whitespace and strip."""
    return re.sub(r"\s+", " ", text or "").strip()


def camel_to_words(value: str) -> str:
    """Convert an ontology identifier such as NullificationLoop to words."""
    return re.sub(r"(?<!^)([A-Z])", r" \1", value)


def ontology_concepts() -> list[dict]:
    """Read FSD class identifiers and labels from the ontology master file."""
    text = ONTOLOGY.read_text(encoding="utf-8")
    concepts = []
    class_pattern = re.compile(
        r"^fsd:(?P<identifier>[A-Za-z0-9_]+)\s*$"
        r"(?P<body>.*?)(?=^fsd:[A-Za-z0-9_]+\s*$|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    for match in class_pattern.finditer(text):
        identifier = match.group("identifier")
        body = match.group("body")
        if "a owl:Class" not in body:
            continue
        label_match = re.search(r'rdfs:label\s+"([^"]+)"', body)
        label = label_match.group(1) if label_match else camel_to_words(identifier)
        concepts.append(
            {
                "identifier": identifier,
                "term": f"fsd:{identifier}",
                "label": label,
            }
        )
    return concepts


def document_text(path: Path) -> str:
    """Extract visible text from Markdown or HTML without changing the source."""
    raw = path.read_text(encoding="utf-8")
    if path.suffix.lower() != ".html":
        return raw
    soup = BeautifulSoup(raw, "html.parser")
    for element in soup(["script", "style", "noscript"]):
        element.decompose()
    return soup.get_text("\n")


def split_passages(text: str) -> list[str]:
    """Keep source passages small enough for each concept occurrence to be traceable."""
    passages = []
    for block in re.split(r"\n\s*\n", text):
        block = clean(block)
        if not block:
            continue
        passages.extend(
            clean(sentence)
            for sentence in re.split(r"(?<=[.!?])\s+", block)
            if clean(sentence)
        )
    return passages


def contains_concept_alias(text: str, alias: str) -> bool:
    """Match a whole class identifier or label, not an arbitrary substring."""
    escaped = re.escape(alias)
    if alias.startswith("fsd:"):
        pattern = rf"(?<![A-Za-z0-9_:]){escaped}(?![A-Za-z0-9_])"
    else:
        pattern = rf"(?<!\w){escaped}(?!\w)"
    return re.search(pattern, text, flags=re.IGNORECASE) is not None


def scrape_concepts(path: Path, concepts: list[dict]) -> list[dict]:
    """Record literal ontology term mentions, not class assignments."""
    passages = split_passages(document_text(path))
    atoms = []
    for passage in passages:
        for concept in concepts:
            aliases = (concept["term"], concept["label"])
            if not any(contains_concept_alias(passage, alias) for alias in aliases):
                continue
            atoms.append(
                {
                    "type": "TERM",
                    "concept": concept["term"],
                    "page": str(path.relative_to(REPO_ROOT)),
                    "section": "",
                    "body": passage,
                    "source": (
                        f"{ONTOLOGY.name} — {concept['label']} "
                        "(term occurrence only; not a classification)"
                    ),
                    "gap": "",
                    "see_also": "",
                }
            )
    return atoms


def path_matches(path: str, pattern: str) -> bool:
    """Match repository-relative paths against manifest glob patterns."""
    if "/" not in pattern and not pattern.startswith("**/"):
        return Path(path).parent == Path(".") and fnmatch.fnmatchcase(
            Path(path).name, pattern
        )
    return Path(path).match(pattern) or (
        pattern.startswith("**/") and Path(path).match(pattern[3:])
    )


def manifest_files(patterns: list[str], excludes: list[str]) -> list[Path]:
    """Expand manifest patterns into a stable, deduplicated file list."""
    selected = set()
    for pattern in patterns:
        selected.update(
            path for path in REPO_ROOT.glob(pattern) if path.is_file()
        )
    return sorted(
        (
            path
            for path in selected
            if not any(
                path_matches(path.relative_to(REPO_ROOT).as_posix(), pattern)
                for pattern in excludes
            )
        ),
        key=lambda path: path.relative_to(REPO_ROOT).as_posix(),
    )


def parse_atom(div, page_path: str, section: str) -> list[dict]:
    """Extract each evidence-tagged paragraph in a .atom block separately."""
    src_el = div.find(class_="src")
    gap_el = div.find(class_="gap")
    sa_el = div.find(class_="see-also")
    source = clean(src_el.get_text()) if src_el else ""
    gap = clean(gap_el.get_text()) if gap_el else ""
    see_also = clean(sa_el.get_text()) if sa_el else ""

    records = []
    seen_containers = set()
    for tag_el in div.find_all(class_="tag"):
        container = tag_el.find_parent(["p", "li"]) or tag_el.parent
        if container is None or id(container) in seen_containers:
            continue
        seen_containers.add(id(container))
        status_raw = clean(tag_el.get_text())
        status = next(
            (key for key in STATUS_MAP if status_raw.upper().startswith(key)),
            status_raw[:3].upper(),
        )
        if status == "FSD":
            status = "FSD_PANEL"
        copy = BeautifulSoup(str(container), "html.parser")
        copied_tag = copy.find(class_="tag")
        if copied_tag:
            copied_tag.decompose()
        body = clean(copy.get_text(" "))
        if body:
            records.append(
                {
                    "type": status,
                    "page": page_path,
                    "section": section,
                    "body": body,
                    "source": source,
                    "gap": gap,
                    "see_also": see_also,
                }
            )

    if records:
        return records

    if not div.find(class_="tag"):
        return []

    fallback = BeautifulSoup(str(div), "html.parser")
    fallback_tag = fallback.find(class_="tag")
    status_raw = clean(fallback_tag.get_text()) if fallback_tag else "UNKNOWN"
    status = next(
        (key for key in STATUS_MAP if status_raw.upper().startswith(key)),
        status_raw[:3].upper(),
    )
    if fallback_tag:
        fallback_tag.decompose()
    return [
        {
            "type": status,
            "page": page_path,
            "section": section,
            "body": clean(fallback.get_text(" ")),
            "source": source,
            "gap": gap,
            "see_also": see_also,
        }
    ]


def parse_fsd_class(div, page_path: str, section: str) -> dict:
    """Extract a .fsd-class block."""
    label_el = div.find(class_="fsd-label")
    src_el = div.find(class_="src")

    label = clean(label_el.get_text()) if label_el else ""
    source = clean(src_el.get_text()) if src_el else ""

    for element in [label_el, src_el]:
        if element:
            element.decompose()

    body = clean(div.get_text())

    return {
        "type": "FSD_PANEL",
        "page": page_path,
        "section": section,
        "body": f"{label} — {body}".strip(" —"),
        "source": source,
        "gap": "",
        "see_also": "",
    }


def parse_chrono(div, page_path: str, section: str) -> dict:
    """Extract a .chrono entry."""
    date_el = div.find(class_="date")
    actor_el = div.find(class_="actor")
    cons_el = div.find(class_="consequence")
    src_el = div.find(class_="src")
    gap_el = div.find(class_="gap")

    date_str = clean(date_el.get_text()) if date_el else ""
    actor = clean(actor_el.get_text()) if actor_el else ""
    consequence = clean(cons_el.get_text()) if cons_el else ""
    source = clean(src_el.get_text()) if src_el else ""
    gap = clean(gap_el.get_text()) if gap_el else ""

    for element in [date_el, actor_el, cons_el, src_el, gap_el]:
        if element:
            element.decompose()

    body = clean(div.get_text())

    return {
        "type": "CHR",
        "page": page_path,
        "section": f"{section} [{date_str} · {actor}]",
        "body": body,
        "source": source,
        "gap": f"{consequence} | {gap}".strip(" |"),
        "see_also": "",
    }


def scrape_file(html_path: Path) -> list[dict]:
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    page_path = str(html_path.relative_to(REPO_ROOT))
    atoms = []
    current_section = ""

    body = soup.find("body")
    if body is None:
        return atoms

    # Parsers remove tagged child nodes while extracting an atom; snapshot the
    # traversal first so adjacent atom blocks are not skipped.
    for element in list(body.descendants):
        if not hasattr(element, "name"):
            continue
        if element.name in ("h2", "h3"):
            current_section = clean(element.get_text())
        elif element.name == "div":
            classes = element.get("class", [])
            if "atom" in classes:
                atoms.extend(parse_atom(element, page_path, current_section))
            elif "fsd-class" in classes:
                atoms.append(parse_fsd_class(element, page_path, current_section))
            elif "chrono" in classes:
                atoms.append(parse_chrono(element, page_path, current_section))

    return atoms


def git_output(*args: str) -> str:
    """Run git and return its output, failing clearly if git fails."""
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def file_sha256(path: Path) -> str:
    """Return a stable content fingerprint for a repository file."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def make_sync_state(
    input_files: list[Path],
    html_files: list[Path],
    term_files: list[Path],
) -> dict:
    """Capture the file and parser state needed for a later incremental sync."""
    return {
        "input_sha256": {
            path.relative_to(REPO_ROOT).as_posix(): file_sha256(path)
            for path in input_files
        },
        "structured_html_inputs": [
            path.relative_to(REPO_ROOT).as_posix() for path in html_files
        ],
        "ontology_term_inputs": [
            path.relative_to(REPO_ROOT).as_posix() for path in term_files
        ],
        "parser_contract_sha256": {
            path.name: file_sha256(path)
            for path in (MANIFEST, Path(__file__).resolve(), ONTOLOGY)
        },
    }


def changed_input_paths(previous: dict, current: dict) -> list[dict]:
    """Find changed, added, and deleted inputs by comparing content hashes."""
    old_hashes = previous.get("input_sha256", {})
    new_hashes = current.get("input_sha256", {})
    changes = []
    for path in sorted(set(old_hashes) | set(new_hashes)):
        if path not in old_hashes:
            status = "A"
        elif path not in new_hashes:
            status = "D"
        elif old_hashes[path] != new_hashes[path]:
            status = "M"
        else:
            continue
        changes.append({"status": status, "path": path, "scope": "input"})
    return changes


def merge_refreshed_atoms(
    existing: list[dict],
    refreshed: list[dict],
    refresh_paths: set[str],
    html_files: list[Path],
    term_files: list[Path],
) -> list[dict]:
    """Replace records from refreshed files and retain all other records."""
    atoms = [
        atom for atom in existing if atom.get("page") not in refresh_paths
    ] + refreshed
    page_order = {
        path.relative_to(REPO_ROOT).as_posix(): index
        for index, path in enumerate(html_files + term_files)
    }
    return sorted(
        atoms,
        key=lambda atom: (
            page_order.get(atom.get("page", ""), len(page_order)),
            atom.get("page", ""),
        ),
    )


def load_sync_baseline(current_state: dict) -> list[dict]:
    """Load and validate prior exports before applying an incremental update."""
    if not STATUS_JSON.is_file() or not OUTPUT_JSON.is_file():
        raise ValueError(
            "Incremental sync needs a previous full-build status and atom "
            "export. Run ./build-atoms.sh once to establish the baseline."
        )
    previous_report = json.loads(STATUS_JSON.read_text(encoding="utf-8"))
    previous_state = previous_report.get("sync_state")
    if not previous_state:
        raise ValueError(
            "The saved build status has no sync baseline. Run "
            "./build-atoms.sh once to establish it."
        )
    if previous_state.get("parser_contract_sha256") != current_state.get(
        "parser_contract_sha256"
    ):
        raise ValueError(
            "The manifest, parser, or ontology changed since the saved "
            "baseline. Run ./build-atoms.sh for a full rebuild before syncing."
        )
    if previous_state.get("atom_export_sha256") != file_sha256(OUTPUT_JSON):
        raise ValueError(
            "atoms.json no longer matches the saved sync baseline. Run "
            "./build-atoms.sh for a full rebuild before syncing."
        )
    atoms = json.loads(OUTPUT_JSON.read_text(encoding="utf-8"))
    if not isinstance(atoms, list) or any(
        not isinstance(atom, dict) or not isinstance(atom.get("page"), str)
        for atom in atoms
    ):
        raise ValueError(
            f"{OUTPUT_JSON.name} is not a valid atom export; run a full rebuild."
        )
    return atoms


def changed_paths(
    base_ref: str | None, manifest: dict
) -> list[dict]:
    """Report changed paths from a supplied base or the local worktree."""
    changes = {}
    if base_ref and set(base_ref) != {"0"}:
        output = git_output("diff", "--name-status", "--no-renames", base_ref, "HEAD", "--")
        for line in output.splitlines():
            status, path = line.split("\t", 1)
            changes[path] = status
    else:
        output = git_output(
            "status", "--porcelain=v1", "--untracked-files=all"
        )
        for line in output.splitlines():
            status = line[:2].strip() or "M"
            path = line[3:]
            changes[path] = "A" if status == "??" else status

    tracked_patterns = manifest["input_scope"]["include"]
    tracked_excludes = manifest["input_scope"]["exclude"]
    control_files = set(manifest["build_control_files"])
    relevant = []
    for path, status in sorted(changes.items()):
        is_control = path in control_files
        is_input = (
            any(path_matches(path, pattern) for pattern in tracked_patterns)
            and not any(path_matches(path, pattern) for pattern in tracked_excludes)
        )
        if is_input or is_control:
            relevant.append(
                {
                    "status": status,
                    "path": path,
                    "scope": "build-control" if is_control else "input",
                }
            )
    return relevant


def load_manifest() -> dict:
    """Load and minimally validate the authoritative build manifest."""
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 1:
        raise ValueError(f"Unsupported manifest schema in {MANIFEST.name}")
    return manifest


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def status_report(
    manifest: dict,
    base_ref: str | None,
    input_files: list[Path],
    html_files: list[Path],
    term_files: list[Path],
    changed: list[dict],
    atoms: list[dict],
    full_rebuild: bool,
    sync_state: dict,
    synchronized_inputs: list[dict],
) -> dict:
    type_counts = {}
    for atom in atoms:
        type_counts[atom["type"]] = type_counts.get(atom["type"], 0) + 1

    html_paths = {
        path.relative_to(REPO_ROOT).as_posix() for path in html_files
    }
    review_scope = manifest["manual_review_scope"]
    changed_inputs = [
        item for item in changed if item["scope"] == "input"
    ]
    changed_controls = [
        item for item in changed if item["scope"] == "build-control"
    ]
    review = [
        item
        for item in changed_inputs
        if item["path"] not in html_paths
        and any(
            path_matches(item["path"], pattern)
            for pattern in review_scope["include"]
        )
        and not any(
            path_matches(item["path"], pattern)
            for pattern in review_scope["exclude"]
        )
    ]
    if base_ref and set(base_ref) != {"0"}:
        trigger = f"git diff from {base_ref} to HEAD"
    elif full_rebuild:
        trigger = "local worktree status"
    else:
        trigger = "content fingerprints since previous build"
    return {
        "status": "SUCCESS",
        "generated_at_utc": datetime.now(timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z"),
        "trigger": trigger,
        "build_mode": "full" if full_rebuild else "sync",
        "full_rebuild": full_rebuild,
        "manifest": MANIFEST.name,
        "discovered_input_files": [
            path.relative_to(REPO_ROOT).as_posix() for path in input_files
        ],
        "discovered_input_count": len(input_files),
        "changed_inputs": changed_inputs,
        "changed_build_controls": changed_controls,
        "synchronized_inputs": synchronized_inputs,
        "manual_review_required": review,
        "sync_state": sync_state,
        "parser_inputs": {
            "structured_html_atoms": [
                path.relative_to(REPO_ROOT).as_posix() for path in html_files
            ],
            "ontology_term_occurrences": [
                path.relative_to(REPO_ROOT).as_posix() for path in term_files
            ],
        },
        "record_counts_by_type": type_counts,
        "total_records": len(atoms),
        "outputs": [
            path.relative_to(REPO_ROOT).as_posix()
            for path in [
                OUTPUT_JSON,
                OUTPUT_CSV,
                OUTPUT_MD,
                STATUS_MD,
                STATUS_JSON,
            ]
        ],
        "notes": [
            "CLAUDE.md is excluded from parser inputs.",
            (
                "TERM records are literal ontology term occurrences, not "
                "evidence or FSD classifications."
            ),
            (
                "New or changed source documents require human atomization "
                "and review; this build does not infer propositions from "
                "arbitrary source files."
            ),
        ],
    }


def render_status_markdown(report: dict) -> str:
    review = report["manual_review_required"]
    generated_files = ", ".join(
        f"`{path}`" for path in report["outputs"]
    )
    lines = [
        "# Atom build status",
        "",
        f"- **Status:** {report['status']}",
        f"- **Generated (UTC):** {report['generated_at_utc']}",
        f"- **Trigger/reference:** {report['trigger']}",
        f"- **Build mode:** "
        f"{'full deterministic rebuild' if report['full_rebuild'] else 'incremental sync'}",
        f"- **Manifest:** `{report['manifest']}`",
        f"- **Discovered inputs:** {len(report['discovered_input_files'])}",
        f"- **Output records:** {report['total_records']}",
        f"- **Generated files:** {generated_files}",
        "",
        "## Record counts by type",
        "",
    ]
    lines.extend(
        f"- `{kind}`: {count}"
        for kind, count in sorted(report["record_counts_by_type"].items())
    )
    if not report["record_counts_by_type"]:
        lines.append("- None")
    lines.extend(["", "## Changed inputs", ""])
    if report["changed_inputs"]:
        lines.extend(
            f"- `{item['status']}` `{item['path']}`"
            for item in report["changed_inputs"]
        )
    else:
        lines.append("- No changed in-scope inputs detected.")
    lines.extend(["", "## Changed build controls", ""])
    if report["changed_build_controls"]:
        lines.extend(
            f"- `{item['status']}` `{item['path']}`"
            for item in report["changed_build_controls"]
        )
    else:
        lines.append("- No build-control changes detected.")
    lines.extend(["", "## Synchronized inputs", ""])
    if report["synchronized_inputs"]:
        lines.extend(
            f"- `{item['status']}` `{item['path']}`"
            for item in report["synchronized_inputs"]
        )
    else:
        lines.append("- No input content changes detected.")
    lines.extend(["", "## Manual atomization/review queue", ""])
    if review:
        lines.extend(f"- `{item['status']}` `{item['path']}`" for item in review)
    else:
        lines.append("- No changed non-index inputs detected.")
    lines.extend(
        [
            "",
            "## Expanded manifest inventory",
            "",
        ]
    )
    lines.extend(
        f"- `{path}`" for path in report["discovered_input_files"]
    )
    lines.extend(
        [
            "",
            "## Processing boundary",
            "",
            (
                "The build extracts authored tagged blocks and FSD panels "
                "from HTML index pages and records literal FSD term "
                "occurrences. It does not semantically atomize arbitrary "
                "source documents. `TERM` occurrences and `FSD_PANEL` "
                "records are not evidence that an FSD class applies. Review "
                "the listed changed inputs and manually update the relevant "
                "analytical layer where needed."
            ),
            "",
            (
                "The full file inventory, parser scope, exclusions, and "
                "invocation instructions are defined in "
                "`atom-build-manifest.json` and `ATOM-BUILD.md`."
            ),
            "",
        ]
    )
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Rebuild atom exports or synchronize only changed inputs, "
            "then write a timestamped status report."
        )
    )
    parser.add_argument(
        "--sync",
        action="store_true",
        help="Update records only for changed inputs using the saved build baseline.",
    )
    parser.add_argument(
        "--base-ref",
        help="Git base revision used to identify changed inputs (for CI builds).",
    )
    args = parser.parse_args()

    manifest = load_manifest()
    input_files = manifest_files(
        manifest["input_scope"]["include"],
        manifest["input_scope"]["exclude"],
    )
    html_config = manifest["parsers"]["structured_html_atoms"]
    html_files = manifest_files(html_config["include"], html_config["exclude"])
    term_config = manifest["parsers"]["ontology_term_occurrences"]
    term_files = manifest_files(term_config["include"], term_config["exclude"])
    changed = changed_paths(args.base_ref, manifest)
    sync_state = make_sync_state(input_files, html_files, term_files)

    if args.sync:
        existing_atoms = load_sync_baseline(sync_state)
        previous_report = json.loads(STATUS_JSON.read_text(encoding="utf-8"))
        previous_state = previous_report["sync_state"]
        synchronized_inputs = changed_input_paths(previous_state, sync_state)
        refresh_paths = {item["path"] for item in synchronized_inputs}
        previous_html = set(previous_state["structured_html_inputs"])
        previous_terms = set(previous_state["ontology_term_inputs"])
        html_paths = {
            path.relative_to(REPO_ROOT).as_posix() for path in html_files
        }
        term_paths = {
            path.relative_to(REPO_ROOT).as_posix() for path in term_files
        }
        refresh_html = (previous_html | html_paths) & refresh_paths
        refresh_terms = (previous_terms | term_paths) & refresh_paths
        refreshed_atoms = []
        for html_path in html_files:
            relative_path = html_path.relative_to(REPO_ROOT).as_posix()
            if relative_path not in refresh_html:
                continue
            results = scrape_file(html_path)
            if results:
                print(f"  {relative_path}: {len(results)} records")
                refreshed_atoms.extend(results)

        concepts = ontology_concepts() if refresh_terms else []
        for path in term_files:
            relative_path = path.relative_to(REPO_ROOT).as_posix()
            if relative_path not in refresh_terms:
                continue
            results = scrape_concepts(path, concepts)
            if results:
                print(f"  {relative_path}: {len(results)} term occurrences")
                refreshed_atoms.extend(results)

        report_changes = {
            item["path"]: item for item in changed + synchronized_inputs
        }
        changed = [report_changes[path] for path in sorted(report_changes)]
        all_atoms = merge_refreshed_atoms(
            existing_atoms,
            refreshed_atoms,
            refresh_paths,
            html_files,
            term_files,
        )
        print(
            f"Synchronized {len(synchronized_inputs)} changed inputs "
            f"({len(refresh_html)} HTML, {len(refresh_terms)} term-search files)."
        )
    else:
        synchronized_inputs = [
            item for item in changed if item["scope"] == "input"
        ]
        all_atoms = []
        for html_path in html_files:
            results = scrape_file(html_path)
            if results:
                print(f"  {html_path.relative_to(REPO_ROOT)}: {len(results)} records")
                all_atoms.extend(results)

        concepts = ontology_concepts()
        for path in term_files:
            results = scrape_concepts(path, concepts)
            if results:
                print(f"  {path.relative_to(REPO_ROOT)}: {len(results)} term occurrences")
                all_atoms.extend(results)

    print(
        f"\nTotal: {len(all_atoms)} records across "
        f"{len(set(atom['page'] for atom in all_atoms))} files"
    )

    write_json(OUTPUT_JSON, all_atoms)
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=CSV_FIELDS, lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(all_atoms)

    # Markdown — grouped by page.
    lines = ["# Atom extract — post-hoc\n"]
    by_page: dict[str, list] = {}
    for atom in all_atoms:
        by_page.setdefault(atom["page"], []).append(atom)

    for page, page_atoms in sorted(by_page.items()):
        lines.append(f"\n## {page}\n")
        for atom in page_atoms:
            concept = atom.get("concept", "")
            label = f" {concept}" if concept else ""
            section = f" — {atom['section']}" if atom["section"] else ""
            lines.append(f"**[{atom['type']}]**{label}{section}")
            lines.append(f"> {atom['body']}")
            if atom["source"]:
                lines.append(f"_source: {atom['source']}_")
            if atom["gap"]:
                lines.append(f"⚠ {atom['gap']}")
            if atom["see_also"]:
                lines.append(f"↗ {atom['see_also']}")
            lines.append("")

    OUTPUT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    sync_state["atom_export_sha256"] = file_sha256(OUTPUT_JSON)
    report = status_report(
        manifest,
        args.base_ref,
        input_files,
        html_files,
        term_files,
        changed,
        all_atoms,
        not args.sync,
        sync_state,
        synchronized_inputs,
    )
    write_json(STATUS_JSON, report)
    STATUS_MD.parent.mkdir(parents=True, exist_ok=True)
    STATUS_MD.write_text(render_status_markdown(report), encoding="utf-8")
    print(
        "\nWrote: atoms.json, atoms.csv, atoms.md, "
        f"{STATUS_MD.relative_to(REPO_ROOT)}, "
        f"{STATUS_JSON.relative_to(REPO_ROOT)}"
    )


if __name__ == "__main__":
    main()
