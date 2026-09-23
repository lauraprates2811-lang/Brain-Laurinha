# 2026-09-22 — Vestibular

## Banco das provas antigas da FGV Direito SP

**O que era**
A Laura quer perguntar ao Brain "o que mais cai" e receber resposta com número. Para isso, todas
as questões das provas antigas precisavam virar um banco organizado por ano, matéria e tema. Ela
mandou 6 edições (zips das provas, grades e gabaritos): 2021.1, 2022.1, 2023.1, 2024.1, 2025.1 e
2026.1.

**Desafios**
1. Metade do material era escaneado (prova objetiva de 2025.1, gabaritos de 2023.1): sem texto.
2. Os gabaritos oficiais não são tabela: são a própria prova com a resposta grifada em amarelo.
3. Cada edição tem um formato: 2021.1 foi toda discursiva (prova própria da Direito SP, na
   pandemia); 2022.1 teve só Matemática e Inglês como objetivas; de 2023.1 em diante o formato é
   fixo. 2023.1 tem dois cadernos objetivos numerados de 1 a 30 cada.
4. Vieram junto reaplicações (Inglês de 2022.1 em 26/11/2021, redação de 2023.1), que não podem
   entrar na contagem.

**Como resolvi**
- PDFs com texto: extração direta. Escaneados: OCR do próprio macOS (Vision), com um detector de
  amarelo que marca a alternativa grifada. Onde o OCR falhou, o gabarito foi lido olhando a imagem
  da página.
- Cada questão virou uma linha de CSV (um arquivo por edição) com matéria, tema, subtema,
  gabarito, valor, palavras-chave e um resumo. Os temas saem de uma lista fechada
  (`temas.json`), senão os números não batem entre os anos.
- `banca.py` valida o banco e responde ranking, busca, linha do tempo de um tema e recomendação
  com peso maior para as provas mais recentes.
- Reaplicações ficaram fora da contagem, anotadas no topo do CSV da edição.

**Ferramentas**
PyMuPDF · OCR do macOS (Swift + Vision) · Python · leitura das páginas como imagem.

**O que aprendi**
- **A prova é estável desde 2023.1:** objetiva com 15 Matemática, 15 Português, 15 Inglês e 15
  Humanas (sempre 3 Atualidades, 6 História, 6 Geografia, nessa ordem); discursiva com 8 Humanas,
  8 Português, 5 Artes e a Redação.
- **Literatura é quase metade de Português objetiva:** 7 de 15 em cada uma das 4 últimas provas.
- **Matemática:** porcentagem, probabilidade e álgebra caíram nas 6 provas.
- **Artes repete autores:** Castells em 3 provas; "Revolution", dos Beatles, em 2; Antonio
  Candido em 3 questões.
- **Redação:** metade dos temas é sobre direitos e liberdades (linguagem neutra, laicidade,
  liberdade de expressão).
- **Grade das discursivas:** 100% completa e sem desvio de redação · 75% completa com desvio ·
  50% parcial sem desvio · 25% parcial com desvio. Um único erro de português derruba um nível.
  Em Humanas, às vezes vale ponto fixo por item citado (0,5 cada em 2025.1).

**O que errei**
- Escrevi que a Literatura de Português vinha "sempre de dois textos"; o próprio banco mostrou que
  2024.1 teve três. Corrigido antes de entregar.
- Três etiquetas inferidas, e não tiradas do texto da prova (Matopiba, Ponto IV, Embrapa), foram
  removidas ao revisar. Etiqueta é só o que está na prova.

**O que ficou aberto**
- O gabarito de 2026.1 é o preliminar: conferir o definitivo.
- O banco só tem as 6 provas que a Laura mandou; provas de antes de 2021 ficam de fora por
  enquanto (formato diferente).

## 🔗 Relacionados

[[2026-09-22]] · [[Vestibular]]
