#!/usr/bin/env python3
"""Install selected suite skills into a Codex skills directory."""
from __future__ import annotations
import argparse
import shutil
from pathlib import Path

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=Path, help="Codex skills directory")
    parser.add_argument("skills", nargs="*", help="Skill names; omit to install all")
    parser.add_argument("--force", action="store_true", help="Replace an existing installed skill")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    source_root = Path(__file__).resolve().parents[1] / "skills"
    available = {path.name: path for path in source_root.iterdir() if path.is_dir()}
    selected = args.skills or sorted(available)
    unknown = sorted(set(selected) - set(available))
    if unknown:
        raise SystemExit(f"Unknown skills: {', '.join(unknown)}")
    target_root = args.target.resolve()
    plan: list[tuple[Path, Path]] = []
    for name in selected:
        destination = target_root / name
        if destination.exists() and not args.force:
            raise SystemExit(f"Already exists: {destination}. Re-run with --force only after review.")
        plan.append((available[name], destination))
    for source, destination in plan:
        print(f"{source.name} -> {destination}")
    if args.dry_run:
        print(f"INSTALL_DRY_RUN_OK skills={len(plan)}")
        return 0
    target_root.mkdir(parents=True, exist_ok=True)
    for source, destination in plan:
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(source, destination)
    print(f"INSTALL_OK skills={len(plan)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

