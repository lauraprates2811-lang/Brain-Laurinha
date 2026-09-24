#!/bin/bash
# brain-rotina — a rotina automatica do Brain.
#
#   brain-rotina.sh lint       confere a forma; so avisa se houver ERRO   (todo dia 09:00)
#   brain-rotina.sh otimizar   roda o /otimizar sozinho                   (segunda 07:00)
#
# Agendado pelo launchd. Instale com Projetos/Brain/instalar-rotina.sh
set -u

BRAIN="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$BRAIN" || exit 1

# o launchd roda com um ambiente minimo: ensine onde mora o claude
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"
# sem USER o claude nao acha o login guardado no chaveiro
export USER="${USER:-$(id -un)}"
export LOGNAME="${LOGNAME:-$USER}"
mkdir -p .claude/logs
LOG=".claude/logs/rotina-$(date +%Y-%m).log"
QUANDO="$(date '+%Y-%m-%d %H:%M')"

avisar() {  # titulo, mensagem
  osascript -e "display notification \"$2\" with title \"$1\"" 2>/dev/null || true
}

case "${1:-}" in
  lint)
    echo "[$QUANDO] lint diario" >> "$LOG"
    SAIDA="$(python3 .claude/hooks/brain-lint.py 2>&1)"
    echo "$SAIDA" >> "$LOG"
    if echo "$SAIDA" | grep -q "^  x "; then
      N=$(echo "$SAIDA" | grep -c "^  x ")
      avisar "Brain" "$N erro(s) de formato. Abra o Claude e rode /otimizar."
    fi
    ;;

  otimizar)
    echo "[$QUANDO] otimizacao semanal" >> "$LOG"
    if ! command -v claude > /dev/null 2>&1; then
      echo "[$QUANDO] claude nao encontrado no PATH" >> "$LOG"
      avisar "Brain" "Nao consegui rodar a otimizacao: Claude Code nao encontrado."
      exit 1
    fi

    # acceptEdits libera editar arquivo, mas nao rodar comando.
    # O /otimizar precisa do guardiao: liberado nominalmente, so ele.
    claude -p "/otimizar" --permission-mode acceptEdits \
      --allowedTools "Bash(python3 .claude/hooks/brain-lint.py:*)" >> "$LOG" 2>&1
    SAIDA="$(python3 .claude/hooks/brain-lint.py 2>&1)"
    echo "$SAIDA" >> "$LOG"

    git add -A >> "$LOG" 2>&1
    git commit -q -m "otimizacao semanal: $QUANDO" >> "$LOG" 2>&1
    if git remote get-url origin > /dev/null 2>&1; then
      git pull -q --rebase origin main >> "$LOG" 2>&1 || git rebase --abort > /dev/null 2>&1
      git push -q >> "$LOG" 2>&1
    fi

    if echo "$SAIDA" | grep -q "^  x "; then
      avisar "Brain" "Otimizacao rodou, mas sobraram erros. Abra o Claude."
    else
      avisar "Brain" "Otimizacao semanal concluida. Tudo limpo."
    fi
    ;;

  *)
    echo "uso: brain-rotina.sh lint | otimizar"
    exit 1
    ;;
esac
