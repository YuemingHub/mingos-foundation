---
id: GOV-0114
title: Three-Repository Reality Rebase Drift Audit
status: Accepted
version: 1.0.0
layer: Layer 5 — Community & Governance
owner: Ming Foundation Architecture
created: 2026-08-15
updated: 2026-08-15
related:
  - GOV-0001
  - GOV-0009
  - GOV-0110
  - GOV-0113
  - ADR-0005
  - ADR-0023
  - ADR-0028
  - PROJECT-MINGOS-0002
  - MF-0004
depends_on:
  - GOV-0001
  - GOV-0009
---

# GOV-0114 — Three-Repository Reality Rebase Drift Audit

> This audit re-reads the current remote reality of `mingos-foundation`,
> `MingOS`, and `Family-Space` and classifies every checked item as
> `current`, `stale`, `historical`, or `unknown`. It does not rewrite any
> historical document in place. Where current state has drifted from a
> historical record, this audit records the drift, the exact evidence, and
> whether Foundation action is required.

## 1. Audit method

Each item below is tagged with:

- **source**: the document, issue, PR, or commit being assessed;
- **exact SHA / issue / PR**: the precise evidence reference;
- **authority status**: the current governance status of the source
  (Accepted / Draft / Proposed / open issue / merged PR / open PR);
- **classification**: `current` (accurate today) / `stale` (accurate then,
  superseded by current reality) / `historical` (a preserved record, not a
  current instruction) / `unknown`;
- **Foundation change required**: `yes` / `no` / `advisory` and why.

Evidence was read on 2026-08-15 from the following checked baselines:

| Repository | Checked baseline |
|---|---|
| `mingos-foundation` | `main` at `7eb33ffc806db1da2fde488a617860ca34b76c0e` |
| `MingOS` | `main` at `c355f2b1fdbe067eb66fbd622dec372b5b12b27d` |
| `Family-Space` | `production` at `3aec7ea47230c2c8b447178ea8238947ccbd748e` |

Open issues and PRs were read from the GitHub API on 2026-08-15.

## 2. Findings

### 2.1 Foundation permanent principles remain correct

| Item | Evidence | Classification | Foundation change |
|---|---|---|---|
| Life Charter `MF-0004` articles (life before system, truth before theory, agency, safety without domination, fact/interpretation separation, correction, contestability, uncertainty, no anxiety conversion, no dependency retention) | `MF-0004` Candidate, `MF-0006` paired translation | **current** | no — the articles remain the correct root. Confirmed against the current product contract and MingOS END_STATE which both express the same commitments. |
| MingOS Charter `PROJECT-MINGOS-0002` commitments MC01–MC14 | Candidate; referenced by MingOS `END_STATE.md` and Family-Space product contract | **current** | no |
| First Principles `MF-0003` P01–P12 | Draft; consistent with MingOS END_STATE decision rule | **current** | no |
| `ADR-0005` three-root-texts boundary (Charter / MingOS Charter / Kernel) | Accepted | **current** | no — the three-layer boundary is still the right architecture. |

**Verdict:** no Charter article is contradicted by current remote reality.
The Foundation root must be preserved, not rewritten for currency.

### 2.2 Foundation current state and roadmap lag behind reality

| Item | Evidence | Classification | Foundation change |
|---|---|---|---|
| `GOV-0001` declares stage "Foundation 1.0 / Day 18 — Restricted Role Nomination and CP2 Pre-Authorization" | `GOV-0001` frontmatter and section 2; `README.md` | **stale as an execution instruction** — accurate as history, but Family-Space is already in real production use and Foundation is not the active construction front | yes — the operating model must be re-based to evidence-led, with CP2 retained as inactive history |
| `ROADMAP.md` Phase A→E (Foundation → Canonical Models → Protocols → Core → Applications) | `ROADMAP.md` | **stale as the driving sequence** — the family-first vertical construction is already the real main line; the horizontal phase plan is not how the three repositories actually advance | yes — supersede as the driving model; keep as provenance |
| `GOV-0001` section 9 "Next canonical work" defaults to Restricted Nomination Execution and CP2 Activation | `GOV-0001` | **stale as a default queue** — no current evidence requires CP2 activation; Family-Space is the active construction front | yes — demote to "retained capability, not default queue" |
| `VERSION.md` `1.0.0-alpha.1` vs repository version `1.0.0-alpha.18` | `VERSION.md` vs `README.md` | **stale metadata** | advisory — align version metadata during this rebase |

### 2.3 MingOS end-state expression is consistent with Foundation

| Item | Evidence | Classification | Foundation change |
|---|---|---|---|
| MingOS `END_STATE.md` "the stronger the system, the freer the person must be" | `MingOS` main | **current** — matches Foundation C04/C10 and MC09 | no |
| MingOS `END_STATE.md` three-repository relationship and "Family Space is the first vertical instance, not the final boundary" | `MingOS` main | **current** | no |
| MingOS `CROSS_REPOSITORY_COORDINATION.md` coordination contract | `MingOS` main | **current** | no — it already implements the evidence-first, authority-subtraction direction this rebase codifies |

### 2.4 MingOS current-state and coordination facts already stale in places

| Item | Evidence | Classification | Foundation change |
|---|---|---|---|
| `CROSS_REPOSITORY_COORDINATION.md` Family-Space baseline `production@2d6d0aeb948b96e178668fa12496d41b6c1a2935` | MingOS coordination contract | **stale** — Family-Space `production` is now `3aec7ea47230c2c8b447178ea8238947ccbd748e` | advisory — MingOS-side refresh, not a Foundation rule |
| Coordination candidate list references source PRs #204/#205 etc. as merge-authoritative | MingOS Issue #33 states these have been absorbed into the #246 → #250 release stack | **stale** — closed/superseded PRs must not remain current merge-authoritative markers | advisory — MingOS Issue #33 already tracks this refresh |
| `FOUNDATION_DEPENDENCY.md` baseline `7eb33ff...` | MingOS | **current** (matches current Foundation main) | no |

### 2.5 What Family-Space is actually validating now

| Evidence | What it demonstrates |
|---|---|
| Family-Space `CURRENT_PROJECT_STATUS.md`: S0 — second-family preparation; real parent = product owner; production authorized 2026-08-11; E0/E1/E2/E3 evidence tiers | The live construction front is a real vertical: first-entry → first response → first three turns → second return → real-life feedback → revised understanding. This is the evidence-led loop Foundation should now serve. |
| Family-Space product contract: FACT/REPORT/FEELING/INTERPRETATION/INFERENCE/UNKNOWN/CORRECTION separation; no-action as a legitimate outcome; product-owned wording/UI/pace | Family-Space is validating Foundation C09 and the "ordinary interaction needs no action" semantics — the exact content of the future `adaptive_default` class |
| Family-Space PR #271 (simplification phase 1, draft) and PR #270 (Response Core VNext, draft): reducing Runtime Decision Depth, removing legacy committee authority (nine-layer / family-stage / loop escalation / V2 recommendation / mandatory action), `RESPONSE_CORE_MODE=off` default | Family-Space is actively subtracting legacy authority — the same direction this rebase codifies for Foundation's relationship to products |
| Family-Space safety boundary, correction chains, provenance-backed memory, stale-context invalidation | Family-Space is implementing Foundation rights/safety commitments as product behavior |

**Verdict:** Family-Space is now the only real construction front and is
validating, in production use, the semantics that this rebase classifies
as `adaptive_default`. This is evidence, not conformance.

### 2.6 Family-Space product implementation must NOT become Foundation rules

| Product detail | Why it must not become a Foundation rule |
|---|---|
| Exact wording, tone, UI, response length, ask/reflect/explain/pause/action cadence | `product_owned_choice` — Foundation must not prescribe these |
| Model/provider selection, prompt topology, agent topology | `product_owned_choice` |
| Family profile, Today / 我家 / 回望 / 我的 navigation, family-specific read model | `product_owned_choice` — do not promote to MingOS Core primitives or Foundation rules merely because they work |
| Context Ledger, Life Translator, Response Posture, Writer/Hard Critic module names | product implementation vocabulary — reusable boundary semantics are in MingOS; the module names stay in Family-Space |
| `RESPONSE_CORE_MODE` flags, allowlists, rollout env vars | product release mechanics — not Foundation semantics |

The forbidden upgrade pattern is:

```text
a Family-Space field → a MingOS object → a Foundation rule
```

This audit rejects that path explicitly. See ADR-0029 and the authority manifest.

### 2.7 Older Foundation work that is provenance, not current execution

| Work | Status | Foundation action |
|---|---|---|
| Day 16 CP0/CP1 synthetic pilot, 12 passes | historical evidence | keep as provenance; no current execution dependency |
| Day 16 controlled-pilot classification `GOV-0087`, `ADR-0023` | historical | retain as retained capability |
| Day 17 role nomination / named accountability `GOV-0094`–`GOV-0098` | historical infrastructure | retain; do not resume as default queue |
| Day 18 restricted nomination and conditional CP2 pre-authorization `GOV-0104`–`GOV-0110`, `ADR-0027`, `ADR-0028` | historical decision records; `CP2 = Blocked / NotExecuted` | **no activation**. No current evidence requires resuming this queue. Retain as provenance and retained capability. |
| Round 07–09 Kernel Draft collections (KERNEL-0000..0005, REF-0045..0051) | Draft, no conformance claim | keep Draft; not a current construction dependency |
| `GOV-0009` Family OS implementation mapping (2026-07-09 snapshot) | historical audit record | preserve in place; Issue #17 current re-audit is delivered as GOV-0115 addendum, not by rewriting GOV-0009 |

## 3. Summary verdict

1. **Foundation permanent principles: correct.** Preserve the Charter root.
2. **Foundation operating model: stale.** The Foundation-first, CP2-next
   default queue no longer matches the real world. It must be re-based to
   evidence-led with CP2 as an inactive retained capability.
3. **MingOS end-state: consistent.** No drift requiring Foundation change.
4. **MingOS coordination facts: partially stale.** Family-Space baseline
   SHA and the candidate PR list are stale; MingOS Issue #33 already tracks
   the refresh. This is advisory for Foundation, not a Foundation rule.
5. **Family-Space: the real construction front.** It is validating the
   semantics that this rebase classifies as `adaptive_default`.
6. **Family-Space implementation must not be promoted.** Product choices
   stay product-owned.
7. **Day 16–18 work is provenance / retained capability.** CP2 remains
   blocked and is not the default next queue.

## 4. What this audit does not claim

- No Charter article has been rewritten.
- No product test result is treated as Foundation conformance.
- No real-family evidence is claimed beyond what Family-Space
  `CURRENT_PROJECT_STATUS.md` itself states (product owner as first real
  parent).
- No CP2 activation is authorized.
- No Kernel Draft is promoted.

## 5. Required follow-up from this audit

Delivered in this rebase:

- `ADR-0029` — three-class authority model and canonical bridge rule;
- authority manifest (`governance/registries/AUTHORITY_MANIFEST.json`);
- `GOV-0115` — current Family-Space re-audit (Issue #17 addendum);
- `ROADMAP.md` re-based to evidence-led with provenance preserved;
- `GOV-0001` current-canonical-state updated to reflect this operating-model change;
- repository validator extended with authority-manifest validation.
