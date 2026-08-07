---
id: KERNEL-0001
title: MingOS Kernel Core Operational Contract
status: Draft
version: 0.2.3-draft.5
layer: Layer 2 — Standards
owner: Ming Foundation Kernel Architecture
created: 2026-07-15
updated: 2026-07-15
language: en
canonical_language: en
translation_status: original
decision_base_commit: 29485e67279d11401bb0f9f2b9afc78f0bdf67f4
related:
  - MF-0004
  - MF-0005
  - PROJECT-MINGOS-0002
  - ADR-0001
  - ADR-0002
  - ADR-0005
  - ADR-0026
  - MOS-0000
  - RFC-0001
  - RFC-0002
  - RFC-0003
  - RFC-0004
  - RFC-0005
  - PROF-0001
  - PROF-0002
  - PROF-0003
  - PROF-0004
  - KERNEL-0000
  - KERNEL-0002
  - KERNEL-0003
  - KERNEL-0004
  - KERNEL-0005
  - REF-0031
  - REF-0032
  - REF-0033
  - REF-0034
depends_on:
  - KERNEL-0000
  - ADR-0026
  - MOS-0000
---

# KERNEL-0001 — MingOS Kernel Core Operational Contract

> The 36 KCR requirements remain Draft, externally unreviewed and nonconforming.

## 1. Purpose and scope

Define the smallest current cross-implementation obligations. KERNEL-0002 and KERNEL-0003 operationalize these requirements without changing KCR wording or resolving the 30 KCR ambiguities.

## 2. Normative language and authority

`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT` and `MAY` follow MOS-0000. Exact KCR text and source mapping remain in the Round 07 table and machine index.

## 3. Round 08 operationalization rule

Every KDO and KLS requirement MUST identify its KCR basis. Object fields and state transitions MUST NOT silently strengthen, weaken or universalize a KCR, RFC, Profile, family method or cultural metaphor.

KERNEL-0002 defines object semantics. KERNEL-0003 defines object-local state machines and separate cross-object process flows. A process flow does not create a state transition by itself.

## 4. Human agency, privacy and safety

The object/lifecycle specifications preserve affected-person participation, refusal, correction, appeal, minimum necessary data, authority expiry, proportionality, human accountability and no permanent vulnerability profile.

## 5. Review and future conformance

KERNEL-0004 and KERNEL-0005 do not yet exist. Product conformance cannot be assessed. Repository validation only checks governed document integrity.

## 6. Version and change history

| Version | Date | Change | Status |
|---|---|---|---|
| 0.1.0-draft.1 | 2026-07-15 | Initial core contract | Draft |
| 0.2.0-draft.2 | 2026-07-15 | Exact KCR source and verification mapping | Draft |
| 0.2.1-draft.3 | 2026-07-15 | Initial Round 08 references | Draft |
| 0.2.2-draft.4 | 2026-07-15 | Correct Round 08 versions and state/process boundary | Draft |
| 0.2.3-draft.5 | 2026-07-15 | Integrate Draft conformance and test references | Draft |

## 7. Current boundary

```text
KERNEL-0000: Draft / 0.5.0-draft.5
KERNEL-0001: Draft / 0.2.3-draft.5
KERNEL-0002: Draft / 0.2.0-draft.2
KERNEL-0003: Draft / 0.2.0-draft.2
KERNEL-0004: Draft / 0.1.0-draft.1
KERNEL-0005: Draft / 0.1.0-draft.1
Review: PreparedNotExecuted
Overall: NoCurrentKernelConformanceClaim
```
