# Library Map

## Core feature loop

- `intent-refiner` — establish V1.
- `progressive-intent` — generate evidence-driven deltas.
- `intent-completion-check` — decide whether iteration should continue.
- `intent-drift-check` — protect original intent from unnecessary expansion.
- `evidence-to-intent` — normalize noisy evidence into justified changes.

## Enterprise extension

- `enterprise-radius-review` — determine radius, ownership, governance, and production readiness.
- `proof-case-study-builder` — package delivery evidence without inflating claims.

## Authority model

```text
Human  -> declares outcomes, boundaries, success criteria
Agent  -> reasons about implementation and next actions
System -> verifies through tests, policy, telemetry, and evidence
```

Skills should reinforce this boundary rather than collapse it.
