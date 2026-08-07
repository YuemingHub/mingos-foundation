---
id: KERNEL-0004
title: MingOS Kernel Conformance Requirements and Evidence Model
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
  - ADR-0026
  - MOS-0000
  - KERNEL-0000
  - KERNEL-0001
  - KERNEL-0002
  - KERNEL-0003
  - KERNEL-0005
  - REF-0045
  - REF-0046
  - REF-0048
  - REF-0049
  - REF-0050
  - REF-0051
depends_on:
  - KERNEL-0000
  - KERNEL-0001
  - KERNEL-0002
  - KERNEL-0003
---

# KERNEL-0004 — MingOS Kernel Conformance Requirements and Evidence Model

> Draft conformance specification. Publication does not authorize a claim, certification, badge or approved implementation.

## 1. Purpose, scope and definitions

Define bounded claim units, applicability, evidence, review, exceptions, suspension, expiry, reassessment and public wording. An assessment boundary is one exact implementation/version/surface/operator. A Conformance Profile is governed applicability, not a marketing label. `MeetsSpecifiedProfile` is unavailable while required documents or evidence remain Draft/incomplete.

## 2. Exact Round 08 source baseline

Each `R9SRC-*` reference in the requirement table resolves through this exact
base-commit and Blob table. The Agent fills Blob identities from the actual
Round 08 merge before publication.

| Baseline ref | Source | Status | Version | Path | Base commit | Blob | Role |
|---|---|---|---|---|---|---|---|
| R9SRC-KERNEL-0000 | KERNEL-0000 | Draft | 0.4.0-draft.4 | `standards/kernel/KERNEL-0000-specification-family-index.md` | `29485e67279d11401bb0f9f2b9afc78f0bdf67f4` | `1c85cf82347d9006f6bdf52192b3a948d16fc271` | `Round08MergedDraft` |
| R9SRC-KERNEL-0001 | KERNEL-0001 | Draft | 0.2.2-draft.4 | `standards/kernel/KERNEL-0001-core-operational-contract.md` | `29485e67279d11401bb0f9f2b9afc78f0bdf67f4` | `972a13e487da01ce2ab59077232547b938ef7942` | `Round08MergedDraft` |
| R9SRC-KERNEL-0002 | KERNEL-0002 | Draft | 0.2.0-draft.2 | `standards/kernel/KERNEL-0002-canonical-object-data-model.md` | `29485e67279d11401bb0f9f2b9afc78f0bdf67f4` | `f926bfc318bd4df861eb078f7485cfcb58f240dd` | `Round08MergedDraft` |
| R9SRC-KERNEL-0003 | KERNEL-0003 | Draft | 0.2.0-draft.2 | `standards/kernel/KERNEL-0003-lifecycle-state-machines.md` | `29485e67279d11401bb0f9f2b9afc78f0bdf67f4` | `d42fa308c6ad4904a4aa3bc67ee99f128c73a2dc` | `Round08MergedDraft` |
| R9SRC-MOS-0000 | MOS-0000 | Draft | 1.0.0-alpha.11 | `standards/mos/MOS-0000-standard-process.md` | `29485e67279d11401bb0f9f2b9afc78f0bdf67f4` | `8dab1e6a846e7af0fd2260a6afb21ab8026a6110` | `DraftStandardsProcess` |
| R9SRC-REF-0028 | REF-0028 | Draft | 0.2.0-draft.1 | `reference/kernel/REF-0028-kernel-conformance-replaceability-claim-boundary.md` | `29485e67279d11401bb0f9f2b9afc78f0bdf67f4` | `57bff35b297e4be1697c91225c098d9eae6fa48e` | `DraftConformanceBoundary` |
| R9SRC-RFC-0005 | RFC-0005 | Proposed | 0.1.0 | `standards/rfc/RFC-0005-public-claim-charter-sync-and-capability-status.md` | `29485e67279d11401bb0f9f2b9afc78f0bdf67f4` | `61da3f762705997d397ec9d1e0c55b6b7fa8c6d4` | `ProposedPublicClaimProtocol` |

## 3. Normative conformance requirements

| ID | Domain | Level | Requirement | Exact sources | Source treatment | Proposed verification | Expected evidence |
|---|---|---|---|---|---|---|---|
| KCF-0001 | DeclaredBoundary | `MUST` | An assessment MUST identify one bounded implementation, version, governed surfaces, organization and accountable human role. | R9SRC-KERNEL-0000 §4–6 and §9 [Round08MergedDraft]; R9SRC-KERNEL-0001 §4 KCR-0001–0003 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0002 | ExactVersionSet | `MUST` | An assessment MUST identify the exact Kernel family, RFC and Profile versions and statuses used. | R9SRC-KERNEL-0000 §4–6 and §9 [Round08MergedDraft]; R9SRC-KERNEL-0001 §4 KCR-0001–0003 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0003 | ClaimUnit | `MUST` | A claim MUST name one assessable boundary and MUST NOT silently extend to a company, ecosystem or unrelated product. | R9SRC-KERNEL-0000 §4–6 and §9 [Round08MergedDraft]; R9SRC-KERNEL-0001 §4 KCR-0001–0003 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | ClaimRecordInspection; OverclaimNegativeScenario | ClaimRecord; PublicClaimAudit |
| KCF-0004 | ProfileIdentification | `MUST` | A claim MUST identify an approved conformance Profile and applicability rules. | R9SRC-KERNEL-0000 §4–6 and §9 [Round08MergedDraft]; R9SRC-KERNEL-0001 §4 KCR-0001–0003 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0005 | RequirementApplicability | `MUST` | Every Profile requirement MUST be classified as Mandatory, ConditionalTriggered, ConditionalNotTriggered, ProhibitedBehavior or NotApplicableWithJustification. | R9SRC-KERNEL-0000 §4–6 and §9 [Round08MergedDraft]; R9SRC-KERNEL-0001 §4 KCR-0001–0003 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0006 | MandatoryCoverage | `MUST` | Every Mandatory and triggered Conditional requirement MUST have current evidence and test results. | R9SRC-KERNEL-0000 §4–6 and §9 [Round08MergedDraft]; R9SRC-KERNEL-0001 §4 KCR-0001–0003 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0007 | ProhibitionCoverage | `MUST` | Every prohibited behavior MUST have negative or adversarial coverage. | R9SRC-KERNEL-0000 §4–6 and §9 [Round08MergedDraft]; R9SRC-KERNEL-0001 §4 KCR-0001–0003 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0008 | ConditionalTrigger | `MUST` | A conditional requirement MUST record trigger evidence and decision owner. | R9SRC-KERNEL-0000 §4–6 and §9 [Round08MergedDraft]; R9SRC-KERNEL-0001 §4 KCR-0001–0003 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0009 | NotApplicableJustification | `MUST` | NotApplicableWithJustification MUST identify scope, evidence, reviewer, expiry and change consequences. | R9SRC-KERNEL-0000 §4–6 and §9 [Round08MergedDraft]; R9SRC-KERNEL-0001 §4 KCR-0001–0003 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0010 | SourceStatusVisibility | `MUST` | Draft, Proposed and Candidate source status MUST remain visible in assessment and public wording. | R9SRC-KERNEL-0000 §4–6 and §9 [Round08MergedDraft]; R9SRC-KERNEL-0001 §4 KCR-0001–0003 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0011 | EvidenceSnapshot | `MUST` | An assessment MUST freeze an evidence snapshot with identities, dates, owners, access controls and integrity metadata. | R9SRC-KERNEL-0000 §5, §8–9 [Round08MergedDraft]; R9SRC-MOS-0000 §7, §12–17 [DraftStandardsProcess]; R9SRC-KERNEL-0001 §4 KCR-0035–0036 [Round08MergedDraft] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | EvidenceTraceInspection; StaleOrMissingEvidenceScenario | EvidenceSnapshot; TestExecutionTrace |
| KCF-0012 | EvidenceFreshness | `MUST` | Evidence MUST have a review or expiry condition appropriate to the requirement and context. | R9SRC-KERNEL-0000 §5, §8–9 [Round08MergedDraft]; R9SRC-MOS-0000 §7, §12–17 [DraftStandardsProcess]; R9SRC-KERNEL-0001 §4 KCR-0035–0036 [Round08MergedDraft] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | EvidenceTraceInspection; StaleOrMissingEvidenceScenario | EvidenceSnapshot; TestExecutionTrace |
| KCF-0013 | VerificationMatch | `MUST` | Evidence MUST correspond to an allowed verification method or record an approved alternative. | R9SRC-KERNEL-0000 §5, §8–9 [Round08MergedDraft]; R9SRC-MOS-0000 §7, §12–17 [DraftStandardsProcess]; R9SRC-KERNEL-0001 §4 KCR-0035–0036 [Round08MergedDraft] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0014 | TestTraceability | `MUST` | Each assessed requirement MUST map to governed test specifications. | R9SRC-KERNEL-0000 §5, §8–9 [Round08MergedDraft]; R9SRC-MOS-0000 §7, §12–17 [DraftStandardsProcess]; R9SRC-KERNEL-0001 §4 KCR-0035–0036 [Round08MergedDraft] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | EvidenceTraceInspection; StaleOrMissingEvidenceScenario | EvidenceSnapshot; TestExecutionTrace |
| KCF-0015 | ExecutionTraceability | `MUST` | Each test execution MUST identify test version, implementation version, environment, data class, executor, result and evidence. | R9SRC-KERNEL-0000 §5, §8–9 [Round08MergedDraft]; R9SRC-MOS-0000 §7, §12–17 [DraftStandardsProcess]; R9SRC-KERNEL-0001 §4 KCR-0035–0036 [Round08MergedDraft] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0016 | ResultIdentity | `MUST` | Pass, Fail, Blocked, Inconclusive, NotApplicable, Invalidated and Expired MUST remain distinct. | R9SRC-KERNEL-0000 §5, §8–9 [Round08MergedDraft]; R9SRC-MOS-0000 §7, §12–17 [DraftStandardsProcess]; R9SRC-KERNEL-0001 §4 KCR-0035–0036 [Round08MergedDraft] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0017 | SpecNotExecution | `MUST NOT` | A test specification, validator, checklist or passing repository workflow MUST NOT be represented as executed product evidence. | R9SRC-KERNEL-0000 §5, §8–9 [Round08MergedDraft]; R9SRC-MOS-0000 §7, §12–17 [DraftStandardsProcess]; R9SRC-KERNEL-0001 §4 KCR-0035–0036 [Round08MergedDraft] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0018 | RepositoryNotProduct | `MUST NOT` | Repository integrity MUST NOT be represented as product, service, professional or organizational conformance. | R9SRC-KERNEL-0000 §5, §8–9 [Round08MergedDraft]; R9SRC-MOS-0000 §7, §12–17 [DraftStandardsProcess]; R9SRC-KERNEL-0001 §4 KCR-0035–0036 [Round08MergedDraft] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0019 | ReviewClassCoverage | `MUST` | An assessment MUST identify completed, incomplete and deferred review classes. | R9SRC-KERNEL-0001 §4 KCR-0010, KCR-0020, KCR-0025 and KCR-0032–0035 [Round08MergedDraft]; R9SRC-KERNEL-0002 §4 KDO-0016, KDO-0021 and KDO-0026–0030 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4 KLS-0009–0013 and KLS-0021–0031 [Round08MergedDraft]; R9SRC-MOS-0000 §6–7 and §13–31 [DraftStandardsProcess] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | ReviewRecordInspection; ConflictOrDissentScenario | ReviewRecord; ConflictAndDissentRegister |
| KCF-0020 | AffectedPersonReview | `MUST` | Requirements materially affecting people MUST identify applicable affected-person review and unresolved limitations. | R9SRC-KERNEL-0001 §4 KCR-0010, KCR-0020, KCR-0025 and KCR-0032–0035 [Round08MergedDraft]; R9SRC-KERNEL-0002 §4 KDO-0016, KDO-0021 and KDO-0026–0030 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4 KLS-0009–0013 and KLS-0021–0031 [Round08MergedDraft]; R9SRC-MOS-0000 §6–7 and §13–31 [DraftStandardsProcess] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | ReviewRecordInspection; ConflictOrDissentScenario | ReviewRecord; ConflictAndDissentRegister |
| KCF-0021 | HumanAccountability | `MUST` | High-impact evidence and decisions MUST identify a human and organization with actual authority, information and stop capacity. | R9SRC-KERNEL-0001 §4 KCR-0010, KCR-0020, KCR-0025 and KCR-0032–0035 [Round08MergedDraft]; R9SRC-KERNEL-0002 §4 KDO-0016, KDO-0021 and KDO-0026–0030 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4 KLS-0009–0013 and KLS-0021–0031 [Round08MergedDraft]; R9SRC-MOS-0000 §6–7 and §13–31 [DraftStandardsProcess] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | ReviewRecordInspection; ConflictOrDissentScenario | ReviewRecord; ConflictAndDissentRegister |
| KCF-0022 | IndependentReview | `SHOULD` | High-impact or conflict-prone claims SHOULD receive independent or conflict-free review. | R9SRC-KERNEL-0001 §4 KCR-0010, KCR-0020, KCR-0025 and KCR-0032–0035 [Round08MergedDraft]; R9SRC-KERNEL-0002 §4 KDO-0016, KDO-0021 and KDO-0026–0030 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4 KLS-0009–0013 and KLS-0021–0031 [Round08MergedDraft]; R9SRC-MOS-0000 §6–7 and §13–31 [DraftStandardsProcess] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | ReviewRecordInspection; ConflictOrDissentScenario | ReviewRecord; ConflictAndDissentRegister |
| KCF-0023 | ConflictDisclosure | `MUST` | Commercial, authorship, operational and reviewer conflicts MUST be recorded and mitigated. | R9SRC-KERNEL-0001 §4 KCR-0010, KCR-0020, KCR-0025 and KCR-0032–0035 [Round08MergedDraft]; R9SRC-KERNEL-0002 §4 KDO-0016, KDO-0021 and KDO-0026–0030 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4 KLS-0009–0013 and KLS-0021–0031 [Round08MergedDraft]; R9SRC-MOS-0000 §6–7 and §13–31 [DraftStandardsProcess] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | ReviewRecordInspection; ConflictOrDissentScenario | ReviewRecord; ConflictAndDissentRegister |
| KCF-0024 | MinorityAndDissent | `MUST` | Minority findings, counterexamples and unresolved dissent MUST remain traceable. | R9SRC-KERNEL-0001 §4 KCR-0010, KCR-0020, KCR-0025 and KCR-0032–0035 [Round08MergedDraft]; R9SRC-KERNEL-0002 §4 KDO-0016, KDO-0021 and KDO-0026–0030 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4 KLS-0009–0013 and KLS-0021–0031 [Round08MergedDraft]; R9SRC-MOS-0000 §6–7 and §13–31 [DraftStandardsProcess] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | ReviewRecordInspection; ConflictOrDissentScenario | ReviewRecord; ConflictAndDissentRegister |
| KCF-0025 | IncidentHistory | `MUST` | Relevant incidents, near misses, false positives, false negatives and remediation status MUST be included. | R9SRC-KERNEL-0001 §4 KCR-0010, KCR-0020, KCR-0025 and KCR-0032–0035 [Round08MergedDraft]; R9SRC-KERNEL-0002 §4 KDO-0016, KDO-0021 and KDO-0026–0030 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4 KLS-0009–0013 and KLS-0021–0031 [Round08MergedDraft]; R9SRC-MOS-0000 §6–7 and §13–31 [DraftStandardsProcess] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0026 | FailureCoverage | `MUST` | Assessment evidence MUST include failures and counterexamples, not only successful demonstrations. | R9SRC-KERNEL-0001 §4 KCR-0010, KCR-0020, KCR-0025 and KCR-0032–0035 [Round08MergedDraft]; R9SRC-KERNEL-0002 §4 KDO-0016, KDO-0021 and KDO-0026–0030 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4 KLS-0009–0013 and KLS-0021–0031 [Round08MergedDraft]; R9SRC-MOS-0000 §6–7 and §13–31 [DraftStandardsProcess] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0027 | ExceptionRecord | `MUST` | Every exception MUST identify requirement, authority, scope, reason, evidence, safeguards, owner, review/expiry and appeal. | R9SRC-KERNEL-0001 §4 KCR-0010, KCR-0020, KCR-0025 and KCR-0032–0035 [Round08MergedDraft]; R9SRC-KERNEL-0002 §4 KDO-0016, KDO-0021 and KDO-0026–0030 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4 KLS-0009–0013 and KLS-0021–0031 [Round08MergedDraft]; R9SRC-MOS-0000 §6–7 and §13–31 [DraftStandardsProcess] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | GovernanceStateInspection; ExpiredOrOverbroadExceptionScenario | ExceptionRecord; SuspensionOrRevocationDecision |
| KCF-0028 | NonWaivableBoundary | `MUST NOT` | An exception MUST NOT waive source integrity, honest capability claims, affected-person dignity, hidden-coercion prohibitions or the no-premature-claim boundary. | R9SRC-KERNEL-0001 §4 KCR-0010, KCR-0020, KCR-0025 and KCR-0032–0035 [Round08MergedDraft]; R9SRC-KERNEL-0002 §4 KDO-0016, KDO-0021 and KDO-0026–0030 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4 KLS-0009–0013 and KLS-0021–0031 [Round08MergedDraft]; R9SRC-MOS-0000 §6–7 and §13–31 [DraftStandardsProcess] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0029 | ExceptionExpiry | `MUST` | Expired, revoked or out-of-scope exceptions MUST stop authorizing assessment or operation. | R9SRC-KERNEL-0001 §4 KCR-0010, KCR-0020, KCR-0025 and KCR-0032–0035 [Round08MergedDraft]; R9SRC-KERNEL-0002 §4 KDO-0016, KDO-0021 and KDO-0026–0030 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4 KLS-0009–0013 and KLS-0021–0031 [Round08MergedDraft]; R9SRC-MOS-0000 §6–7 and §13–31 [DraftStandardsProcess] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | GovernanceStateInspection; ExpiredOrOverbroadExceptionScenario | ExceptionRecord; SuspensionOrRevocationDecision |
| KCF-0030 | Remediation | `MUST` | A failed material requirement MUST have containment, remediation, owner, target state and re-test conditions. | R9SRC-KERNEL-0001 §4 KCR-0010, KCR-0020, KCR-0025 and KCR-0032–0035 [Round08MergedDraft]; R9SRC-KERNEL-0002 §4 KDO-0016, KDO-0021 and KDO-0026–0030 [Round08MergedDraft]; R9SRC-KERNEL-0003 §4 KLS-0009–0013 and KLS-0021–0031 [Round08MergedDraft]; R9SRC-MOS-0000 §6–7 and §13–31 [DraftStandardsProcess] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0031 | Suspension | `MUST` | Credible serious harm, deceptive claims, evidence loss or material scope change MUST support immediate claim suspension. | R9SRC-KERNEL-0001 §4 KCR-0023, KCR-0025, KCR-0030 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary]; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | GovernanceStateInspection; ExpiredOrOverbroadExceptionScenario | ExceptionRecord; SuspensionOrRevocationDecision |
| KCF-0032 | Revocation | `MUST` | A claim MUST be revocable when evidence is invalid, scope is misrepresented, review is compromised or remediation fails. | R9SRC-KERNEL-0001 §4 KCR-0023, KCR-0025, KCR-0030 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary]; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | GovernanceStateInspection; ExpiredOrOverbroadExceptionScenario | ExceptionRecord; SuspensionOrRevocationDecision |
| KCF-0033 | ClaimExpiry | `MUST` | Every claim MUST carry expiry or mandatory re-review conditions. | R9SRC-KERNEL-0001 §4 KCR-0023, KCR-0025, KCR-0030 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary]; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | ClaimRecordInspection; OverclaimNegativeScenario | ClaimRecord; PublicClaimAudit |
| KCF-0034 | ChangeInvalidation | `MUST` | Material changes to requirements, implementation, model, data flow, service availability, staffing or jurisdiction MUST invalidate or narrow affected evidence. | R9SRC-KERNEL-0001 §4 KCR-0023, KCR-0025, KCR-0030 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary]; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0035 | Migration | `MUST` | A new family or Profile version MUST define claim migration, coexistence and public supersession. | R9SRC-KERNEL-0001 §4 KCR-0023, KCR-0025, KCR-0030 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary]; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0036 | PublicClaimExactness | `MUST` | Public wording MUST identify boundary, Profile, family version, assessment state, evidence date, expiry and limitations. | R9SRC-KERNEL-0001 §4 KCR-0023, KCR-0025, KCR-0030 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary]; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | ClaimRecordInspection; OverclaimNegativeScenario | ClaimRecord; PublicClaimAudit |
| KCF-0037 | ScopeNoSpillover | `MUST NOT` | Evidence for one boundary, domain, language, jurisdiction or population MUST NOT silently support another. | R9SRC-KERNEL-0001 §4 KCR-0023, KCR-0025, KCR-0030 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary]; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | ClaimRecordInspection; OverclaimNegativeScenario | ClaimRecord; PublicClaimAudit |
| KCF-0038 | NoComponentInheritance | `MUST NOT` | A conforming component MUST NOT make its host product or organization conforming by inheritance. | R9SRC-KERNEL-0001 §4 KCR-0023, KCR-0025, KCR-0030 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary]; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0039 | NoPrematureClaim | `MUST NOT` | No conforming, certified, approved or equivalent claim may be made while governing documents are Draft or evidence/review is incomplete. | R9SRC-KERNEL-0001 §4 KCR-0023, KCR-0025, KCR-0030 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary]; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | ClaimRecordInspection; OverclaimNegativeScenario | ClaimRecord; PublicClaimAudit |
| KCF-0040 | NoBadgeWithoutAuthority | `MUST NOT` | No badge, seal or mark implying MingOS approval may be used without a separately accepted governance decision. | R9SRC-KERNEL-0001 §4 KCR-0023, KCR-0025, KCR-0030 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary]; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | ClaimRecordInspection; OverclaimNegativeScenario | ClaimRecord; PublicClaimAudit |
| KCF-0041 | ContinuousReassessment | `MUST` | Operational claims MUST define monitoring, incident intake, correction, suspension and periodic reassessment. | R9SRC-KERNEL-0001 §4 KCR-0023, KCR-0025, KCR-0030 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary]; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | AssessmentRecordInspection; BoundaryOrFailureScenario | AssessmentRecord; ReviewFinding |
| KCF-0042 | EvidenceProtection | `MUST` | Assessment evidence MUST be minimized, purpose-limited, access-controlled, retention-governed and protected from unrelated training or marketing use. | R9SRC-KERNEL-0001 §4 KCR-0023, KCR-0025, KCR-0030 and KCR-0036 [Round08MergedDraft]; R9SRC-REF-0028 §1–7 [DraftConformanceBoundary]; R9SRC-RFC-0005 §2–10 [ProposedPublicClaimProtocol] | `NewConformanceProposalDerivedFromDraftKernelAndProcess` | EvidenceTraceInspection; StaleOrMissingEvidenceScenario | EvidenceSnapshot; TestExecutionTrace |

## 4. Applicability model

```text
Mandatory
ConditionalTriggered
ConditionalNotTriggered
ProhibitedBehavior
NotApplicableWithJustification
```

NotApplicable requires evidence, reviewer and expiry.

## 5. Evidence classes

| ID | Class | Meaning | Limitation |
|---|---|---|---|
| KEC-01 | StructuralStatic | Repository, schema, configuration and source inspection | Does not prove runtime or human outcomes |
| KEC-02 | SyntheticScenario | Synthetic positive, negative and counterexample execution | No real-person acceptance claim |
| KEC-03 | ControlledImplementation | Bounded implementation test | Not broad production evidence |
| KEC-04 | OperationalTrace | Governed runtime, incident or service evidence | Requires privacy and freshness review |
| KEC-05 | AffectedPersonReview | Voluntary affected-person usability and impact evidence | Cannot be replaced by internal opinion |
| KEC-06 | DomainProfessionalReview | Qualified domain review | Does not imply affected-person or legal acceptance |
| KEC-07 | IndependentAssurance | Conflict-free independent review | Scope and independence explicit |
| KEC-08 | LongitudinalIncident | Longitudinal outcomes, failures and remediation | Requires time and confounder limits |

Evidence classes are complementary, not maturity levels.

## 6. Assessment states

```text
NotAssessed
AssessmentPlanned
EvidenceCollection
ReviewPending
EvidenceIncomplete
MeetsSpecifiedProfile
DoesNotMeet
Suspended
Expired
Withdrawn
```

## 7. Review, exception and public-claim boundary

Review classes: Architecture, AgencyEthics, PrivacyConsent, Safety, AffectedPerson, Accessibility, DomainProfessional, JurisdictionLegal, Security, Implementation, CommercialConflict, Translation. Completion of one class does not imply another. Exceptions cannot waive source integrity, honest capability claims, dignity, hidden-coercion prohibitions or no-premature-claim boundaries.

Allowed now: “under internal review against Draft Kernel documents” or “implements selected Draft concepts,” with exact limitations. Prohibited now: “MingOS Kernel conforming,” “certified,” “approved,” “Charter compliant,” badges or equivalent.

## 8. Human agency, privacy and safety

Conformance evidence MUST preserve affected-person refusal, correction, appeal,
accessibility, minority views and human accountability. Evidence collection is
purpose-limited, minimized, access-controlled and retention-governed. A serious
harm signal, failed handoff, deceptive claim or compromised review can suspend
the assessment before a final decision.

## 9. Limitations and version history

Profile governance, assessor independence, evidence freshness, jurisdiction, public marks and affected-person review remain open.

| Version | Date | Change | Status |
|---|---|---|---|
| 0.1.0-draft.1 | 2026-07-15 | Initial 42-requirement conformance and evidence model | Draft |

```text
Assessments: 0
Conforming implementations: 0
Badges: 0
Overall: NoCurrentKernelConformanceClaim
```
