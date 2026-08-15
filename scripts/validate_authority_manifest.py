#!/usr/bin/env python3
"""Validate the authority manifest as a consumable, non-self-promoting contract."""

from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "governance/registries/AUTHORITY_MANIFEST.json"
ADR = ROOT / "governance/decisions/ADR-0029-three-class-authority-model-and-canonical-bridge.md"

REQUIRED_TOP_KEYS = {
    "schema_version",
    "manifest_id",
    "shared_compass_contract",
    "title",
    "status",
    "canonical_repository",
    "governing_record",
    "audit_evidence",
    "reviewed_against_commit",
    "purpose",
    "canonical_bridge",
    "forbidden_upgrade",
    "authority_classes",
    "authority_items",
    "semantic_compatibility_contract",
    "current_state_reference",
    "non_claims",
    "evidence_gate",
}

CLASSES = {"hard_invariant", "adaptive_default", "product_owned_choice"}
APPLICABILITY = {
    "trigger_gated",
    "always_applicable_boundary",
    "ordinary_interaction_default",
    "product_decision",
}
ITEM_KEYS = {
    "key",
    "class",
    "owner",
    "applicability",
    "trigger_evidence",
    "permitted_downstream_effect",
    "forbidden_authority_upgrade",
    "test_expectation",
}


def frontmatter_status(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8-sig")
    match = re.search(r"^status:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def main() -> int:
    errors: list[str] = []
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))

    missing = REQUIRED_TOP_KEYS - set(data)
    if missing:
        errors.append(f"missing top-level keys: {sorted(missing)}")

    commit = data.get("reviewed_against_commit", "")
    if not (len(commit) == 40 and all(c in "0123456789abcdef" for c in commit)):
        errors.append("reviewed_against_commit must be a 40-char lowercase hex SHA")

    classes = data.get("authority_classes", [])
    if not isinstance(classes, list) or set(classes) != CLASSES or len(classes) != len(CLASSES):
        errors.append(f"authority_classes must contain exactly {sorted(CLASSES)}")

    items = data.get("authority_items", [])
    if not isinstance(items, list) or not items:
        errors.append("authority_items must be a non-empty list")
        items = []

    seen: set[str] = set()
    represented: set[str] = set()
    for index, item in enumerate(items):
        label = item.get("key", f"item[{index}]") if isinstance(item, dict) else f"item[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{label}: item must be an object")
            continue
        missing_item = ITEM_KEYS - set(item)
        if missing_item:
            errors.append(f"{label}: missing keys {sorted(missing_item)}")
        key = item.get("key")
        if not isinstance(key, str) or not key:
            errors.append(f"{label}: key must be a non-empty string")
        elif key in seen:
            errors.append(f"{label}: duplicate key")
        else:
            seen.add(key)
        cls = item.get("class")
        if cls not in CLASSES:
            errors.append(f"{label}: invalid class {cls!r}")
        else:
            represented.add(cls)
        if item.get("applicability") not in APPLICABILITY:
            errors.append(f"{label}: invalid applicability {item.get('applicability')!r}")
        for field in (
            "owner",
            "trigger_evidence",
            "permitted_downstream_effect",
            "forbidden_authority_upgrade",
            "test_expectation",
        ):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"{label}: {field} must be non-empty text")

    if represented != CLASSES:
        errors.append("authority_items must represent all three authority classes")

    bridge = data.get("canonical_bridge", {})
    for key in ("foundation", "mingos", "products"):
        if not isinstance(bridge.get(key), str) or not bridge[key].strip():
            errors.append(f"canonical_bridge missing {key}")

    contract = data.get("semantic_compatibility_contract", {})
    for key in ("foundation", "mingos", "product"):
        if not isinstance(contract.get(key), list) or not contract[key]:
            errors.append(f"semantic compatibility requires non-empty {key} list")
    if contract.get("no_shared_sha_requirement") is not True:
        errors.append("semantic compatibility must explicitly reject shared-SHA coupling")

    state_ref = data.get("current_state_reference", {})
    state_path = state_ref.get("document") if isinstance(state_ref, dict) else None
    if not isinstance(state_path, str) or not state_path:
        errors.append("current_state_reference.document is required")
    elif not (ROOT / state_path).exists():
        errors.append(f"current_state_reference does not exist: {state_path}")

    for evidence_id in data.get("audit_evidence", []):
        if not isinstance(evidence_id, str) or not evidence_id:
            errors.append("audit_evidence entries must be non-empty strings")

    gate = data.get("evidence_gate", {})
    if gate.get("conformance") is not False:
        errors.append("evidence_gate.conformance must be false")
    if gate.get("promotion_requires_explicit_decision") is not True:
        errors.append("promotion_requires_explicit_decision must be true")

    # The validator checks status consistency; it does not promote policy.
    adr_status = frontmatter_status(ADR)
    manifest_status = str(data.get("status", ""))
    if adr_status != "Accepted" and manifest_status.lower().startswith("accepted"):
        errors.append(
            "manifest must not claim Accepted while governing ADR is not Accepted"
        )

    if errors:
        print("Authority-manifest validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        "Authority-manifest validation passed: structured per-item contract, "
        "status consistency, references, semantic compatibility, and non-conformance gate verified."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
