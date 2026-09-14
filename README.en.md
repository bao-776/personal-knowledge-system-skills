# Personal Knowledge System Skills

> An open-source suite of 11 Codex skills for students, researchers, and knowledge workers who want to build a personalized, evidence-based knowledge system in Markdown or Obsidian.

[Website](https://bao-776.github.io/personal-knowledge-system-skills/en/) · [中文说明](README.md) · [Installation](#quick-start) · [GitHub Issues](https://github.com/bao-776/personal-knowledge-system-skills/issues)

![Codex Skills](https://img.shields.io/badge/Codex-Skills-111827?style=flat-square)
![Obsidian Compatible](https://img.shields.io/badge/Obsidian-Compatible-7C3AED?style=flat-square)
![Skills](https://img.shields.io/badge/Skills-11-0EA5E9?style=flat-square)
![Version](https://img.shields.io/badge/Version-0.1.3-FF6B35?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square)

Saving information is easy. Turning it into understanding that remains useful across projects, study, and daily life is harder. This project helps you preserve raw material, separate evidence from interpretation, connect reusable notes, test ideas in practice, review what happened, and produce work for a clear audience.

Start with `$knowledge-vault` if you are unsure which workflow you need. It routes the request to the shortest relevant path and previews proposed writes before changing a vault.

## What makes it different

- **Simple enough to start:** begin with a small `Raw / Wiki / Outputs` structure instead of designing an entire life taxonomy.
- **Connected with intent:** atomic notes link to meaningful sources, topics, dependencies, and real applications rather than collecting decorative backlinks.
- **Personalized:** the bootstrap interview asks about your goals, habits, existing files, and privacy boundaries before proposing a structure.
- **Built for growth:** books and courses remain inputs; capability is supported by explanation, practice, feedback, exception handling, and transfer evidence.
- **Rich enough for real work:** follow a project from question and evidence through decisions, execution, validation, retrospective, output, and later updates.
- **Careful about self-knowledge:** observations retain context, confidence, counterevidence, and alternative explanations instead of turning one event into a fixed personality label.

The core workflow is:

```text
Capture → Preserve → Examine → Connect → Plan → Practice → Validate → Review → Distill → Publish → Update
```

## The 11 skills

| Skill | Use it when you want to… |
|---|---|
| `$knowledge-vault` | route a request across several stages or find the right starting point |
| `$vault-bootstrap` | interview your needs and create a minimum viable vault |
| `$knowledge-intake` | process articles, conversations, meeting notes, or mixed source material |
| `$atomic-notes` | turn reusable ideas into focused notes and update existing knowledge first |
| `$obsidian-vault` | use Properties, Wikilinks, Backlinks, Bases, and dashboards while keeping Markdown portable |
| `$growth-system` | assess learning candidates, capacity, practice, and capability evidence |
| `$inspire-time` | preserve a small transferable insight and connect it to a real-world practice |
| `$project-lifecycle` | track goals, decisions, evidence, interruptions, validation, and completion |
| `$retrospective` | review a project or period from recorded events and define the next experiment |
| `$self-observation` | examine recurring preferences or work patterns without diagnosis or fixed labels |
| `$knowledge-output` | create an audience-specific report, article, application, or briefing with disclosure control |

## Quick start

Clone or download this repository, then inspect the available installation profiles:

```powershell
python -X utf8 scripts/install_codex_skills.py --list
```

Preview and install the full suite:

```powershell
python -X utf8 scripts/install_codex_skills.py <codex-skills-directory> --profile full --dry-run
python -X utf8 scripts/install_codex_skills.py <codex-skills-directory> --profile full
python -X utf8 scripts/install_codex_skills.py <codex-skills-directory> --profile full --verify
```

Open a new Codex task after installation and call `$knowledge-vault`. During initial setup, the skill interviews you, shows the proposed directory and files, and waits for write authorization before creating them.

Three profiles are available:

| Profile | Included workflow |
|---|---|
| `lightweight` | intake, atomic notes, and output |
| `growth` | lightweight plus learning, projects, and retrospectives |
| `full` | all 11 skills |

## Evidence and safety boundaries

- AI inferences are not recorded as confirmed facts.
- One success is not treated as stable capability.
- Published output does not become a source of truth by itself.
- Interests remain candidates until the vault owner commits to them.
- Self-observation is not diagnosis.
- No third-party Obsidian plugin is required.
- Without write authorization, the skills provide proposals and previews only.
- All public examples use fictional material.

The methods draw from knowledge provenance, atomic note-taking, human-centered design, deliberate practice, experiential learning, reflective practice, and structured communication. See the [theoretical foundations](docs/00-overview/theoretical-foundations.md) for sources and limits.

## Validation

```powershell
python -X utf8 scripts/run_checks.py
```

The automated suite checks repository contracts, links, evaluation cases, privacy scanning, installation, and minimum-vault creation. These checks do not claim that every live Codex behavior has been evaluated. See the [behavior evaluation guide](tests/evals/README.md).

This project is released under the [MIT License](LICENSE). Feedback and real-world usage reports are welcome through [GitHub Issues](https://github.com/bao-776/personal-knowledge-system-skills/issues).
