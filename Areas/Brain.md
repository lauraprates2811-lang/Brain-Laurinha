# Brain

> **Status:** No MacBook, com backup no GitHub e as três rotinas no ar. **Todoist** com a rotina de estudo dia a dia
> até 19/10 (79 tarefas, sem repetição), para ela ver tudo com antecedência. Na rede da escola, GitHub, claude.ai
> e Todoist não conectam. Provas e apostilas seguem **fora do backup**.

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
| Lista de tarefas (prazos grandes e o Brain) | `Tarefas/dados/*.json` |
| Tarefas do dia e estudos fixos | Todoist (conector; conta `lauraprates2811@gmail.com`) |
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
- [ ] Testar se o Todoist aparece no Claude do celular (o conector está na conta do Claude do Mac)
- [ ] Dizer quais tarefas atrasadas do Brain (23–25/09) já foram feitas e quais passam para o Todoist
- [ ] Conferir, fora da rede da escola, se o auto-save subiu para o GitHub (em 29/09 o Mac ficou 2 commits à frente)
- [ ] Tarefa do Todoist com ano errado (27/09/2027, "finalizar as questões da aula de atu"): perguntar se apaga ou corrige
- [ ] Montar a rotina do Todoist depois da FGV (a partir de 20/10), dia a dia: perguntar a ela até quando — tarefa #42
- [ ] **Decidir o backup** das provas (~130 MB) e das apostilas do cursinho: desde 23/09 são a única cópia

## Regras da área

- Mudança de estrutura só entra depois do ok da Laura. Arquivo novo dentro do padrão, pode.
- Todo erro apontado pelo `brain-lint` é corrigido antes de encerrar a sessão.

## Projeções

*(preenchido pelo `/sono`)*

## Histórico (últimas entradas)

| Data | O que aconteceu | Resultado |
|---|---|---|
| 2026-09-22 | Agentes `/banca` e `/discursiva`, detector de mensagens e gerador de PDF de correção | 9 agentes · 2 entram sozinhos |
| 2026-09-23 | Faxina dos Downloads: 103 itens na Lixeira, provas e material organizados, atalhos `Materias` e `Provas-FGV` | Downloads com 3 itens · backup virou risco |
| 2026-09-23 | O `/discursiva` passou a gravar o PDF na pasta da matéria (`questoes-discursivas/`); `discursivas/` fica só com as fichas | Pendência da pasta fechada |
| 2026-09-28 | Todoist conectado ao Claude; tarefas do dia saem do chat e vão para o app, com a semana fixa de matérias e as aulas particulares. Assunto do dia vai na tarefa fixa da matéria | 14 tarefas fixas · ela marca sozinha no celular |
| 2026-09-29 | Todoist refeito com a rotina nova ("Dia:"/"Noite:" no título, sem emoji, 4 tarefas novas, oral virou lembrete em 16/11); tabela das semanas em PDF (Chrome) e `.docx` montado sem biblioteca | 17 tarefas fixas · rede da escola bloqueia os conectores |
| 2026-09-29 | Rotina do Todoist virou uma tarefa por dia até 19/10: as 17 recorrentes viraram a 1ª data, o resto foi criado dia a dia, com Insper e FGV | 79 tarefas · nada apagado · assunto do dia no título |

## 🔗 Relacionados

[[STATUS]] · [[Calendario]] · [[Laura]] · [[Brain-projeto]] · [[Brain-historico]]
