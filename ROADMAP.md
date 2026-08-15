# Ming Foundation Roadmap

## Foundation 1.0 objective

Create a coherent, implementable, and governable foundation for Living Intelligence, calibrated by real life rather than by internal completeness.

## Current driving model — Evidence-led Evolution

This roadmap change is the operating-model proposal carried by PR #20. `ADR-0029`
documents the proposed three-class authority model; it remains `Proposed` until an
explicit review/decision promotes it. The previous Foundation-first phase plan
(below) is preserved as historical provenance and is not the intended driving
sequence if this roadmap change is accepted and merged.

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

Guiding rules:

1. Family-Space is the current real construction front. Foundation does not
   expand for system-completeness.
2. MingOS extracts only capabilities proven to have cross-space meaning.
3. Foundation is the principle / calibration layer; it defines what must
   never be violated, not how products must be built.
4. No product field automatically becomes a MingOS object or a Foundation
   rule.
5. "No change / no activation" is a legitimate result. CP2 remains governed
   by the current canonical state; this roadmap does not independently
   authorize or activate it.
6. Every new Foundation structure must answer: which real, reproducible
   current problem cannot be solved without it? If none, do not add it.

## Historical phase plan (provenance, superseded as the driving model)

The following phase plan described the original horizontal build-out
sequence. It remains valid history and individual items may still inform
future work, but it does not define the current execution order if this
roadmap change is accepted.

### Phase A — Repository Foundation

- Repository DNA and document metadata
- Charter, mission, vision, and first principles
- Standards lifecycle
- Architecture Decision Records
- Terminology and architecture map
- Automated repository validation

### Phase B — Canonical Models

- MOS-0001 First Principles
- MOS-0002 Life Ontology
- MOS-0003 Identity Model
- MOS-0004 Relationship Model
- MOS-0005 Life Event Model
- MOS-0006 State Model
- MOS-0007 Context Model
- MOS-0008 Consent Model

### Phase C — Core Protocols

- Observation Protocol
- Memory Specification
- Reasoning Protocol
- Reflection Protocol
- Choice and Action Protocol
- Evidence, Confidence, and Revision Protocol
- Safety and Escalation Protocol

### Phase D — MingOS Core

- Unified identity and family graph
- Life event system
- Observation store
- Revisable memory
- State snapshots and timelines
- Action-feedback loop
- Audit and consent infrastructure

### Phase E — Reference Applications

- Enterprise WeChat + H5 MVP
- Ming Family
- MingOS Web
- Human support workbench
- Developer reference application

## Release rule

No standard becomes Stable merely because it is well written. Stable status requires:

1. at least one reference implementation;
2. documented real-world cases;
3. ethics and safety review;
4. compatibility review;
5. evidence that users can correct or reject system interpretations.

## Current active entry surface

To understand the branch under review, read these first:

1. `README.md` — project identity and branch-proposed stage;
2. `governance/status/GOV-0001-current-canonical-state.md` — canonical-state
   record that becomes authoritative only when merged to the default branch;
3. `governance/decisions/ADR-0029-three-class-authority-model-and-canonical-bridge.md`
   — **Proposed** authority model; not self-promoted by this PR;
4. `governance/registries/AUTHORITY_MANIFEST.json` — **Proposed**
   machine-readable adoption contract governed by ADR-0029;
5. `governance/audits/GOV-0114-three-repository-reality-rebase-drift-audit.md`
   — review evidence for current/stale/historical distinctions;
6. `ROADMAP.md` (this file) — operating-model proposal.

The operational `THREE_REPO_COMPASS_V1` companion is introduced by Foundation
PR #19 and is a navigation/agent first-read surface, not a second formal source
of governance authority. Shared semantic changes must remain aligned with that
contract or explicitly record temporary divergence.
