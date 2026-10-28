# How to Use the Intent-Driven Engineering Skills Library

## A feature from first thought to DONE

Assume the human says:

```text
Users should be able to export the current report as CSV.
```

### 1. Refine only enough intent

Invoke `intent-refiner`.

Expected shape:

```text
Intent
Allow a user viewing a report to export the currently displayed report data as CSV.

Inputs / Context
- Current report data and filters.
- Existing authorization rules.

Outputs
- A downloadable CSV representing the visible report data.

Success Criteria
- Export is available from the report UI.
- Exported rows match the current filtered report.
- CSV opens correctly in common spreadsheet tools.
- Unauthorized data is not included.

Constraints / Boundaries
- Preserve existing report authorization.
- Do not introduce a new export service unless evidence shows it is needed.

Evidence Required
- Passing tests for filtered export and authorization.
- Observed sample CSV containing expected rows and headers.
```

Notice what is intentionally absent: framework choice, class names, queueing, database changes, or a prescribed implementation sequence.

### 2. Implement

Let the engineering agent choose a reasonable implementation inside the stated boundaries.

### 3. Gather evidence

Run tests and inspect observable results. Keep raw evidence separate from interpretation.

Example:

```text
PASS: filtered export test
PASS: authorization test
FAIL: quoted commas produce malformed CSV
OBSERVED: UI button downloads file successfully
```

### 4. Check completion

Invoke `intent-completion-check`.

Because a success criterion is not satisfied, the result should be `NOT_DONE` and identify the smallest unresolved gap: CSV escaping/quoting correctness.

### 5. Generate only the next intent

Invoke `progressive-intent` with Intent V1 plus the new evidence.

A good next intent is small:

```text
Intent V2 delta
Ensure exported CSV correctly escapes fields containing commas, quotes, and line breaks.

Success Criteria delta
- CSV parser round-trip test passes for commas, quotes, and line breaks.

Evidence required
- Passing edge-case export test.
```

It should **not** redesign the export subsystem, introduce a queue, or refactor unrelated reporting code.

### 6. Build, test, observe again

Once the new evidence satisfies the remaining criteria, invoke `intent-completion-check` again.

Expected result:

```text
DONE
```

At that point, `progressive-intent` must stop. No new iteration is justified.

## When to use each skill

### `intent-refiner`
Use at the beginning when the request is rough, ambiguous, conversational, or overloaded with implementation ideas.

### `progressive-intent`
Use after at least one implementation/evidence cycle. It is the main iterative engine.

### `evidence-to-intent`
Use when there is a large pile of logs, tests, screenshots, review comments, or observations and you want to derive only supported changes.

### `intent-completion-check`
Use at gates: before another iteration, before merge/release, or when the agent appears to keep working after success.

### `intent-drift-check`
Use when the implementation is getting bigger than the request, when architecture expands, or when an agent starts adding speculative improvements.

### `enterprise-radius-review`
Use when the question becomes "where does this belong?", "who owns it?", or "is this production ready?"

### `proof-case-study-builder`
Use after delivery when packaging evidence for stakeholders, portfolios, architecture reviews, or case studies.

## Composition pattern

A strong default composition is:

```text
intent-refiner
    -> implementation
    -> evidence-to-intent (optional for noisy evidence)
    -> intent-completion-check
    -> progressive-intent (only if NOT_DONE)
    -> implementation
    -> intent-completion-check
    -> DONE
    -> proof-case-study-builder
```

Run `intent-drift-check` anywhere the scope starts expanding.
