#!/usr/bin/env python3
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / '.claude' / 'skills'
NAME_RE = re.compile(r'^[a-z0-9-]{1,64}$')
FRONT_RE = re.compile(r'^---\n(.*?)\n---\n', re.S)
REF_RE = re.compile(r'\[[^\]]+\]\(([^)]+\.md)\)')
errors = []

for folder in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
    skill = folder / 'SKILL.md'
    if not skill.exists():
        errors.append(f'{folder.name}: missing SKILL.md')
        continue
    text = skill.read_text()
    m = FRONT_RE.match(text)
    if not m:
        errors.append(f'{folder.name}: missing YAML frontmatter')
        continue
    meta = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            k,v = line.split(':',1)
            meta[k.strip()] = v.strip()
    name = meta.get('name','')
    desc = meta.get('description','')
    if name != folder.name:
        errors.append(f'{folder.name}: frontmatter name {name!r} does not match folder')
    if not NAME_RE.match(name):
        errors.append(f'{folder.name}: invalid name')
    if not desc or len(desc) > 1024:
        errors.append(f'{folder.name}: description must be 1..1024 chars')
    if len(text.splitlines()) > 500:
        errors.append(f'{folder.name}: SKILL.md exceeds 500 lines')
    for ref in REF_RE.findall(text):
        target = folder / ref
        if not target.exists():
            errors.append(f'{folder.name}: missing referenced file {ref}')

if errors:
    print('Validation FAILED')
    for e in errors: print(' -', e)
    sys.exit(1)
print(f'Validation PASSED: {len(list(SKILLS.iterdir()))} skills')
