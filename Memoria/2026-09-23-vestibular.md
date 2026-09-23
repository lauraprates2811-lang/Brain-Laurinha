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

## 🔗 Relacionados

[[2026-09-23]] · [[Vestibular]]
