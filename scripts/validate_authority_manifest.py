#!/usr/bin/env python3
"""Validate the machine-readable authority manifest against ADR-0029."""

from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "governance/registries/AUTHORITY_MANIFEST.json"

REQUIRED_TOP_KEYS = {
    "schema_version",
    "manifest_id",
    "title",
    "status",
    "canonical_repository",
    "governing_record",
    "audit_evidence",
    "reviewed_against_commit",
    "purpose",
    "canonical_bridge",
    "forbidden_upgrade",
    "no_action_is_legal",
    "cp2_authorization_state",
    "cp2_execution_state",
    "cp2_default_queue",
    "classes",
    "semantic_compatibility_contract",
    "non_claims",
    "evidence_gate",
}

CLASSES = {"hard_invariant", "adaptive_default", "product_owned_choice"}
OWNERS = {"Foundation", "MingOS", "downstream product"}


def load(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))

    missing = REQUIRED_TOP_KEYS - set(data)
    if missing:
        errors.append(f"missing top-level keys: {sorted(missing)}")

    if data.get("canonical_repository") != "YuemingHub/mingos-foundation":
        errors.append("canonical repository mismatch")
    if data.get("governing_record") != "ADR-0029":
        errors.append("governing record mismatch")

    commit = data.get("reviewed_against_commit", "")
    if not (len(commit) == 40 and all(c in "0123456789abcdef" for c in commit)):
        errors.append("reviewed_against_commit must be a 40-char hex SHA")

    classes = data.get("classes", {})
    if set(classes) != CLASSES:
        errors.append(f"classes must be exactly {sorted(CLASSES)}")

    expected_owner = {"hard_invariant": "Foundation", "adaptive_default": "MingOS",
                      "product_owned_choice": "downstream product"}
    for cls in CLASSES:
        entry = classes.get(cls, {})
        if entry.get("owner") != expected_owner[cls]:
            errors.append(f"{cls}: owner must be {expected_owner[cls]!r}")
        if not isinstance(entry.get("items"), list) or not entry["items"]:
            errors.append(f"{cls}: items must be a non-empty list")
        if "binding" not in entry or "non_negotiable" not in entry:
            errors.append(f"{cls}: missing binding or non_negotiable")

    if not classes.get("hard_invariant", {}).get("non_negotiable"):
        errors.append("hard_invariant must be non_negotiable")
    if classes.get("adaptive_default", {}).get("non_negotiable"):
        errors.append("adaptive_default must not be non_negotiable")
    if classes.get("product_owned_choice", {}).get("non_negotiable"):
        errors.append("product_owned_choice must not be non_negotiable")

    if data.get("no_action_is_legal") is not True:
        errors.append("no_action_is_legal must be true")
    if data.get("cp2_authorization_state") != "Blocked":
        errors.append("cp2_authorization_state must remain Blocked")
    if data.get("cp2_execution_state") != "NotExecuted":
        errors.append("cp2_execution_state must remain NotExecuted")
    if data.get("cp2_default_queue") is not False:
        errors.append("cp2_default_queue must be false")

    bridge = data.get("canonical_bridge", {})
    for key in ("foundation", "mingos", "products"):
        if not bridge.get(key):
            errors.append(f"canonical_bridge missing {key}")

    contract = data.get("semantic_compatibility_contract", {})
    for key in ("foundation", "mingos", "product"):
        if not isinstance(contract.get(key), list):
            errors.append(f"semantic compatibility missing {key} list")

    non_claims = data.get("non_claims", [])
    required_claims = {
        "Foundation conformance",
        "Family-Space general effectiveness",
        "CP2 authorization",
    }
    for claim in required_claims:
        if claim not in non_claims:
            errors.append(f"non_claim must include {claim!r}")

    gate = data.get("evidence_gate", {})
    if gate.get("conformance") is not False:
        errors.append("evidence_gate.conformance must be false")

    if errors:
        print("Authority-manifest validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "Authority-manifest validation passed. Three classes, canonical "
        "bridge, semantic compatibility contract, and non-claims verified."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
