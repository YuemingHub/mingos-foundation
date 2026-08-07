#!/usr/bin/env python3
"""Prevent canonical repository governance from being blocked by external systems."""

from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "governance/reviews/GOV-0027-day7-audit-scope-correction.md": [
        "YuemingHub/Ming-Foundation",
        "External implementation evidence",
        "not prerequisites",
    ],
    "governance/decisions/ADR-0009-canonical-repository-audit-scope.md": [
        "Canonical repository audit",
        "External implementation-conformance validation",
        "explicit user scope",
    ],
    "governance/status/GOV-0001-current-canonical-state.md": [
        "https://github.com/YuemingHub/mingos-foundation",
        "external implementation evidence",
        "do not enter another repository without explicit user instruction",
    ],
}

FORBIDDEN_IN_CANONICAL_NEXT_WORK = [
    "register the current website and Family OS repositories and revisions",
    "private website repository access",
    "current website and Family OS repositories",
]


def main() -> int:
    errors: list[str] = []

    for rel, markers in REQUIRED.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing required scope file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                errors.append(f"{rel}: missing marker {marker!r}")

    gov1_path = ROOT / "governance/status/GOV-0001-current-canonical-state.md"
    if gov1_path.exists():
        gov1 = gov1_path.read_text(encoding="utf-8")
        next_work = gov1.split("## 9. Next canonical work", 1)[-1]
        for phrase in FORBIDDEN_IN_CANONICAL_NEXT_WORK:
            if phrase in next_work:
                errors.append(
                    "GOV-0001 next work incorrectly makes external implementation "
                    f"a canonical prerequisite: {phrase!r}"
                )

    adr8 = ROOT / "governance/decisions/ADR-0008-treat-day7-as-bounded-audit.md"
    if adr8.exists() and "status: Superseded" not in adr8.read_text(encoding="utf-8"):
        errors.append("ADR-0008 must remain Superseded")

    adr9 = ROOT / "governance/decisions/ADR-0009-canonical-repository-audit-scope.md"
    if adr9.exists() and "status: Accepted" not in adr9.read_text(encoding="utf-8"):
        errors.append("ADR-0009 must remain Accepted")

    backlog_path = ROOT / "governance/remediation/backlog/DAY7_REMEDIATION_BACKLOG.json"
    if not backlog_path.exists():
        errors.append("missing scoped Day 7 backlog")
    else:
        data = json.loads(backlog_path.read_text(encoding="utf-8"))
        if data.get("canonical_repository") != "YuemingHub/mingos-foundation":
            errors.append("backlog canonical_repository is incorrect")
        if data.get("canonical_repository_audit") != "accepted":
            errors.append("canonical repository audit must remain accepted")
        for item in data.get("external_implementation_evidence_targets", []):
            if not item.get("non_blocking_for_canonical_repository"):
                errors.append(
                    f"{item.get('id')}: external evidence target is not marked non-blocking"
                )

    if errors:
        print("Audit-scope validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print("Audit-scope validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
