---
id: REF-0052
title: Adoption Bridge and Authority Guide
status: Proposed
version: 1.0.0
layer: Layer 5 — Community & Governance
owner: Ming Foundation Architecture
created: 2026-08-15
updated: 2026-08-15
related:
  - ADR-0029
  - GOV-0114
  - GOV-0115
  - GOV-0001
  - KERNEL-0000
  - KERNEL-0001
depends_on:
  - ADR-0029
---

# REF-0052 — Adoption Bridge and Authority Guide

> Human-readable guide to the authority manifest
> (`governance/registries/AUTHORITY_MANIFEST.json`) and the canonical
> bridge rule (`ADR-0029`). This guide is not a standard and carries no
> normative force by itself.

## 1. Purpose

When a MingOS or product agent asks:

1. Which boundaries are non-negotiable here, and what current evidence owns
   them?
2. Inside those boundaries, what remains genuinely free for the product /
   person to decide — including the legitimate option to do nothing yet?

This guide and the manifest answer deterministically.

## 2. The three classes in one screen

| Class | Owner | Binding | Examples |
|---|---|---|---|
| `hard_invariant` | Foundation | only when trigger/evidence present | life safety, consent, privacy, coercion, correction, contestability, evidence-not-upgraded, professional boundary, no AI final authority |
| `adaptive_default` | MingOS | guides, does not prescribe | understanding before advice, FACT/REPORT/… separation, no-action legal, optional/rejectable action |
| `product_owned_choice` | product | product decides | wording, tone, UI, length, ask/reflect/pause/action, model/provider, prompt/agent topology, navigation |

## 3. Reading the manifest

Each item in the manifest's `classes` carries:

- `owner` — which layer owns the authority;
- `binding` — when it binds;
- `items` — the semantic keys.

For each semantic key a downstream consumer must be able to state:

- class;
- authority owner;
- trigger/evidence expectation;
- permitted downstream effect;
- forbidden authority upgrade;
- evidence/test expectation.

The manifest exposes these at the class level; a downstream adoption
contract (MingOS Issue #33) may restate them per semantic key without
changing the class boundary.

## 4. Canonical bridge rule (how authority travels)

```text
Foundation  → hard constraints
MingOS      → reusable runtime semantics
Products    → real-world implementation
Real life   → evidence / failure / counterexample / unknown
Products    → repeated evidence
MingOS      → cross-space candidate
Foundation  → only long-lived non-negotiable principle
```

Forbidden: `product field → MingOS object → Foundation rule`.

## 5. What "adopting a Draft concept" means

- Selective use of Draft Kernel / Foundation concepts is allowed when
  labelled with exact document, version, scope, and limitations.
- It is NOT conformance, certification, merge approval, or production
  authorization.
- A product test result is evidence for review, never a conformance claim.

## 6. North Star test

Every new Foundation rule must pass:

1. Does it protect life, not the system itself?
2. If system capability increases, does the person become freer, more able
   to understand, judge, correct, and own their choices?

If `system authority ↑` while `human agency ↓`, the rule is an
architectural risk, however professional it sounds.

## 7. Semantic compatibility (no shared SHA)

- Foundation: `hard_invariant_version`;
- MingOS: `adopted_foundation_version`, `runtime_semantics_version`;
- Product: `compatible_foundation_version`, `compatible_mingos_semantics`,
  `product_policy_version`.

Foundation does not change because Family-Space changes; it changes only
when a semantic boundary changes.

## 8. Non-claims

The manifest and this guide do not claim:

- Foundation conformance;
- Family-Space general effectiveness;
- CP2 authorization;
- real-family evidence is publicly available;
- the current product implementation is already a generic MingOS or
  Foundation standard.
