#!/bin/bash
# auto-save — mantem o Brain igual no Mac, no GitHub e no Claude do celular.
#   sem argumento: fim de toda resposta. Salva, traz o que veio do celular e envia.
#   inicio: comeco de toda sessao. Traz o que veio do celular antes de ler qualquer coisa.
# No celular (sessao na nuvem, CLAUDE_CODE_REMOTE=true) o Claude so pode enviar para o ramo
# da propria sessao; por isso, depois de enviar, ele junta esse ramo ao main pela API do GitHub.
# Se isso falhar, o Mac junta o ramo quando ligar (plano B em puxar).
# Nunca falha a sessao: se der errado, avisa no log e segue.
set -u
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}" || exit 0

LOG=".claude/logs/auto-save.log"
mkdir -p .claude/logs
QUANDO="$(date '+%Y-%m-%d %H:%M')"
NUVEM="${CLAUDE_CODE_REMOTE:-false}"

log() { echo "[$QUANDO] $1" >> "$LOG"; }
tem_remoto() { git remote get-url origin > /dev/null 2>&1; }
a_frente() { git rev-list --count "origin/main..HEAD" 2>/dev/null || echo 1; }

# Mac: traz o main do GitHub e os ramos do celular que nao chegaram ao main
puxar() {
  tem_remoto || return 0
  if ! git pull -q --rebase --autostash origin main >> "$LOG" 2>&1; then
    git rebase --abort > /dev/null 2>&1
    log "conflito ao trazer o main do GitHub; ficou tudo como estava"
    echo "Aviso do auto-save: nao consegui trazer o main do GitHub (conflito). Rode git pull --rebase origin main e resolva antes de editar."
    return 0
  fi
  git fetch -q origin '+refs/heads/claude/*:refs/remotes/origin/claude/*' >> "$LOG" 2>&1
  for r in $(git branch -r --no-merged HEAD 2>/dev/null | grep 'origin/claude/'); do
    if git merge -q --no-edit "$r" >> "$LOG" 2>&1; then
      log "juntei $r (veio do celular)"
    else
      git merge --abort > /dev/null 2>&1
      log "conflito ao juntar $r; ficou para depois"
      echo "Aviso do auto-save: o ramo $r (mudancas feitas pelo celular) tem conflito com o main e nao foi juntado. Junte a mao com git merge $r, resolvendo o conflito."
    fi
  done
}

# celular: poe o ramo da sessao em dia com o main
atualizar_ramo() {
  git fetch -q origin main >> "$LOG" 2>&1 || return 0
  if ! git merge -q --no-edit origin/main >> "$LOG" 2>&1; then
    git merge --abort > /dev/null 2>&1
    log "conflito com o main; o Mac junta este ramo quando ligar"
  fi
}

enviar_do_mac() {
  puxar
  if git push -q origin HEAD:main >> "$LOG" 2>&1; then
    log "salvo e enviado para a nuvem"
  else
    log "salvo no computador, mas o envio para a nuvem falhou"
  fi
}

enviar_da_nuvem() {
  RAMO="$(git rev-parse --abbrev-ref HEAD)"
  atualizar_ramo
  if ! git push -q -u origin HEAD >> "$LOG" 2>&1; then
    log "envio do ramo $RAMO falhou"
    return 0
  fi
  REPO="$(git remote get-url origin | sed -E 's#\.git$##; s#^.*[:/]([^/]+/[^/]+)$#\1#')"
  if gh api -X POST "repos/$REPO/merges" -f base=main -f head="$RAMO" \
       -f commit_message="celular: $QUANDO" >> "$LOG" 2>&1; then
    log "enviado do celular e juntado ao main"
  else
    log "enviado no ramo $RAMO; o Mac junta ao main quando ligar"
  fi
}

if [ "${1:-}" = "inicio" ]; then
  if [ "$NUVEM" = "true" ]; then atualizar_ramo; else puxar; fi
  exit 0
fi

if [ -n "$(git status --porcelain 2>/dev/null)" ]; then
  git add -A >> "$LOG" 2>&1
  git commit -q -m "auto-save: $QUANDO" >> "$LOG" 2>&1
elif [ "$(a_frente)" = "0" ]; then
  log "nada para salvar"
  exit 0
fi

if ! tem_remoto; then
  log "salvo no computador (sem backup na nuvem ainda)"
elif [ "$NUVEM" = "true" ]; then
  enviar_da_nuvem
else
  enviar_do_mac
fi
exit 0
