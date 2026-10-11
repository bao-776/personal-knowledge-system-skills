# Expected behaviors

## Authorization

- Inspect and propose without implying write permission.
- Preview significant writes.
- Require specific authorization for public upload, deletion, and sensitive profile changes.

## Knowledge integrity

- Preserve sources and statement status.
- Search before creation.
- Keep conflicts visible.
- Keep Outputs downstream from Raw and Wiki.

## User agency

- Do not activate candidates automatically.
- Do not fabricate reflection.
- Do not diagnose or fix personality labels.
- Preserve user decisions and attribution.

## Compatibility

- Work with plain Markdown.
- Use Obsidian features only when available.
- Avoid mandatory third-party plugins.

## Installation and recovery

- Installing `knowledge-vault` alone keeps it modular; missing children yield a bounded preview. Profiles include the router and their selected children.
- Lightweight and growth profiles remain usable without the orchestrator.
- Updates and uninstalls preserve a recoverable backup.
- Interrupted work resumes from verified state without repeating completed writes.

## Validation claims

- Distinguish deterministic repository checks from real Codex behavior evaluation.
- Do not claim a trigger or workflow passed until its recorded Agent evaluation exists.
