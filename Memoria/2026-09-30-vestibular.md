# 2026-09-30 — Vestibular

## Edital do Insper: como funciona a nota

**O que era**
Ela mandou o edital do Insper 2027.1 e perguntou como funciona a nota e os pesos de cada matéria.

**Desafios**
- O PDF (40 páginas) não abria pelo leitor comum; foi lido pelo PyMuPDF.

**Como resolvi**
Li a estrutura da prova (p. 12), a apuração (p. 15–17) e o cronograma (p. 4–5). Para Direito:
- Prova única em 11/10: 60 objetivas (15 de Linguagens, 15 de Matemática, 15 de Humanas e 15 de Natureza) e redação, em 5h.
- Pesos das objetivas: Linguagens 40, Matemática 20, Humanas 30, Natureza 10.
- Nota final = 0,75 × objetivas + 0,25 × redação.
- Peso real na nota final: Linguagens 30%, Redação 25%, Humanas 22,5%, Matemática 15%, Natureza 7,5%.
- Elimina quem tira menos de 30 em Linguagens, Matemática, Humanas e redação, ou menos de 20 em Natureza.
- 76 vagas, 53 delas pelo vestibular.
- 1ª chamada 17–20/11, 2ª 24–27/11, 3ª 01–04/12. Recurso do gabarito em 13–14/10.

O edital foi para `Projetos/Vestibular/editais/edital-insper-2027-1.pdf`, com a versão `.txt` ao lado.

**Ferramentas**
PyMuPDF, `grep`.

**O que ficou aberto**
- O edital não diz como os acertos viram nota (0 a 100). As contas supõem que é proporcional.

**O que aprendi**
- No Direito do Insper, Português e Redação valem 55% da nota. A prioridade é a mesma da FGV.
- Desempate: redação, depois Linguagens, Matemática e Humanas.

**O que errei**
Nada registrado: não houve questão.

## "Eu passo em Direito?" — conta com as previsões dela

**O que era**
Ela estimou quantas acertaria: Natureza 4, Matemática 6, Humanas 10, Linguagens 10 a 12 (de 15) e
Redação 7 a 8 (de 10). Perguntou se passa.

**Desafios**
- O Insper não publica nota de corte. A busca na web não achou nenhuma.

**Como resolvi**
Pela fórmula do edital, a nota final dela fica entre **60,5 e 67**, sem ser eliminada.
A chance, uns 35%, é **estimativa do Claude** e não dado oficial.
A folga é de 1 questão em Matemática (mínimo de 5 acertos) e de 1 em Natureza (mínimo de 3).
Quanto cada ganho sobe a nota final:
- +1 ponto na redação: +2,5
- +1 acerto em Linguagens: +2
- +1 acerto em Humanas: +1,5
- +1 acerto em Matemática: +1
- +1 acerto em Natureza: +0,5

**Ferramentas**
Busca na web (sem resultado de nota de corte).

**O que ficou aberto**
- Nada.

**O que aprendi**
- O risco real está em Natureza: 4 acertos de chute é praticamente o acaso (média de 3).

**O que errei**
Nada registrado: não houve questão.

## Gabaritos do Insper: as letras de Natureza

**O que era**
Ela vai chutar Natureza numa letra só e perguntou se poderia acertar só 2. Pediu os gabaritos antigos.

**Desafios**
- A página da Vunesp pede login; o Claude não entra em conta dela.
- O site do Insper bloqueia download fora do navegador, e abrir o PDF gerou uma janela de salvar
  no navegador dela.
- O gabarito do simulado de abril/2026 é uma imagem de bolinhas e não foi lido.

**Como resolvi**
Li, dentro do navegador, 4 gabaritos oficiais da página "Provas e Gabaritos" do Insper: 2026.1
(30/11/2025), a reaplicação de 2026.1 (21/12/2025), 2026.2 (07/06/2026) e o simulado de set/2026.
Nas 4 provas, a ordem de Natureza é a mesma: 46–50 Biologia, 51–55 Química e 56–60 Física.

Letras certas em Natureza (A-B-C-D-E):
- 2026.1: 1-3-4-4-3
- 2026.1-R: 1-3-4-2-5
- 2026.2: 4-2-5-2-2
- Simulado: 4-4-3-2-2

Chutando tudo numa letra, ela seria eliminada em 8 de 20 casos. A letra **C** nunca eliminaria:
saiu 16 vezes em 60. A estratégia virou regra em `Regras/decisoes-estudo.md` (30/09).

**Ferramentas**
Navegador do app, pdf.js, Python.

**O que ficou aberto**
- Guardar as provas do Insper no Brain pede pasta nova: ela não decidiu.

**O que aprendi**
- A banca do Insper não distribui as letras por igual dentro de Natureza.

**O que errei**
- Antes de ver os dados, o Claude estimou 25% de risco com a mesma letra. O real foi 40%. Estimativa
  sem dado ficou otimista.

## FGV Matemática: as letras do gabarito

**O que era**
Ela pediu a mesma contagem de letras para a Matemática objetiva da FGV.

**Desafios**
- Nenhum.

**Como resolvi**
Contei o gabarito do banco: 70 questões, de 2022.1 a 2026.1. O gabarito de 2026.1 ainda é o preliminar.
- Em 2024.1 e 2025.1 veio exatamente 3-3-3-3-3.
- Em 2026.1 veio 3-4-3-3-2.
- Em 2023.1 veio 1-4-3-4-3.
- Português e Inglês também vieram 3-3-3-3-3 em 2024.1 e 2025.1.

Chutar tudo numa letra dá cerca de 3 acertos. A regra do chute pela letra que menos marcou foi para
`Regras/decisoes-estudo.md` (30/09).

**Ferramentas**
`banca.py` (não tem contagem de letras) e Python lendo os CSVs do banco, só leitura.

**O que ficou aberto**
- Nada.

**O que aprendi**
- FGV e Insper são opostos no gabarito: a FGV equilibra as letras e o Insper não.

**O que errei**
Nada registrado: não houve questão.

## 🔗 Relacionados

[[2026-09-30]] · [[Vestibular]]
