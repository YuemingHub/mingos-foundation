\
#!/usr/bin/env python3
"""Validate the currently integrated MingOS Kernel Draft family."""

from __future__ import annotations

from pathlib import Path
import json
import re

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


def main() -> int:
    errors: list[str] = []
    docs = {
        "KERNEL-0000": ("KERNEL-0000-specification-family-index.md", "0.4.0-draft.4"),
        "KERNEL-0001": ("KERNEL-0001-core-operational-contract.md", "0.2.2-draft.4"),
        "KERNEL-0002": ("KERNEL-0002-canonical-object-data-model.md", "0.2.0-draft.2"),
        "KERNEL-0003": ("KERNEL-0003-lifecycle-state-machines.md", "0.2.0-draft.2"),
    }
    for doc_id, (name, version) in docs.items():
        path = ROOT / "standards/kernel" / name
        if not path.exists():
            errors.append("missing " + doc_id)
            continue
        metadata = fm(path.read_text(encoding="utf-8-sig"))
        if metadata.get("id") != doc_id or metadata.get("status") != "Draft" or metadata.get("version") != version:
            errors.append(doc_id + " metadata")

    for doc_id in ["KERNEL-0004", "KERNEL-0005"]:
        if list((ROOT / "standards/kernel").glob(doc_id + "-*.md")):
            errors.append(doc_id + " exists on integration-repair main")

    model = json.loads((ROOT / "reference/kernel/mingos-kernel-object-lifecycle-model.json").read_text(encoding="utf-8-sig"))
    if model.get("schema") != "mingos.kernel-object-lifecycle-model.v0.2":
        errors.append("object/lifecycle schema")

    pairs = [
        (ROOT / "standards/kernel/KERNEL-0002-canonical-object-data-model.md", "object_requirements", "KDO-"),
        (ROOT / "standards/kernel/KERNEL-0003-lifecycle-state-machines.md", "lifecycle_requirements", "KLS-"),
    ]
    for path, key, prefix in pairs:
        markdown_rows = rows(path, prefix, 8)
        json_rows = model[key]
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
    if [item[0] for item in object_rows] != [item["id"] for item in model["object_types"]]:
        errors.append("object IDs")

    for state_machine in model["state_machines"]:
        states = set(state_machine["states"])
        seen: set[tuple[str, str]] = set()
        for start, end in state_machine["transitions"]:
            if start not in states or end not in states or start == end or (start, end) in seen:
                errors.append(state_machine["id"] + " transition")
            seen.add((start, end))

    for flow in model["process_flows"]:
        expected = [[start, end] for start, end in zip(flow["stages"], flow["stages"][1:])]
        if flow["transitions"] != expected:
            errors.append(flow["id"] + " flow")

    core = json.loads((ROOT / "reference/kernel/mingos-kernel-core-requirements.json").read_text(encoding="utf-8-sig"))
    if core["family"]["id"] != "kernel-family/0.4.0-draft.4":
        errors.append("kernel family version")
    if core["family"]["reserved_not_created"] != ["KERNEL-0004", "KERNEL-0005"]:
        errors.append("kernel family reserved IDs")
    if model["review"]["state"] != "PreparedNotExecuted":
        errors.append("review boundary")
    if model["conformance"]["current_claim"] != "NoCurrentKernelConformanceClaim":
        errors.append("conformance boundary")

    state_text = (ROOT / "governance/status/GOV-0001-current-canonical-state.md").read_text(encoding="utf-8-sig")
    state_meta = fm(state_text)
    stage_match = re.search(r"^- \*\*Current repository stage:\*\* (.+)$", state_text, re.MULTILINE)
    version_match = re.search(r"^- \*\*Current repository version:\*\* `([^`]+)`$", state_text, re.MULTILINE)
    readme = (ROOT / "README.md").read_text(encoding="utf-8-sig")
    if not stage_match or not version_match:
        errors.append("canonical state metadata")
    else:
        stage = stage_match.group(1)
        version = version_match.group(1)
        if state_meta.get("version") != version:
            errors.append("canonical version mismatch")
        if stage not in readme or version not in readme:
            errors.append("README/canonical-state mismatch")

    if errors:
        print("Kernel family validation failed:")
        for error in errors:
            print(" -", error)
        return 1

    print(
        "Kernel family validation passed: KERNEL-0000 through KERNEL-0003 remain Draft; "
        "35 objects, 36 KDO, 34 KLS, 17 object state machines, 9 process flows; "
        "KERNEL-0004/0005 absent; no Kernel conformance claim; canonical state and README agree."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
