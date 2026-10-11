---
description: Responde com números o que mais cai na FGV e no Insper (provas de Direito), a partir do banco de provas antigas. Use SEMPRE, mesmo sem a Laura digitar /banca, quando ela perguntar sobre provas ou questões antigas, o que mais cai ou apareceu, quantas vezes um tema caiu, estatística ou frequência de matérias, ou o que estudar/priorizar com base na prova
---

# /banca — o estatístico das provas antigas

Responde perguntas como "o que mais cai em Humanas?", "quantas vezes caiu logaritmo nos últimos
3 anos?" ou "o que eu estudo essa semana?" **com números tirados do banco**, nunca de memória.
Leia `Regras/decisoes-estudo.md` antes de recomendar qualquer coisa.

**Uso:** `/banca <pergunta em português>`
Ex.: `/banca o que mais cai em matemática` · `/banca literatura nos últimos 3 anos` ·
`/banca o que estudar essa semana`

## Onde está o banco

`Projetos/Vestibular/provas-antigas/banco/`

| Arquivo | O que é |
|---|---|
| `AAAA.S.csv` | Uma linha por questão de uma edição (separador `;`). Colunas: edicao · prova · numero · materia · tema · subtema · gabarito · valor · tags · resumo |
| `temas.json` | Lista **fechada** de temas por matéria. Toda questão usa um deles |
| `banca.py` | Lê, valida e conta. Nunca altera os CSVs |

Os PDFs originais ficam em `Projetos/Vestibular/provas-antigas/<edição>/`.

## Banco do Insper (subpasta `insper/`)

Mesmo formato, mesmo `temas.json`, mesmo script: acrescente **`--vest insper`** em qualquer comando
(sem ele, a conta é só da FGV). Ex.: `python3 banca.py tema figuras --vest insper`.

- **Só provas que valem para Direito**, por decisão da Laura (11/10/2026): 2026.1 (30/11/2025, números
  1–60, e a reaplicação de 21/12/2025, números R1–R60) e 2026.2 (07/06/2026). São 183 itens: 180
  objetivas e 3 redações (número R; a da reaplicação é RR).
- As provas de 2016 a 2020 que estão no site **não entram**: a capa lista só Administração, Economia
  e Engenharias. As de 2021 a 2025 o Insper não publica.
- Formato (2026): Português 1–15 · Matemática 16–30 · História 31–35 · Geografia 36–41 ·
  Filosofia/Sociologia 42–45 · Biologia 46–50 · Química 51–55 · Física 56–60. Não tem Inglês.
- Os PDFs **não estão no Brain**: foram lidos no site (provas-e-gabaritos), sem baixar. Gabarito oficial
  conferido letra por letra. Para mandar a Laura à prova real, dê o id e o link da página do Insper.
- Base pequena (3 provas): diga isso sempre que der um número do Insper.

## Como responder

1. **Traduza a pergunta num comando** e rode. Nunca conte na mão, nunca estime.
   ```
   cd Projetos/Vestibular/provas-antigas/banco
   python3 banca.py ranking --materia Matemática            # o que mais cai numa matéria
   python3 banca.py ranking --materia História --ultimas 3  # só as 3 últimas edições
   python3 banca.py ranking --desde 2023.1 --por materia    # formato atual da prova
   python3 banca.py ranking --materia Artes --por subtema   # obras e autores
   python3 banca.py tema logaritmo                          # linha do tempo de um tema
   python3 banca.py busca "Machado"                         # autor, obra, palavra-chave
   python3 banca.py recomendar --materia Geografia          # frequência com peso de recência
   python3 banca.py edicoes                                 # o que tem em cada edição
   ```
2. **Responda em uma frase com o número** e depois mostre a tabela curta.
   Ex.: *"Probabilidade caiu 9 vezes em 79 questões de Matemática (11%), em todas as 6 edições."*
3. **Sempre diga a base**: quantas questões e quais edições entraram na conta.
4. Quando citar questões, dê o id (`2025.1-OBJ-14`) e onde está o PDF, para ela abrir a prova real.

## Os limites que você sempre precisa lembrar

- O banco tem **6 edições (2021.1 a 2026.1)**, só as que a Laura mandou. Diga isso quando a
  pergunta for "até hoje" ou "sempre".
- **2021.1 foi toda discursiva** (prova própria da Direito SP, na pandemia) e **2022.1 teve só
  Matemática e Inglês como objetivas**. Para "como é a prova hoje", use `--desde 2023.1`: de
  2023.1 a 2026.1 o formato é o mesmo.
- **A classificação por tema foi feita pelo Claude**, lendo cada questão. Para ranking isso
  quase não muda o resultado, mas uma questão isolada pode estar no tema vizinho.
- O gabarito de 2026.1 é o **preliminar** oficial. Questões anuladas têm `ANULADA` no gabarito.
- Duas reaplicações (2022.1 e a redação de 2023.1) ficaram **fora da contagem**, anotadas no
  topo do CSV da edição.

## O que o banco já mostra sobre o formato (2023.1–2026.1)

- **Objetiva, 60 questões:** Matemática 15 · Língua Portuguesa 15 · Inglês 15 ·
  Ciências Humanas 15 (sempre 3 de Atualidades, 6 de História, 6 de Geografia, nessa ordem).
- **Discursiva:** Ciências Humanas 8 (em geral 4 de História e 4 de Geografia) · Língua Portuguesa 8 ·
  Artes e Questões Contemporâneas 5 · Redação 1.
- Em Língua Portuguesa objetiva, **7 das 15 questões são de Literatura** em todas as edições desse
  período, sobre dois ou três textos literários.

Confira com `banca.py edicoes` antes de repetir esses números. Se um CSV novo mudar a conta,
vale o script.

## Como recomendar o que estudar

Recomendação = **o que mais cai** × **o que ela mais erra** × **as regras dela**.

1. `banca.py recomendar --materia <M>` para cada matéria em jogo.
2. Leia `Projetos/Vestibular/banco-erros/<materia>.md`. Se estiver vazio, diga isso claramente:
   a recomendação sai só pela frequência, e cada `/questoes` que ela fizer vai melhorar a próxima.
3. Aplique as regras de `Regras/decisoes-estudo.md`: dissertativa antes de objetiva, Matemática
   todo dia, rigor extra nas matérias que eliminam abaixo de 3,0 (Redação, Língua Portuguesa, Inglês).
4. Entregue **3 a 5 temas**, cada um com o número que o justifica e as questões reais para treinar.
   Ex.: *"Literatura: 7 de 15 questões de Português em cada uma das 4 últimas provas. Treine com
   2024.1-OBJ-21 a 25 (Estorvo e Os sertões)."*

## Quando chegar prova nova

1. Salve os PDFs em `Projetos/Vestibular/provas-antigas/<edição>/`.
2. Crie `banco/<edição>.csv` no mesmo formato, usando só temas de `temas.json`. Se precisar de
   tema novo, acrescente em `temas.json` primeiro e avise a Laura.
3. Rode `python3 banca.py validar` até dar ✅.
4. Nunca preencha gabarito de memória: sem gabarito oficial, deixe a coluna vazia.

## Ao terminar

Se a resposta trouxe algo que o Brain ainda não sabia (uma decisão de estudo, um tema novo que
entrou no plano), **sugira a linha do `/save`**. Se foi só consulta, não sugira.
