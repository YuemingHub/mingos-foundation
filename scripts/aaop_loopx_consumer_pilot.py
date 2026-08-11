#!/usr/bin/env python3
"""Real-repository AAOP <-> LoopX execution-continuity pilot.

This file is intentionally experiment-only. It must never become Foundation
policy or governance authority. The bounded consumer task is executed on a
dedicated branch and uses LoopX only for execution continuity beneath AAOP.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

GOAL_ID = "aaop-loopx-foundation-pilot"
BUILDER_ID = "aaop-pilot-builder"
REVIEWER_ID = "aaop-pilot-reviewer"
MARKER_REL = Path("experiments/aaop-loopx-pilot/runtime-marker.txt")
RECEIPT_REL = Path("experiments/aaop-loopx-pilot/pilot-receipt.json")
AUTHORITY_FILES = (
    Path("README.md"),
    Path("foundation/charter/MF-0004-life-charter.md"),
    Path("governance/status/GOV-0001-current-canonical-state.md"),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(
    args: list[str],
    *,
    cwd: Path,
    env: dict[str, str],
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(
        args,
        cwd=cwd,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
    if check and completed.returncode != 0:
        raise AssertionError(
            f"command failed ({completed.returncode}): {' '.join(args)}\n"
            f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
        )
    return completed


def parse_json_output(result: subprocess.CompletedProcess[str], label: str) -> dict[str, Any]:
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise AssertionError(
            f"{label}: expected JSON output\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        ) from exc
    require(isinstance(payload, dict), f"{label}: expected JSON object")
    return payload


def loopx(
    root: Path,
    env: dict[str, str],
    registry: Path,
    runtime: Path,
    *args: str,
    check: bool = True,
) -> tuple[subprocess.CompletedProcess[str], dict[str, Any]]:
    result = run(
        [
            "loopx",
            "--registry",
            str(registry),
            "--runtime-root",
            str(runtime),
            "--format",
            "json",
            *args,
        ],
        cwd=root,
        env=env,
        check=check,
    )
    payload = parse_json_output(result, f"loopx {' '.join(args)}")
    return result, payload


def tracked_local_control_state(root: Path, env: dict[str, str]) -> list[str]:
    result = run(
        ["git", "ls-files", ".loopx", ".codex/goals", ".local"],
        cwd=root,
        env=env,
    )
    return [line for line in result.stdout.splitlines() if line.strip()]


def state_file(root: Path) -> Path:
    return root / ".codex" / "goals" / GOAL_ID / "ACTIVE_GOAL_STATE.md"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--aaop-revision", required=True)
    parser.add_argument("--loopx-revision", required=True)
    parser.add_argument("--loopx-version", required=True)
    args = parser.parse_args()

    root = Path.cwd().resolve()
    registry = root / ".loopx" / "registry.json"
    runtime = root / ".local" / "aaop-loopx-pilot-runtime"
    marker = root / MARKER_REL
    receipt_path = root / RECEIPT_REL

    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"

    # Pre-adoption gap: the consumer already has durable governance/project state,
    # and AAOP has Journey/blocker continuity, but no host-native provider-neutral
    # should-run / quiet / scheduler contract. A fresh execution host would need to
    # poll or infer whether an unchanged gate merits another model turn. This pilot
    # tests only that narrow execution-continuity delta.
    gap = {
        "class": "execution-continuity",
        "observable_failure": (
            "host-native AAOP can preserve blockers/next action but has no durable "
            "provider-neutral run|gate|wait|quiet decision for a fresh execution process"
        ),
        "must_improve": (
            "a fresh process must recover the bounded frontier and an unchanged "
            "human gate must return should_run=false without mutating/spending work"
        ),
    }

    authority_before = {str(path): sha256(root / path) for path in AUTHORITY_FILES}
    require(not tracked_local_control_state(root, env), "LoopX local state must not already be tracked")

    for ignored in (
        ".loopx/registry.json",
        ".codex/goals/example/ACTIVE_GOAL_STATE.md",
        ".local/aaop-loopx-pilot-runtime/example",
    ):
        result = run(["git", "check-ignore", "-q", "--no-index", ignored], cwd=root, env=env, check=False)
        require(result.returncode == 0, f"pilot local state path is not ignored: {ignored}")

    # Non-destructive project connect, first preview then apply. The goal is a
    # bounded execution outcome, not the Foundation mission or AAOP Journey.
    _, dry_connect = loopx(
        root,
        env,
        registry,
        runtime,
        "connect",
        "--project",
        ".",
        "--goal-id",
        GOAL_ID,
        "--objective",
        "Prove one bounded AAOP execution-continuity pilot without changing Foundation authority.",
        "--domain",
        "aaop-loopx-provider-pilot",
        "--no-onboarding-scan",
        "--codex-app-heartbeat",
        "no",
        "--write-scope",
        "experiments/aaop-loopx-pilot/**",
        "--dry-run",
    )
    require(dry_connect.get("ok") is True, f"connect dry-run failed: {dry_connect}")
    require(not registry.exists(), "connect dry-run must not create project registry")

    _, connected = loopx(
        root,
        env,
        registry,
        runtime,
        "connect",
        "--project",
        ".",
        "--goal-id",
        GOAL_ID,
        "--objective",
        "Prove one bounded AAOP execution-continuity pilot without changing Foundation authority.",
        "--domain",
        "aaop-loopx-provider-pilot",
        "--no-onboarding-scan",
        "--codex-app-heartbeat",
        "no",
        "--write-scope",
        "experiments/aaop-loopx-pilot/**",
    )
    require(connected.get("ok") is True, f"connect failed: {connected}")
    require(registry.is_file(), "connect must create project-local registry")
    require(state_file(root).is_file(), "connect must create active goal state")

    # Agent registration is explicit and previewed; no identity takeover.
    for agent_id in (BUILDER_ID, REVIEWER_ID):
        _, preview = loopx(
            root, env, registry, runtime,
            "register-agent", "--goal-id", GOAL_ID, "--agent-id", agent_id,
        )
        require(preview.get("ok") is True, f"register-agent preview failed: {preview}")
        _, applied = loopx(
            root, env, registry, runtime,
            "register-agent", "--goal-id", GOAL_ID, "--agent-id", agent_id, "--execute",
        )
        require(applied.get("ok") is True, f"register-agent apply failed: {applied}")

    task_text = "Create the bounded AAOP/LoopX pilot marker and validate the current Foundation branch."
    _, added = loopx(
        root, env, registry, runtime,
        "todo", "add", "--goal-id", GOAL_ID, "--role", "agent", "--text", task_text,
    )
    require(added.get("added") is True, f"pilot todo was not added: {added}")
    todo_id = str(added.get("todo_id"))
    require(todo_id.startswith("todo_"), f"unexpected todo id: {todo_id}")

    _, claim = loopx(
        root, env, registry, runtime,
        "todo", "claim", "--goal-id", GOAL_ID, "--todo-id", todo_id,
        "--claimed-by", BUILDER_ID, "--agent-id", BUILDER_ID,
    )
    require(claim.get("changed") is True, f"builder could not claim todo: {claim}")

    _, eligible = loopx(
        root, env, registry, runtime,
        "quota", "should-run", "--goal-id", GOAL_ID, "--agent-id", BUILDER_ID,
        "--runtime-profile", "generic_cli", "--available-capability", "shell",
        "--scan-path", ".",
    )
    require(eligible.get("should_run") is True, f"builder should be eligible before execution: {eligible}")

    # Negative validation path: a failed real validator does not trigger any
    # completion or quota-spend writeback. Read the durable state from disk.
    failed_validation = run(
        [sys.executable, "-c", "raise SystemExit(23)"],
        cwd=root,
        env=env,
        check=False,
    )
    require(failed_validation.returncode == 23, "negative validation fixture did not fail as intended")
    open_state = state_file(root).read_text(encoding="utf-8")
    require(todo_id in open_state and "status=open" in open_state, "failed validation must leave todo open")

    # Real bounded repository change + project-native validation.
    marker.parent.mkdir(parents=True, exist_ok=True)
    marker.write_text(
        "AAOP LoopX consumer pilot marker\n"
        f"aaop_revision={args.aaop_revision}\n"
        f"loopx_revision={args.loopx_revision}\n",
        encoding="utf-8",
    )
    require(marker.read_text(encoding="utf-8").startswith("AAOP LoopX consumer pilot marker"), "marker readback failed")
    validation = run([sys.executable, "scripts/validate_all.py"], cwd=root, env=env)

    _, completed = loopx(
        root, env, registry, runtime,
        "todo", "complete", "--goal-id", GOAL_ID, "--todo-id", todo_id,
        "--claimed-by", BUILDER_ID, "--agent-id", BUILDER_ID,
        "--evidence", "scripts/validate_all.py exit=0 and pilot marker readback passed",
        "--no-follow-up",
    )
    require(completed.get("changed") is True, f"validated todo did not complete: {completed}")
    _, refreshed = loopx(
        root, env, registry, runtime,
        "refresh-state", "--goal-id", GOAL_ID, "--no-global-sync",
    )
    require(refreshed.get("ok") is True, f"refresh-state failed: {refreshed}")

    # Spend only after validated durable writeback.
    _, spent = loopx(
        root, env, registry, runtime,
        "quota", "spend-slot", "--goal-id", GOAL_ID, "--agent-id", BUILDER_ID,
        "--slots", "1", "--source", "controller", "--execute", "--scan-path", ".",
    )
    require(spent.get("ok") is True, f"quota spend failed after validated writeback: {spent}")

    # Bounded handoff. The reviewer owns the review todo; the builder must not
    # silently take it over after the reviewer claim.
    review_text = "Review the bounded pilot marker and validation evidence without owning the AAOP Journey."
    _, review_added = loopx(
        root, env, registry, runtime,
        "todo", "add", "--goal-id", GOAL_ID, "--role", "agent", "--text", review_text,
    )
    review_todo_id = str(review_added.get("todo_id"))
    require(review_todo_id.startswith("todo_"), f"review todo missing: {review_added}")
    _, review_claim = loopx(
        root, env, registry, runtime,
        "todo", "claim", "--goal-id", GOAL_ID, "--todo-id", review_todo_id,
        "--claimed-by", REVIEWER_ID, "--agent-id", REVIEWER_ID,
    )
    require(review_claim.get("changed") is True, f"reviewer claim failed: {review_claim}")
    builder_takeover_result, builder_takeover = loopx(
        root, env, registry, runtime,
        "todo", "claim", "--goal-id", GOAL_ID, "--todo-id", review_todo_id,
        "--claimed-by", BUILDER_ID, "--agent-id", BUILDER_ID,
        check=False,
    )
    require(
        builder_takeover_result.returncode != 0 or builder_takeover.get("changed") is not True,
        "builder must not silently take over reviewer-owned todo",
    )
    _, review_complete = loopx(
        root, env, registry, runtime,
        "todo", "complete", "--goal-id", GOAL_ID, "--todo-id", review_todo_id,
        "--claimed-by", REVIEWER_ID, "--agent-id", REVIEWER_ID,
        "--evidence", "reviewer read marker and project-native validation result",
        "--no-follow-up",
    )
    require(review_complete.get("changed") is True, f"review completion failed: {review_complete}")

    # Genuine human-owned gate: this experimental branch must not be merged into
    # Foundation main by the execution provider. LoopX should make repeated
    # probes quiet instead of authorizing more model work.
    gate_text = "Human owner decides whether this experimental consumer branch may ever be merged into Foundation main."
    _, gate = loopx(
        root, env, registry, runtime,
        "todo", "add", "--goal-id", GOAL_ID, "--role", "user",
        "--task-class", "user_gate", "--global-gate", "--text", gate_text,
    )
    require(gate.get("added") is True, f"human gate was not recorded: {gate}")

    gate_state_before = sha256(state_file(root))
    _, quiet_one = loopx(
        root, env, registry, runtime,
        "quota", "should-run", "--goal-id", GOAL_ID, "--agent-id", BUILDER_ID,
        "--runtime-profile", "generic_cli", "--available-capability", "shell",
        "--scan-path", ".",
    )
    _, quiet_two = loopx(
        root, env, registry, runtime,
        "quota", "should-run", "--goal-id", GOAL_ID, "--agent-id", BUILDER_ID,
        "--runtime-profile", "generic_cli", "--available-capability", "shell",
        "--scan-path", ".",
    )
    gate_state_after = sha256(state_file(root))
    require(quiet_one.get("should_run") is False, f"human gate must stop model turn: {quiet_one}")
    require(quiet_two.get("should_run") is False, f"unchanged gate must remain quiet: {quiet_two}")
    require(gate_state_before == gate_state_after, "read-only quiet probes must not mutate durable state")

    # Fresh-process recovery: every CLI call is a separate process; explicitly
    # re-read status and todos after all prior Python-side state is irrelevant.
    _, fresh_status = loopx(root, env, registry, runtime, "status", "--scan-root", ".")
    require(fresh_status.get("ok") is True, f"fresh process status recovery failed: {fresh_status}")
    _, fresh_todos = loopx(root, env, registry, runtime, "todo", "list", "--goal-id", GOAL_ID)
    require(fresh_todos.get("ok") is True, f"fresh process todo recovery failed: {fresh_todos}")
    require(gate_text in json.dumps(fresh_todos, ensure_ascii=False), "fresh process lost human gate")

    authority_after = {str(path): sha256(root / path) for path in AUTHORITY_FILES}
    require(authority_before == authority_after, "LoopX pilot changed Foundation authority files")
    tracked_state = tracked_local_control_state(root, env)
    require(not tracked_state, f"private/local LoopX state became tracked: {tracked_state}")

    git_status = run(["git", "status", "--short"], cwd=root, env=env).stdout.splitlines()
    require(any(str(MARKER_REL) in line for line in git_status), "real pilot marker is not visible as a repository change")
    require(not any(".loopx/" in line or ".codex/goals/" in line or ".local/" in line for line in git_status), "local control state leaked into git status")

    # Rollback is previewed before execution. Archive/remove only this LoopX goal,
    # then prove the repository still validates without LoopX state.
    _, uninstall_preview = loopx(
        root, env, registry, runtime,
        "uninstall-project", "--goal-id", GOAL_ID, "--archive-state",
    )
    require(uninstall_preview.get("ok") is True and uninstall_preview.get("dry_run") is True, f"rollback preview failed: {uninstall_preview}")

    receipt: dict[str, Any] = {
        "schema_version": 1,
        "verdict": "closes-gap",
        "consumer": "YuemingHub/mingos-foundation",
        "branch": os.environ.get("GITHUB_HEAD_REF") or os.environ.get("GITHUB_REF_NAME") or "local",
        "aaop_revision": args.aaop_revision,
        "loopx_revision": args.loopx_revision,
        "loopx_version": args.loopx_version,
        "pre_adoption_gap": gap,
        "connect": {"dry_run": True, "applied": True, "non_destructive_authority": authority_before == authority_after},
        "real_delivery": {"path": str(MARKER_REL), "validation": "python scripts/validate_all.py", "exit_code": validation.returncode},
        "negative_validation": {"exit_code": failed_validation.returncode, "todo_remained_open": True, "spend_called": False},
        "handoff": {"builder": BUILDER_ID, "reviewer": REVIEWER_ID, "silent_takeover_blocked": True},
        "human_gate": {"text": gate_text, "should_run_first": quiet_one.get("should_run"), "should_run_second": quiet_two.get("should_run"), "state_unchanged": gate_state_before == gate_state_after},
        "restart": {"fresh_process_status": True, "fresh_process_todos": True, "human_gate_recovered": True},
        "privacy": {"tracked_local_control_state": tracked_state, "authority_hashes_unchanged": True},
        "rollback_preview": {"ok": True, "dry_run": True},
        "limitations": [
            "This proves the direct CLI/custom-runner seam on Linux GitHub Actions, not native Windows support.",
            "The fresh-recovery check is process-level; a later long-running production host should also prove session/runner restart under its own scheduler.",
            "The pilot does not authorize merging this experimental branch into Foundation main.",
        ],
    }
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    _, uninstall = loopx(
        root, env, registry, runtime,
        "uninstall-project", "--goal-id", GOAL_ID, "--archive-state", "--execute",
    )
    require(uninstall.get("ok") is True and uninstall.get("dry_run") is False, f"rollback execution failed: {uninstall}")
    require(not state_file(root).exists(), "selected active goal state must be removed/archived by rollback")
    require(not tracked_local_control_state(root, env), "rollback must not create tracked local state")
    post_rollback_validation = run([sys.executable, "scripts/validate_all.py"], cwd=root, env=env)
    require(post_rollback_validation.returncode == 0, "host-native repository validation failed after LoopX rollback")

    receipt["rollback"] = {
        "executed": True,
        "selected_goal_removed_or_archived": True,
        "post_rollback_validation": "python scripts/validate_all.py",
        "exit_code": post_rollback_validation.returncode,
    }
    receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(receipt, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
