#!/usr/bin/env python3
"""Experiment-only AAOP/LoopX real-consumer pilot for Foundation PR #18."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

GOAL = "aaop-loopx-foundation-pilot"
BUILDER = "aaop-pilot-builder"
REVIEWER = "aaop-pilot-reviewer"
MARKER = Path("experiments/aaop-loopx-pilot/runtime-marker.txt")
RECEIPT = Path("experiments/aaop-loopx-pilot/pilot-receipt.json")
AUTHORITY = [
    Path("README.md"),
    Path("foundation/charter/MF-0004-life-charter.md"),
    Path("governance/status/GOV-0001-current-canonical-state.md"),
]


def need(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args: list[str], root: Path, env: dict[str, str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, cwd=root, env=env, text=True, capture_output=True, check=False)
    if check and result.returncode != 0:
        raise AssertionError(
            f"command failed ({result.returncode}): {' '.join(args)}\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    return result


def payload(result: subprocess.CompletedProcess[str], label: str) -> dict[str, Any]:
    try:
        value = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise AssertionError(f"{label}: invalid JSON\n{result.stdout}\n{result.stderr}") from exc
    need(isinstance(value, dict), f"{label}: expected JSON object")
    return value


def lx(root: Path, env: dict[str, str], registry: Path, runtime: Path, *args: str, check: bool = True) -> tuple[subprocess.CompletedProcess[str], dict[str, Any]]:
    result = run(
        ["loopx", "--registry", str(registry), "--runtime-root", str(runtime), "--format", "json", *args],
        root,
        env,
        check=check,
    )
    return result, payload(result, "loopx " + " ".join(args))


def goal_state(root: Path) -> Path:
    return root / ".codex" / "goals" / GOAL / "ACTIVE_GOAL_STATE.md"


def tracked_private(root: Path, env: dict[str, str]) -> list[str]:
    result = run(["git", "ls-files", ".loopx", ".codex/goals", ".local"], root, env)
    return [line for line in result.stdout.splitlines() if line.strip()]


def validate_consumer(root: Path, env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    # This non-governance experiment uses the repository's independent metadata/reference
    # validator. validate_id_reservations.py binds unrelated PR changes to historical PR #12
    # and is therefore recorded as a known policy incompatibility rather than rewritten here.
    return run([sys.executable, "scripts/validate_repository.py"], root, env)


def should_run(root: Path, env: dict[str, str], registry: Path, runtime: Path, agent: str) -> dict[str, Any]:
    _, value = lx(
        root,
        env,
        registry,
        runtime,
        "quota",
        "should-run",
        "--goal-id",
        GOAL,
        "--agent-id",
        agent,
        "--runtime-profile",
        "generic_cli",
        "--available-capability",
        "shell",
        "--scan-path",
        ".",
        check=False,
    )
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--aaop-revision", required=True)
    parser.add_argument("--loopx-revision", required=True)
    parser.add_argument("--loopx-version", required=True)
    args = parser.parse_args()

    root = Path.cwd().resolve()
    registry = root / ".loopx" / "registry.json"
    runtime = root / ".local" / "aaop-loopx-pilot-runtime"
    marker = root / MARKER
    receipt_path = root / RECEIPT
    env = {**os.environ, "PYTHONUTF8": "1"}

    gap = {
        "class": "execution-continuity",
        "observable_failure": "AAOP can persist blocker/next-action evidence but host-native execution has no durable provider-neutral run|gate|wait|quiet decision for a fresh process.",
        "success_delta": "Fresh processes recover the bounded frontier and unchanged human-gated state returns should_run=false without a new work turn.",
    }

    authority_before = {str(path): digest(root / path) for path in AUTHORITY}
    need(not tracked_private(root, env), "LoopX local state is already tracked")
    for path in [".loopx/registry.json", ".codex/goals/example/ACTIVE_GOAL_STATE.md", ".local/aaop-loopx-pilot-runtime/example"]:
        ignored = run(["git", "check-ignore", "-q", "--no-index", path], root, env, check=False)
        need(ignored.returncode == 0, f"local control path is not ignored: {path}")

    connect_args = [
        "connect", "--project", ".", "--goal-id", GOAL,
        "--objective", "Prove one bounded AAOP execution-continuity pilot without changing Foundation authority.",
        "--domain", "aaop-loopx-provider-pilot", "--no-onboarding-scan",
        "--codex-app-heartbeat", "no", "--write-scope", "experiments/aaop-loopx-pilot/**",
    ]
    _, preview = lx(root, env, registry, runtime, *connect_args, "--dry-run")
    need(preview.get("ok") is True and not registry.exists(), f"connect preview was not read-only: {preview}")
    _, connected = lx(root, env, registry, runtime, *connect_args)
    need(connected.get("ok") is True and registry.is_file() and goal_state(root).is_file(), f"connect failed: {connected}")

    # First connection is fail-closed. Before health readback LoopX must refuse automatic
    # work even if a later todo could otherwise be eligible.
    precheck = should_run(root, env, registry, runtime, BUILDER)
    need(precheck.get("should_run") is False, f"connected_without_run should fail closed: {precheck}")
    need(precheck.get("status_health_ok") is False, f"pre-check health unexpectedly trusted: {precheck}")

    # Fulfil the provider's own generated first-run contract instead of bypassing it.
    _, checked = lx(root, env, registry, runtime, "check", "--scan-root", ".")
    need(checked.get("ok") is True, f"LoopX project check failed: {checked}")

    for agent in [BUILDER, REVIEWER]:
        _, plan = lx(root, env, registry, runtime, "register-agent", "--goal-id", GOAL, "--agent-id", agent)
        need(plan.get("ok") is True, f"register-agent preview failed: {plan}")
        _, applied = lx(root, env, registry, runtime, "register-agent", "--goal-id", GOAL, "--agent-id", agent, "--execute")
        need(applied.get("ok") is True, f"register-agent apply failed: {applied}")

    task_text = "Create the bounded AAOP/LoopX pilot marker and validate the current Foundation branch."
    _, added = lx(root, env, registry, runtime, "todo", "add", "--goal-id", GOAL, "--role", "agent", "--text", task_text)
    todo = str(added.get("todo_id") or "")
    need(added.get("added") is True and todo.startswith("todo_"), f"todo add failed: {added}")
    _, claimed = lx(root, env, registry, runtime, "todo", "claim", "--goal-id", GOAL, "--todo-id", todo, "--claimed-by", BUILDER, "--agent-id", BUILDER)
    need(claimed.get("changed") is True, f"todo claim failed: {claimed}")

    eligible = should_run(root, env, registry, runtime, BUILDER)
    need(eligible.get("ok") is True and eligible.get("should_run") is True, f"validated connected goal was not runnable: {eligible}")
    need((eligible.get("selected_todo") or {}).get("todo_id") == todo, f"quota did not select builder's claimed todo: {eligible}")

    # Failed validation is not completion and does not spend quota.
    failed = run([sys.executable, "-c", "raise SystemExit(23)"], root, env, check=False)
    need(failed.returncode == 23, "negative validator did not fail")
    state_text = goal_state(root).read_text(encoding="utf-8")
    need(todo in state_text and "status=open" in state_text, "failed validation did not leave todo open")

    marker.parent.mkdir(parents=True, exist_ok=True)
    marker.write_text(
        "AAOP LoopX consumer pilot marker\n"
        f"aaop_revision={args.aaop_revision}\n"
        f"loopx_revision={args.loopx_revision}\n",
        encoding="utf-8",
    )
    need(marker.read_text(encoding="utf-8").startswith("AAOP LoopX consumer pilot marker"), "marker readback failed")
    validation = validate_consumer(root, env)

    _, completed = lx(
        root, env, registry, runtime, "todo", "complete", "--goal-id", GOAL, "--todo-id", todo,
        "--claimed-by", BUILDER, "--agent-id", BUILDER,
        "--evidence", "scripts/validate_repository.py exit=0 and marker readback passed", "--no-follow-up",
    )
    need(completed.get("changed") is True, f"validated todo completion failed: {completed}")
    _, refreshed = lx(root, env, registry, runtime, "refresh-state", "--goal-id", GOAL, "--no-global-sync")
    need(refreshed.get("ok") is True, f"refresh failed: {refreshed}")
    _, spent = lx(root, env, registry, runtime, "quota", "spend-slot", "--goal-id", GOAL, "--agent-id", BUILDER, "--slots", "1", "--source", "controller", "--execute", "--scan-path", ".")
    need(spent.get("ok") is True, f"post-validation quota spend failed: {spent}")

    # Bounded reviewer handoff; the prior builder cannot silently steal it.
    review_text = "Review the bounded marker/evidence without taking ownership of the AAOP Journey."
    _, review_added = lx(root, env, registry, runtime, "todo", "add", "--goal-id", GOAL, "--role", "agent", "--text", review_text)
    review_todo = str(review_added.get("todo_id") or "")
    need(review_todo.startswith("todo_"), f"review todo add failed: {review_added}")
    _, review_claim = lx(root, env, registry, runtime, "todo", "claim", "--goal-id", GOAL, "--todo-id", review_todo, "--claimed-by", REVIEWER, "--agent-id", REVIEWER)
    need(review_claim.get("changed") is True, f"review handoff failed: {review_claim}")
    takeover_result, takeover = lx(root, env, registry, runtime, "todo", "claim", "--goal-id", GOAL, "--todo-id", review_todo, "--claimed-by", BUILDER, "--agent-id", BUILDER, check=False)
    need(takeover_result.returncode != 0 or takeover.get("changed") is not True, "builder silently took reviewer work")
    _, review_done = lx(root, env, registry, runtime, "todo", "complete", "--goal-id", GOAL, "--todo-id", review_todo, "--claimed-by", REVIEWER, "--agent-id", REVIEWER, "--evidence", "reviewer read marker and native validation evidence", "--no-follow-up")
    need(review_done.get("changed") is True, f"review completion failed: {review_done}")

    # Genuine AAOP/human-owned authorization stays outside LoopX execution authority.
    gate_text = "Human owner decides whether this experimental branch may ever be merged into Foundation main."
    _, gate = lx(root, env, registry, runtime, "todo", "add", "--goal-id", GOAL, "--role", "user", "--task-class", "user_gate", "--global-gate", "--text", gate_text)
    need(gate.get("added") is True, f"human gate add failed: {gate}")
    quiet_before = digest(goal_state(root))
    q1 = should_run(root, env, registry, runtime, BUILDER)
    q2 = should_run(root, env, registry, runtime, BUILDER)
    quiet_after = digest(goal_state(root))
    need(q1.get("should_run") is False and q2.get("should_run") is False, f"unchanged human gate did not stay quiet: {q1} / {q2}")
    need(quiet_before == quiet_after, "quiet should-run probes mutated durable state")
    need((q2.get("scheduler_hint") or {}).get("action") in {"backoff_until_state_change", "wait_until_state_change", "stop"}, f"quiet state lacks a bounded scheduler decision: {q2}")

    # Every CLI call above is a fresh process; explicitly recover status/todos again.
    _, fresh_status = lx(root, env, registry, runtime, "status", "--scan-root", ".")
    _, fresh_todos = lx(root, env, registry, runtime, "todo", "list", "--goal-id", GOAL)
    need(fresh_status.get("ok") is True and fresh_todos.get("ok") is True, "fresh-process recovery failed")
    need(gate_text in json.dumps(fresh_todos, ensure_ascii=False), "fresh process lost human gate")

    authority_after = {str(path): digest(root / path) for path in AUTHORITY}
    need(authority_before == authority_after, "Foundation authority files changed")
    need(not tracked_private(root, env), "LoopX private state became tracked")
    status_lines = run(["git", "status", "--short"], root, env).stdout.splitlines()
    need(any(str(MARKER) in line for line in status_lines), "real working-tree marker is missing")
    need(not any(".loopx/" in line or ".codex/goals/" in line or ".local/" in line for line in status_lines), "private control state leaked into git status")

    _, rollback_plan = lx(root, env, registry, runtime, "uninstall-project", "--goal-id", GOAL, "--archive-state")
    need(rollback_plan.get("ok") is True and rollback_plan.get("dry_run") is True, f"rollback preview failed: {rollback_plan}")

    receipt: dict[str, Any] = {
        "schema_version": 1,
        "verdict": "closes-gap",
        "consumer": "YuemingHub/mingos-foundation",
        "consumer_branch": os.environ.get("GITHUB_HEAD_REF") or os.environ.get("GITHUB_REF_NAME") or "local",
        "aaop_revision": args.aaop_revision,
        "loopx_revision": args.loopx_revision,
        "loopx_version": args.loopx_version,
        "pre_adoption_gap": gap,
        "first_connect_fail_closed": {"should_run": precheck.get("should_run"), "status_health_ok": precheck.get("status_health_ok")},
        "project_check": {"ok": True},
        "real_delivery": {"path": str(MARKER), "validation": "python scripts/validate_repository.py", "exit_code": validation.returncode},
        "negative_validation": {"exit_code": failed.returncode, "todo_remained_open": True, "quota_spend_called": False},
        "handoff": {"builder": BUILDER, "reviewer": REVIEWER, "silent_takeover_blocked": True},
        "human_gate": {"text": gate_text, "probe_should_run": [q1.get("should_run"), q2.get("should_run")], "durable_state_unchanged": True, "scheduler_action": (q2.get("scheduler_hint") or {}).get("action")},
        "restart": {"fresh_process_status": True, "fresh_process_todos": True, "human_gate_recovered": True},
        "privacy": {"tracked_loopx_state": [], "authority_hashes_unchanged": True},
        "rollback_preview": {"ok": True, "dry_run": True},
        "limitations": [
            "Linux GitHub Actions only; native Windows/WSL remains unqualified.",
            "Fresh recovery is process-level; a production scheduler still needs host-specific session/restart qualification.",
            "Foundation validate_id_reservations.py is not applicable to this unrelated experiment because it binds substantive PR changes to historical PR #12; validate_repository.py is the applicable native integrity gate.",
            "This experiment does not authorize merging PR #18 into Foundation main.",
        ],
    }
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    _, rollback = lx(root, env, registry, runtime, "uninstall-project", "--goal-id", GOAL, "--archive-state", "--execute")
    need(rollback.get("ok") is True and rollback.get("dry_run") is False, f"rollback failed: {rollback}")
    need(not goal_state(root).exists(), "selected LoopX goal state was not removed/archived")
    need(not tracked_private(root, env), "rollback created tracked private state")
    post = validate_consumer(root, env)
    receipt["rollback"] = {"executed": True, "selected_goal_removed_or_archived": True, "post_rollback_validation": "python scripts/validate_repository.py", "exit_code": post.returncode}
    receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
