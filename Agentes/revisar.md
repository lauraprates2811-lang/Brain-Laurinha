# Agente `/revisar`

## O que faz
Monta a revisão do dia cruzando **o que você errou**, **há quanto tempo errou** e **o que está
perto de cair**. É repetição espaçada alimentada pelo seu próprio banco de erros.

## O que ele sabe sobre você
Que erro de causa `conceito` pesa mais que `desatenção`. Que seus flashcards são **antes de
dormir e nos horários livres**, das matérias do **dia anterior**. Que perto de um intensivo ou
da prova, a matéria daquela data sobe na fila.

## Como usar
```
/revisar              a revisão do dia (assume 30 min se você não disser)
/revisar geografia
/revisar flashcards   gera cartões do banco de erros de ontem
```

## Como ele conduz
Pergunta **antes** de explicar — reconhecer não é lembrar. Intervalos: 1 · 3 · 7 · 15 · 30 dias.
Acertou, sobe de intervalo; errou de novo, volta para 1 dia.

## 🔗 Relacionados
[[questoes]] · [[Vestibular]]
