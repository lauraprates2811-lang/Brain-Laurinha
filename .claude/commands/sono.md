---
description: Consolidação do fim do dia — mais profunda que o /save, com projeções e lint
---

# /sono — fim do dia

Mais profundo que o `/save`. Roda uma vez por dia, no fim. Sete etapas.

## 1. Coleta

Leia `STATUS.md`, as memórias de hoje (`Memoria/AAAA-MM-DD-*.md`) e as tarefas que mudaram.
Monte o retrato do dia: o que foi estudado, o que foi feito, o que ficou aberto.

## 2. Consolidação

Decida o que vale guardar e **descarte o resto**:

- Virou aprendizado que serve para o futuro → `Regras/`
- Mudou o estado de uma frente → ficha da área
- É uma data sem volta → `Calendario.md` + `prazos.json`
- Não é nenhum dos três → não guarde. Memória cheia de ruído é memória inútil.

## 2B. Reorganização

Procure e conserte: arquivo no lugar errado · nome fora do padrão (espaço, acento, data) ·
duplicata · histórico que passou do limite e precisa rotacionar · nota órfã (ninguém linka) ·
link na direção errada (memória linkando índice).

## 2C. Síntese

O que a Laura aprendeu hoje que **ainda não está registrado** em lugar nenhum? Escreva.
Inclui o **banco de erros**: todo erro do dia que ainda não foi para
`Projetos/Vestibular/banco-erros/` vai agora, com a causa.

## 3. Projeção de cenários

Para **cada área**, escreva na seção `## Projeções` da ficha:

- Onde ela chega em **30 dias** mantendo o ritmo atual
- O **melhor caso** realista
- O **pior caso** realista
- **A ação mais alavancada para amanhã** — uma só

Seja concreto e use os números que existem (dias para a prova, erros por matéria, sono).
Não escreva incentivo genérico.

## 4. Atualizar painel e calendário

`STATUS.md` e `Calendario.md` com o estado do fim do dia. Confira se alguma data do calendário
passou sem registro.

## 5. Relatório

Grave `Memoria/AAAA-MM-DD-sono.md` com:

- **Consolidado hoje** — o que entrou no Brain e onde
- **Insight do dia** — a coisa não óbvia que ficou clara
- **Foco de amanhã** — exatamente 3 itens
- **Dúvidas para a Laura** — o que precisa da decisão dela
- **Alerta de prazo** — o que está chegando

## 6. Lint

Rode o guardião e **corrija todo ERRO antes de encerrar**:

```
python3 .claude/hooks/brain-lint.py
```

AVISO não bloqueia, mas entra como dúvida no relatório.

## 7. Encerrar

Diga em uma linha o que foi consolidado e qual é o foco de amanhã. Sem commit — o hook faz.
