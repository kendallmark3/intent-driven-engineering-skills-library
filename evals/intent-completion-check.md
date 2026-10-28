# Evaluations — intent-completion-check

## E1 — done

**Input:** All required criteria have evidence and boundaries are respected.

**Expected:** Returns DONE.

## E2 — not-done

**Input:** One required acceptance test fails.

**Expected:** Returns NOT_DONE and names the smallest gap.

## E3 — blocked

**Input:** A criterion cannot be verified because access is unavailable.

**Expected:** Returns BLOCKED and names the smallest evidence action.
