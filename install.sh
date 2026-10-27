#!/usr/bin/env bash
# Synk Skills: instalador para macOS e Linux
# Uso: curl -fsSL https://raw.githubusercontent.com/kalango99/synk-skills/main/install.sh | bash
set -euo pipefail
REPO="https://github.com/kalango99/synk-skills/archive/refs/heads/main.tar.gz"
DESTINO="$HOME/.claude/skills"
TMP="$(mktemp -d)"

echo "Baixando as Synk Skills..."
mkdir -p "$DESTINO"
curl -fsSL "$REPO" | tar -xz -C "$TMP"
ORIGEM="$(find "$TMP" -maxdepth 2 -type d -name skills | head -1)"

for skill in "$ORIGEM"/*/; do
  nome="$(basename "$skill")"
  rm -rf "${DESTINO:?}/$nome"
  cp -R "$skill" "$DESTINO/$nome"
  echo "  ok  $nome"
done
rm -rf "$TMP"

echo ""
echo "Pronto. Skills instaladas em $DESTINO"
echo "Feche e abra o Claude Code para ele enxergar as skills novas."
