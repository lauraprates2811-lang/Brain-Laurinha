# Brain

> **Status:** No MacBook, com backup no GitHub e as três rotinas no ar. `/banca` e `/discursiva` entram
> sozinhos, mas o detector dispara em falso. Downloads limpo (o Brain e 2 atalhos); provas e apostilas
> agora são cópia única, **fora do backup**.

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
- [ ] Conferir se o `/discursiva` entra sozinho com uma questão e a resposta (o `/banca` já entra)
- [ ] Ajustar os detectores do `/banca` e do `/discursiva`, que disparam em mensagem fora do assunto
- [x] Dar ok (ou mudar) a pasta nova `Projetos/Vestibular/discursivas/` — fica só com as fichas; os PDFs vão para `questoes-discursivas/` de cada matéria (23/09)
- [ ] **Decidir o backup** das provas (~130 MB) e das apostilas do cursinho: desde 23/09 são a única cópia

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
| 2026-09-23 | Faxina dos Downloads: 103 itens na Lixeira, provas e material organizados, atalhos `Materias` e `Provas-FGV` | Downloads com 3 itens · backup virou risco |

## 🔗 Relacionados

[[STATUS]] · [[Calendario]] · [[Laura]] · [[Brain-projeto]]
