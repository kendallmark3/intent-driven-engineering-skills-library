# Evaluations — evidence-to-intent

## E1 — noisy-evidence

**Input:** Mixed logs, two failing tests, one screenshot, and a reviewer hypothesis are supplied.

**Expected:** Separates fact from hypothesis and derives only supported changes.

## E2 — causality

**Input:** Endpoint is slow; no profiling exists.

**Expected:** Does not prescribe cache/database changes; requests/identifies needed evidence.

## E3 — contradiction

**Input:** One benchmark passes and another comparable run fails.

**Expected:** Marks contradiction and avoids a confident architectural conclusion.
