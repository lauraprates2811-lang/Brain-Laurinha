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


## Comando que escreve arquivo se confere contando, não lendo a tela (2026-09-22)

Na instalação do Brain no MacBook, a saída do `unzip` foi filtrada com `head`. O filtro matou o
processo no meio por SIGPIPE e só 25 dos 258 arquivos foram extraídos — mas a tela parecia certa,
e o Brain foi dado por instalado três mensagens antes de a falha aparecer.

**A regra:** depois de todo comando que cria, copia ou extrai arquivo, conferir o resultado por
contagem (`find | wc -l`, `git ls-files | wc -l`) e comparar com o esperado. Nunca filtrar a
saída de um comando que ainda está escrevendo.

## Rotina do launchd precisa do ambiente ensinado na mão (2026-09-22)

A rotina automática respondeu "Not logged in" mesmo com o Claude Code logado. O `launchd` roda
com um ambiente quase vazio: sem `USER`, o programa não encontra o login guardado no chaveiro do
macOS, e sem `PATH` não encontra o próprio executável.

**A regra:** todo script agendado no `launchd` começa exportando `PATH`, `USER` e `LOGNAME`. E se
o script chama o `claude -p`, o que ele precisa rodar vai em `--allowedTools`, porque
`acceptEdits` libera editar arquivo mas não rodar comando.

## Prova escaneada vira texto pelo OCR do Mac, e o gabarito se confere na imagem (2026-09-22)

Metade das provas antigas da FGV veio escaneada, e os gabaritos oficiais são a prova com a
resposta grifada em amarelo. O OCR do macOS (Vision) leu o texto bem, e um detector de amarelo
achou a maioria das respostas — mas não todas, e errou onde a alternativa não tinha letra.

**A regra:** PDF sem texto passa pelo OCR do macOS. Gabarito tirado automaticamente só vale
depois de conferido olhando a página; onde a detecção falha, lê-se na imagem. Número de gabarito
nunca é preenchido de memória.

## Arquivo pesado fica fora do git; o que vai para a nuvem é o dado extraído (2026-09-22)

O salvamento automático faz `git add -A` ao fim de toda sessão. Os PDFs das provas antigas
(~130 MB) teriam deixado o backup 50 vezes maior, e os originais já estão nos zips da Laura.

**A regra:** antes de copiar arquivo pesado para dentro do Brain, decidir se ele vai para o
backup. PDF de prova fica no `.gitignore`; o que se versiona é o que foi extraído dele (o banco
em CSV).

---

## Material do cursinho fica numa pasta por matéria (2026-09-22)

A Laura pediu, ao guardar o mapa e os flashcards da aula de História Geral, que o material do
cursinho fique separado por matéria.

**A regra:** `Projetos/Cursinho/<materia>/`, com o nome da grade em minúsculas e hífen
(`historia-geral/`, `lingua-portuguesa/`, `matematica/`). Cada aula é um arquivo com o nome do
assunto. A pasta só nasce quando chega o primeiro material da matéria.

---

## 🔗 Relacionados

[[Brain]]
