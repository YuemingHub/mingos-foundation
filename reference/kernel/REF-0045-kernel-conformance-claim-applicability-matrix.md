---
id: REF-0045
title: Kernel Conformance Claim Unit and Applicability Matrix
status: Draft
version: 0.1.1-draft.2
layer: Reference
owner: Ming Foundation Kernel Conformance
created: 2026-07-15
updated: 2026-08-06
language: en
canonical_language: en
translation_status: original
decision_base_commit: 280a68705d13bbb5beed3a64713575fad7cba189
related:
  - KERNEL-0004
depends_on:
  - KERNEL-0004
---

# REF-0045 — Kernel Conformance Claim Unit and Applicability Matrix

## 1. Bounded conformance claim units

| Unit | Required identity | Prohibited spillover |
|---|---|---|
| Product surface | product, version, surface, operator, Profile | whole company or unrelated surface |
| Service workflow | workflow, roles, service class, jurisdiction | all professional work |
| Agent/system | version, tools, provider/model, authority | provider or host product |
| Organization operation | named process and accountable roles | all organizational activity |
| Component | component and integration boundary | automatic host conformance |

## 2. Adoption is not conformance

This reference distinguishes practical adoption from formal conformance. It does not change the requirements in KERNEL-0004.

A product or service may use selected Draft Kernel concepts without entering a formal conformance assessment, provided it does not imply certification, approval, completeness or Profile conformance. Selective adoption is intended to let implementations learn, translate and iterate before the evidence needed for a formal claim exists.

| Adoption lane | Intended use | Minimum discipline | Not permitted |
|---|---|---|---|
| Exploration | prototypes, internal learning, concept translation | name the concepts used; keep Draft status visible; avoid real-person or live-case claims | certification, approval or safety claims |
| Bounded implementation | one identified product surface or workflow | identify owner, scope, known limitations and applicable hard safety/privacy boundaries | spillover to the whole product or organization |
| Evidence-building | controlled tests and governed operational learning | record versions, failures, counterexamples and evidence limitations | presenting repository checks as product evidence |
| Formal conformance assessment | assessment against an approved Profile | apply all KERNEL-0004 requirements for the declared boundary | partial evidence represented as complete conformance |
| Public conformance claim | public wording after an effective assessment decision | use only authorized language, scope, version and expiry | implied certification or unbounded claims |

## 3. Risk-proportionate adoption

Selective adoption should be proportionate to the effect on life, rights and safety. Flexibility applies to implementation method, sequencing, explanation style and growth-path design; it does not waive boundaries that prevent foreseeable harm.

| Effect tier | Typical context | Proportionate expectation |
|---|---|---|
| Low | reversible reflection, explanation, journaling, non-sensitive planning | lightweight rationale, clear uncertainty and easy user correction |
| Moderate | repeated guidance, family-state interpretation, stored profiles, consequential recommendations | accountable owner, source/assumption visibility, correction path, privacy controls and failure review |
| High | self-harm, violence, abuse, medical/legal crisis, coercive authority, irreversible or rights-affecting action | hard safety gate, human escalation, minimum necessary action, auditability and explicit authority limits |

The effect tier is determined by the reasonably foreseeable consequence of error, not by whether the implementation is called a prototype, assistant, conversation or recommendation.

## 4. MingOS product interpretation

For MingOS product work, the default is not to force every ordinary interaction through a certification workflow. The product may translate a difficult situation into a comprehensible and actionable growth path while retaining flexibility in language, pacing, mode selection and family-context interpretation.

The non-negotiable boundary is narrow and hard: when foreseeable life safety, violence, abuse, severe rights impact, privacy breach or professional-authority risk is present, the applicable safety, consent, contestability, handoff and accountability controls take priority over conversational flexibility.