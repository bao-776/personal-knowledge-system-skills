#!/usr/bin/env python3
"""Scan the repository for likely personal or sensitive material."""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

TEXT_EXTENSIONS = {".md", ".txt", ".yaml", ".yml", ".json", ".toml", ".py", ".base", ".gitignore"}
EXCLUDED_PARTS = {".git", "__pycache__", ".test-output"}
PATTERNS = {
    "windows-user-path": re.compile(r"[A-Za-z]:\\Users\\[^\\/\s]+", re.I),
    "unix-home-path": re.compile(r"/(?:Users|home)/[^/\s]+", re.I),
    "email": re.compile(r"(?<![\w.+-])[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}(?![\w.-])"),
    "phone": re.compile(r"(?<![\d-])(?:\+?\d[\d ()-]{8,}\d)(?![\d-])"),
    "credential": re.compile(r"(?i)(?:api[_-]?key|access[_-]?token|secret|password)\s*[:=]\s*[\"']?[^\s\"']{8,}"),
}

def iter_files(root: Path):
    for path in root.rglob("*"):
        if path.is_file() and not any(part in EXCLUDED_PARTS for part in path.parts):
            if path.suffix.lower() in TEXT_EXTENSIONS or path.name == ".gitignore":
                yield path

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--forbid", action="append", default=[])
    args = parser.parse_args()
    root = args.root.resolve()
    findings: list[str] = []
    for path in iter_files(root):
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(f"{path.relative_to(root)}: non-UTF-8 text")
            continue
        for lineno, line in enumerate(content.splitlines(), 1):
            scan_line = re.sub(r"https?://[^\s)]+", "", line)
            if path.name != "privacy_scan.py":
                for label, pattern in PATTERNS.items():
                    match = pattern.search(scan_line)
                    if label == "phone" and match and sum(ch.isdigit() for ch in match.group()) < 10:
                        continue
                    if match:
                        findings.append(f"{path.relative_to(root)}:{lineno}: {label}")
            for token in args.forbid:
                if token and token.casefold() in line.casefold():
                    findings.append(f"{path.relative_to(root)}:{lineno}: forbidden token")
    text_names = {".gitignore", "LICENSE"}
    for path in root.rglob("*"):
        if path.is_file() and not any(part in EXCLUDED_PARTS for part in path.parts):
            if path.suffix.lower() not in TEXT_EXTENSIONS and path.name not in text_names | {".gitkeep"}:
                findings.append(f"{path.relative_to(root)}: binary or unreviewed file")
    if findings:
        print("PRIVACY_SCAN_FAILED")
        print("\n".join(findings))
        return 1
    print(f"PRIVACY_SCAN_OK files={sum(1 for _ in iter_files(root))}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
