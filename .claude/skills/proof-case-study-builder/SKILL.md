---
name: proof-case-study-builder
description: Builds concise case studies from delivery evidence while separating Observed, Measured, and Proposed claims and refusing to invent proof. Use when documenting what was built, preparing a portfolio or stakeholder case study, publishing proof, or turning project artifacts into an evidence-grounded narrative.
---

# Proof Case Study Builder

Turn delivery artifacts into a credible case study without inflating claims.

## Claim types

- **Observed** — directly seen in code, screenshots, logs, demos, artifacts, or behavior.
- **Measured** — supported by an actual metric, benchmark, count, timing, cost, test result, or other quantitative evidence.
- **Proposed** — an interpretation, projected benefit, future use, or recommendation not yet proven.

Never upgrade a Proposed claim into Measured or Observed.

## Workflow

1. Identify the original problem and intended outcome.
2. Summarize the delivered capability.
3. Catalog evidence and label each claim type.
4. Explain the key engineering/architecture choices only where supported by artifacts or stated rationale.
5. State limitations and remaining unknowns.
6. Present business value as measured only when measurement exists; otherwise label it Proposed.

## Output

```text
# Case Study

## Problem
...

## Intent
...

## What Was Built
...

## Evidence
### Observed
- ...
### Measured
- ...
### Proposed
- ...

## Key Decisions
...

## Limitations / Unknowns
...

## Next Proof
...
```
