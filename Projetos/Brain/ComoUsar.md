# Como usar o Brain — a rotina do dia a dia

Uma página. Se você só ler isto, já dá para usar tudo.

## A ideia em três frases

Você conversa com o Claude dentro desta pasta. Ele lê o painel, entende onde você está, e faz o
que você pedir. No fim de cada bloco você digita `/save` — e ele grava tudo no lugar certo,
sozinho, para você não precisar lembrar de nada.

---

## Quando você começa a estudar

Abra o Claude nesta pasta e diga o que vai fazer. Não precisa de comando:

> *"vou estudar História do Brasil agora, 2 horas"*

Ele lê o `STATUS.md`, vê o que você errou da última vez, o que está perto de cair, e te dá o
ponto de partida. Se quiser que ele monte o bloco todo:

```
/plano hoje
```

## Durante o bloco — os 4 passos do seu método

| Seu passo | O que digitar |
|---|---|
| 10 min — resumo + questões simples | `/questoes historia-do-brasil Era Vargas 5` |
| 40 min — questões antigas, dissertativas | `/questoes historia-do-brasil` |
| 1 hora — teoria | `/explica Estado Novo` |
| 10 min — explicar em voz alta | `/explica Estado Novo` e responder de volta, ou `/oral tema Era Vargas` |

Outras coisas que você vai usar direto:

```
/redacao              cola sua redação e ele corrige no formato da FGV
/revisar              a revisão do dia, montada do que você errou
/revisar flashcards   cartões das matérias de ontem, para antes de dormir
```

## Quando termina um bloco

```
/save
```

**Esse é o comando mais importante do Brain.** Em 30 segundos ele: atualiza o painel, atualiza a
ficha da área, escreve a memória do dia com o que você aprendeu e o que errou, joga os erros no
banco de erros, e sincroniza as tarefas.

Se você não der `/save`, o bloco aconteceu mas o Brain não sabe. Faça no fim de cada bloco,
não uma vez por dia.

## No fim do dia

```
/sono
```

Mais profundo que o `/save`. Ele consolida o dia, arruma o que ficou fora do lugar, e escreve
uma projeção por área: onde você chega em 30 dias no ritmo atual, no melhor caso, no pior caso,
e **a ação mais alavancada para amanhã**. Termina com os 3 focos do dia seguinte e as dúvidas
que precisam de você.

## No domingo, depois do simulado

```
/simulado
```

Ele pergunta nota por matéria, registra, e te mostra em quais matérias você **subiu e caiu**
em relação ao simulado anterior. É o número mais honesto que você tem.

## No sábado, depois da aula do Júlio

```
/oral
```

Treino de Exame Oral nos critérios exatos do edital da FGV. Vale peso 2 e elimina com nota
abaixo de 3,0 — e você só pode fazer **uma vez**. Não deixe para novembro: a convocação sai dia
16/11 e o exame pode ser dia 18.

Antes de tudo, uma vez só, vale fazer:

```
/oral trajetoria
```

O edital diz que suas respostas são avaliadas **à luz da sua trajetória biográfica**. Ou seja:
a sua história é matéria de estudo. Esse comando te ajuda a escrevê-la e organizá-la.

## O que você quer saber a qualquer momento

```
/tarefas              o que fazer hoje, o que vence essa semana
```

E para qualquer pergunta, é só perguntar: *"quanto tempo falta para a FGV?"*,
*"em que matéria eu mais erro?"*, *"o que eu combinei de perguntar na escola?"*

---

## O que acontece sozinho

| Quando | O quê |
|---|---|
| Fim de toda sessão | O guardião confere o formato e o Brain se salva no git |
| Todo dia 09:00 | Conferência de formato — só te avisa se houver erro |
| **Segunda 07:00** | O Brain se reorganiza sozinho (`/otimizar`) e te notifica quando termina |

Você não precisa fazer nada disso à mão.

## Exemplo de uma terça-feira sua

| Hora | O que você faz | O que você digita |
|---|---|---|
| 06:30 | Estudo do pico da manhã | *"vou fazer 1h30 de Matemática"* → `/questoes matematica` |
| 08:00 | Escola | — |
| 09:26 | Free period, 50 min de Artes & QC | `/explica arte contemporânea brasileira` |
| 14:30 | Cursinho (Literatura, História Geral, Português) | — |
| 20:00 | Bloco 1 — pico depois do cursinho | `/plano hoje`, depois `/questoes literatura` |
| 22:00 | `/save` | `/save` |
| 22:10 | Bloco 2 — rende menos, então revisão | `/revisar` |
| 00:05 | Fecha o dia | `/sono` |

---

## Se alguma coisa der errado

- **O Claude travou no fim da sessão?** O guardião achou um erro de formato. Ele te diz qual é
  e conserta sozinho — é só deixar.
- **Quer desligar o guardião por um dia?** Crie o arquivo `.claude/brain-lint.off`.
- **Quer ver se está tudo certo?** `python3 .claude/hooks/brain-lint.py`

## 🔗 Relacionados

`Areas/Brain.md`
