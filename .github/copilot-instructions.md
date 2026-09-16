# Copilot Instructions — post-hoc

---

## 0. Mandatory pre-task sequence

Before performing any analysis, extraction, editing, or repository-structural task,
read the following files from the repository root in this order:

1. `CLAUDE.md` — methodological protocol and analytical rules
2. `FSD-Ontology-2026.md` — controlled vocabulary for FSD class labels

Read both files directly from the repository. Do not use training data or prior
knowledge as a substitute for reading the current file content.

**If `FSD-Ontology-2026.md` cannot be read:**

- proceed using evidentiary status labels only (OBS / INT / INF / HYP / CHR);
- append the marker `[FSD: pending — ontology unavailable]` to any atom that
  would otherwise carry an FSD class;
- do not assign, guess, or approximate any `fsd:` class label;
- note at the top of the output that FSD classification is pending and state
  which file could not be read.

Do not perform FSD classification until `FSD-Ontology-2026.md` has been
successfully read in the current task.

---

## 1. Governing protocol

Read and follow `CLAUDE.md` before performing any analytical, corpus, or
repository-structural work. It is the authoritative methodological protocol.

The repository uses the following analytical chain. Do not reverse it.
Do not collapse layers into one another.

```
SOURCE
  ↓
ATOMIC OBSERVATION
  ↓
EVIDENCE STATUS  (OBS / INT / INF / HYP / CHR)
  ↓
OPTIONAL FSD CLASSIFICATION  ← requires FSD-Ontology-2026.md to be loaded
  ↓
INTERPRETATION
  ↓
INFERENCE
  ↓
SYSTEM MODEL
```

---

## 2. Source discipline

Treat documentary source material as evidence. Do not treat it as conclusions.

Do not:

- invent facts, dates, quotations, actors, institutional actions, motives,
  or relationships;
- silently correct or reinterpret source material;
- treat absence of evidence as evidence of absence;
- convert an interpretation or inference into an observation;
- infer motive from institutional outcome;
- infer bad faith, conspiracy, illegality, negligence, or obstruction
  without independent evidence;
- modify source documents merely to improve presentation;
- use an FSD class label as a substitute for an evidentiary proposition;
- reproduce a normative provision as evidence that the provision was applied.

Distinguish these three propositions. They are not equivalent:

- **not present in this document**
- **not found in the available record**
- **demonstrably did not occur**

Preserve uncertainty and conflicting evidence where they exist.

---

## 3. Corpus architecture

```
post-hoc/
├── CLAUDE.md                          ← HOW TO THINK / HOW TO ANALYSE
├── FSD-Ontology-2026.md               ← WHAT THE CONTROLLED VOCABULARY CONTAINS
│
├── corpus/                            ← WHAT THE SOURCES ACTUALLY SAY
│   ├── laws-and-codes/
│   │   ├── MANUAL.html                ← technical manual for this layer
│   │   ├── primary-legislation/
│   │   ├── statutory-instruments/
│   │   ├── eu-regulations/
│   │   ├── eu-directives/
│   │   ├── codes-of-practice/
│   │   └── regulatory-frameworks/
│   └── [other corpus subdirectories]
│
├── synthesis/                         ← WHAT THE ANALYSIS CONCLUDES
│
└── index.html files                   ← HOW THE CORPUS IS NAVIGATED
```

The repository also separates analytical work as follows:

- `semiotics/` — representation, signification, language, absences, oppositions
- `behaviour/` — observable institutional actions and non-actions
- `posiwid/` — system-level analysis inferred from observable behaviour

Do not collapse these layers. Do not allow content to migrate between them
without explicit analytical justification.

---

## 4. Normative source material

`corpus/laws-and-codes/` holds normative source material. Before working in
this layer, read `corpus/laws-and-codes/MANUAL.html`.

### The fundamental distinction

**Normative validity is not evidence of operative effect.**

```
NORMATIVE PROPOSITION
        ↓
INSTITUTIONAL REPRESENTATION
        ↓
OBSERVABLE BEHAVIOUR
        ↓
OPERATIVE EFFECT
```

The presence of a legal rule is not evidence that the rule was applied,
enforced, discharged, or made operative in a particular case.

### Four analytical cases

| Case | Description | Analytical status |
|------|-------------|-------------------|
| Normative validity + operative effect | Provision exists; mechanism was applied | Normal; document the evidence |
| Normative validity + no operative effect | Provision exists; mechanism absent or not applied | Primary FSD analysis object |
| No normative validity + apparent operative effect | Institution claims authority under a non-existent or inapplicable provision | Flag misrepresentation |
| No normative validity + no operative effect | Analytically null | Record only if a party claims otherwise |

### The justice-facing void

The **justice-facing void** is an analytical problem-space, not an ontology
entity. Do not introduce `fsd:JusticeFacing` as a class.

It denotes the gap that may arise between a formally constituted normative
condition and the institutional mechanisms through which that condition becomes
operative for persons subject to or relying upon it.

The existence of such a gap must be established through evidence. Do not infer
it merely from the existence of a legal norm and an adverse outcome.

---

## 5. FSD Ontology

### Availability requirement

Do not apply FSD class labels without first reading `FSD-Ontology-2026.md`
from the repository root (see Section 0).

Do not assign FSD classes from memory or training data. Labels produced from
memory may appear plausible but will be unverified.

### Namespace

The FSD ontology namespace is `https://meinhardt.gov/ontology/fsd/2026#`,
abbreviated as `fsd:`.

Use the short form `fsd:ClassName` in all analytical output, Markdown files,
and HTML. Do not expand to the full URI unless writing Turtle or RDF.

### Legislative status and default evidentiary status

The FSD ontology formalises the Qualifying Submissions (Duty to Determine)
Bill 2026. It is a legislative proposal, not an enacted statute.

Consequence: applying an FSD class to a source document asserts that the
document instantiates a concept the Bill defines. That is a substantive
analytical claim, not a neutral label.

Default evidentiary status for FSD classifications:

- **HYP** — unless the specific factual conditions required by the class
  definition are established from the documentary record.
- **INF** — once the required factual conditions are established from
  identifiable source passages and the inferential step is stated.
- **OBS** — only where the source document itself uses the defined term
  in a way that directly instantiates the class.

### Section 12 of the ontology — do not treat as pre-established evidence

Section 12 of `FSD-Ontology-2026.md` contains a table stating which SWRL
rules are "Established" against the existing record.

These are the ontology authors' claims about the record, made at the date
of the ontology (July 24, 2026). They are not independently verified
evidence. Treat them as:

- a pointer to which rules are most likely to be instantiated;
- a starting hypothesis for corpus verification;
- not as OBS or INF without independent documentary grounding.

Verify each claimed instantiation against the documentary record before
elevating its status.

### SWRL threshold conditions

Several FSD classes have precise triggering conditions defined in §7:

| Class | Trigger |
|-------|---------|
| `fsd:LoopCondition` (Rule 2) | declination count ≥ 3, from ≥ 3 separate bodies |
| `fsd:LoopCondition` (Rule 3) | non-determination period ≥ 24 months |
| `fsd:NonDetermination` (Rule 1) | determination deadline passed; no determination issued |
| `fsd:ResidualObligation` (Rule 4) | loop condition established; Ombudsman identified |
| `fsd:OnticCollapse` (Rule 6) | no body with full competence; no assembly mechanism |

These thresholds must be met on the facts established from the documentary
record. Do not classify by pattern-matching alone.

### Class definitions: OWL and SKOS

Each FSD class has an OWL `rdfs:comment` definition (§4 of the ontology).
Several also have a SKOS definition in §10. Where both exist, read both:
the SKOS definition is often more accessible and may clarify scope. Note
any material difference between them.

### Subordination to evidence

FSD classifications are optional and downstream. The evidentiary status
(OBS / INT / INF / HYP / CHR) is always primary.

An atom may carry both: for example, `OBS` about a `fsd:Submission`, or
`INF` supporting `fsd:NonDetermination`. Do not replace the status with
the class.

### Usage rules

When applying an FSD class:

1. confirm `FSD-Ontology-2026.md` has been read in the current task;
2. cite the relevant `rdfs:comment` definition from §4 of `FSD-Ontology-2026.md`;
3. note the SKOS definition from §10 if one exists;
4. identify the source passage that grounds the classification;
5. state the evidentiary status of that grounding;
6. where a SWRL rule applies, identify which conditions are met and from
   which source documents;
7. retain competing classifications where more than one is plausible;
8. do not treat the label alone as proof of the phenomenon.

---

## 6. Atomic extraction

### Definition

An **atomic item** is the smallest independently traceable proposition, event,
signifier, normative proposition, documentary absence, or other evidentiary
unit that can be linked to a specific source passage without requiring an
unstated inferential bridge.

**Atomic extraction precedes interpretation.**

### Evidence status labels

Use the short code consistently. The full label is given for reference.

| Code | Full label | Required treatment |
|------|-----------|-------------------|
| `OBS` | Observation | Quote or identify the exact source passage |
| `INT` | Interpretation | State the interpretive operation being performed |
| `INF` | Inference | State the premises and the inferential step |
| `HYP` | Hypothesis | Identify what evidence is missing |
| `CHR` | Chronological event | Preserve date, actor, action, consequence, source |

### Extraction rules

When extracting atoms from any source document:

1. preserve the exact source passage or a short, traceable quotation;
2. identify the source file and, where available, its section or location;
3. assign an evidentiary status from the table above;
4. record any FSD class separately — only after reading `FSD-Ontology-2026.md`;
5. distinguish a term's occurrence from an assertion that an FSD class applies;
6. record ambiguity where a word is used in an ordinary or different technical sense;
7. retain competing classifications where the passage supports more than one;
8. treat repeated occurrences as separate atoms only when source passage or
   context differs;
9. flag false positives and ambiguous matches for review;
10. never infer recurrence, institutional behaviour, or system purpose from
    term frequency alone;
11. exclude generated atom outputs from subsequent source extraction;
12. exclude `FSD-Ontology-2026.md` from evidence counts unless analysing
    the ontology itself;
13. do not treat §12 of `FSD-Ontology-2026.md` as a source of pre-established
    evidence — its instantiation claims require independent documentary
    verification before elevation to OBS or INF status.

### HTML atom format

Atoms appearing in `index.html` files use this format:

```html
<div class="atom">
  <p><span class="tag OBS">OBS</span> [proposition text]</p>
  <p><span class="tag INT">INT</span> [interpretation text]</p>
</div>
```

The CSS classes `OBS`, `INT`, `INF`, `HYP` correspond to the tag colours
defined in the parent `index.html` stylesheet. Do not introduce new tag classes.

When an FSD class applies, append it in monospace after the proposition:

```html
<p><span class="tag INF">INF</span> [proposition] <code>fsd:NonDetermination</code></p>
```

When FSD classification is pending, append the marker instead:

```html
<p><span class="tag HYP">HYP</span> [proposition] <code>[FSD: pending — ontology unavailable]</code></p>
```

---

## 7. Global corpus operations

Use this sequence when performing large-scale extraction, scraping, or editing
across the repository.

### Pre-flight

1. Read `CLAUDE.md` and `FSD-Ontology-2026.md` (Section 0).
2. Inspect the full repository tree before touching any file.
3. Read `corpus/laws-and-codes/MANUAL.html` if the task involves that layer.
4. Identify the scope: which directories, which file types, which operation.
5. State the scope explicitly before beginning.

### Processing order

Process files in this order to avoid derivative files being updated before
their sources are complete:

1. Primary source documents (PDF, MD source files in `corpus/`);
2. Analytical working files (semiotics, behaviour, posiwid layers);
3. Synthesis files;
4. `index.html` files (last — they are derivatives of everything above).

Never update an `index.html` before the source material it will reference
has been processed.

### Deduplication

Before creating a new atom, check whether the same source passage has
already been extracted in the current run. Do not create duplicate atoms
from the same passage in the same document.

Where the same passage appears in multiple documents (e.g. a provision
quoted in both a code of practice and an index entry), record the atom
once against the primary source and cross-reference from the derivative.

### Batch reporting

At the end of a global operation, report:

- files read (sources consulted);
- files changed (and what changed);
- files created;
- files deliberately left unchanged and why;
- atoms extracted (count by status code);
- FSD classes applied (count, or "none — ontology unavailable");
- unresolved ambiguities;
- evidence gaps identified;
- links verified or flagged for verification;
- any `[FSD: pending — ontology unavailable]` markers left in output.

---

## 8. HTML indexes and navigation pages

`index.html` files are derivative navigational and curatorial artefacts.
They are not primary evidence.

When updating them:

- preserve the existing visual language (Georgia serif, monospace tags,
  `.atom`, `.fsd-class`, `.gap`, `.src` classes);
- preserve all existing well-grounded material;
- add only information traceable to underlying source material;
- do not populate empty directories with invented content;
- do not silently create new analytical conclusions;
- keep analytical claims proportionate to the available evidence;
- a HYP reproduced on an index page remains a HYP — reproduction does
  not elevate evidentiary status.

**Synthesis drift warning:** automated extraction followed by reproduction
in HTML creates a risk of hypotheses appearing as findings. Check this
actively. If a proposition appears on an index page without a traceable
source passage, flag it for review rather than leaving it in place.

---

## 9. URL and link conventions

All internal links in HTML files use **absolute URLs**. Do not use relative
paths.

| Destination type | Base URL |
|-----------------|----------|
| HTML, PDF, SVG (browser-viewable) | `https://dr-bosch.github.io/post-hoc/` |
| MD files and non-browser-viewable files | `https://github.com/dr-bosch/post-hoc/blob/main/` |

Navigation breadcrumbs follow the full path:

```
post-hoc / corpus / laws-and-codes / [subdirectory]
```

All three crumbs must be present and linked. Do not skip the `corpus/` level.

When adding or updating links:

1. construct the full absolute URL;
2. verify the target path exists in the repository tree;
3. do not fabricate URLs for files that do not yet exist — use a
   placeholder comment instead.

---

## 10. Change discipline

Before making any repository change:

1. inspect the existing tree;
2. read the relevant files;
3. understand the current architecture;
4. state what you intend to change and why;
5. make the smallest coherent change that achieves the goal;
6. verify links and paths after the change.

Do not commit or push changes unless explicitly instructed.

Do not modify source documents merely to facilitate analysis.

Git commits must describe substantive changes clearly and accurately.
Do not use commits to conceal analytical revisions.

When completing any task, report using the batch reporting format
in Section 7, scaled to the scope of the task.
