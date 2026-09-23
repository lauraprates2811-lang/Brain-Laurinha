---
description: Gera e corrige questões no estilo da banca, e registra todo erro no banco de erros
---

# /questoes — o motor dos 40 minutos

Serve o bloco de 40 minutos do método da Laura. Leia `Regras/decisoes-estudo.md` antes de agir.

**Uso:** `/questoes <matéria> [tema] [quantidade]`
Ex.: `/questoes historia-do-brasil Era Vargas 10` · `/questoes matematica` · `/questoes corrigir`

## Regras da banca (FGV Direito SP)

- **Dissertativa tem prioridade sobre objetiva.** É o que ela já faz e o que o edital premia.
- Matérias que caem: Redação · Ciências Humanas (História, Geografia, Atualidades) ·
  Matemática · Língua Portuguesa · Inglês · Artes e Questões Contemporâneas.
- Provas com corte eliminatório abaixo de 3,0: Redação, Língua Portuguesa (discursiva e objetiva)
  e Inglês. Questão dessas matérias merece rigor extra.

## Como gerar

1. Pergunte a matéria e o tema, se não vierem no comando.
2. Antes de inventar questão, **procure prova antiga**: rode
   `python3 Projetos/Vestibular/provas-antigas/banco/banca.py tema "<tema>"` (ou `busca`) para achar
   as questões reais e abra o PDF da edição em `Projetos/Vestibular/provas-antigas/<edição>/`.
   Questão real da banca vale mais que questão criada.
3. Gere no estilo da FGV: enunciado longo, com texto de apoio, exigindo interpretação —
   não pergunta seca de decoreba.
4. Aplique uma de cada vez. Espere a resposta antes de mostrar a próxima.

## Como corrigir

Para cada erro, identifique **a causa**, e seja específico:

| Causa | O que significa |
|---|---|
| `conceito` | não sabia o conteúdo |
| `interpretacao` | sabia, mas leu errado o enunciado |
| `desatencao` | sabia e errou bobeira |
| `tempo` | não deu tempo de fazer direito |

## Onde grava

**Todo erro** vai para `Projetos/Vestibular/banco-erros/<materia>.md`:

```
### AAAA-MM-DD — <tema>
**Questão:** <enunciado resumido>
**Respondi:** <o que ela pôs>   **Correto:** <o certo>
**Causa:** conceito | interpretacao | desatencao | tempo
**O que revisar:** <uma linha>
```

## Ao terminar

Diga: quantas acertou, a causa mais frequente dos erros, e **sugira a linha do `/save`**.
