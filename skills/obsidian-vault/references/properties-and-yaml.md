# Properties and YAML

Use stable keys and valid YAML. Quote values containing `#`, colons, brackets, links, or ambiguous dates. Prefer block lists for complex values. Do not mix document lifecycle status with domain-specific progress states.

Validate parsing after edits. Keep essential meaning readable in plain Markdown. Use `sources` for a list of evidence locators; accept legacy `source` on read rather than bulk-migrating it. Keep document `status` (draft, needs-review, active, stale, superseded, archived) separate from `project_status`, `learning_status`, `candidate_status`, and verification state. Reuse local equivalents and document a mapping when needed. Review dates flag a need to check, not automatic falsity; archive only after confirming replacement and preserving links.
