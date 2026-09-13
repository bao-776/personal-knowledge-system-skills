# Recovery protocol

Use this protocol when a workflow stops midway, a write fails, the user returns after an interruption, or the required child Skill is unavailable.

## Reconstruct the checkpoint

Report only verified state:

```text
Goal
Completed
Files created or updated
Current position
Unresolved decisions
Validation already run
Safest next action
```

- Read back written files before claiming completion.
- Do not repeat completed mutations merely because the conversation resumed.
- Separate an environment or tool failure from a content or reasoning failure.
- Preserve partial output when it is valid and label its status.
- If a routed child Skill is missing, name it and provide a limited proposal or installation instruction. Do not imitate a workflow whose essential rules are unavailable.
- Ask the user only when the missing decision changes scope, disclosure, irreversible action, or the meaning of maintained knowledge.

After recovery, continue from the first unverified step and report the new validation evidence.

