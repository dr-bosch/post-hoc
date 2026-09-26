# post-hoc
## Post Hoc Report/Audit

**A structural method for inferring institutional purpose from documented institutional behaviour.**

*post hoc*, Latin: "after the fact." This project does not argue about intentions, motives, or what an institution says it exists to do. It works backward from what a system **produced** — the corpus, the record, the trail — to what that system's behaviour, considered as a whole, functioned to accomplish.

### Landing Pages
- [dr-bosch.github.io/](https://dr-bosch.github.io/)
  - [intro](https://dr-bosch.github.io/intro)
  - [post-hoc/report](https://dr-bosch.github.io/post-hoc/report)
  - [post-hoc/feasible-region](https://dr-bosch.github.io/post-hoc/feasible-region)  
  - [post-hoc/fsd-ontology](https://dr-bosch.github.io/post-hoc/fsd-ontology)  

### PDF Links
- [Operations Research Corpus - Competent Authority Determination](http://dr-bosch.github.io/post-hoc/ANNEX-Operations-Research-Corpus-Competent-Authority-Determination.pdf)
- [Interregnum Nullificans](http://dr-bosch.github.io/post-hoc/Interregnum-Nullificans.pdf)
- [Political Risk Report 2026 (Marsh Global)](http://dr-bosch.github.io/post-hoc/Political-Risk-Report-2026-MAR-GLOBAL.pdf)

### SVG Links
- [Constitutional Map - Article 40.3](http://dr-bosch.github.io/post-hoc/Constitutional-Map_Article-40-3_revised.svg)
- [Interregnum Nullificans - constitutional mapping](http://dr-bosch.github.io/post-hoc/Interregnum-Nullificans-constitutional-mapping.svg)

### PNG Links
- [FSD Ontology (A2 poster)](http://dr-bosch.github.io/post-hoc/fsd-ontology-poster-a2.png)
- [FSD Ontology (A3 poster, front)](http://dr-bosch.github.io/post-hoc/fsd-ontology-poster-a3-front.png)
- [FSD Ontology (A3 poster, back)](http://dr-bosch.github.io/post-hoc/fsd-ontology-poster-a3-back.png)


---

## The Method

```
                 CORPUS
                   │
       ┌───────────┴───────────┐
       │                       │
 documentary               normative
 evidence                  framework
       │                       │
       └───────────┬───────────┘
                   ↓
              SEMIOTICS
                   │
       How reality is represented
                   ↓
              BEHAVIOUR
                   │
       What the system actually does
                   ↓
               POSIWID
                   │
       What function behaviour
          appears to produce
                   ↓
              SYNTHESIS
```

Five stages, each with its own working directory and its own `index.html`. Each stage constrains the one after it: semiotics is read only from what the corpus actually contains; behaviour is read only from what can be documented, not what is claimed; POSIWID inference is drawn only from behaviour, never from stated intent; synthesis draws only on what survives all three prior stages.

---

## Semiotic Analytical Layer

### [`/corpus`](https://dr-bosch.github.io/post-hoc/corpus/index.html) — the documentary base

The evidentiary and normative material the rest of the project is built on top of. Nothing downstream is permitted to introduce a fact that doesn't originate here.

- [`statements`](https://dr-bosch.github.io/post-hoc/corpus/statements/index.html) — first-person and institutional statements of position
- [`correspondence`](https://dr-bosch.github.io/post-hoc/corpus/correspondence/index.html) — letters, emails, and formal exchanges
- [`decisions`](https://dr-bosch.github.io/post-hoc/corpus/decisions/index.html) — rulings, determinations, and formal dispositions
- [`institutional-records`](https://dr-bosch.github.io/post-hoc/corpus/institutional-records/index.html) — minutes, logs, registers, and internal records
- [`laws-and-codes`](https://dr-bosch.github.io/post-hoc/corpus/laws-and-codes/index.html) — the normative framework the behaviour is measured against
  - [`primary-legislation`](https://dr-bosch.github.io/post-hoc/corpus/laws-and-codes/primary-legislation/index.html)
  - [`statutory-instruments`](https://dr-bosch.github.io/post-hoc/corpus/laws-and-codes/statutory-instruments/index.html)
  - [`eu-regulations`](https://dr-bosch.github.io/post-hoc/corpus/laws-and-codes/eu-regulations/index.html)
  - [`eu-directives`](https://dr-bosch.github.io/post-hoc/corpus/laws-and-codes/eu-directives/index.html)
  - [`codes-of-practice`](https://dr-bosch.github.io/post-hoc/corpus/laws-and-codes/codes-of-practice/index.html)

### [`/semiotics`](https://dr-bosch.github.io/post-hoc/semiotics/index.html) — how reality is represented

The layer of representation: what the corpus says, implies, and omits, independent of whether what it says is true.

- [`signifiers`](https://dr-bosch.github.io/post-hoc/semiotics/signifiers/index.html) — recurring terms, labels, and framings
- [`narratives`](https://dr-bosch.github.io/post-hoc/semiotics/narratives/index.html) — the stories the corpus tells about itself
- [`metaphors`](https://dr-bosch.github.io/post-hoc/semiotics/metaphors/index.html) — figurative structures carrying argumentative weight
- [`absences`](https://dr-bosch.github.io/post-hoc/semiotics/absences/index.html) — what is conspicuously not said
- [`oppositions`](https://dr-bosch.github.io/post-hoc/semiotics/oppositions/index.html) — binary framings the corpus relies on

### [`/behaviour`](https://dr-bosch.github.io/post-hoc/behaviour/index.html) — what the system actually does

The observable record, stripped of framing: actions and non-actions as documented events, not as characterised by any party.

- [`actions`](https://dr-bosch.github.io/post-hoc/behaviour/actions/index.html)
- [`non-actions`](https://dr-bosch.github.io/post-hoc/behaviour/non-actions/index.html)
- [`delays`](https://dr-bosch.github.io/post-hoc/behaviour/delays/index.html)
- [`referrals`](https://dr-bosch.github.io/post-hoc/behaviour/referrals/index.html)
- [`closures`](https://dr-bosch.github.io/post-hoc/behaviour/closures/index.html)

### [`/posiwid`](https://dr-bosch.github.io/post-hoc/posiwid/index.html) — what function behaviour appears to produce

*The Purpose Of a System Is What It Does.* This stage draws no conclusions about intent. It asks only: given the documented behaviour, and only the documented behaviour, what function does the system appear, structurally, to be performing?

- [`system-observations`](https://dr-bosch.github.io/post-hoc/posiwid/system-observations/index.html)
- [`purpose-inferred-from-behaviour`](https://dr-bosch.github.io/post-hoc/posiwid/purpose-inferred-from-behaviour/index.html)

### [`/synthesis`](https://dr-bosch.github.io/post-hoc/synthesis/index.html) — where the stages are drawn together

- [`system-analysis.md`](https://github.com/dr-bosch/post-hoc/blob/main/synthesis/system-analysis.md)

---

## Epistemic Discipline

Every claim in this project is held to one of five categories, and the category travels with the claim:

| Category | What it means |
|---|---|
| **Observation** | Directly present in a corpus document |
| **Interpretation** | A reading of what an observation represents |
| **Inference** | A conclusion drawn from a pattern across observations |
| **Hypothesis** | A proposed explanation not yet corroborated |
| **Evidence gap** | A point where the corpus is silent and no claim is made |

Nothing here is presented as an established institutional fact until it has been corroborated against a primary or independently verifiable source — dated correspondence, an official decision, committee minutes, legislation, regulation, or a court or Ombudsman record. Where the underlying record has not yet been consulted, that is stated rather than assumed. Overlap in wording or subject matter across corpus documents is not treated as independent corroboration of a claim.

This is preparatory, provisional working material. No system-level conclusion is adopted before the corpus, semiotics, and behaviour stages have each been completed and cross-checked.

---

## Core Terminology

structural inference • documentary evidence • normative framework • semiotic layer • signifier • narrative • absence • opposition • observed behaviour • non-action • procedural delay • referral • closure • POSIWID • purpose-from-behaviour • system observation • epistemic status • corroboration • provenance • evidence gap • synthesis

---

## Project Files

- [`CLAUDE.md`](./CLAUDE.md) — working notes and project instructions
