# Projeto — Vestibular (material)

Hub da pasta de material do vestibular. A ficha de estado da área é `Areas/Vestibular.md`.

## O que tem aqui

| Pasta | O que guarda |
|---|---|
| `editais/` | Edital Unificado FGV 1º/2027 (PDF + texto extraído para `grep`), o conteúdo programático das provas (`conteudo-programatico-fgv-2027.pdf`) e toda resposta oficial |
| `provas-antigas/` | **A pasta única das provas antigas da FGV** (PDFs por edição, 2021.1–2026.1) e o `banco/` com todas as questões classificadas — consultado pelo `/banca`. A Laura abre pelo atalho `~/Downloads/Provas-FGV`. É a única cópia: os zips de Downloads foram para a Lixeira em 23/09. Em `2026.1/` há 3 arquivos de outro curso (Matemática discursiva e `RMH-T01`), fora do banco |
| `simulados/` | Resultado dos simulados de domingo, por matéria |
| `discursivas/` | As fichas (`.json`) das dissertativas corrigidas pelo `/discursiva` e o gerador `gerar_pdf.py`. O PDF corrigido vai para a matéria: `Projetos/Cursinho/<materia>/questoes-discursivas/` |
| `redacoes/` | Redações escritas e corrigidas (cursinho, Tarsila e `/redacao`) |
| `banco-erros/` | **Todo erro cometido**, com a causa. É o que alimenta o `/revisar`. Já tem: [[artes-e-questoes-contemporaneas]] · [[lingua-portuguesa]] |
| `oral/` | Trajetória biográfica, temas treinados e registro dos treinos de `/oral` |
| `comparativo-fgv-sp-rio-enade-oab.pdf` | Pesquisa pedida pelo representante da FGV Direito Rio (set/2026): grades SP × Rio, ENADE 2018/2022 e OAB 2018–2026 de FGV SP, FGV Rio, USP, UFMG, PUC-SP e PUC-Rio, com fontes oficiais |

## Como ler o edital sem estourar o contexto

O edital tem 119 páginas. Nunca leia inteiro. Use `grep` no texto extraído:

```
grep -n -i "exame oral" Projetos/Vestibular/editais/edital-unificado-fgv-2027.txt
```

Seções que já foram lidas e aproveitadas: 9.1.3 (vagas), 9.3.1 (estrutura da 1ª fase),
9.6 (exames internacionais), 9.7 (exame oral), 9.9 (cronograma), 14 (matrícula).

## Regra do banco de erros

Um arquivo por matéria, `banco-erros/<materia>.md`. Cada erro registra: a questão, o que ela
respondeu, **por que errou** (conceito · desatenção · interpretação · tempo) e a data.
Erro sem causa registrada não serve para revisão.

## 🔗 Relacionados

`Areas/Vestibular.md` · `Calendario.md`
