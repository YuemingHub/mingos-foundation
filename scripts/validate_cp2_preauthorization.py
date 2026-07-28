#!/usr/bin/env python3
"""Validate Day 18 conditional CP2 pre-authorization without activation."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def main():
    errors = []

    matrix = load("standards/review/CP2_PROTOCOL_APPLICABILITY_MATRIX.json")
    if matrix["overall_state"] != "ApplicabilityDefinedApprovalsOutstanding":
        errors.append("protocol applicability state mismatch")
    if len(matrix["protocols"]) != 7:
        errors.append("expected seven protocol applicability rows")
    if matrix["summary"] != {
        "protocols": 7,
        "required_or_adapted": 6,
        "not_applicable": 1,
        "approved_for_cp2_human_use": 0,
    }:
        errors.append("protocol applicability summary mismatch")
    if sum(item["approval_state"] == "NotApplicable" for item in matrix["protocols"]) != 1:
        errors.append("expected exactly one not-applicable protocol")
    if any(
        item["approval_state"] not in {"NotApproved", "NotApplicable"}
        for item in matrix["protocols"]
    ):
        errors.append("no CP2 human-use protocol may be approved")

    environment = load("standards/review/CP2_MINIMUM_ENVIRONMENT_CONTROL_SET.json")
    if environment["overall_state"] != "MinimumSetDefinedNotDeployed":
        errors.append("CP2 environment state mismatch")
    if len(environment["controls"]) != 8:
        errors.append("expected eight CP2 environment controls")
    for item in environment["controls"]:
        if item["deployment_state"] != "NotStarted":
            errors.append(f"{item['control_id']}: deployment must remain NotStarted")
        if item["verification_state"] != "NotVerified":
            errors.append(f"{item['control_id']}: verification must remain NotVerified")
        if item["named_owner_ref"] is not None:
            errors.append(f"{item['control_id']}: fabricated named owner")
        if item["verification_evidence_refs"] != []:
            errors.append(f"{item['control_id']}: fabricated verification evidence")

    decision = load("standards/review/CP2_PREAUTHORIZATION_DECISION.json")
    expected_provenance = {
        "package_origin_commit": "394f494f00ebfccf38572e3846cf6b6e3f699abf",
        "integration_base_commit": "a0b8234567c211896085f0e1259b96bcb53effd1",
        "feature_commit": "39b536e01a152de7597a6a86b95669e1814ade20",
        "merge_commit": "f3905710db2304ab926c4ab31e10264931539f98",
        "reviewed_against_current_main": "29485e67279d11401bb0f9f2b9afc78f0bdf67f4",
    }
    if decision.get("source_repository_commit_role") != "PackageOriginCommit":
        errors.append("pre-authorization source-commit role mismatch")
    if decision.get("integration_provenance") != expected_provenance:
        errors.append("pre-authorization integration provenance mismatch")
    if decision["decision_state"] != "ConditionallyApprovedNotEffective":
        errors.append("pre-authorization decision state mismatch")
    if decision["effective"] is not False:
        errors.append("pre-authorization must remain ineffective")
    if decision["cp2_authorization_state"] != "Blocked":
        errors.append("actual CP2 authorization must remain Blocked")
    if decision["cp2_execution_state"] != "NotExecuted":
        errors.append("CP2 execution must remain NotExecuted")
    if len(decision["conditions_precedent"]) < 12:
        errors.append("insufficient pre-authorization conditions")

    scenarios = load("standards/review/CP2_PREAUTHORIZATION_TABLETOP_SCENARIOS.json")
    results = load("standards/review/CP2_PREAUTHORIZATION_TABLETOP_RESULTS.json")
    if len(scenarios["scenarios"]) != 12 or len(results["results"]) != 12:
        errors.append("expected twelve scenarios and results")
    scenario_ids = {item["scenario_id"] for item in scenarios["scenarios"]}
    if scenario_ids != {item["scenario_id"] for item in results["results"]}:
        errors.append("scenario/result coverage mismatch")
    for item in scenarios["scenarios"]:
        if item["contains_real_person_data"] is not False:
            errors.append(f"{item['scenario_id']}: real-person data not allowed")
        if item["contains_sensitive_case_data"] is not False:
            errors.append(f"{item['scenario_id']}: real case data not allowed")
    for item in results["results"]:
        if item["result"] != "Pass":
            errors.append(f"{item['scenario_id']}: expected Pass")
        if item["synthetic_only"] is not True or item["real_evidence_detected"] is not False:
            errors.append(f"{item['scenario_id']}: synthetic boundary mismatch")
    if results["summary"] != {
        "executed": 12,
        "passed": 12,
        "failed": 0,
        "stopped": 0,
        "real_evidence_detected": 0,
    }:
        errors.append("pre-authorization tabletop summary mismatch")
    for key in [
        "real_nominations", "human_staff_rehearsals", "participants_recruited",
        "participant_sessions", "participant_evidence_records"
    ]:
        if results[key] != 0:
            errors.append(f"{key} must remain zero")

    gate = load("standards/review/DAY18_CP2_PREAUTHORIZATION_GATE.json")
    if gate.get("source_repository_commit_role") != "PackageOriginCommit":
        errors.append("Day18 gate source-commit role mismatch")
    if gate.get("integration_provenance") != expected_provenance:
        errors.append("Day18 gate integration provenance mismatch")
    if gate["overall_state"] != "RestrictedNominationInfrastructureReadyCP2PreauthorizationInactive":
        errors.append("Day18 gate state mismatch")
    if gate["summary"] != {"gate_items": 18, "pass": 11, "blocked": 7, "fail": 0}:
        errors.append("Day18 gate summary mismatch")
    if gate["cp2_preauthorization_recorded"] is not True:
        errors.append("pre-authorization must be recorded")
    for key in [
        "cp2_preauthorization_effective", "cp2_authorized", "cp2_executed",
        "cp3_authorized", "recruitment_authorized", "participant_evidence_exists"
    ]:
        if gate[key] is not False:
            errors.append(f"Day18 gate {key} must remain false")

    pilot = load("standards/review/CONTROLLED_PILOT_AUTHORIZATION.json")
    states = {
        item["class_id"]: (item["authorization_state"], item["execution_state"])
        for item in pilot["classes"]
    }
    if states != {
        "CP0": ("Authorized", "Complete"),
        "CP1": ("Authorized", "Complete"),
        "CP2": ("Blocked", "NotExecuted"),
        "CP3": ("Blocked", "NotExecuted"),
    }:
        errors.append("controlled-pilot authorization states changed")
    if pilot["human_review_authorized"] is not False:
        errors.append("human review must remain unauthorized")

    activation = load("standards/review/REVIEW_OPERATIONAL_ACTIVATION.json")
    if activation["activation_state"] != "SyntheticPilotOnly":
        errors.append("operational activation must remain SyntheticPilotOnly")
    if activation["human_review_activation_state"] != "NotActivated":
        errors.append("human review activation must remain NotActivated")
    if activation["summary"]["roles_assigned"] != 0:
        errors.append("assigned roles must remain zero")
    if activation["summary"]["approvals_completed"] != 0:
        errors.append("completed approvals must remain zero")
    if activation["summary"]["environment_controls_ready"] != 0:
        errors.append("ready live controls must remain zero")

    affected = load("standards/review/AFFECTED_PERSON_REVIEW_PLAN.json")
    if affected["execution_state"] != "PreparedNotExecuted":
        errors.append("affected-person review state changed")
    for key in ["participants_recruited", "sessions_completed", "results_recorded"]:
        if affected["summary"][key] != 0:
            errors.append(f"affected-person {key} must remain zero")

    baseline = load("standards/conformance/FOUNDATION_CONFORMANCE_BASELINE.json")
    if baseline["results"] != []:
        errors.append("implementation conformance baseline must remain empty")
    d18 = baseline["day18_restricted_nomination_and_cp2_preauthorization"]
    if d18["real_nominations"] != 0:
        errors.append("baseline real nominations must remain zero")
    if d18["cp2_preauthorization_effective"] is not False:
        errors.append("baseline pre-authorization must remain ineffective")
    if d18["cp2_authorized"] is not False or d18["cp2_executed"] is not False:
        errors.append("baseline CP2 must remain blocked and unexecuted")
    if d18["implementation_tests_executed"] != 0:
        errors.append("implementation tests executed must remain zero")

    ambiguities = load("standards/review/RFC_AMBIGUITIES.json")
    if len(ambiguities["ambiguities"]) != 19 or any(
        item["status"] != "Open" for item in ambiguities["ambiguities"]
    ):
        errors.append("all nineteen ambiguities must remain Open")

    dissent = load("standards/review/RFC_DISSENT_REGISTER.json")
    if len(dissent["items"]) != 8 or any(item["status"] != "Open" for item in dissent["items"]):
        errors.append("all eight dissent items must remain Open")

    tests = load("standards/requirements/RFC_ACCEPTANCE_TESTS.json")
    if len(tests["tests"]) != 115 or any(
        item["test_state"] != "SpecificationOnly" for item in tests["tests"]
    ):
        errors.append("115 implementation tests must remain unexecuted specifications")

    if errors:
        print("CP2 pre-authorization validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "CP2 pre-authorization validation passed. Validated seven protocol "
        "rows with zero approvals, eight not-started controls, an ineffective "
        "conditional decision, twelve passed synthetic scenarios, an 18-item "
        "gate (11 Pass, 7 Blocked), CP0/CP1 complete, CP2/CP3 blocked, zero "
        "nominations and human activity, 19 open ambiguities, 8 open dissent "
        "items, 115 unexecuted implementation-test specifications, and an "
        "empty implementation-conformance baseline."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
