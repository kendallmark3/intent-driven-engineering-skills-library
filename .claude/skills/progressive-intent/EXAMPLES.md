# Examples

## Example 1 — One failing edge case

Current intent: export filtered report as valid CSV.

Evidence:
- filtered rows: PASS
- authorization: PASS
- download behavior: OBSERVED PASS
- quoted comma field: FAIL

Good next intent:

```text
Ensure exported CSV correctly escapes fields containing commas, quotes, and line breaks.
```

Bad next intent:

```text
Create a distributed export service, add a queue, refactor reporting, and add Excel export.
```

## Example 2 — Already done

Evidence satisfies every current success criterion. Return `DONE`. Do not add performance work, cleanup, or future features unless they were part of the stated criteria.

## Example 3 — Missing evidence

If a criterion requires authorization proof but no authorization test or observation exists, return `BLOCKED` or a minimal validation intent instead of claiming success.
