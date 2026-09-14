#!/usr/bin/env python3
"""Scan the working tree and optional Git history for sensitive material."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

TEXT_EXTENSIONS = {".md", ".txt", ".yaml", ".yml", ".json", ".toml", ".py", ".base", ".gitignore", ".html", ".css", ".xml"}
TEXT_NAMES = {"LICENSE", "VERSION", ".gitignore", ".gitkeep", ".nojekyll"}
REVIEWED_BINARIES = {
    "site/assets/social-preview.png": "ba131beb6433cb431dff634fd72b4ffa0df9617c8ac1d3cc611a00830554fcce",
}
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
        relative_parts = path.relative_to(root).parts
        if path.is_file() and not any(part in EXCLUDED_PARTS for part in relative_parts):
            yield path

def scan_text(content: str, location: str, forbidden: list[str]) -> list[str]:
    findings: list[str] = []
    for lineno, line in enumerate(content.splitlines(), 1):
        scan_line = re.sub(r"https?://[^\s)]+", "", line)
        for label, pattern in PATTERNS.items():
            match = pattern.search(scan_line)
            if label == "phone" and match and sum(ch.isdigit() for ch in match.group()) < 10:
                continue
            if match:
                findings.append(f"{location}:{lineno}: {label}")
        for token in forbidden:
            if token and token.casefold() in line.casefold():
                findings.append(f"{location}:{lineno}: forbidden token")
    return findings

def reviewed_binary(name: str, content: bytes) -> bool:
    expected = REVIEWED_BINARIES.get(Path(name).as_posix())
    return bool(expected and hashlib.sha256(content).hexdigest() == expected)

def git_output(root: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=root, text=True, encoding="utf-8", errors="replace", capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "git command failed")
    return result.stdout

def scan_history(root: Path, forbidden: list[str]) -> tuple[list[str], int]:
    if not (root / ".git").exists():
        return ["git-history: repository metadata not found"], 0
    findings: set[str] = set()
    commits = [line for line in git_output(root, "rev-list", "--all").splitlines() if line]
    for commit in commits:
        names = git_output(root, "ls-tree", "-r", "--name-only", commit).splitlines()
        for name in names:
            path = Path(name)
            if path.suffix.lower() not in TEXT_EXTENSIONS and path.name not in TEXT_NAMES:
                result = subprocess.run(["git", "show", f"{commit}:{name}"], cwd=root, capture_output=True)
                if result.returncode == 0 and reviewed_binary(name, result.stdout):
                    continue
                findings.add(f"git-history:{commit[:12]}:{name}: binary or unreviewed file")
                continue
            result = subprocess.run(["git", "show", f"{commit}:{name}"], cwd=root, capture_output=True)
            if result.returncode:
                findings.add(f"git-history:{commit[:12]}:{name}: unreadable")
                continue
            content = result.stdout.decode("utf-8", errors="replace")
            if path.name == "privacy_scan.py":
                continue
            for finding in scan_text(content, f"git-history:{commit[:12]}:{name}", forbidden):
                findings.add(finding)
    return sorted(findings), len(commits)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--forbid", action="append", default=[])
    parser.add_argument("--git-history", action="store_true", help="Scan every committed text version and flag historical binaries")
    parser.add_argument("--report", type=Path, help="Write a machine-readable JSON report")
    args = parser.parse_args()
    root = args.root.resolve()
    findings: list[str] = []
    scanned_files = 0
    for path in iter_files(root):
        relative = path.relative_to(root).as_posix()
        if path.suffix.lower() not in TEXT_EXTENSIONS and path.name not in TEXT_NAMES:
            if reviewed_binary(relative, path.read_bytes()):
                continue
            findings.append(f"{relative}: binary or unreviewed file")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(f"{relative}: non-UTF-8 text")
            continue
        scanned_files += 1
        if path.name != "privacy_scan.py":
            findings.extend(scan_text(content, relative, args.forbid))

    history_commits = 0
    if args.git_history:
        history_findings, history_commits = scan_history(root, args.forbid)
        findings.extend(history_findings)
    findings = sorted(set(findings))
    report = {
        "status": "failed" if findings else "passed",
        "root": str(root),
        "working_tree_files": scanned_files,
        "git_history_enabled": args.git_history,
        "git_commits_scanned": history_commits,
        "findings": findings,
    }
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if findings:
        print("PRIVACY_SCAN_FAILED")
        print("\n".join(findings))
        return 1
    print(f"PRIVACY_SCAN_OK files={scanned_files} commits={history_commits}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
