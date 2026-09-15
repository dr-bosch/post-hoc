"""
scrape-atoms.py
Extracts tagged analytical atoms from post-hoc index.html files and
ontology-governed concept occurrences in root-level Markdown and HTML files.
Output: atoms.json, atoms.csv, atoms.md

Evidentiary status ladder (per CLAUDE.md):
  OBS  — directly verifiable from stated source
  INT  — analytical interpretation; requires argument
  INF  — derived from OBS; requires a logical step
  HYP  — requires additional evidence to establish
  FSD  — OWL class definition from FSD-Ontology-2026.md
  CHR  — dated behavioural event; legal-chronology register
"""

import csv
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

REPO_ROOT = Path(".")
ONTOLOGY = REPO_ROOT / "FSD-Ontology-2026.md"
OUTPUT_JSON = Path("atoms.json")
OUTPUT_CSV = Path("atoms.csv")
OUTPUT_MD = Path("atoms.md")

STATUS_MAP = {
    "OBS": "OBS",
    "INT": "INT",
    "INF": "INF",
    "HYP": "HYP",
}
GENERATED_FILES = {OUTPUT_JSON, OUTPUT_CSV, OUTPUT_MD}


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


def scrape_concepts(path: Path, concepts: list[dict]) -> list[dict]:
    """Extract one FSD concept atom for each ontology term found in a passage."""
    passages = split_passages(document_text(path))
    atoms = []
    for passage in passages:
        lowered = passage.casefold()
        for concept in concepts:
            aliases = (concept["term"], concept["label"])
            if not any(alias.casefold() in lowered for alias in aliases):
                continue
            atoms.append(
                {
                    "type": "FSD",
                    "concept": concept["term"],
                    "page": str(path.relative_to(REPO_ROOT)),
                    "section": "",
                    "body": passage,
                    "source": f"{ONTOLOGY.name} — {concept['label']}",
                    "gap": "",
                    "see_also": "",
                }
            )
    return atoms


def parse_atom(div, page_path: str, section: str) -> dict:
    """Extract a tagged .atom div into a structured record."""
    tag_el = div.find(class_="tag")
    status_raw = clean(tag_el.get_text()) if tag_el else "UNKNOWN"
    # Tag text may be 'OBSERVATION', 'OBS', etc. — normalise.
    status = next(
        (key for key in STATUS_MAP if status_raw.upper().startswith(key)),
        status_raw[:3].upper(),
    )

    # Remove the tag span before extracting body text.
    if tag_el:
        tag_el.decompose()

    src_el = div.find(class_="src")
    gap_el = div.find(class_="gap")
    sa_el = div.find(class_="see-also")

    source = clean(src_el.get_text()) if src_el else ""
    gap = clean(gap_el.get_text()) if gap_el else ""
    see_also = clean(sa_el.get_text()) if sa_el else ""

    # Strip extracted child elements before reading body.
    for element in [src_el, gap_el, sa_el]:
        if element:
            element.decompose()

    body = clean(div.get_text())

    return {
        "type": status,
        "page": page_path,
        "section": section,
        "body": body,
        "source": source,
        "gap": gap,
        "see_also": see_also,
    }


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
        "type": "FSD",
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
                atoms.append(parse_atom(element, page_path, current_section))
            elif "fsd-class" in classes:
                atoms.append(parse_fsd_class(element, page_path, current_section))
            elif "chrono" in classes:
                atoms.append(parse_chrono(element, page_path, current_section))

    return atoms


def main():
    all_atoms = []
    for html_path in sorted(REPO_ROOT.rglob("*/index.html")):
        results = scrape_file(html_path)
        if results:
            print(f"  {html_path}: {len(results)} atoms")
            all_atoms.extend(results)

    concepts = ontology_concepts()
    for path in sorted(REPO_ROOT.iterdir()):
        if (
            path.is_file()
            and path.suffix.lower() in {".md", ".html"}
            and path != ONTOLOGY
            and path.name not in {file.name for file in GENERATED_FILES}
        ):
            results = scrape_concepts(path, concepts)
            if results:
                print(f"  {path}: {len(results)} concept atoms")
                all_atoms.extend(results)

    print(
        f"\nTotal: {len(all_atoms)} atoms across "
        f"{len(set(atom['page'] for atom in all_atoms))} pages"
    )

    # JSON
    OUTPUT_JSON.write_text(
        json.dumps(all_atoms, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    # CSV
    fields = [
        "type",
        "concept",
        "page",
        "section",
        "body",
        "source",
        "gap",
        "see_also",
    ]
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
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

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote: {OUTPUT_JSON}, {OUTPUT_CSV}, {OUTPUT_MD}")


if __name__ == "__main__":
    main()
