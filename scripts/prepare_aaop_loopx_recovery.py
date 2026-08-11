#!/usr/bin/env python3
"""Keep fresh-process LoopX recovery inside the already-authorized pilot scan scope."""
from pathlib import Path

path = Path("scripts/aaop_loopx_consumer_pilot_v4.py")
text = path.read_text(encoding="utf-8")
old = '_, recovered_status = lx(root, env, registry, runtime, "status", "--scan-root", ".")'
new = '_, recovered_status = lx(root, env, registry, runtime, "status", "--scan-path", ".gitignore", "--goal-id", GOAL, "--agent-id", BUILDER)'
if old not in text:
    raise SystemExit("expected fresh-process status call not found")
path.write_text(text.replace(old, new), encoding="utf-8")
print("Scoped fresh-process LoopX status recovery to the bounded pilot surface and explicit goal/agent identity.")
