---
created: 2026-07-12
depends_on:
- ADR-0003
- ADR-0004
id: GOV-0002
layer: Layer 5 — Community & Governance
owner: Ming Foundation Governance
related:
- GOV-0001
- GOV-0003
- ADR-0003
- ADR-0004
- PROJECT-MINGOS-0001
- GOV-0007
- GOV-0008
- GOV-0009
status: Accepted
title: Source Registry
updated: 2026-08-06
version: 1.0.0-alpha.18
---

# GOV-0002 — Source Registry

## 1. Purpose

This registry records the known source classes from which Ming
Foundation and MingOS knowledge may be derived. It prevents source
confusion, accidental authority escalation, and loss of provenance
across repositories, websites, conversation windows, codebases, and
handoff packages.

## 2. Source status vocabulary

- **Canonical:** current authoritative source for a defined scope.
- **Official:** an approved public representation, which should derive
  from canonical records.
- **Accepted:** reviewed and adopted, but not necessarily the sole
  source for every scope.
- **Draft:** under active development and not yet authoritative.
- **Experimental:** retained to test a possible direction.
- **Superseded:** replaced by a newer accepted source.
- **Archived:** preserved for historical traceability and not used for
  current decisions.
- **Unregistered:** known to exist but not yet reviewed or assigned
  authority.

## 3. Registered sources

| Source ID | Source                                                                                                   | Role                                                              | Authority                                                | Current state                                          | Handling rule                                                                                                       |
|-----------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|----------------------------------------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| SRC-0001  | `YuemingHub/mingos-foundation` default branch                                                              | Public knowledge repository for formalized project outcomes       | Canonical for published project knowledge and governance | Active                                                 | Accepted repository documents govern their stated scope                                                             |

| SRC-0002  | `https://mingos.cn`                                                                                      | Official MingOS public website                                    | Official public representation                           | Active                                                 | Public claims SHOULD be traceable to repository records                                                             |
| SRC-0003  | Cross-window MingOS conversations                                                                        | Exploration, synthesis, critique, and drafting                    | Non-canonical source                                     | Active                                                 | Process through `GOV-0003` before repository adoption                                                               |
| SRC-0004  | Codex, coding-agent, and developer conversations                                                         | Implementation analysis and delivery planning                     | Non-canonical source                                     | Active                                                 | Preserve technical evidence; convert material decisions into ADR, RFC, standard, project, or implementation records |
| SRC-0005  | `Ming-Foundation-Day1-v1.0` handoff package                                                              | Initial repository construction package                           | Superseded by imported repository state                  | Archived after import                                  | Use Git history and current repository files, not the package, for current authority                                |
| SRC-0006  | Day 2 and future structured handoff packages                                                             | Transfer artifacts prepared for repository application            | Proposed until merged                                    | Active                                                 | Package contents gain repository status only after merge                                                            |
| SRC-0007  | Historical ZIP files and early architecture packs                                                        | Early exploration and delivery attempts                           | Non-canonical                                            | Unregistered / Archived                                | Review before use; mark Superseded where appropriate                                                                |
| SRC-0008  | Product and implementation repositories                                                                  | Runtime evidence and implementation constraints                   | Scope-dependent                                          | Unregistered until explicitly recorded                 | Do not infer repository names, ownership, or authority without registration                                         |
| SRC-0009  | Research papers, books, standards, and external evidence                                                 | Scientific, philosophical, legal, and technical input             | Informative unless adopted                               | Ongoing                                                | Record citations, limitations, date, and applicability; research does not automatically become a standard           |
| SRC-0010  | De-identified cases and field observations                                                               | Validation evidence for standards and products                    | Evidence, not automatic authority                        | Restricted                                             | Must follow consent, privacy, de-identification, and access rules                                                   |
| SRC-0011  | MingOS website implementation and deployment snapshot (`YuemingHub/Mingos-life`, production `mingos.cn`) | Website implementation and operational evidence                   | Scope-limited implementation evidence                    | Active, direct repository access not verified in Day 5 | Use for bounded audit; re-verify current repository and live pages before relying on freshness                      |
| SRC-0012  | `CODE_WIKI.md` Family OS snapshot dated 2026-07-09                                                       | Structured implementation inventory                               | Documentary implementation evidence                      | Active snapshot, not a direct current code audit       | Preserve date and limitations; verify against current code and tests before conformance claims                      |
| SRC-0013  | Structured MingOS architecture and deployment discussion record dated 2026-07-12                         | Deployment, product, website, and implementation context          | Non-canonical source evidence                            | Active                                                 | Extract governed findings; do not publish secrets, credentials, private operations, or raw personal data            |
| SRC-0014  | Independent external Charter reviews                                                                     | Domain review, objections, and recommendations                    | Evidence, not automatic authority                        | Prepared, review not yet completed                     | Preserve conflict disclosures, conditions, dissent, and publication preference                                      |
| SRC-0015  | Affected-person Charter review evidence                                                                  | Lived and affected experience                                     | Restricted evidence, not automatic authority             | Prepared, collection not yet completed                 | Store outside public repository under `GOV-0018`; publish only safe aggregate findings                              |
| SRC-0016  | Day 7 direct website and implementation audit evidence                                                   | Current code, page, configuration, test, and operational evidence | Scope-limited direct evidence                            | Planned                                                | Record revision, environment, method, result, limitation, and restricted-data boundary                              |
| SRC-0017  | `YuemingHub/Ming-Foundation` historical repository path                                  | Historical name for the Foundation repository                       | Historical / not current                                | Archived                                               | Preserve for provenance; do not use as current canonical identifier                                        |

## 4. Public repository inclusion rule

Project-relevant outcomes SHOULD eventually be represented in the
canonical repository, but the following MUST NOT be committed to the
public repository unless an explicit, lawful, reviewed basis exists:

- identifiable family or child information;
- private counseling or consultation records;
- medical or mental-health records;
- raw credentials, tokens, keys, or secrets;
- private contact information;
- proprietary third-party material without permission;
- content whose publication would create a foreseeable safety risk.

The duty to account for discussion does not override privacy, consent,
copyright, or safety.

## 5. Registration requirements for new sources

A new material source SHOULD be added to this registry with:

- stable name or locator;
- owner or steward when known;
- scope;
- authority level;
- current state;
- privacy classification;
- import or synchronization rule;
- known limitations;
- review date when the source may become stale.

## 6. Website synchronization

`mingos.cn` is official but not an independent normative source. When
the website and accepted repository records conflict:

1.  identify whether the repository record is current;
2.  correct the website if it is stale or inaccurate;
3.  use an RFC or ADR if the website reveals a needed project-level
    change;
4.  do not silently modify repository doctrine merely to match published
    marketing copy.

## 7. Historical import policy

Historical discussion material should be imported by topic, not by chat
chronology. Recommended import groups are:

1.  identity, mission, naming, and boundaries;
2.  Life Charter and MingOS Charter;
3.  life logic, theory, ontology, and terminology;
4.  MOSS and Kernel;
5.  Ming Family and real implementation evidence;
6.  memory, agents, SDK, cloud, and ecosystem proposals;
7.  website, white paper, and public communication.

Each import MUST preserve uncertainty and identify duplicates,
conflicts, rejected directions, and unresolved questions. \## 8.
Validation source rule

A deployment report, code wiki, screenshot, conversation, or agent
statement may support an evidence record, but it MUST NOT be described
as a direct current audit unless the reviewed artifact, revision,
environment, and test result are independently available.

Day 5 therefore distinguishes:

- repository-verified evidence;
- documentary implementation evidence;
- live or production evidence not independently re-verified;
- evidence not yet collected.
## 9. Day 7 access outcome

Day 7 directly verified the canonical Ming Foundation repository.

The private website repository, current Family OS source repository, and live domains were not accessible to the audit environment. `SRC-0016` therefore remains incomplete and MUST NOT be described as a completed direct implementation audit.

See `GOV-0021`.

## 10. Canonical audit versus external evidence

`YuemingHub/mingos-foundation` is the current canonical repository.

Product repositories, website sources, domains, runtime reports, and code snapshots are external evidence sources. They may test implementation conformance, but they:

- do not become canonical authority;
- do not block canonical repository audit or development;
- are not active work targets without explicit user scope;
- must retain revision, method, authority, and limitation metadata.

See `GOV-0027` and `ADR-0009`.
## 11. Day 8 structured evidence sources

The following structured records are repository infrastructure rather than independent truth sources:

- RFC requirement registry — derived from RFC source text;
- conformance matrices — bounded findings about a named target and revision;
- external implementation evidence intake records — non-canonical evidence governed by `GOV-0030`.

These records must identify authority and limitations. They never silently override the source RFC or canonical repository.
## 12. Day 9 review and baseline records

The following are structured governance infrastructure:

- requirement fidelity review;
- acceptance-test specifications;
- RFC review checklists;
- ambiguity and revision register;
- non-implementation conformance baseline.

They describe preparation, structure, or open questions. They are not implementation evidence and do not promote an RFC.

## Day 10 internal review evidence

Internal review results, revision plans, and dissent records are canonical governance evidence about RFC quality. They are not product, external, affected-person, legal, or conformance evidence.

## 14. Day 11 source revision evidence

RFC source text, exact Git blob SHAs, revision-plan state, and synchronized
requirement and test registries are canonical repository evidence.

They do not constitute implementation, external-review, legal, or
affected-person evidence.

## 15. Day 12 review and test evidence

Round 2 internal review records and repository source-test results are
canonical governance evidence.

The 63-item requirement registry remains a historical derived baseline for
earlier source and is explicitly pending re-baselining for RFC-0001 through
RFC-0003 `0.2.0-draft.1`.

## 16. Day 13 requirement and profile sources

The current 115-requirement registry, 115-test specification registry,
legacy archives, identity mapping, and four Proposed profiles are canonical
repository records.

They are not product implementation evidence or affected-person acceptance.

## 17. Day 14 review and preparation evidence

Profile internal-review results, revision plans, review instruments,
safeguards, and preparation state are canonical governance evidence.

They are not participant evidence, affected-person acceptance, legal
qualification, or implementation conformance.

## 18. Day 15 Profile revision and readiness evidence

Current Profile sources, archived historical snapshots, revision evidence,
source tests, Round 2 review, readiness gate, and operational activation
register are canonical governance records.

They are not participant evidence, legal qualification, operational
authorization, or product conformance.

## 19. Day 16 operational and synthetic evidence

Role, protocol, environment, pilot authorization, synthetic scenario, and
synthetic result registries are canonical governance evidence.

They are not participant evidence, human-use approval, legal qualification,
live-system evidence, or product implementation conformance.

## 19. Day 17 accountability evidence

Public accountability state, restricted-record references, small-team
separation rules, nomination workflow, protocol approval routes, environment
deployment plan, tabletop evidence, and activation gate are canonical
governance records.

They are not real-person assignments, private identity records, human-use
approvals, live control evidence, or participant evidence.

## 20. Day 18 restricted nomination evidence

Public slot states, non-identifying restricted-record references,
pre-authorization decisions, and synthetic tabletop evidence are canonical
governance records.

Private identity, qualification, conflict, signature, and acceptance records
remain outside the public repository.
## 11. Repository identity transition

On 2026-08-06, the named human owner accepted
`YuemingHub/mingos-foundation` as the current Foundation repository.
`YuemingHub/Ming-Foundation` remains a historical identifier for provenance only.
Existing source records and filenames are not silently rewritten; all new
current references MUST use the canonical path above.
