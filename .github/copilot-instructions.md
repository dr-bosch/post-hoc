# Copilot Instructions — post-hoc

## Governing protocol

Read and follow `CLAUDE.md` before performing analytical, corpus, or repository-structural work.

`CLAUDE.md` is the authoritative methodological protocol for this repository.

The repository uses the following analytical chain:

SOURCE → OBSERVATION → INTERPRETATION → INFERENCE → SYSTEM MODEL

Maintain these distinctions at all times.

## Source discipline

Treat documentary source material as evidence, not as conclusions.

Do not:

* invent facts, dates, quotations, actors, institutional actions, motives, or relationships;
* silently correct or reinterpret source material;
* treat absence of evidence as evidence of absence;
* convert an interpretation or inference into an observation;
* infer motive from institutional outcome;
* infer bad faith, conspiracy, illegality, negligence, or obstruction without evidence;
* modify source documents merely to improve presentation.

Preserve uncertainty and conflicting evidence where they exist.

## Corpus architecture

The repository separates:

1. `corpus/` — documentary and normative source material;
2. `semiotics/` — analysis of representation, signification, language, absences, and oppositions;
3. `behaviour/` — observable institutional actions and non-actions;
4. `posiwid/` — system-level analysis inferred from observable behaviour;
5. `synthesis/` — higher-level analytical integration.

Do not collapse these layers.

### Laws and codes

`corpus/laws-and-codes/` contains normative source material.

Distinguish:

* normative validity;
* institutional representation of the norm;
* observable institutional behaviour;
* operative effect.

A legal or regulatory text does not by itself establish that the corresponding institutional act occurred.

Do not introduce `fsd:JusticeFacing` as an ontology class unless explicitly instructed.

The phrase **justice-facing void** may be used as an analytical description of the problem-space at the interface between normative architecture and operative behaviour.

## Atomic extraction

When processing source files, prefer discrete, traceable propositions over broad summaries.

Where possible, preserve provenance:

* source file;
* section or heading;
* date;
* evidence status;
* destination/category.

Use the repository's evidence labels:

* `OBSERVATION`
* `INTERPRETATION`
* `INFERENCE`
* `HYPOTHESIS`

## HTML indexes

`index.html` files are curated gateways into the corpus and analytical layers.

When updating them:

* preserve the existing minimalist visual language;
* preserve useful existing material;
* add only source-grounded information;
* maintain working relative links;
* do not duplicate the same information indiscriminately across directories;
* do not populate empty directories with invented content;
* keep analytical claims proportionate to the available evidence.

## Change discipline

Before making broad repository changes:

1. inspect the existing tree;
2. inspect relevant files;
3. understand the current architecture;
4. make the smallest coherent change;
5. verify links and paths afterwards.

Do not commit or push changes unless explicitly instructed.

When completing a repository task, report:

* files changed;
* files created;
* files deliberately left unchanged;
* unresolved ambiguities;
* evidence gaps;
* verification performed.
