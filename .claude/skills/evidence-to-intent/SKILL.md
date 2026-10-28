---
name: evidence-to-intent
description: Classifies tests, logs, screenshots, benchmarks, reviews, and runtime observations into evidence states and derives only the intent changes justified by them. Use when evidence is noisy, mixed, contradictory, or large enough that the next engineering action is unclear.
---

# Evidence to Intent

Turn raw evidence into justified changes without expanding scope.

## Workflow

1. Normalize each evidence item as `OBSERVED`, `MEASURED`, `REPORTED`, or `UNKNOWN`.
2. Mark result state as `PASS`, `FAIL`, `PARTIAL`, `CONTRADICTORY`, or `NOT_APPLICABLE` where meaningful.
3. Link each item to the success criterion or constraint it informs.
4. Distinguish a symptom from a demonstrated cause.
5. Identify the smallest supported change.
6. State what additional evidence is needed when causality or scope is uncertain.
7. Reject proposed changes that have no supporting evidence.

## Output

```text
Evidence table
- E1 | OBSERVED | PASS | <criterion> | <fact>
- E2 | MEASURED | FAIL | <criterion> | <fact>

Supported intent changes
- ...

Unsupported / premature changes
- ...

Missing evidence
- ...
```

See [EXAMPLES.md](EXAMPLES.md).
