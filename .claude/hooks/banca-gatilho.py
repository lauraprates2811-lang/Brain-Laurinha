#!/usr/bin/env python3
"""banca-gatilho — aciona o /banca sozinho.

Roda a cada mensagem da Laura (hook UserPromptSubmit). Se a pergunta for sobre provas
antigas, o que mais cai, estatística de conteúdo ou prioridade de estudo com base na prova,
injeta um lembrete para o Claude usar o agente /banca antes de responder.

Nunca bloqueia a mensagem e nunca falha a sessão: qualquer erro vira silêncio.
"""
import json
import re
import sys
import unicodedata

# Cada padrão, sozinho, já basta para acionar. O texto chega sem acento e em minúsculas.
GATILHOS = [
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
]

LEMBRETE = (
    "[gatilho automático do Brain] Esta mensagem é sobre provas antigas, frequência de "
    "conteúdo ou prioridade de estudo. Antes de responder, acione o agente /banca (Skill "
    "\"banca\") e siga as instruções dele: rode "
    "Projetos/Vestibular/provas-antigas/banco/banca.py para tirar os números do banco, "
    "diga a base (quantas questões e quais edições) e não responda de memória. "
    "Se a pergunta for de planejamento da semana, use os números do /banca junto com o /plano."
)


def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", texto.lower())


def main():
    try:
        dados = json.load(sys.stdin)
    except Exception:
        return
    prompt = normalizar(str(dados.get("prompt", "")))
    # já chamou o /banca direto: não precisa lembrar
    if prompt.lstrip().startswith("/banca"):
        return
    if any(re.search(p, prompt) for p in GATILHOS):
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": LEMBRETE,
            }
        }, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
