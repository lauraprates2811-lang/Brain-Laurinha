# Decisões — técnicas

Receitas e armadilhas de ferramenta: Obsidian, git, Claude, PDF, planilhas.

---

## PDF de edital vira texto antes de virar conhecimento (2026-09-21)

O edital da FGV tem 119 páginas e a leitura direta do PDF pela web falhou: voltou estrutura
binária, sem texto. A extração local com `pypdf` funcionou e permitiu achar as seções exatas.

**A regra:** edital, apostila ou prova antiga em PDF que interesse ao Brain é convertido para
`.txt` e guardado ao lado do original em `Projetos/<X>/`. Depois disso se lê **por `grep`**,
nunca inteiro — 119 páginas estouram o contexto sem entregar nada.

---

## Nome de pasta e arquivo sem espaço e sem acento (2026-09-21)

A pasta nasceu como "Brain Laura" e foi renomeada para `Brain-Laura` antes de qualquer arquivo
existir. Espaço em nome quebra script e exige aspas em todo comando.

**A regra:** pastas e arquivos sem espaço e sem acento. Datas sempre `AAAA-MM-DD`.

---

## Caminho absoluto quebra quando a pasta muda de computador (2026-09-21)

Este Brain foi montado no Mac do João e vai ser usado no MacBook da Laura.

**A regra:** nenhum caminho absoluto dentro de hook, script ou comando. Usar sempre caminho
relativo ou `$CLAUDE_PROJECT_DIR`. O que depende da máquina (agendamento do launchd, remoto do
git) fica isolado no instalador, que se roda uma vez por computador.

---

## 🔗 Relacionados

[[Brain]]
