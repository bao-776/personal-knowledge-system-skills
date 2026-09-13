#!/usr/bin/env python3
"""Exercise profiles, router dependencies, update backup, verify, and uninstall backup."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".test-output" / "installer-lifecycle"
INSTALLER = "scripts/install_codex_skills.py"

def run(*args: str) -> str:
    result = subprocess.run([sys.executable, "-X", "utf8", INSTALLER, *args], cwd=ROOT, text=True, encoding="utf-8", capture_output=True)
    if result.returncode:
        print(result.stdout)
        print(result.stderr)
        raise SystemExit(result.returncode)
    return result.stdout

def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    listing = run("--list")
    for profile in ("lightweight", "growth", "full"):
        if f"{profile}:" not in listing:
            raise SystemExit(f"profile missing from --list: {profile}")

    router_plan = run(str(OUT / "router"), "knowledge-vault", "--dry-run")
    if "including all routed child skills" not in router_plan or "skills=11" not in router_plan:
        raise SystemExit("knowledge-vault did not expand to the full routed suite")

    target = OUT / "lightweight"
    run(str(target), "--profile", "lightweight")
    run(str(target), "--profile", "lightweight", "--verify")
    run(str(target), "atomic-notes", "--force")
    run(str(target), "atomic-notes", "--verify")
    run(str(target), "atomic-notes", "--uninstall")
    if (target / "atomic-notes").exists():
        raise SystemExit("uninstall left the selected skill active")
    backups = list((target / ".personal-knowledge-system-backups").rglob("atomic-notes"))
    if len(backups) < 2:
        raise SystemExit("update and uninstall backups were not both preserved")

    print("INSTALLER_LIFECYCLE_OK profiles=3 router_dependencies=11 backups=2")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

