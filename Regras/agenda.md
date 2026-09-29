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

Os eventos dela estão **só** na agenda `lauraprates2811@gmail.com` (passar como `calendarId`). A
agenda principal do conector é de outra pessoa: nunca procurar coisa da Laura nela (2026-09-28).

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

**Substituída em 28/09** pela regra abaixo: as metas do dia agora vão para o Todoist.

## Tarefas do dia moram no Todoist, que ela abre e marca sozinha (2026-09-28)

Ver a lista só perguntando ao Claude não funcionou para ela. Ela queria um app tipo Google Tarefas,
com aviso no celular. O Google Tarefas não tem conector; o Todoist tem, e foi conectado ao Claude
(conta `lauraprates2811@gmail.com`).

**A regra:** meta ou tarefa do dia que ela mandar entra **na hora** no Todoist, com data (e hora, se
tiver). "Fiz X" marca como feita lá. "Quais são minhas tarefas de hoje" se responde lendo o Todoist.
O `tarefas.json` continua para prazos grandes (vestibular, certificação, SAT) e tarefas do Brain,
que o `/sono` e o `/plano` leem. Estudos fixos e aulas particulares já estão lá como tarefas que se
repetem: não recriar, só mudar a existente. A semana fixa hoje (rotina nova de 29/09):

| Dia | De dia | À noite |
|---|---|---|
| Todo dia | Matemática (mínimo 40 min), com o plano por data na descrição da tarefa | |
| Segunda | — | Atualidades · Língua Portuguesa (o que mais cai ou dificuldade) |
| Terça | Revisão de Atualidades (só questões) | História Geral · Língua Portuguesa · Literatura (aula + o que mais cai / dissertativas) |
| Quarta | Revisão de HG + LP + Literatura (só questões) | HG ou HB · aula particular de Redação 21:30–22:30 |
| Quinta | Redação (de manhã, na escola) · Revisão de HG e/ou HB | Geografia · Matemática do Matias (2h a mais) · aula particular de Matemática 20:30–21:30 |
| Sexta | Matemática, só 40 min | Geografia · História do Brasil |
| Sábado | Obras (todas) e um pouco de Matemática — saem do sábado quando ela aprovar as manhãs de obras | |
| Domingo | Simulado, com Redação | |

As matérias mudam por dia da semana; só Matemática é todo dia. Aula particular nova ou com
horário mudado entra no Todoist também, sempre.

Quando ela disser o assunto de uma matéria que **já está fixa naquele dia** ("em Geografia vou
estudar Europa"), **edite a tarefa fixa daquela matéria**, nunca crie outra (pedido dela, 28/09,
repetido duas vezes). O assunto vai no topo da descrição, com a data ("**Hoje (28/09):** …"), e
substitui o do dia anterior; o que já estava na descrição fica embaixo. Só se a matéria **não**
estiver fixa naquele dia é que nasce uma tarefa nova, para aquele dia.

## O Todoist só se mexe quando ela pedir (2026-09-29)

No `/save` de 29/09 ela contou o que tinha estudado (Atualidades, e log e porcentagem em Matemática).
O Claude foi ao Todoist para pôr o assunto na tarefa fixa. Ela cortou: "não precisa mexer no
todoist, mexe apenas quando eu pedir".

**A regra:** criar, editar ou marcar tarefa no Todoist **só a pedido dela** ("põe no Todoist",
"marca como feita", "coloca essa meta"). Contar o que estudou, num `/save` ou numa conversa, não é
pedido. As duas regras acima ("entra na hora", "edite a tarefa fixa") valem quando ela pede para pôr
no Todoist. Ler o Todoist para entender o dia pode. Na dúvida, pergunte.

## No Todoist, "Dia:" e "Noite:" no título, e nada de emoji (2026-09-29)

Com a rotina nova ela pediu para não esquecer se cada estudo é de dia, à noite ou os dois. O Claude
marcou com ☀️ e 🌙 no título, e ela pediu para tirar os emojis.

**A regra:** tarefa de estudo com período fixo começa com `Dia:` ou `Noite:` no título, sem emoji.
A tarefa de Matemática mantém o nome, e o período de cada data vai na descrição, no plano
("30/09 (qua) · assunto · **dia e noite**").

## 🔗 Relacionados

[[Calendario]] · [[Vestibular]]
