---
id: GOV-0113
title: Parallel Workstream Integration and Document ID Reservation
status: Accepted
version: 1.0.0
layer: Layer 5 — Community & Governance
owner: Ming Foundation Architecture and Validation
created: 2026-07-28
updated: 2026-07-28
related:
  - GOV-0001
  - GOV-0081
  - GOV-0082
  - GOV-0083
  - GOV-0103
  - GOV-0110
  - KERNEL-0000
  - KERNEL-0001
  - KERNEL-0002
  - KERNEL-0003
depends_on:
  - GOV-0003
  - GOV-0081
  - GOV-0083
---

# GOV-0113 — Parallel Workstream Integration and Document ID Reservation

## 1. Purpose

This record governs multiple conversation, agent, documentation, and review
workstreams that prepare changes for the same canonical repository.

Parallel work MAY draft content concurrently. Formal integration into `main`
MUST be serialized.

## 2. Central rule

A document identifier becomes available to a workstream only after it is
recorded in:

```text
governance/registries/DOCUMENT_ID_RESERVATIONS.json
```

A detailed draft, local branch, ZIP package, conversation statement, or
GitHub `mergeable=true` result does not allocate an identifier by itself.

## 3. Reservation states

The registry uses the following states:

- `PlannedReservation` — proposed allocation not yet attached to an open PR;
- `ReservedForOpenDraftPR` — allocation held for one identified open Draft PR;
- `ReadyForSerialIntegration` — re-audited against the latest main and ready
  for the sole merge-ready slot;
- `Integrated` — the reserved documents are present on main;
- `Released` — the reservation was deliberately returned without integration;
- `ExpiredOnMainChange` — main advanced and the reservation has not yet been
  re-audited.

## 4. Main-change rule

Whenever `main` advances, every non-integrated reservation MUST be re-audited.

Until that audit is recorded, it MUST NOT be treated as merge-ready.

An agent MUST NOT automatically rebase, renumber, or resolve a governance-ID
collision merely because Git can merge the files.

## 5. Shared integration surfaces

The following files are finalised by the integration workstream, not by two
parallel workstreams independently:

```text
README.md
CHANGELOG.md
REPOSITORY_INDEX.md
governance/status/GOV-0001-current-canonical-state.md
scripts/validate_all.py
.github/workflows/* repository-wide validation entry points
```

A source workstream MAY propose changes to these files, but the serial
integration step MUST reconcile the full current state.

## 6. Required reservation record

Each reservation MUST contain:

- a unique reservation ID;
- workstream and accountable owner;
- source PR, branch, or governing record;
- reservation state;
- reserved IDs;
- creation date;
- commit against which the allocation was reviewed;
- whether a main change expires the review;
- release, replacement, or integration evidence when the state changes.

## 7. Current integration decision

The Day18 governance line and Kernel Round08 are both present on main.

Kernel Round09 PR #12 is not integrated by this decision. Its proposed IDs
are reserved as:

```text
KERNEL-0004
KERNEL-0005
REF-0045 through REF-0051
```

`REF-0035` remains the Accepted Day18 guide and is not available to another
workstream.

## 8. Safety boundary

This record does not:

- merge or modify PR #12;
- promote any Kernel Draft;
- create a Kernel conformance claim;
- activate CP2 or CP3;
- create real role assignments or private identity records;
- change Charter, RFC, or Profile status.
