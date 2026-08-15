---
id: ADR-0029
title: Three-Class Authority Model and Canonical Bridge Rule
status: Proposed
version: 1.0.0
layer: Layer 5 — Community & Governance
owner: Ming Foundation Architecture
created: 2026-08-15
updated: 2026-08-15
related:
  - MF-0004
  - PROJECT-MINGOS-0002
  - GOV-0001
  - GOV-0114
  - GOV-0115
  - ADR-0005
  - ADR-0023
  - ADR-0028
depends_on:
  - MF-0004
  - ADR-0005
---

# ADR-0029 — Three-Class Authority Model and Canonical Bridge Rule

## Context

`GOV-0114` (three-repository reality rebase drift audit) established that:

1. the Foundation root principles remain correct;
2. the Foundation operating model (Foundation-first, CP2-next default queue)
   no longer matches current reality;
3. Family-Space is the only real construction front and is validating, in
   production use, the semantics of ordinary, non-coercive, no-action-legal
   interaction;
4. product implementation details must not automatically become MingOS
   objects or Foundation rules.

Issue #14 in `mingos-foundation` asks for a "Foundation → MingOS product
adoption bridge" that lets MingOS consume selected Foundation boundaries
without turning them into a new classifier, mandatory state machine,
product script, or certification claim.

MingOS Issue #33 asks for the same adoption contract encoded on the MingOS
side (`hard_invariant | adaptive_default | product_owned_choice`).

This ADR establishes the authority model on the Foundation side and the
canonical bridge rule that governs how authority travels down (constraint)
and up (evidence) between the three repositories.

## Decision

### D1. Three authority classes

Authority in the three-repository system is divided into exactly three
classes. Every cross-repository semantic item belongs to exactly one class.

```text
hard_invariant        Owner: Foundation
adaptive_default      Owner: MingOS
product_owned_choice  Owner: downstream product
```

#### 1. `hard_invariant` — Foundation-owned

Non-negotiable boundaries that may NOT be sacrificed for efficiency,
growth, model judgment, or product convenience. A hard invariant is
binding only when its trigger / evidence is present.

Covered boundaries include:

- life safety; violence / abuse protection;
- consent; privacy; coercion boundary;
- correction; contestability; reversibility;
- evidence / provenance must not be silently upgraded;
- unsupported inference must not be presented as fact;
- professional authority boundary (no medical / legal / diagnostic /
  mental-health claims);
- AI must not acquire final authority over a person's identity, meaning,
  life direction, or conscience;
- legacy / model / category output cannot by itself prescribe or prohibit;
- protective guard activation requires a current independent evidence
  owner;
- in Safety-owned situations, minimum necessary protective action may be
  required.

A hard invariant does not become binding without its trigger/evidence. An
ordinary product preference must NOT be dressed up as a hard invariant.

#### 2. `adaptive_default` — MingOS-owned cross-space semantics

Reusable runtime semantics that organize cross-Life-Space ordinary
interaction. They guide behavior but do not prescribe a product outcome,
and a legitimate ordinary outcome is **no action**.

Examples:

- first receive the person, then clarify what is actually known
  (understanding before advice);
- observation / evidence before interpretation;
- FACT / REPORT / FEELING / INTERPRETATION / INFERENCE / UNKNOWN /
  CORRECTION separation;
- preserve uncertainty;
- new evidence / correction can retire an older interpretation;
- ordinary interaction may legitimately end with no action;
- action may exist but must remain optional / rejectable in ordinary
  scenes;
- pacing adapts to current evidence / intent rather than being decided by
  an old category.

Foundation acknowledges the existence of this layer but must not promote
every specific adaptive default into a permanent Foundation rule.

#### 3. `product_owned_choice` — downstream product authority

The product decides its own implementation, including:

- exact wording, tone, UI, response length;
- ask / reflect / explain / pause / action;
- action cadence;
- model / provider;
- prompt topology; agent topology;
- family profile; navigation;
- family-specific read model;
- Today / 我家 / 回望 / 我的 concrete implementation.

These do not automatically become MingOS Core primitives or Foundation
rules simply because the current implementation works.

### D2. Canonical bridge rule

```text
Foundation  defines what must never be violated.
MingOS      defines how authority, evidence, memory, context, and
            correction travel across spaces.
Products    decide how to help within those boundaries.
```

### D3. Constraint flow (down) and evidence flow (up)

```text
Foundation
    ↓ hard constraints

MingOS
    ↓ reusable runtime semantics

Products
    ↓ real-world implementation

Real life
    ↓ evidence / failure / counterexample / unknown

Products
    ↑ repeated evidence

MingOS
    ↑ cross-space candidate

Foundation
    ↑ only long-lived non-negotiable principle
```

The forbidden shortcut is:

```text
a Family-Space field → a MingOS object → a Foundation rule
```

This automatic upgrade is rejected.

### D4. Evidence-led evolution replaces Foundation-first sequencing

The previous driving model was:

```text
finish Foundation → Canonical Models → Protocols → Core → Applications
```

The driving model is now:

```text
North Star / Hard Invariants
        ↓
minimal runnable system
        ↓
real Life Space
        ↓
real use
        ↓
failure / counterexample / unknown / working experience
        ↓
candidate capability
        ↓
cross-scene / cross-space validation
        ↓
MingOS abstraction
        ↓
only long-lived non-negotiable parts enter Foundation
```

The historical roadmap is preserved as provenance, not deleted.

### D5. CP2 is an inactive retained capability, not the default queue

- Day 16–18 CP0/CP1 synthetic work, role nomination, and conditional CP2
  pre-authorization remain valid historical records.
- CP2 remains `Blocked / NotExecuted`.
- No new evidence currently requires resuming Restricted Nomination
  Execution or CP2 Activation as the default execution queue.
- **No change / No activation is a legitimate result.**
- These capabilities may be re-activated later only if new real evidence
  requires the corresponding governance work.

### D6. Semantic compatibility, not shared-SHA

Three repositories do not need to share the same SHA. Foundation does not
need to change dozens of times a day because Family-Space has dozens of
commits a day.

The contract is semantic:

```text
Foundation:
  hard_invariant_version

MingOS:
  adopted_foundation_version
  runtime_semantics_version

Product:
  compatible_foundation_version
  compatible_mingos_semantics
  product_policy_version
```

Upstream work is triggered only when a semantic boundary actually changes,
not when implementation churn occurs.

## Reasons

1. The drift audit (`GOV-0114`) showed the Foundation-first default queue is
   stale while the Charter root remains correct. The three-class model keeps
   the root intact and fixes only the operating model.
2. Family-Space production use is already validating `adaptive_default`
   semantics; classifying them explicitly prevents them from being
   accidentally promoted to Foundation rules.
3. The canonical bridge rule makes the anti-upgrade boundary explicit and
   testable, satisfying the North Star test: stronger system capability must
   preserve, not reduce, human agency and revisability.
4. Semantic compatibility prevents the anti-drift maintenance trap of
   hard-coding another repository's PR numbers, branch names, or SHAs into
   permanent tests.

## Consequences

### Positive

- A single, thin, machine-readable surface (the authority manifest) tells
  any new agent which boundaries are non-negotiable, what remains free for
  products/people, and what evidence is still missing.
- Products keep full freedom of wording, UI, action cadence, and
  implementation.
- Foundation stops acting as an active construction front and returns to
  its role as principle/calibration layer.
- CP2 stays provably blocked without deleting its historical infrastructure.

### Negative

- Requires maintaining the authority manifest and its validator over time.
- Some historical "next work" wording in `GOV-0001` and `ROADMAP.md` is
  explicitly marked as superseded, which may surprise contributors who only
  read those files.

## Alternatives considered

- **Promote Family-Space implementation as the reference standard.**
  Rejected: product tests passing is not Foundation conformance; it would
  violate the North Star test and freeze the product.
- **Add a new classifier / state machine for authority.**
  Rejected: this ADR is about classifying authority, not adding runtime
  architecture. `GOV-0114` and the complexity budget forbid adding
  layers/state/gates without a real reproducible problem.
- **Require all three repositories to share the same SHA.**
  Rejected: impossible at product velocity and unnecessary for semantic
  compatibility.

## Follow-up

- Authority manifest: `governance/registries/AUTHORITY_MANIFEST.json`;
- adoption guide: `reference/REF-0052-adoption-bridge-and-authority-guide.md`;
- current Family-Space re-audit: `GOV-0115`;
- `ROADMAP.md` and `GOV-0001` updated in this rebase;
- MingOS side contract is tracked by MingOS Issue #33 (downstream, not this
  repository).
