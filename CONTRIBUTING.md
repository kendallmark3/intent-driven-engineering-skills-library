# Contributing

A new Skill should earn its place by solving a repeated, observable failure mode.

Before adding one:

1. Show the representative task where the agent struggles or repeatedly needs the same guidance.
2. Explain why an existing Skill cannot handle it cleanly.
3. Define trigger language and non-trigger cases.
4. Keep `SKILL.md` concise and move optional depth to adjacent files.
5. Add at least three representative evaluations.
6. Run `python scripts/validate_skills.py`.
7. Review the change for unnecessary prescription, overlap, and security implications.

Do not add a Skill merely because a prompt could exist for it.
