# Agente `/simulado`

## O que faz
Registra o resultado do simulado **por matéria**, compara com o anterior e diz em quais matérias
você subiu e em quais caiu.

## O que ele sabe sobre você
Que simulado é **domingo** (manhã e tarde) e que a prova antiga de **segunda** é estudo, não
teste — ele não trata as duas do mesmo jeito nem cobra tempo na de segunda.

## Como usar
```
/simulado             registrar o de hoje
/simulado historico   ver a evolução
```

## O que ele pergunta
Nota por matéria (nunca só a geral) · tempo que sobrou ou faltou · quais questões errou ·
como você se sentiu (cansaço, ansiedade, travou onde).

## Onde grava
`Projetos/Vestibular/simulados/AAAA-MM-DD-<nome>.md`, os erros no banco de erros, e atualiza o
número que importa no `STATUS.md`.

## 🔗 Relacionados
[[questoes]] · [[plano]] · [[Vestibular]]
