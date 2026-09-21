---
description: Ritual de fim de bloco de estudo — registra o que aconteceu e atualiza o Brain
---

# /save — fim de bloco

Ritual executado ao fim de **cada bloco de estudo ou de trabalho**. Ordem fixa, sem pular passo.

Antes de começar, leia `STATUS.md` inteiro e identifique **quais áreas foram tocadas** neste bloco.
Se não estiver claro o que aconteceu, pergunte à Laura antes de escrever.

## Passo 1 — `STATUS.md`

- Adicione **uma entrada de até 2 linhas** no topo de "Últimas atualizações", apontando para
  `[[AAAA-MM-DD-<area>]]`. Máximo **14 entradas**; o excedente vai para `STATUS-historico.md`.
- Atualize a linha da área na tabela "Áreas". Cada célula em **3–4 linhas**, sem narrativa.
- Mexa em "Alertas críticos" **só** se algo passou a travar prazo ou nota, ou deixou de travar.

## Passo 2 — ficha da área tocada (`Areas/<Area>.md`)

- Atualize o cabeçalho `> **Status:**` (1 a 3 linhas).
- Atualize as pendências: marque o que foi feito, acrescente o que nasceu.
- Acrescente **uma linha nova** na tabela "Histórico (últimas entradas)".
  A tabela tem **6 linhas**; a mais antiga desce para `Areas/<Area>-historico.md`
  (crie o arquivo se ainda não existir).

## Passo 3 — memória do dia

Crie ou atualize `Memoria/AAAA-MM-DD-<area>.md` para **cada área tocada**. Cada tarefa registrada
responde:

- **O que era** · **Desafios** · **Como resolvi** · **Ferramentas** · **O que ficou aberto**
- **O que aprendi** — sempre
- **O que errei** — sempre, e todo erro de questão também vai para
  `Projetos/Vestibular/banco-erros/<materia>.md`

Atualize o índice `Memoria/AAAA-MM-DD.md` com **só a lista das partes do dia**, nada mais.

Rodapé da parte do dia: `[[AAAA-MM-DD]]` + a ficha da área. **Nunca** linkar `STATUS.md`,
`Calendario.md` ou `Regras/` a partir da memória — cite em crase.

## Passo 4 — regra nova, se surgiu

Se o bloco produziu um aprendizado que vale para o futuro, grave no arquivo certo de `Regras/`
(`decisoes.md` · `decisoes-estudo.md` · `decisoes-tecnicas.md` · `agenda.md`), no formato:

```
## Título que já é a regra (AAAA-MM-DD)

<o caso que gerou a regra>

**A regra:** <o que fazer daqui para frente>
```

Não invente regra. Só grave o que realmente aconteceu.

## Passo 5 — sincronizar as tarefas

Em `Tarefas/dados/`: feche o que saiu, crie o que nasceu, atualize `atualizado` da área em
`areas.json`. Se nasceu uma data sem volta, ela entra também em `prazos.json` e no `Calendario.md`.

## Passo 6 — conferir a forma

Em todo arquivo tocado: wikilinks corretos, direção do grafo respeitada, rodapé
`## 🔗 Relacionados` presente.

## Passo 7 — relatar

Liste o que mudou, em uma linha por arquivo. **Não faça commit** — o hook faz sozinho.
