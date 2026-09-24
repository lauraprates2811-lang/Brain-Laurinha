# 2026-09-24 — Vestibular

## Simulado no formato completo da FGV (26–27/09) na agenda

**O que era**
A Laura pediu para colocar na agenda um simulado no formato exato da prova da FGV, no fim de
semana de 26 e 27/09: sábado com discursiva (08h–11h30) e objetiva (14h30–18h), domingo com a
2ª parte, online (08h–11h). Pediu também para tirar o simulado padrão de domingo, só nesse dia
27, porque ele é fixo (recorrente).

**Desafios**
1. Existem duas contas de Google Calendar ligadas ao Brain (a do João e a da Laura); os eventos
   de "Simulado" que já existiam ficam na agenda `lauraprates2811@gmail.com`, não na padrão.
2. Havia dois blocos fixos de "Simulado" no domingo (manhã e tarde, este com correção de erros).
   Era preciso remover só a ocorrência de 27/09 de cada um, sem mexer nas próximas datas.

**Como resolvi**
- Achei a agenda certa com `list_calendars` e conferi os dois eventos de domingo: "Simulado"
  (08h–11h30) e "Simulado (tarde) + correção dos erros" (14h30–18h).
- Criei os 3 eventos do fim de semana com os mesmos horários e matérias da prova real de 18–19/10
  (ver `Vestibular`).
- Apaguei só a instância de 27/09 dos dois blocos de Simulado, usando o `eventId` daquela
  ocorrência (com sufixo de data), o que mantém a recorrência normal nos outros domingos.

**Ferramentas**
Conector do Google Calendar (`list_calendars`, `list_events`, `create_event`, `delete_event`).

**O que aprendi**
- O sábado 26/09 já tinha o intensivo de Geografia do cursinho e outros compromissos (Cursinho
  Oral e Artes & QC, aniversário de 18 anos da Julia às 17h) — o novo simulado bate em cima de
  tudo isso. Não decidi por ela, só registrei o conflito.
- Apagar uma instância de evento recorrente pelo `eventId` com sufixo de data cancela só aquela
  ocorrência; a série continua normal.

**O que errei**
Nada nesta parte — o conflito de horário do sábado foi avisado no chat, ainda não resolvido.

**O que ficou aberto**
- Resolver o conflito de 26/09 entre o simulado, o intensivo de Geografia, o cursinho de sábado
  e o aniversário da Julia.

## 🔗 Relacionados

[[2026-09-24]] · [[Vestibular]]
