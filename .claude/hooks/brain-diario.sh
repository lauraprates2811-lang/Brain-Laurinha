#!/bin/bash
# brain-diario — varredura do fim do dia.
#
# Salva o que estiver pendente, varre as mudancas do dia no git e escreve
# um resumo tecnico em .claude/logs/diario-AAAA-MM.md.
#
# Nao substitui o /sono: aqui e so o registro do que mudou nos arquivos.
# O /sono e a consolidacao pensada do dia, feita com a Laura.
#
# Agendado pelo launchd, todo dia 23:50. Instale com Projetos/Brain/instalar-rotina.sh
set -u

BRAIN="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$BRAIN" || exit 1
mkdir -p .claude/logs

HOJE="$(date +%Y-%m-%d)"
AGORA="$(date '+%H:%M')"
DIARIO=".claude/logs/diario-$(date +%Y-%m).md"

avisar() {
  osascript -e "display notification \"$1\" with title \"Brain\"" 2>/dev/null || true
}

# 1. salva o que ficou solto, para a varredura enxergar tudo
if [ -n "$(git status --porcelain 2>/dev/null)" ]; then
  git add -A > /dev/null 2>&1
  git commit -q -m "diario: fechamento de $HOJE" > /dev/null 2>&1
fi

# 2. o que mudou hoje
COMMITS="$(git log --since="$HOJE 00:00" --until="$HOJE 23:59" --pretty='- %h %s' 2>/dev/null)"

if [ -z "$COMMITS" ]; then
  printf '\n## %s\n\nNada mudou no Brain hoje.\n' "$HOJE" >> "$DIARIO"
  exit 0
fi

N_COMMITS="$(printf '%s\n' "$COMMITS" | grep -c .)"
ARQUIVOS="$(git log --since="$HOJE 00:00" --until="$HOJE 23:59" \
              --name-status --pretty=format: 2>/dev/null \
            | grep -E '^[AMDR]' | sort -u -k2)"
N_ARQ="$(printf '%s\n' "$ARQUIVOS" | grep -c .)"

# 3. escreve o resumo
{
  printf '\n## %s\n\n' "$HOJE"
  printf 'Fechado as %s · %s versao(oes) salva(s) · %s arquivo(s) tocado(s).\n\n' \
         "$AGORA" "$N_COMMITS" "$N_ARQ"
  printf '**Arquivos que mudaram**\n\n'
  printf '%s\n' "$ARQUIVOS" | sed 's/^A\t/- criado: /; s/^M\t/- alterado: /; s/^D\t/- apagado: /; s/^R[0-9]*\t/- renomeado: /'
  printf '\n**Versoes salvas**\n\n'
  printf '%s\n' "$COMMITS"
} >> "$DIARIO"

# 4. estado do formato, so para constar
python3 .claude/hooks/brain-lint.py --stop-hook > /dev/null 2>&1 \
  || printf '\n> O guardiao achou erro de formato. Abra o Claude e rode /otimizar.\n' >> "$DIARIO"

avisar "Dia fechado: $N_ARQ arquivo(s) mudaram. Falta o /sono."
exit 0
