#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS="$ROOT/.claude/skills"
DIST="$ROOT/dist"
mkdir -p "$DIST"
rm -f "$DIST"/*.zip
for dir in "$SKILLS"/*; do
  [ -d "$dir" ] || continue
  name="$(basename "$dir")"
  (
    cd "$SKILLS"
    zip -qr "$DIST/$name.zip" "$name"
  )
  echo "Built dist/$name.zip"
done
