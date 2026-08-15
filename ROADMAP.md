# Ming Foundation Roadmap

## Foundation 1.0 objective

Create a coherent, implementable, and governable foundation for Living Intelligence, calibrated by real life rather than by internal completeness.

## Current driving model — Evidence-led Evolution

Adopted by `ADR-0029` and re-based by the three-repository reality rebase
audit (`GOV-0114`). The previous Foundation-first phase plan (below) is
preserved as historical provenance. It is no longer the driving model.

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
5. "No change / no activation" is a legitimate result. CP2 remains a
   blocked, inactive retained capability.
6. Every new Foundation structure must answer: which real, reproducible
   current problem cannot be solved without it? If none, do not add it.

## Historical phase plan (provenance, superseded as the driving model)

The following phase plan described the original horizontal build-out
sequence. It remains valid history and individual items may still inform
future work, but it does not define the current execution order.

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

## Current active canonical entry surface

To know what is current, a new contributor should read these first (thin
entry, not the full history):

1. `README.md` — why we exist and current stage;
2. `governance/status/GOV-0001-current-canonical-state.md` — what is
   currently accepted;
3. `governance/decisions/ADR-0029-three-class-authority-model-and-canonical-bridge.md`
   — how authority is divided;
4. `governance/registries/AUTHORITY_MANIFEST.json` — machine-readable
   authority model;
5. `governance/audits/GOV-0114-three-repository-reality-rebase-drift-audit.md`
   — what is current / stale / historical;
6. `ROADMAP.md` (this file) — the evidence-led driving model.

Everything else is history, proposals, or retained capability.
