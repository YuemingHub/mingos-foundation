#!/usr/bin/env python3
"""Keep LoopX recovery and Git evidence inside the bounded pilot contract."""
from pathlib import Path

path = Path("scripts/aaop_loopx_consumer_pilot_v4.py")
text = path.read_text(encoding="utf-8")

old_status = '_, recovered_status = lx(root, env, registry, runtime, "status", "--scan-root", ".")'
new_status = '_, recovered_status = lx(root, env, registry, runtime, "status", "--scan-path", ".gitignore", "--goal-id", GOAL, "--agent-id", BUILDER)'
if old_status not in text:
    raise SystemExit("expected fresh-process status call not found")
text = text.replace(old_status, new_status)

# `git status --short` is allowed to collapse a wholly untracked directory to
# `?? experiments/`, which made an existing marker look absent. Ask Git for all
# untracked paths so the evidence assertion proves the exact bounded file.
old_git_status = 'run(["git", "status", "--short"], root, env).stdout.splitlines()'
new_git_status = 'run(["git", "status", "--short", "--untracked-files=all"], root, env).stdout.splitlines()'
if old_git_status not in text:
    raise SystemExit("expected git status evidence call not found")
text = text.replace(old_git_status, new_git_status)

path.write_text(text, encoding="utf-8")
print("Scoped fresh-process status and made exact untracked marker evidence observable.")
