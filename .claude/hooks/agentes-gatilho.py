#!/usr/bin/env python3
"""agentes-gatilho — aciona agentes de estudo sozinhos.

Roda a cada mensagem da Laura (hook UserPromptSubmit). Se a mensagem casa com o assunto de
um agente, injeta um lembrete para o Claude usar esse agente antes de responder.

  /banca       perguntas sobre provas antigas, o que mais cai, estatística, prioridade
  /discursiva  questão dissertativa enviada com a resposta dela para corrigir

Nunca bloqueia a mensagem e nunca falha a sessão: qualquer erro vira silêncio.
"""
import json
import re
import sys
import unicodedata

# O texto chega sem acento e em minúsculas. Cada padrão, sozinho, já aciona o agente.
AGENTES = [
    {
        "comando": "/banca",
        "padroes": [
            # provas e questões antigas
            r"\bprovas? (antigas?|anteriores?|passadas?|de anos anteriores)\b",
            r"\bquest(ao|oes) (antigas?|anteriores?|passadas?|reais?|da fgv|das provas)\b",
            r"\bvestibulares? (antigos?|anteriores?|passados?)\b",
            r"\bbanco de quest(ao|oes)\b",
            r"\b(prova|vestibular|questao|questoes|fgv) (de|do|da|em) 20(1\d|2[0-6])\b",
            r"\b20(1\d|2[0-6])\.[12]\b",
            # o que cai / frequência
            r"\b(o )?que (mais )?(cai|caiu|costuma cair|aparece|apareceu|a fgv cobra)\b",
            r"\b(mais|menos) (cai|caiu|aparece|apareceu|cobrad[oa]s?|recorrentes?|frequentes?)\b",
            r"\b(cai|caiu|aparece|apareceu|cobra|cobrou) mais\b",
            r"\bja (caiu|cairam|apareceu|apareceram|foi cobrad[oa])\b",
            r"\bquantas vezes\b",
            r"\bnos ultimos \d+ anos\b|\bnos ultimos (dois|tres|quatro|cinco) anos\b",
            r"\b(estatisticas?|frequencia|incidencia|recorrencia|ranking|porcentagem das questoes)\b",
            r"\b(tendencia|padrao) da (prova|banca|fgv)\b",
            # prioridade de estudo com base na prova
            r"\bo que (eu )?(devo |preciso |tenho que )?estudar\b",
            r"\b(priorizar|prioridade de estudo|estudar primeiro|focar mais)\b",
        ],
        "lembrete": (
            "Esta mensagem é sobre provas antigas, frequência de conteúdo ou prioridade de estudo. "
            "Antes de responder, acione o agente /banca (Skill \"banca\") e siga as instruções dele: "
            "rode Projetos/Vestibular/provas-antigas/banco/banca.py para tirar os números do banco, "
            "diga a base (quantas questões e quais edições) e não responda de memória. "
            "Se a pergunta for de planejamento da semana, use os números do /banca junto com o /plano."
        ),
    },
    {
        "comando": "/discursiva",
        "padroes": [
            r"\bminhas? respostas?\b",
            r"\b(respostas?|gabaritos?) (indicad[ao]s?|sugerid[ao]s?|esperad[ao]s?|oficia(l|is)|comentad[ao]s?|padrao)\b",
            r"\bquest(ao|oes) (dissertativas?|discursivas?)\b",
            r"\b(dissertativas?|discursivas?) (para|pra) (corrigir|correcao)\b",
            r"\bgrade (de correcao|da fgv)\b",
            r"\b(corrij\w*|corrig\w*|correcao)\b.*\b(dissertativ\w*|discursiv\w*|gabarito)\b",
            r"\b(dissertativ\w*|discursiv\w*|gabarito)\b.*\b(corrij\w*|corrig\w*|correcao)\b",
        ],
        "lembrete": (
            "Esta mensagem parece trazer uma questão dissertativa com a resposta da Laura para corrigir. "
            "Acione o agente /discursiva (Skill \"discursiva\") e siga as instruções dele: corrija pela "
            "grade da FGV Direito SP guiada pelo gabarito, corrija a língua, gere o PDF com "
            "Projetos/Vestibular/discursivas/gerar_pdf.py e entregue o arquivo. "
            "Se for redação (texto dissertativo-argumentativo com tema), use o /redacao em vez disso."
        ),
    },
]


def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", texto.lower())


def main():
    try:
        dados = json.load(sys.stdin)
    except Exception:
        return
    prompt = normalizar(str(dados.get("prompt", "")))
    lembretes = []
    for ag in AGENTES:
        if prompt.lstrip().startswith(ag["comando"]):
            continue  # ela já chamou o agente direto
        if any(re.search(p, prompt) for p in ag["padroes"]):
            lembretes.append(ag["lembrete"])
    if lembretes:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": "[gatilho automático do Brain] " + " ".join(lembretes),
            }
        }, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
