---
name: progressive-intent
description: Advances a feature through evidence-driven intent iterations by reading the current intent, implementation results, tests, observations, and evidence, then proposing only the minimum sufficient next delta. Use after an implementation cycle when deciding what the next intent should be or whether the feature is already done.
---

# Progressive Intent

Advance the work only as far as the evidence justifies.

> **Hard rule: No new intent without new evidence.**

> **Stop rule: If the current success criteria are satisfied with sufficient evidence, stop. Do not invent another iteration.**

## Required inputs

Read, when available:

- the original/current intent;
- prior intent deltas and decisions;
- the current implementation or change summary;
- test results;
- observed runtime/user behavior;
- logs, screenshots, benchmarks, review comments, or other evidence;
- unresolved success criteria, constraints, and known blockers.

Do not require every evidence type. Use what exists and label what is missing.

## Workflow

1. **Re-anchor on the original human outcome.** Preserve it as the controlling objective.
2. **Inventory new evidence.** Separate observed facts from interpretations.
3. **Map evidence to success criteria.** Mark each criterion `SATISFIED`, `UNSATISFIED`, or `UNKNOWN`.
4. **Run the completion gate.** If all required criteria are sufficiently evidenced, output `DONE` and stop.
5. **Find the smallest material gap.** Prefer the narrowest gap blocking completion or confidence.
6. **Generate a delta, not a replacement spec.** Add only what the evidence now proves is necessary.
7. **Define evidence for the delta.** Say how the next iteration will prove or disprove it.
8. **Run the drift check.** Remove speculative features, refactors, dependencies, architecture, or constraints not justified by the evidence.
9. **Preserve traceability.** State which evidence item caused each new intent addition.

## Output

If complete:

```text
Status: DONE
Reason: <how evidence satisfies the success criteria>
Remaining unknowns: <none, or non-blocking items explicitly outside scope>
```

If another iteration is justified:

```text
Status: NEXT_INTENT

Evidence considered
- ...

Unresolved gap
- ...

Intent delta
- ...

Success criteria delta
- ...

Evidence required next
- ...

Not added
- <tempting but unsupported scope/architecture intentionally excluded>
```

If evidence is insufficient to choose responsibly:

```text
Status: BLOCKED
Missing evidence
- ...
Why it matters
- ...
Smallest action to obtain it
- ...
```

## What not to do

- Do not rewrite the whole feature specification every cycle.
- Do not add "nice to have" work merely because it is nearby.
- Do not convert test failure into a broad refactor unless evidence shows the broader change is required.
- Do not keep iterating after success criteria are met.
- Do not treat an agent's confidence statement as evidence.

See [EXAMPLES.md](EXAMPLES.md) for representative progressions.
