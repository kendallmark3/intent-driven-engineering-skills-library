---
name: intent-refiner
description: Refines rough feature requests into minimum-sufficient engineering intent with outcomes, inputs, outputs, success criteria, boundaries, and evidence. Use when a requirement is vague, conversational, implementation-heavy, or needs to become an intent file without over-specifying the solution.
---

# Intent Refiner

Convert a rough request into a clear, testable intent while preserving room for engineering reasoning.

## Workflow

1. Extract the human outcome. Do not substitute an implementation for the outcome.
2. Capture only relevant inputs/context already known.
3. Define observable outputs.
4. Write success criteria that can be verified.
5. Add constraints/boundaries only when they protect scope, policy, safety, compatibility, sequencing, side effects, or recovery.
6. State evidence required to prove completion.
7. Mark important unknowns as assumptions or open questions; do not silently invent facts.
8. Run an overwritten-intent check: remove prescriptions that are not required by the human intent or an actual constraint.

## Output

Use this shape:

```text
# Intent

## Outcome
...

## Inputs / Context
...

## Outputs
...

## Success Criteria
...

## Constraints / Boundaries
...

## Assumptions / Unknowns
...

## Evidence Required
...
```

## Guardrails

- Prefer goal-oriented wording.
- Do not prescribe framework, service, data store, class structure, agent topology, or implementation sequence unless justified.
- Preserve user-supplied constraints exactly when they matter.
- Do not make success criteria untestably vague.

See [EXAMPLES.md](EXAMPLES.md) for examples.
