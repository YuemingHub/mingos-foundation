---
id: REF-0046
title: Kernel Evidence and Assurance Class Matrix
status: Draft
version: 0.1.0-draft.1
layer: Reference
owner: Ming Foundation Kernel Conformance
created: 2026-07-15
updated: 2026-07-15
language: en
canonical_language: en
translation_status: original
decision_base_commit: 29485e67279d11401bb0f9f2b9afc78f0bdf67f4
related:
  - KERNEL-0004
depends_on:
  - KERNEL-0004
---

# REF-0046 — Kernel Evidence and Assurance Class Matrix

| ID | Class | Meaning | Limitation |
|---|---|---|---|
| KEC-01 | StructuralStatic | Repository, schema, configuration and source inspection | Does not prove runtime or human outcomes |
| KEC-02 | SyntheticScenario | Synthetic positive, negative and counterexample execution | No real-person acceptance claim |
| KEC-03 | ControlledImplementation | Bounded implementation test | Not broad production evidence |
| KEC-04 | OperationalTrace | Governed runtime, incident or service evidence | Requires privacy and freshness review |
| KEC-05 | AffectedPersonReview | Voluntary affected-person usability and impact evidence | Cannot be replaced by internal opinion |
| KEC-06 | DomainProfessionalReview | Qualified domain review | Does not imply affected-person or legal acceptance |
| KEC-07 | IndependentAssurance | Conflict-free independent review | Scope and independence explicit |
| KEC-08 | LongitudinalIncident | Longitudinal outcomes, failures and remediation | Requires time and confounder limits |

No single class proves the whole Profile. Repository validation is StructuralStatic only.
