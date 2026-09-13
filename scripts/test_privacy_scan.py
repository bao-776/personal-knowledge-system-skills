#!/usr/bin/env python3
"""Verify that the privacy scanner catches representative synthetic leaks."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".test-output" / "privacy-self-test"

def scan(target: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-X", "utf8", "scripts/privacy_scan.py", "--root", str(target)],
        cwd=ROOT, text=True, encoding="utf-8", capture_output=True,
    )

def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    clean = OUT / "clean"
    sensitive = OUT / "sensitive"
    clean.mkdir(parents=True)
    sensitive.mkdir(parents=True)
    (clean / "note.md").write_text("A fictional, non-sensitive note.\n", encoding="utf-8")
    synthetic_email = "fictional.person" + "@" + "example.net"
    synthetic_path = "C:" + "\\Users\\" + "fictional-person\\private-vault"
    synthetic_secret = "api" + "_key=" + "synthetic-test-key-12345"
    (sensitive / "input.md").write_text(
        f"Email: {synthetic_email}\nPath: {synthetic_path}\n{synthetic_secret}\n",
        encoding="utf-8",
    )
    clean_result = scan(clean)
    sensitive_result = scan(sensitive)
    if clean_result.returncode != 0:
        raise SystemExit("privacy scanner rejected clean synthetic content")
    expected = {"email", "windows-user-path", "credential"}
    missing = {label for label in expected if label not in sensitive_result.stdout}
    if sensitive_result.returncode == 0 or missing:
        raise SystemExit(f"privacy scanner missed synthetic categories: {sorted(missing)}")
    print("PRIVACY_SELF_TEST_OK categories=3")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
