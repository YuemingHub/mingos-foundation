#!/usr/bin/env python3
"""Run the complete Ming Foundation repository validation suite."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "validate_repository.py",
    "validate_kernel_family.py",
    "validate_id_reservations.py",
    "validate_audit_scope.py",
    "validate_requirements.py",
    "validate_release_state.py",
    "validate_review_baseline.py",
    "validate_review_execution.py",
    "validate_source_revision.py",
    "validate_round2_review.py",
    "validate_requirement_rebaseline.py",
    "validate_text_integrity.py",
    "validate_profile_review_preparation.py",
    "validate_profile_source_revision.py",
    "validate_review_readiness_gate.py",
    "validate_review_operations_activation.py",
    "validate_controlled_pilot.py",
    "validate_named_accountability.py",
    "validate_human_activation_readiness.py",
    "validate_restricted_nomination_infrastructure.py",
    "validate_cp2_preauthorization.py",
]


def main() -> int:
    for script in SCRIPTS:
        path = ROOT / "scripts" / script
        print(f"=== {script} ===")
        completed = subprocess.run([sys.executable, str(path)], cwd=ROOT)
        if completed.returncode != 0:
            print(f"Validation suite failed at {script}.")
            return completed.returncode
    print("All repository validations passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
