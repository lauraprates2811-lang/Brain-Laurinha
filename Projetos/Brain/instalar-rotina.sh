#!/bin/bash
# instalar-rotina.sh — liga a rotina automatica do Brain neste Mac.
# Roda UMA VEZ por computador. Pode rodar de novo sem problema.
set -eu

BRAIN="$(cd "$(dirname "$0")/../.." && pwd)"
AGENTES="$HOME/Library/LaunchAgents"
mkdir -p "$AGENTES" "$BRAIN/.claude/logs"

echo "Brain encontrado em: $BRAIN"
echo

fazer_plist() {  # nome, argumento, hora, minuto, [dia-da-semana]
  local NOME="$1" ARG="$2" HORA="$3" MIN="$4" DIA="${5:-}"
  local PLIST="$AGENTES/$NOME.plist"
  local QUANDO="        <key>Hour</key><integer>$HORA</integer>
        <key>Minute</key><integer>$MIN</integer>"
  [ -n "$DIA" ] && QUANDO="        <key>Weekday</key><integer>$DIA</integer>
$QUANDO"

  cat > "$PLIST" <<PLISTEOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key><string>$NOME</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>$BRAIN/.claude/hooks/brain-rotina.sh</string>
        <string>$ARG</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
$QUANDO
    </dict>
    <key>WorkingDirectory</key><string>$BRAIN</string>
    <key>StandardOutPath</key><string>$BRAIN/.claude/logs/launchd-$ARG.log</string>
    <key>StandardErrorPath</key><string>$BRAIN/.claude/logs/launchd-$ARG.log</string>
</dict>
</plist>
PLISTEOF

  launchctl unload "$PLIST" 2>/dev/null || true
  launchctl load "$PLIST"
  echo "  ok: $NOME"
}

# Weekday 1 = segunda-feira
fazer_plist "com.laura.brain.otimizar" otimizar 7 0 1
fazer_plist "com.laura.brain.lint"     lint     9 0

echo
echo "Pronto. A partir de agora, sozinho:"
echo "  - toda SEGUNDA as 07:00, o Brain se reorganiza (/otimizar)"
echo "  - todo dia as 09:00, ele confere o formato e so avisa se houver erro"
echo
echo "Se o Mac estiver dormindo na hora, o launchd roda assim que ele acordar."
echo "Para desligar:  launchctl unload ~/Library/LaunchAgents/com.laura.brain.*.plist"
