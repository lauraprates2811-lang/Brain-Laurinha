# Brain

> **Status:** Criado em 21/09/2026. Estrutura, 6 áreas, 7 agentes de estudo, 4 rituais e o
> guardião `brain-lint` no ar. Falta a Laura usar de verdade e conectar o backup na nuvem.

## O que é

O próprio sistema: a pasta, as regras, os comandos e a automação. Esta área existe para registrar
mudanças **no Brain**, separadas das mudanças na vida da Laura.

### O que existe

| Parte | Onde |
|---|---|
| Regras de operação | `CLAUDE.md` |
| Painel | `STATUS.md` · `STATUS-historico.md` |
| Linha do tempo | `Calendario.md` |
| Fichas de área | `Areas/` |
| Memória diária | `Memoria/` |
| Lista de tarefas | `Tarefas/dados/*.json` |
| Regras e decisões | `Regras/` |
| Agentes de estudo | `.claude/commands/` + doc em `Agentes/` |
| Guardião de formato | `.claude/hooks/brain-lint.py` |
| Rotina automática | `.claude/hooks/brain-rotina.sh` (launchd, segunda 07:00) |
| Como usar | `Projetos/Brain/ComoUsar.md` |

## Pendências

- [ ] Criar conta no GitHub e conectar o repositório **privado** para backup na nuvem
- [ ] Configurar `git config user.email` com o e-mail real da Laura (hoje é um placeholder)
- [ ] Instalar a rotina automática de segunda-feira no MacBook dela (`instalar-rotina.sh`)
- [ ] Abrir a pasta no Obsidian como cofre e conferir o grafo
- [ ] Preencher os blocos da entrevista que ficaram de fora (projetos pessoais, ferramentas)

## Regras da área

- Mudança de estrutura só entra depois do ok da Laura. Arquivo novo dentro do padrão, pode.
- Todo erro apontado pelo `brain-lint` é corrigido antes de encerrar a sessão.

## Projeções

*(preenchido pelo `/sono`)*

## Histórico (últimas entradas)

| Data | O que aconteceu | Resultado |
|---|---|---|
| 2026-09-21 | Brain criado do zero a partir da entrevista e do edital da FGV | Estrutura no ar |

## 🔗 Relacionados

[[STATUS]] · [[Calendario]] · [[Laura]] · [[Brain-projeto]]
