# Qualifying Submissions (Duty to Determine) — OWL Ontology Framework
## FSD-Ontology-2026 · European Interoperability

---

## 1. Purpose and Scope

This document maps the legislative concepts of the Qualifying Submissions (Duty to Determine) Bill 2026 to a formal OWL 2 DL ontology, expressed in Turtle syntax. It is designed for compatibility with the following European and international frameworks:

| Framework | Role in this ontology |
|---|---|
| **LKIF** (Legal Knowledge Interchange Format, ESTRELLA/EU) | Core legal concepts: obligation, legal act, public body |
| **ELI** (European Legislation Identifier, Council Recommendation 2012/C 325/02) | Legislation identification and provenance |
| **SEMIC Core Public Service Vocabulary** (EU Publications Office) | PublicOrganisation, PublicService alignment |
| **Akoma Ntoso** (UN/OASIS, ISO 36016) | Document structure for determinations |
| **LegalRuleML** (W3C) | Rule encoding for loop condition logic |
| **SKOS** (W3C) | Concept scheme for the corpus lexicon |
| **Dublin Core / DCAT-AP** (EU) | Metadata and dataset description |
| **FOAF** (W3C) | Agent and person identification |
| **EIF** (European Interoperability Framework, COM(2017)134) | Interoperability layer alignment |

The ontology introduces the namespace `fsd:` for new concepts with no equivalent in existing legal ontologies. These are the ontology's genuine contributions — concepts the bill legislates into existence and that no prior framework has formalised.

---

## 2. Namespace Declarations

```turtle
@prefix fsd:    <https://meinhardt.gov/ontology/fsd/2026#> .
@prefix lkif:   <http://www.estrellaproject.org/lkif-core/lkif-core.owl#> .
@prefix eli:    <http://data.europa.eu/eli/ontology#> .
@prefix cpv:    <http://data.europa.eu/m8g/> .
@prefix skos:   <http://www.w3.org/2004/02/skos/core#> .
@prefix owl:    <http://www.w3.org/2002/07/owl#> .
@prefix rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix foaf:   <http://xmlns.com/foaf/0.1/> .
@prefix dcat:   <http://www.w3.org/ns/dcat#> .
@prefix legal:  <http://www.w3.org/ns/legal#> .
@prefix eu-reg: <http://data.europa.eu/eli/reg/> .
```

---

## 3. Ontology Declaration

```turtle
<https://meinhardt.gov/ontology/fsd/2026>
    a owl:Ontology ;
    dcterms:title "Qualifying Submissions (Duty to Determine) Ontology 2026"@en ,
                  "Ointlocht Aighneachtaí Foirmiúla (Dualgas Cinneadh a Dhéanamh) 2026"@ga ;
    dcterms:description """
        OWL 2 DL formalisation of the Qualifying Submissions (Duty to Determine)
        Bill 2026, mapping the duty of determination, prohibited administrative
        practices, structural failure conditions, and loop closure mechanisms
        to a machine-readable knowledge graph compatible with EU interoperability
        frameworks.
    """@en ;
    dcterms:creator [
        a foaf:Agent ;
        foaf:name "Meinhardt Initiative" ;
        foaf:homepage <https://dr-crunch.github.io/nullification-loops>
    ] ;
    dcterms:date "2026-07-24"^^xsd:date ;
    dcterms:language <http://publications.europa.eu/resource/authority/language/ENG> ,
                     <http://publications.europa.eu/resource/authority/language/GLE> ;
    owl:versionInfo "1.0.0" ;
    dcterms:conformsTo <https://www.w3.org/TR/owl2-profiles/#OWL_2_DL> ,
                       <https://joinup.ec.europa.eu/collection/semic-support-centre> ;
    eli:is_about <http://data.europa.eu/eli/reg/2021/821> ,
                 <http://data.europa.eu/eli/reg/2024/1689> .
```

---

## 4. Class Hierarchy

### 4.1 Core Submission Classes

```turtle
# ── Root class ──────────────────────────────────────────────────────────────

fsd:Submission
    a owl:Class ;
    rdfs:label "Submission"@en , "Aighneacht"@ga ;
    rdfs:comment """
        A formal written communication received by a public body that
        identifies the submitter, sets out material of potential national
        utility, and invites a determination or response.
    """@en ;
    rdfs:subClassOf lkif:LegalDocument ;
    owl:equivalentClass [
        a owl:Class ;
        owl:intersectionOf (
            lkif:LegalDocument
            [ a owl:Restriction ;
              owl:onProperty fsd:hasSubmitter ;
              owl:minCardinality "1"^^xsd:nonNegativeInteger ]
        )
    ] .

fsd:SubmissionOfNationalUtility
    a owl:Class ;
    rdfs:label "Submission of National Utility"@en ,
               "Aighneacht d'Úsáid Náisiúnta"@ga ;
    rdfs:comment """
        A submission satisfying the four-part test in s.2(1) of the Act:
        (a) addresses a matter of national significance;
        (b) expressly invokes the duty of determination;
        (c) is submitted by an identified natural or legal person; and
        (d) is lodged with a public body having a plausible connection to
            the subject matter.
        Saving provision: for retrospective cases, condition (b) is treated
        as satisfied if conditions (a), (c), and (d) are met.
    """@en ;
    rdfs:subClassOf fsd:Submission ;
    skos:broader fsd:Submission .

fsd:DualUseSubmission
    a owl:Class ;
    rdfs:label "Dual-Use Submission"@en ;
    rdfs:comment """
        A submission asserting dual-use characteristics within the meaning
        of Article 2(1) of Regulation (EU) 2021/821, triggering the
        Article 9(2) assessment obligation of the designated competent
        authority from the date of formal presentation.
    """@en ;
    rdfs:subClassOf fsd:SubmissionOfNationalUtility ;
    fsd:engagesRegulation <http://data.europa.eu/eli/reg/2021/821> .

fsd:HighRiskAISubmission
    a owl:Class ;
    rdfs:label "High-Risk AI Submission"@en ;
    rdfs:comment """
        A submission asserting that the submitted system constitutes or
        incorporates a high-risk AI system within the meaning of the AI Act
        (Regulation (EU) 2024/1689), engaging conformity assessment
        obligations under Articles 9, 13, 14, and 27.
    """@en ;
    rdfs:subClassOf fsd:SubmissionOfNationalUtility ;
    fsd:engagesRegulation <http://data.europa.eu/eli/reg/2024/1689> .

fsd:TestableSubmission
    a owl:Class ;
    rdfs:label "Testable Submission"@en ;
    rdfs:comment """
        A submission including an operational, executable, or otherwise
        empirically testable component in respect of which the submitter
        has offered a means of testing. Triggers s.5A obligations.
        A sufficiency assertion is not available in response without
        prior arrangement of a testing opportunity.
    """@en ;
    rdfs:subClassOf fsd:SubmissionOfNationalUtility .
```

### 4.2 Institutional Classes

```turtle
fsd:PublicBody
    a owl:Class ;
    rdfs:label "Public Body"@en , "Comhlacht Poiblí"@ga ;
    rdfs:subClassOf cpv:PublicOrganisation ;
    rdfs:subClassOf lkif:PublicBody ;
    rdfs:comment """
        Any body designated under Irish statute or EU regulation as
        bearing a determination obligation in respect of submissions
        of national utility. Includes ministers, departments, statutory
        bodies, Oireachtas clerks (subject to Art. 15 savings), and
        designated competent authorities.
    """@en .

fsd:CompetentAuthority
    a owl:Class ;
    rdfs:label "Competent Authority"@en , "Údarás Inniúil"@ga ;
    rdfs:subClassOf fsd:PublicBody ;
    rdfs:comment """
        The body designated under Article 9(1) of Regulation (EU) 2021/821
        to control exports, brokering, technical assistance, transit and
        transfer of dual-use items. Required by Article 9(2) to maintain
        and exercise the capacity to assess items formally brought to its
        attention. In Ireland: DFA 2009–2024-08-22; DETE from 2024-08-22.
    """@en .

fsd:Ombudsman
    a owl:Class ;
    rdfs:label "Ombudsman"@en , "Ombudsman"@ga ;
    rdfs:subClassOf fsd:PublicBody ;
    rdfs:comment """
        The residual determination authority under Part VI of the Act.
        On establishment of the loop condition under s.10B, the Ombudsman
        holds the obligation to investigate, report, and apply to the
        High Court for an order compelling a determination.
    """@en .

fsd:IndependentAuditor
    a owl:Class ;
    rdfs:label "Independent Technical Auditor"@en ;
    rdfs:subClassOf foaf:Agent ;
    rdfs:comment """
        A qualified person appointed under s.5C to conduct an independent
        technical audit of a testable submission. Must satisfy independence
        conditions under s.5B: no financial, contractual, or institutional
        relationship with a party whose interests could be affected by the
        audit outcome.
    """@en .
```

### 4.3 Determination Classes

```turtle
fsd:Determination
    a owl:Class ;
    rdfs:label "Determination"@en , "Cinneadh"@ga ;
    rdfs:comment """
        A written administrative act issued by a public body in response
        to a submission of national utility. Must take one of three forms:
        acceptance, rejection with reasons, or referral with stated legal
        basis. Silence, acknowledgement, and sufficiency assertion are
        each expressly excluded from this class by s.3(3).
    """@en ;
    rdfs:subClassOf lkif:LegalAct ;
    rdfs:subClassOf cpv:PublicService ;
    owl:disjointWith fsd:NonDetermination .

fsd:AcceptanceDetermination
    a owl:Class ;
    rdfs:label "Acceptance Determination"@en ;
    rdfs:subClassOf fsd:Determination ;
    rdfs:comment """
        A determination accepting a submission and initiating a statutory
        evaluation process (s.2(1)(a) of the Act).
    """@en .

fsd:RejectionDetermination
    a owl:Class ;
    rdfs:label "Rejection Determination"@en ;
    rdfs:subClassOf fsd:Determination ;
    rdfs:comment """
        A determination rejecting a submission with specific and
        attributable reasons capable of review by a court or tribunal
        (s.2(1)(b) of the Act). Must engage the specific submitted
        corpus — generic domain familiarity does not satisfy this class.
    """@en .

fsd:ReferralDetermination
    a owl:Class ;
    rdfs:label "Referral Determination"@en ;
    rdfs:subClassOf fsd:Determination ;
    rdfs:comment """
        A determination referring a submission to a named competent body
        with a stated legal basis for the referral (s.2(1)(c) and s.4
        of the Act). The referring body's obligation terminates on
        transmission; the receiving body's 12-month clock commences.
    """@en .

fsd:NonDetermination
    a owl:Class ;
    rdfs:label "Non-Determination"@en , "Neamh-Chinneadh"@ga ;
    rdfs:comment """
        The condition in which a public body has received a submission of
        national utility but has not issued a determination within the
        period prescribed by s.3(1). Established regardless of the form
        of the body's conduct — silence, acknowledgement, sufficiency
        assertion, and administrative amnesia each instantiate this class.
    """@en ;
    owl:disjointWith fsd:Determination .
```

### 4.4 Prohibited Practices

```turtle
fsd:ProhibitedPractice
    a owl:Class ;
    rdfs:label "Prohibited Practice"@en , "Cleachtas Toirmiscthe"@ga ;
    rdfs:comment """
        The superclass of the five administrative practices prohibited by
        Parts II and III of the Act. Each is a categorically wrong act
        performed in place of the categorically required one. None
        constitutes a lesser form of determination — each is a
        qualitatively different act that the Act declares incapable of
        satisfying the duty under s.3.
    """@en .

fsd:RemitDisplacement
    a owl:Class ;
    rdfs:label "Remit Displacement"@en , "Easú Remit"@ga ;
    rdfs:subClassOf fsd:ProhibitedPractice ;
    rdfs:comment """
        The practice of characterising a submission as falling outside
        the receiving body's remit without: (a) identifying the body
        to which remit is displaced; (b) transmitting the submission
        to that body within 30 days; or (c) notifying the submitter.
        Prohibited by s.4. Distinct from lawful referral, which satisfies
        the duty; remit displacement does not.
    """@en .

fsd:SufficiencyAssertion
    a owl:Class ;
    rdfs:label "Sufficiency Assertion"@en , "Maíomh Leordhóthanachta"@ga ;
    rdfs:subClassOf fsd:ProhibitedPractice ;
    rdfs:comment """
        An assertion, by a public body, that existing capacity, practice,
        or provision in the relevant domain is sufficient to address the
        subject matter of the submission — issued without evaluation of
        the specific submitted corpus against the applicable statutory
        framework. The three-part test: (a) claims adequacy of existing
        provision; (b) does not engage the specific submission on its own
        terms; (c) is issued in purported satisfaction of the s.3 duty.
        Prohibited by s.5.
    """@en .

fsd:AdministrativeAmnesia
    a owl:Class ;
    rdfs:label "Administrative Amnesia"@en , "Ainnéis Riaracháin"@ga ;
    rdfs:subClassOf fsd:ProhibitedPractice ;
    rdfs:comment """
        The structural condition in which a public body or successive
        officers of that body encounter a submission as if for the first
        time, without awareness of prior engagement, commitments, or
        accumulated obligation in respect of the same submission or
        submitter. Produces fresh cycles of superficial closure.
        Prohibited by s.6. Distinct from designed forgetting: amnesia
        is passive reset; forgetting is active deletion.
    """@en .

fsd:DesignedForgetting
    a owl:Class ;
    rdfs:label "Designed Forgetting"@en , "Dearmad Deartha"@ga ;
    rdfs:subClassOf fsd:ProhibitedPractice ;
    rdfs:comment """
        The active deletion, destruction, or rendering inaccessible of
        formally lodged correspondence relating to a submission of national
        utility, without: (a) issuing a determination; (b) transmitting
        to a competent body; or (c) placing on the formal record.
        Prohibited by s.7. Engages the right of access to file under
        Art. 41 CFR directly. Named practice in the record: JCEUA
        deletion, October 2025.
    """@en .

fsd:ForeClosureByProxy
    a owl:Class ;
    rdfs:label "Foreclosure by Proxy"@en , "Dúnadh trí Sheachvótáil"@ga ;
    rdfs:subClassOf fsd:ProhibitedPractice ;
    rdfs:comment """
        The acute form of non-determination: a purported determination
        issued by a body that: (a) did not hold the competent authority
        designation at the time of submission; (b) relies exclusively on
        conclusions of a body that also did not hold the CA designation;
        and (c) does not engage formally rebutted conclusions. Covered
        by s.8A of the Act. Named instance in the record: DOD-MO-01201-
        2025, February 4th 2026.
    """@en .
```

### 4.5 Structural Failure Conditions

```turtle
fsd:StructuralCondition
    a owl:Class ;
    rdfs:label "Structural Condition"@en , "Coinníoll Struchtúrach"@ga ;
    rdfs:comment """
        A systemic condition affecting the capacity of a public body or
        system of bodies to discharge the duty of determination. Four
        conditions are defined by s.2A of the Act. Each may produce or
        sustain the others; none is mutually exclusive.
    """@en .

fsd:NormativeCollapse
    a owl:Class ;
    rdfs:label "Normative Collapse"@en , "Clis Normach"@ga ;
    rdfs:subClassOf fsd:StructuralCondition ;
    rdfs:comment """
        The condition in which a public body or system of bodies produces
        procedurally valid outputs — acknowledgements, referrals,
        sufficiency assertions, declinations — while systematically failing
        to discharge the substantive obligation those forms purport to
        represent. The gap between governance form and governance substance
        is structural and self-sustaining, not incidental. Defined in
        s.2(1) and s.2A(2)(a) of the Act.
    """@en .

fsd:SilenceVeto
    a owl:Class ;
    rdfs:label "Silence Veto"@en , "Veto Tosta"@ga ;
    rdfs:subClassOf fsd:StructuralCondition ;
    rdfs:comment """
        The condition in which procedural silence functions as a
        substantive adverse determination, leaving the submitter without
        a reviewable outcome, without notice, and without hearing.
        Established without proof of intent: the test is practical effect,
        not motivation. Engages Art. 41 CFR (right to be heard; obligation
        to give reasons) and Re Haughey [1971] (audi alteram partem).
        Defined in s.2(1) and s.2A(2)(b) of the Act.
    """@en .

fsd:StructuralDisplacement
    a owl:Class ;
    rdfs:label "Structural Displacement"@en , "Easú Struchtúrach"@ga ;
    rdfs:subClassOf fsd:StructuralCondition ;
    rdfs:comment """
        The condition in which the statutory architecture governing the
        relevant bodies distributes the components of the required
        competence across multiple bodies without a coordination
        mechanism capable of assembling them into a body able to issue
        a determination. Established by reference to the statutory
        architecture — no proof of coordination between bodies or
        individual awareness is required. Defined in s.2A(2)(c) of
        the Act.
    """@en .

fsd:OnticCollapse
    a owl:Class ;
    rdfs:label "Ontic Collapse"@en , "Clis Ontach"@ga ;
    rdfs:subClassOf fsd:StructuralDisplacement ;
    rdfs:comment """
        The most acute form of structural displacement. The institutional
        capacity required to discharge a statutory obligation has ceased
        to exist within the public body architecture: (a) no single body
        holds the full competence required; and (b) no statutory mechanism
        assembles the partial competences held by separate bodies. The
        obligation cannot be discharged not by reason of refusal but by
        reason of the absence of an institutional subject capable of
        performing the required act. A finding of ontic collapse
        identifies the level of intervention — legislative or executive
        — required to reconstitute the competent authority function.
        Defined in s.2(1) and s.2A(1A) of the Act.
    """@en .
```

### 4.6 Loop Architecture

```turtle
fsd:NullificationLoop
    a owl:Class ;
    rdfs:label "Nullification Loop"@en , "Lúba Neamhnithe"@ga ;
    rdfs:comment """
        The five-stage structural attractor producing non-determination
        regardless of personnel: (1) Acknowledgement; (2) Deferral;
        (3) Remit Displacement; (4) Sufficiency Assertion;
        (5) Record Suppression. Output invariant: no determination.
        The Loop is personnel-independent and has operated through
        successive administrations without change of output.
        Not a class of act but a pattern of acts — identified by
        aggregate conduct, not any single instance.
    """@en .

fsd:LoopCondition
    a owl:Class ;
    rdfs:label "Loop Condition"@en , "Coinníoll Lúibe"@ga ;
    rdfs:comment """
        The statutory trigger for Part VI of the Act. Established under
        s.10B when: (a) three or more separate public bodies have each
        declined to examine the submission on its merits; or (b) the
        aggregate period during which no body has held carriage of the
        determination obligation exceeds 24 months. On establishment,
        the residual determination obligation vests in the Ombudsman.
    """@en .

fsd:ResidualObligation
    a owl:Class ;
    rdfs:label "Residual Determination Obligation"@en ,
               "Oibleagáid Chinnidh Iarmharach"@ga ;
    rdfs:comment """
        The obligation vested in the Ombudsman on establishment of the
        loop condition under s.10B. Requires the Ombudsman to: (a)
        investigate the submission on its merits; (b) issue a report
        under s.10C(3)(b) identifying structural conditions present;
        and (c) apply to the High Court for an order compelling a
        determination if no body has issued one within 6 months of
        the report.
    """@en .

fsd:LoopClosure
    a owl:Class ;
    rdfs:label "Loop Closure"@en , "Dúnadh Lúibe"@ga ;
    rdfs:comment """
        A recorded instance in which the Nullification Loop has been
        terminated by: (a) a determination issued by a public body
        before Ombudsman application; (b) a High Court order under
        s.10C(7); or (c) a finding of ontic collapse requiring
        legislative intervention. Each closure is entered on the
        Ombudsman's public register under s.10E.
    """@en .

fsd:TechnicalAudit
    a owl:Class ;
    rdfs:label "Independent Technical Audit"@en ,
               "Iniúchadh Teicniúil Neamhspleách"@ga ;
    rdfs:comment """
        A formal assessment of the operational, executable, or testable
        components of a submission, conducted by an independent auditor
        under s.5C. The audit assesses: (a) operational capacity;
        (b) executability; (c) replicability of outputs; (d) compliance
        with Regulation (EU) 2021/821 Art. 9(2) and AI Act Arts. 13–14
        where applicable. The audit does not determine the submission's
        merits — it provides an independent technical basis for
        the public body's determination.
    """@en .
```

---

## 5. Object Properties

```turtle
# ── Submission relationships ─────────────────────────────────────────────────

fsd:hasSubmitter
    a owl:ObjectProperty ;
    rdfs:label "has submitter"@en ;
    rdfs:domain fsd:Submission ;
    rdfs:range foaf:Agent ;
    rdfs:comment "Links a submission to the natural or legal person who lodged it."@en .

fsd:hasReceivingBody
    a owl:ObjectProperty ;
    rdfs:label "has receiving body"@en ;
    rdfs:domain fsd:Submission ;
    rdfs:range fsd:PublicBody ;
    rdfs:comment "Links a submission to the public body with which it was lodged."@en .

fsd:engagesRegulation
    a owl:ObjectProperty ;
    rdfs:label "engages regulation"@en ;
    rdfs:domain fsd:Submission ;
    rdfs:range eli:LegalResource ;
    rdfs:comment """
        Links a submission to the EU regulation whose assessment
        obligations are engaged by the submission's content.
    """@en .

# ── Public body relationships ────────────────────────────────────────────────

fsd:hasReceived
    a owl:ObjectProperty ;
    rdfs:label "has received"@en ;
    rdfs:domain fsd:PublicBody ;
    rdfs:range fsd:Submission ;
    owl:inverseOf fsd:hasReceivingBody .

fsd:hasDetermined
    a owl:ObjectProperty ;
    rdfs:label "has determined"@en ;
    rdfs:domain fsd:PublicBody ;
    rdfs:range fsd:Determination ;
    rdfs:comment "Links a public body to a determination it has issued."@en .

fsd:hasDisplacedTo
    a owl:ObjectProperty ;
    rdfs:label "has displaced to"@en ;
    rdfs:domain fsd:PublicBody ;
    rdfs:range fsd:PublicBody ;
    rdfs:comment """
        Links a body that has performed remit displacement to the body
        to which it has characterised the obligation as belonging.
        Lawful only where accompanied by transmission within 30 days
        and submitter notification — otherwise instantiates
        fsd:RemitDisplacement.
    """@en .

fsd:hasInstantiated
    a owl:ObjectProperty ;
    rdfs:label "has instantiated"@en ;
    rdfs:domain fsd:PublicBody ;
    rdfs:range fsd:ProhibitedPractice ;
    rdfs:comment """
        Links a public body to a prohibited practice it has performed.
        Established by aggregate conduct, not single act.
    """@en .

fsd:hasStructuralCondition
    a owl:ObjectProperty ;
    rdfs:label "has structural condition"@en ;
    rdfs:domain fsd:Submission ;
    rdfs:range fsd:StructuralCondition ;
    rdfs:comment """
        Links a submission (or the system of bodies that has received it)
        to a structural condition identified in respect of it by the
        Ombudsman under s.10C(3)(b).
    """@en .

# ── Loop architecture ────────────────────────────────────────────────────────

fsd:triggersLoopCondition
    a owl:ObjectProperty ;
    rdfs:label "triggers loop condition"@en ;
    rdfs:domain fsd:NullificationLoop ;
    rdfs:range fsd:LoopCondition ;
    rdfs:comment """
        Links an identified nullification loop to the statutory loop
        condition it establishes under s.10B.
    """@en .

fsd:vestsObligationIn
    a owl:ObjectProperty ;
    rdfs:label "vests obligation in"@en ;
    rdfs:domain fsd:LoopCondition ;
    rdfs:range fsd:Ombudsman ;
    rdfs:comment "Links the loop condition to the Ombudsman in whom the residual obligation vests."@en .

fsd:hasAudited
    a owl:ObjectProperty ;
    rdfs:label "has audited"@en ;
    rdfs:domain fsd:TechnicalAudit ;
    rdfs:range fsd:TestableSubmission .

fsd:conductedBy
    a owl:ObjectProperty ;
    rdfs:label "conducted by"@en ;
    rdfs:domain fsd:TechnicalAudit ;
    rdfs:range fsd:IndependentAuditor .
```

---

## 6. Data Properties

```turtle
fsd:submissionDate
    a owl:DatatypeProperty ;
    rdfs:label "submission date"@en ;
    rdfs:domain fsd:Submission ;
    rdfs:range xsd:date ;
    rdfs:comment "The date on which the submission was lodged with the public body."@en .

fsd:referenceNumber
    a owl:DatatypeProperty ;
    rdfs:label "reference number"@en ;
    rdfs:domain fsd:Submission ;
    rdfs:range xsd:string ;
    rdfs:comment "The reference number, if any, assigned by the receiving body on receipt."@en .

fsd:determinationDeadline
    a owl:DatatypeProperty ;
    rdfs:label "determination deadline"@en ;
    rdfs:domain fsd:Submission ;
    rdfs:range xsd:date ;
    rdfs:comment """
        The date by which the receiving body must issue a determination
        under s.3(1): 12 months from fsd:submissionDate.
    """@en .

fsd:determinationDate
    a owl:DatatypeProperty ;
    rdfs:label "determination date"@en ;
    rdfs:domain fsd:Determination ;
    rdfs:range xsd:date .

fsd:declinationCount
    a owl:DatatypeProperty ;
    rdfs:label "declination count"@en ;
    rdfs:domain fsd:Submission ;
    rdfs:range xsd:nonNegativeInteger ;
    rdfs:comment """
        The number of separate public bodies that have declined to examine
        the submission on its merits. When this value reaches 3, the
        loop condition under s.10B(1)(a) is triggered.
    """@en .

fsd:nonDeterminationPeriodMonths
    a owl:DatatypeProperty ;
    rdfs:label "non-determination period (months)"@en ;
    rdfs:domain fsd:Submission ;
    rdfs:range xsd:nonNegativeInteger ;
    rdfs:comment """
        The aggregate period in months during which no body has held
        carriage of the determination obligation. When this value
        reaches 24, the loop condition under s.10B(1)(b) is triggered.
    """@en .

fsd:isDualUse
    a owl:DatatypeProperty ;
    rdfs:label "is dual-use"@en ;
    rdfs:domain fsd:Submission ;
    rdfs:range xsd:boolean ;
    rdfs:comment "True where the submission formally asserts dual-use characteristics under Regulation (EU) 2021/821 Art. 2(1)."@en .

fsd:isHighRiskAI
    a owl:DatatypeProperty ;
    rdfs:label "is high-risk AI"@en ;
    rdfs:domain fsd:Submission ;
    rdfs:range xsd:boolean ;
    rdfs:comment "True where the submission asserts high-risk AI characteristics under Regulation (EU) 2024/1689 Annex III."@en .
```

---

## 7. SWRL Rules (Loop Condition Logic)

The following rules are expressed in SWRL (Semantic Web Rule Language), compatible with LegalRuleML. They encode the operative logic of Parts II, III, and VI of the Act.

```
# Rule 1 — Non-Determination (s.3(1))
# Where a body has received a submission and the determination deadline
# has passed without a determination issuing, NonDetermination is established.

Submission(?s) ∧ hasReceivingBody(?s, ?b) ∧
submissionDate(?s, ?d) ∧ determinationDeadline(?s, ?dl) ∧
¬hasDetermined(?b, ?det) ∧ swrlb:greaterThan(now(), ?dl)
→ NonDetermination(?s)

# Rule 2 — Loop Condition: Three Declinations (s.10B(1)(a))
# Where three or more bodies have each declined examination on the merits,
# the loop condition is triggered.

Submission(?s) ∧ declinationCount(?s, ?n) ∧
swrlb:greaterThanOrEqual(?n, 3)
→ LoopCondition(?lc) ∧ hasLoopCondition(?s, ?lc)

# Rule 3 — Loop Condition: 24-Month Non-Determination (s.10B(1)(b))
# Where no body has held carriage for 24 months, the loop condition
# is triggered independently of the declination count.

Submission(?s) ∧ nonDeterminationPeriodMonths(?s, ?m) ∧
swrlb:greaterThanOrEqual(?m, 24)
→ LoopCondition(?lc) ∧ hasLoopCondition(?s, ?lc)

# Rule 4 — Residual Obligation Vesting (s.10C)
# On loop condition establishment, the residual obligation vests in
# the Ombudsman.

LoopCondition(?lc) ∧ hasLoopCondition(?s, ?lc) ∧
Ombudsman(?o)
→ ResidualObligation(?ro) ∧ vestsObligationIn(?lc, ?o)

# Rule 5 — Testable Submission: Sufficiency Assertion Blocked (s.5A)
# Where a submission is testable and no testing opportunity has been
# arranged, sufficiency assertion is prohibited.

TestableSubmission(?s) ∧ hasReceivingBody(?s, ?b) ∧
¬hasArrangedTesting(?b, ?s)
→ SufficiencyAssertionBlocked(?s)

# Rule 6 — Structural Condition: Ontic Collapse (s.2A(1A))
# Where no single body holds the full competence and no mechanism
# assembles partial competences, ontic collapse is established.

Submission(?s) ∧ StructuralDisplacement(?sd) ∧
hasStructuralCondition(?s, ?sd) ∧
¬hasBodyWithFullCompetence(?s) ∧
¬hasAssemblyMechanism(?s)
→ OnticCollapse(?oc) ∧ hasStructuralCondition(?s, ?oc)
```

---

## 8. European Framework Alignment Table

| Bill Concept | OWL Class | LKIF Mapping | SEMIC CPV Mapping | ELI Mapping | Akoma Ntoso Mapping |
|---|---|---|---|---|---|
| Submission of National Utility | `fsd:SubmissionOfNationalUtility` | `lkif:LegalDocument` | `cpv:Evidence` | `eli:LegalResource` | `an:doc` |
| Public Body | `fsd:PublicBody` | `lkif:PublicBody` | `cpv:PublicOrganisation` | — | `an:organization` |
| Competent Authority | `fsd:CompetentAuthority` | `lkif:CompetentAuthority` | `cpv:PublicOrganisation` | — | `an:organization` |
| Determination (Accept) | `fsd:AcceptanceDetermination` | `lkif:Permission` | `cpv:PublicService` | `eli:LegalAct` | `an:decision` |
| Determination (Reject) | `fsd:RejectionDetermination` | `lkif:Obligation` | `cpv:PublicService` | `eli:LegalAct` | `an:decision` |
| Determination (Refer) | `fsd:ReferralDetermination` | `lkif:Obligation` | `cpv:PublicService` | `eli:LegalAct` | `an:decision` |
| Non-Determination | `fsd:NonDetermination` | `lkif:Void` | — | — | — |
| Remit Displacement | `fsd:RemitDisplacement` | `lkif:Exception` | — | — | — |
| Sufficiency Assertion | `fsd:SufficiencyAssertion` | `lkif:Exception` | — | — | — |
| Administrative Amnesia | `fsd:AdministrativeAmnesia` | — | — | — | — |
| Designed Forgetting | `fsd:DesignedForgetting` | — | — | — | — |
| Normative Collapse | `fsd:NormativeCollapse` | — | — | — | — |
| Silence Veto | `fsd:SilenceVeto` | — | — | — | — |
| Ontic Collapse | `fsd:OnticCollapse` | — | — | — | — |
| Loop Condition | `fsd:LoopCondition` | — | — | — | — |
| Residual Obligation | `fsd:ResidualObligation` | `lkif:Obligation` | — | — | — |
| Technical Audit | `fsd:TechnicalAudit` | `lkif:Evaluation` | `cpv:PublicService` | — | `an:report` |

**Note on blank cells:** Concepts with no LKIF, SEMIC, ELI, or Akoma Ntoso mapping are genuine ontological contributions of this framework. They have no equivalent in existing European legal ontologies because the administrative failure conditions they name have not previously been formalised in any jurisdiction. This is the ontology's core legislative innovation.

---

## 9. Alignment with the European Interoperability Framework (EIF)

The EIF (COM(2017)134) defines four interoperability layers. The FSD ontology addresses each:

| EIF Layer | FSD Ontology Contribution |
|---|---|
| **Legal interoperability** | The Act makes the duty of determination justiciable across EU member state law (Art. 41/47 CFR, Art. 2/4(3) TEU). The ontology maps these obligations to machine-readable axioms. |
| **Organisational interoperability** | The `fsd:LoopCondition` and `fsd:ResidualObligation` classes model cross-body coordination failures and the statutory mechanism for resolving them. |
| **Semantic interoperability** | The SKOS concept scheme (Section 10 below) provides a controlled vocabulary for the corpus lexicon, enabling consistent cross-system interpretation of the defined terms. |
| **Technical interoperability** | The OWL 2 DL profile ensures the ontology is compatible with standard triple stores (Apache Jena, Stardog, GraphDB) and SPARQL querying — enabling integration with EUR-Lex, national legislation databases, and Ombudsman case management systems. |

---

## 10. SKOS Concept Scheme (Corpus Lexicon)

```turtle
fsd:MeinhardtConceptScheme
    a skos:ConceptScheme ;
    skos:prefLabel "Meinhardt Initiative — Governance Failure Vocabulary"@en ,
                   "Tionscnamh Mheinhardt — Foclóir Teipe Rialachais"@ga ;
    dcterms:description """
        A SKOS concept scheme formalising the operational vocabulary of
        the Interregnum Nullificans corpus (2006–2026) and the Qualifying
        Submissions (Duty to Determine) Bill 2026. Designed for
        integration with EU IATE (Inter-Active Terminology for Europe)
        and EuroVoc.
    """@en .

fsd:NullificationLoopConcept
    a skos:Concept ;
    skos:inScheme fsd:MeinhardtConceptScheme ;
    skos:prefLabel "Nullification Loop"@en , "Lúba Neamhnithe"@ga ;
    skos:definition """
        A five-stage administrative attractor producing non-determination
        regardless of personnel: (1) Acknowledgement; (2) Deferral;
        (3) Remit Displacement; (4) Sufficiency Assertion;
        (5) Record Suppression.
    """@en ;
    skos:related fsd:NormativeCollapseConcept ;
    skos:related fsd:SilenceVetoConcept .

fsd:NormativeCollapseConcept
    a skos:Concept ;
    skos:inScheme fsd:MeinhardtConceptScheme ;
    skos:prefLabel "Normative Collapse"@en , "Clis Normach"@ga ;
    skos:definition """
        The structural condition in which procedurally valid outputs
        are produced while substantive obligations remain permanently
        unmet. The gap between governance form and governance substance
        is self-sustaining.
    """@en .

fsd:SilenceVetoConcept
    a skos:Concept ;
    skos:inScheme fsd:MeinhardtConceptScheme ;
    skos:prefLabel "Silence Veto"@en , "Veto Tosta"@ga ;
    skos:definition """
        Procedural silence functioning as a substantive adverse
        determination, rendered without notice, hearing, or reasons.
        Engages Art. 41 CFR directly.
    """@en .

fsd:OnticCollapseConcept
    a skos:Concept ;
    skos:inScheme fsd:MeinhardtConceptScheme ;
    skos:prefLabel "Ontic Collapse"@en , "Clis Ontach"@ga ;
    skos:definition """
        The condition in which no institutional subject capable of
        issuing a determination exists within the current public body
        architecture. The most acute form of structural displacement.
    """@en ;
    skos:broader fsd:StructuralDisplacementConcept .

fsd:StructuralDisplacementConcept
    a skos:Concept ;
    skos:inScheme fsd:MeinhardtConceptScheme ;
    skos:prefLabel "Structural Displacement"@en , "Easú Struchtúrach"@ga ;
    skos:narrower fsd:OnticCollapseConcept .
```

---

## 11. Linked Data Integration Points

The ontology is designed to connect directly to the following European and Irish linked data resources:

| Resource | URI Pattern | Integration Point |
|---|---|---|
| EUR-Lex (Regulation (EU) 2021/821) | `http://data.europa.eu/eli/reg/2021/821` | `fsd:engagesRegulation` |
| EUR-Lex (AI Act 2024/1689) | `http://data.europa.eu/eli/reg/2024/1689` | `fsd:engagesRegulation` |
| EU Publications Office — Authority Tables | `http://publications.europa.eu/resource/authority/` | Language, country, institution codes |
| Irish Statute Book (Qualifying Submissions Act 2026) | `http://www.irishstatutebook.ie/eli/2026/` | `eli:is_about` (once enacted) |
| Oireachtas Open Data (Bills) | `https://data.oireachtas.ie/` | Bill provenance and stage tracking |
| Irish Ombudsman (case register) | TBD — ontology reserves `fsd:ombudsmanCaseURI` | Loop closure register (s.10E) |
| Wassenaar Arrangement control lists | Via DG Trade linked data | Dual-use classification validation |

---

## 12. Governance Note

This ontology is a formalisation of a legislative proposal, not an enacted statute. Its classes, properties, and rules describe obligations that will be justiciable on enactment of the Bill. Until enactment:

- The ontology functions as a **semantic specification** for the governance architecture the Bill proposes.
- The SWRL rules function as **testable hypotheses** about how the loop condition logic would operate if applied to the existing record.
- The SKOS concept scheme functions as the **canonical vocabulary** for the Interregnum Nullificans corpus, suitable for cross-institutional reference in PETI submissions, Ombudsman complaints, and CJEU filings.

Applied to the existing record, the SWRL rules produce the following instantiations:

| Rule | Instantiation on Existing Record |
|---|---|
| Rule 1 (Non-Determination) | Established: submission date November 2006; determination deadline November 2007; no determination to date |
| Rule 2 (Loop Condition: 3 declinations) | Established: JCEUA, JCPP, SSCEUST, JCFAT, Defence, Justice, Finance, PAC (partial), Budgetary Oversight — declination count exceeds threshold by a factor of three |
| Rule 3 (Loop Condition: 24 months) | Established: non-determination period approximately 236 months at date of this document |
| Rule 4 (Residual Obligation) | Would vest in the Ombudsman on enactment — complaint OMB-260331-CSD014 currently active as the pre-legislative equivalent |
| Rule 6 (Ontic Collapse) | Established: CA function distributed across DETE (licensing), DFA (regime memberships), DoD (security assessment) with no statutory coordination mechanism |

---

*FSD-Ontology-2026 · Version 1.0.0 · July 24, 2026*
*Compatible with: OWL 2 DL · LKIF · ELI · SEMIC CPV · Akoma Ntoso · LegalRuleML · SKOS · EIF*
*Namespace: `https://meinhardt.gov/ontology/fsd/2026#`*
