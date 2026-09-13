#!/usr/bin/env python3
"""Validate the reusable Codex behavior-evaluation manifest."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
REQUIRED_FIELDS = {"id", "language", "prompt", "expected_skills", "forbidden_skills", "assertions"}

def main() -> int:
    path = ROOT / "tests" / "evals" / "cases.json"
    cases = json.loads(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    ids: set[str] = set()
    covered: set[str] = set()
    chinese = 0
    boundary = 0
    for index, case in enumerate(cases, 1):
        missing = REQUIRED_FIELDS - set(case)
        if missing:
            errors.append(f"case {index}: missing {sorted(missing)}")
            continue
        if case["id"] in ids:
            errors.append(f"{case['id']}: duplicate id")
        ids.add(case["id"])
        expected = set(case["expected_skills"])
        forbidden = set(case["forbidden_skills"])
        unknown = (expected | forbidden) - EXPECTED
        if unknown:
            errors.append(f"{case['id']}: unknown skills {sorted(unknown)}")
        if expected & forbidden:
            errors.append(f"{case['id']}: skill both expected and forbidden")
        if not case["prompt"].strip() or not case["assertions"]:
            errors.append(f"{case['id']}: prompt and assertions are required")
        covered |= expected
        chinese += case["language"].lower().startswith("zh")
        boundary += bool(forbidden)
    if covered != EXPECTED:
        errors.append(f"skill coverage mismatch: missing={sorted(EXPECTED-covered)}")
    if chinese < 10:
        errors.append("at least 10 Chinese cases are required")
    if boundary < 5:
        errors.append("at least 5 boundary cases are required")
    if errors:
        print("EVAL_CASES_FAILED")
        print("\n".join(errors))
        return 1
    print(f"EVAL_CASES_OK cases={len(cases)} skills={len(covered)} chinese={chinese} boundaries={boundary}")
    return 0

if __name__ == "__main__":
    sys.exit(main())

