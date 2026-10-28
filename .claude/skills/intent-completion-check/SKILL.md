---
name: intent-completion-check
description: Determines whether an intent is DONE, NOT_DONE, or BLOCKED by comparing its success criteria and constraints with available tests and observed evidence. Use before another iteration, merge, release, handoff, or whenever an agent may be continuing work after the requested outcome is already satisfied.
---

# Intent Completion Check

Decide whether the work should stop.

## Workflow

1. Read the controlling intent and success criteria.
2. Map concrete evidence to each required criterion.
3. Verify constraints/boundaries were not violated.
4. Do not count plans, claims, code existence, or agent confidence as proof by themselves.
5. Return exactly one status:
   - `DONE` — required criteria are sufficiently evidenced and boundaries are respected.
   - `NOT_DONE` — at least one required criterion is demonstrated unmet.
   - `BLOCKED` — completion cannot be determined because critical evidence or access is missing.
6. For `NOT_DONE`, identify the smallest unresolved gap.
7. For `BLOCKED`, identify the smallest evidence-gathering action.

## Output

```text
Status: DONE | NOT_DONE | BLOCKED

Criteria
- C1: SATISFIED — <evidence>
- C2: UNSATISFIED — <evidence>
- C3: UNKNOWN — <missing evidence>

Boundary check
- ...

Smallest next gap/action
- ...
```
