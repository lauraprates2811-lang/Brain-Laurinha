# Agente `/banca`

## O que faz
Responde **com números** o que mais cai na FGV Direito SP, a partir do banco com todas as questões
das provas antigas (2021.1 a 2026.1, 423 itens). Diz quantas vezes um tema apareceu, em quantas
edições, se está subindo ou sumindo, e recomenda o que estudar cruzando isso com o seu banco de erros.

## O que ele sabe sobre você
Lê `Regras/decisoes-estudo.md` antes de recomendar: dissertativa vem antes de objetiva,
Matemática é todo dia, e Redação, Português e Inglês eliminam abaixo de 3,0. Nunca conta de
cabeça — roda o `banca.py` e mostra a base de cada número.

## Como usar
```
/banca o que mais cai em matemática
/banca quantas vezes caiu literatura nos últimos 3 anos
/banca quais obras já caíram em Artes
/banca o que eu estudo essa semana
```

## Onde fica o banco
`Projetos/Vestibular/provas-antigas/banco/` — um CSV por edição (abre no Excel), a lista fechada
de temas (`temas.json`) e o script (`banca.py`). Os PDFs ficam em `provas-antigas/<edição>/`.

## 🔗 Relacionados
[[questoes]] · [[Vestibular]]
