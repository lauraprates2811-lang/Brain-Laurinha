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

## 🔗 Relacionados

[[2026-09-23]] · [[Vestibular]]
