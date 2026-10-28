---
name: intent-drift-check
description: Compares the original human intent with the current implementation and proposed work to detect unnecessary architecture, speculative features, premature abstractions, invented constraints, and unrelated refactors. Use when scope is expanding, complexity is increasing, or an agent may be overwriting the human intent.
---

# Intent Drift Check

Protect the original human outcome from unearned complexity.

## Compare

- original human intent;
- explicit constraints and success criteria;
- current implementation;
- proposed next work;
- evidence that allegedly justifies expansion.

## Classify additions

For each meaningful addition, mark:

- `REQUIRED` — directly required by intent, constraint, or evidence;
- `JUSTIFIED` — not originally stated but supported by new evidence;
- `SPECULATIVE` — plausible but unsupported;
- `UNRELATED` — outside the current feature intent.

Pay special attention to:

- new services or microservices;
- queues, caches, databases, or infrastructure;
- new agents/subagents;
- framework migrations;
- generalized abstractions;
- broad refactors;
- adjacent features;
- invented nonfunctional requirements.

## Output

```text
Drift assessment: CLEAN | MINOR_DRIFT | MATERIAL_DRIFT

Required / justified
- ...

Speculative / unrelated
- ...

Recommended rollback of scope
- ...

Evidence that would justify expansion later
- ...
```
