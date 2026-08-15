# Ming Foundation Agent Working Contract

Any AI agent, coding agent, automation, or maintainer entering this repository must use the following reading order before changing files.

## First read

1. `COMPASS.md` — current direction, three-repository role, authority classes, and anti-drift rules;
2. `governance/status/GOV-0001-current-canonical-state.md` — current canonical repository state and formal authority order;
3. the exact Charter / RFC / Profile / ADR / governance documents relevant to the task;
4. current issue / PR / reservation evidence for the requested work;
5. current downstream evidence only when the task explicitly depends on MingOS or Family-Space.

`COMPASS.md` is an operational navigation surface. It does not override formal document status or accepted governance decisions.

## Working rule

```text
read current authority
→ classify hard_invariant / adaptive_default / product_owned_choice
→ inspect current evidence
→ find the smallest real delta
→ preserve counterexamples and unknowns
→ change only the layer that owns the decision
→ validate
→ record what remains uncertain
```

## Hard constraints

- Do not turn a useful Family-Space implementation into a Foundation rule merely because it exists.
- Do not turn a MingOS adaptive default into a hard invariant without evidence and the proper governance path.
- Do not treat a merged Draft / Proposed / Candidate document as Accepted or Stable.
- Do not silently rewrite historical audits to make them look current.
- Do not use synthetic tests, one real interaction, or product deployment as automatic Foundation conformance evidence.
- Do not publish real-family data, restricted evidence, secrets, or identity records.
- Do not expand governance structure merely to make the repository look complete.
- Do not directly modify `main` unless the repository owner has explicitly authorized that exact write path.

## Complexity gate

Before adding a new Layer, Gate, Role, Profile, Classifier, universal object, pilot structure, or governance workflow, state the current reproducible problem that cannot be solved safely without it.

If that problem is not evidenced, prefer no change, narrower authority, deletion, supersession, or UNKNOWN.

## Cross-repository rule

```text
Foundation → hard boundaries
MingOS     → reusable cross-space semantics
Products   → product-owned implementation
Real life  → evidence that may challenge every layer
```

A lower layer may generate evidence for review. It cannot silently promote itself into a higher layer.

A higher layer may constrain a lower layer. It should not prescribe ordinary product behavior without a hard-invariant reason.
