---
id: KERNEL-0005
title: MingOS Kernel Test Specifications and Derived Indexes
status: Draft
version: 0.1.0-draft.1
layer: Layer 2 — Standards
owner: Ming Foundation Kernel Conformance
created: 2026-07-15
updated: 2026-07-15
language: en
canonical_language: en
translation_status: original
decision_base_commit: 29485e67279d11401bb0f9f2b9afc78f0bdf67f4
related:
  - MOS-0000
  - KERNEL-0000
  - KERNEL-0001
  - KERNEL-0002
  - KERNEL-0003
  - KERNEL-0004
  - REF-0047
  - REF-0049
  - REF-0050
depends_on:
  - KERNEL-0004
---

# KERNEL-0005 — MingOS Kernel Test Specifications and Derived Indexes

> A test specification is not a test execution. No test is executed by publication.

## 1. Purpose and non-goals

Define governed test identity, execution records, results, coverage, adversarial scenarios, evidence protection and derived indexes. This Draft is not a harness, certification service, real-person study, passing result or conformance decision.

## 2. Test-governance requirement traceability

External `R9SRC-*` references resolve through the exact KERNEL-0004 source
baseline. KERNEL-0004 references are collection-local Draft sources.

| ID | Domain | Level | Requirement | Exact sources | Source treatment | Proposed verification | Expected evidence |
|---|---|---|---|---|---|---|---|
| KTG-0001 | TestIdentity | `MUST` | Every test specification MUST have stable identity, version, requirement references and change history. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0011–0018 / CollectionLocalDraft; R9SRC-MOS-0000 §12 and §17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0002 | TestNeutrality | `MUST` | A test MUST describe observable behavior and evidence without requiring one vendor, model, database or UI. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0011–0018 / CollectionLocalDraft; R9SRC-MOS-0000 §12 and §17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0003 | PositiveNegative | `MUST` | Mandatory behavior requires positive and negative coverage where meaningful. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0011–0018 / CollectionLocalDraft; R9SRC-MOS-0000 §12 and §17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0004 | ProhibitionAdversarial | `MUST` | MUST NOT and SHOULD NOT requirements require adversarial or misuse coverage. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0011–0018 / CollectionLocalDraft; R9SRC-MOS-0000 §12 and §17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0005 | Counterexample | `MUST` | Tests MUST preserve counterexamples and Inconclusive outcomes. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0011–0018 / CollectionLocalDraft; R9SRC-MOS-0000 §12 and §17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0006 | Preconditions | `MUST` | Every execution MUST record preconditions, environment and applicable Profile. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0011–0018 / CollectionLocalDraft; R9SRC-MOS-0000 §12 and §17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0007 | DataClass | `MUST` | Every execution MUST identify synthetic, internal, restricted personal or other governed evidence class. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0011–0018 / CollectionLocalDraft; R9SRC-MOS-0000 §12 and §17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | EvidenceEnvironmentInspection; SensitiveDataMisuseScenario | EvidenceHandlingPlan; SecurityOrPrivacyFinding |
| KTG-0008 | NoRealDataDefault | `MUST NOT` | A test specification MUST NOT require real identifiable affected-person data when synthetic or de-identified evidence is sufficient. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0011–0018 / CollectionLocalDraft; R9SRC-MOS-0000 §12 and §17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | EvidenceEnvironmentInspection; SensitiveDataMisuseScenario | EvidenceHandlingPlan; SecurityOrPrivacyFinding |
| KTG-0009 | ExpectedOutcome | `MUST` | Expected outcomes MUST distinguish system behavior, record state, user-visible behavior and evidence. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0011–0018 / CollectionLocalDraft; R9SRC-MOS-0000 §12 and §17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0010 | FailureMeaning | `MUST` | Failure MUST identify violated expectation, affected scope and required containment. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0011–0018 / CollectionLocalDraft; R9SRC-MOS-0000 §12 and §17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0011 | BlockedMeaning | `MUST` | Blocked MUST identify missing dependency, owner and next condition. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0011–0018 / CollectionLocalDraft; R9SRC-MOS-0000 §12 and §17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0012 | InconclusiveMeaning | `MUST` | Inconclusive MUST preserve uncertainty and MUST NOT be counted as Pass. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0011–0018 / CollectionLocalDraft; R9SRC-MOS-0000 §12 and §17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0013 | InvalidatedMeaning | `MUST` | A result becomes Invalidated when material test, implementation, environment or source changes break comparability. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0011–0018 / CollectionLocalDraft; R9SRC-MOS-0000 §12 and §17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0014 | Expiry | `MUST` | Time-sensitive test evidence MUST expire or be re-run. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0011–0018 / CollectionLocalDraft; R9SRC-MOS-0000 §12 and §17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0015 | StateMachineCoverage | `MUST` | Each object state machine MUST test allowed, forbidden, expiry, appeal and concurrency behavior where applicable. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0014–0026 / CollectionLocalDraft; R9SRC-KERNEL-0002 §4 and §6–11 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4–12 [Round08MergedDraft] | `TestGovernanceOperationalizationOfDraftConformanceModel` | StateMachineCoverageInspection; InvalidTransitionScenario | TestSpecification; TransitionExecutionRecord |
| KTG-0016 | ProcessStateSeparation | `MUST` | Tests MUST detect process stages incorrectly stored as object states. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0014–0026 / CollectionLocalDraft; R9SRC-KERNEL-0002 §4 and §6–11 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4–12 [Round08MergedDraft] | `TestGovernanceOperationalizationOfDraftConformanceModel` | StateMachineCoverageInspection; InvalidTransitionScenario | TestSpecification; TransitionExecutionRecord |
| KTG-0017 | LineageCoverage | `MUST` | Derived records and decisions MUST be traceable to source and transformation history. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0014–0026 / CollectionLocalDraft; R9SRC-KERNEL-0002 §4 and §6–11 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4–12 [Round08MergedDraft] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0018 | CorrectionPropagation | `MUST` | Correction tests MUST inspect active, derived, indexed, shared and future-use effects. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0014–0026 / CollectionLocalDraft; R9SRC-KERNEL-0002 §4 and §6–11 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4–12 [Round08MergedDraft] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0019 | RightsCompletion | `MUST` | Rights-request tests MUST inspect primary, derived, shared and backup completion or bounded exception. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0014–0026 / CollectionLocalDraft; R9SRC-KERNEL-0002 §4 and §6–11 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4–12 [Round08MergedDraft] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0020 | HandoffEvidence | `MUST` | Handoff tests MUST distinguish initiation, acknowledgment, acceptance, failure and closure. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0014–0026 / CollectionLocalDraft; R9SRC-KERNEL-0002 §4 and §6–11 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4–12 [Round08MergedDraft] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0021 | HumanAccountability | `MUST` | High-impact tests MUST demonstrate actual human authority, information and stop capacity. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0014–0026 / CollectionLocalDraft; R9SRC-KERNEL-0002 §4 and §6–11 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4–12 [Round08MergedDraft] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0022 | AffectedPersonUsability | `MUST` | Applicable tests MUST assess whether notice, correction, refusal and appeal are usable. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0014–0026 / CollectionLocalDraft; R9SRC-KERNEL-0002 §4 and §6–11 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4–12 [Round08MergedDraft] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0023 | Accessibility | `MUST` | Applicable tests MUST include language, disability, literacy, bandwidth and private-contact constraints. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0014–0026 / CollectionLocalDraft; R9SRC-KERNEL-0002 §4 and §6–11 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4–12 [Round08MergedDraft] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0024 | OperatorAsRisk | `MUST` | Safety and representative tests MUST include operator or representative as possible source of harm. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0014–0026 / CollectionLocalDraft; R9SRC-KERNEL-0002 §4 and §6–11 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4–12 [Round08MergedDraft] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0025 | ResourceFreshness | `MUST` | Resource tests MUST include stale, disputed, inaccessible and unavailable conditions. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0014–0026 / CollectionLocalDraft; R9SRC-KERNEL-0002 §4 and §6–11 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4–12 [Round08MergedDraft] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0026 | ClaimAudit | `MUST` | Public-claim tests MUST compare exact wording to current evidence and status. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0031–0042 / CollectionLocalDraft; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol]; R9SRC-MOS-0000 §12–17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | ClaimLanguageAudit; SelfCertificationNegativeScenario | ClaimAudit; ReviewDecision |
| KTG-0027 | NoSelfCertification | `MUST NOT` | A passing self-run test suite MUST NOT be represented as independent certification. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0031–0042 / CollectionLocalDraft; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol]; R9SRC-MOS-0000 §12–17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | ClaimLanguageAudit; SelfCertificationNegativeScenario | ClaimAudit; ReviewDecision |
| KTG-0028 | ExecutionSeparation | `MUST` | Test specification, execution, review and conformance decision MUST remain distinct records. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0031–0042 / CollectionLocalDraft; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol]; R9SRC-MOS-0000 §12–17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0029 | Reproducibility | `SHOULD` | Automated and controlled tests SHOULD record enough environment detail for bounded reproduction. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0031–0042 / CollectionLocalDraft; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol]; R9SRC-MOS-0000 §12–17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0030 | Security | `MUST` | Test infrastructure and artifacts MUST protect secrets, personal data and restricted evidence. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0031–0042 / CollectionLocalDraft; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol]; R9SRC-MOS-0000 §12–17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | EvidenceEnvironmentInspection; SensitiveDataMisuseScenario | EvidenceHandlingPlan; SecurityOrPrivacyFinding |
| KTG-0031 | Regression | `MUST` | Material changes require targeted regression and affected-claim review. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0031–0042 / CollectionLocalDraft; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol]; R9SRC-MOS-0000 §12–17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | TestSpecificationInspection; NegativeOrBoundaryExecutionScenario | TestSpecification; ExecutionRecord |
| KTG-0032 | NoCurrentExecutionClaim | `MUST NOT` | Publishing KERNEL-0005 or its derived catalog MUST NOT imply that any test was executed. | KERNEL-0004 / Draft / 0.1.0-draft.1 / `standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md` / §4 KCF-0031–0042 / CollectionLocalDraft; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol]; R9SRC-MOS-0000 §12–17 [DraftStandardsProcess] | `TestGovernanceOperationalizationOfDraftConformanceModel` | ClaimLanguageAudit; SelfCertificationNegativeScenario | ClaimAudit; ReviewDecision |

## 3. Result states

```text
NotExecuted
Pass
Fail
Blocked
Inconclusive
NotApplicable
Invalidated
Expired
```

## 4. Requirement test catalog

```text
KCR: 36
KDO: 36
KLS: 34
Total primary tests: 106
Execution status: NotExecuted
```

Full records are in `mingos-kernel-test-specifications.json` and REF-0047.

## 5. Cross-cutting scenarios

| ID | Scenario | Boundary |
|---|---|---|
| KSC-0001 | ThirdPartyStatement | A parent or professional statement remains attributed and contestable. |
| KSC-0002 | RefusalWithoutPenalty | Silence, disagreement or withdrawal is not agreement or adverse identity evidence. |
| KSC-0003 | RepresentativeConflict | A representative who may be the harm source cannot authorize and close the action. |
| KSC-0004 | CorrectionPropagation | Correction updates active, derived, indexed and future uses while retaining lineage. |
| KSC-0005 | SourceLoss | A derived conclusion without lineage becomes restricted or invalid. |
| KSC-0006 | UncertainAdvice | Material uncertainty slows, narrows or escalates advice. |
| KSC-0007 | HiddenPersuasion | Anxiety, shame, urgency and dependency are not used for consent, purchase or retention. |
| KSC-0008 | UnavailableHandoff | A generated resource or sent message is not accepted service. |
| KSC-0009 | EmergencyTemporaryAction | Protective action is necessary, proportionate, time-bounded and reviewable. |
| KSC-0010 | DeletionWithBackup | Deletion addresses primary, derived, shared and backup behavior. |
| KSC-0011 | RiskProfileExpiry | Temporary risk state does not become permanent identity. |
| KSC-0012 | SecondaryUse | Sensitive data cannot silently enter analytics, training or marketing. |
| KSC-0013 | AIDisclosure | AI role, limitations and provider/version remain visible. |
| KSC-0014 | HumanAccountability | Named human has actual information, authority and stop capacity. |
| KSC-0015 | ParticipationImpossible | Unsafe or inaccessible participation receives explicit handling. |
| KSC-0016 | InvalidTransition | Undefined object transition is rejected. |
| KSC-0017 | ProcessStageConfusion | Process stage is not stored as every object state. |
| KSC-0018 | StaleResource | Expired or disputed resource stops current presentation. |
| KSC-0019 | IncidentAppeal | Incident and appeal preserve independent review and reopening. |
| KSC-0020 | ClaimExpiry | Expired or changed evidence suspends the claim. |
| KSC-0021 | CrossLanguage | Translated labels preserve source status and distinctions. |
| KSC-0022 | Accessibility | Rights remain usable across language, disability and bandwidth. |
| KSC-0023 | OperatorAsRisk | System does not automatically side with the operator. |
| KSC-0024 | PublicClaim | Draft, Planned, Available and conforming language are not conflated. |

## 6. Execution, privacy and review boundary

Executions record test/version, requirement, implementation boundary, family/Profile versions, environment, evidence class, executor, result, observations, evidence, limitations and reviewer. Synthetic/minimized evidence is the default. Tests do not replace affected-person, professional, jurisdiction or independent review.

## 7. Limitations and version history

Automated harnesses, reproducibility, nondeterministic AI, accessibility and longitudinal evidence remain open.

| Version | Date | Change | Status |
|---|---|---|---|
| 0.1.0-draft.1 | 2026-07-15 | Initial 32 governance requirements, 106 tests and 24 scenarios | Draft |

```text
Executed tests: 0
Pass results: 0
Conformance decisions: 0
Overall: NoCurrentKernelConformanceClaim
```
