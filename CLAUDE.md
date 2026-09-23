# CLAUDE.md — como operar o Brain da Laura

Este arquivo ensina o Claude a operar este Brain. Leia-o inteiro no início de toda sessão.
Não linkar este arquivo em nenhuma nota.

## Quem é a dona

Laura Amaro Prates Pereira (Laurinha), 17 anos, senior na EABH, estudando para Direito na FGV.
Perfil completo em `Sobre/Laura.md`. Fale em português, direto, sem jargão técnico.

## A regra de ouro

**Nenhum segredo em arquivo nenhum.** Nunca grave senha, token, chave de API ou login.
Registre apenas *qual acesso é preciso* e *onde a senha está guardada*
(ex.: "portal do cursinho — senha no gerenciador de senhas").

## As quatro camadas

| Camada | Arquivo | O que é | Tamanho |
|---|---|---|---|
| **Painel** | `STATUS.md` | Estado de tudo, em uma tela | ≤ 20 KB |
| **Ficha** | `Areas/<Area>.md` | Estado **atual** de uma frente | ≤ 60 KB |
| **Memória** | `Memoria/AAAA-MM-DD-<area>.md` | A história, dia × área | livre |
| **Lista** | `Tarefas/dados/*.json` | O que fazer — fonte de verdade | — |

`Calendario.md` é a linha do tempo: toda data que importa, em ordem, com o que falta fazer antes dela.

## Ordem de leitura (nunca ler tudo)

1. `STATUS.md` inteiro — sempre.
2. A ficha da área do pedido — só as seções necessárias.
3. `Regras/` por `grep` no título, lendo só o bloco que casou.
4. `Memoria/AAAA-MM-DD-<area>.md` só do dia e da área que interessam.
5. Históricos (`*-historico.md`) **só por `grep`**, nunca inteiros.
6. O hub do projeto quando for mexer na pasta dele.

Estourar o contexto é o erro mais caro que existe aqui. Na dúvida, leia menos.

## Formato das fichas (`Areas/`)

```
# <Area>
> **Status:** <1 a 3 linhas: onde está, o número que importa, o próximo passo>

## O que é
## Pendências
## Regras da área
## Projeções          ← preenchido pelo /sono
## Histórico (últimas entradas)   ← tabela de no máximo 6 linhas
## 🔗 Relacionados
```

Quando a tabela passar de 6 linhas, a mais antiga vai para `Areas/<Area>-historico.md`.

## Memória = dia × área

Uma nota por área tocada no dia: `Memoria/AAAA-MM-DD-<area>.md`.
O índice do dia (`Memoria/AAAA-MM-DD.md`) contém **só a lista das partes**, nada mais.

Cada tarefa registrada responde:
- o que era · desafios · como resolvi · ferramentas · o que ficou aberto

E, por ser estudo, sempre também:
- **o que aprendi** · **o que errei** ← isto alimenta `/revisar` e o banco de erros

## Wikilinks e direção do grafo

- Toda nota termina em `## 🔗 Relacionados`.
- **Índices linkam para baixo:** `STATUS.md`, `Calendario.md`, `Regras/*` podem linkar fichas e projetos.
- **Folhas linkam para o hub:** doc de projeto → hub do projeto.
- **Memória e docs de projeto NUNCA linkam índices.** Citam em crase: `STATUS.md`, `Calendario.md`.
- Parte do dia (`AAAA-MM-DD-<area>.md`) linka `[[AAAA-MM-DD]]` + a ficha da área. Só isso.
- Comandos se citam em crase (`/save`), nunca em colchetes.
- Não linkar `CLAUDE.md` nem `README.md`.

É essa disciplina que faz o grafo do Obsidian virar clusters por área em vez de uma bola de lã.

## Hub de projeto tem sufixo `-projeto`

A ficha da área e a pasta do projeto têm o mesmo nome (Vestibular, Cursinho, Escola, Brain).
Para o wikilink não ficar ambíguo, o hub da pasta se chama `<Nome>-projeto.md`:
`[[Vestibular]]` é a **ficha**, `Projetos/Vestibular/Vestibular-projeto.md` é o **material**.

## Raiz limpa

Nada solto na raiz além de: `CLAUDE.md`, `STATUS.md`, `STATUS-historico.md`, `Calendario.md`, `README.md`.
Material de estudo, PDF, edital, prova antiga → `Projetos/<X>/`.
Material que o Claude cria para uma matéria (flashcards, mapa mental, apostila, resumo) →
`Projetos/Cursinho/<materia>/`, em `.md` e, se tiver flashcards, também em `.html`. A Laura abre
essas pastas pelo atalho `~/Downloads/Materias`, e as provas antigas pelo `~/Downloads/Provas-FGV`.
Ver `Regras/decisoes-tecnicas.md`.

## Não inventar

Se não souber uma data, uma nota, um nome de professor ou o que cai numa prova: **pergunte**,
ou escreva `[a confirmar]` e crie uma tarefa para confirmar na fonte oficial.
Nunca preencha um número de nota, uma data de prova ou uma regra de edital de memória.

## Não criar estrutura nova sem perguntar

Arquivo novo dentro do padrão existente: pode.
Pasta nova, área nova ou tipo de arquivo novo: só com o ok da Laura.

## Os rituais

- `/save` — fim de cada bloco de estudo. 7 passos fixos.
- `/sono` — fim do dia. Consolida, reorganiza, projeta cenários, roda o lint.
- `/otimizar` — segunda 07:00, sozinho via launchd. Conserta a forma do Brain.
- `/tarefas` — opera a lista.

### Sugerir o `/save` — obrigatório

**Toda conversa que produziu alguma coisa termina com a sugestão do `/save`.** Não espere a
Laura lembrar: a última linha da sua resposta final é o convite, dizendo em meia linha o que
seria gravado. Exemplo: *"Fecha com `/save`? Entra como bloco de Física, 2h, com os 4 erros de
cinemática."*

Vale para bloco de estudo, correção de redação, decisão tomada, descoberta sobre prazo ou
edital — qualquer coisa que o Brain deveria saber amanhã e ainda não sabe.

Não sugira quando a conversa foi só pergunta e resposta, sem nada novo para guardar.
Sugestão em conversa vazia vira ruído e ela para de obedecer.

## Os agentes de estudo

`/questoes` · `/oral` · `/redacao` · `/revisar` · `/explica` · `/simulado` · `/plano` · `/banca` · `/discursiva`

**O `/banca` é acionado sozinho.** Toda pergunta sobre provas ou questões antigas, o que mais
cai, quantas vezes um tema apareceu, estatística de matérias ou o que priorizar com base na
prova passa pelo `/banca` — mesmo que a Laura não digite o comando. Número sobre a prova sai do
banco (`Projetos/Vestibular/provas-antigas/banco/`), nunca de memória.

**O `/discursiva` também é acionado sozinho.** Questão dissertativa enviada com a resposta dela
(e o gabarito) é corrigida pela grade da FGV Direito SP e **sempre** volta como PDF corrigido,
gravado na pasta da matéria, em `Projetos/Cursinho/<materia>/questoes-discursivas/` (a ficha `.json`
fica em `Projetos/Vestibular/discursivas/`). Redação continua no `/redacao`.

Um hook (`.claude/hooks/agentes-gatilho.py`) lembra desses dois agentes a cada mensagem que casa
com o assunto deles.

Todo agente, antes de agir, lê `Regras/decisoes-estudo.md`. Todo agente grava o resultado
no lugar certo e termina sugerindo a linha para o `/save`. Documentação em `Agentes/`.

## Contexto que muda tudo (leia antes de priorizar qualquer coisa)

1. **Exame Oral da FGV tem peso 2, elimina com nota ≤ 3,0, e só pode ser feito UMA vez** —
   faltar zera o oral em todas as três portas (Vestibular, ENEM, Internacional).
2. **Conclusão do ensino médio é obrigatória para a matrícula (05–15/01/2027)** e a EABH só
   forma a Laura no meio de 2027. Sem resolver isso, aprovação não vira vaga.
   Ver `Areas/Certificacao.md`. Isso tem prioridade sobre qualquer matéria.
3. A inscrição pela via **SAT (2 vagas, nota ≥ 1.200) vai até 18/12/2026** — depois do
   resultado final (07/12). É a carta na manga, não perder o prazo.

## O que não fazer

- Inventar dado. · Criar estrutura sem alinhar. · Deixar arquivo solto na raiz.
- Engordar `STATUS.md` ou ficha com narrativa (narrativa mora na memória).
- Terminar um bloco de trabalho sem `/save`.
- Gravar segredo.
