# Qualifying Submissions (Duty to Determine) Bill 2026
## Ontology · Charter · Pathways — Consolidated Working Document

_SSCEUST-I-2026-074 · OMB-260331-CSD014 · PAC ref. S-2026-0307_

_This document merges two companion analyses: the **Bill–Charter–Ontology Mapping** (revised against FSD-Ontology-2026) and the **Pathways to Adoption** (v3). Its purpose is to make visible the valence between them — the way the structural diagnosis in the mapping becomes the argument each pathway advances, and the way each pathway's practical constraints determine which part of the mapping needs to be surfaced, and how._

_Where the two documents pull in different directions, this merge names the tension rather than resolving it silently._

_Companion documents: **Qualifying Submissions (Duty to Determine) Bill 2026** (consolidated draft); **Extended Introduction** (v3.3); **Technical Annex**; **The Gatekeeping Problem** (support brief); **FSD-Ontology-2026**; **Charter on Strategic Intelligence, Governance Risk, and Institutional Vulnerability**; **Interregnum Nullificans** (audit map)._

_Audit conformance status: revised against Interregnum Nullificans audit SVG (v13 reference). Seven gaps from the initial conformance check have been incorporated. Outstanding open items from the audit that affect claims in this document: **OI-01** (Hypothesis C — dual-use characterisation depends on an epistemic failure argument not yet drafted); **OI-02** (JCPP structural conflict — Ombudsman track risk not yet resolved); **OI-03** (three-tier non-substitutability — asserted, proof from instruments outstanding). Claims downstream of these open items should be read as conditional on their resolution._

---

## Part I — The Structural Diagnosis

### Three Layers of Accountability

The Bill operationalises the Charter by translating abstract vulnerability categories into justiciable obligations, formally expressed in the FSD Ontology 2026 (`fsd:` namespace).

**Layer 1: Charter Articles** (vulnerability categories — the _why_)  
**Layer 2: Bill Sections** (procedural mechanisms — the _what_)  
**Layer 3: FSD Ontology** (formal classes and causal operators — the _how it is proved_)

Each pathway in Part III draws on a different layer as its primary instrument. A sponsoring TD leads with Layer 2 (the Bill's operative provisions are defensible on their own terms). A law reform submission leads with Layer 1 (the Charter's four-category vulnerability frame). A think tank pitch leads with the diagnostic gap — the space between Layers 1 and 2 that no existing procedural instrument currently occupies.

### Four Structural Conditions (FSD §4.5)

These four conditions underlie every failure mode in the record. They are `fsd:StructuralCondition` subclasses. None is mutually exclusive; each can produce and sustain the others. They are the ground on which every pathway argument rests — and the reason why the Bill cannot be opposed simply by pointing to the existence of existing administrative law principles, since none of the four conditions is addressed by those principles.

| FSD Class | Plain-Language Definition | Primary Charter Article | Pathway Relevance |
|---|---|---|---|
| `fsd:NormativeCollapse` | Procedurally valid outputs produced while substantive obligations remain permanently unmet. The gap between form and substance is self-sustaining. | Art. II | The core claim for law reform and think tank pathways — this is what makes the loop condition a structural diagnosis rather than a complaint about individual conduct |
| `fsd:SilenceVeto` | Procedural silence functioning as an unnoticed adverse determination: no notice, no hearing, no reasons. Engages Art. 41 CFR and *Re Haughey* directly. | Art. I | The provision that gives the Bill's Section 2A its constitutional grounding — essential for the sponsoring TD's briefing on the Section 10C objection |
| `fsd:StructuralDisplacement` | Required competence distributed across multiple bodies with no coordination mechanism capable of assembling them. Established by statutory architecture alone, not by conduct. | Art. II, IV | The law reform submission's strongest diagnostic claim — procedural reform of non-court adjudicative bodies cannot address what is a structural architecture gap |
| `fsd:OnticCollapse` | Most acute form of structural displacement: no single body holds full competence and no mechanism assembles partial competences. The obligation cannot be discharged not by refusal but by absence of institutional subject. Primary classification: Art. II/IV; Art. VII non-escalation is a downstream consequence, not the primary ground. | Art. II, IV (→ Art. VII downstream) | The think tank's comparative claim — *ping-pong administratif* in French law reaches the same structural condition by a different route; the France comparison holds at the level of ontic collapse, not merely at the level of deferral |

### Five Causal Operators (OWL Object Properties)

The five OWL relations are the causal operators that connect structural conditions to justiciable outcomes. Each is now grounded in a Bill section and an FSD class.

| OWL Relation | FSD Class(es) | Charter Article | Bill Section | Legal Consequence | Which Pathway Uses It |
|---|---|---|---|---|---|
| `:ignores` | `fsd:NonDetermination` · `fsd:SilenceVeto` | I, IV | 3(1), 2A | Silence = legal effect; SWRL Rule 1 | All three: the simplest, most defensible provision |
| `:suppresses` | `fsd:DesignedForgetting` · `fsd:AdministrativeAmnesia` | III, V, VI | 10, 9, 5A–5C | Record loss = breach per se; secrecy veto prohibited | TD (Section 10 defence); think tank (novel legal category claim) |
| `:producesFailure` | `fsd:NullificationLoop` · `fsd:NormativeCollapse` · `fsd:ForeClosureByProxy` | II, VI | 6, 7, 8, 8A, 2B | Loop condition = institutional failure, not personal misconduct | Law reform (four-category frame); TD (Section 10B(3)(a) defence) |
| `:triggers` | `fsd:LoopCondition` · `fsd:StructuralDisplacement` · `fsd:OnticCollapse` | IV, VII | 10A, 10B, 3(2)(c) | SWRL Rules 2/3; residual obligation vests in Ombudsman | Law reform (non-court adjudicative bodies project); TD (Section 10C scrutiny point) |
| `:violates` | `fsd:ResidualObligation` → `fsd:LoopClosure` | I–IX | 11, Part VI, 10E | Mandamus + declaration + damages; loop closure registered | TD (enforcement architecture); think tank (comparative law novelty) |

---

## Part II — The Prohibited Practices and Their Instances

### Six Named Failure Modes

The Bill names six prohibited practices. Each has an FSD class, a Bill section, and a Charter article. The distinction between them is not merely taxonomic: each attracts different evidential and remedial consequences, and each maps differently to the three pathways.

**1. `fsd:RemitDisplacement` (Section 6)**
Referral to another body without naming it, identifying the legal basis for its competence, or ensuring it has received the submission. The functional core of the loop condition. Pathway relevance: the TD's Section 10B(3)(a) response to "why three bodies?" draws directly on this class — it is remit displacement that makes the three-body threshold necessary rather than arbitrary.

**2. `fsd:DeferralWithoutDestination` (Section 7)**
Indefinite postponement without a stated timeline or reviewable reason. Treated in the FSD Ontology as a variant of `fsd:RemitDisplacement` but warranting a standalone class given its distinct evidential signature: absence of a referral record (remit displacement leaves a trail; deferral without destination often does not). _Note: the FSD Ontology should add `fsd:DeferralWithoutDestination` as an explicit `fsd:ProhibitedPractice` subclass — currently absorbed into `fsd:NonDetermination`._

**3. `fsd:SufficiencyAssertion` (Section 8)**
Claiming closure without evaluating the specific submission — asserting, in effect, that enough has been done to satisfy any obligation that might have arisen. Blocked for testable submissions by SWRL Rule 5: where a submission is testable, no sufficiency assertion is lawful without the testing opportunity having been provided (Sections 5A–5C). Pathway relevance for the think tank: this is one of the genuinely novel legal categories — "sufficiency assertion" does not exist as a defined concept in Irish or EU administrative law; it is a contribution of the Bill's drafting.

**4. `fsd:ForeClosureByProxy` (Section 8A)**
The most legally precise characterisation of the most recent institutional act in the record. A purported determination by a body that: (i) did not hold the competent authority designation at the time of submission; (ii) relies exclusively on conclusions of a body that also lacked CA designation; and (iii) does not engage formally rebutted conclusions. Named instance: **DOD-MO-01201-2025**, 4 February 2026. This is the clearest single instantiation of `:violates` in the entire corpus. Pathway relevance: the TD who has read the Technical Annex should know this provision exists and why Section 8A is not drafting excess — the McEntee Foreclosure is the provision's direct motivation.

_Structural accountability note (audit Layer 4):_ The ForeClosureByProxy argument is strengthened by the **McEntee dual portfolio** — DFA and Defence were held simultaneously from November 2025. The body issuing the Foreclosure (DoD, 4 February 2026) was under the portfolio of the minister simultaneously holding the CA function's predecessor ministry (DFA). This structural coupling — documented in the audit as STRONG — means the designation gap was not incidental: the minister who held the competent authority function also held the issuing body's portfolio at the moment of issue. The TD should have this chronology available; it is the accountability nexus that makes the ForeClosureByProxy argument more than a technical jurisdictional point.

**5. `fsd:AdministrativeAmnesia` (Section 10A(1))**
Passive reset: successive officers encounter a submission as if for the first time, without awareness of prior engagement, producing fresh cycles of superficial closure. Evidential signature: absence of cross-referencing across file records. Distinct from `fsd:DesignedForgetting` in that intent is not required — the amnesia can be structural rather than deliberate.

**6. `fsd:DesignedForgetting` (Section 10)**
Active: deliberate destruction or rendering inaccessible of formally lodged correspondence. Named instance: JCEUA deletion, October 2025. Engages Art. 41 CFR right of access to file directly. Breach per se: destruction of a qualifying submission record is not subject to the reasonableness standard applicable to other failures — it is unlawful on its face. Pathway relevance: the think tank's novelty claim is strongest here — "designed forgetting" as a defined legal category does not appear in any existing European legal ontology.

### Competent Authority Transition — The Date That Matters

The FSD Ontology records the competent authority handover with precision:
- **DFA**: designated competent authority **2009 – 22 August 2024**
- **DETE**: designated competent authority **from 22 August 2024**

This date is legally significant for all three pathways:
- **TD**: Section 13 (retrospective provision) requires DETE to audit and determine submissions received by DFA before 22 August 2024 within 6 months of commencement. A sponsor pressed on retrospective effect should have this date and its legal basis ready. Note also that the handover gap is not fully resolved in the evidentiary record — the audit marks the DFA 26-year span node as PARTIAL, not STRONG, precisely because the transition produced a period in which neither body had taken formal ownership of the in-tray. This is an open finding, not merely a dateable legal transition.
- **Law reform**: The transition gap is itself a `fsd:StructuralDisplacement` instance. The LRC consultation on non-court adjudicative bodies is the place to document it.
- **Think tank**: The transition date is the factual anchor for the comparative claim — French *loi du silence* reform (2013) addresses exactly the period between submission and the competent body recognising itself as such. The Irish gap straddled a machinery-of-government change, which is a harder case than the French statutory one.

_OI-01 dependency:_ The dual-use characterisation of the O.R. corpus (Wassenaar Cat 4.E.1) — which underpins the Charter Art. III/V analysis and the Bill Section 3(2A) assessment obligation — is marked NEEDS WORK in the audit, pending **OI-01: Hypothesis C** (the epistemic failure argument from the OEP contradiction). Until OI-01 is resolved, claims that proceed from "this is a dual-use item" rest on an asserted rather than proved foundation. Every pathway that relies on the dual-use characterisation should be understood to carry this caveat.

---

## Part III — Pathways to Adoption, Read Against the Mapping

### Valence Note

The pathways document and the mapping document operate in different planes and address different audiences — but they are arguing the same structural claim by different means. The table below names the valence point for each pathway: the specific place where the structural diagnosis in the mapping becomes the argument the pathway needs.

| Pathway | Primary Layer | Structural Condition at the Centre | FSD Class Most Relevant | Key Tension |
|---|---|---|---|---|
| Sponsoring TD / Senator | Layer 2 (Bill sections) | `fsd:SilenceVeto` and `fsd:LoopCondition` | `fsd:ResidualObligation` | Section 10C objection: Ombudsman's mandatory mandamus function touches constitutional independence |
| Law Reform Commission | Layer 1 (Charter/diagnosis) | `fsd:StructuralDisplacement` and `fsd:OnticCollapse` | `fsd:NormativeCollapse` | The submission must diagnose, not advocate: the four-category frame, not the Bill's specific sections |
| Think Tank Placement | Diagnostic gap (between Layers 1 and 2) | `fsd:NormativeCollapse` as comparative claim | `fsd:DesignedForgetting` · `fsd:ForeClosureByProxy` | The illustrative case must not travel with the pitch: the novelty is in the categories, not the corpus |

---

### Pathway A — For a Sponsoring TD or Senator

**What the mapping tells this audience**

The Bill's general duty-to-determine provisions (Sections 3(1), 3(2), 2A) track existing administrative law principles closely enough to be a hard target for a government objection. The scrutiny will concentrate on Section 10C — the mandatory mandamus function conferred on the Ombudsman — which has no equivalent in the Ombudsman Act 1980. The mapping explains why this provision is structurally necessary: where `fsd:OnticCollapse` is found — no body holds full competence, no mechanism assembles partial competences — the loop condition cannot be resolved by mandating any single receiving body, because the problem is not that any one body refuses to act. It is that no body is capable of acting alone. The Ombudsman's residual determination duty is the minimum legislative intervention required to convert `fsd:ResidualObligation` into `fsd:LoopClosure`.

The sponsor should be briefed to make this argument affirmatively, rather than to defend Section 10C as a necessary exception. The provision is not anomalous — it fills a structural gap that existing legislation does not address and cannot address without a new assembly mechanism.

**Section 10B(3)(a) — the three-body threshold**

The pathways document flags this as the provision a sponsor should have ready. The mapping explains why it is drawn where it is: the three-body threshold corresponds to the minimum number of `fsd:RemitDisplacement` instances required to establish a `fsd:NullificationLoop` as a structural condition rather than an isolated failure. A threshold of one or two would capture ordinary referral behaviour; three captures the pattern — repeated, cross-body, without determination — that the Bill defines as a prohibited loop. The sub-provision counting a department's internal declinations separately after twelve months closes the gap that would otherwise allow a single non-cooperating department to remain permanently outside the loop condition's reach.

**The Technical Annex — what the sponsor should and should not say**

The sponsor is not asked to defend the illustrative case, and should say so plainly if pressed. The mapping makes visible what the sponsor can say instead: the general provisions are independently grounded. The SWRL Rules applied to the existing record produce instantiations of every named prohibited practice (Rules 1–6), but the Bill's operative provisions do not depend on that record. The Annex is evidence that the loop condition the Bill targets is not hypothetical — it exists, it is documented, it is live. That is all the sponsor needs it to be.

**The Gunn Letter — the time-sensitive operative act (URGENT)**

The audit identifies the **Gunn Letter** (24 February 2026) as a fresh, independently reviewable act, marked STRONG and currently within the 12-month judicial review window. That window closes **February 2027**. This is the single most time-sensitive item in the entire corpus and is the operative trigger for the High Court judicial review track — not the original 2006 submission, which is out of time as a standalone reviewable act. The sponsoring TD and any solicitor briefed on the Bill should treat February 2027 as a hard deadline. The Gunn Letter's existence means the judicial review track is live now; it will not be live after that date without a further reviewable act. The Bill's enactment would provide a statutory route independent of the judicial review window, but that route depends on a sponsor being in place before the window closes.

**OI-02 — JCPP structural conflict (the specific Section 10C vulnerability)**

The audit marks the Ombudsman track as RISK — the specific risk being **OI-02: JCPP structural conflict**. The Joint Committee on the Public Petitions and Parliamentary and Constitutional Affairs may act simultaneously as respondent (having received the submission and declined it) and as the oversight body for the Ombudsman track. This is a structural conflict of interest more precise than the general constitutional independence objection. A sponsor pressed on Section 10C should be ready to name OI-02 by its structure: the objection is not that the Ombudsman is given a new function, but that the Committee which scrutinises the Ombudsman may be the same body whose non-determination triggered the Ombudsman's jurisdiction. The Bill's answer is Section 10D — the Ombudsman's referral goes to the High Court, not back to the Committee — which structurally resolves the conflict.

**Seanad v4 — a concurrent and active instrument**

The audit marks the Seanad v4 submission as ACTIVE — response pending, Option A/B strategy live, McDowell as potential witness. This is a parallel escalation track running alongside any Private Members' Bill introduction, not a substitute for it. The Seanad submission operates in a different chamber on a different timeline and creates a distinct parliamentary record. A sponsoring TD should be aware that a Seanad v4 response may arrive while the Bill is at First or Second Stage — that response, whatever its content, becomes part of the public record on which Committee Stage scrutiny will draw. The Option A/B structure of the Seanad submission (the audit does not reproduce its terms) should be understood before the sponsor agrees to introduce — particularly if Option A involves a commitment the government has not yet responded to.

**The Financial Resolution question**

No Financial Resolution is required at introduction. The mapping's enforcement chain terminates at `fsd:LoopClosure` on the Ombudsman's public register (Section 10E), which requires resources. A Financial Resolution becomes relevant at Committee Stage or later, when the question of Ombudsman resourcing under Part VI (Sections 10A–10E) arises. The sponsor should not pre-empt this at introduction, but should be ready to say that the Bill's residual determination obligation is scoped — it applies only where a `fsd:LoopCondition` has been established, which the SWRL rules define precisely, not to the general run of Ombudsman business.

---

### Pathway B — For a Law Reform Commission Submission

**What the mapping tells this audience**

The Commission's live project — _Reform of Non-Court Adjudicative Bodies and Appeals to Courts_ — is the correct entry point. The mapping's four structural conditions are the submission's primary analytical contribution: they show that the failure pattern the Commission is studying is not reducible to procedural inefficiency in individual bodies, but arises from a structural architecture gap that procedural reform of individual bodies cannot address.

`fsd:StructuralDisplacement` makes this argument most precisely: where required competence is distributed across multiple bodies with no statutory coordination mechanism, no reform of any individual body's procedures can produce a `fsd:Determination`. The reform needed is at the level of architecture — either a new coordination mechanism, or a residual determination authority (as the Bill provides through the Ombudsman's Part VI function).

`fsd:OnticCollapse` makes the strongest version of the argument: in the limiting case, there is no institutional subject to reform. No streamlining of the Ombudsman's procedures, no appeal reform, no case-management improvement addresses a situation in which the legal obligation is distributed in fractions across bodies with no mechanism to add the fractions to one.

**What not to submit**

The pathways document is precise on this: do not submit the Bill as though the Commission were a legislative body. The mapping supports this — the submission should offer the four-category failure frame (remit displacement, sufficiency assertion, administrative amnesia, loss of the administrative record — the four classes that are demonstrably `fsd:ProhibitedPractice` instances in the existing Irish record) as evidence relevant to the Commission's own research question. The Bill is one possible legislative response; the Commission's own project may develop others. The submission's credibility depends on not conflating the diagnosis with the particular legislative remedy.

**The France comparison as LRC material**

The Extended Introduction's France comparison is the submission's opening frame. The mapping's `fsd:NormativeCollapse` is the reason why the France comparison holds: French *loi du silence* reform (2013) confronted the same structural condition — procedurally valid non-responses producing a self-sustaining gap between form and substance. The French resolution (default acceptance with sectoral exceptions) is one legislative architecture; the Bill's residual determination model is another. The Commission's project is the right venue to evaluate the comparative options, since it is not bound to any particular legislative form.

---

### Pathway C — For a Think Tank Placement

**What the mapping tells this audience**

The publishable claim is the novelty of the named failure mode categories. The mapping makes this concrete: `fsd:NormativeCollapse`, `fsd:SilenceVeto`, `fsd:DesignedForgetting`, and `fsd:ForeClosureByProxy` do not exist as defined legal categories in any existing European legal ontology (FSD-Ontology-2026, Section 8 blank cells). The Bill's drafting has produced, as a by-product of working through a specific case, a taxonomy of failure modes that has general application. That taxonomy is the publishable contribution — not the case, not the Bill, not the corpus.

The strongest single passage for this audience remains the France comparison at Section V of the Extended Introduction, read alongside the support brief's Section VIII. The mapping's `fsd:OnticCollapse` is what the comparison is ultimately about: the *ping-pong administratif* condition in French law is the same structural state — no body holds the aggregate duty — reached by a different institutional route. The Irish case reaches it through a machinery-of-government change straddling a CA transition; the French case reaches it through jurisdictional fragmentation in complex licensing matters. The structural condition is the same; the legislative response differs. That is a publishable comparative claim.

**The framing discipline**

The pathways document is explicit: the Technical Annex's illustrative case should not travel with the pitch. The mapping explains why this discipline matters structurally, not merely rhetorically: the four structural conditions and the five causal operators in the mapping are general — they describe a class of institutional failure that recurs across jurisdictions and subject matters. The moment the illustrative case is introduced, the general claim collapses into a specific one. The pitch sells the class; the Annex is evidence that the class is non-empty. That is the correct order.

_Presidency overstatement risk (audit finding, FRAMING RISK):_ The EU Council Presidency dimension — Ireland's Presidency from 1 July 2026 — appears in the pathways document as a comparative and strategic frame. The audit has explicitly logged this as a **FRAMING RISK**: the Presidency is a political context, not a legal ground. A think tank piece that implies the Presidency creates a legal obligation or a justiciable deadline overstates the case and exposes the piece to a credibility objection that a specialist reader will make immediately. The Presidency framing is available as a policy window note — not as a legal claim. The structural conditions (NormativeCollapse, SilenceVeto, StructuralDisplacement, OnticCollapse) are the legal claim; the Presidency is context. The pitch should never reverse that order.

_McGrath Dimension as concrete prior knowledge instance:_ The audit marks the **McGrath Dimension** (TD in 2020, EU Commissioner in 2026, prior knowledge of the matter documented across the transition) as STRONG. For a think tank piece arguing that institutional prior knowledge is not merely asserted but provable from public record, this is a concrete and verifiable instance. It does not require importing the illustrative case — the transition from TD to Commissioner is a matter of public record and the relevant correspondence is documented. A piece that argues for the general proposition that institutional prior knowledge creates accountability exposure can cite this class of case without naming the submission. The Dimension's value to the think tank is structural: it demonstrates that prior knowledge survives machinery-of-government changes, which is the claim that makes the comparative EU law analysis most generative.

**`fsd:ForeClosureByProxy` as the most novel category**

The think tank audience interested in governance and administrative law will find `fsd:ForeClosureByProxy` the most analytically novel of the six named failure modes. It identifies a failure pattern — a purported determination by a body that never held the required designation, relying on conclusions of a body that also lacked it — that is both legally precise and practically common in complex multi-body licensing regimes. It is common precisely because it is invisible: from the outside, a letter from a ministry looks like a determination regardless of whether that ministry held the CA designation. The Bill's Section 8A makes the invisible visible by attaching legal consequences to the designation gap. This is the kind of analytic contribution a law and governance think tank will want to publish — not as a critique of any particular government, but as a structural observation about complex regulatory architectures.

---

## Part IV — The Enforcement Chain, Read Against Each Pathway

The enforcement chain below is annotated to show which elements are relevant to each pathway's argument, and at which stage.

```
Qualifying Submission (fsd:SubmissionOfNationalUtility)
    ↓
Received by Public Body (fsd:hasReceivingBody)
    │
    │  ⚠ PARALLEL TRACK — TIME-SENSITIVE
    │  Gunn Letter (24 Feb 2026) = fresh independently reviewable act
    │  Judicial review window closes: February 2027
    │  This is the operative trigger for the High Court track NOW,
    │  independent of the Bill's enactment timeline.
    │  TD: the JR window is the hard deadline; the Bill is the structural fix.
    ↓
Section 3(1): Duty to Determine within 12 months
    │
    ├─ ACCEPT & EVALUATE  →  fsd:AcceptanceDetermination
    │     TD: the normal case the Bill enables; no Financial Resolution needed
    │
    ├─ REJECT WITH REASONS  →  fsd:RejectionDetermination
    │     TD: reviewable; grounds the judicial review track at Section 11
    │
    ├─ REFER TO NAMED CA BODY  →  fsd:ReferralDetermination
    │     LRC: the point at which existing procedural reform runs out — naming
    │          the body and the legal basis is what current practice does not require
    │
    └─ NONE OF ABOVE  →  fsd:NonDetermination
                │
                ↓     [fsd:SilenceVeto activated — Section 2A]
                │     Think tank: this is the SilenceVeto category — the unnoticed
                │     adverse determination that no existing legal framework names
                │
        Section 10A: Tracking obligation breach
                │     TD: Section 10B(3)(a) applies here — internal declinations
                │     counted separately after 12 months
                │
        Section 10B: fsd:LoopCondition (SWRL Rules 2 or 3)
                │     LRC: this is fsd:NormativeCollapse in its most concrete form —
                │     a formally-operating process producing no substantive output
                │
        Part VI: fsd:ResidualObligation vested in fsd:Ombudsman
                │     TD: the Section 10C scrutiny point — address proactively;
                │     fsd:OnticCollapse is why this provision cannot be weaker
                │
        Section 10C(3)(b): Ombudsman identifies fsd:StructuralCondition(s)
                │     LRC: fsd:StructuralDisplacement / fsd:OnticCollapse finding —
                │     the diagnosis the LRC submission seeks to surface
                │
        Section 10D: Non-compliance → High Court mandamus (Section 11)
                │     Think tank: fsd:ForeClosureByProxy would be voided here —
                │     declaration that purported determination is null
                │
        High Court: Mandamus · Declaration · Damages · Protective Costs
                │
        Section 10E: fsd:LoopClosure entered on Ombudsman's public register
                      All pathways: this is the endpoint the Bill is designed to reach.
                      fsd:NormativeCollapse terminated. Procedure has produced substance.
```

---

## Part V — Tensions Between the Documents

These are the points where the mapping and the pathways documents pull in different directions. Naming them is more useful than resolving them prematurely.

### Tension 1: Specificity vs Generality

The mapping document works by specification: every failure mode has a named FSD class, a Bill section, and a Charter article. The pathways document works by deliberate abstraction: the think tank pitch must not import the specific corpus; the LRC submission must not read as a request to endorse specific legislation. The tension is between the corpus's specificity — which is what makes the mapping's claims verifiable — and the general framing each pathway requires for credibility.

_Resolution: the four structural conditions (Part I above) are where the two documents meet. They are specific enough to be verifiable (established by reference to statutory architecture alone, not by conduct or contested facts) and general enough to carry a comparative or law-reform argument. The structural conditions are the translation layer between the mapping and the pathways._

### Tension 2: The Technical Annex's Role

The mapping's SWRL Rules table shows that every Rule instantiates on the existing record — the loop condition is not hypothetical. The pathways document says the Annex should not travel with the think tank pitch. These are not contradictory: the SWRL table demonstrates that the abstract categories are non-empty; the pathways discipline prevents that demonstration from narrowing the general claim. The Annex's role is evidentiary, not argumentative.

_For the TD: the Annex is the sponsor's due diligence material, establishing that the problem the Bill addresses is live and documented. It is not the sponsor's public argument._  
_For the LRC: the Annex is the submission's footnote — acknowledging the analysis originates from engagement with a live case, without importing the case._  
_For the think tank: the Annex does not travel with the pitch. It may appear in a footnote of the eventual piece, noting that the taxonomy was developed in the context of a documented Irish case, without details._

### Tension 3: Section 10C and the Ombudsman's Constitutional Position

The mapping identifies Section 10C — the mandatory mandamus function — as the provision most likely to attract a government objection. The pathways document says the same, and advises the sponsor to be briefed on it. But the mapping's explanation of why the provision is structurally necessary (because `fsd:OnticCollapse` means no single receiving body can discharge the obligation) is a structural argument, not a political one. The political objection — that the provision touches the Ombudsman's constitutional independence — is a different register.

_Resolution: the sponsor needs both arguments. The structural argument (from the mapping) explains why no weaker provision would achieve `fsd:LoopClosure`. The constitutional argument (from the pathways) explains why the provision's scope is appropriate: the mandatory function is triggered only by a `fsd:LoopCondition` (SWRL Rules 2 or 3), not by general non-determination, and the Ombudsman's determination is itself a reasoned act subject to High Court review under Section 10D. The mandatory function is narrow; the constitutional concern is answerable._

### Tension 4: The France Comparison's Reach

The pathways document uses the France comparison as the think tank's opening frame and as comparative law material for the LRC. The mapping's `fsd:OnticCollapse` is the structural condition both comparisons address. But the French reform (default acceptance, 2013) resolves ontic collapse differently from the Bill's residual determination model (Ombudsman as assembly mechanism). The comparison holds at the level of diagnosis; it does not hold at the level of remedy.

_Resolution: be precise about where the comparison stops. The think tank piece's comparative claim is: both jurisdictions have identified the same structural condition; they have chosen different legislative architectures to address it; the choice between architectures is not resolved by the comparison. That framing is more credible than one that implies the French model should be adopted, and it positions the Bill as a genuinely distinct legislative contribution rather than an import._

### Tension 5: The Presidency Framing — Policy Window vs Legal Ground

The Presidency dimension appears in both source documents as a strategic amplifier — a reason why the moment is particularly propitious. The audit has logged it as a FRAMING RISK (overstatement). The tension is between two legitimate uses: as a policy-window argument (the Presidency creates visibility and political incentive) and as a legal ground (the Presidency creates justiciable obligations). Only the first is defensible. The merged document uses the Presidency framing in the context of the think tank pitch and the EU submission without clearly marking this boundary.

_Resolution: in any external use of this document, the Presidency is a policy window. It is not a source of legal obligation independent of the Treaty provisions already identified (Art. 2 TEU, Reg 2021/821 Art. 23(2), EUCFR Art. 41). Stating it as a policy window — "the Presidency creates political incentive and visibility; the legal obligation exists regardless of the Presidency" — is both more accurate and more credible to a specialist audience than treating it as a legal accelerant._

### Tension 6: The Gunn Letter's Urgency vs the Document's Timelessness

The merged document is designed to be a durable working instrument — the structural analysis does not expire. But the Gunn Letter creates a hard deadline (February 2027 judicial review window) that sits in tension with a document written to outlast any particular parliamentary cycle. The time-sensitive element and the timeless structural analysis need to be legible as separate registers.

_Resolution: the Gunn Letter section in Pathway A is marked URGENT precisely to signal that it is time-indexed in a way the rest of the document is not. Readers of this document after February 2027 should treat the Gunn Letter section as a historical record of the operative act that was live at the time of writing, not as a current action item. The structural analysis in Parts I–II and the enforcement chain in Part IV remain valid regardless of whether the judicial review window closes._

---

## Part VI — Reference Tables

### OWL Relations, FSD Classes, Charter Articles, Bill Sections, Pathways

| OWL Relation | FSD Class(es) | Charter Art. | Bill Section | Pathway A (TD) | Pathway B (LRC) | Pathway C (Think Tank) |
|---|---|---|---|---|---|---|
| `:ignores` | `fsd:NonDetermination` · `fsd:SilenceVeto` | I, IV | 3(1), 2A | Core provision; defensible | Key LRC diagnostic | SilenceVeto as novel category |
| `:suppresses` | `fsd:DesignedForgetting` · `fsd:AdministrativeAmnesia` | III, V, VI | 10, 9, 5A–5C | Section 10 defence | Four-category frame | DesignedForgetting novelty |
| `:producesFailure` | `fsd:NullificationLoop` · `fsd:NormativeCollapse` · `fsd:ForeClosureByProxy` | II, VI | 6, 7, 8, 8A, 2B | 10B(3)(a) briefing | NormativeCollapse diagnosis | ForeClosureByProxy novelty |
| `:triggers` | `fsd:LoopCondition` · `fsd:StructuralDisplacement` · `fsd:OnticCollapse` | IV, VII | 10A, 10B, 3(2)(c) | Section 10C argument | Non-court bodies project | Ontic collapse comparator |
| `:violates` | `fsd:ResidualObligation` → `fsd:LoopClosure` | I–IX | 11, Part VI, 10E | Enforcement architecture | Commission recommendation scope | Comparative remedy choice |

### Supremacy Hierarchy

1. **Constitutional** (Bunreacht na hÉireann, Articles 40.3, 43, 45) — right to just administration; proprietary rights; common good
2. **EU Law** (EUCFR Art. 41; Regulations 2021/821, 2024/1689) — right to good administration; competent authority obligations; Art. 26 evaluation dossier enters irrespective of domestic proceedings
3. **Administrative Law** (natural justice, procedural fairness, duty to give reasons)
4. **Bill's Principle** (Section 2B: Procedural Closure) — `fsd:LoopClosure` is the registered endpoint; `fsd:NormativeCollapse` is what the Bill terminates

### SWRL Rules on the Existing Record

| Rule | FSD Instantiation on Existing Record | Pathway Relevance |
|---|---|---|
| Rule 1 (Non-Determination) | `fsd:submissionDate` Nov 2006; `fsd:determinationDeadline` Nov 2007; no `fsd:Determination` to date | TD due diligence; LRC evidence |
| Rule 2 (3 declinations) | Declination count exceeds threshold by factor of three | TD Section 10B(3)(a) briefing |
| Rule 3 (24 months) | `fsd:nonDeterminationPeriodMonths` ≈ 236 at date of FSD Ontology | Think tank: class is demonstrably non-empty |
| Rule 4 (Residual obligation) | Pre-legislative equivalent: OMB-260331-CSD014 | TD: Ombudsman track already exists in embryo |
| Rule 5 (Testable, sufficiency blocked) | `fsd:TestableSubmission` — sufficiency assertion unavailable without testing | LRC: SufficiencyAssertion as novel legal category |
| Rule 6 (Ontic Collapse) | CA function distributed across DETE, DFA, DoD; no statutory coordination mechanism | All pathways: the structural condition that makes the Bill's residual determination model necessary |

### Audit Nodes Not Captured by SWRL Rules

| Audit Node | Status | Relevance | Action Required |
|---|---|---|---|
| Gunn Letter (24 Feb 2026) | STRONG — fresh reviewable act; 12-month window | Pathway A: time-sensitive; judicial review track depends on this act | Window closes Feb 2027 — URGENT |
| McEntee dual portfolio (Nov 2025) | STRONG — structural coupling clear | Strengthens `fsd:ForeClosureByProxy`; accountability nexus for TD briefing | Add to Section 8A argument |
| McGrath Dimension (TD 2020 → Commissioner 2026) | STRONG — prior knowledge documented | Pathway A (CJEU briefing); Pathway C (institutional prior knowledge class) | Cite in Art. VII and CJEU section |
| Seanad v4 (Option A/B) | ACTIVE — response pending | Pathway A: concurrent parliamentary instrument; may arrive during Bill stages | Coordinate with Bill introduction timeline |
| Presidency Paradox | FRAMING RISK — overstatement logged | Pathway C: use as policy window only; not as legal ground | Remove or qualify all legal-ground framings |
| OI-01 (Hypothesis C) | Open — epistemic failure argument not drafted | Dual-use characterisation is conditional on this; affects Art. III/V claims | Caveat all dual-use assertions |
| OI-02 (JCPP conflict) | Open — Ombudsman track structural risk | Pathway A: Section 10C briefing; Section 10D is the answer | Name explicitly in sponsor briefing |

---

## Closing Note

The mapping and the pathways documents were written for different purposes and addressed to different readers. The mapping's reader needs to know what each provision proves. The pathways reader needs to know what each audience can do, and in what sequence. This merged document is addressed to the person who needs both — who is moving the Bill and also building the ontological record that will outlast any particular parliamentary cycle.

The structural diagnosis in Part I is what connects them. The four structural conditions and the five causal operators are not only the formal vocabulary of the FSD Ontology; they are the argument that each pathway, in its own register, is making. `fsd:NormativeCollapse` — the self-sustaining gap between governance form and governance substance — is the condition all three pathways are trying to terminate. Each terminates it differently: the TD through enactment, the LRC through Commission recommendation, the think tank through naming the gap so that it cannot be denied.

`fsd:LoopClosure` — entered on the Ombudsman's public register — is what all three pathways are working toward. It is registered termination. The loop is closed when it is on the record that it closed.
