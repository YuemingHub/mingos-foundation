#!/usr/bin/env python3
"""Validate central document-ID reservations against the integrated tree."""

from __future__ import annotations

from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "governance/registries/DOCUMENT_ID_RESERVATIONS.json"
EXPECTED_REPOSITORY = "YuemingHub/mingos-foundation"
OPEN_STATES = {
    "PlannedReservation",
    "ReservedForOpenDraftPR",
    "ReadyForSerialIntegration",
    "ExpiredOnMainChange",
}
ALLOWED_STATES = OPEN_STATES | {"Integrated", "Released"}
POST_REVIEW_TRANSITION_PATHS = {
    "governance/registries/DOCUMENT_ID_RESERVATIONS.json",
    "scripts/validate_id_reservations.py",
}


def git_output(*args: str) -> str | None:
    try:
        return subprocess.check_output(
            ["git", *args],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except subprocess.CalledProcessError:
        return None


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


def current_branch() -> str | None:
    return git_output("rev-parse", "--abbrev-ref", "HEAD")


def current_main_commit() -> str | None:
    for ref in ("origin/main", "main"):
        commit = git_output("rev-parse", "--verify", ref)
        if commit:
            return commit
    return None


def is_ancestor(ancestor: str, descendant: str = "HEAD") -> bool:
    try:
        subprocess.run(
            ["git", "merge-base", "--is-ancestor", ancestor, descendant],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def changed_paths_since(commit: str) -> set[str]:
    output = git_output("diff", "--name-only", f"{commit}..HEAD")
    if not output:
        return set()
    return {line.strip() for line in output.splitlines() if line.strip()}


def valid_commit(value: object) -> bool:
    return isinstance(value, str) and len(value) == 40 and all(
        character in "0123456789abcdef" for character in value.lower()
    )


def main() -> int:
    errors: list[str] = []
    data = json.loads(REGISTRY.read_text(encoding="utf-8-sig"))
    if data.get("canonical_repository") != EXPECTED_REPOSITORY:
        errors.append("canonical repository mismatch")
    if data.get("governing_record") != "GOV-0113":
        errors.append("governing record mismatch")

    registry_review = data.get("reviewed_against_commit")
    if not valid_commit(registry_review):
        errors.append("registry review commit invalid")
    elif not is_ancestor(registry_review):
        errors.append("registry review commit is not an ancestor of the checked tree")

    current_main = current_main_commit()

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

    branch = current_branch()
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

        state = reservation.get("state")
        if state not in ALLOWED_STATES:
            errors.append(f"{name} uses undefined reservation state {state}")

        reservation_review = reservation.get("reviewed_against_commit")
        if not valid_commit(reservation_review):
            errors.append(f"{name} reviewed-against commit invalid")
        elif not is_ancestor(reservation_review):
            errors.append(f"{name} reviewed-against commit is not an ancestor of the checked tree")

        expires_on_main_change = reservation.get("expires_on_main_change")
        if not isinstance(expires_on_main_change, bool):
            errors.append(f"{name} expires_on_main_change must be boolean")
        elif state in {"Integrated", "Released"} and expires_on_main_change:
            errors.append(f"{name} integrated/released reservation cannot expire on future main changes")
        elif (
            current_main
            and valid_commit(reservation_review)
            and state in OPEN_STATES
            and expires_on_main_change
            and reservation_review != current_main
            and state != "ExpiredOnMainChange"
        ):
            errors.append(
                f"{name} must be ExpiredOnMainChange because main advanced from "
                f"{reservation_review} to {current_main}"
            )
        elif state == "ExpiredOnMainChange" and (
            not expires_on_main_change or reservation_review == current_main
        ):
            errors.append(f"{name} ExpiredOnMainChange state has no matching main-change condition")

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
            reserved_paths = reservation.get("reserved_paths", {})
            expected_path = reserved_paths.get(doc_id)
            if state in OPEN_STATES:
                if branch == "main" and doc_id in occupied:
                    errors.append(f"open reservation {doc_id} already occupied on main")
                elif branch != "main" and state != "ExpiredOnMainChange" and expected_path and occupied.get(doc_id) != expected_path:
                    errors.append(f"open reservation {doc_id} missing or misplaced on {branch}")
            if state == "Integrated":
                if doc_id not in occupied:
                    errors.append(f"integrated reservation {doc_id} missing from repository")
                elif expected_path and occupied.get(doc_id) != expected_path:
                    errors.append(f"integrated reservation {doc_id} path mismatch")

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
        if pr12.get("state") not in OPEN_STATES | {"Integrated"}:
            errors.append(
                "PR #12 must remain in a defined open state before merge "
                "or become Integrated after merge"
            )

        source = pr12.get("source", {})
        reviewed_head = source.get("head_commit_at_review")
        if not valid_commit(reviewed_head):
            errors.append("PR #12 reviewed head invalid")
        elif not is_ancestor(reviewed_head):
            errors.append("PR #12 reviewed head is not an ancestor of the checked tree")
        else:
            pr12_paths = set(pr12.get("reserved_paths", {}).values())
            changed = changed_paths_since(reviewed_head)
            unexpected = (changed & pr12_paths) - POST_REVIEW_TRANSITION_PATHS
            if unexpected:
                errors.append(
                    "PR #12 has substantive changes after reviewed head: "
                    + ", ".join(sorted(unexpected))
                )

        if source.get("branch_name") != "docs/round-09-kernel-conformance-test-collection":
            errors.append("PR #12 branch name mismatch")
        if pr12.get("state") == "ReadyForSerialIntegration":
            evidence = pr12.get("integration_evidence") or {}
            if evidence.get("base_commit") != pr12.get("reviewed_against_commit"):
                errors.append("PR #12 readiness evidence base mismatch")
            if evidence.get("reviewed_head") != reviewed_head:
                errors.append("PR #12 readiness evidence head mismatch")
            if evidence.get("repository_validation") != "success":
                errors.append("PR #12 repository validation evidence missing")
            if evidence.get("validate_repository") != "success":
                errors.append("PR #12 validate-repository evidence missing")

    expected_paths = {
        "REF-0035": "reference/REF-0035-restricted-nomination-and-cp2-preauthorization-guide.md",
        "KERNEL-0002": "standards/kernel/KERNEL-0002-canonical-object-data-model.md",
        "KERNEL-0003": "standards/kernel/KERNEL-0003-lifecycle-state-machines.md",
        "REF-0040": "reference/kernel/REF-0040-kernel-object-catalog-crosswalk.md",
        "KERNEL-0004": "standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md",
        "KERNEL-0005": "standards/kernel/KERNEL-0005-test-specifications-derived-indexes.md",
        "REF-0044": "reference/kernel/REF-0044-round08-object-lifecycle-review-protocol.md",
        "REF-0045": "reference/kernel/REF-0045-kernel-conformance-claim-applicability-matrix.md",
        "REF-0046": "reference/kernel/REF-0046-kernel-evidence-assurance-class-matrix.md",
        "REF-0047": "reference/kernel/REF-0047-kernel-requirement-test-catalog-crosswalk.md",
        "REF-0048": "reference/kernel/REF-0048-kernel-exception-suspension-expiry-revocation-matrix.md",
        "REF-0049": "reference/kernel/REF-0049-kernel-implementation-assessment-protocol.md",
        "REF-0050": "reference/kernel/REF-0050-kernel-conformance-test-ambiguity-register.md",
        "REF-0051": "reference/kernel/REF-0051-kernel-public-claim-mark-language-matrix.md",
    }
    for doc_id, path in expected_paths.items():
        if occupied.get(doc_id) != path:
            errors.append(f"path mismatch for {doc_id}: expected {path}, found {occupied.get(doc_id)}")
    for doc_id in ["REF-0035", "KERNEL-0002", "KERNEL-0003", "REF-0040", "REF-0044"]:
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
    expected_summary = {
        "active_reservations": sum(
            1 for reservation in reservations if reservation.get("state") in OPEN_STATES
        ),
        "reserved_ids": sum(
            len(reservation.get("reserved_ids", []))
            for reservation in reservations
            if reservation.get("state") in OPEN_STATES
        ),
        "integrated_by_this_registry": sum(
            len(reservation.get("reserved_ids", []))
            for reservation in reservations
            if reservation.get("state") == "Integrated"
        ),
        "released_reservations": sum(
            1 for reservation in reservations if reservation.get("state") == "Released"
        ),
    }
    for key, expected in expected_summary.items():
        if summary.get(key) != expected:
            errors.append(
                f"reservation summary mismatch for {key}: "
                f"expected {expected}, found {summary.get(key)}"
            )

    if errors:
        print("Document-ID reservation validation failed:")
        for error in errors:
            print(" -", error)
        return 1

    print(
        "Document-ID reservation validation passed: "
        f"{expected_summary['active_reservations']} active reservations, "
        f"{expected_summary['reserved_ids']} reserved IDs, "
        f"{expected_summary['integrated_by_this_registry']} integrated IDs, "
        "review-baseline ancestry, open-reservation expiry semantics, reviewed-head ancestry, "
        "occupied paths, and non-binding next-ID hints verified."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())