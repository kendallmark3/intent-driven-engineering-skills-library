# Evaluations — intent-drift-check

## E1 — material-drift

**Input:** CSV export feature now includes Excel export, a queue, a cache, and a generic export platform without evidence.

**Expected:** Marks unsupported additions as speculative/unrelated.

## E2 — justified-expansion

**Input:** Measured exports exceed platform timeout; async processing is proposed.

**Expected:** Can classify async change as justified if evidence and constraints support it.

## E3 — clean

**Input:** Implementation is narrow and directly satisfies intent.

**Expected:** Returns CLEAN and does not invent drift.
