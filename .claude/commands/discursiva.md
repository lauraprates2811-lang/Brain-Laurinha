---
description: Corrige a resposta da Laura a uma questão dissertativa pela grade da FGV Direito SP, guiada pelo gabarito, e entrega um PDF corrigido. Use SEMPRE, mesmo sem ela digitar /discursiva, quando ela mandar uma questão dissertativa com a resposta dela (e o gabarito/resposta indicada) para corrigir
---

# /discursiva — correção de dissertativa pela grade FGV, em PDF

A Laura manda **o enunciado, a resposta indicada (gabarito) e a resposta dela**. Você corrige
pela **grade da FGV Direito SP**, corrige a língua, diz o que melhorar e **entrega um PDF** com a
resposta dela marcada. Leia `Regras/decisoes-estudo.md` antes de corrigir.

**Uso:** `/discursiva` e cole (ou fotografe) enunciado + gabarito + sua resposta.
Várias questões de uma vez → um PDF só, com resumo das notas na frente.

## 1. Receber

- Separe as três partes: **enunciado**, **gabarito** (resposta indicada / grade) e **resposta dela**.
  Se faltar alguma, pergunte antes de corrigir. Sem gabarito dá para corrigir, mas diga que a nota
  fica menos segura.
- **Resposta em foto (manuscrita):** transcreva **exatamente** o que está escrito, com os erros
  dela — é isso que vai ser corrigido. Palavra ilegível vira `[ilegível]`; se ela mudar a nota,
  pergunte antes.
- **Questão de prova antiga?** Procure no banco:
  `python3 Projetos/Vestibular/provas-antigas/banco/banca.py busca "<palavra do enunciado>"`.
  Se achar, abra a **grade oficial** da edição em `Projetos/Vestibular/provas-antigas/<edição>/`
  (arquivos com `GC`, `grade` ou `GAB` no nome) e use a grade oficial daquela questão — ela manda
  mais que o gabarito que a Laura colou.

## 2. Corrigir pela grade FGV Direito SP

Estas são as regras que a FGV usa nas grades oficiais (2021.1–2026.1, todas no Brain).
**Não invente critério fora delas.**

**Grade por níveis** (é a padrão em Português, Artes e boa parte de Humanas), por questão ou por item:

| Nível | Quando |
|---|---|
| **100%** | resposta **completa/correta**, **sem** desvio de redação |
| **75%** | resposta completa/correta, **com** algum desvio de redação |
| **50%** | resposta **parcial**, sem desvio de redação |
| **25%** | resposta parcial, com desvio de redação |
| **0%** | não atende ao pedido |

- Questão com itens a) e b): cada item tem sua régua e vale a sua parte da questão
  (em Humanas 2026.1, 50% cada). Se o gabarito não disser o peso, divida igualmente e **avise**.
- Quando o enunciado pede "dois exemplos", "duas razões": dar só um é **parcial**.
- Em Português, **"sim" ou "não" sem justificativa correta não pontua**.
- **Desvio de redação** = erro de ortografia, acentuação, concordância, regência, crase,
  pontuação que atrapalhe o sentido, frase truncada ou registro informal. **Um desvio já derruba
  um nível.** Seja rigorosa: é assim que a banca corrige.

**Grade por elementos** (aparece em Humanas quando o enunciado pede uma lista, ex.: "aponte quatro
medidas"): cada elemento correto vale um valor fixo (em 2025.1, 0,5 cada). Use **só** quando a
grade oficial ou o gabarito disser isso; se não, use a grade por níveis.

**O gabarito é referência, não camisa de força.** As próprias grades da FGV dizem "o candidato
poderia citar diversas…" e aceitam respostas diferentes quando bem justificadas. Se a resposta dela
**atende ao que o enunciado pede** com conteúdo correto, **dê o crédito e diga isso com todas as
letras** no campo `de_acordo` ("Sua resposta está de acordo com o pedido, mesmo sendo diferente do
gabarito, porque…"). Se o conteúdo estiver errado, diga que está errado — sem suavizar.

**Nota honesta.** Nada de nota de consolo: nota inflada agora custa a vaga em outubro.

## 3. Montar a ficha e gerar o PDF

Grave a ficha em `Projetos/Vestibular/discursivas/AAAA-MM-DD-<materia>-<tema-curto>.json`.
Veja o formato completo com `python3 Projetos/Vestibular/discursivas/gerar_pdf.py --exemplo`.

Campos: `titulo` · `data` · `materia` · `origem` (ex.: "FGV 2025.1 · Humanas · questão 2", ou
"questão enviada pela Laura") · `valor` · `tipo_grade` (`niveis` ou `elementos`) · `enunciado` ·
`gabarito` · `grade` (a grade oficial, se houver) · `resposta_marcada` · `comentarios` · `itens` ·
`nota` · `de_acordo` · `gramatica` · `melhorar` · `reescrita`.

**`resposta_marcada` é o texto dela, palavra por palavra** — você só acrescenta marcas, nunca
corrige em silêncio:

| Marca | Aparece como | Uso |
|---|---|---|
| `{-trecho-}` | riscado vermelho | o que tirar |
| `{+trecho+}` | verde | o que colocar |
| `[[trecho]]` | grifo amarelo | trecho comentado |
| `…\|n` no fim de qualquer marca | número sobrescrito | liga ao comentário `n` |

Faça a menor correção possível — `remuneradas{+,|1+} a jornada` — e não reescreva a frase inteira.

- `comentarios`: `{"n", "tipo": "gramatica" | "conteudo" | "elogio", "texto"}` — aponte também o
  que está **bom** (tipo `elogio`); ela precisa saber o que repetir.
- `itens`: um por item da grade — `item`, `esperado` (o que a grade pede), `voce` (o que ela fez),
  `nivel` (100%…0%), `pontos`.
- `nota`: `obtida`, `maxima`, `percentual`, `criterio` (uma frase: "Item a completo; item b
  parcial e com desvio de redação").
- `gramatica`: cada desvio — `trecho`, `correcao`, `regra` (a regra em uma linha, sem jargão).
- `melhorar`: **no máximo 3**, concretos e em ordem do que mais rende ponto.
- `reescrita`: **as ideias dela**, com as correções e o que faltou para 100%. Não é um gabarito
  novo — é a versão dela que tiraria nota máxima.

Várias questões → a ficha é uma **lista** de fichas, num arquivo só.

Gere e confira:
```
python3 Projetos/Vestibular/discursivas/gerar_pdf.py Projetos/Vestibular/discursivas/<ficha>.json
```
Se aparecer ❌ ou ⚠️, conserte a ficha e gere de novo. Depois **entregue o PDF para a Laura**
(envie o arquivo na conversa).

## 4. Registrar o erro

Todo item abaixo de 100% vai para `Projetos/Vestibular/banco-erros/<materia>.md`, no formato do
`/questoes`, com a **causa**: `conceito` · `interpretacao` · `desatencao` · `tempo` — e, quando a
perda veio de língua, diga qual desvio foi. Erro sem causa registrada não serve para nada.

## 5. Responder no chat

Curto: a nota (ex.: **0,75 / 1,0 — 75%**), uma frase de veredito, **o** ponto que mais rende
melhorar, e o PDF. Os detalhes estão no PDF — não repita tudo no chat.
Termine sugerindo a linha do `/save` (ex.: *"Entra como bloco de Humanas: 2 discursivas, média
62,5%, perda por desvio de redação no item b"*).
