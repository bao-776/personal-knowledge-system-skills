#!/usr/bin/env python3
"""Exercise profiles, router dependencies, update backup, verify, and uninstall backup."""
from __future__ import annotations

import shutil
import importlib.util
from uuid import uuid4
from unittest.mock import patch
import io
from contextlib import redirect_stdout
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".test-output" / "installer-lifecycle"
INSTALLER = "scripts/install_codex_skills.py"

def run(*args: str) -> str:
    spec = importlib.util.spec_from_file_location("installer_cli_test", ROOT / INSTALLER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    output = io.StringIO()
    with patch.object(sys, "argv", [INSTALLER, *args]), redirect_stdout(output):
        result = module.main()
    if result:
        raise AssertionError(output.getvalue())
    return output.getvalue()


def exercise(out: Path) -> int:
    global OUT
    OUT = out
    OUT.mkdir(parents=True, exist_ok=True)

    listing = run("--list")
    for profile in ("lightweight", "growth", "full"):
        if f"{profile}:" not in listing:
            raise SystemExit(f"profile missing from --list: {profile}")

    for profile, expected in (("lightweight", 6), ("growth", 10), ("full", 16)):
        profile_target = OUT / ("profile-" + profile)
        run(str(profile_target), "--profile", profile)
        run(str(profile_target), "--profile", profile, "--verify")
        installed = [p for p in profile_target.iterdir() if p.is_dir() and (p / "SKILL.md").exists()]
        if len(installed) != expected:
            raise AssertionError(f"{profile} installed {len(installed)} skills, expected {expected}")
    for name in ("knowledge-capture", "knowledge-retrieve", "knowledge-impact", "knowledge-triage", "knowledge-health"):
        single_target = OUT / ("single-" + name)
        run(str(single_target), name)
        run(str(single_target), name, "--verify")
        if sorted(p.name for p in single_target.iterdir() if p.is_dir()) != [name]:
            raise AssertionError(f"{name} unexpectedly requires another installed module")

    router_plan = run(str(OUT / "router"), "knowledge-vault", "--dry-run")
    if "skills=1" not in router_plan:
        raise SystemExit("standalone router unexpectedly expanded the suite")

    target = OUT / "lightweight"
    run(str(target), "--profile", "lightweight")
    run(str(target), "--profile", "lightweight", "--verify")
    run(str(target), "atomic-notes", "--force")
    run(str(target), "atomic-notes", "--verify")
    run(str(target), "atomic-notes", "--uninstall")
    if (target / "atomic-notes").exists():
        raise SystemExit("uninstall left the selected skill active")
    backups = list((target.parent / ("." + target.name + "-personal-knowledge-system-backups")).rglob("atomic-notes"))
    if len(backups) < 2:
        raise SystemExit("update and uninstall backups were not both preserved")

    spec = importlib.util.spec_from_file_location("installer_under_test", ROOT / INSTALLER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    failure_target = OUT / "rollback"
    run(str(failure_target), "knowledge-intake", "atomic-notes")
    (failure_target / "atomic-notes" / "user-customization.md").write_text("keep me", encoding="utf-8")
    before = module.tree_hashes(failure_target)
    real_move = module.shutil.move
    def fail_install(source, destination, *args, **kwargs):
        if ".pks-stage-" in str(source) and Path(destination) == failure_target / "knowledge-intake":
            raise OSError("injected replacement failure")
        return real_move(source, destination, *args, **kwargs)
    with patch.object(sys, "argv", [INSTALLER, str(failure_target), "atomic-notes", "knowledge-intake", "--force"]):
        with patch.object(module.shutil, "move", side_effect=fail_install):
            try:
                module.main()
            except OSError:
                pass
            else:
                raise AssertionError("injected failure did not occur")
    if before != module.tree_hashes(failure_target):
        raise AssertionError("rollback did not restore exact customized old versions")
    if (failure_target / ".personal-knowledge-system-backups").exists():
        raise AssertionError("backup is inside skill discovery")
    print("INSTALLER_LIFECYCLE_OK profiles=3 installed_counts=6/10/16 standalone_tasks=5 standalone_router=1 backups=2 rollback=exact")
    return 0

def main() -> int:
    scratch = ROOT / (".pks-installer-test-" + uuid4().hex)
    scratch.mkdir()
    try:
        return exercise(scratch)
    finally:
        if scratch.resolve().parent != ROOT.resolve():
            raise RuntimeError("Unexpected test cleanup path")
        shutil.rmtree(scratch)

if __name__ == "__main__":
    raise SystemExit(main())

