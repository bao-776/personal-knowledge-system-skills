#!/usr/bin/env python3
"""Install, verify, update, or safely remove suite skills."""
from __future__ import annotations

import argparse
import hashlib
import shutil
from contextlib import contextmanager
from uuid import uuid4
from datetime import datetime
from pathlib import Path

PROFILES = {
    "lightweight": ["knowledge-vault", "knowledge-intake", "atomic-notes", "knowledge-output", "knowledge-retrieve", "knowledge-capture"],
    "growth": ["knowledge-vault", "knowledge-intake", "atomic-notes", "knowledge-output", "growth-system", "project-lifecycle", "retrospective", "knowledge-impact", "knowledge-retrieve", "knowledge-capture"],
    "full": [],
}

def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()

def tree_hashes(root: Path) -> dict[str, str]:
    return {p.relative_to(root).as_posix(): file_hash(p) for p in root.rglob("*") if p.is_file()}

def select_skills(args: argparse.Namespace, available: dict[str, Path]) -> list[str]:
    if args.profile:
        if args.skills:
            raise SystemExit("Choose either --profile or explicit skill names, not both.")
        selected = PROFILES[args.profile] or sorted(available)
    else:
        selected = args.skills or sorted(available)
    unknown = sorted(set(selected) - set(available))
    if unknown:
        raise SystemExit(f"Unknown skills: {', '.join(unknown)}")
    return list(dict.fromkeys(selected))

def backup_path(target_root: Path, operation: str) -> Path:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    return target_root.parent / ("." + target_root.name + "-personal-knowledge-system-backups") / f"{stamp}-{operation}"

@contextmanager
def staging_directory(parent: Path):
    parent = parent.resolve()
    stage = parent / (".pks-stage-" + uuid4().hex)
    stage.mkdir()
    try:
        yield stage
    finally:
        if stage.resolve().parent != parent:
            raise RuntimeError("Unexpected staging cleanup path")
        if stage.exists():
            shutil.rmtree(stage)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=Path, nargs="?", help="Codex skills directory")
    parser.add_argument("skills", nargs="*", help="Skill names; omit to install all")
    parser.add_argument("--profile", choices=sorted(PROFILES), help="Install a tested skill set")
    parser.add_argument("--list", action="store_true", help="List skills and profiles")
    parser.add_argument("--force", action="store_true", help="Update existing skills after backing them up")
    parser.add_argument("--verify", action="store_true", help="Compare installed files with this repository")
    parser.add_argument("--uninstall", action="store_true", help="Move selected skills to a backup folder")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    source_root = Path(__file__).resolve().parents[1] / "skills"
    available = {p.name: p for p in source_root.iterdir() if p.is_dir()}
    if args.list:
        print("Skills:")
        for name in sorted(available):
            print(f"  {name}")
        print("Profiles:")
        for name, members in PROFILES.items():
            print(f"  {name}: {', '.join(members or sorted(available))}")
        return 0
    if args.target is None:
        parser.error("target is required unless --list is used")
    if args.verify and args.uninstall:
        parser.error("--verify and --uninstall cannot be combined")

    selected = select_skills(args, available)
    target_root = args.target.resolve()
    if args.verify:
        errors = []
        for name in selected:
            destination = target_root / name
            if not destination.is_dir():
                errors.append(f"{name}: not installed")
            elif tree_hashes(available[name]) != tree_hashes(destination):
                errors.append(f"{name}: installed files differ")
        if errors:
            print("VERIFY_FAILED")
            print("\n".join(errors))
            return 1
        print(f"VERIFY_OK skills={len(selected)}")
        return 0

    if args.uninstall:
        present = [n for n in selected if (target_root / n).exists()]
        if not present:
            print("UNINSTALL_NOOP no selected skills are installed")
            return 0
        backup = backup_path(target_root, "uninstall")
        for name in present:
            print(f"MOVE {target_root / name} -> {backup / name}")
        if args.dry_run:
            print(f"UNINSTALL_DRY_RUN_OK skills={len(present)}")
            return 0
        backup.mkdir(parents=True, exist_ok=True)
        for name in present:
            shutil.move(str(target_root / name), str(backup / name))
        print(f"UNINSTALL_OK skills={len(present)} backup={backup}")
        return 0

    existing = [n for n in selected if (target_root / n).exists()]
    if existing and not args.force:
        raise SystemExit("Already installed: " + ", ".join(existing) + ". Re-run with --force to update after backup.")
    for name in selected:
        print(f"COPY {available[name]} -> {target_root / name}")
    if args.dry_run:
        print(f"INSTALL_DRY_RUN_OK skills={len(selected)}")
        return 0

    # Stage and verify all copies outside the discovery directory before mutation.
    target_root.parent.mkdir(parents=True, exist_ok=True)
    backup = backup_path(target_root, "update") if existing else None
    moved: list[str] = []
    installed: list[str] = []
    with staging_directory(target_root.parent) as stage:
        for name in selected:
            shutil.copytree(available[name], stage / name)
            if tree_hashes(available[name]) != tree_hashes(stage / name):
                raise RuntimeError(f"Staged verification failed: {name}")
        target_root.mkdir(parents=True, exist_ok=True)
        try:
            if backup:
                backup.mkdir(parents=True, exist_ok=True)
                for name in existing:
                    shutil.move(str(target_root / name), str(backup / name))
                    moved.append(name)
            for name in selected:
                shutil.move(str(stage / name), str(target_root / name))
                installed.append(name)
        except Exception:
            for name in reversed(installed):
                shutil.move(str(target_root / name), str(stage / name))
            for name in reversed(moved):
                shutil.move(str(backup / name), str(target_root / name))
            raise
    verb = "UPDATE_OK" if existing else "INSTALL_OK"
    suffix = f" backup={backup}" if backup else ""
    print(f"{verb} skills={len(selected)}{suffix}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
