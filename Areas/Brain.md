# Brain

> **Status:** Instalado no MacBook da Laura em 22/09/2026, com backup privado no GitHub e as
> três rotinas automáticas testadas. Falta só a Laura usar no estudo do dia a dia.

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
| Rotina automática | `.claude/hooks/brain-rotina.sh` (launchd: segunda 07:00 e diário 09:00) |
| Fechamento diário | `.claude/hooks/brain-diario.sh` (launchd, 23:50) |
| Backup na nuvem | GitHub privado `Brain-Laurinha`, por chave SSH |
| Como usar | `Projetos/Brain/ComoUsar.md` |

## Pendências

- [x] Criar conta no GitHub e conectar o repositório **privado** para backup na nuvem
- [x] Configurar `git config user.email` com o e-mail real da Laura
- [x] Instalar a rotina automática no MacBook dela (`instalar-rotina.sh`)
- [x] Abrir a pasta no Obsidian como cofre e conferir o grafo
- [ ] Preencher os blocos da entrevista que ficaram de fora (projetos pessoais, ferramentas)
- [ ] Abrir a pasta no Obsidian por **Open folder as vault**, para ele não criar cofre dentro

## Regras da área

- Mudança de estrutura só entra depois do ok da Laura. Arquivo novo dentro do padrão, pode.
- Todo erro apontado pelo `brain-lint` é corrigido antes de encerrar a sessão.

## Projeções

*(preenchido pelo `/sono`)*

## Histórico (últimas entradas)

| Data | O que aconteceu | Resultado |
|---|---|---|
| 2026-09-21 | Brain criado do zero a partir da entrevista e do edital da FGV | Estrutura no ar |
| 2026-09-22 | Instalação no MacBook da Laura: git, rotinas, CLI e backup no GitHub | Brain operando sozinho |

## 🔗 Relacionados

[[STATUS]] · [[Calendario]] · [[Laura]] · [[Brain-projeto]]
