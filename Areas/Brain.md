# Brain

> **Status:** Instalado no MacBook, com backup no GitHub e as três rotinas no ar. Ganhou o banco de
> provas antigas e dois agentes que entram sozinhos (`/banca` e `/discursiva`). Falta conferir o
> acionamento automático numa conversa nova.

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
| Detector de agentes | `.claude/hooks/agentes-gatilho.py` (a cada mensagem: aciona `/banca` e `/discursiva`) |
| Banco de provas antigas | `Projetos/Vestibular/provas-antigas/banco/` (CSV por edição + `banca.py`) |
| PDF de correção | `Projetos/Vestibular/discursivas/gerar_pdf.py` |
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
- [ ] Conferir numa conversa nova se o `/banca` e o `/discursiva` entram sozinhos
- [ ] Dar ok (ou mudar) a pasta nova `Projetos/Vestibular/discursivas/`
- [ ] Decidir se os PDFs das provas antigas (~130 MB) entram no backup — hoje ficam fora

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
| 2026-09-22 | Agentes `/banca` e `/discursiva`, detector de mensagens e gerador de PDF de correção | 9 agentes · 2 entram sozinhos |

## 🔗 Relacionados

[[STATUS]] · [[Calendario]] · [[Laura]] · [[Brain-projeto]]
