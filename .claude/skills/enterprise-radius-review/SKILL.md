---
name: enterprise-radius-review
description: Reviews an AI or software initiative across five enterprise Radius levels—Intent & Discovery, Prototype & Proof, Engineering & Integration, Delivery & Production, and Enterprise Operation & Governance—and identifies ownership, gaps, and evidence. Use for architecture reviews, production-readiness questions, ownership boundaries, or when asking where a capability belongs.
---

# Enterprise Radius Review

Review how far an initiative must extend and who owns what.

## Radius levels

1. **Intent & Discovery** — problem, outcome, stakeholders, value, success criteria.
2. **Prototype & Proof** — proof of feasibility, workflows, models/agents/tools, evidence.
3. **Engineering & Integration** — services, APIs, data, repositories, testing, architecture.
4. **Delivery & Production** — environments, CI/CD, IAM, secrets, networking, observability, release/rollback, resiliency.
5. **Enterprise Operation & Governance** — shared services, security, compliance, model/cost governance, registries, audit, support, incidents, standards, ownership.

## Workflow

1. Identify the requested/actual radius.
2. State what evidence exists at each level.
3. Identify the first material gap preventing movement outward.
4. Assign likely ownership by responsibility, not by guessing named teams.
5. Separate human authority, agent reasoning, and system-enforced controls.
6. Avoid demanding Radius 5 controls for a Radius 1 exploration unless risk requires them.

## Output

```text
Current radius: R#
Target radius: R#

Evidence by radius
R1 ...
R2 ...
R3 ...
R4 ...
R5 ...

Ownership boundaries
- ...

First material gap
- ...

Recommended next evidence
- ...
```

See [EXAMPLES.md](EXAMPLES.md).
