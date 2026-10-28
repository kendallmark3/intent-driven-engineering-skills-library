# Intent-Driven Engineering — Repository Guidance

This repository contains reusable Agent Skills. Treat the Skill files as governed instructions inside the repository trust boundary.

## Operating rules

- Prefer outcomes and success criteria over implementation prescription.
- Add constraints only when they protect a boundary, ordering requirement, side effect, safety property, recovery path, or acceptance criterion.
- Do not create a new intent iteration unless new evidence justifies it.
- Preserve the original human intent and make deltas explicit.
- Separate observations from interpretations.
- Stop when success criteria are satisfied with sufficient evidence.
- When implementation exceeds stated intent, call out drift instead of normalizing it.
- Never invent measurements, test results, screenshots, logs, approvals, or business outcomes.
- Treat `Observed`, `Measured`, and `Proposed` as different claim types.

## Skill authoring

- Keep `SKILL.md` concise.
- Put optional depth in adjacent reference/example files and link them from `SKILL.md`.
- Use specific third-person descriptions that state what the Skill does and when it should trigger.
- Keep skill names lowercase with letters, numbers, and hyphens.
- Add representative evaluations before expanding a Skill.
