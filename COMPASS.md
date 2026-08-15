# Ming Foundation Compass

> Shared contract: `THREE_REPO_COMPASS_V1`  
> Status: operational compass for maintainers and AI agents.  
> Scope: direction, authority boundaries, anti-drift checks, and three-repository coordination.  
> This file does **not** silently promote, replace, or override the status of the Charter, RFCs, Profiles, ADRs, or governance records. Formal authority still follows the repository's canonical governance rules.

## 1. North Star

Ming Foundation exists to answer one durable question:

> **What must not be sacrificed when technology becomes more capable?**

The long-term aim of the wider MingOS project is not to build a stronger chatbot, parenting expert, agent platform, or optimization system. It is to help create life-supporting infrastructure in which stronger technology leaves people **more able to understand, choose, correct, refuse, act, and live for themselves**.

A useful test is:

```text
system capability ↑
should imply
human understanding / agency / revisability ↑

not
hidden system authority / dependency / control ↑
```

If a proposal makes the system more complete, efficient, persuasive, or governable while making a person less free, less contestable, or more dependent, treat that as an architectural risk.

## 2. Three-repository constitutional map

```text
mingos-foundation
    ↓ defines non-negotiable boundaries

MingOS
    ↓ turns boundaries into reusable cross-space runtime semantics

Family-Space
    ↓ applies them in one real vertical life space

real life
    ↓ produces evidence, failure, counterexample, correction, and unknowns

Family-Space / future Life Spaces
    ↑ repeated evidence may create a MingOS candidate

MingOS
    ↑ only long-lived, genuinely non-negotiable findings may become Foundation candidates
```

The three repositories are **not three parallel products** and must not be kept aligned by copying the same implementation details into all three.

Alignment means authority and semantics remain compatible, not that files, PR numbers, models, prompts, or SHAs are identical.

## 3. Authority classes

Every cross-repository rule or proposal should be classified before it is implemented or promoted.

### 3.1 `hard_invariant` — Foundation-owned

Use only for boundaries that must not be silently traded away for product preference, growth, engagement, automation, model confidence, or implementation convenience.

Examples include, subject to the formal status of their source documents:

- life-safety, violence, abuse, and serious-harm boundaries;
- consent, privacy, coercion, and third-party rights;
- correction, contestability, refusal, exit, and meaningful reversibility;
- no fabricated certainty, diagnosis, or unsupported causal claim;
- evidence, provenance, uncertainty, and knowledge status must not be silently upgraded;
- AI or institutional authority must not silently replace human agency, conscience, or accountable professional judgment;
- legacy/model/category output cannot by itself prescribe **or prohibit**;
- a protective guard requires a current independent evidence owner appropriate to the risk;
- safety powers must remain proportionate, reviewable, and minimally intrusive.

A `hard_invariant` is not an ordinary product mode. It becomes active only when its relevant trigger/evidence exists.

### 3.2 `adaptive_default` — MingOS-owned

Cross-space runtime semantics that help systems operate safely and intelligibly while remaining non-prescriptive and revisable.

Typical examples:

- understanding before advice;
- observation/evidence before interpretation;
- distinguish FACT / REPORT / FEELING / INTERPRETATION / INFERENCE / UNKNOWN / CORRECTION;
- preserve uncertainty and provenance;
- allow new evidence to retire older interpretations;
- ordinary interaction may legitimately end with **no action**;
- optional actions remain rejectable unless an independent Safety authority owns the requirement;
- pacing and response depth follow current evidence and expressed intent, not inherited category authority.

Foundation may constrain this layer, but must not absorb every useful operating default into permanent constitutional law.

### 3.3 `product_owned_choice` — downstream-owned

Products decide how to help inside the higher-level boundaries.

Examples:

- exact wording, tone, length, rhythm, and interface;
- whether to reflect, ask, explain, pause, or offer an action in an ordinary interaction;
- action wording and cadence;
- model/provider selection;
- prompt, agent, router, and orchestration topology;
- product-specific profiles, navigation, read models, UI, and domain language.

A successful Family-Space mechanism does not become a MingOS primitive or Foundation rule merely because it exists or works once.

## 4. Canonical bridge rule

Use this sentence when repository boundaries are unclear:

> **Foundation defines what must never be violated. MingOS defines how authority, evidence, context, memory, correction, and action semantics travel across spaces. Products decide how to help within those boundaries.**

A lower layer may discover evidence that challenges a higher layer. It may not silently rewrite the higher layer.

A higher layer may constrain a lower layer. It should not prescribe ordinary product behavior without a real hard-invariant reason.

## 5. Evidence-led evolution

Foundation must not become a theory-first expansion project that attempts to finish a universal life system before reality has tested it.

Preferred evolution:

```text
North Star + current hard boundaries
        ↓
minimum runnable product/system
        ↓
real life
        ↓
failure / counterexample / correction / useful result / unknown
        ↓
product learning
        ↓
cross-space candidate
        ↓
MingOS abstraction and validation
        ↓
only durable non-negotiable findings become Foundation candidates
```

Historical governance programs, pilots, role structures, RFCs, Profiles, and review machinery remain valuable provenance and may be reactivated when current evidence or authorization requires them. Their existence alone must not make them the default next task.

**No change, no activation, no new rule, and UNKNOWN are legitimate outcomes.**

## 6. Anti-drift rules

### A. Do not synchronize by stale construction details

Do not encode moving Family-Space PR numbers, branch names, UI fields, prompt names, or temporary product stages as permanent Foundation truth.

Use exact SHAs and PRs as evidence records when auditing a point in time; do not turn them into long-lived constitutional dependencies.

### B. Synchronize semantics and authority

Cross-repository compatibility should answer:

1. Which Foundation hard boundaries are being relied on?
2. Which MingOS runtime semantics are being adopted?
3. Which choices remain product-owned?
4. What evidence activates a hard guard?
5. What is still unknown or provisional?

### C. Preserve historical truth without letting history run the present

Accepted historical audits remain historical facts about their stated scope. They must not be silently rewritten to look current.

When the implementation changes materially, create a current re-audit/addendum through the repository's governance process.

### D. Product evidence is evidence, not conformance

A passing product regression, synthetic eval, one successful real interaction, or one production release does not by itself establish Foundation conformance, universal validity, or a stable standard.

### E. Protect the right to remain unabstracted

A product-specific field, family concept, workflow, or successful response pattern may remain product-specific indefinitely. Upstream promotion is optional and evidence-burdened.

## 7. Complexity budget

Before creating another Layer, Gate, Role, Profile, Classifier, State, universal object, review workflow, or governance mechanism, answer:

> **What current, reproducible problem cannot be solved safely without this new structure?**

If there is no concrete answer, prefer:

- deleting stale authority;
- narrowing a rule;
- combining duplicated responsibilities;
- recording an UNKNOWN;
- preserving a proposal without activating it;
- waiting for better evidence.

Foundation quality is not measured by document count.

## 8. Decision checks

Before changing Foundation, ask:

1. Is this truly non-negotiable across products and contexts, or merely a good current practice?
2. What current evidence or counterexample motivates the change?
3. Does the change protect life, or protect the framework from being wrong?
4. Does it increase human agency and correction rights, or increase hidden system authority?
5. Could this remain a MingOS adaptive default or product choice instead?
6. What evidence would make us reverse this decision?
7. Are we preserving affected-person voice, third-party rights, uncertainty, and dissent?
8. Are we confusing a well-written rule with a validated rule?

If these cannot be answered, do not promote the rule.

## 9. Repository-specific mission

Ming Foundation should primarily maintain:

- the Charter of Life and MingOS self-restraint boundaries;
- rights, safety, evidence, provenance, accountability, and governance constraints;
- the process by which claims become reviewable and correctable;
- failure, counterexample, dissent, and unknown preservation;
- current audits that distinguish historical evidence from present evidence.

It should **not** become the owner of:

- Family-Space response templates or UI;
- family stages, navigation coordinates, or product profiles;
- provider/model choices;
- a universal agent topology;
- ordinary response cadence;
- product roadmaps;
- implementation details that have not earned cross-space authority.

## 10. When sources conflict

Use formal repository authority rules first. This Compass is a navigation and anti-drift surface, not a shortcut around governance status.

When a newer real-world observation conflicts with an older Accepted historical audit:

- preserve the old audit as historical truth within its scope;
- record the new evidence separately;
- create the appropriate review/revision path;
- do not make either side disappear for convenience.

Truth before theory also means Foundation must remain correctable.

## 11. Current operating posture

Until current evidence justifies otherwise:

- treat Family-Space as the first major real-world validation surface, not as the definition of all future Life Spaces;
- let Family-Space continue product learning without waiting for Foundation to become complete;
- let MingOS add abstractions only when a cross-space semantic need is demonstrated;
- let Foundation add or strengthen rules only when they are genuinely non-negotiable and evidence-backed;
- prefer reality-led correction over framework completion.

## 12. Shared compass change protocol

`THREE_REPO_COMPASS_V1` identifies the shared semantic contract, not identical file contents.

The shared semantics are:

- the North Star direction;
- the three-repository constitutional map;
- the three authority classes and their owners;
- the Foundation → MingOS → Product bridge;
- no silent authority upgrade;
- evidence is not automatic conformance;
- reality may challenge every layer.

A material change to these shared semantics MUST NOT be silently made in one repository as though the other two already agree.

When a shared semantic change is needed, either:

1. create/update companion changes in the affected repositories; or
2. explicitly record a `temporary_divergence` with the reason, affected semantics, evidence, responsible owner, and the condition for convergence.

Moving facts — current product stage, PR number, deployment SHA, provider status, or a local implementation detail — remain owned by their source repository and do **not** require synchronized Compass edits.

`THREE_REPO_COMPASS_V1` should change only when all three repositories have adopted a materially new compatible shared contract.

## 13. One-line compass

> **Ming Foundation protects what must not be sacrificed; it does not decide how every life-supporting product must look or speak.**
