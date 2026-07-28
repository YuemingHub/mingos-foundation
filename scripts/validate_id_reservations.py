#!/usr/bin/env python3
"""Validate central document-ID reservations against the integrated tree."""

from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "governance/registries/DOCUMENT_ID_RESERVATIONS.json"
EXPECTED_REPOSITORY = "YuemingHub/Ming-Foundation"
EXPECTED_REVIEW_COMMIT = "29485e67279d11401bb0f9f2b9afc78f0bdf67f4"
OPEN_STATES = {
    "PlannedReservation",
    "ReservedForOpenDraftPR",
    "ReadyForSerialIntegration",
    "ExpiredOnMainChange",
}


def frontmatter_id(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8-sig")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    for line in text[4:end].splitlines():
        if line.startswith("id:"):
            return line.split(":", 1)[1].strip()
    return None


def main() -> int:
    errors: list[str] = []
    data = json.loads(REGISTRY.read_text(encoding="utf-8-sig"))
    if data.get("canonical_repository") != EXPECTED_REPOSITORY:
        errors.append("canonical repository mismatch")
    if data.get("governing_record") != "GOV-0113":
        errors.append("governing record mismatch")
    if data.get("reviewed_against_commit") != EXPECTED_REVIEW_COMMIT:
        errors.append("registry review commit mismatch")

    occupied: dict[str, str] = {}
    duplicates: list[str] = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        doc_id = frontmatter_id(path)
        if not doc_id:
            continue
        relative = str(path.relative_to(ROOT)).replace("\\", "/")
        if doc_id in occupied:
            duplicates.append(doc_id)
        occupied[doc_id] = relative
    if duplicates:
        errors.append("duplicate governed IDs: " + ", ".join(sorted(set(duplicates))))

    reservation_ids: set[str] = set()
    reservation_names: set[str] = set()
    reservations = data.get("reservations", [])
    for reservation in reservations:
        required = [
            "reservation_id",
            "workstream",
            "owner",
            "source",
            "state",
            "reserved_ids",
            "created_at",
            "reviewed_against_commit",
            "expires_on_main_change",
        ]
        for key in required:
            if key not in reservation:
                errors.append(f"{reservation.get('reservation_id', 'unknown')} missing {key}")
        name = reservation.get("reservation_id")
        if name in reservation_names:
            errors.append(f"duplicate reservation ID {name}")
        reservation_names.add(name)
        if reservation.get("reviewed_against_commit") != data.get("reviewed_against_commit"):
            errors.append(f"{name} reviewed-against mismatch")
        source = reservation.get("source", {})
        if (
            not source.get("pull_request")
            and not source.get("branch_name")
            and not source.get("governing_record")
        ):
            errors.append(f"{name} missing source PR, branch, or governing record")
        for doc_id in reservation.get("reserved_ids", []):
            if doc_id in reservation_ids:
                errors.append(f"ID {doc_id} reserved more than once")
            reservation_ids.add(doc_id)
            state = reservation.get("state")
            if state in OPEN_STATES and doc_id in occupied:
                errors.append(f"open reservation {doc_id} already occupied by {occupied[doc_id]}")
            if state == "Integrated" and doc_id not in occupied:
                errors.append(f"integrated reservation {doc_id} missing from repository")

    expected_pr12 = {
        "KERNEL-0004",
        "KERNEL-0005",
        "REF-0045",
        "REF-0046",
        "REF-0047",
        "REF-0048",
        "REF-0049",
        "REF-0050",
        "REF-0051",
    }
    pr12 = next(
        (r for r in reservations if r.get("source", {}).get("pull_request") == 12),
        None,
    )
    if pr12 is None:
        errors.append("PR #12 reservation missing")
    else:
        if set(pr12.get("reserved_ids", [])) != expected_pr12:
            errors.append("PR #12 reserved-ID set mismatch")
        if pr12.get("state") != "ReservedForOpenDraftPR":
            errors.append("PR #12 must remain ReservedForOpenDraftPR")
        if (
            pr12.get("source", {}).get("head_commit_at_review")
            != "614da9d1a5c8cb151b7da06158c2074406802e18"
        ):
            errors.append("PR #12 reviewed head mismatch")

    expected_paths = {
        "REF-0035": "reference/REF-0035-restricted-nomination-and-cp2-preauthorization-guide.md",
        "KERNEL-0002": "standards/kernel/KERNEL-0002-canonical-object-data-model.md",
        "KERNEL-0003": "standards/kernel/KERNEL-0003-lifecycle-state-machines.md",
        "REF-0040": "reference/kernel/REF-0040-kernel-object-catalog-crosswalk.md",
        "REF-0044": "reference/kernel/REF-0044-round08-object-lifecycle-review-protocol.md",
    }
    for doc_id, path in expected_paths.items():
        if occupied.get(doc_id) != path:
            errors.append(f"occupied assertion mismatch for {doc_id}")
        if doc_id in reservation_ids:
            errors.append(f"occupied ID {doc_id} cannot be reserved")

    hints = data.get("next_unreserved_hint", {})
    for family in ["GOV", "ADR", "REF", "GOV-TPL", "KERNEL"]:
        hint = hints.get(family)
        if not hint:
            errors.append(f"missing next hint {family}")
        elif hint in occupied or hint in reservation_ids:
            errors.append(f"next hint {hint} is already occupied or reserved")
    if hints.get("binding") is not False:
        errors.append("next-number hints must be non-binding")

    summary = data.get("summary", {})
    if summary.get("active_reservations") != 1 or summary.get("reserved_ids") != 9:
        errors.append("reservation summary mismatch")

    if errors:
        print("Document-ID reservation validation failed:")
        for error in errors:
            print(" -", error)
        return 1

    print(
        "Document-ID reservation validation passed: one active PR reservation, "
        "nine unique reserved IDs, REF-0035 protected as occupied, "
        "KERNEL-0002/0003 and REF-0040/0044 integrated, and non-binding "
        "next-ID hints remain free."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
