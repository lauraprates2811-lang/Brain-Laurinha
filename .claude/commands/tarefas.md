---
description: Abre e opera a lista de tarefas por conversa
---

# /tarefas — a lista

Opera `Tarefas/dados/*.json` por conversa. **O JSON é a fonte de verdade** — nunca edite tarefa
direto no `STATUS.md` nem numa ficha.

## Ao abrir, mostre

1. **Vence hoje ou está atrasada** — em vermelho, primeiro
2. **Vence esta semana**
3. **Prioridade alta sem prazo**
4. Quantas tarefas abertas por área

Ordene por prazo e, com o mesmo prazo, por prioridade.

## O que a Laura pode pedir

| Ela diz | Você faz |
|---|---|
| "o que tenho hoje" | lista as de hoje e as atrasadas |
| "fecha a 6" | `status: "fechada"`, acrescenta `fechado: "AAAA-MM-DD"` |
| "adia a 14 para sexta" | muda `prazo`, registra o motivo em `notas` |
| "cria: ligar para o cursinho" | nova tarefa com o próximo `id`, pergunta área e prazo se não der para inferir |
| "o que vence antes da FGV" | filtra por data até 18/10/2026 |

## Regras

- Todo `id` é único e sequencial (`proximo_id` no topo do arquivo).
- `area` tem que existir em `areas.json`.
- Ao fechar uma tarefa que muda o estado de uma frente, **lembre a Laura de rodar `/save`**.
- Sempre que mexer, atualize `atualizado` no topo do `tarefas.json`.
- Valide o JSON depois de escrever:
  `python3 -c "import json;json.load(open('Tarefas/dados/tarefas.json'))"`
