#!/usr/bin/env python3
"""Run deterministic repository checks and disposable install smokes."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".test-output" / "automated-checks"

def run(*args: str) -> None:
    result = subprocess.run([sys.executable, "-X", "utf8", *args], cwd=ROOT)
    if result.returncode:
        raise SystemExit(result.returncode)

def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    run("scripts/validate_skill_structure.py")
    run("scripts/validate_internal_links.py")
    run("scripts/validate_site.py")
    run("scripts/validate_eval_cases.py")
    run("scripts/test_privacy_scan.py")
    run("scripts/privacy_scan.py", "--git-history", "--report", str(OUT / "privacy-report.json"))
    run("scripts/create_test_vault.py", str(OUT / "vault"))
    run("scripts/install_codex_skills.py", str(OUT / "skills"), "--profile", "full")
    run("scripts/install_codex_skills.py", str(OUT / "skills"), "--profile", "full", "--verify")
    run("scripts/test_installer.py")
    print("ALL_CHECKS_OK contract_checks=9 agent_evaluation=not_run")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
