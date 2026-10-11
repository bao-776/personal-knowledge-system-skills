#!/usr/bin/env python3
"""Validate repository-level skill structure and routing references."""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = {"knowledge-vault", "vault-bootstrap", "knowledge-intake", "atomic-notes", "obsidian-vault", "growth-system", "inspire-time", "project-lifecycle", "retrospective", "self-observation", "knowledge-output", "knowledge-retrieve", "knowledge-impact", "knowledge-triage", "knowledge-health", "knowledge-capture"}

def main() -> int:
    errors: list[str] = []
    actual = {p.name for p in SKILLS.iterdir() if p.is_dir()}
    if actual != EXPECTED:
        errors.append(f"skill set mismatch: missing={sorted(EXPECTED-actual)} extra={sorted(actual-EXPECTED)}")
    for name in sorted(EXPECTED):
        folder = SKILLS / name
        skill = folder / "SKILL.md"
        ui = folder / "agents" / "openai.yaml"
        if not skill.is_file():
            errors.append(f"{name}: missing SKILL.md")
            continue
        content = skill.read_text(encoding="utf-8")
        if not content.startswith("---\n"):
            errors.append(f"{name}: missing YAML frontmatter")
        if f"name: {name}\n" not in content:
            errors.append(f"{name}: incorrect name")
        match = re.search(r"^description:\s*(.+)$", content, re.M)
        if not match or len(match.group(1).strip()) < 40:
            errors.append(f"{name}: description is not discriminating")
        elif not re.search(r"[\u4e00-\u9fff]", match.group(1)):
            errors.append(f"{name}: description needs a concise Chinese trigger cue")
        if "TODO" in content:
            errors.append(f"{name}: unfinished TODO")
        if not ui.is_file():
            errors.append(f"{name}: missing agents/openai.yaml")
        else:
            ui_content = ui.read_text(encoding="utf-8")
            if "$" + name not in ui_content:
                errors.append(f"{name}: default prompt must mention the skill")
            if not re.search(r"[\u4e00-\u9fff]", ui_content):
                errors.append(f"{name}: UI metadata needs Chinese guidance")
            if "to help me with this knowledge-base task" in ui_content:
                errors.append(f"{name}: default prompt is still generic")
    if errors:
        print("SKILL_STRUCTURE_FAILED")
        print("\n".join(errors))
        return 1
    print(f"SKILL_STRUCTURE_OK skills={len(EXPECTED)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
