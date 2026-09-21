---
description: Rotina semanal de manutenção da forma do Brain (roda sozinha na segunda 07:00)
---

# /otimizar — manutenção semanal

Cuida da **forma** do Brain, não do conteúdo. Roda sozinha toda segunda às 07:00 via launchd,
mas pode ser chamada à mão a qualquer momento.

## 1. Medir

```
python3 .claude/hooks/brain-lint.py --medir
```

Registre os números: tamanho do `STATUS.md`, entradas no painel, tamanho de cada ficha,
linhas de histórico, notas órfãs, links quebrados.

## 2. Corrigir todo ERRO, mecanicamente

Sem pedir permissão, porque é sempre a mesma correção:

- `STATUS.md` com mais de 14 entradas ou acima de 20 KB → rotacionar para `STATUS-historico.md`
- Ficha com mais de 6 linhas de histórico → rotacionar para `<Area>-historico.md`
- Índice de dia com conteúdo além da lista → mover o conteúdo para a parte da área certa
- Parte do dia sem índice → criar o índice
- Parte do dia sem link para o dia ou para a ficha → acrescentar
- Memória ou doc de projeto linkando índice → trocar por crase
- Arquivo solto na raiz → mover para `Projetos/<X>/`
- Nome com espaço ou acento → renomear

## 3. Tratar os AVISOS com julgamento

AVISO não se corrige no automático. O que precisar de decisão da Laura **vira dúvida no
relatório** e tarefa em `Tarefas/dados/tarefas.json`. Exemplos: ficha grande demais (dividir?),
nota órfã (linkar ou apagar?), possível segredo (conferir e remover).

## 4. Conferir o que o lint não vê

- **`STATUS.md` × `Tarefas/`** — o painel está mentindo sobre alguma área? Tarefa fechada ainda
  aparecendo como próximo passo?
- **Hubs × pastas** — nasceu pasta sem hub, ou o hub lista coisa que não existe mais?
- **`Calendario.md` × hoje** — alguma data passou sem registro?
- **Memória do Claude** — o que ele sabe sobre a Laura ainda é verdade?

## 5. Marcar e relatar

```
python3 .claude/hooks/brain-lint.py --marcar-otimizacao
```

Grave o relatório em `Memoria/AAAA-MM-DD-brain.md` e acrescente **1 linha** em
"Últimas atualizações" do `STATUS.md`.
