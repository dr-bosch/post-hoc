# EU Regulatory Annotation — v2
## Qualifying Submissions (Duty to Determine) Bill 2026 (v3)

*Companion document. Updated against Bill v3 and Gatekeeping Brief v4.4.
Maps each operative provision of the Bill to the corresponding article of
Regulation (EU) 2024/1689 (the EU AI Act) and/or Regulation (EU) 2021/821
(the Dual-Use Regulation) that grounds, implies, or is given domestic effect
by that provision. Where the Digital Omnibus on AI — Regulation (EU) 2026/1744,
in force 27 July 2026 — amends the application dates of 2024/1689, that amendment
is noted. References to the Regulation of Artificial Intelligence Act 2026 (Ireland)
are to the Act signed into law on 21 July 2026.*

*New in v2: annotations for ss. 2B, 2C, 3A and the Explanatory Memorandum (all new in
Bill v3); cross-reference table updated; Simon/OR/AI grounding from Gatekeeping Brief
v4.4 integrated where it informs the legal annotations; OR Office proposal (Gatekeeping
Brief §X) cross-referenced where it projects beyond what the Bill currently enacts.*

*This document is support material only.*
*SSCEUST-I-2026-074 · OMB-260331-CSD014 · PAC ref. S-2026-0307*

---

## Preliminary Note on Application Dates (Digital Omnibus)

Regulation (EU) 2026/1744 (Digital Omnibus on AI), in force 27 July 2026:

| Obligation cluster | Original date | Omnibus-amended date |
|---|---|---|
| High-risk systems — Annex III (standalone) | 2 August 2026 | **2 December 2027** |
| High-risk systems — Annex I (product safety) | 2 August 2027 | **2 August 2028** |
| Prohibited practices (Art. 5) | 2 February 2025 | Unchanged |
| General-Purpose AI (Chapter V) | 2 August 2025 | Unchanged |
| AI literacy (Art. 4) | 2 February 2025 | Unchanged |

The Bill's domestic obligations are not deferred by the Omnibus. The duty to determine
attaches from the Bill's commencement regardless of when EU conformity assessment
obligations become enforceable against developers.

---

## RECITAL

### Third Clause (as amended and introduced)

> *"and having regard to the guarantee of personal rights under Article 40.3 of
> Bunreacht na hÉireann and the right to good administration under Article 41 of
> the EU Charter of Fundamental Rights"*

**EU grounding:**
- **Art. 41 CFR** — Right to good administration: impartial handling within a reasonable
  time; right to be heard; right of access to one's file; obligation to give reasons.
  Procedural floor beneath every provision of the Bill.
- **Art. 47 CFR** — Effective remedy before a tribunal. Grounds the High Court pathway
  under Part VI (s. 10C).
- **Art. 9(2) Reg. 2021/821** — The CA must maintain and exercise the capacity to
  assess. The Recital's EU law anchor is Art. 9(2) for the dual-use dimension and
  Arts. 41/47 CFR for the procedural floor.

---

## PART I — PRELIMINARY AND GENERAL

### s. 1(4) — Scope limitations (new in v3)

The six enumerated exclusions in s. 1(4) — no right to a favourable decision, no
policy transfer to the Ombudsman, no alteration of existing jurisdictions, no
replacement of sufficient procedures, no obligation to adopt submissions, no substantive
rights — now appear in the operative text rather than only in the Introduction.

**EU grounding:** This structure tracks the procedural/substantive distinction at
the heart of Art. 41 CFR: good administration is a procedural guarantee, not a
guarantee of any particular outcome. The Explanatory Memorandum (General Purpose)
names this explicitly: "Its purpose is procedural."

---

### s. 2(1) — "AI system" and "high-risk AI system"

**EU AI Act — Art. 3(1):**
*"AI system means a machine-based system that is designed to operate with varying
levels of autonomy and that may exhibit adaptiveness after deployment, and that,
for explicit or implicit objectives, infers, from the input it receives, how to generate
outputs such as predictions, content, recommendations, or decisions that can influence
physical or virtual environments."*

**EU AI Act — Art. 6 / Annex III:**
High-risk classification. Annex III categories most likely to engage OR methodology:
- Point 3: AI systems used to evaluate access to essential public services
- Point 6: AI systems used by competent authorities to assess risks (law enforcement,
  civil protection)
- Point 8: AI systems for administration of justice and democratic processes

**Omnibus note:** Annex III high-risk obligations apply from 2 December 2027.
The Bill's definitions operate from commencement regardless.

---

### s. 2(1) — "operative submission" (new in v3)

The definition introduces a three-limb test: (a) deployed/executable/persistently
scheduled component; (b) unrestricted access offered by submitter; (c) outputs that are
independently observable, replicable, and refutable.

**The Simon/OR grounding (Gatekeeping Brief §"Why This Background Matters Here"):**
The naming dispute between AI and OR — and Simon's observation that "we were doing AI
before Dartmouth, we just called it operations research" — is directly operative here.
An operative submission in the sense of s. 2(1) is what Simon and Newell would have
recognised as a reduction to practice: not a claim about what a system can do, but a
running demonstration that it does it. The Bill's distinction between operative and
non-operative submissions imports the patent-law distinction between mere conception
and reduction to practice (Explanatory Memorandum, "Operative Submissions"). Simon's
Logic Theorist was, in the same sense, an operative submission: it ran, it produced
verifiable outputs, and those outputs were independently replicable. The institutional
resistance it met — McCarthy's attempt to present it as an output of Dartmouth rather
than independent prior work — is the procedural analogue of the sufficiency assertion.

**EU AI Act grounding:**
- **Art. 9(8):** Testing "shall be carried out against prior defined metrics and
  probabilistic thresholds." A system capable of producing verifiable outputs on demand
  is, in Art. 9(8) terms, already in the testing phase. The operative submission
  definition captures this: the component must be producing or capable of producing
  outputs independently observable and refutable on stated criteria — the same standard
  Art. 9(8) applies to developer testing.
- **Art. 13(2):** Instructions for use must enable deployers to correctly interpret
  the system's outputs. A component whose outputs are replicable under conditions the
  submitter has specified in writing has already satisfied the transparency standard
  Art. 13 sets for deployers — it has stated the conditions under which its outputs
  should be interpreted and tested.

---

### s. 2(1) — "structural displacement"

**EU grounding:**
- **Art. 70 Reg. 2024/1689:** Member States must designate one or more competent
  authorities and a single point of contact. Where three bodies together constitute the
  CA function with no coordination mechanism, the single-point-of-contact requirement
  is satisfied in form (AI Office) but not in substance for the dual-use dimension
  (DETE/DFA/DoD).
- **Art. 9(1)-(2) Reg. 2021/821:** The CA designation and the assessment capacity must
  be maintained and exercised together. Structural displacement — each body holding a
  component — means neither obligation can be discharged by any single body.

---

### s. 2B — Principle of Procedural Closure (new in v3)

*"Every lawful administrative process initiated by a qualifying submission shall
conclude through a lawful determination."*

**EU grounding:**
- **Art. 41 CFR** — The right to good administration includes the right to have one's
  affairs handled within a reasonable time and with a reasoned decision. A process that
  circulates without concluding violates both elements simultaneously. s. 2B converts
  this CFR guarantee into a domestic statutory principle from which every subsequent
  provision is construed as flowing (s. 2B(4)).
- **Art. 47 CFR** — Effective remedy requires that there be a determination to review.
  A process that never concludes forecloses the Art. 47 remedy at source. s. 2B(3)
  supplies the residual mechanism (Part VI) that converts the permanent circulation
  into a reviewable event.
- **Art. 2 TEU** — Rule of law requires legal certainty. A statutory obligation that
  circulates indefinitely without resolution is antithetical to legal certainty. The
  Explanatory Memorandum (Constitutional Narrative) names this: s. 2B "completes"
  the progression of natural justice, due process, and good administration principles
  by reaching the one condition those principles do not individually close.

---

### s. 2C — Operative submissions: general principle (new in v3)

**Five sub-provisions with distinct EU law connections:**

**(1)-(2) Elevated standard of engagement:**

**EU AI Act — Art. 9(5):**
Risk management measures must ensure that "the overall residual risk of the high-risk
AI system is judged to be acceptable." Where the submitted system is operational and
produces verifiable outputs, the receiving body cannot assess residual risk without
engaging those outputs. The *O'Keeffe* principle (s. 2C(7)(a)) and the Art. 9(5)
adequacy standard operate in parallel: a judgment of acceptability that does not engage
specific empirical material is unreasonable under *O'Keeffe* and inadequate under Art. 9.

**(3) Estoppel on domain familiarity:**

**EU AI Act — Art. 13(3):**
Instructions for use must contain information enabling deployers to correctly interpret
the system's outputs. A body that has declined to observe an operative component cannot
claim to have interpreted its outputs correctly. s. 2C(3) gives this statutory form:
a determination relying on general domain knowledge after declining access to the
operative component is not a determination.

**(5) Field-proven sufficiency:**

**EU AI Act — Art. 43(4):**
Where a high-risk AI system has already been placed on the market and the provider
demonstrates continued compliance, simplified conformity assessment procedures apply.
The field-proven sufficiency principle in s. 2C(5) imports the same logic into the
administrative determination context: prior operational use in a comparable domain
satisfies the sufficiency threshold; the receiving body must identify specific material
differences rather than treating prior operational history as irrelevant.

**Reg. 2021/821 — Art. 14:**
Notification of decisions. Where a body disputes the relevance of prior operational
evidence, its notification must give the specific grounds for that dispute. A general
assertion that prior use is insufficiently comparable, without identifying the specific
material difference, does not satisfy Art. 14's reasons requirement.

**(6) Democratised computing:**

**EU AI Act — Art. 9(8):**
Testing requirements must be proportionate to the system's intended purpose and the
risk it poses. A body that treats ordinarily accessible computing infrastructure as
specialised has applied a disproportionate infrastructure threshold to its assessment
obligations. The *O'Keeffe* standard (s. 2C(7)(a)) and the proportionality principle
in Art. 9(8) converge: irrationality is found more readily where the claimed
infrastructure barrier is inconsistent with the public accessibility of the tools
the system uses.

**The OR/AI democratisation parallel (Gatekeeping Brief §X, Democratised Computing):**
The Explanatory Memorandum's observation that "the diverse set of system solvers now
available — turnkey software spanning optimisation, simulation, scheduling, and
decision-support, deployable without specialist configuration" — carries a direct
connection to the AI Act's own conformity assessment framework. The same democratisation
of computing capacity that makes OR systems independently observable also makes the
AI Act's testing requirements (Art. 9(8)) operationally feasible for competent
authorities without specialist infrastructure. The two provisions — s. 2C(6) and
Art. 9(8) — are calibrated to the same technological baseline.

**(7) Interpretive provision — case law triad:**
- *O'Keeffe v An Bord Pleanála* [1993] → maps to Art. 9 adequacy
- *Stefan v Minister for Justice* [2001] → maps to Art. 14 Reg. 2021/821 (reasons)
- *Wiley v Revenue Commissioners* [1994] → maps to Art. 41 CFR (estoppel on
  procedural choice adverse to submitter)

---

### s. 3(2)(b) — High-risk AI qualifying submissions

> *"asserts that the submitted system or methodology constitutes or incorporates a
> high-risk AI system within the meaning of the AI Act, engaging the conformity
> assessment obligations under Articles 9, 13, 14, and 27 of that Regulation"*

**The four operative AI Act articles — exact obligations:**

**Art. 9 — Risk management system** *(applies from 2 December 2027, Omnibus-amended)*
Requires: identification and analysis of known and reasonably foreseeable risks;
estimation and evaluation of risks under intended purpose and foreseeable misuse;
adoption of risk management measures. Testing against probabilistic thresholds (Art. 9(8)).
*OR connection:* Estimating and evaluating risks under foreseeable misuse conditions
is stochastic optimisation. A CA that cannot independently verify the developer's
probabilistic claims relies on developer documentation — capture in the sense of
Gatekeeping Brief §IV.

**Art. 13 — Transparency and information to deployers**
Requires: instructions for use identifying the system's capabilities, limitations,
performance metrics, and the human oversight measures of Art. 14.
*OR connection:* Verifying that stated performance bounds hold under deployment
conditions is a stochastic programming question. A sufficiency assertion claiming
general AI familiarity does not constitute this verification.

**Art. 14 — Human oversight**
Requires: effective oversight by natural persons; systems must be observable by
persons assigned oversight; those persons must be enabled to understand capabilities
and limitations and to correctly interpret outputs.
*OR connection:* Assessing whether human oversight is "effective" requires modelling
the human-AI interaction under operational conditions — a decision-support problem
OR addresses directly. s. 5's prohibition and s. 3A's elevated duty are the domestic
expressions of the standard Art. 14 implies for a CA assessing oversight adequacy.

**Art. 27 — Fundamental rights impact assessment**
Requires: public bodies deploying high-risk AI to assess risks to fundamental rights
before putting the system into service; disclosure to the relevant market surveillance
authority.
*OR connection:* A structured FRIA is a decision-analysis problem. A public body
without OR capacity either performs it without the analytical tools it requires, or
relies on the developer's documentation — exactly the capture dynamic ss. 5A–5C
are designed to displace.

---

### s. 3A — Elevated duty in respect of operative submissions (new in v3)

Ten subsections; the EU law connections are subsection-specific.

**s. 3A(2) — Reduced determination period (6 months):**
**Reg. 2021/821 — Art. 12:** Competent authorities shall make licensing decisions
within specified timeframes. The 6-month period for operative submissions reflects
the principle that where evidence is present and observable, the time required for
assessment is determinable rather than open-ended.

**s. 3A(3) — Categorical unavailability of sufficiency assertion:**
**EU AI Act — Art. 9(8):** Testing "shall be carried out against prior defined metrics
and probabilistic thresholds." A body that has been offered access to an operative
component and has not taken it cannot assert that existing metrics are adequate — it
has not applied metrics to this component. The categorical unavailability in s. 3A(3)
is the statutory expression of the Art. 9(8) testing obligation applied to the
administrative determination context.

**s. 3A(4) — Loop acceleration (immediate declination):**
A sufficiency assertion on an operative submission where access was declined counts
immediately toward the loop condition threshold, without the ordinary 5-year
accumulation period. **EU grounding: Art. 47 CFR** — effective remedy cannot be
indefinitely deferred by a sequence of non-engagements each individually valid.
Where the submission is demonstrably operational, the deferral mechanism that the
5-year period otherwise permits would compound the Art. 47 violation rather than
provide for its remedy.

**s. 3A(5) — Estoppel on domain familiarity:**
Tracks s. 2C(3). **EU AI Act — Art. 13:** A body that has not observed the component
cannot have interpreted its outputs. A determination representing general domain
knowledge as equivalent to specific component evaluation contravenes the transparency
standard Art. 13 sets.

**s. 3A(6) — Requirements for valid rejection after observation:**
The determination must engage the submitter's stated refutability criteria.
**Reg. 2021/821 — Art. 14; EU AI Act — Art. 13:** Reasons must be responsive to
the specific system's documented characteristics, not to the category.
*Stefan v Minister for Justice* [2001] is the domestic law expression of the same
standard; s. 2C(7)(b) makes this explicit.

**s. 3A(7) — Requirements for rejection without observation:**
Must state expressly that no observation was undertaken; must give specific reasons
for that choice; those reasons cannot be grounded in general domain familiarity.
**EU AI Act — Art. 9(8):** The choice not to test, where testing has been offered,
must itself be explained against the testing standard. A body cannot rely on the
decision not to test as though it were itself a finding about the system.

**s. 3A(8) — Persistent schedule — continuity of operative status:**
Where a component generates outputs continuously or at intervals, the operative status
does not lapse with time. **EU AI Act — Art. 72 (post-market monitoring):** Providers
must monitor high-risk AI systems continuously after deployment. The same logic applies
to assessment obligations: a system that continues to operate continues to require
assessment; the obligation does not expire while the system runs.

**s. 3A(9) — Loop acceleration for operative submissions:**
The 5-year accumulation period does not apply. **Art. 47 CFR:** The effective remedy
timeline cannot be calibrated to a period designed for non-operational submissions
when the submission is demonstrably operational and the evidence is immediately
available. The accelerated loop closure is the remedy proportionate to the immediacy
of the evidence.

---

### s. 5 — Prohibition on sufficiency assertion

**EU AI Act — Arts. 9(8), 13(3), 14(4):** Each requires engagement with the specific
system's documented characteristics. Generic disciplinary awareness cannot satisfy
Art. 9(8)'s testing standard, Art. 13(3)'s instructions-accuracy standard, or
Art. 14(4)'s oversight-enablement standard.

**Reg. 2021/821 — Art. 9(2):** The CA must "maintain and exercise" assessment
capacity. A sufficiency assertion is the performance of assessment without its exercise.

**Mertonian grounding (Gatekeeping Brief §IV):**
The sufficiency assertion violates universalism (evaluation by impersonal criteria
applied to the claim itself, not to the category) and organised scepticism (critical
scrutiny of the specific claim). s. 5 is the statutory expression of both norms.

---

### ss. 5A–5C — Independent technical audit

**EU AI Act — Art. 43:** Conformity assessment for most Annex III systems is
self-assessment against harmonised standards. Where independent assessment is needed,
Art. 43(4) provides for it; Arts. 43(5)-(6) set independence and competence
requirements. ss. 5A–5C build the equivalent mechanism for the domestic
administrative determination context, with Ombudsman nomination as the independence
safeguard where parties cannot agree (s. 5B).

**EU AI Act — Art. 68 (Scientific Panel):** The AI Office may call on independent
experts for technical advice. ss. 5B–5C track this architecture: the auditor is
nominated independently, must disclose any relationship with the subject domain
(disinterestedness norm, Gatekeeping Brief §IV), and reports simultaneously to the
submitter and the receiving body.

**EU AI Act — Art. 84 (Union testing support structures):**
Where no domestic testing facility exists, ss. 5A–5C provide the equivalent function
at the domestic level, making Ireland potentially the first Member State to establish
a formalised technical assessment pathway for OR corpus submissions engaging both
the AI Act and the Dual-Use Regulation simultaneously (as noted in the annotation v1,
Technical Annex section — unchanged).

**Science denial / degenerate norm grounding (Gatekeeping Brief §IV):**
The disinterestedness requirement in s. 5B — the auditor must have no relevant
relationship with the sector whose practice would otherwise be cited as the standard —
directly addresses the disinterestedness norm violation the Gatekeeping Brief
identifies. Industrial technologist default is displaced by a commissioned
appointment. The unreviewable is made reviewable.

---

## PART III — ADMINISTRATIVE MEMORY AND CONTINUITY OF RECORD

### s. 6 — Prohibition on administrative amnesia

**Reg. 2021/821 — Art. 9(2):** Assessment capacity must be "maintained." A body
that treats a twenty-year engagement as a first encounter has not maintained its
assessment capacity — it has lost its institutional memory of the obligation.

**EU AI Act — Art. 72:** Post-market monitoring requires continuous records.
The same record-continuity logic applies to assessment obligations: the administrative
record of a formally submitted corpus is the monitoring record that the CA's Art. 9(2)
capacity obligation depends on.

**Bateson/Deutero-Learning grounding (Gatekeeping Brief §IV, Deutero-Learning):**
Administrative amnesia is the institutional expression of deutero-learning failure:
the system learns not to learn, producing fresh officers who encounter the record
as though for the first time. s. 6 is the statutory disruption of that loop.

---

### s. 7 — Prohibition on loss of the administrative record

**Art. 41 CFR** — Right of access to one's file. Deletion of formally lodged
correspondence after declination (the JCEUA deletion of October 2025) violates this
right directly. s. 7 converts the Art. 41 right into a statutory prohibition backed
by the Ombudsman Act 1980 maladministration classification.

---

## PART IV — RETROSPECTIVE APPLICATION

### s. 8 — Transitional duty of determination

**Reg. 2021/821 — Arts. 9(2), 12, 14:** The obligation has been continuous since
2009 (DFA designation under predecessor Reg. 428/2009). s. 8's 6-month period is the
domestic expression of the urgency Arts. 12 and 14 carry.

**EU AI Act — Art. 113(c):** The AI Act's high-risk obligations apply from
2 December 2027 (Omnibus-amended). s. 8's retrospective application to AI Act
submissions ensures that where a submission asserting high-risk AI characteristics
has been formally lodged, the domestic duty to determine runs from commencement
regardless of the EU conformity-assessment timeline.

---

### s. 8A — Non-determination by reliance on unresolved prior conclusions

**EU AI Act — Art. 9(5):** A judgment of acceptability based on contested and
unanswered conclusions is not a reasoned residual-risk assessment.
**Meadows v Minister for Justice [2010] 2 IR 701** — reasons must engage the specific
case. The McEntee Foreclosure (DOD-MO-01201-2025) is the documented instance: it
relied on OEP conclusions formally rebutted the following day and never defended.

---

### s. 8B — Non-determination by over-extension of powers

The section-92 problem (Gatekeeping Brief §III, "The Section 92 Problem"):
the use of a correspondence-management power to close a substantive submission
without determination. **Art. 41 CFR** — the right to good administration is
violated when a management power is deployed to foreclose a procedural right.
s. 8B makes this a cognisable event without requiring proof of bad faith.

---

### ss. 8C–8D — Chain-of-duty and shared responsibility

**s. 8C:**
The August 2024 DFA→DETE transfer is the documented instance. **Reg. 2021/821 —
Art. 9(2):** The assessment obligation is not extinguished by transfer of designation.
s. 8C ensures it vests in the receiving body from the date of transfer and the
compliance clock is not reset.

**s. 8D:**
The JCPP–JCEUA gatekeeping chain is the documented instance. A body aware of
another's failure to determine, that takes no steps to bring the submission to a
competent body, shares responsibility. **Art. 4(3) TEU** — sincere cooperation
extends to awareness of and response to compliance failures; wilful non-transmission
is the parliamentary expression of the same obligation.

---

### ss. 8E–8F — Bad faith and inadequate assessment

**s. 8F:**
**EU AI Act — Art. 74(3):** Market surveillance authorities must have necessary
resources. A determination made without the technical capacity to evaluate is a
determination made without the Art. 74(3) resources. **Reg. 2021/821 — Art. 9(2):**
"Maintain and exercise" — a body that issues an adequacy conclusion without exercising
the assessment capacity has not discharged Art. 9(2).

---

## PART VI — LOOP CLOSURE

### ss. 10B–10C — The loop condition and residual determination obligation

**Art. 47 CFR:** Effective remedy before a tribunal. The loop condition is the
condition in which Art. 47 has been violated at scale: three or more bodies, no
merits examination, no body producing a determination. s. 10C(4)'s mandatory High
Court referral by the Ombudsman is the domestic instrument of Art. 47 enforcement.

**Art. 267 TFEU:** Where the High Court applies EU law standards (Arts. 12 and 14
Reg. 2021/821 as the basis for mandamus), a refusal to grant mandamus is in effect
a refusal to enforce directly applicable EU law — cognisable as a question for CJEU
reference. The EU oversight dimension is embedded in the domestic standard, not a
parallel track.

**Jurisdictional indeterminacy (Explanatory Memorandum §"Jurisdictional Indeterminacy
Distinguished from Temporal Indeterminacy"):**
The loop condition addresses what French law has not: the case where three bodies
successively disclaim competence without any body holding the integrated obligation.
The ping-pong administratif has a name in French law but no remedy; s. 10B provides
the remedy.

---

## PART VII — EU AND AI REGULATORY COMPLIANCE

### s. 11 — Competent authority reporting

**Reg. 2021/821 — Art. 26:** Member States must provide statistical data to the
Commission. The review opens 10 September 2026. s. 11 converts the implied obligation
into an express domestic statutory duty timed to the Oireachtas calendar.

### s. 11A — AI Act compliance reporting

**EU AI Act — Arts. 70(1), 75, 112:** Designation of NCAs; inter-authority
cooperation; Commission evaluation. s. 11A produces the domestic statistical record
that feeds into the Commission's mandatory Art. 112 review, ensuring gaps between
stated conformity assessment capacity and actual assessment activity are on record.

**Reg. AI Act 2026 (Ireland) — s. 14:** The AI Office's own annual report is the
coordination layer; s. 11A is the determination-specific accountability layer.
Together they constitute the full accountability picture the EU evaluation framework
requires.

---

## EXPLANATORY MEMORANDUM — EU Law Connections

### "Operative Submissions: The Common Law Foundation"

The patent-law/reduction-to-practice distinction imported by this section has a
direct EU AI Act analogue in **Art. 43**: conformity assessment turns on whether
the system meets the requirements applicable to it — not on whether the subject matter
is a known field. The Bill's adaptation of the patent-law distinction to administrative
procedure closes the same gap Art. 43 closes for conformity assessment: a running
system is assessed against its actual outputs, not against general disciplinary
awareness of systems of its class.

### "Democratised Computing"

The democratised computing principle in s. 2C(6) and the Explanatory Memorandum
is the domestic statutory expression of the same baseline the **EU AI Act implicitly
assumes** in setting its observability and testing standards: that modern computing
tools are sufficiently accessible that a CA exercising its functions has no principled
basis for treating ordinary computational observation as requiring specialised
infrastructure it does not possess.

**OR Office projection (Gatekeeping Brief §X):** The Explanatory Memorandum's
democratised computing section anticipates, without yet proposing, the institutional
consequence Gatekeeping Brief §X draws explicitly: a sovereign OR assessment capacity
is now technologically feasible without specialist infrastructure, which means the
only remaining barrier to establishing it is institutional will, not technical
capacity. The OR Office proposal converts that observation into a legislative
recommendation.

### "Jurisdictional Indeterminacy Distinguished from Temporal Indeterminacy"

This section of the Explanatory Memorandum is the Bill's direct response to the
French comparative material in Gatekeeping Brief §VIII. It names what no other
identified jurisdiction has yet legislated for: the condition in which an obligation
is distributed across bodies none of which holds it in full, producing a permanent
non-determination that temporal mechanisms (silence rules, deadlines) cannot reach.

**EU law grounding:** Art. 41 CFR's reasonable-time guarantee addresses temporal
indeterminacy. Art. 47 CFR's effective-remedy guarantee addresses jurisdictional
indeterminacy — but only at the EU level, within EU institutions. No Member State
mechanism was identified that creates a domestic residual determination obligation
triggered by the exhaustion of ordinary administrative channels. This Bill creates it.

---

## Cross-Reference Table (updated for Bill v3)

| Bill section | EU AI Act article | Reg. 2021/821 article | Domestic AI Act 2026 |
|---|---|---|---|
| Recital (3rd clause) | Arts. 41, 47 CFR | Art. 9(2) | — |
| s. 1(4) | Art. 41 CFR | — | — |
| s. 2 ("AI system") | Art. 3(1); Art. 6; Annex III | — | s. 3 (definitions) |
| s. 2 ("competent authority") | Art. 70 | Arts. 9(1), 9(2); Art. 2(1) | s. 7 (AI Office) |
| s. 2 ("operative submission") | Arts. 9(8), 13(2) | — | — |
| s. 2 ("structural displacement") | Art. 70 | Arts. 9(1), 9(2) | s. 7 |
| s. 2B (Procedural Closure) | Arts. 41, 47 CFR; Art. 2 TEU | — | — |
| s. 2C(1)-(2) (elevated standard) | Art. 9(5) | — | — |
| s. 2C(3) (estoppel) | Art. 13(3) | — | — |
| s. 2C(5) (field-proven sufficiency) | Art. 43(4) | Art. 14 | — |
| s. 2C(6) (democratised computing) | Art. 9(8) | — | — |
| s. 2C(7) (interpretive provision) | Arts. 9, 13, 41 CFR | Art. 14 | — |
| s. 3(2)(a) | — | Art. 9(2) | — |
| s. 3(2)(b) | Arts. 9, 13, 14, 27 | — | — |
| s. 3A(2) (reduced period) | — | Art. 12 | — |
| s. 3A(3) (sufficiency unavailable) | Art. 9(8) | — | — |
| s. 3A(4) (loop acceleration) | Art. 47 CFR | — | — |
| s. 3A(5) (estoppel) | Art. 13 | — | — |
| s. 3A(6) (valid rejection) | Art. 13 | Art. 14 | — |
| s. 3A(7) (rejection without observation) | Art. 9(8) | — | — |
| s. 3A(8) (persistent schedule) | Art. 72 | — | — |
| s. 3A(9) (loop acceleration — operative) | Art. 47 CFR | — | — |
| s. 5 (sufficiency assertion ban) | Arts. 9(8), 13(3), 14(4) | Art. 9(2) | — |
| ss. 5A–5C (independent audit) | Arts. 43, 68, 84 | — | s. 14 |
| s. 6 (administrative amnesia) | Art. 72 | Art. 9(2) | — |
| s. 7 (record loss) | Art. 41 CFR | — | — |
| s. 8 (retrospective) | Art. 113(c) | Arts. 9(2), 12, 14 | — |
| s. 8A (unresolved conclusions) | Art. 9(5) | Art. 14 | — |
| s. 8B (over-extension) | Art. 41 CFR | — | — |
| s. 8C (chain-of-duty) | — | Art. 9(2) | — |
| s. 8D (shared responsibility) | Art. 4(3) TEU | — | — |
| s. 8F (inadequate assessment) | Art. 74(3) | Art. 9(2) | — |
| ss. 10B–10C (loop closure) | Art. 47 CFR; Art. 267 TFEU | Arts. 12, 14 | — |
| s. 11 (CA reporting) | — | Art. 26 | — |
| s. 11A (AI Act reporting) | Arts. 70(1), 75, 112 | — | s. 14 |
| s. 14 (Technical Annex) | Arts. 70(2), 84 | — | — |

---

## Note on the Digital Omnibus

The Omnibus defers high-risk enforcement but does not defer:
- Art. 70 competent authority designation (already in force)
- Arts. 41/47 CFR (Charter, always in force)
- Reg. 2021/821 CA assessment obligation (in force since 2009/2021)
- The Bill's duty to determine (from commencement)

The Omnibus is not a defence to non-determination. It defers developer conformity
obligations; it does not defer CA assessment obligations or this Bill's domestic duties.

---

## OR Office Projection

The OR Office proposal in Gatekeeping Brief §X is not operative under this Bill.
It is a legislative recommendation for an amendment to the Regulation of Artificial
Intelligence Act 2026. Its EU law grounding — Arts. 9, 13, 14, 27, 70(2), 84 of the
AI Act; the dual-use convergence under Reg. 2021/821 — is fully documented in the
annotation for those sections above. The OR Office would supply the sovereign OR
assessment capacity that those articles presuppose in a CA but do not themselves create.

---

*Annotation v2 prepared September 2026. EU AI Act text from OJ version of 12 July 2024
as amended by Digital Omnibus Reg. (EU) 2026/1744 (OJ L, 24 July 2026). Reg. of
Artificial Intelligence Act 2026 (Ireland) as signed 21 July 2026. Bill v3 as uploaded
September 2026. All case law citations verified against Irish Reports.*

*CC0 — the record is public.*
*SSCEUST-I-2026-074 · OMB-260331-CSD014 · PAC ref. S-2026-0307*
