# Tarefas

A lista do que fazer. **A fonte de verdade são os arquivos em `dados/`** — não edite tarefa
direto no `STATUS.md` nem numa ficha.

| Arquivo | O que guarda |
|---|---|
| `dados/tarefas.json` | Toda tarefa: título, área, prazo, prioridade, status |
| `dados/areas.json` | As áreas do Brain e quando cada ficha foi atualizada |
| `dados/prazos.json` | As datas sem volta, extraídas do `Calendario.md` |

## Como usar

Digite `/tarefas` e converse: "o que tenho para hoje", "o que vence essa semana",
"fecha a 6", "adia a 14 para sexta", "cria uma tarefa de X".

## Campos de uma tarefa

- `status`: `aberta` · `fazendo` · `fechada` · `cancelada`
- `prioridade`: `alta` · `media` · `baixa`
- `area`: tem que existir em `areas.json`
- `prazo`: `AAAA-MM-DD`, ou `null` quando não houver
