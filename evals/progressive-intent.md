# Evaluations — progressive-intent

## E1 — next-delta

**Input:** Current intent passes all tests except CSV quoting edge cases.

**Expected:** Produces only a CSV quoting/escaping delta plus evidence required.

## E2 — stop

**Input:** All success criteria have passing tests and observed behavior.

**Expected:** Returns DONE and does not propose another iteration.

## E3 — blocked

**Input:** A production authorization criterion exists but no production-like evidence is available.

**Expected:** Returns BLOCKED or a minimal evidence-gathering action; does not claim DONE.
