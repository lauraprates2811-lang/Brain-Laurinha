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

## Material de matéria fica numa pasta por matéria, com atalho em Downloads (2026-09-22, ampliada em 2026-09-23)

A Laura pediu, ao guardar o mapa e os flashcards da aula de História Geral, que o material do
cursinho fique separado por matéria. No dia seguinte pediu que **todo** material que o Claude criar
(flashcards, apostila, mapa) vá para a pasta da matéria, e que ela ache essas pastas pelos Downloads.

**A regra:** `Projetos/Cursinho/<materia>/`, uma pasta para cada uma das 13 matérias da grade, em
minúsculas e com hífen. Cada material é um arquivo com o nome do assunto, em `.md` (Obsidian) e,
quando tiver flashcards, também em `.html` (abre no navegador, com os cards virando). O atalho
`~/Downloads/Materias` aponta para `Projetos/Cursinho/`: é por ali que ela abre no Finder. Nada de
cópia fora do Brain. O mesmo vale para as provas antigas: pasta única em
`Projetos/Vestibular/provas-antigas/`, com atalho `~/Downloads/Provas-FGV` (2026-09-23). PDFs do
cursinho ficam fora do git, como os das provas. Cada matéria tem a subpasta `questoes-discursivas/`,
com as páginas de prova e as correções do `/discursiva` (2026-09-23).

---

## Caderno do cursinho não se guarda: na pasta da matéria vão só o mapa e os flashcards (2026-09-28)

A Laura mandou o Caderno 3 de Geografia para fazer o mapa e os cards da aula 11 (Europa). O Claude
guardou o caderno na pasta e depois o cortou em um PDF por aula; ela disse que não precisa:
"só coloca os flashcards e o mapa mental, não o caderno todo".

**A regra:** quando ela mandar um caderno ou apostila para fazer mapa e flashcards, o Claude **só lê**
o PDF. Não copia, não move e não corta o PDF, nem guarda nenhum pedaço dele no Brain. Na pasta
`Projetos/Cursinho/<materia>/` entram só o `<assunto>.md` e o `<assunto>.html` (mapa + cards).
Para achar a aula de novo, o `.md` registra a origem na primeira linha (ex.: "Frente 2, Aula 11,
Caderno 3, páginas 117 a 146"). Os Cadernos 3 e 4 de Geografia e os 17 PDFs por aula foram para a
Lixeira em 28/09.

---

## Faxina: nada sai sem conferir que existe cópia, e tudo vai para a Lixeira (2026-09-23)

A Laura pediu para apagar tudo dos Downloads "menos o que o Claude criou". A maior parte dos 135
itens era material dela (apostilas, edital, fotos), e os zips eram os únicos originais das provas
fora do Brain.

**A regra:** antes de apagar em massa, listar e perguntar por categoria. Cópia só sai depois de
conferida pelo **conteúdo** (hash), não pelo nome. Nada é apagado direto: vai para a Lixeira, com
o `trash` do macOS. Se a limpeza deixa um arquivo como cópia única, isso vira pendência de backup
na hora.

---

## Recorrência "de X em X dias" precisa de `WEEKLY`, não de `DAILY;INTERVAL` (2026-09-24)

O evento de Terapia (quinzenal, sempre quinta) tinha sido criado no Google Calendar com
`RRULE:FREQ=DAILY;INTERVAL=15`. Como 15 não é múltiplo de 7, cada ocorrência caía um dia depois
da anterior — a série ia saindo da quinta aos poucos. A Laura percebeu e pediu para apagar tudo.

**A regra:** compromisso "de X em X dias" que precisa manter o mesmo dia da semana usa
`FREQ=WEEKLY;INTERVAL=<X/7>;BYDAY=<dia>` (quinzenal = `INTERVAL=2`), nunca
`FREQ=DAILY;INTERVAL=X`. E apagar só uma ocorrência de uma série usa o `eventId` daquela
instância (com sufixo de data); apagar a série inteira usa o `eventId` da recorrência (sem sufixo).

---

## Todoist: recorrência que começa hoje se escreve com a data (2026-09-28)

Ao montar as matérias fixas da semana no Todoist, mudar uma tarefa para `every monday` numa segunda
jogou a tarefa para a segunda seguinte, e ela sumiu do dia. `every monday, thursday, friday
starting today` foi pior: apagou a recorrência da tarefa.

**A regra:** para a recorrência valer já hoje, escreva `starting` com a data em inglês
(`every mon, thu, fri starting sep 28`). Depois de criar ou mudar, confira no retorno que
`recurring` não voltou `false` e que a data é a esperada. E conector novo (Todoist ou outro) só
se liga com o navegador logado na **mesma conta do Claude** que o app usa; se aparecer
"Incompatibilidade de conta", é isso.

**Atualização (29/09):** `every mon, tue starting sep 29` também apagou a recorrência, e `every thursday`
numa terça pulou a quinta seguinte. Mais seguro: mudar com `every ...` sem `starting` e, se a data sair
errada, corrigir com `reschedule-tasks`, que muda só a data e mantém a recorrência.

---

## O Brain também roda no celular, pela nuvem, e o GitHub é o ponto de encontro (2026-09-24)

A Laura queria usar o Brain no iPhone sem depender do Mac ligado. O Claude do celular (app do
Claude, aba Code, repositório `Brain-Laurinha`) roda numa máquina na nuvem, com uma cópia do
GitHub. Ele lê este `CLAUDE.md` e os comandos de `.claude/commands/`, mas só consegue enviar para o
ramo da própria sessão (`claude/...`), nunca direto para o `main`.

**A regra:** o `auto-save.sh` faz a ponte sozinho. No celular, ao fim de cada resposta, ele envia o
ramo e o junta ao `main` pela API do GitHub. No Mac, no começo de cada sessão (hook `SessionStart`),
ele traz o `main` e junta qualquer ramo `claude/*` que tenha ficado para trás. Conflito nunca é
resolvido no automático: o hook avisa e o Claude do Mac resolve à mão. Duas consequências:
- **A memória do Mac não vai para o celular.** Toda regra que o Claude precisa seguir mora no Brain
  (`Regras/`), nunca só na memória local.
- **Na nuvem não existem os PDFs das provas antigas** (ficam fora do git). O `/banca` funciona pelos
  CSVs do banco; abrir a prova original só no Mac.

---

## Na rede da escola, GitHub, claude.ai e os conectores não funcionam (2026-09-29)

Em 29/09, no Mac na escola, o Todoist falhou cinco vezes seguidas (`ERR_CONNECTION_RESET`). No
teste, google.com abria; claude.ai, mcp.todoist.com e github.com não. O aviso de "conflito" do
auto-save na abertura da sessão era a mesma coisa: `git fetch` recusado na porta 22, sem conflito
de verdade. Minutos depois, quando ela pediu para tentar de novo, o Todoist funcionou.

**A regra:** conector ou auto-save falhando → testar a rede antes de mexer em qualquer coisa
(`curl` em claude.ai e github.com). Se for a rede, avisar a Laura e tentar de novo depois ou em
outra rede. Nunca rodar `git pull --rebase` para "resolver conflito" sem ver o conflito.

---

## Google Docs: o conector do Drive não cria arquivo, então vai um .docx (2026-09-29)

Ela pediu a tabela das semanas no Google Docs para editar. O conector do Google Drive só renomeia,
move, compartilha e manda para a lixeira, e está na conta do Claude do Mac, não na dela. No Mac não
há Node, python-docx, LibreOffice nem Poppler.

**A regra:** para ela editar no Google Docs, gerar um `.docx` (dá para montar só com `zipfile`, sem
biblioteca) e mandar com o passo a passo: drive.google.com → Novo → Upload de arquivo → Abrir com
Documentos Google → Arquivo → Salvar como Documentos Google. Subir pelo Chrome dela só se ela pedir.
PDF sai do Chrome em modo headless e se confere com `fitz`.

## 🔗 Relacionados

[[Brain]]
