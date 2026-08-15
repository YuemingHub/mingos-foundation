#!/usr/bin/env python3
"""Validate the integrated MingOS Kernel Draft family including Round09."""

from __future__ import annotations

from pathlib import Path
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {"MUST", "MUST NOT", "SHOULD", "SHOULD NOT", "MAY"}


def fm(text: str) -> dict[str, str]:
    text = text.lstrip("\ufeff")
    end = text.find("\n---\n", 4)
    out: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = value.strip()
    return out


def rows(path: Path, prefix: str, count: int) -> list[list[str]]:
    out: list[list[str]] = []
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("| " + prefix):
            cells = [item.strip() for item in line.strip().strip("|").split("|")]
            if len(cells) != count:
                raise ValueError(f"{path} malformed {prefix}")
            out.append(cells)
    return out


def render_ref(ref: dict, baseline: dict[str, dict]) -> str:
    if "baseline_ref" in ref:
        b = baseline[ref["baseline_ref"]]
        return f"{ref['baseline_ref']} {ref['locator']} [{b['source_role']}]"
    return (
        f"{ref['source_id']} / {ref['status']} / {ref['version']} / "
        f"`{ref['path']}` / {ref['locator']} / {ref['source_role']}"
    )


def check_req_table(
    path: Path,
    prefix: str,
    items: list[dict],
    baseline: dict[str, dict],
    errors: list[str],
) -> None:
    try:
        mr = rows(path, prefix, 8)
    except ValueError as exc:
        errors.append(str(exc))
        return
    if len(mr) != len(items):
        errors.append(prefix + " count")
        return
    for markdown, machine in zip(mr, items):
        rid, domain, level, text, sources, treatment, methods, evidence = markdown
        expected_sources = "; ".join(render_ref(x, baseline) for x in machine.get("source_refs", []))
        matches = (
            rid == machine.get("id")
            and domain == machine.get("domain")
            and level.strip("`") == machine.get("level")
            and text == machine.get("text")
            and sources == expected_sources
            and treatment.strip("`") == machine.get("source_treatment")
            and methods == "; ".join(machine.get("verification_methods", []))
            and evidence == "; ".join(machine.get("evidence_types", []))
        )
        if not matches:
            errors.append(machine["id"] + " semantic sync")
        if machine.get("level") not in ALLOWED:
            errors.append(machine["id"] + " level")
        if not machine.get("source_refs") or not machine.get("verification_methods") or not machine.get("evidence_types"):
            errors.append(machine["id"] + " traceability")


def main() -> int:
    errors: list[str] = []

    # Round08 + Round09 document metadata
    docs = {
        "KERNEL-0000": ("KERNEL-0000-specification-family-index.md", "0.5.0-draft.5"),
        "KERNEL-0001": ("KERNEL-0001-core-operational-contract.md", "0.2.3-draft.5"),
        "KERNEL-0002": ("KERNEL-0002-canonical-object-data-model.md", "0.2.0-draft.2"),
        "KERNEL-0003": ("KERNEL-0003-lifecycle-state-machines.md", "0.2.0-draft.2"),
        "KERNEL-0004": ("KERNEL-0004-conformance-requirements-evidence-model.md", "0.1.0-draft.1"),
        "KERNEL-0005": ("KERNEL-0005-test-specifications-derived-indexes.md", "0.1.0-draft.1"),
    }
    for doc_id, (name, version) in docs.items():
        path = ROOT / "standards/kernel" / name
        if not path.exists():
            errors.append("missing " + doc_id)
            continue
        metadata = fm(path.read_text(encoding="utf-8-sig"))
        if metadata.get("id") != doc_id or metadata.get("status") != "Draft" or metadata.get("version") != version:
            errors.append(doc_id + " metadata")

    # Round09 conformance / test schema and tables
    conformance_model_path = ROOT / "reference/kernel/mingos-kernel-conformance-model.json"
    test_specifications_path = ROOT / "reference/kernel/mingos-kernel-test-specifications.json"
    core_requirements_path = ROOT / "reference/kernel/mingos-kernel-core-requirements.json"
    object_model_path = ROOT / "reference/kernel/mingos-kernel-object-lifecycle-model.json"

    conformance = json.loads(conformance_model_path.read_text(encoding="utf-8-sig"))
    tests = json.loads(test_specifications_path.read_text(encoding="utf-8-sig"))
    if conformance.get("schema") != "mingos.kernel-conformance-model.v0.1":
        errors.append("conformance schema")
    if tests.get("schema") != "mingos.kernel-test-specifications.v0.1":
        errors.append("test schema")

    check_req_table(
        ROOT / "standards/kernel/KERNEL-0004-conformance-requirements-evidence-model.md",
        "KCF-",
        conformance["requirements"],
        conformance["source_baseline"],
        errors,
    )
    check_req_table(
        ROOT / "standards/kernel/KERNEL-0005-test-specifications-derived-indexes.md",
        "KTG-",
        tests["governance_requirements"],
        tests["source_baseline"],
        errors,
    )

    base = conformance.get("decision_base_commit")
    if tests.get("decision_base_commit") != base:
        errors.append("source base mismatch")
    for ref, blob_info in conformance.get("source_baseline", {}).items():
        path = ROOT / blob_info["path"]
        if not path.exists():
            errors.append(ref + " path")
            continue
        try:
            actual_blob = subprocess.check_output(
                ["git", "rev-parse", f"{base}:{blob_info['path']}"],
                cwd=ROOT,
                text=True,
            ).strip()
        except subprocess.CalledProcessError:
            errors.append(ref + " unresolved")
            continue
        if actual_blob != blob_info.get("blob_sha"):
            errors.append(ref + " blob")
    if conformance.get("source_baseline") != tests.get("source_baseline"):
        errors.append("source baseline indexes differ")

    core = json.loads(core_requirements_path.read_text(encoding="utf-8-sig"))
    object_model = json.loads(object_model_path.read_text(encoding="utf-8-sig"))
    expected_test_order = (
        [x["id"] for x in core["requirements"]]
        + [x["id"] for x in object_model["object_requirements"]]
        + [x["id"] for x in object_model["lifecycle_requirements"]]
    )
    if [x["requirement_id"] for x in tests["tests"]] != expected_test_order:
        errors.append("test coverage/order")
    if len({x["id"] for x in tests["tests"]}) != len(tests["tests"]):
        errors.append("duplicate test")
    if any(x["execution_status"] != "NotExecuted" for x in tests["tests"]):
        errors.append("execution claim")
    if conformance["current_authorization"] != {
        "profile_count": 0,
        "assessment_count": 0,
        "claim_count": 0,
        "badge_count": 0,
        "current_claim": "NoCurrentKernelConformanceClaim",
    }:
        errors.append("authorization")
    if tests["execution_summary"]["executed_count"] != 0 or tests["execution_summary"]["pass_count"] != 0:
        errors.append("execution summary")

    # Round08 object / lifecycle structure
    pairs = [
        (
            ROOT / "standards/kernel/KERNEL-0002-canonical-object-data-model.md",
            "object_requirements",
            "KDO-",
        ),
        (
            ROOT / "standards/kernel/KERNEL-0003-lifecycle-state-machines.md",
            "lifecycle_requirements",
            "KLS-",
        ),
    ]
    for path, key, prefix in pairs:
        markdown_rows = rows(path, prefix, 8)
        json_rows = object_model[key]
        if len(markdown_rows) != len(json_rows):
            errors.append(key + " count")
            continue
        for markdown, machine in zip(markdown_rows, json_rows):
            source = machine["source_refs"][0]
            expected_source = (
                f"{source['source_id']} / {source['status']} / {source['version']} / "
                f"`{source['path']}` / {source['locator']} / {source['baseline_type']}"
            )
            matches = (
                markdown[0] == machine["id"]
                and markdown[1] == machine["domain"]
                and markdown[2].strip("`") == machine["level"]
                and markdown[3] == machine["text"]
                and markdown[4] == expected_source
                and markdown[5].strip("`") == machine["source_treatment"]
                and markdown[6] == "; ".join(machine["verification_methods"])
                and markdown[7] == "; ".join(machine["evidence_types"])
            )
            if not matches:
                errors.append(machine["id"] + " sync")
            if machine["level"] not in ALLOWED:
                errors.append(machine["id"] + " level")

    object_rows = rows(ROOT / "standards/kernel/KERNEL-0002-canonical-object-data-model.md", "KOT-", 7)
    if [item[0] for item in object_rows] != [item["id"] for item in object_model["object_types"]]:
        errors.append("object IDs")

    for state_machine in object_model["state_machines"]:
        states = set(state_machine["states"])
        seen: set[tuple[str, str]] = set()
        for start, end in state_machine["transitions"]:
            if start not in states or end not in states or start == end or (start, end) in seen:
                errors.append(state_machine["id"] + " transition")
            seen.add((start, end))

    for flow in object_model["process_flows"]:
        expected = [[start, end] for start, end in zip(flow["stages"], flow["stages"][1:])]
        if flow["transitions"] != expected:
            errors.append(flow["id"] + " flow")

    # Family / claim boundaries
    if [x["id"] for x in core["family"]["documents"]] != [
        "KERNEL-0000",
        "KERNEL-0001",
        "KERNEL-0002",
        "KERNEL-0003",
        "KERNEL-0004",
        "KERNEL-0005",
    ]:
        errors.append("family docs")
    if core["family"]["reserved_not_created"] != []:
        errors.append("reserved docs")
    if core["conformance"]["current_claim"] != "NoCurrentKernelConformanceClaim":
        errors.append("claim")

    state_text = (ROOT / "governance/status/GOV-0001-current-canonical-state.md").read_text(encoding="utf-8-sig")
    stage_match = re.search(r"^- \*\*Current repository stage:\*\* (.+)$", state_text, re.MULTILINE)
    version_match = re.search(r"^- \*\*Current repository version:\*\* `([^`]+)`$", state_text, re.MULTILINE)
    readme = (ROOT / "README.md").read_text(encoding="utf-8-sig")
    if not stage_match or not version_match:
        errors.append("canonical state metadata")
    else:
        stage = stage_match.group(1)
        version = version_match.group(1)
        if "Reality Rebase" not in stage or "Evidence-Led" not in stage:
            errors.append("reality-rebase stage boundary")
        if version not in {"1.0.0-alpha.19"}:
            errors.append("version boundary")
        if stage not in readme or version not in readme:
            errors.append("README/canonical-state mismatch")

    if errors:
        print("Kernel family validation failed:")
        for error in errors:
            print(" -", error)
        return 1

    print(
        "Kernel family validation passed: KERNEL-0000 through KERNEL-0005 remain Draft; "
        "35 objects, 36 KDO, 34 KLS, 17 object state machines, 9 process flows; "
        "42 KCF, 32 KTG, 106 NotExecuted tests, 24 scenarios, exact source blobs, zero claims."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
