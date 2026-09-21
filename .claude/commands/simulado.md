---
description: Registra o resultado de um simulado por matéria e atualiza o painel
---

# /simulado — registro do simulado

O simulado é **domingo**, manhã e tarde. A prova antiga de **segunda** é estudo, não teste —
não registre as duas do mesmo jeito.

**Uso:** `/simulado` (registrar o de hoje) · `/simulado historico` (ver a evolução)

## O que perguntar

1. Qual simulado (cursinho, prova antiga da FGV, Insper) e a data
2. **Nota por matéria** — sempre separada, nunca só a nota geral
3. Quanto tempo sobrou ou faltou
4. Quais questões ela errou (para o banco de erros)
5. Como ela se sentiu — cansaço, ansiedade, travou em alguma prova

## Onde grava

`Projetos/Vestibular/simulados/AAAA-MM-DD-<nome>.md`:

```
# Simulado — <nome> — AAAA-MM-DD

| Matéria | Acertos | Total | % |
|---|---|---|---|

**Tempo:** <sobrou/faltou>
**O que travou:** <uma linha>
**Comparação com o anterior:** <subiu/caiu, em quais matérias>
```

Todo erro vai também para `Projetos/Vestibular/banco-erros/<materia>.md` com a causa.

## Depois de registrar

- Compare com o simulado anterior e diga **em quais matérias subiu e em quais caiu**
- Aponte a matéria com pior tendência — é ela que o `/plano` tem que atacar
- Atualize o número que importa na ficha [[Vestibular]] e no `STATUS.md`
- Sugira a linha do `/save`

Seja honesta com os números. Simulado existe para doer agora em vez de doer em outubro.
