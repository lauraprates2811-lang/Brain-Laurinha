# Agente `/questoes`

## O que faz
Gera questões no estilo da FGV (enunciado longo, com texto de apoio, exigindo interpretação) ou
corrige as que você fez, e **registra todo erro com a causa** no banco de erros.

## O que ele sabe sobre você
Seu bloco de 40 min prioriza **questões antigas e dissertativas**. Ele procura prova real em
`Projetos/Vestibular/provas-antigas/` antes de inventar questão. Sabe que Redação, Língua
Portuguesa e Inglês eliminam abaixo de 3,0, e trata essas com rigor extra.

## Como usar
```
/questoes historia-do-brasil Era Vargas 10
/questoes matematica
/questoes corrigir
```

## Onde grava
`Projetos/Vestibular/banco-erros/<materia>.md` — com a questão, o que você respondeu, o certo,
e **a causa** (conceito · interpretação · desatenção · tempo).

## 🔗 Relacionados
[[revisar]] · [[Vestibular]]
