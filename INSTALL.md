# Installation

## Option 1 — Use inside a Claude Code project

This repository already uses Claude Code's project Skill layout:

```text
.claude/skills/<skill-name>/SKILL.md
```

### New project

1. Unzip or clone this repository.
2. Work from the repository root in Claude Code.
3. Run `/skills` to verify the skills are visible.
4. Ask naturally for a matching workflow, for example:

```text
Use Progressive Intent on this feature. Read the current intent, implementation, tests, and evidence and propose only the next justified delta.
```

### Existing project

Copy the desired folders from:

```text
.claude/skills/
```

into your project's:

```text
<your-project>/.claude/skills/
```

Example:

```bash
mkdir -p .claude/skills
cp -R /path/to/intent-driven-engineering-skills-library/.claude/skills/progressive-intent .claude/skills/
```

Restart the Claude Code session if needed, then run `/skills`.

## Option 2 — Install for all Claude Code projects

Copy one or more skill folders to your personal Skill directory:

```bash
mkdir -p ~/.claude/skills
cp -R .claude/skills/progressive-intent ~/.claude/skills/
cp -R .claude/skills/intent-refiner ~/.claude/skills/
```

Then start a new Claude Code session and run `/skills`.

## Option 3 — Upload to Claude.ai

Claude.ai accepts custom Skill ZIPs.

1. Run `./scripts/package-skills.sh`, or use the prebuilt ZIPs in `dist/`.
2. In Claude.ai, open **Customize > Skills**.
3. Choose **Create skill** / **Upload a skill**.
4. Upload one ZIP, such as `progressive-intent.zip`.
5. Enable it.
6. Test it with several prompts that should and should not trigger it.

The ZIP must contain the skill directory as its top-level folder:

```text
progressive-intent.zip
└── progressive-intent/
    ├── SKILL.md
    └── EXAMPLES.md
```

## Recommended first install

Start with these four:

```text
intent-refiner
progressive-intent
intent-completion-check
intent-drift-check
```

Add `evidence-to-intent` when you want a dedicated evidence-processing step. Add the Radius and proof skills when architecture/governance and proof packaging are relevant.

## Security review before installation

Skills are instructions inside the agent's trust boundary. Before installing any third-party Skill:

- Read `SKILL.md` fully.
- Inspect scripts and commands.
- Look for network access, credential handling, package installation, destructive operations, or external uploads.
- Verify that referenced files are expected and local.
- Version-control changes to shared Skills.

This library intentionally contains no network-calling or destructive scripts.
