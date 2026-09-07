#!/usr/bin/env python3
"""Create a minimal test vault from the public template."""
from __future__ import annotations
import argparse
import shutil
from pathlib import Path

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / "skills" / "vault-bootstrap" / "assets" / "minimum-vault"
    target = args.target.resolve()
    if target.exists() and any(target.iterdir()) and not args.force:
        raise SystemExit("Target is not empty; use --force only for a disposable test directory.")
    target.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target, dirs_exist_ok=True)
    print(f"TEST_VAULT_CREATED {target}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

