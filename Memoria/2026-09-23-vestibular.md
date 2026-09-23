# 2026-09-23 — Vestibular

## Quanto tempo por questão dissertativa

**O que era**
A Laura quis saber quanto tempo, em média, levar em cada dissertativa. Hoje ela faz a redação em 2h
e quer baixar para 1h40.

**Desafios**
1. O tempo depende do período da prova, e a Redação divide o primeiro período com Humanas.
2. As questões de Português e de Artes pedem esforços muito diferentes.
3. O detector de mensagens achou que era uma dissertativa para corrigir e mandou acionar o
   `/discursiva`. Não tinha questão nem resposta: era alarme falso, e o agente não foi acionado.

**Como resolvi**
Horários do edital de 2027 (item 1.9.2) + formato do banco, igual nas 4 últimas provas (2023.1 a 2026.1):
- **18/10, 08:00–11:30 (3h30):** Redação + 8 dissertativas de Humanas (em geral 4 de História e
  4 de Geografia). Com redação em 2h, sobram ~11 min por questão, sem folga. Com **1h40**, dá
  **~12 min** por questão e sobram 10 min.
- **19/10, 08:00–11:00 (3h):** 8 de Português + 5 de Artes. Proposta: **~10 min** por questão de
  Português (reescrita, sinônimo, pronome, figura) e **~18 min** por questão de Artes
  (comparação de obras, autor e presente), com 10 min de folga.
- O edital diz que o tempo inclui passar a limpo no caderno definitivo.

**Ferramentas**
Edital unificado (`Projetos/Vestibular/editais/`) · `banca.py` e os CSVs das edições.

**O que aprendi**
- A meta de 1h40 na redação é o que faz o primeiro dia fechar com folga.
- Na dissertativa, rascunho é só esquema de 2 ou 3 linhas; a resposta vai direto para o definitivo.
- Se uma de Humanas passar de 15 min, pula e volta: a Redação elimina abaixo de 3,0 e não pode
  perder tempo para Humanas.

**O que errei**
Nada nesta parte. A divisão entre Português e Artes é estimativa pelo tipo de pergunta, e isso foi
dito para ela.

**O que ficou aberto**
- Cronometrar as dissertativas nos simulados de domingo e ajustar o tempo-alvo com o tempo real dela.
- O detector do `/discursiva` dispara em mensagem que só fala de dissertativa, sem questão para corrigir.

## Duas dissertativas de provas antigas: Crise de 29 e Semana de 22

**O que era**
A Laura pediu 2 dissertativas de provas antigas: uma sobre a Crise de 1929 (História Geral) e uma
sobre modernismo e Semana de Arte Moderna (Literatura).

**Desafios**
1. A Crise de 1929 nunca caiu: nas 6 provas do banco não aparece 1929, Grande Depressão, New Deal,
   Keynes nem bolsa.
2. O texto das questões é da FGV: vai como página da prova, não copiado na conversa.

**Como resolvi**
- Modernismo: **2022.1-DIS-AR11 e AR12** (prova de Artes). Enunciado comum sobre o centenário da
  Semana de 22 e o *Manifesto Antropófago*: as contradições do Manifesto (Benedito Nunes) e a
  antropofagia diante da questão indígena hoje. Na mesma página está a AR13 (Cézanne × Anita Malfatti).
- História: a mais próxima é **2023.1-DIS-CH4** (Hobsbawm, barbárie anti-iluminista na Europa
  contemporânea), que conversa com a aula da Crise de 29 ao nazifascismo.
- A página de cada prova virou um PDF na pasta da matéria (`historia-geral/` e `literatura/`).
- Ofereci criar uma questão inédita sobre 1929 no estilo FGV, marcada como inédita.

**Ferramentas**
`banca.py busca` · PyMuPDF para separar a página da prova.

**O que aprendi**
- **Modernismo cai pela prova de Artes, não pela de Português:** 4 discursivas de Artes
  (2022.1-AR11, AR12 e AR13; 2025.1-AR2, *Abaporu* × *Os bichos*).
- A Crise de 29 entra na FGV de lado, pelo que veio depois: nazifascismo, totalitarismo, barbárie.

**O que errei**
Nada nesta parte.

**O que ficou aberto**
- A Laura vai responder as duas e mandar para correção pelo `/discursiva`.
- A questão inédita sobre 1929, se ela quiser.

## Provas antigas numa pasta só

**O que era**
Na faxina dos Downloads, a Laura pediu todas as provas antigas da FGV numa pasta só.

**Como resolvi**
A pasta única já existia: `Projetos/Vestibular/provas-antigas/`, uma subpasta por edição. Os 26
zips e 4 pastas de Downloads foram conferidos arquivo por arquivo (pelo conteúdo, não pelo nome):
tudo já estava lá, menos 3 arquivos de 2026.1 de outro curso (Matemática discursiva e `RMH-T01`),
que foram salvos antes. Atalho novo: `~/Downloads/Provas-FGV`.

**O que aprendi**
Os zips repetidos (até 5 cópias do mesmo) eram downloads repetidos do mesmo arquivo.

**O que errei**
Nada nesta parte.

**O que ficou aberto**
Esta pasta agora é a **única cópia** das provas, e ela fica fora do backup do GitHub.

## Quanto caem pensadores (Marx, Locke e companhia)

**O que era**
A Laura quis saber se cai muita questão que exige conhecer Marx, Locke e outros pensadores.

**Como resolvi**
`/banca` com busca por 30 nomes nas 6 provas do banco (152 dissertativas).

**O que aprendi**
- **11 das 152 dissertativas (~7%)** pedem a ideia de um pensador. **Nenhuma objetiva.**
- **Castells caiu 4 vezes** (2021.1-AR3, 2022.1-AR14 e AR15, 2025.1-AR5), sempre sobre a crise
  da democracia liberal. Depois: Kant 2, Marx 2, e Montesquieu, Adam Smith, Arendt e Hobsbawm
  1 cada.
- **Locke nunca apareceu pelo nome.** Hobbes, Rousseau, Weber e Durkheim também não.
- A FGV imprime o trecho do autor e pede a ideia central, o contexto ou a comparação entre dois
  autores; não cobra teoria a fundo.

**O que errei**
Nada nesta parte.

**O que ficou aberto**
Ficou oferecida uma ficha de uma página com esses pensadores e flashcards, na pasta de Artes.

## Como escrever uma dissertativa

**O que era**
Três perguntas seguidas: qual a estrutura de uma resposta, se erro de português tira ponto, e um
passo a passo.

**Como resolvi**
- **Estrutura por item:** resposta direta na 1ª frase → explicação em 2 ou 3 frases → prova (trecho
  do texto ou fato) → fecho de uma frase, só se ele acrescentar algo. Contextualização só quando o
  comando pede.
- **Erro de português:** conferido na grade oficial, que é igual em todas as provas. "Algum desvio
  de redação" derruba um nível (100% → 75%; 50% → 25%). Um erro ou cinco no mesmo item custam o
  mesmo. Pontuação conta; pronúncia só no Exame Oral.
- **Passo a passo** para Humanas (~12 min):
  1. circular verbos e quantidades
  2. ler o texto atrás do pedido
  3. fazer um esquema curto no rascunho
  4. escrever direto no definitivo
  5. caçar erros por 1 minuto
  6. conferir a lista
  7. pular se passar de 15 min
- **Por que circular os verbos:** cada verbo é uma exigência da grade. Um verbo esquecido deixa
  a resposta parcial (ex.: 2022.1-CH8, "aponte e explique").

**O que aprendi**
A grade da FGV não conta os erros, só pergunta se houve algum. Frase curta é a defesa.

**O que errei**
Nada nesta parte.

**O que ficou aberto**
O passo a passo foi entregue, mas **não virou regra**: a Laura ainda não confirmou.

## Correção: FGV 2022.1, Artes, pergunta 11 (Manifesto Antropófago) — 25%

**O que era**
Primeira dissertativa corrigida pelo `/discursiva`: a resposta dela, à mão, à pergunta 11 (segundo
Benedito Nunes, quais elementos do Manifesto mostram que "no antropofagismo tudo é contraditório").

**Desafios**
Transcrever a letra dela sem corrigir nada em silêncio. Os acentos duvidosos foram conferidos
ampliando a foto, e só entraram os que dava para ver com certeza.

**Como resolvi**
Grade oficial da edição (vale 2,0) + resposta oficial. Nota **0,5 / 2,0 (25%)**: resposta parcial
e com desvios. PDF em `Projetos/Cursinho/artes-e-questoes-contemporaneas/questoes-discursivas/`.

**Ferramentas**
`/discursiva` · `gerar_pdf.py` · grade oficial em `provas-antigas/2022.1/`.

**O que aprendi**
- Ela acerta a ideia central da antropofagia ("comer o estrangeiro e misturar com o nacional") e
  escolhe um trecho válido ("Já tínhamos o comunismo…").
- Falta dizer os **dois lados** de cada contradição, que é o que a grade chama de "identificar os contrastes".

**O que errei** (dela, registrado no banco de erros de Artes)
- **Conteúdo:** leu a "idade de ouro" como a Era de Ouro do pós-1945 ("Europa ocidental, Japão e
  EUA"). No Manifesto (1928) é o mito primitivo, e a contradição é o "atrasado" já ter as
  utopias da Europa "moderna".
- **Língua:** "ultilizar" (3x), "extrangeiro" (3x), "apresentão", "Segundo ao", concordância
  ("elementos extraido"), vírgulas, maiúsculas e acentos (época, Antropófago, tínhamos, contraditória).
- Padrão que também aparece fora da prova: "-oens" no lugar de "-ões" (questoens) e "n" antes de
  "p" (Contenporaneas).

**O que ficou aberto**
- Responder a pergunta 12 (2022.1) e a de Hobsbawm (2023.1-CH4).
- Os pares contraditórios do Manifesto vão para o `/revisar`.

## 🔗 Relacionados

[[2026-09-23]] · [[Vestibular]]
