# laws-and-codes: Technical Manual

`post-hoc` / `corpus` / `laws-and-codes` / MANUAL
**version 0.1 · September 2026 · post-hoc corpus · working document**

This manual describes the structure, methodology, and working procedures of the `laws-and-codes/` corpus layer within the post-hoc analytical system. It is addressed to analysts who are adding documents, extracting atomic propositions, and applying the FSD ontology to normative source material. It is not an introduction to the FSD ontology itself; it assumes familiarity with the ontology's core concepts and focuses on how those concepts are applied to legal and regulatory texts.

## Contents

1. [Purpose and scope of this layer](#1-purpose-and-scope-of-this-layer)
2. [Directory structure and document placement](#2-directory-structure-and-document-placement)
3. [Epistemic framework: the four atom classes](#3-epistemic-framework-the-four-atom-classes)
4. [The normative–operative distinction](#4-the-normativeoperative-distinction)
5. [Workflow: adding a document and extracting atoms](#5-workflow-adding-a-document-and-extracting-atoms)
6. [Atom extraction from normative texts](#6-atom-extraction-from-normative-texts-detailed-guidance)
7. [Worked example: Code of Conduct for Members of Dáil Éireann](#7-worked-example-code-of-conduct-for-members-of-dáil-éireann-non-officeholders)
8. [Source registry](#8-source-registry)
9. [Conventions and constraints](#9-conventions-and-constraints)

---

## 1. Purpose and scope of this layer

The `laws-and-codes/` layer holds normative source material: legislation, regulations, codes, and related instruments. Its function is to constitute the normative reference layer — the set of prescriptions, authorisations, constraints, and definitions — against which institutional representations and observable behaviour are subsequently compared.

The layer does not hold analysis. It holds sources, and the analytical apparatus applied to those sources: provision-by-provision breakdowns, FSD atomic propositions, enforcement architecture assessments, and cross-references to other layers of the corpus. Analysis is embedded in the index pages associated with each document, not in the documents themselves.

The central analytical question this layer addresses is not "what does the law say?" but "what operative condition does the law establish, and can that condition be shown to have obtained in the circumstances under examination?" The distinction between normative validity and operative effect is the primary object of attention throughout.

## 2. Directory structure and document placement

The layer is divided into six subdirectories. Each subdirectory holds a class of normative instrument and an index page describing the analytical method applied to that class.

```
laws-and-codes/
├── MANUAL.html                    ← this document
├── index.html                     ← directory overview and methodology statement
├── primary-legislation/           ← Acts and primary legislative texts
├── statutory-instruments/         ← regulations and orders under delegated authority
├── eu-regulations/                ← directly applicable EU regulations
├── eu-directives/                 ← EU directives requiring transposition
├── codes-of-practice/             ← formal codes, guidance, procedural standards
└── regulatory-frameworks/         ← composite multi-instrument frameworks
```

### Document placement rules

Place each document in the directory matching its primary instrument type. Where a document spans types — for example, a statutory instrument that implements an EU directive and is accompanied by a non-statutory code of practice — place the primary instrument in its correct directory and create cross-references in the other relevant directories.

Composite frameworks (e.g. the ethics-in-public-office regime, which comprises primary legislation, a code of conduct, and institutional machinery) are assembled in `regulatory-frameworks/` with cross-references to the constituent instruments in their primary directories.

### Naming convention

Files follow the Oireachtas `data.oireachtas.ie` naming convention where documents originate from that repository:

```
YYYY-MM-DD_descriptive-title_en.pdf
```

For documents from other sources, use:

```
YYYY-MM-DD_source-abbreviation_descriptive-title_en.pdf
```

Markdown working copies (for annotation and atom extraction) use the same base name with a `.md` extension.

## 3. Epistemic framework: the four atom classes

All propositions in the corpus are assigned one of four epistemic classes. The class is not a judgment about the importance of the proposition; it is a claim about the epistemic status of the proposition — what kind of support it has and what would be required to challenge it.

### `OBS` Observation

A proposition directly established by the source text or the documentary record, without requiring interpretation beyond the ordinary meaning of the words. An OBS atom from a normative text records what the text says. It is falsifiable by pointing to the text.

> **OBS** — Article 6 of the Code of Conduct for Members of Dáil Éireann (non-officeholders) provides that Members "may not solicit, accept or receive any financial benefit or profit in exchange for promoting, or voting on, a Bill, a motion for a resolution or order or any question put to the Dáil or to any of its committees."

### `INT` Interpretation

A proposition that follows from careful reading of the source text but requires interpretive judgment — identifying the implications of a drafting choice, the scope of a defined term, the relationship between two provisions, or the consequence of an ambiguity. An INT atom is contestable on interpretive grounds; a different reading of the same text could reach a different conclusion.

> **INT** — The definition of conflict of interest at article 5(i) of the Code requires three cumulative mental elements — knowledge, impropriety, and dishonesty. Negligent or reckless conduct does not satisfy the definition on its face. The threshold is materially higher than a strict-liability or negligence standard.

### `INF` Inference

A proposition that follows logically from one or more OBS or INT atoms, or from the combination of a normative proposition and an established factual premise. An INF atom is the output of reasoning across sources; it is contestable by challenging either the premises or the inferential step.

> **INF** — Because Article 6 of the Code is an absolute prohibition without mental element qualification, and Article 5(i)'s high mental-element definition applies only to the conflict of interest provisions, conduct involving receipt of financial benefit for voting does not require proof of knowledge, impropriety, or dishonesty to satisfy Article 6. The two provisions operate on different evidential bases.

### `HYP` Hypothesis

A proposition that is analytically plausible given the normative architecture and the available evidence, but whose conditions have not yet been established against the documentary record in the specific circumstances under examination. A HYP atom is a candidate claim awaiting evidential grounding; it should be elevated to INF or OBS only when supporting evidence is identified and assessed.

> **HYP** — Where a Member invokes the conscientious objection qualification at article 3(i) of the Code, there is no institutional mechanism capable of adjudicating the validity of that invocation. If the circumstances of a specific case involve such an invocation, the absence of an adjudicatory body may constitute an operative-condition failure with respect to that provision. This is a hypothesis; its conditions require factual grounding.

### Discipline rules for atom classification

- Do not elevate a HYP to INF without identifying the specific documentary evidence that grounds it.
- Do not present an INT as an OBS: interpretation is not observation, even when the interpretation seems obvious.
- Do not chain more than three inferential steps in a single INF atom without breaking the chain into intermediate atoms.
- A finding of illegality, bad faith, negligence, or intentional obstruction is never an OBS or INT from a normative text alone. It is at best a HYP, and requires its own evidentiary pathway.

## 4. The normative–operative distinction

The foundational analytical distinction in this layer is between **normative validity** and **operative effect**. It is stated in the laws-and-codes index and repeated here because it governs every atom extraction exercise.

A normative text is *valid* if it was lawfully made by a competent authority and has not been repealed. A normative provision has *operative effect* in a specific situation if the institutional mechanism through which the provision would be given effect was present, functioning, and applied to that situation.

These are independent conditions. Both can be present; neither can be present; or one can be present without the other. The analytically significant cases are:

- **Normative validity + operative effect:** the provision exists and there is documentary evidence that the mechanism through which it operates was applied. This is the normal case and requires no special analytical treatment.
- **Normative validity + no operative effect:** the provision exists but the mechanism through which it would be applied is absent, inoperative, or was not applied in the specific situation. This is the primary object of FSD analysis. It is not automatically evidence of illegality or bad faith; it is a structural observation requiring further characterisation.
- **No normative validity + apparent operative effect:** an institution purports to act under a provision that does not exist, has been repealed, or does not apply in the circumstances. Relevant where institutions misrepresent their legal authority.
- **No normative validity + no operative effect:** the provision does not exist and no action was taken. Analytically null; this case arises only when a party claims that action was taken under a non-existent provision.

### Applying the distinction in atom extraction

When extracting atoms from a normative text, each provision generates at minimum two atoms: one recording what the provision says (OBS), and one recording whether the operative condition for the provision's application can be identified from the documentary record (which may be OBS, INT, or HYP depending on what is known). The enforcement architecture of the provision — the institutional mechanism through which it would be given effect — is always an explicit analytical object.

## 5. Workflow: adding a document and extracting atoms

The following sequence applies to each new document added to the layer.

**Step 1 — Identify and verify the source.**
Confirm the authoritative online source — the Oireachtas data repository, the Irish Statute Book, EUR-Lex, or another primary publisher. Record the URL and the date of retrieval. Note any version or amendment issues: is this the text as enacted, as amended, or as operative at a specific date?

**Step 2 — Place the document in the correct subdirectory.**
Apply the naming convention. Create a markdown working copy from the PDF if annotation is needed.

**Step 3 — Identify the instrument's analytical categories.**
Before reading for atoms, identify which of the following the instrument establishes: competence, duty, discretion, procedure, remedy, exception. Record these in the index entry. They determine which FSD concepts are candidates for application.

**Step 4 — Read provision by provision.**
For each provision or sub-provision, extract the primary OBS atom (what does the text say?), the primary INT atom (what does careful reading establish?), and any INF or HYP atoms that follow. Record the enforcement architecture of each provision as a separate analytical block.

**Step 5 — Identify cross-cutting structural atoms.**
After the provision-by-provision analysis, step back and ask: what does the instrument establish as a whole? Are there internal tensions between provisions? Does the instrument depend on external mechanisms that are not constituted within it? Does it generate any evidence-production voids — provisions whose observance would produce no documentary residue?

**Step 6 — Apply FSD classifications tentatively.**
Identify which FSD concepts the instrument's structure makes candidates for application — competence vacancy, duty displacement, procedural displacement, transposition gap, structural failure, normative collapse. Record these as HYP atoms with explicit conditions. Do not apply FSD concepts as findings; they are analytical classifications awaiting evidential grounding.

**Step 7 — Update the index page.**
Add the document entry to the relevant subdirectory index. Include: doc-meta (title, date, authority, scope, source URLs), doc-abstract, provision table, enforcement architecture assessment, analytical classifications atom block, and FSD class panel.

**Step 8 — Register cross-references.**
Where the document intersects with documents in other subdirectories — for example, a code of practice that accompanies an Act, or a statutory instrument made under primary legislation already in the layer — add cross-reference links in both directions.

> ⚠️ **Evidence discipline throughout:** at no step in this workflow does the existence of a normative provision establish that the provision was observed, applied, or given effect. Claims about institutional behaviour require corroborating documentary evidence from the administrative record. This constraint applies even when the normative provision is clear, unambiguous, and apparently mandatory.

## 6. Atom extraction from normative texts: detailed guidance

### What a normative text can and cannot yield

A normative text yields OBS and INT atoms directly. It yields INF atoms when combined with other established propositions. It yields HYP atoms when the structure of the text reveals a gap, dependency, or condition that has not yet been grounded in the documentary record.

A normative text cannot by itself yield atoms about what institutions actually did. The text prescribes; the documentary record establishes what occurred. The connection between the two is always an inferential or hypothetical step, not an observation.

### Provision types and their characteristic atoms

**Absolute prohibitions**
Generate a clear OBS (the prohibition exists), an INT (there is no mental element / no exception / scope of the prohibition), and often an INF (overlap or non-overlap with adjacent statutory or criminal provisions). The enforcement architecture question is whether any body is competent to determine a breach and what the consequence of a finding would be.

**Qualified duties ("must," "shall," "are required to")**
Generate an OBS (the duty exists), an INT (the standard — best efforts, strict, results-based — and whether qualifications narrow the scope), and a HYP (whether the duty was discharged in specific circumstances). The word "conscientiously" elevates the standard; "as soon as practicable" introduces a temporal qualification whose meaning requires contextual determination.

**Definitional provisions**
Generate an OBS (the definition), multiple INTs (threshold analysis — is the definition narrow or broad? what conduct does and does not satisfy it?), and INFs (consequences for adjacent provisions that use the defined term). High mental-element thresholds in definitions are analytically significant because they limit the reach of the provision at the classification stage, not only at the enforcement stage.

**Exceptions and exclusions**
Generate an OBS (the exception exists), an INT (the scope — what does the exception cover and what does it exclude?), and often a HYP (where the exception is undefined, its scope is determined by subsequent interpretation, generating an analytical indeterminacy that cannot be resolved from the text alone). Undefined exceptions are evidence-production voids: compliance cannot be assessed against an undetermined standard.

**Procedural requirements**
Generate an OBS (the requirement), an INT (whether it is mandatory or directory — what is the consequence of non-compliance?), and a HYP or INF (whether non-compliance produces nullity, irregularity, or no legal consequence). Procedural provisions are among the most tractable for documentary analysis: a specified form, deadline, or notification requirement either appears in the record or it does not.

**Institutional designations**
Generate an OBS (a body is designated to perform a function), an INT (the scope and limits of the designation), and a HYP (whether the body was constituted, operative, and applied its designated function in the circumstances). The absence of an institutional designation — a duty without a designated enforcer — is itself an OBS that generates a HYP about enforcement architecture failure.

### Evidence-production voids

Some provisions are structured so that compliance would produce no documentary residue. A prohibition on receiving gifts, unaccompanied by a disclosure requirement, is an example: a Member who receives a prohibited gift leaves no trace in any required record. These provisions are analytically significant because non-compliance is only discoverable through external means. Identify them explicitly and flag them as evidence-production voids in the atom set.

## 7. Worked example: Code of Conduct for Members of Dáil Éireann (non-officeholders)

This section summarises the atom set derived from the Code of Conduct in the form in which it would be held for cross-referencing against the Acts. The full provision-by-provision analysis, enforcement architecture assessment, and FSD classifications are in the codes-of-practice index entry. This summary presents the atom set in canonical form.

**Source:** [data.oireachtas.ie — 2012-05-30 Code of Conduct (non-officeholders)](https://data.oireachtas.ie/ie/oireachtas/committee/dail/31/committee_on_members_interests_dail_eireann/termsOfReference/2012/2012-05-30_code-of-conduct-for-members-of-dail-eireann-non-officeholders_en.pdf) · [Oireachtas committee documents listing](https://www.oireachtas.ie/en/committees/32/members-interests-dail/documents/)

### Structural atoms (document-level)

- **OBS** — The Code was adopted by Members of Dáil Éireann under Article 15.10 of the Constitution and circulated in December 2011 as Appendix 2 of the Guidelines for Members of Dáil Éireann Who Are Not Office Holders. It was formally published on 30 May 2012 by the Committee on Members' Interests of Dáil Éireann.
- **OBS** — The Code applies to Members of Dáil Éireann other than office holders. Office holders are a separately governed class; their conduct is subject to different instruments including SIPO-administered codes.
- **INT** — The Code designates no enforcement body. The preamble frames electoral accountability as the primary mechanism and explicitly limits the House's jurisdiction over Members' conduct to breaches of obligations placed on Members "by law, by Standing Orders or by Codes of Conduct established by the House." The enforcement architecture is entirely externalised.
- **INT** — The Code contains no graduated response mechanism and specifies no consequence for breach beyond the general accountability structures of the House and the electorate.
- **HYP** — The Code's operative architecture — electoral accountability, parliamentary scrutiny, media exposure — is contingent on conditions (public knowledge of conduct, proximity of elections, continued membership of the House) that may not obtain in specific circumstances. Where those conditions are absent, the Code's obligations exist without an operative enforcement vehicle. This is a candidate structural finding for FSD analysis, requiring factual grounding in specific circumstances.

### Provision-level atom set (condensed)

**Art. 1**
- **OBS** — Members must in good faith strive to maintain public trust and exercise influence to advance the public interest. Best-efforts standard; not results-based.
- **INT** — Non-achievement of the public interest is not a breach; absence of good faith or effort is required. Internal state is a necessary element, making standalone breach findings under Art. 1 analytically difficult without corroborating evidence.

**Art. 2**
- **OBS** — Members must comply with the provisions and spirit of the Code and must not bring the integrity of their office or the Dáil into serious disrepute.
- **INT** — "Serious disrepute" is a threshold qualifier. Minor or technical departures from the Code's terms do not satisfy Art. 2 on its face. The threshold has no authoritative interpreter within the Code.
- **INF** — Because no body is designated to determine what constitutes "serious disrepute," the threshold functions as a rhetorical constraint rather than a justiciable one in the absence of external enforcement machinery.

**Art. 3(i)**
- **OBS** — Members must behave consistently with their role as public representative and legislator, save where there is a "legitimate and sustainable conscientious objection."
- **INT** — "Legitimate" and "sustainable" are not synonyms. The former concerns whether the objection qualifies; the latter concerns whether it can be maintained under scrutiny. No procedure for raising or adjudicating either limb is provided.
- **HYP** — Art. 3(i) contains an evidence-production void: a Member may invoke the conscientious objection exception without any institutional mechanism being available to test its validity or reject it. The provision cannot be enforced or rebutted through the Code's own machinery.

**Art. 3(ii)**
- **OBS** — Members must interact with public administration and law enforcement consistently with their role as public representative and legislator.
- **INT** — The standard is role-defined, not conduct-defined. Its content depends on a prior account of what the role requires, which the Code does not supply.

**Arts. 4(i)–(ii)**
- **OBS** — Members must prevent conflicts of interest from arising, arrange their private financial affairs to prevent conflicts, and resolve any conflicts that arise quickly and in the public interest.
- **INT** — The duty of prevention is higher than a duty of disclosure. A Member who passively acquires a conflicting interest without taking structural steps to prevent it may breach Art. 4(ii) even if no actual decision in conflict has yet been made.
- **INT** — "Quickly" is time-qualified but undefined. No timeframe is specified; the obligation is determinable only in context by an authoritative resolver the Code does not designate.

**Art. 5(i)**
- **OBS** — A conflict of interest exists where a Member participates in or makes a decision knowing it will improperly and dishonestly further private financial interest (their own or another's) directly or indirectly.
- **INT** — Three cumulative mental elements: knowledge, impropriety, dishonesty. This is a composite threshold materially higher than a negligence or strict-liability standard. Naively self-interested or reckless conduct does not satisfy it.
- **INF** — The definition at Art. 5(i) is narrower than the prevention duty at Art. 4. A Member may breach Art. 4 (by failing to prevent a structural conflict) without satisfying the Art. 5(i) definition (for want of the required mental elements). These provisions operate on different planes and must not be conflated.

**Art. 5(ii)**
- **OBS** — Benefit as a member of the general public or a broad class of persons does not constitute a conflict of interest.
- **INT** — "Broad class" is undefined. The scope of the exception is entirely open to interpretation; the Code provides no further guidance and designates no authoritative interpreter.

**Art. 6**
- **OBS** — Members may not solicit, accept, or receive any financial benefit or profit in exchange for promoting or voting on a Bill, motion, resolution, order, or any question put to the Dáil or its committees.
- **INT** — Absolute prohibition. No mental element qualification; no exception. The transaction itself constitutes the breach regardless of whether conduct was altered.
- **INF** — Art. 6 maps directly onto the corruption provisions of the Ethics Acts and related criminal law. It is the one provision in the Code where breach most directly implicates consequences available outside the Code's own enforcement architecture.

**Art. 7**
- **OBS** — Members must conscientiously fulfil requirements of the Dáil and the law regarding registration and declaration of interests and must familiarise themselves with guidelines from the Committee on Members' Interests and SIPO.
- **INT** — "Conscientiously" elevates the standard above technical compliance. The familiarisation obligation is rolling and active: it is not discharged by a one-time reading; Members must update their knowledge as new guidelines are published.

**Arts. 8(i)–(ii)**
- **OBS** — Members must not accept gifts that may pose a conflict or might interfere with impartial exercise. Incidental gifts and customary hospitality are permitted.
- **INT** — The prohibition triggers on potential, not actual, interference ("may," "might"). This is a lower bar than the Art. 5(i) conflict definition.
- **HYP** — Arts. 8(i)–(ii) constitute an evidence-production void: no disclosure requirement, no threshold value, no designated recipient for notification, no definition of "incidental" or "customary." Compliance with the gift regime generates no required documentary residue. Non-compliance is only discoverable through external means. This is structurally significant for any investigation of conduct under this provision.

**Art. 9**
- **OBS** — Members must apply public resources prudently and only for their intended purposes.
- **INT** — "Intended purposes" is defined by the authorising instrument for each resource type, not by the Code. The obligation is derivative on external definitions the Code does not supply.

**Art. 10**
- **OBS** — Members must not use non-public official information, or information obtained in confidence in official duties, for personal gain or the gain of others.
- **INT** — Two independent categories of information are covered. Information in the public domain but obtained in confidence remains covered by the second limb; the two limbs have independent scope.
- **INT** — The prohibition extends to gain for others. It is not ego-bounded.
- **INF** — Art. 10 is the most tractable provision in the Code for documentary tracing: if information can be established as non-public or confidentially obtained, and its use in a context producing gain can be shown, the inference of breach is direct, subject only to confirmation that the information was obtained in the course of official duties.

**Art. 11**
- **OBS** — Members must co-operate with Tribunals of Inquiry and other bodies inquiring into matters of public importance established by the Houses of the Oireachtas.
- **INT** — The Code makes co-operation a professional obligation of the Member's role, supplementary to any legally enforceable compulsion. A Member who technically complies with a legal summons but obstructs the inquiry's substantive work may breach Art. 11 without breaching a legal obligation.
- **HYP** — Art. 11 has operative teeth only to the extent that the inquiry machinery itself is constituted and functional. Where an inquiry's terms of reference are narrowed or its powers are structurally limited, the duty to co-operate cannot produce the substantive accountability the provision assumes.

## 8. Source registry

This section records the canonical online sources for documents currently in the layer, with direct links. As new documents are added, their sources are registered here. The registry is the authoritative reference for provenance; individual document entries link to it.

### Code of Conduct for Members of Dáil Éireann Other Than Office Holders (2012)

| Field | Value |
|---|---|
| Issuing body | Committee on Members' Interests of Dáil Éireann (31st Dáil) |
| Date | 30 May 2012 |
| Accompanying instrument | Guidelines for Members of Dáil Éireann Who Are Not Office Holders concerning compliance with the Ethics in Public Office Acts 1995 and 2001 |
| Oireachtas listing | [oireachtas.ie/en/committees/32/members-interests-dail/documents/](https://www.oireachtas.ie/en/committees/32/members-interests-dail/documents/) |
| Canonical PDF | [data.oireachtas.ie · 2012-05-30_code-of-conduct-for-members-of-dail-eireann-non-officeholders_en.pdf](https://data.oireachtas.ie/ie/oireachtas/committee/dail/31/committee_on_members_interests_dail_eireann/termsOfReference/2012/2012-05-30_code-of-conduct-for-members-of-dail-eireann-non-officeholders_en.pdf) |
| Local file | `codes-of-practice/code-of-conduct-members-dail-eireann-2011.md` |
| Index entry | `codes-of-practice/index.html` |
| Atom set status | complete (provision-by-provision, structural, FSD classifications) |
| Cross-references | Ethics in Public Office Act 1995 (pending); Standards in Public Office Act 2001 (pending) |

### Ethics in Public Office Act 1995

| Field | Value |
|---|---|
| Status | *pending upload* |
| Expected location | `primary-legislation/` |
| Irish Statute Book (revised) | [revisedacts.lawreform.ie · 1995/act/22](https://revisedacts.lawreform.ie/eli/1995/act/22/front/revised/en/html) |
| Oireachtas page | [oireachtas.ie · ethics-in-public-office-acts](https://www.oireachtas.ie/en/working-in-parliament/ethics/ethics-in-public-office-acts/) |
| Cross-references | Code of Conduct (codes-of-practice); Standards in Public Office Act 2001 (primary-legislation, pending) |

### Standards in Public Office Act 2001

| Field | Value |
|---|---|
| Status | *pending upload* |
| Expected location | `primary-legislation/` |
| Irish Statute Book (revised) | [revisedacts.lawreform.ie · 2001/act/31](https://revisedacts.lawreform.ie/eli/2001/act/31/front/revised/en/html) |
| Cross-references | Code of Conduct (codes-of-practice); Ethics in Public Office Act 1995 (primary-legislation, pending) |

> **Registry note:** entries marked *pending upload* indicate documents whose online sources have been identified and verified but whose content has not yet been added to the corpus. Atom extraction for these documents begins on upload.

## 9. Conventions and constraints

### What this layer does not do

- It does not reach findings of illegality, bad faith, negligence, or intentional obstruction. Those are propositions for other layers of the corpus with their own evidentiary requirements.
- It does not assume that a normative provision was known to, observed by, or applied by any institution. Knowledge and application are factual claims requiring documentary support.
- It does not treat the presence of a code or guideline as evidence of its operative effect. A code may exist while being entirely unknown to the persons it governs, or while the enforcement machinery it assumes is non-functional.
- It does not treat a HYP atom as established. HYP atoms are working hypotheses; they are revised, elevated, or abandoned as the documentary record develops.

### Version control

Where a normative instrument has been amended, the version operative at the material time is the analytical reference. This manual and the index pages will note version history where it bears on interpretation. Where multiple versions of a document are in circulation, the version in this layer is identified by its date and, where applicable, its Oireachtas document ID.

### The relationship between this layer and other corpus layers

This layer provides the normative reference against which documentary evidence from other layers is assessed. It does not stand alone. The analytical output of this layer — the atom sets — is consumed by the reasoning layer of the corpus, where normative atoms are combined with factual atoms from the documentary record to generate INF and HYP propositions about institutional conduct and operative effect.

#### FSD ontology: this layer and the normative–operative gap

The FSD ontology emerged from the problem this layer addresses: a normative framework may be formally present while the institutional mechanisms through which its protections, duties, procedures, or remedies are made operative are absent, fragmented, displaced, or otherwise ineffective. This layer maps the normative side of that gap. The documentary record maps the operative side. The FSD concepts — competence vacancy, duty displacement, procedural displacement, transposition gap, structural failure, normative collapse — describe particular forms of gap between the two sides. They are applied as analytical classifications, not as findings, and their conditions must always be established against the evidence.

*Sources: FSD-Ontology-2026.md · FSD-Ontology-2026-Extended-Framework.md*

---

*post-hoc · corpus · laws-and-codes · MANUAL · version 0.1*
