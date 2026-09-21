#!/bin/bash
# auto-save — salva o Brain no git ao fim de toda sessao.
# Nunca falha a sessao: se der errado, avisa no log e segue.
set -u
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}" || exit 0

LOG=".claude/logs/auto-save.log"
mkdir -p .claude/logs
QUANDO="$(date '+%Y-%m-%d %H:%M')"

if [ -z "$(git status --porcelain 2>/dev/null)" ]; then
  echo "[$QUANDO] nada para salvar" >> "$LOG"
  exit 0
fi

git add -A >> "$LOG" 2>&1
git commit -q -m "auto-save: $QUANDO" >> "$LOG" 2>&1

# so tenta empurrar se existir um remoto configurado
if git remote get-url origin > /dev/null 2>&1; then
  if git push -q >> "$LOG" 2>&1; then
    echo "[$QUANDO] salvo e enviado para a nuvem" >> "$LOG"
  else
    echo "[$QUANDO] salvo no computador, mas o envio para a nuvem falhou" >> "$LOG"
  fi
else
  echo "[$QUANDO] salvo no computador (sem backup na nuvem ainda)" >> "$LOG"
fi
exit 0
