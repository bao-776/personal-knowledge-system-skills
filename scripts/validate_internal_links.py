#!/usr/bin/env python3
"""Check relative Markdown links in repository text files."""
from __future__ import annotations
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

def main() -> int:
    errors: list[str] = []
    checked = 0
    for source in ROOT.rglob("*.md"):
        if ".git" in source.parts:
            continue
        content = source.read_text(encoding="utf-8")
        for raw in LINK.findall(content):
            target = raw.strip().strip("<>")
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            checked += 1
            if not (source.parent / target).resolve().exists():
                errors.append(f"{source.relative_to(ROOT)} -> {target}")
    if errors:
        print("LINK_CHECK_FAILED")
        print("\n".join(errors))
        return 1
    print(f"LINK_CHECK_OK links={checked}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

