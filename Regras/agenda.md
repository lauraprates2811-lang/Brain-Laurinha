# Regras — agenda e calendário

Como as datas entram e saem do Brain.

## O que é o `Calendario.md`

A linha do tempo única: toda data que importa, em ordem, com **o que precisa estar pronto antes**
dela. Não é lista de compromissos do dia — é o mapa dos pontos sem volta.

## O que entra

- Data de prova, inscrição, resultado e matrícula (sempre com a fonte oficial)
- Prazo de trabalho e entrega da EABH
- Intensivo, simulado marcado e aula que não pode ser perdida
- Qualquer prazo que, se perdido, não tem segunda chance

## O que não entra

- Compromisso comum do dia a dia (isso é tarefa, vai para `Tarefas/`)
- Data provável, chutada ou lembrada de cabeça — ou vem da fonte, ou entra como `[a confirmar]`

## Como se mantém

- O `/save` atualiza o `Calendario.md` quando uma data nasce, muda ou vence.
- O `/sono` confere se alguma data passou sem registro.
- O `brain-lint` avisa quando existe prazo vencido no `Calendario.md` sem nada registrado.

## Google Calendar

A Laura usa o Google Calendar do dia a dia (`lauraprates2811@gmail.com`, compartilhado com o
Claude pelo conector) — aulas fixas, provas, terapia. Eventos entram e saem de lá direto, a
pedido dela, sem confirmação extra (2026-09-24). O `Calendario.md` continua sendo a fonte de
verdade para **prazos e datas sem volta**; o Google Calendar é o dia a dia, e a sincronização
entre os dois é manual, feita quando a data também é desse tipo (ver "O que entra" acima).

## Depois da meia-noite, o "amanhã" da Laura é o dia que está começando (2026-09-22)

Às ~00:20 de quarta ela perguntou o que estudar "amanhã" e queria dizer quarta: ela dorme às
00:10, então o dia dela só vira quando ela dorme. O Claude respondeu quinta e, quando ela disse
"tá errado", reescreveu a rotina em 6 arquivos. Teve que voltar tudo.

**A regra:** entre a meia-noite e a hora de dormir, "hoje" e "amanhã" seguem o dia dela, não o
calendário. Na dúvida, diga o dia com a data ("quarta, 23/09") antes de responder. E quando ela
disser que uma resposta está errada, pergunte o que está errado antes de mudar um fato que ela já
confirmou.

## Metas do dia: gravar na hora, mostrar em lista quando ela pedir (2026-09-23)

A Laura manda metas e tarefas do dia aos poucos e, no fim do dia, pergunta quais são. PDF e
arquivo complicam a vida dela.

**A regra:** cada meta entra em `Tarefas/dados/tarefas.json` **assim que ela manda**, com `prazo` =
o dia e a `area` certa. Quando ela pedir a lista, mostrar direto no chat, com ✅ para feita e ⬜
para aberta, sem PDF. "Fiz X" fecha a tarefa. O que ficou aberto no fim do dia: perguntar se vai
para amanhã ou se cancela. Tarefa com hora marcada pode virar evento no Google Calendar dela.

## 🔗 Relacionados

[[Calendario]] · [[Vestibular]]
