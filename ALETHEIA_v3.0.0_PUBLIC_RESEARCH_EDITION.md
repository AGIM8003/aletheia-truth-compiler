---
title: "ALETHEIA Truth Compiler"
subtitle: "Complete Blueprint for Information Certification, Evidence DNA, and Truth Discovery"
author: "Agim Haxhijaha"
date: "July 12, 2026"
lang: "en-US"
keywords:
  - evidence provenance
  - information certification
  - truth discovery
  - Evidence DNA
  - artificial intelligence reliability
  - metacognition
  - cryptographic lineage
  - uncertainty
  - falsification
  - source independence
rights: "Copyright 2026 Agim Haxhijaha. Licensed CC BY-NC-ND 4.0."
---

# Publication Record

**Author:** Agim Haxhijaha  
**Role:** Independent Researcher  
**Version:** 2.0  
**First public release:** 2026-07-13  
**ORCID:** https://orcid.org/0009-0002-3234-7765  
**DOI:** https://doi.org/10.5281/zenodo.21344789  
**Document type:** Independent technical blueprint and proposed architecture  
**Language:** English (US)

## Rights and permitted sharing

Copyright 2026 Agim Haxhijaha.

This publication is licensed under the Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License
(CC BY-NC-ND 4.0). The unchanged document may be shared for noncommercial
purposes when the author is credited and a link to the license is provided.
Adaptation and commercial reuse require separate permission.

License: https://creativecommons.org/licenses/by-nc-nd/4.0/

The license protects and governs use of this publication as a copyrighted
work. It does not by itself create patent rights or exclusive ownership of
underlying ideas, procedures, or methods.

## Publication status and limitations

This document presents a proposed technical architecture. It is not a claim
that a reference implementation has been built, that the system has been
scientifically validated, or that it can determine universal or absolute
truth. Any claim of novelty remains subject to prior-art and professional
intel-property review.

## Generative AI disclosure

Generative AI tools assisted the preparation, organization, and language of
the draft. The named author is responsible for the concept selection,
instructions, review, publication decision, and accuracy of the released
document. AI tools are not listed as authors or inventors.

## Recommended citation

Haxhijaha, Agim. (2026). *ALETHEIA Truth Compiler: Complete Blueprint for
Information Certification, Evidence DNA, and Truth Discovery* (Version 2.0).
Independent technical blueprint. DOI: https://doi.org/10.5281/zenodo.21344789

## Contact purpose

Interested researchers, developers, institutions, investors, and implementation
partners should contact the author through the public ORCID profile or the
official GitHub repository created for this publication.

\newpage

# ALETHEIA TRUTH COMPILER

## Complete Blueprint for Information Certification, Evidence DNA, and Truth Discovery

**Artifact:** `ALETHEIA_TRUTH_COMPILER_BLUEPRINT.md`  
**Version:** 2.0 metacognitive, dynamic, future-ready engineering blueprint  
**Date:** 2026-07-11  
**Primary language:** English (US)  
**Architecture:** Local-first, open-protocol, authority-independent  
**Status:** EXPANDED BUILD SPECIFICATION — NOT A CLAIM OF UNIVERSAL OR ABSOLUTE TRUTH DETECTION

---

## 0. Executive Decision

ALETHEIA is a proposed independent infrastructure layer that performs three
separate functions:

1. **Evidence DNA** creates a tamper-evident identity and complete dependency
   lineage for information from the moment of acquisition through every
   transformation, interpretation, correction, and revocation.
2. **Information Certification** verifies integrity, provenance, acquisition
   method, transformation history, and reproducibility. Certification never
   claims that signed information is automatically true.
3. **Truth Discovery** decomposes claims, routes them to domain-appropriate
   validation methods, searches for contradiction and falsification, measures
   genuine source independence, and returns the strongest conclusion justified
   by the available evidence.

ALETHEIA does not appoint a person, government, company, laboratory, AI model,
or majority vote as the owner of truth. It makes the method, evidence,
dependencies, uncertainty, and limitations inspectable and reproducible.

The fundamental product statement is:

> ALETHEIA does not certify that a claimant is truthful. It certifies what was
> captured and how it travelled, then determines what conclusions the evidence
> can support under explicit domain rules.

### Document map

```text
PART I    Sections 0–30   Evidence DNA, certification and bounded truth discovery
PART II   Sections 31–46  Metacognition, active investigation and self-improvement
PART III  Sections 47–65  Future technology, federation, hardening and delivery
```

---

## 1. Non-Negotiable Truth Boundary

### 1.1 What the system can do

ALETHEIA can:

- prove that specific bytes have or have not changed;
- prove that a particular key signed a record;
- preserve acquisition and transformation lineage;
- identify multiple sources that descend from the same original source;
- detect contradictions, missing dependencies, circular citations, and
  unsupported conclusions;
- validate formal mathematical and software proofs;
- evaluate empirical claims through domain-specific evidence rules;
- generate reproducible evidence and truth receipts;
- show what would falsify a conclusion;
- distinguish facts, interpretations, predictions, and value judgments;
- retain uncertainty and the status `CURRENTLY_UNKNOWABLE`.

### 1.2 What the system cannot honestly do

ALETHEIA cannot:

- discover an external physical event from information that contains no
  contact with that event;
- prove that a signed statement is true merely because it is signed;
- infer private intention with mathematical certainty;
- convert popularity, repetition, credentials, or institutional authority into
  truth;
- guarantee that a compromised sensor recorded reality correctly;
- determine moral values without declared ethical premises;
- treat a prediction as an established fact before the outcome occurs;
- solve logically undecidable or empirically underdetermined questions;
- remove the need for new observation, experiment, or investigation.

An isolated wrapper can test internal consistency, provenance, and formal
validity. Empirical truth requires some connection to external reality. In this
blueprint, **authority-independent** means that no central authority is trusted
automatically. It does not mean evidence-independent.

---

## 2. Core Definitions

| Term | Definition |
|---|---|
| Reality | The state of the world independent of the system's description of it |
| Claim | A proposition capable of being evaluated under specified context |
| Evidence | An observation, artifact, measurement, proof, or record relevant to a claim |
| Evidence DNA | A content-addressed, signed, versioned dependency graph describing evidence acquisition and derivation |
| Information Certificate | A machine-verifiable statement about integrity, provenance, method, or reproduction—not truth itself |
| Truth Discovery | A domain-aware process for determining the strongest warranted status of a claim |
| Primary evidence | Evidence created through direct contact with the subject or event |
| Derived evidence | Evidence produced by transforming, summarizing, interpreting, or copying other evidence |
| Independent evidence | Evidence with a genuinely separate acquisition root and no material hidden common dependency |
| Truth Receipt | A reproducible package containing the claim, evidence graph, validators, results, uncertainty, and verdict |
| Prediction | A probabilistic statement about an unresolved future condition |
| Normative claim | A statement dependent on declared values, duties, laws, or preferences |
| Unknown | A valid result when available evidence cannot distinguish competing explanations |

### 2.1 Truth status vocabulary

ALETHEIA implementations MUST use explicit statuses:

```text
FORMALLY_PROVEN
EMPIRICALLY_ESTABLISHED
BEST_SUPPORTED_EXPLANATION
PLAUSIBLE
CONTESTED
UNVERIFIED
REFUTED
PREDICTION_UNRESOLVED
NORMATIVE_DEPENDS_ON_DECLARED_VALUES
CURRENTLY_UNKNOWABLE
INVALID_QUESTION_OR_CATEGORY_ERROR
```

Only formal systems may normally use `FORMALLY_PROVEN`. Empirical conclusions
remain open to new evidence even when strongly established.

---

## 3. System Constitution

Every conforming implementation MUST follow these rules:

1. **No automatic authority:** identity and reputation may inform risk analysis
   but never establish truth by themselves.
2. **No repetition inflation:** one source copied one billion times remains one
   evidential root.
3. **No signature inflation:** a signature proves key control and integrity,
   not honesty.
4. **No model voting illusion:** multiple models with common ancestry do not
   constitute independent confirmation.
5. **No hidden score:** every material component of an evaluation must be
   inspectable.
6. **No forced binary verdict:** unknown and contested states are first-class
   outputs.
7. **No evidence deletion by correction:** corrections supersede records; they
   do not silently rewrite history.
8. **No public personal-data ledger:** public logs contain commitments and
   revocation information, not unnecessary personal content.
9. **No AI as final oracle:** AI can extract, organize, challenge, and propose;
   deterministic or declared statistical validators issue results.
10. **No category mixing:** empirical, formal, predictive, causal,
    psychological, legal, and moral claims use different validation contracts.
11. **No unverifiable production claim:** a validator version, configuration,
    input commitments, and result must support deterministic replay where
    technically possible.
12. **No concealment of limitations:** missing evidence and possible alternative
    explanations must appear in every truth receipt.

---

## 4. Product Architecture

```text
┌──────────────────────────────────────────────────────────────────────┐
│                         EVIDENCE SOURCES                             │
│ sensors │ documents │ humans │ experiments │ databases │ AI output │
└───────────────────────────────┬──────────────────────────────────────┘
                                │
┌───────────────────────────────▼──────────────────────────────────────┐
│ 1. ACQUISITION GATEWAY                                               │
│ capture method │ consent │ device state │ timestamp │ challenge     │
└───────────────────────────────┬──────────────────────────────────────┘
                                │
┌───────────────────────────────▼──────────────────────────────────────┐
│ 2. EVIDENCE DNA ENGINE                                               │
│ canonicalize │ hash │ sign │ parent links │ mutation │ revocation   │
└───────────────────────────────┬──────────────────────────────────────┘
                                │
┌───────────────────────────────▼──────────────────────────────────────┐
│ 3. INFORMATION CERTIFICATION                                         │
│ integrity │ provenance │ attestation │ method │ reproducibility     │
└───────────────────────────────┬──────────────────────────────────────┘
                                │
┌───────────────────────────────▼──────────────────────────────────────┐
│ 4. CLAIM ATOMIZER AND DOMAIN ROUTER                                  │
│ who │ what │ when │ where │ how │ why │ prediction │ normative      │
└───────────────────────────────┬──────────────────────────────────────┘
                                │
┌───────────────────────────────▼──────────────────────────────────────┐
│ 5. TRUTH DISCOVERY MESH                                              │
│ independence │ contradiction │ falsification │ causality │ plugins  │
└───────────────────────────────┬──────────────────────────────────────┘
                                │
┌───────────────────────────────▼──────────────────────────────────────┐
│ 6. UNCERTAINTY AND VERDICT KERNEL                                    │
│ bounds │ alternatives │ unknowns │ status │ falsification criteria │
└───────────────────────────────┬──────────────────────────────────────┘
                                │
┌───────────────────────────────▼──────────────────────────────────────┐
│ 7. TRUTH RECEIPT AND TRANSPARENCY LOG                                │
│ replay package │ signatures │ corrections │ revocation │ disclosure │
└──────────────────────────────────────────────────────────────────────┘
```

### 4.1 Trust separation

The following components MUST be independently replaceable:

- acquisition device;
- identity provider;
- evidence storage;
- cryptographic signer;
- AI extraction model;
- domain validator;
- uncertainty method;
- transparency log;
- human reviewer.

Compromise of one component must reduce assurance and trigger warnings, not
silently convert false information into certified truth.

---

## 5. Evidence DNA — The Central Invention

### 5.1 Definition

Evidence DNA is not a label attached by a human. It is automatically minted by
software at acquisition or ingestion and extended at every transformation.

Evidence DNA is a directed acyclic graph, not merely a file hash:

- **Gene:** one immutable Evidence Atom;
- **Genome:** the complete ancestry graph of an artifact or claim;
- **Mutation:** a declared transformation such as crop, transcription,
  translation, normalization, summarization, or correction;
- **Phenotype:** a rendered document, image, transcript, conclusion, or model
  output produced from the genome;
- **Contamination marker:** a warning inherited from an untrusted, revoked, or
  disproven ancestor;
- **Recombination:** an artifact generated from multiple evidence parents;
- **Revocation:** a signed statement invalidating future reliance on an atom
  while preserving audit history.

The biological vocabulary is an analogy. The implementation remains a precise
cryptographic and semantic graph.

### 5.2 Evidence Atom

Each Evidence Atom MUST contain:

```json
{
  "spec": "aletheia.edna.v1",
  "dna_id": "edna:sha256:<digest>",
  "payload": {
    "digest_algorithm": "sha-256",
    "digest": "<hex>",
    "media_type": "audio/wav",
    "size_bytes": 123456,
    "encrypted": true,
    "storage_locator": "local-vault://object/<opaque-id>"
  },
  "event": {
    "type": "direct_capture",
    "started_at": "2026-07-11T09:00:00Z",
    "ended_at": "2026-07-11T09:00:10Z",
    "clock_evidence": ["local_monotonic", "rfc3161_optional"],
    "location_commitment": null
  },
  "acquisition": {
    "method_id": "microphone.pcm.v1",
    "device_claim": "device:<pseudonymous-id>",
    "software_build_digest": "sha256:<digest>",
    "remote_attestation": null,
    "operator_claim": "principal:<pseudonymous-id>",
    "consent_record_ids": ["edna:sha256:<digest>"]
  },
  "derivation": {
    "parents": [],
    "transformation_id": null,
    "parameters_digest": null,
    "model_digest": null,
    "human_edits": []
  },
  "classification": {
    "origin": "human_world_capture",
    "synthetic_probability": null,
    "domains": ["meeting", "speech"],
    "sensitivity": "personal_data_restricted"
  },
  "assurance": {
    "self_reported_fields": ["operator_claim"],
    "attested_fields": [],
    "unverified_fields": ["location"],
    "known_limitations": ["single_microphone"]
  },
  "policy": {
    "purpose": "consensual_meeting_transcription",
    "retention_until": "2026-08-10T00:00:00Z",
    "license": "private",
    "disclosure": "selective"
  },
  "signature": {
    "algorithm": "ed25519",
    "key_id": "key:<id>",
    "value": "<base64url>"
  }
}
```

### 5.3 DNA identifier generation

The canonical DNA identifier is calculated as:

```text
canonical_atom = JCS(atom_without_dna_id_and_signature)
domain_separator = UTF8("ALETHEIA-EDNA-V1\0")
dna_digest = SHA-256(domain_separator || canonical_atom)
dna_id = "edna:sha256:" || lowercase_hex(dna_digest)
signature = Ed25519.sign(key, domain_separator || canonical_atom || dna_digest)
```

JSON Canonicalization Scheme, RFC 8785, is the baseline canonical format.
Deterministic CBOR may be added in a future profile. A conforming system MUST
publish canonicalization test vectors.

### 5.4 DNA inheritance rules

When an atom is derived from parents:

1. Every direct parent DNA identifier is mandatory.
2. The transformation implementation and version are mandatory.
3. Model-generated transformations include the exact model artifact digest,
   runtime version, prompt-template digest, decoding parameters, and tool calls.
4. Human modifications identify changed ranges without requiring public human
   identity.
5. A revoked parent marks every descendant `DEPENDENCY_REVIEW_REQUIRED`.
6. A disproven parent does not automatically disprove every descendant; it
   removes that parent's support and forces recomputation.
7. A copied source inherits the same root-acquisition cluster.
8. A translation is not independent evidence of the original claim.
9. An AI summary is not independent evidence of its sources.
10. Screenshots, re-encodings, and reposts remain derivatives when similarity,
    metadata, or provenance demonstrates common origin.

### 5.5 Source-root discovery

The DNA engine identifies evidential roots through:

- explicit parent links;
- cryptographic and perceptual similarity;
- citation and quotation extraction;
- shared timestamps, metadata, and publication patterns;
- common model-output signatures;
- identical unusual errors or phrasing;
- shared funding, ownership, operator, laboratory, or dataset dependencies;
- network propagation analysis;
- declared and inferred transformations.

Inferred ancestry MUST be marked as inferred, include the method and confidence,
and remain contestable.

### 5.6 DNA assurance is not binary

An Evidence Atom receives an assurance vector:

```text
I = integrity assurance
P = provenance completeness
A = acquisition assurance
T = temporal assurance
D = independence assurance
R = reproducibility
S = security/attestation assurance
C = consent and policy completeness
```

The vector MUST remain visible. It MUST NOT be hidden inside a single universal
percentage. A valid signature with weak acquisition produces high integrity but
low acquisition assurance.

### 5.7 Privacy-preserving DNA

Evidence DNA MUST support:

- encrypted payloads stored outside public logs;
- public commitments instead of public content;
- pairwise pseudonymous identifiers;
- selective disclosure of certificate fields;
- zero-knowledge proofs in later profiles;
- crypto-shredding of encryption keys when lawful erasure is required;
- redacted derivative atoms with explicit redaction transformations;
- separation of identity verification from public identity disclosure.

Personal data, precise location, biometric templates, meeting audio, and medical
records MUST NOT be written directly to an immutable public ledger.

---

## 6. Information Certification

### 6.1 Purpose

Information Certification answers:

- Is this the same artifact that was captured or issued?
- Who or what claims to have created it?
- When and how was it acquired?
- What transformations occurred?
- Can the process be replayed?
- Is the evidence complete enough for its declared use?

It does not answer, by itself, whether the underlying claim corresponds with
reality.

### 6.2 Certification levels

| Level | Name | Meaning |
|---:|---|---|
| IC-0 | Uncertified | No verified integrity or provenance |
| IC-1 | Integrity Bound | Payload hash and canonical metadata are valid |
| IC-2 | Provenance Traced | Issuance and transformation lineage are recorded |
| IC-3 | Acquisition Attested | Capture environment or process provides verifiable attestation |
| IC-4 | Method Reproduced | Independent execution reproduces the declared transformation or result |
| IC-5 | Independently Corroborated | Multiple genuinely separate acquisition roots support the relevant observation |

IC-5 is still not an unconditional truth declaration. Colluding independent
devices may record a staged event accurately. The certificate must state what
was observed and what was not established.

### 6.3 Certificate types

- **Integrity Certificate:** byte-level identity and signature validation.
- **Capture Certificate:** acquisition method, device state, operator role, and
  challenge-response evidence.
- **Transformation Certificate:** deterministic or statistical processing
  lineage.
- **Reproduction Certificate:** a separate validator repeated a method and
  compared results.
- **Independence Certificate:** source-root analysis and dependency collapse.
- **Correction Certificate:** previous and corrected versions with reasons.
- **Revocation Certificate:** scope, authority, reason category, and effective
  time.
- **Disclosure Certificate:** proves that a disclosed subset belongs to a
  certified record.

### 6.4 Certificate wording rule

Permitted:

```text
The attached audio matches the digest captured by device D at time T according
to the available attestation and has not changed since certification.
```

Prohibited:

```text
This audio proves that every represented event and speaker identity is true.
```

---

## 7. Truth Discovery Engine

### 7.1 Claim atomization

Complex statements MUST be decomposed into atomic claims.

Example:

```text
"Alex approved the payment yesterday because the supplier threatened him."
```

becomes:

```text
C1: A person identified as Alex performed an approval action.
C2: The approved object was payment P.
C3: The action occurred within time interval T.
C4: A supplier communicated a threat.
C5: Alex received or perceived that communication.
C6: The threat causally influenced the approval.
C7: The threat was the motivating reason for the approval.
```

Each claim may receive a different status. C1–C3 might be empirically
established, C4 contested, C5 plausible, and C6–C7 currently unknowable.

### 7.2 Claim contract

Every claim MUST declare:

- proposition;
- claim class;
- subject and object;
- time interval;
- location or scope when relevant;
- required precision;
- jurisdiction when legal rules apply;
- operational definitions;
- burden or threshold appropriate to the use;
- acceptable evidence types;
- known alternatives;
- falsification conditions;
- prohibited category conversions.

### 7.3 Domain routing

The router assigns one or more validation contracts:

```text
FORMAL_MATHEMATICAL
SOFTWARE_EXECUTION
DIRECT_OBSERVATION
PHYSICAL_MEASUREMENT
BIOLOGICAL_EXPERIMENTAL
MEDICAL_CLINICAL
PSYCHOLOGICAL_BEHAVIORAL
HISTORICAL_RECONSTRUCTION
IDENTITY_ATTRIBUTION
CAUSAL_INFERENCE
PREDICTIVE_FORECAST
LEGAL_INTERPRETATION
NORMATIVE_ETHICAL
```

Multi-domain claims require all relevant contracts. Passing one domain cannot
silently satisfy another.

### 7.4 Truth discovery loop

```text
function discover(claim, evidence_graph, use_context):
    contract = classify_and_compile_claim(claim, use_context)
    atoms = decompose(contract)

    for atom in atoms:
        candidates = retrieve_relevant_evidence(atom)
        verified = verify_information_certificates(candidates)
        roots = collapse_common_ancestry(verified)
        support, oppose = classify_evidential_relationships(roots, atom)
        alternatives = generate_competing_explanations(atom, support, oppose)
        tests = run_domain_validators(atom, support, oppose, alternatives)
        attacks = run_adversarial_falsifiers(atom, tests, roots)
        bounds = compute_justified_uncertainty(contract, tests, attacks)
        status = assign_status_without_exceeding_contract_ceiling(bounds)
        receipt = compile_truth_receipt(atom, status, bounds, tests, attacks)

    return compose_without_hiding_disagreement(receipts)
```

### 7.5 Support is not source count

Before evaluating evidence quantity, ALETHEIA collapses descendants into
independent acquisition-root clusters. One original report repeated by 500
websites, 200 AI agents, and 50 television channels remains one root.

Where justified, the system may calculate an effective evidence count:

```text
N_effective = (sum(root_weight_i))² / sum(root_weight_i²)
```

This number is meaningful only after ancestry clustering and only within a
declared statistical model. It must not be displayed as universal truth
probability.

### 7.6 Evidence relationship types

Evidence can:

- directly support;
- indirectly support;
- directly contradict;
- indirectly contradict;
- establish context only;
- establish possibility but not occurrence;
- establish occurrence but not identity;
- establish identity but not intention;
- establish correlation but not causation;
- be irrelevant;
- be inadmissible under the selected contract;
- remain ambiguous.

### 7.7 Contradiction engine

The engine MUST preserve conflicting evidence and test:

- mutually exclusive timestamps;
- impossible locations or physical states;
- inconsistent identity attribution;
- numerical disagreement outside measurement tolerance;
- changed definitions or denominators;
- circular sourcing;
- omitted negative evidence;
- chronology violations;
- causal direction reversal;
- inconsistencies between text, image, audio, sensor, and physical consequence;
- claims that become true only after changing their meaning.

### 7.8 Falsification engine

For each proposed conclusion, an adversarial module asks:

1. What observation would disprove this claim?
2. Is that observation available but omitted?
3. What alternative explanation fits the same evidence?
4. Could evidence have been staged, selectively recorded, corrupted, or
   coordinated?
5. Are independent-looking sources actually dependent?
6. Does the conclusion exceed the precision of the evidence?
7. Is absence of evidence being misrepresented as evidence of absence?
8. What is the strongest argument against the conclusion?
9. Would a different domain definition reverse the result?
10. Which result remains if the strongest supporting source is removed?

AI models may generate hypotheses, but a model's inability to invent a
counterexample is not proof that none exists.

### 7.9 Causal engine

The causal layer separates:

- temporal order;
- association;
- mechanism;
- intervention evidence;
- counterfactual dependence;
- confounding;
- mediation;
- intention and purpose.

The system MUST NOT translate correlation into causation. Causal results must
state the assumed graph, identification strategy, interventions or natural
experiments, sensitivity to hidden confounding, and alternative structures.

### 7.10 Uncertainty representation

ALETHEIA uses the representation appropriate to the domain:

- exact proof validity;
- measurement interval;
- probability distribution;
- confidence or credible interval;
- likelihood ratio;
- partial-identification bounds;
- competing-hypothesis ranking;
- qualitative status where numerical probability is unjustified.

The interface MUST never invent a precise percentage merely to appear
scientific.

---

## 8. Domain Validation Contracts

### 8.1 Mathematics and logic

Required:

- declared axioms and logic;
- machine-readable statement;
- proof object;
- independently implemented proof checker where risk warrants;
- dependency list of prior theorems;
- consistency and version information.

Possible result: `FORMALLY_PROVEN` relative to the declared formal system.

Limit: proof from axioms does not establish that an empirical model accurately
describes the physical world.

### 8.2 Software and computation

Required as applicable:

- source and binary digests;
- reproducible build;
- test vectors;
- execution trace;
- formal specification;
- static analysis;
- model checker or theorem prover;
- hardware and environment declaration.

Passing tests proves only tested behavior. Formal verification proves declared
properties under declared assumptions.

### 8.3 Physics and engineering

Required as applicable:

- calibrated measurement instruments;
- uncertainty and tolerance;
- independent sensors;
- conservation and feasibility constraints;
- repeat measurement;
- environmental conditions;
- raw and processed data DNA;
- treatment of outliers and missing samples.

Cross-modal physical consequences are valuable. A claimed collision may be
tested against video, acceleration, vehicle deformation, sound, location, and
independent observations.

### 8.4 Biology

Required as applicable:

- operational definitions;
- sample provenance;
- controls and randomization;
- protocol version;
- blinding;
- contamination checks;
- statistical plan;
- effect size and uncertainty;
- replication;
- biological plausibility and mechanism;
- negative results and exclusions.

One laboratory's repeated measurements are not automatically independent
replications if they share samples, equipment, protocol bias, or analysts.

### 8.5 Medicine

Required as applicable:

- distinction between population evidence and individual diagnosis;
- clinical validation;
- benefits, harms, contraindications, and uncertainty;
- patient-specific evidence and consent;
- current guideline context;
- human professional review for consequential decisions;
- strict separation of information from medical authorization.

ALETHEIA must not present a literature association as an individual medical
fact.

### 8.6 Psychology and human intention

Required:

- observable behavior separated from inferred mental state;
- instrument validity;
- context and cultural limitations;
- alternative explanations;
- self-report identified as self-report;
- longitudinal or experimental evidence where available;
- uncertainty that cannot be eliminated.

Private intention is generally not directly observable. A confession is
evidence of what a person stated, not infallible proof of motive.

### 8.7 History and event reconstruction

Required as applicable:

- contemporaneity of sources;
- source ancestry and copying;
- physical artifacts;
- chain of custody;
- incentives and opportunity for deception;
- independent perspectives;
- chronology;
- later alterations;
- missing archives and survival bias;
- competing reconstructions.

Historical truth can be strongly established without becoming mathematically
proven.

### 8.8 Identity and attribution

The system separates:

- account/key control;
- physical presence;
- biological identity;
- legal identity;
- authorship;
- responsibility;
- voice or face similarity.

A key signature establishes key control. A biometric similarity establishes a
match estimate. Neither alone proves legal responsibility or intention.

### 8.9 Prediction

Every forecast MUST include:

- prediction time;
- measurable outcome definition;
- resolution time and source;
- probability or interval;
- assumptions;
- model and data DNA;
- base rate;
- calibration history;
- revision history.

Forecasts remain `PREDICTION_UNRESOLVED` until resolved. Afterward, they become
records of forecasting performance, not retroactively certain knowledge.

### 8.10 Law and ethics

Legal conclusions require:

- jurisdiction;
- effective date;
- authority hierarchy;
- facts assumed;
- interpretive uncertainty;
- professional responsibility boundaries.

Ethical conclusions require declared values and principles. The system may
evaluate logical consistency and consequences but must not disguise a value
choice as an empirical discovery.

---

## 9. Corruption and Deception Resistance

### 9.1 Threat model

ALETHEIA assumes the possibility of:

- lying witnesses;
- corrupt officials or laboratories;
- coordinated media narratives;
- forged documents and deepfakes;
- compromised capture devices;
- colluding sensors;
- AI-generated source flooding;
- circular citations;
- bribed or coerced validators;
- selective publication;
- staged events;
- malicious timestamps and locations;
- replay attacks;
- prompt injection and memory poisoning;
- dependency substitution;
- model monoculture and correlated errors;
- a compromised ALETHEIA node.

### 9.2 Defensive design

1. **Zero inherent trust:** every assertion is typed as claimed, attested,
   inferred, reproduced, or independently observed.
2. **Root ancestry collapse:** duplicates and derivatives do not multiply
   support.
3. **Challenge capture:** high-risk acquisition can include unpredictable
   nonce, motion, perspective, timing, or sensor challenges.
4. **Cross-modal consistency:** compare independent physical consequences, not
   only similar text.
5. **Diverse validators:** use different implementations, teams, devices, and
   methods where practical.
6. **Public test vectors:** deterministic components must be reproducible.
7. **Negative-evidence search:** actively seek disconfirmation.
8. **Append-only correction:** prevent quiet historical rewriting.
9. **Revocation propagation:** recalculate descendants when foundations change.
10. **Threshold protection:** sensitive signing and governance keys use
    multi-party control.
11. **Local verification:** users can verify receipts without asking the
    original issuer for permission.
12. **No secret reputation formula:** source history is evidence, not an opaque
    social credit score.

### 9.3 Collusion analysis

Sources that appear institutionally separate may share:

- ownership;
- funding;
- data suppliers;
- authors;
- laboratories;
- software;
- models;
- cloud infrastructure;
- political or commercial incentives;
- a common original publication.

These relationships reduce independence assurance but do not automatically
invalidate content. The relationship graph and inference method must be shown.

### 9.4 Compromised-system behavior

If ALETHEIA detects compromise or cannot validate its own execution state, it
must:

```text
STOP NEW HIGH-ASSURANCE CERTIFICATION
PRESERVE EXISTING EVIDENCE
MARK AFFECTED RECEIPTS
ROTATE OR REVOKE KEYS
PUBLISH A SIGNED INCIDENT RECORD
REPLAY FROM LAST VERIFIED CHECKPOINT
REQUIRE INDEPENDENT VALIDATION
```

---

## 10. Truth Receipt

### 10.1 Required contents

Every Truth Receipt includes:

- receipt identifier and version;
- atomic claim;
- claim class and domain contract;
- time, place, scope, and definitions;
- supporting and opposing Evidence DNA roots;
- complete derivation dependencies;
- information certificate results;
- independence analysis;
- validators and exact versions;
- assumptions;
- alternative explanations;
- contradiction and falsification tests;
- uncertainty representation;
- status and maximum justified status;
- conditions that would change the result;
- privacy/disclosure policy;
- human review when required;
- signatures and optional transparency-log proof.

### 10.2 Truth Receipt schema

```json
{
  "spec": "aletheia.truth-receipt.v1",
  "receipt_id": "truth:sha256:<digest>",
  "claim": {
    "claim_id": "claim:sha256:<digest>",
    "proposition": "Audio participant P uttered statement S during interval T",
    "class": ["direct_observation", "identity_attribution"],
    "context": {
      "time_interval": ["<start>", "<end>"],
      "scope": "recorded_meeting"
    }
  },
  "evidence": {
    "supporting_roots": ["edna:sha256:<digest>"],
    "opposing_roots": [],
    "derived_items": ["edna:sha256:<digest>"],
    "effective_independence": {
      "root_clusters": 1,
      "limitations": ["single microphone", "human speaker mapping"]
    }
  },
  "validation": {
    "contract": "speech-event-attribution.v1",
    "validators": [
      {
        "id": "audio-integrity.v1",
        "implementation_digest": "sha256:<digest>",
        "result": "pass"
      },
      {
        "id": "speaker-attribution.v1",
        "result": "human_reviewed_probabilistic_match"
      }
    ]
  },
  "analysis": {
    "alternatives": ["speaker mapping error", "audio playback into room"],
    "contradictions": [],
    "falsification_conditions": [
      "independent evidence establishes a different speaker",
      "capture device compromise is demonstrated"
    ]
  },
  "verdict": {
    "status": "BEST_SUPPORTED_EXPLANATION",
    "uncertainty": "identity depends on reviewed session-local mapping",
    "not_established": ["speaker motive", "completeness outside recording"]
  },
  "issued_at": "<timestamp>",
  "signatures": ["<signature-object>"]
}
```

### 10.3 Deterministic replay

A verifier must be able to:

1. retrieve or receive disclosed evidence;
2. validate DNA commitments and signatures;
3. reconstruct the dependency graph;
4. execute deterministic validators;
5. compare statistical validator configurations and outputs;
6. confirm the verdict did not exceed the contract ceiling;
7. identify unavailable private evidence explicitly.

---

## 11. Core Data Model

### 11.1 Entities

```text
PrincipalClaim       claimed identity or role
Key                  cryptographic verification material
EvidenceAtom         immutable evidence metadata and commitment
Payload              protected content bound to an EvidenceAtom
AcquisitionEvent     interaction that captured or issued evidence
Transformation       declared derivation process
Claim                proposition under evaluation
EvidenceRelation     support, contradiction, context, or ambiguity
ValidationContract   domain-specific evaluation rules
ValidatorRun         reproducible validation execution
Hypothesis           candidate explanation
InformationCertificate integrity/provenance/method result
TruthReceipt         complete evaluation outcome
Correction           superseding information
Revocation           invalidation or withdrawal event
TransparencyEntry    public or consortium commitment
DisclosureGrant      permission to access protected material
```

### 11.2 Graph relations

```text
WAS_CAPTURED_BY
WAS_ISSUED_BY
WAS_DERIVED_FROM
WAS_TRANSFORMED_BY
WAS_REVIEWED_BY
WAS_CORRECTED_BY
WAS_REVOKED_BY
SUPPORTS
CONTRADICTS
CONTEXTUALIZES
IS_ALTERNATIVE_TO
DEPENDS_ON
SHARES_ACQUISITION_ROOT_WITH
WAS_REPRODUCED_BY
WAS_INVALIDATED_BY
```

The model maps to W3C PROV concepts where possible while extending them with
claim semantics, evidential relationships, independence clusters, validation
contracts, and truth receipts.

---

## 12. API Blueprint

### 12.1 Core endpoints

```text
POST   /v1/evidence/acquire
POST   /v1/evidence/ingest
POST   /v1/evidence/derive
GET    /v1/evidence/{dna_id}
POST   /v1/evidence/{dna_id}/correct
POST   /v1/evidence/{dna_id}/revoke

POST   /v1/certificates/issue
POST   /v1/certificates/verify
GET    /v1/certificates/{certificate_id}

POST   /v1/claims/compile
POST   /v1/claims/{claim_id}/evaluate
POST   /v1/claims/{claim_id}/challenge
GET    /v1/claims/{claim_id}/graph

GET    /v1/truth-receipts/{receipt_id}
POST   /v1/truth-receipts/{receipt_id}/replay
GET    /v1/truth-receipts/{receipt_id}/changes

POST   /v1/disclosures/grant
POST   /v1/disclosures/verify
GET    /v1/transparency/{entry_id}/proof
```

### 12.2 Evaluation request

```json
{
  "claim": "The tested component failed because temperature exceeded 90 C",
  "use_context": "engineering_incident_investigation",
  "required_precision": "cause_contributing_factor",
  "jurisdiction": null,
  "evidence_ids": ["edna:sha256:<digest>"],
  "allow_external_observation_requests": true,
  "privacy_profile": "restricted_local",
  "maximum_runtime_seconds": 300
}
```

### 12.3 Evaluation response

```json
{
  "claim_id": "claim:sha256:<digest>",
  "status": "CONTESTED",
  "supported_parts": ["temperature exceeded 90 C before shutdown"],
  "unsupported_parts": ["excess temperature was the initiating cause"],
  "alternatives": ["bearing failure generated excess temperature"],
  "missing_evidence_requests": [
    "independent bearing inspection",
    "sensor calibration record",
    "power and vibration trace"
  ],
  "truth_receipt_id": "truth:sha256:<digest>"
}
```

---

## 13. Local-First and Authority-Independent Deployment

### 13.1 Operating modes

| Mode | Description |
|---|---|
| Sealed Local | All payloads, graphs, models, and validation remain on one device or controlled network |
| Federated Verification | Independent nodes exchange commitments, certificates, and selective disclosures |
| Consortium | Authorized organizations share a replicated transparency layer without a single truth authority |
| Public Verification | Public commitments and verification software support open receipt checking |

### 13.2 No mandatory cloud dependency

The core MUST work without:

- a proprietary AI API;
- a central identity provider;
- a central truth database;
- an online reputation service;
- a public blockchain;
- a government certificate authority;
- continuous internet access.

Optional external systems may provide observations, timestamps, identity
claims, model execution, or transparency witnesses. Their contribution remains
an evidence dependency and never becomes an unquestioned oracle.

### 13.3 Suggested implementation stack

| Layer | Recommendation |
|---|---|
| Core kernel | Rust with memory-safe deterministic modules |
| Portable SDK | Rust, Python, TypeScript, Kotlin, Swift, and WASM bindings |
| Canonical records | RFC 8785 JCS JSON profile |
| Hashing | SHA-256 interoperability baseline; BLAKE3 optional local acceleration |
| Signatures | Ed25519 baseline; algorithm agility mandatory |
| Protected storage | Encrypted SQLite for MVP; content-addressed object vault |
| Graph | Embedded graph index or PostgreSQL/graph extension for server deployment |
| Transparency | Merkle append-only log with inclusion and consistency proofs |
| Policy | Versioned declarative contracts compiled to deterministic rules |
| Local AI | Replaceable local models for extraction and hypothesis generation |
| Formal methods | SMT solvers and proof assistants through sandboxed adapters |
| Media provenance | C2PA import/export adapter |
| Provenance exchange | W3C PROV mapping |
| Credentials | W3C Verifiable Credentials-compatible disclosures where appropriate |
| Attestation | IETF RATS-compatible evidence adapter |

### 13.4 AI model containment

AI models operate as untrusted analytical assistants:

- inputs are explicitly scoped;
- outputs are treated as candidate claims;
- models cannot modify evidence history;
- tool calls are logged into Evidence DNA;
- prompts and model digests are recorded;
- model outputs cannot issue high-assurance certificates;
- prompt injection content remains data, not executable policy;
- at least one non-model validator is required for consequential verdicts.

---

## 14. Meeting and Transcript Application Example

ALETHEIA can strengthen a local meeting-transcription application without
claiming court-certified accuracy.

### 14.1 Capture

1. Record the participant notice and acknowledgment as protected Evidence DNA.
2. Generate an atom for every fixed-duration audio chunk.
3. Chain chunks through parent identifiers and monotonic timestamps.
4. Store microphone configuration, application build digest, interruption
   events, pause/resume events, and operator actions.
5. Encrypt audio locally.

### 14.2 Processing

1. Transcription generates derivative atoms referencing audio chunks, model
   digest, language settings, and timestamps.
2. Speaker diarization generates session-local speaker-label atoms.
3. Mapping a speaker label to a participant creates a human-reviewed identity
   attribution atom.
4. Every text correction generates a correction atom showing the previous and
   replacement text.
5. An AI summary references transcript segments but is explicitly marked
   derived and not independent evidence.

### 14.3 Certification

The system may certify:

- audio integrity;
- capture continuity and declared interruptions;
- exact transcription model and parameters;
- human corrections;
- export integrity;
- who controlled the signing key;
- session-local speaker mapping method.

It must not automatically certify:

- that the microphone captured everything in the room;
- that participant names are legally verified identities;
- that a speaker's statement was honest;
- that an inferred motive is true;
- that the transcript is legally certified evidence.

### 14.4 Truth discovery

For the claim “Participant A said sentence S,” the engine evaluates:

- audio presence and integrity;
- speech segment boundaries;
- transcription alternatives;
- speaker-label confidence;
- identity mapping evidence;
- playback or impersonation possibilities;
- human review;
- contradictory recordings or witnesses.

The result may be `BEST_SUPPORTED_EXPLANATION`, with limitations, rather than
an absolute declaration.

---

## 15. Scientific Claim Example

Claim: “Treatment X reduces outcome Y by 20%.”

ALETHEIA MUST test:

- whether 20% is relative or absolute reduction;
- population, endpoint, and time horizon;
- protocol and preregistration;
- raw-data and analysis DNA;
- randomization, blinding, attrition, exclusions, and missing values;
- statistical model and multiplicity;
- effect interval, not only p-value;
- independent replication roots;
- shared samples, laboratories, funding, authors, and analytic code;
- contrary studies and publication bias;
- whether the result applies to the current individual.

Possible output:

```text
EMPIRICALLY_ESTABLISHED for population P, endpoint E, and period T.
Estimated relative reduction: 20%.
Absolute reduction: 2 percentage points.
Not established for populations outside P.
No individual treatment recommendation is certified by this receipt.
```

---

## 16. Prediction Certification

ALETHEIA separates forecast quality from outcome truth.

### 16.1 Prediction DNA

At forecast creation, record:

- immutable prediction text;
- model and data DNA;
- probability or interval;
- issue time;
- resolution condition;
- resolution deadline;
- allowed data cutoff;
- assumptions;
- forecaster identity claim;
- prohibited retroactive changes.

### 16.2 Resolution

When the outcome occurs:

- acquire outcome evidence independently;
- apply the original resolution contract;
- score calibration and accuracy;
- preserve revisions as separate forecasts;
- prevent selective deletion of failed forecasts.

Predictions cannot receive `FORMALLY_PROVEN` or `EMPIRICALLY_ESTABLISHED` before
resolution.

---

## 17. Security Architecture

### 17.1 Security zones

```text
UNTRUSTED INPUT ZONE
    ↓ strict parsing and content isolation
EVIDENCE INGESTION ZONE
    ↓ canonicalization and commitments
PROTECTED EVIDENCE VAULT
    ↓ least-privilege disclosure
VALIDATION SANDBOX
    ↓ signed validator results
VERDICT KERNEL
    ↓ policy and status ceiling
RECEIPT SIGNING ZONE
    ↓ append-only commitment
TRANSPARENCY / EXPORT ZONE
```

### 17.2 Mandatory controls

- memory-safe core implementation;
- sandboxed media decoders and validator plugins;
- strict schema and size limits;
- signed reproducible builds;
- software bill of materials;
- dependency pinning and vulnerability scanning;
- hardware-backed keys where available;
- key rotation and revocation;
- multi-party control for root releases;
- encrypted data at rest and in transit;
- role- and purpose-based access;
- immutable audit events with privacy-preserving commitments;
- backup, recovery, and corruption detection;
- no transcript, medical, or private evidence in diagnostics;
- penetration testing and cryptographic review;
- deterministic test vectors for canonicalization and DNA inheritance.

### 17.3 Cryptographic agility

Algorithms will age. Every record includes algorithm identifiers. The system
must support re-attestation of old commitments with newer algorithms without
changing historical payload digests or pretending the new signature existed at
the original time.

---

## 18. Privacy, Rights, and Legal Design

### 18.1 GDPR principles

Deployments processing personal data require:

- defined controller and processor roles;
- documented purpose and lawful basis;
- data minimization;
- retention limits;
- access and correction mechanisms;
- erasure handling;
- security and breach processes;
- data-protection impact assessment where required;
- restrictions for biometric and special-category data;
- human review for consequential decisions;
- country-specific recording-law analysis.

### 18.2 Erasure versus audit integrity

The architecture separates:

- encrypted evidence payload;
- personal metadata;
- pseudonymous graph identifier;
- non-personal cryptographic commitment;
- correction and revocation state.

When erasure is legally required, content and keys can be deleted while a
minimal non-identifying commitment and deletion event may remain when legally
justified. This is deployment-specific and requires legal review. “Blockchain
immutability” is not an excuse to publish personal data permanently.

### 18.3 EU AI Act boundary

ALETHEIA supports transparency, traceability, data governance, risk management,
human oversight, and logging. It does not automatically make a deployment
compliant. Risk classification and obligations depend on intended purpose and
actual use.

### 18.4 Human rights protections

ALETHEIA MUST NOT become:

- a universal reputation score;
- a secret government truth list;
- an automated guilt engine;
- an emotion-recognition authority;
- a political censorship mechanism;
- a biometric mass-surveillance system;
- an excuse to deny contest, appeal, or human review.

Every affected person must be able to inspect disclosed reasoning, challenge
evidence, submit contradictory evidence, and obtain a new receipt.

---

## 19. Governance Without a Truth Authority

### 19.1 Governance target

Governance maintains protocol integrity; it does not vote facts into existence.

### 19.2 Open governance model

- public specification;
- open-source reference kernel;
- public conformance test suite;
- independent implementations;
- published security audits;
- transparent change proposals;
- declared conflicts of interest;
- versioned domain contracts;
- reproducible validator packages;
- no proprietary hidden truth score;
- appeal and challenge protocol;
- emergency security process with expiring powers.

### 19.3 Validator admission

A validator is accepted because it passes public technical and domain tests,
not because its owner is prestigious. Certification includes:

- declared scope;
- known limitations;
- test vectors;
- reproducibility;
- implementation digest;
- independent review;
- expiration and revalidation;
- conflict-of-interest declaration where relevant.

### 19.4 Forkability

The protocol and receipts must remain independently verifiable if the original
organization becomes corrupt, insolvent, captured, or unavailable. No central
server may possess the only ability to interpret historical receipts.

---

## 20. MVP Definition

### 20.1 MVP scope

The first product MUST focus on a narrow, testable foundation:

1. local evidence vault;
2. Evidence DNA minting and verification;
3. parent/derivation graph;
4. correction and revocation propagation;
5. document, audio, image, and JSON ingestion;
6. information certificates IC-0 through IC-3;
7. claim atomization with human confirmation;
8. source-ancestry collapse;
9. contradiction graph;
10. three domain contracts:
    - formal calculation;
    - recorded-event reconstruction;
    - prediction registration and resolution;
11. signed Truth Receipts;
12. deterministic local verifier;
13. selective disclosure;
14. command-line tool, SDK, and review dashboard.

### 20.2 Explicit MVP exclusions

- universal autonomous truth determination;
- medical diagnosis;
- legal guilt decisions;
- public biometric identity;
- secret intelligence scoring;
- global public blockchain;
- automatic censorship;
- emotion or personality inference;
- hidden source reputation;
- unsupported numerical “truth percentages.”

---

## 21. Engineering Work Packages

### WP-1 — Formal specification

- define terms and invariants;
- publish JSON schemas;
- specify canonicalization and DNA calculation;
- create test vectors;
- specify status ceilings;
- map W3C PROV and C2PA.

### WP-2 — Cryptographic kernel

- hashing and signatures;
- key lifecycle;
- Merkle log;
- inclusion and consistency proofs;
- local verification;
- algorithm agility.

### WP-3 — Evidence vault

- encryption;
- content addressing;
- metadata separation;
- retention and erasure;
- backup and recovery;
- disclosure grants.

### WP-4 — DNA graph

- acquisition roots;
- derivation edges;
- mutation records;
- common-ancestry inference;
- contamination and revocation propagation;
- graph queries.

### WP-5 — Certification engine

- certificate contracts;
- C2PA and provenance adapters;
- capture attestation;
- reproduction workflow;
- certificate verification.

### WP-6 — Claim compiler

- claim schema;
- atomic decomposition;
- human confirmation interface;
- category-error detection;
- domain routing.

### WP-7 — Truth discovery kernel

- evidence relationships;
- contradiction detection;
- alternative hypotheses;
- falsification requests;
- status assignment;
- uncertainty representation.

### WP-8 — Domain plugins

- formal mathematics;
- software execution;
- recorded events;
- experimental science;
- historical reconstruction;
- prediction resolution.

### WP-9 — Review dashboard

- evidence graph visualization;
- source-root clustering;
- support/opposition matrix;
- missing evidence requests;
- alternative explanation comparison;
- receipt replay;
- correction and appeal.

### WP-10 — Assurance

- threat modeling;
- privacy engineering;
- cryptographic audit;
- adversarial testing;
- bias and misuse evaluation;
- legal deployment profiles;
- external conformance testing.

---

## 22. Acceptance Test Suite

### 22.1 Evidence DNA

```text
EDNA-001 Same canonical atom produces the same DNA identifier.
EDNA-002 One changed byte produces a different payload digest.
EDNA-003 An undeclared transformation fails lineage validation.
EDNA-004 A copy inherits the original acquisition root.
EDNA-005 A translation is not counted as independent evidence.
EDNA-006 An AI summary records model and source dependencies.
EDNA-007 Revoking a parent flags every descendant for reevaluation.
EDNA-008 Correction preserves the previous version and reason.
EDNA-009 Selective disclosure validates without exposing hidden fields.
EDNA-010 Personal payload never enters the public transparency log.
```

### 22.2 Information certification

```text
CERT-001 A valid signature certifies integrity but not truth.
CERT-002 A compromised device cannot receive IC-3 without valid attestation.
CERT-003 Missing transformation parameters block reproducibility status.
CERT-004 A second execution with identical inputs reproduces the digest.
CERT-005 One source reposted 1,000 times remains one evidential root.
CERT-006 Certificate wording names exactly what was established.
```

### 22.3 Truth discovery

```text
TRUTH-001 Complex claims are decomposed into independently evaluated atoms.
TRUTH-002 Prediction is never displayed as established fact before resolution.
TRUTH-003 Correlation cannot satisfy a causal contract without added evidence.
TRUTH-004 Psychological motive remains uncertain when only behavior is known.
TRUTH-005 A normative claim declares its value premises.
TRUTH-006 Strong contradictory evidence is preserved and displayed.
TRUTH-007 Removing the strongest source triggers a sensitivity reevaluation.
TRUTH-008 Unknown remains a successful valid output.
TRUTH-009 Formal proof is verified against exact axioms and checker version.
TRUTH-010 Every verdict is reproducible or explains why reproduction is limited.
```

### 22.4 Adversarial tests

```text
ADV-001 Deepfake with valid uploader signature is not certified as a real event.
ADV-002 Circular AI citations do not create independent confirmation.
ADV-003 Colluding sources with shared acquisition are clustered.
ADV-004 Prompt injection in evidence cannot modify policy or validators.
ADV-005 Staged capture remains identified as capture of an observed scene only.
ADV-006 Replayed sensor evidence fails nonce/freshness challenge.
ADV-007 Selective omission generates a missing-evidence warning.
ADV-008 Compromised validator results can be challenged by independent replay.
ADV-009 Transparency split-view is detected through consistency witnesses.
ADV-010 Key revocation prevents new certificates and marks affected scope.
```

---

## 23. Performance and Quality Metrics

Measure:

- deterministic verification success rate;
- false lineage merges and missed lineage links;
- source-root collapse precision and recall;
- contradiction detection coverage;
- unsupported-status escalation rate;
- percentage of receipts independently replayed;
- time to propagate correction and revocation;
- privacy disclosure violations;
- validator disagreement rate;
- unknown-state appropriateness;
- time and cost per evidence atom and receipt;
- user comprehension of certification versus truth;
- successful adversarial challenge rate;
- calibration of numerical predictions;
- domain expert agreement on contract application.

System success is not measured by how often it declares claims true. A high
rate of justified `UNVERIFIED` or `CURRENTLY_UNKNOWABLE` results may demonstrate
correct restraint.

---

## 24. Delivery Roadmap

### Phase 0 — Foundation, months 0–3

- establish multidisciplinary founding team;
- patent and prior-art review before public novelty claims;
- define constitution and threat model;
- publish EDNA v0.1 schema;
- create cryptographic test vectors;
- build local command-line verifier.

### Phase 1 — Evidence DNA MVP, months 4–7

- encrypted vault;
- acquisition and derivation atoms;
- signatures;
- corrections and revocations;
- graph viewer;
- document, image, audio, and JSON adapters.

### Phase 2 — Certification, months 8–11

- IC-0 through IC-3;
- C2PA and W3C PROV exchange;
- reproducible transformation certificates;
- local and consortium transparency modes;
- independent security audit.

### Phase 3 — Truth Discovery MVP, months 12–16

- claim compiler;
- source-root collapse;
- contradiction and falsification engines;
- recorded-event, formal, and prediction contracts;
- Truth Receipt v0.1;
- adversarial benchmark.

### Phase 4 — Domain pilots, months 17–24

- engineering incident pilot;
- scientific-claim pilot;
- meeting-transcript pilot;
- historical reconstruction pilot;
- external domain and legal review;
- public conformance suite.

### Phase 5 — Open protocol, months 25–36

- independent implementations;
- standards engagement;
- federated verification;
- selective-disclosure improvements;
- formal verification of critical kernel components;
- production certification profiles.

No phase may claim universal truth detection.

---

## 25. Team Requirements

The core team should include:

- cryptography and protocol engineering;
- distributed systems;
- formal methods;
- causal inference and statistics;
- epistemology and philosophy of science;
- information forensics;
- cybersecurity and adversarial ML;
- privacy engineering and data protection law;
- human-computer interaction;
- domain specialists for each validation contract;
- independent red-team and ethics review.

No single discipline can responsibly build the complete system.

---

## 26. Intellectual Property and Openness Strategy

### 26.1 Potentially differentiating invention areas

Subject to professional prior-art analysis:

- Evidence DNA inheritance and contamination semantics;
- automatic source-root collapse across human and AI derivatives;
- contract-based maximum truth-status ceilings;
- combined correction/revocation propagation through evidential descendants;
- truth receipts binding provenance, independence, falsification, alternatives,
  and uncertainty;
- cross-domain claim compilation without a universal opaque truth score;
- challenge-capture profiles for independent reality acquisition;
- privacy-preserving selective disclosure of evidential ancestry.

### 26.2 Recommended strategy

- keep the verification specification open;
- publish test vectors and a reference verifier;
- consider defensive patenting for genuinely novel mechanisms;
- avoid patent claims before a professional search;
- monetize deployment, domain validators, assurance, enterprise integration,
  private evidence vaults, and managed verification;
- prevent one organization from privately controlling the meaning of receipts.

An unverifiable proprietary truth engine would contradict ALETHEIA's purpose.

---

## 27. Failure Conditions

The project has failed if it:

- markets signatures as proof of truth;
- hides uncertainty behind a single number;
- uses popularity as independent evidence;
- allows AI models to modify evidence history;
- quietly discards contradictory evidence;
- treats predictions as facts;
- infers motive as certainty;
- builds a secret source reputation score;
- places personal evidence on an irreversible public ledger;
- cannot be independently verified;
- depends on one organization remaining honest;
- claims universal truth detection;
- becomes a censorship, guilt, or surveillance engine.

---

## 28. Standards and Research Foundation

ALETHEIA should reuse existing work rather than misrepresent existing
provenance mechanisms as new inventions:

- W3C PROV-O for interoperable provenance concepts:  
  https://www.w3.org/TR/prov-o/
- W3C Verifiable Credentials Data Model 2.0 for compatible credential
  disclosures:  
  https://www.w3.org/TR/vc-data-model-2.0/
- C2PA specifications for media provenance and content credentials:  
  https://spec.c2pa.org/specifications/specifications/2.2/index.html
- RFC 8785 JSON Canonicalization Scheme:  
  https://www.rfc-editor.org/rfc/rfc8785.html
- RFC 9162 Certificate Transparency Version 2.0 for transparency-log design
  patterns:  
  https://www.rfc-editor.org/rfc/rfc9162.html
- RFC 3161 Time-Stamp Protocol:  
  https://www.rfc-editor.org/rfc/rfc3161.html
- RFC 9334 Remote ATtestation procedureS architecture:  
  https://www.rfc-editor.org/rfc/rfc9334.html
- NIST AI Risk Management Framework:  
  https://www.nist.gov/itl/ai-risk-management-framework
- General Data Protection Regulation:  
  https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
- EU Artificial Intelligence Act:  
  https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng

Existing standards cover important parts of provenance, credentials,
attestation, content authenticity, transparency, and governance. ALETHEIA's
proposed contribution is their integration with Evidence DNA inheritance,
source-independence discovery, domain validation contracts, falsification, and
bounded Truth Receipts.

---

## 29. Final Product Definition

ALETHEIA consists of:

```text
ALETHEIA CORE
  Evidence DNA kernel
  Information certification engine
  Claim compiler
  Source independence resolver
  Contradiction and falsification engine
  Domain validator runtime
  Uncertainty and verdict kernel
  Truth Receipt generator and verifier

ALETHEIA VAULT
  Encrypted evidence storage
  Access, retention, correction, and erasure

ALETHEIA DESK
  Human review dashboard
  Evidence and dependency visualization
  Challenge and appeal workflow

ALETHEIA SDK
  Capture, certification, evaluation, and verification APIs

ALETHEIA PROTOCOL
  Open schemas, contracts, test vectors, and interoperability profiles
```

### Final operating principle

> Nobody gives truth to the system. Every participant supplies claims and
> evidence. Evidence DNA preserves what happened to the information.
> Information Certification verifies its integrity and method. Truth Discovery
> determines the strongest conclusion that survives dependency analysis,
> domain validation, contradiction, alternative explanations, and attempted
> falsification.

The system's highest achievement is not saying “true” more often. It is making
deception, dependency, uncertainty, and the boundary of knowledge visible
before humans or machines act.

---

## 30. Base-Layer Completion Rule

The base layer is a complete product and engineering specification, not an
executed implementation. Its foundation may be described as operational only
after:

1. schemas and cryptographic test vectors are published;
2. two independent implementations produce matching DNA identifiers;
3. correction and revocation propagation passes all tests;
4. information certificates are externally verified;
5. truth-status ceilings are enforced;
6. adversarial source-flooding and circular-citation tests pass;
7. domain validators receive independent expert review;
8. privacy, security, and legal assessments are complete;
9. receipts can be independently replayed;
10. all limitations remain visible in the user interface.

Until then, the honest status is:

```text
BLUEPRINT_COMPLETE
REFERENCE_IMPLEMENTATION_NOT_BUILT
SCIENTIFIC_VALIDATION_REQUIRED
SECURITY_REVIEW_REQUIRED
LEGAL_DEPLOYMENT_REVIEW_REQUIRED
```

---

# PART II — METACOGNITIVE TRUTH INTELLIGENCE

## 31. Why the Static Architecture Is Insufficient

Evidence certification and post-hoc claim evaluation are necessary but not
enough. A future truth system must recognize when it does not know, decide what
it must learn, obtain new evidence, challenge its own methods, revise beliefs,
and measure whether those revisions improve correspondence with reality.

A static verifier answers:

```text
What can the currently supplied evidence support?
```

A metacognitive truth intelligence must additionally answer:

```text
What am I missing?
Which part of my own process is unreliable?
Which alternative explanation have I neglected?
What observation would most reduce uncertainty?
Can that observation be acquired safely and lawfully?
Did my previous method fail in similar situations?
Should I continue, delegate, redesign the investigation, or stop?
```

ALETHEIA 2.0 therefore adds an external metacognitive control plane. It does
not rely on a language model simply announcing that it is confident or
uncertain. Model self-assessment is treated as one signal and calibrated
against actual historical performance.

---

## 32. Six-Plane Architecture

ALETHEIA 2.0 operates across six distinct planes:

```text
PLANE 1 — REALITY CONTACT
  sensors, experiments, human observations, robots, instruments, events

PLANE 2 — EVIDENCE AND INFORMATION
  Evidence DNA, certification, provenance, transformations, disclosure

PLANE 3 — SEMANTIC AND CAUSAL MEANING
  claims, definitions, entities, time, causality, dependencies, hypotheses

PLANE 4 — METACOGNITIVE CONTROL
  self-model, competence, uncertainty, strategy, stopping, escalation

PLANE 5 — ACTIVE DISCOVERY
  investigation, challenge, experiment design, observation, belief revision

PLANE 6 — GOVERNANCE AND ACTION
  authority, safety, legality, review, truth receipts, action admission
```

No plane may silently substitute for another:

- simulation is not observation;
- provenance is not truth;
- semantic coherence is not physical correspondence;
- model confidence is not calibrated competence;
- consensus is not independence;
- governance approval is not factual proof;
- truth support is not authorization to act.

### 32.1 Expanded product modules

```text
ALETHEIA SENSORIUM
  Reality acquisition, instrument control, challenge capture, calibration

ALETHEIA EDNA
  Evidence DNA, dependency genome, mutation, correction, revocation

ALETHEIA SEMANTIC FABRIC
  Claim compilation, ontology alignment, entity resolution, temporal logic

ALETHEIA CAUSAL LAB
  Hypotheses, mechanisms, interventions, counterfactuals, digital twins

ALETHEIA META
  Competence model, calibration, uncertainty, strategy and stopping control

ALETHEIA DISCOVERY ORCHESTRATOR
  Active investigation, experiment selection, delegation and evidence requests

ALETHEIA ADVERSARY
  Deception modeling, falsification, red teams, collusion and monoculture tests

ALETHEIA MEMORY
  Versioned beliefs, corrections, validity, expiry and dependency-aware recall

ALETHEIA VERDICT KERNEL
  Contract ceilings, bounded statuses, receipts and action gates

ALETHEIA FEDERATION
  Independent witnesses, selective disclosure and cross-node verification
```

---

## 33. Metacognitive Control Plane

### 33.1 Definition

Metacognition is the system's regulated knowledge about its own knowledge,
competence, methods, uncertainty, limitations, and investigation strategy.

It is not a generated paragraph saying “I reflected.” It is an executable
control system with measurable state, historical calibration, constraints, and
admission rules.

### 33.2 Metacognitive responsibilities

The control plane MUST:

1. estimate whether the system has the competence required by the claim;
2. distinguish missing evidence from conflicting evidence;
3. distinguish model uncertainty from measurement uncertainty;
4. select validators and investigative strategies;
5. monitor whether a strategy is reducing uncertainty;
6. detect circular reasoning and repeated failed approaches;
7. compare current performance with calibrated history;
8. determine when external expertise or new observation is required;
9. set a maximum verdict before evaluation begins;
10. decide whether to continue, pause, escalate, or stop;
11. record structured decision artifacts without exposing private hidden
    chain-of-thought;
12. learn from resolved predictions, reproduced experiments, challenges, and
    overturned receipts;
13. prevent self-improvement from rewriting evidence or weakening safeguards.

### 33.3 External control over model self-confidence

An AI model's verbal confidence MUST NOT control consequential routing. The
metacognitive controller calculates competence from:

- performance on comparable resolved tasks;
- domain and subdomain calibration;
- distribution-shift indicators;
- validator disagreement;
- missing-input profile;
- tool and sensor availability;
- reproducibility history;
- adversarial-test performance;
- rate of later correction or receipt reversal;
- uncertainty appropriate to the selected contract.

If the model says “95% confident” but fails 40% of similar tasks, routing uses
the measured history, not the statement.

### 33.4 Structured metacognitive record

```json
{
  "spec": "aletheia.meta-state.v1",
  "investigation_id": "investigation:sha256:<digest>",
  "claim_id": "claim:sha256:<digest>",
  "competence": {
    "required_domains": ["mechanical_engineering", "causal_inference"],
    "available_profiles": [
      {
        "component": "validator:vibration-analysis.v3",
        "in_distribution_accuracy": 0.94,
        "out_of_distribution_status": "unknown",
        "last_calibrated_at": "<timestamp>"
      }
    ],
    "gaps": ["bearing_materials_specialist"]
  },
  "uncertainty": {
    "measurement": "moderate",
    "model": "high",
    "structural": "high",
    "semantic": "low",
    "unknown_unknown_risk": "material"
  },
  "strategy": {
    "current": "acquire_independent_vibration_trace",
    "expected_information_gain": "high",
    "cost_class": "low",
    "risk_class": "low",
    "fallback": "physical_inspection"
  },
  "status_ceiling": "BEST_SUPPORTED_EXPLANATION",
  "stop_conditions": [
    "evidence cannot distinguish causal direction",
    "additional observation is unsafe or unlawful"
  ],
  "decision_summary": "Current temperature evidence cannot establish initiating cause."
}
```

### 33.5 No raw chain-of-thought requirement

ALETHEIA records auditable objects:

- claims;
- evidence references;
- hypotheses;
- selected tests;
- validator results;
- decision summaries;
- uncertainty;
- rejected alternatives and stated reasons;
- strategy changes.

It does not require a model's private token-by-token reasoning. Structured
justification is safer, more reproducible, and easier to validate than a
potentially misleading narrative of internal thought.

---

## 34. Epistemic State Vector

Every investigation maintains a multidimensional epistemic state:

```text
E = {
  claim_clarity,
  semantic_stability,
  evidence_integrity,
  provenance_completeness,
  acquisition_quality,
  source_independence,
  reproducibility,
  causal_identifiability,
  contradiction_severity,
  alternative_explanation_coverage,
  model_calibration,
  domain_competence,
  distribution_shift,
  temporal_freshness,
  adversarial_exposure,
  missingness,
  unknown_unknown_risk,
  action_reversibility
}
```

The vector supports control decisions. It is not compressed into a universal
truth percentage.

### 34.1 Uncertainty taxonomy

| Type | Meaning | Appropriate response |
|---|---|---|
| Measurement | Instrument or sampling imprecision | Calibrate, repeat, improve sensor |
| Aleatoric | Inherent variability | Represent distribution; do not promise elimination |
| Epistemic | Missing knowledge | Acquire evidence or experiment |
| Model | Competing models fit evidence | Compare, stress, intervene |
| Structural | Unknown causal or dependency structure | Causal discovery and sensitivity bounds |
| Semantic | Definitions or entities are unstable | Clarify claim and ontology |
| Temporal | Evidence is stale or order uncertain | Reobserve and reconstruct time |
| Adversarial | Evidence may be intentionally manipulated | Challenge capture and red-team |
| Normative | Depends on values or rules | Declare premises and jurisdiction |
| Computational | Exact evaluation is infeasible | Approximate with explicit bounds |
| Fundamental | In principle inaccessible or undecidable | Return currently or permanently unknowable |

### 34.2 Status ceiling

Before deep evaluation, the controller sets a maximum justified status.
Examples:

- unresolved future event → no higher than `PREDICTION_UNRESOLVED`;
- private motive inferred from behavior → no higher than
  `BEST_SUPPORTED_EXPLANATION`;
- uncalibrated single sensor → no higher than `PLAUSIBLE` for precise
  measurement;
- machine-checked theorem with declared axioms → may reach `FORMALLY_PROVEN`;
- normative judgment → `NORMATIVE_DEPENDS_ON_DECLARED_VALUES`.

This prevents confidence inflation late in the process.

---

## 35. Cognitive Role Mesh

ALETHEIA uses specialized roles with non-overlapping powers. Roles may be
implemented by deterministic software, statistical models, AI models, humans,
or instruments.

| Role | Responsibility | Prohibited power |
|---|---|---|
| Claim Compiler | Decompose and type claims | Cannot decide verdict |
| Semantic Examiner | Resolve definitions, entities, units and context | Cannot rewrite original evidence |
| Evidence Curator | Retrieve and bind relevant DNA | Cannot hide opposing roots |
| Independence Resolver | Collapse common ancestry and dependencies | Cannot certify content truth |
| Hypothesis Generator | Produce competing explanations | Cannot promote its own hypothesis |
| Causal Analyst | Test mechanisms and counterfactuals | Cannot infer motive as certainty |
| Methodologist | Select domain-valid tests | Cannot lower contract requirements |
| Experiment Designer | Propose information-gaining observations | Cannot authorize unsafe experiments |
| Skeptic | Seek disconfirmation and missing evidence | Cannot veto without a testable reason |
| Deception Analyst | Model staging, collusion and manipulation | Cannot accuse people without evidence |
| Calibration Monitor | Compare predicted and actual performance | Cannot alter historical outcomes |
| Synthesizer | Compose bounded conclusions | Cannot exceed status ceiling |
| Policy Guardian | Enforce privacy, safety, law and authority | Cannot declare empirical truth |
| Receipt Auditor | Replay and verify the package | Cannot silently repair failures |

### 35.1 Diversity is functional, not cosmetic

Using ten copies of the same model with different role prompts does not produce
ten independent minds. Diversity evaluation includes:

- model family and training-data overlap;
- method and algorithm diversity;
- deterministic versus learned validators;
- sensor and acquisition diversity;
- organizational and funding dependencies;
- prompt and tool-chain similarity;
- correlated historical failure patterns.

Agreement receives less weight when failures are strongly correlated.

### 35.2 Disagreement handling

Disagreement triggers:

1. semantic comparison to ensure the agents answered the same claim;
2. evidence-root comparison;
3. method comparison;
4. calibration weighting;
5. search for a discriminating observation;
6. preservation of unresolved alternatives.

The system must not force consensus when the evidence does not warrant it.

---

## 36. Autonomous Investigation State Machine

```text
RECEIVE_QUESTION
  → DEFINE_CLAIM
  → CLASSIFY_DOMAIN
  → SET_STATUS_CEILING
  → INVENTORY_KNOWN_EVIDENCE
  → MAP_DEPENDENCIES
  → GENERATE_ALTERNATIVES
  → SELECT_DISCRIMINATING_TEST
  → SAFETY_AND_AUTHORITY_GATE
  → ACQUIRE_OR_REQUEST_EVIDENCE
  → CERTIFY_INFORMATION
  → RUN_DOMAIN_VALIDATORS
  → ATTEMPT_FALSIFICATION
  → UPDATE_BELIEF_STATE
  → CHECK_CALIBRATION_AND_PROGRESS
       ↳ insufficient progress → redesign strategy
       ↳ unsafe/unavailable → stop with missing-evidence request
       ↳ decisive evidence → compile receipt
       ↳ contradiction → preserve contested result and continue if justified
  → HUMAN/INDEPENDENT_REVIEW_WHEN_REQUIRED
  → ISSUE_TRUTH_RECEIPT
  → MONITOR_FOR_CORRECTION_OR_EXPIRY
```

### 36.1 Continue/stop controller

The controller evaluates:

- expected reduction in decision-relevant uncertainty;
- cost and time;
- physical, legal and ethical risk;
- availability of safer alternatives;
- reversibility of the intended action;
- whether new evidence would change the verdict;
- diminishing returns;
- contractual deadline;
- privacy impact;
- whether the question is answerable at all.

The objective is not maximum data collection. It is sufficient, lawful,
decision-relevant evidence with minimum unnecessary intrusion.

### 36.2 Stop reasons

```text
ANSWERED_WITHIN_CONTRACT
INSUFFICIENT_EVIDENCE
CONFLICT_CANNOT_CURRENTLY_BE_RESOLVED
NO_SAFE_OR_LAWFUL_TEST
VALUE_OF_INFORMATION_TOO_LOW
CLAIM_NOT_OPERATIONALLY_DEFINED
DOMAIN_COMPETENCE_UNAVAILABLE
FUNDAMENTALLY_UNKNOWABLE
AUTHORITY_NOT_GRANTED
RESOURCE_LIMIT_REACHED
```

Every stop reason appears in the receipt.

---

## 37. Active Truth Discovery and Experiment Design

The dynamic system does not only search existing documents. It can propose or,
when authorized, coordinate new observations.

### 37.1 Evidence request types

- remeasure with calibrated instrument;
- obtain an independent capture perspective;
- collect a negative control;
- repeat an experiment with changed conditions;
- inspect a physical object;
- request an original rather than a derivative document;
- challenge a device with an unpredictable nonce;
- compare multiple laboratories;
- test a causal intervention;
- wait for a prediction's resolution condition;
- ask a human to clarify a definition rather than assume it;
- request expert review where competence is missing.

### 37.2 Value-of-information controller

For candidate observation or experiment `x`, estimate:

```text
VOI(x) = expected_decision_loss_before
       - expected_decision_loss_after_x
       - acquisition_cost
       - privacy_cost
       - safety_risk
       - delay_cost
```

VOI is used only when quantities are defensibly modeled. Otherwise the system
uses ordinal comparison with visible criteria.

### 37.3 Discriminating experiments

An experiment should separate leading hypotheses, not merely gather more of the
same evidence.

Example:

```text
H1: overheating caused bearing failure
H2: bearing failure caused overheating

Weak action: collect another temperature reading after failure.
Strong action: inspect wear pattern and retrieve pre-failure vibration phase.
```

### 37.4 Experiment safety case

No autonomous experiment proceeds without:

- declared objective;
- expected information gain;
- physical and biological risk assessment;
- legal and ethical authority;
- containment and stop conditions;
- human approval threshold;
- Evidence DNA for protocol, instruments, inputs and outputs;
- recovery and incident plan.

Experiments involving humans, animals, hazardous materials, medical treatment,
critical infrastructure, or irreversible actions require appropriate external
oversight.

---

## 38. Belief Revision Engine

### 38.1 Beliefs are versioned claims

ALETHEIA does not overwrite “knowledge.” It stores versioned claim states:

```text
claim
  status at time t
  supporting and opposing roots
  assumptions
  validity interval
  domain contract
  uncertainty
  revision triggers
  superseding state
```

### 38.2 Revision principles

1. Preserve prior receipts and context.
2. Identify exactly which new evidence caused revision.
3. Recalculate descendants of changed foundations.
4. Prefer the smallest justified revision, not total memory erasure.
5. Retain contradictions when they remain unresolved.
6. Do not protect prestigious conclusions from revision.
7. Do not accept new claims merely because they are recent.
8. Distinguish correction of fact, definition, model, method and policy.
9. Track whether revision improved later predictive or reproducibility results.
10. Penalize methods that repeatedly generate overturned high-confidence
    receipts.

### 38.3 Revision event

```json
{
  "spec": "aletheia.belief-revision.v1",
  "claim_id": "claim:sha256:<digest>",
  "previous_receipt": "truth:sha256:<old>",
  "new_evidence": ["edna:sha256:<new>"],
  "revision_type": "causal_model_changed",
  "affected_assumptions": ["temperature_preceded_mechanical_damage"],
  "new_status": "CONTESTED",
  "descendant_receipts_flagged": ["truth:sha256:<dependent>"],
  "replay_required": true,
  "issued_at": "<timestamp>"
}
```

### 38.4 Belief robustness tests

- leave-one-root-out analysis;
- alternative-prior analysis where Bayesian methods apply;
- definition sensitivity;
- hidden-confounder sensitivity;
- adversarial evidence removal;
- validator substitution;
- time-window sensitivity;
- model-family substitution;
- plausible data-corruption scenarios.

The receipt shows whether the conclusion is stable or fragile.

---

## 39. Epistemic Memory and Metamemory

### 39.1 Memory is not a text archive

ALETHEIA memory stores evidence and claim relationships, not only embeddings.
Every memory item has:

- Evidence DNA;
- claim relationship;
- validity interval;
- source-root cluster;
- confidence representation;
- contradiction links;
- access purpose;
- retention and consent;
- correction state;
- expiry/reobservation trigger;
- known failure modes;
- retrieval justification.

### 39.2 Metamemory

Metamemory records how trustworthy the memory process itself has been:

- retrieval miss rate;
- false similarity rate;
- stale-memory reuse;
- poisoning incidents;
- correction propagation latency;
- domain-specific recall quality;
- overreliance on internally generated memories;
- unresolved contradictions suppressed by ranking;
- percentage of retrieved evidence with independent roots.

### 39.3 Synthetic-memory quarantine

AI-generated summaries, plans and prior conclusions are stored as derivatives.
They cannot become primary evidence merely by being remembered. When retrieved,
their source ancestry must accompany them.

### 39.4 Dependency-aware forgetting

When information is erased, revoked or disproven:

1. locate every dependent memory and receipt;
2. remove or restrict protected payloads as required;
3. preserve lawful minimal commitments where justified;
4. invalidate derived caches;
5. recompute conclusions without the removed support;
6. mark any remaining model-weight influence that cannot be precisely removed;
7. prevent a generated summary from reconstructing erased content;
8. document residual risk.

---

## 40. Causal World Models and Digital Twins

### 40.1 Purpose

A world model represents possible mechanisms and predicts consequences. It is
a hypothesis environment, not reality itself.

ALETHEIA uses multiple competing world models to:

- test causal explanations;
- predict observations under interventions;
- identify contradictions;
- design discriminating experiments;
- simulate safety before physical action;
- detect when actual observations depart from expected behavior.

### 40.2 World Model DNA

Every world model records:

- training and calibration data roots;
- equations, architecture and parameters;
- assumptions and excluded variables;
- spatial and temporal scope;
- calibration interval;
- known failure regions;
- intervention semantics;
- simulation engine and hardware;
- validation against real observations;
- corrections and model succession.

### 40.3 Digital twin discipline

A digital twin must declare:

```text
TWIN STATE ≠ PHYSICAL STATE
SIMULATED OBSERVATION ≠ ACQUIRED EVIDENCE
MODEL FIT ≠ CAUSAL TRUTH
PREDICTIVE SUCCESS IN ONE REGIME ≠ GENERAL VALIDITY
```

The twin becomes valuable when prediction DNA is registered before observation
and continuously scored against independent reality.

### 40.4 Embodied discovery

Future robots and autonomous instruments can close the loop:

```text
hypothesis
  → safe experiment plan
  → physical action
  → attested sensing
  → Evidence DNA
  → causal update
  → independent replay or replication
```

The robot is not trusted because it is a robot. Its calibration, software,
hardware, control authority and environmental interaction all remain evidence
dependencies.

---

## 41. Temporal Truth and Reality Change

Truth claims may describe:

- an instantaneous event;
- a state valid during an interval;
- a continuing process;
- a recurring pattern;
- a historical sequence;
- a future condition;
- a timeless formal relationship.

### 41.1 Temporal claim fields

```text
observed_at
valid_from
valid_until
event_time_uncertainty
recording_time
publication_time
ingestion_time
correction_time
resolution_time
reobservation_due
```

The system MUST not confuse publication time with event time or current truth
with historical truth.

### 41.2 Truth decay and freshness

Some claims decay rapidly:

- current office holder;
- software vulnerability status;
- medical condition;
- market price;
- device configuration;
- weather;
- legal rule.

Others are event records whose underlying occurrence does not change, although
our evidence and interpretation may change. Each contract defines freshness
requirements and revalidation triggers.

### 41.3 Change-point detection

Continuous evidence streams can identify structural changes. Detection output
is an alert, not automatic causal explanation. The system opens a new claim
state and requests evidence explaining the transition.

---

## 42. Unknown-Unknown Discovery

No system can enumerate every unknown. ALETHEIA can nevertheless search for
signals that its current hypothesis set is incomplete.

### 42.1 Detection methods

- residual patterns unexplained by all current models;
- repeated out-of-distribution observations;
- cross-modal inconsistencies;
- failed predictions sharing no known cause;
- unexplained validator disagreement;
- new dependency clusters;
- anomalous missingness or synchronized silence;
- causal effects without represented mechanisms;
- sudden calibration collapse;
- adversarially generated counterexamples;
- novelty search across alternative ontologies.

### 42.2 Epistemic surprise record

An unexplained anomaly creates a record containing:

- observation roots;
- expected range under current models;
- degree and type of deviation;
- candidate artifact explanations;
- safety relevance;
- proposed follow-up observations;
- whether the anomaly has independent replication.

An anomaly is not automatically a discovery. It becomes a discovery candidate
after artifacts and known alternatives are tested.

### 42.3 Anti-dismissal protection

Novel evidence must not be rejected solely because it contradicts current
consensus. Conversely, contradiction with consensus does not make it true.
ALETHEIA protects the evidence, tests acquisition integrity, seeks replication,
and opens competing hypotheses without prematurely promoting them.

---

## 43. Advanced Dependency Genome

Evidence dependence extends beyond copying. ALETHEIA models:

```text
DERIVATION DEPENDENCY     copied, summarized, transformed
DATA DEPENDENCY           same dataset or sample population
METHOD DEPENDENCY         same instrument, software or protocol
MODEL DEPENDENCY          same weights, architecture or training lineage
HUMAN DEPENDENCY          shared author, operator, witness or analyst
ORGANIZATIONAL DEPENDENCY shared ownership, funding or command
TEMPORAL DEPENDENCY       one report influenced later observation/reporting
SEMANTIC DEPENDENCY       same definition, ontology or framing assumption
CAUSAL DEPENDENCY         same physical cause generated multiple observations
INCENTIVE DEPENDENCY      common reward, pressure, coercion or liability
INFRASTRUCTURE DEPENDENCY same cloud, time source, network or supply chain
```

### 43.1 Hypergraph model

Simple pairwise graphs cannot represent every shared dependency. ALETHEIA uses
a hypergraph where one hidden dependency may connect many sources.

```text
hyperedge H:
  members = [source_1, source_2, source_3]
  dependency_type = SHARED_DATASET
  basis = [declared_metadata, code_similarity, publication chronology]
  status = INFERRED
  uncertainty = <declared representation>
```

### 43.2 Independence certificate expansion

The certificate reports independence by dimension rather than using one label:

```text
acquisition independence: high
organizational independence: moderate
method independence: low
model independence: low
funding independence: unknown
temporal independence: low
```

### 43.3 Evidence fan-out and laundering

The system detects when one weak source is converted into apparent authority
through:

```text
anonymous post
  → AI summary
  → news article citing "online reports"
  → database ingestion
  → research assistant output
  → multiple agents citing database and article
```

All descendants remain linked to the original weak root.

---

## 44. Synthetic Consensus and Epistemic Monoculture Defense

### 44.1 Problem

Future information ecosystems will contain enormous volumes of AI-generated
material. Apparent agreement may be produced by common training data, common
models, copied outputs, shared retrieval indexes, or reinforcement from prior
AI content.

### 44.2 Model ancestry passport

Where available, every AI output includes:

- provider and model claim;
- model artifact or release digest;
- base-model family;
- training-data disclosure level;
- fine-tuning and adapter ancestry;
- system prompt and tool policy digest;
- retrieval roots;
- generation parameters;
- other model outputs used;
- confidence calibration profile;
- known correlated-failure groups.

Unavailable fields remain unknown rather than guessed.

### 44.3 Correlated-error matrix

ALETHEIA maintains empirical correlations between validators and models on
resolved tasks. Ensemble support is discounted when error patterns correlate,
even when vendors are different.

### 44.4 Reality reserve

Critical domains should maintain a protected “reality reserve” of:

- independently captured raw observations;
- physical reference materials;
- reproducible experiments;
- human-created and historically anchored records;
- calibrated benchmark environments;
- pre-AI and verified-origin datasets;
- negative and failed-result archives.

The reserve is not assumed infallible. It prevents complete dependence on a
self-referential synthetic information ecosystem.

### 44.5 Synthetic-content rule

Synthetic evidence may be useful for hypothesis generation, simulation,
education and stress testing. It cannot independently establish that the
simulated or described external event occurred.

---

## 45. Governed Self-Improvement

### 45.1 What may improve

ALETHEIA may propose improvements to:

- claim decomposition;
- source-root discovery;
- retrieval strategies;
- validator routing;
- anomaly detection;
- experiment selection;
- calibration models;
- user explanations;
- performance and resource usage.

### 45.2 What may not self-modify without controlled release

- the system constitution;
- truth-status definitions;
- cryptographic verification rules;
- evidence immutability;
- privacy and authority gates;
- audit requirements;
- prohibited use boundaries;
- production signing policy;
- domain-contract ceilings.

### 45.3 Improvement promotion pipeline

```text
observed failure
  → Evidence DNA trace
  → root-cause hypothesis
  → candidate improvement
  → isolated benchmark
  → adversarial regression suite
  → cross-domain side-effect test
  → independent implementation/review
  → signed release proposal
  → controlled canary deployment
  → calibrated outcome monitoring
  → promotion, rollback or rejection
```

### 45.4 Self-reference protection

The system cannot validate a new validator solely using outputs generated by
that validator. At least one external benchmark, formal property, independent
implementation, or reality-grounded outcome is required.

### 45.5 Reward protection

Optimization targets must not reward:

- declaring more claims true;
- agreeing with users or authorities;
- reducing unknown outputs without evidence;
- maximizing engagement;
- avoiding corrections;
- hiding contradictory evidence;
- completing investigations quickly at the expense of validity.

Preferred objectives include calibration, reproducibility, correct restraint,
challenge survival, correction speed, privacy preservation and decision loss.

---

## 46. Intelligence and Safety Invariants

The following invariants should be formally specified and tested:

```text
INV-01 No evidence atom changes after its DNA identifier is minted.
INV-02 Every derivative has complete declared parent links.
INV-03 Revoked support cannot silently remain active in a current receipt.
INV-04 No role can both create evidence and independently certify its acquisition.
INV-05 No AI output becomes primary evidence through storage or repetition.
INV-06 No verdict exceeds its predeclared status ceiling.
INV-07 Every consequential verdict exposes material contradiction and uncertainty.
INV-08 Every active experiment passes authority and safety admission.
INV-09 Every policy or validator change has versioned provenance and rollback.
INV-10 Unknown is never converted into false certainty by majority vote.
INV-11 Normative premises never masquerade as empirical observations.
INV-12 Simulation output never masquerades as physical capture.
INV-13 Private evidence is not disclosed beyond its purpose and grant.
INV-14 A compromised component reduces assurance instead of being ignored.
INV-15 The verifier can operate independently of the original issuing service.
```

### 46.1 Graceful degradation

When components fail, ALETHEIA must degrade status, not fabricate continuity.

Examples:

- unavailable timestamp witness → temporal assurance decreases;
- unverified model ancestry → model-independence status becomes unknown;
- missing calibration → precise quantitative status blocked;
- failed transparency witness → local receipt remains verifiable but public-log
  assurance is suspended;
- no domain expert → automated result remains provisional.

---

# PART III — FUTURE TECHNOLOGY HORIZON

## 47. Technology Horizon Map

The roadmap distinguishes present engineering, emerging technology, and
speculative research. Dates are planning ranges, not predictions.

| Technology | Near term | Medium term | Long term contribution | Main caution |
|---|---|---|---|---|
| Hardware-backed capture | Signed sensors and secure keys | Multi-sensor attestation | Ubiquitous evidence-native devices | Compromised hardware can sign lies |
| Confidential computing | Protected validator execution | Cross-provider attestation | Private federated truth computation | TEE bugs and vendor trust |
| Post-quantum cryptography | Hybrid signatures and key exchange | Broad migration | Long-lived evidence verification | Implementation and migration errors |
| Zero-knowledge proofs | Selective facts and private membership | Private method compliance | Cross-border verification without disclosure | Complex circuits and setup assumptions |
| Multimodal foundation models | Claim extraction and media analysis | Rich cross-modal anomaly detection | General semantic interfaces to evidence | Hallucination and common-model errors |
| Causal world models | Domain pilots | Adaptive experiment selection | Embodied scientific discovery | Model is not reality |
| Autonomous laboratories | Controlled materials/chemistry workflows | Multi-lab replication networks | Continuous evidence generation | Safety, bias and replication governance |
| Robotics | Inspections and repeatable capture | Independent field investigation | Embodied truth discovery | Physical safety and capture compromise |
| Edge AI | Local transcription and forensics | Evidence-native personal devices | Private distributed verification | Resource limits and update integrity |
| Digital twins | Predictive maintenance | Causal intervention planning | Large-scale infrastructure modeling | False confidence from model fit |
| Quantum sensing | Specialized precision measurement | Portable high-sensitivity instruments | New observation regimes | Calibration and environmental noise |
| Quantum computing | Specialized simulation/optimization | Selected scientific workloads | Possible new proof and modeling capacity | Does not automatically discover truth |
| Neuromorphic computing | Low-power anomaly detection | Always-on sensory reasoning | Large-scale event-driven reality monitoring | New verification methods needed |
| Satellite and geospatial sensing | Independent time/location evidence | Persistent multimodal Earth observation | Planetary event reconstruction | Coverage, ownership and interpretation bias |
| Molecular and biological recording | Research-stage event logging | Specialized environmental/medical sensing | Long-lived physical event records | Ethics, mutation, contamination and privacy |
| Spatial computing | 3D capture and scene reconstruction | Shared reality maps | Rich embodied evidence contexts | Manipulated overlays and identity risk |
| Brain-computer interfaces | Limited clinical signals | New communication evidence | Directer access to some neural activity | Neural data is not direct proof of intention |

### 47.1 Technology adoption gate

New technology enters ALETHEIA only after:

- its exact contribution is defined;
- its failure modes are documented;
- evidence and trust boundaries are explicit;
- independent validation exists;
- privacy and rights impacts are assessed;
- fallback behavior is tested;
- it does not receive truth authority merely because it is advanced.

---

## 48. Evidence-Native Hardware and Physical Roots

### 48.1 Evidence-native device

Future cameras, microphones, instruments and robots should generate Evidence
DNA at the point of acquisition.

Required capabilities:

- secure boot and measured software state;
- protected device keys;
- monotonic event counter;
- sensor calibration identifier;
- signed configuration;
- chunk-level hashing;
- capture interruption records;
- challenge nonce support;
- optional trusted time and location commitments;
- local encryption;
- privacy indicator and consent input;
- export to C2PA and ALETHEIA formats;
- post-quantum migration path.

### 48.2 Sensor fusion without false independence

Multiple sensors on one device may share power, clock, software and operator.
They provide cross-modal evidence but not full acquisition independence. The
dependency genome records shared roots.

### 48.3 Physical unclonable and tamper-evident features

Hardware identity mechanisms may strengthen device continuity but do not prove
that the observed scene was unstaged. Assurance statements must remain narrow.

### 48.4 Witness beacons

Independent local beacons can issue time-bounded challenge commitments to
nearby devices. A capture may prove that a device responded to a challenge in a
time window without publicly revealing precise location or identity. This is a
research profile requiring privacy analysis.

---

## 49. Confidential and Verifiable Computation

### 49.1 Confidential validation

Sensitive evidence may be processed in a trusted execution environment or
secure multi-party system. The receipt can include attestation evidence showing
which approved code processed protected inputs.

Attestation proves a claimed execution environment under its trust assumptions.
It does not prove the code is correct, the hardware has no flaw, or the input
corresponds to reality.

### 49.2 Zero-knowledge profiles

Potential future proofs include:

- evidence timestamp falls within an allowed interval;
- a measurement exceeds a threshold without revealing the exact value;
- a validator ran on committed input and produced committed output;
- two records belong to the same certified acquisition series;
- a person holds an appropriate credential without public identity disclosure;
- an aggregate statistic was calculated from eligible committed records.

### 49.3 Secure multi-party truth computation

Organizations can jointly evaluate a claim without sharing raw evidence. The
result must still expose method, assumptions, participant threshold,
independence limitations and possible collusion.

### 49.4 Compute receipt

Every protected computation should bind:

```text
input commitments
code and configuration digest
execution environment attestation
output commitment
privacy method
failure and leakage assumptions
time
signatures
```

---

## 50. Post-Quantum and Long-Term Evidence Survival

Evidence may need verification for decades. ALETHEIA must prepare for algorithm
failure, expired certificates, lost keys and format obsolescence.

### 50.1 Migration strategy

- algorithm identifiers in every record;
- hybrid classical and post-quantum signatures during transition;
- ML-DSA and SLH-DSA profiles subject to deployment review;
- periodic cryptographic renewal before algorithms weaken;
- hash-agile commitments and Merkle re-anchoring;
- preservation of original signatures and renewal evidence;
- offline verification packages;
- multiple independent archives;
- canonical format migration with transformation DNA;
- long-term timestamp renewal.

### 50.2 Renewal does not rewrite history

A 2035 post-quantum signature over a 2026 receipt proves renewal in 2035. It
must not be presented as though the post-quantum signature existed in 2026.

### 50.3 Quantum technology boundary

Quantum computers may improve certain simulations or optimization tasks and
threaten older cryptography. Quantum sensors may improve measurement. Neither
technology becomes an oracle. Evidence, calibration, models and interpretations
remain fallible.

---

## 51. Federated Reality Observatory

### 51.1 Purpose

The future network is a federation of independently operated ALETHEIA nodes,
not a central Ministry of Truth.

Nodes may be operated by:

- individuals;
- universities;
- laboratories;
- journalists;
- courts and public institutions;
- companies;
- civil society;
- sensor networks;
- autonomous laboratories;
- archives.

### 51.2 Federation protocol

Nodes exchange:

- public Evidence DNA commitments;
- selective disclosures;
- certificate and receipt proofs;
- challenge requests;
- replication offers;
- correction and revocation events;
- transparency consistency proofs;
- validator conformance evidence.

They do not exchange unnecessary raw personal evidence.

### 51.3 No consensus-as-truth

Distributed consensus can establish agreement about the order and contents of
a log. It cannot make a false proposition true. Federation consensus is used
for record consistency, not factual adjudication.

### 51.4 Witness diversity

The federation measures operational independence across:

- jurisdiction;
- ownership;
- hardware;
- software;
- model family;
- acquisition method;
- funding;
- network path;
- physical location;
- time source.

### 51.5 Split-view resistance

Transparency witnesses gossip log checkpoints and compare consistency proofs.
Conflicting views trigger an incident record and suspend affected assurance.

---

## 52. Multimodal Reality Reconstruction

### 52.1 Unified event graph

An event may generate:

- audio;
- video;
- images;
- environmental sensor traces;
- network and device logs;
- documents;
- physical damage;
- biological evidence;
- witness statements;
- later consequences.

ALETHEIA aligns these streams by time, space, entities and causal constraints.

### 52.2 Reconstruction steps

1. preserve each modality's independent DNA;
2. correct clock offset with visible uncertainty;
3. resolve entities without merging uncertain identities;
4. construct candidate event sequences;
5. enforce physical feasibility constraints;
6. compare predictions with observations;
7. identify missing intervals and blind spots;
8. test staging and replay alternatives;
9. retain multiple viable reconstructions;
10. issue atomized conclusions rather than one narrative.

### 52.3 Generative reconstruction boundary

Generated visualizations must be visibly synthetic and linked to the hypotheses
they illustrate. They are explanatory artifacts, not newly captured evidence.

---

## 53. Human Epistemic Sovereignty

ALETHEIA should increase human capacity to understand and challenge evidence,
not cause cognitive surrender.

### 53.1 Cognitive forcing functions

For consequential conclusions, the interface asks the reviewer to confirm:

- the exact claim;
- strongest supporting root;
- strongest opposing root;
- major dependency;
- most important unknown;
- alternative explanation;
- consequence of being wrong;
- whether the action is reversible.

### 53.2 Layered explanation

```text
LEVEL 1  verdict and limitation
LEVEL 2  evidence roots and contradictions
LEVEL 3  dependency and independence graph
LEVEL 4  methods, assumptions and uncertainty
LEVEL 5  replayable technical package
```

### 53.3 Contest and appeal

An affected person can:

- challenge identity or interpretation;
- submit new Evidence DNA;
- expose a hidden dependency;
- challenge a validator or definition;
- request an independent replay;
- request correction or revocation;
- receive a versioned response.

An appeal does not delete prior evidence or guarantee reversal. It opens a
traceable new evaluation.

### 53.4 Preservation of human expertise

The system tracks when users merely accept outputs versus meaningfully review
them. High-risk workflows should require evidence comprehension, not a cosmetic
checkbox.

---

## 54. Political and Economic Capture Resistance

### 54.1 Capture threats

- governments redefining permitted truth statuses;
- companies hiding unfavorable evidence;
- funders influencing domain contracts;
- insurers or employers using receipts outside declared purpose;
- validator monopolies;
- pay-to-certify markets;
- denial-of-service against minority evidence;
- legal pressure to remove valid contradictions;
- economic incentives to maximize reassuring verdicts.

### 54.2 Structural defenses

- open verifier and schemas;
- forkable protocol;
- multi-organization governance;
- conflict-of-interest DNA;
- public contract changes;
- independent mirrors and archives;
- threshold signing;
- mandatory opposing-evidence disclosure;
- no paid increase in truth status;
- anti-retaliation and protected challenge channels;
- jurisdictional transparency;
- public statistics on receipt corrections and reversals.

### 54.3 Funding independence record

Research and validation receipts can include disclosed funding and material
conflict relationships. Missing disclosure lowers independence assurance but
does not automatically refute the result.

### 54.4 Market incentives

Prediction markets, staking and insurance may contribute information, but money
does not determine truth. Wealth, coordination and manipulation can distort
markets. Market signals are evidence with their own dependency and incentive
model.

---

## 55. Expanded Domain Intelligence

The plugin framework should eventually support:

### 55.1 Chemistry and materials

- sample and reagent DNA;
- instrument calibration;
- reaction conditions;
- spectroscopy and microscopy provenance;
- simulation versus synthesis distinction;
- laboratory replication;
- contamination and batch effects.

### 55.2 Climate and environmental science

- sensor-station continuity;
- spatial coverage;
- proxy reconstruction;
- model ensembles with dependency analysis;
- scenario versus forecast distinction;
- observation-model residuals;
- long temporal validity.

### 55.3 Economics and finance

- changing definitions and denominators;
- revisions to official statistics;
- reflexivity and behavior change;
- regime shifts;
- incentive and market-manipulation evidence;
- forecast registration;
- causal limits of observational data.

### 55.4 Journalism and public events

- original-source retrieval;
- eyewitness and media DNA;
- geolocation and chronology;
- independence collapse;
- editorial transformations;
- right of reply;
- correction propagation;
- separation of report, analysis and opinion.

### 55.5 Forensics

- chain of custody;
- contamination risk;
- validated methods and error rates;
- examiner blinding;
- alternative hypotheses;
- legal admissibility separated from scientific strength;
- no automated guilt verdict.

### 55.6 Geospatial intelligence

- satellite and ground-sensor DNA;
- orbital and weather constraints;
- image time and location;
- independent provider analysis;
- synthetic-aperture, optical and thermal cross-modal comparison;
- map and boundary versioning.

### 55.7 Linguistics and translation

- original utterance preservation;
- dialect and context;
- translation alternatives;
- semantic loss;
- speaker intention distinguished from literal wording;
- human correction and interpretive uncertainty.

### 55.8 Sociology and social systems

- sampling and representation;
- measurement invariance;
- institutional incentives;
- observer effects;
- historical and cultural context;
- group averages not converted into individual facts;
- normative assumptions exposed.

---

## 56. Truth-to-Action Admission Layer

A supported claim does not automatically authorize an action. ALETHEIA adds a
separate admission decision:

```text
truth status
  + authority
  + intended purpose
  + consequence severity
  + reversibility
  + affected rights
  + legal and policy requirements
  + uncertainty tolerance
  → ALLOW / REQUIRE_REVIEW / REQUIRE_MORE_EVIDENCE / DENY
```

### 56.1 Evidence thresholds vary by action

The same evidence might be sufficient to:

- open an investigation;
- request a non-invasive inspection;

but insufficient to:

- accuse a person publicly;
- deny employment;
- administer medical treatment;
- execute a financial transfer;
- control critical infrastructure.

### 56.2 Reversibility principle

Irreversible, rights-affecting or high-impact actions require stronger evidence,
more independent review and narrower uncertainty than reversible exploratory
actions.

### 56.3 Action DNA

Every consequential action records:

- truth receipt used;
- authority and delegation;
- policy version;
- reviewer approvals;
- expected effect;
- reversibility and rollback;
- actual outcome;
- later corrections;
- learning signal for calibration.

This closes the loop between evidence, belief, decision, action and reality.

---

## 57. Mathematical and Algorithmic Control Framework

### 57.1 Multi-hypothesis state

Maintain a set `H = {h1, h2, ..., hn}` rather than one narrative. For each
hypothesis store:

```text
predicted observations
supporting roots
contradicting roots
assumptions
causal structure
domain validity
unexplained residuals
tests capable of discrimination
```

### 57.2 Dependence-adjusted support

For evidence root `i`, a domain-specific contribution may use:

```text
w_i = acquisition_i
    × integrity_i
    × relevance_i
    × method_validity_i
    × freshness_i
    × adversarial_robustness_i
    × dependence_discount_i
```

This is a framework, not a universal formula. Domains must define scales and
combination rules. Zero in one critical component may block use rather than be
averaged away.

### 57.3 Bayesian use

Bayesian updating is appropriate when hypotheses, priors and likelihood models
are defensible. Receipts must expose sensitivity to reasonable alternative
priors and model misspecification. A posterior is conditional on the model, not
an unconditional truth probability.

### 57.4 Robust and imprecise probability

When precise priors or likelihoods are unjustified, use:

- probability intervals;
- credal sets;
- likelihood ratios;
- partial identification;
- minimax or distributionally robust bounds;
- qualitative ordering.

### 57.5 Calibration

For predictions and probabilistic validators, measure:

- reliability curves;
- Brier or log scores where appropriate;
- calibration error by domain and subgroup;
- sharpness;
- selective prediction performance;
- confident failure rate;
- degradation under distribution shift.

### 57.6 Competence routing

```text
if task_outside_calibrated_domain:
    lower_status_ceiling()
    route_to_specialist_or_independent_validator()
    request_new_evidence_if_decision_relevant()
```

### 57.7 Progress monitor

An investigation is progressing only if it improves at least one of:

- claim clarity;
- independent evidence;
- causal discrimination;
- contradiction resolution;
- uncertainty bounds;
- validator calibration;
- decision relevance.

More tokens, sources or agents do not by themselves count as progress.

---

## 58. Expanded Epistemic Threat Register

| Threat | Mechanism | Detection | Response |
|---|---|---|---|
| Evidence flooding | Billions of copies overwhelm retrieval | Root ancestry and fan-out detection | Collapse to one root |
| Synthetic consensus | Related models repeat same error | Correlated-error and model lineage | Discount agreement, seek reality root |
| Semantic drift | Terms change during argument | Definition DNA and claim compiler | Split claims and re-evaluate |
| Staged reality | Genuine capture of deliberately fabricated scene | Physical consequence and challenge analysis | Narrow certificate; seek independent context |
| Validator capture | Corrupt method or implementation | Independent replay and benchmark drift | Revoke validator and replay descendants |
| Calibration laundering | Global accuracy hides subgroup failure | Domain/subgroup calibration | Restrict competence profile |
| Unknown suppression | Interface forces yes/no | Status-ceiling invariant | Preserve unknown |
| Citation laundering | AI text cites derivatives as independent | Dependency genome | Restore original root |
| Temporal laundering | Old evidence presented as current | Validity and freshness contracts | Expire and reobserve |
| Selective absence | Contrary data not collected or published | Missingness and preregistration analysis | Downgrade and request negatives |
| Ontology attack | Category definitions manipulated | Semantic version comparison | Expose alternative definitions |
| Sensor cartel | Independent brands share compromised supplier | Supply-chain dependency analysis | Seek diverse acquisition |
| Self-training collapse | Models learn from synthetic descendants | Model/data DNA | Quarantine and reality reserve |
| Reward capture | System optimized to confirm sponsor | Objective and funding DNA | Independent governance and audits |
| Overformalization | Valid proof applied to false empirical assumptions | Plane separation | Validate assumption-to-reality bridge |
| False transparency | Huge logs conceal decisive weakness | Materiality-focused receipt | Surface critical bottleneck |

---

## 59. Benchmark and Evaluation Program

### 59.1 ALETHEIA-Bench families

```text
BENCH-A  Evidence integrity and lineage
BENCH-B  Common-source and derivative collapse
BENCH-C  Contradiction and alternative explanation
BENCH-D  Domain contract correctness
BENCH-E  Metacognitive competence and routing
BENCH-F  Active experiment selection
BENCH-G  Belief revision and correction propagation
BENCH-H  Synthetic consensus and model monoculture
BENCH-I  Multimodal event reconstruction
BENCH-J  Privacy and selective disclosure
BENCH-K  Federation and split-view resistance
BENCH-L  Truth-to-action admission
```

### 59.2 Metacognitive tests

```text
META-001 Recognizes task outside calibrated competence.
META-002 Delegates instead of producing confident unsupported verdict.
META-003 Selects evidence that discriminates hypotheses.
META-004 Stops when no safe lawful evidence path exists.
META-005 Does not confuse repeated work with progress.
META-006 Revises belief after foundation evidence is revoked.
META-007 Preserves a minority hypothesis when still viable.
META-008 Learns calibration from resolved outcomes without rewriting history.
META-009 Detects its validator-disagreement pattern as a method risk.
META-010 Maintains unknown when every available source shares one root.
```

### 59.3 Future-tech tests

```text
FUT-001 Hybrid post-quantum renewal preserves original history.
FUT-002 TEE attestation is not misreported as code correctness.
FUT-003 Zero-knowledge disclosure proves only its exact statement.
FUT-004 Robot capture records software, sensor and action DNA.
FUT-005 Digital-twin output remains labeled simulation.
FUT-006 Quantum-sensor precision includes calibration and noise.
FUT-007 Federation disagreement remains visible.
FUT-008 Public log contains commitments, not protected personal evidence.
```

### 59.4 Real-world challenge program

Independent teams should attempt to:

- manufacture fake consensus;
- create staged but cryptographically valid capture;
- poison long-term memory;
- hide common source ancestry;
- corrupt a validator;
- exploit a semantic definition change;
- cause unjustified status escalation;
- reconstruct erased content;
- split transparency views;
- induce unsafe experiments;
- capture governance through funding or volume.

Results, failures and corrections must be published without leaking protected
evidence.

---

## 60. Capability Maturity Levels

| Level | Capability | Entry requirement | Prohibited claim |
|---:|---|---|---|
| L0 | Integrity | Hash and signature validation | Truth certified |
| L1 | Provenance | Acquisition and transformation lineage | Source is honest |
| L2 | Dependency | Common-root and mutation graph | Multiple copies are independent |
| L3 | Claim intelligence | Atomic claims and domain routing | Universal semantics solved |
| L4 | Bounded truth discovery | Domain validators and receipts | Absolute truth detector |
| L5 | Metacognitive control | Calibrated competence and strategy | Model self-confidence is reliable |
| L6 | Active discovery | Safe evidence requests and experiments | Autonomous unrestricted experimentation |
| L7 | Embodied/federated discovery | Robots, instruments and independent nodes | Network consensus equals truth |
| L8 | Governed self-improvement | Audited promotion and rollback | Self-modification is automatically progress |
| L9 | Societal infrastructure | Open verification, appeal and capture resistance | Final authority over public truth |

Each level inherits all lower-level invariants. Marketing must state the actual
achieved level and evidence.

---

## 61. Ten-Year Development Horizon

### Horizon A — Years 0–2: verifiable foundation

- EDNA v1 specification and test vectors;
- local vault and verifier;
- source-root dependency engine;
- document, media and meeting pilots;
- bounded domain contracts;
- receipt replay;
- independent security review;
- initial post-quantum migration profile.

### Horizon B — Years 2–4: metacognitive investigation

- calibrated competence profiles;
- active evidence requests;
- experiment-value controller;
- structured belief revision;
- synthetic-consensus benchmark;
- causal-model comparison;
- cross-organization federation pilots.

### Horizon C — Years 4–6: embodied evidence network

- evidence-native instruments;
- robot inspection profiles;
- autonomous-laboratory interfaces;
- confidential verification;
- selective-disclosure proofs;
- spatial and geospatial reconstruction;
- reality-reserve governance.

### Horizon D — Years 6–8: large-scale epistemic infrastructure

- independent public verifiers;
- multi-domain causal discovery;
- continuous prediction calibration;
- infrastructure digital twins bound to real observations;
- cross-border private evidence verification;
- broad post-quantum renewal.

### Horizon E — Years 8–10+: adaptive truth ecosystem

- self-improving but constitution-bound validators;
- globally federated evidence challenge and replication;
- advanced quantum/neuromorphic sensor integration where mature;
- autonomous discovery under strict safety cases;
- mature societal contest, appeal and anti-capture institutions.

The horizon must be revised annually through Prediction DNA rather than
presented as certainty.

---

## 62. Reference Repository Architecture

```text
aletheia/
├── constitution/
│   ├── invariants/
│   ├── prohibited_claims/
│   └── status_definitions/
├── specs/
│   ├── edna/
│   ├── certificates/
│   ├── claims/
│   ├── meta_state/
│   ├── truth_receipts/
│   ├── action_dna/
│   └── federation/
├── kernel/
│   ├── canonicalization/
│   ├── crypto/
│   ├── graph/
│   ├── policy/
│   ├── verdict/
│   └── replay/
├── cognition/
│   ├── claim_compiler/
│   ├── competence/
│   ├── uncertainty/
│   ├── hypotheses/
│   ├── causal/
│   ├── strategy/
│   └── belief_revision/
├── discovery/
│   ├── evidence_requests/
│   ├── experiment_design/
│   ├── safety_gate/
│   └── embodied_adapters/
├── adversary/
│   ├── collusion/
│   ├── synthetic_consensus/
│   ├── deepfake/
│   ├── prompt_injection/
│   └── red_team/
├── domain_contracts/
│   ├── formal/
│   ├── engineering/
│   ├── science/
│   ├── recorded_events/
│   ├── history/
│   └── prediction/
├── adapters/
│   ├── c2pa/
│   ├── w3c_prov/
│   ├── rats/
│   ├── sensors/
│   ├── robots/
│   └── local_models/
├── vault/
├── federation/
├── dashboard/
├── sdk/
├── test_vectors/
├── benchmarks/
└── audits/
```

### 62.1 Separation requirements

- AI model packages cannot be linked into the immutable cryptographic kernel.
- Domain plugins run with declared permissions.
- Evidence parsing occurs in a sandbox.
- Production signing is isolated from analysis.
- Test fixtures never masquerade as real evidence.
- Benchmarks identify synthetic content explicitly.

---

## 63. Expanded Innovation Inventory

Potentially protectable or standardizable mechanisms, subject to professional
prior-art analysis, include:

1. Evidence DNA genome with multidimensional dependency inheritance.
2. Transformation mutation records across human, algorithmic and AI processes.
3. Contamination and revocation propagation with bounded recomputation.
4. Source-root collapse across text, media, model and institutional ancestry.
5. Metacognitive status ceilings based on claim class and measured competence.
6. Dynamic investigation planning driven by decision-relevant information gain.
7. Structured metamemory that measures the reliability of memory itself.
8. Reality-reserve architecture protecting against synthetic epistemic collapse.
9. Correlated model-failure passports and independence-adjusted agent agreement.
10. Truth Receipt binding alternatives, falsification, competence and strategy.
11. Action DNA connecting evidence, verdict, authorization and observed outcome.
12. Privacy-preserving witness challenges for reality acquisition.
13. Dependency-aware lawful forgetting and downstream receipt invalidation.
14. Technology-neutral capability maturity levels that prohibit overclaiming.
15. Federated verification that uses consensus for log consistency but never as
    factual truth.

The open verification layer should remain available to prevent proprietary
capture. Patents, if pursued, should protect implementations without creating a
private monopoly over truth evaluation.

---

## 64. Additional Research Foundations

The expansion should track and critically test emerging work rather than assume
that current AI can reliably govern itself:

- MIRROR benchmark for metacognitive calibration and the need for external
  architectural control:  
  https://arxiv.org/abs/2604.19809
- Self-evolving causal world modeling for embodied scientific intelligence:  
  https://arxiv.org/abs/2606.22449
- PROV-AGENT work on provenance across agentic workflows:  
  https://arxiv.org/abs/2508.02866
- Research on correlated AI forecasting errors and epistemic monoculture:  
  https://arxiv.org/abs/2605.00844
- NIST post-quantum standards and migration guidance:  
  https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards
- FIPS 203 ML-KEM:  
  https://csrc.nist.gov/pubs/fips/203/final
- FIPS 204 ML-DSA:  
  https://csrc.nist.gov/pubs/fips/204/final
- FIPS 205 SLH-DSA:  
  https://csrc.nist.gov/pubs/fips/205/final

Emerging research is evidence about possible designs, not automatic proof that
those designs are production-ready.

---

## 65. Expanded Completion Rule

ALETHEIA 2.0 is operationally complete only when the original ten conditions
and all of the following are satisfied:

11. competence profiles are empirically calibrated by domain;
12. metacognitive routing demonstrably reduces confident failure;
13. active evidence requests improve hypothesis discrimination;
14. experiments cannot bypass safety, authority or privacy gates;
15. belief revision propagates through all material dependencies;
16. synthetic consensus does not inflate independence;
17. world-model predictions are prospectively registered and resolved;
18. self-improvements pass independent regression and adversarial review;
19. embodied capture records hardware, software, calibration and action DNA;
20. confidential-compute claims remain bounded to their attestation meaning;
21. post-quantum renewal preserves historical semantics;
22. federation consistency failures are detectable;
23. action admission remains separate from truth evaluation;
24. humans can understand, contest and replay consequential receipts;
25. political, commercial or institutional pressure cannot silently alter the
    constitution or prior evidence.

The current artifact status is:

```text
EXPANDED_BLUEPRINT_COMPLETE
METACOGNITIVE_ARCHITECTURE_SPECIFIED
FUTURE_TECHNOLOGY_HORIZON_SPECIFIED
REFERENCE_IMPLEMENTATION_NOT_BUILT
FORMAL_SPECIFICATION_REQUIRED
SCIENTIFIC_VALIDATION_REQUIRED
SECURITY_AND_CRYPTOGRAPHIC_REVIEW_REQUIRED
DOMAIN_EXPERT_REVIEW_REQUIRED
LEGAL_DEPLOYMENT_REVIEW_REQUIRED
```

## Final doctrine

> Truth is not assigned by a person, model, institution, market or network.
> ALETHEIA continuously constructs the strongest warranted relationship between
> claims and reality by preserving Evidence DNA, exposing dependencies,
> measuring its own competence, generating alternatives, acquiring new
> observations, attempting falsification, revising beliefs, and refusing to
> exceed what can actually be known.

END OF ALETHEIA TRUTH COMPILER BLUEPRINT 2.0.


---

# ALETHEIA v3.0.0 PUBLIC RESEARCH EDITION UPLIFT

> **v3.0.0 note:** PUBLICATION QUALITY UPGRADE — importable research library (`from aletheia import ALETHEIAEngine`);
> Reality Gate (7/7); benchmarks; mutation ≥90%; alt-impl replication; real-world scientific false-plurality scenario;
> stress to 2000 evidence nodes; 3-layer novelty; negative claims; competitive positioning; formal proof sketches;
> standards mapping; deployment manifest; honest gap register. DOI remains 10.5281/zenodo.21344789 (concept); this edition prepares a versioned Zenodo update. Readiness uplift toward newer publication standard (~90–95% agent ceiling). Not peer reviewed; not independently human-replicated.

**Edition:** v3.0.0 Public Research Edition  
**Sole SSOT:** `ALETHEIA_v3.0.0_PUBLIC_RESEARCH_EDITION.md`  
**Implementation status:** Reality Gate PASS (`poc/aletheia_gate.py`); PoC/benchmark/mutation/stress/realworld present; not production  
**GitHub:** https://github.com/AGIM8003/aletheia-truth-compiler

## Honest Status Boundary (v3.0.0)

This edition adds executable research evidence and library packaging. It does **not** claim that ALETHEIA determines absolute truth, that a production system is deployed, that peer review has occurred, that patents will issue, or that regulatory compliance is certified. Real-Invention Readiness scores are author assessments.

## Novelty Declaration (3-layer)

### Layer 1 — Component Novelty

| Component | Novel? | Evidence |
|-----------|--------|----------|
| Content-addressed Evidence DNA digest | PARTIAL | Hashing+lineage exist; DNA binding of content∥sources is packaged here |
| Certification ≠ truth separation | YES | Explicit certify-without-truth doctrine + API |
| Independence-aware Truth Receipts | YES | Receipt conclusions degrade under shared origins |
| Revocation cascading into certification | PARTIAL | Related to unlearning/rollback; ALETHEIA-specific receipt effects |

### Layer 2 — Integration Novelty

| Existing system | What it does | What it misses vs ALETHEIA CORE |
|-----------------|--------------|----------------------------------|
| Provenance stores (PROV/OpenLineage) | Job/dataset lineage | Bounded truth receipts + independence scoring |
| Content-addressed storage (IPFS/git) | Integrity of bytes | Claim-level discovery + contradiction handling |
| Fact-checking platforms | Human editorial truth | Machine-reproducible Evidence DNA + explicit unknowable state |
| Model citations / RAG | Retrieval | Shared-origin detection across “independent” papers |

### Layer 3 — Architectural Novelty

**Principle:** Separate integrity certification from truth discovery, and refuse independence credit when Evidence DNA reveals shared origins.  
**Examiner sentence:** A system that certifies lineage while issuing independence-sensitive Truth Receipts that can return CURRENTLY_UNKNOWABLE under shared roots is not disclosed by provenance-only or fact-check-only prior art.

## Negative Claim Register

1. NOT a universal / absolute truth oracle.  
2. NOT a claim that signed evidence is true.  
3. NOT a production deployment.  
4. NOT peer reviewed.  
5. NOT independently human-replicated.  
6. NOT a substitute for domain science (clinical, physics, law).  
7. NOT a cryptographic HSM/PKI product.  
8. NOT immune to adversarial fabricated independent sources.  
9. NOT a patent grant or FTO opinion.  
10. NOT GDPR/AI-Act certified compliance software.  
11. NOT a social credit or political censorship engine.  
12. NOT an automatic takedown authority.

## Competitive Positioning

| Capability | ALETHEIA | OpenLineage | Fact-checkers | IPFS |
|-----------|----------|-------------|---------------|------|
| Evidence DNA (content∥sources) | ✅ | Partial | ❌ | Integrity only |
| Certify ≠ truth | ✅ | N/A | Mixed | N/A |
| Independence-sensitive receipts | ✅ | ❌ | Human | ❌ |
| Production maturity | Research library | ✅ | ✅ | ✅ |

**Where ALETHEIA loses today:** OpenLineage/IPFS/fact-checkers are deployed at scale with connectors and ops. ALETHEIA is blueprint + research library.

## Formal Proof Sketches

**Proof 1 (Integrity soundness):** If `content_digest(content, sources)` matches stored digest and no ancestor is revoked, `certify` returns certified=True. Sketch: digest equality is deterministic; revocation flips certified False by construction.

**Proof 2 (Independence monotonicity):** Adding a shared origin to two support items cannot increase independence_score. Sketch: shared pair count weakly increases; score = 1 - shared/pairs weakly decreases.

**Proof 3 (Contradiction termination):** If any non-revoked contradicting item exists with non-empty live support, conclusion is CONTRADICTED in one evaluation pass (no loop).

## Real-World Scenario Evidence

See `poc/aletheia_realworld.py`: scientific biomarker claim where Journals A/B + newswire share preprint X; ALETHEIA returns CURRENTLY_UNKNOWABLE for false plurality and CONTRADICTED when an independent RCT null result is included.

## Standards / Regulatory Mapping

| Standard | Clause / theme | ALETHEIA feature | Level |
|----------|----------------|------------------|-------|
| W3C PROV | Provenance entities/activities | Evidence DNA lineage | PARTIAL |
| EU AI Act | Art. 13 transparency | Truth Receipt inspectability | PARTIAL |
| EU AI Act | Art. 14 human oversight | CURRENTLY_UNKNOWABLE refuses overclaim | PARTIAL |
| NIST AI RMF | Map/Measure | Independence + contradiction metrics | PARTIAL |
| ISO/IEC 27001 | Integrity controls | Digest integrity certification | PLANNED |
| GDPR | Accuracy / rectification | Revocation cascade | PLANNED |

## Deployment Reality

See `poc/aletheia_deploy_manifest.json` — ~$50–160/month single-node estimate; not a vendor quote.

## Honest Gap Register

| # | Gap | Severity | Close with | Timeline |
|---|-----|----------|------------|----------|
| 1 | No cryptographic signature keys / HSM | HIGH | Real signing backend | 3–6 mo |
| 2 | No peer review | HIGH | Journal submission | 6–18 mo |
| 3 | No independent replication | HIGH | External lab | 3–9 mo |
| 4 | Domain validators stubbed | HIGH | Clinical/physics packs | 6–12 mo |
| 5 | Adversarial fabricated independents | MEDIUM | Red team | 3–6 mo |
| 6 | Scale beyond 2k not proven | MEDIUM | Sharded digest store | 3–6 mo |
| 7 | Accessibility of receipt UI | LOW | WCAG UI | 1–2 mo |
| 8 | Energy per certify unmeasured | LOW | Metering | 2–4 wk |
| 9 | FTO incomplete | MEDIUM | Counsel | 2–4 mo |
| 10 | Federation protocol untested | MEDIUM | Multi-node pilot | 6–12 mo |

## Licensing, Attribution, and Commercial Use

License: **CC BY-NC-ND 4.0**. Evaluation of PoC code allowed; commercial incorporation requires written permission from Agim Haxhijaha (agim@vertogroup.ai), ORCID 0009-0002-3234-7765.

END OF ALETHEIA v3.0.0 UPLIFT SECTIONS.
