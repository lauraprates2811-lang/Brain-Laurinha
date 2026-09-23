#!/usr/bin/env python3
"""Banco de questões das provas antigas da FGV Direito SP.

Os dados são os CSVs desta pasta (um por edição, separador ';').
Este script só lê, valida e conta — nunca altera os CSVs.

Uso:
  python3 banca.py validar
  python3 banca.py edicoes
  python3 banca.py ranking [--materia M] [--prova P] [--desde 2024.1] [--ultimas 3] [--por tema|subtema|materia|tag] [--top 20]
  python3 banca.py tema "<tema ou subtema>"          # linha do tempo + lista das questões
  python3 banca.py busca "<termo>" [--materia M]      # procura em tema, subtema, tags e resumo
  python3 banca.py recomendar [--materia M] [--prova P] [--ultimas 3] [--top 15]

Nos CSVs: separador ';' — nunca usar ';' dentro de um campo (use ' — ').
"""
import csv, glob, json, os, re, sys, unicodedata
from collections import Counter, defaultdict

AQUI = os.path.dirname(os.path.abspath(__file__))
COLUNAS = ["edicao", "prova", "numero", "materia", "tema", "subtema", "gabarito", "valor", "tags", "resumo"]
PROVAS = {"Objetiva", "Discursiva", "Redação"}


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    return s.lower().strip()


def ordem_edicao(e):
    a, s = e.split(".")
    return (int(a), int(s))


def carregar():
    temas = json.load(open(os.path.join(AQUI, "temas.json"), encoding="utf-8"))
    qs, erros = [], []
    for f in sorted(glob.glob(os.path.join(AQUI, "*.csv"))):
        with open(f, encoding="utf-8") as fh:
            linhas = [l for l in fh if l.strip() and not l.startswith("#")]
        for i, r in enumerate(csv.DictReader(linhas, delimiter=";"), start=2):
            onde = f"{os.path.basename(f)}:{i}"
            if set(r) != set(COLUNAS) or None in r.values():
                erros.append(f"{onde}: colunas erradas ({list(r)})")
                continue
            r = {k: (v or "").strip() for k, v in r.items()}
            if r["prova"] not in PROVAS:
                erros.append(f"{onde}: prova '{r['prova']}' fora de {sorted(PROVAS)}")
            if r["materia"] not in temas:
                erros.append(f"{onde}: matéria '{r['materia']}' não existe em temas.json")
            elif r["tema"] not in temas[r["materia"]]:
                erros.append(f"{onde}: tema '{r['tema']}' não existe em {r['materia']}")
            r["tags"] = [t.strip() for t in r["tags"].split(",") if t.strip()]
            r["id"] = f"{r['edicao']}-{r['prova'][:3].upper()}-{r['numero']}"
            qs.append(r)
    ids = Counter(q["id"] + q["materia"] for q in qs)
    erros += [f"id repetido: {k}" for k, n in ids.items() if n > 1]
    return qs, temas, erros


def filtrar(qs, a):
    eds = sorted({q["edicao"] for q in qs}, key=ordem_edicao)
    if a.get("ultimas"):
        eds = eds[-int(a["ultimas"]):]
    if a.get("desde"):
        eds = [e for e in eds if ordem_edicao(e) >= ordem_edicao(a["desde"])]
    out = [q for q in qs if q["edicao"] in eds]
    if a.get("materia"):
        out = [q for q in out if norm(a["materia"]) in norm(q["materia"])]
    if a.get("prova"):
        out = [q for q in out if norm(a["prova"]) in norm(q["prova"])]
    return out, eds


def args(argv):
    a, pos, i = {}, [], 0
    while i < len(argv):
        if argv[i].startswith("--"):
            a[argv[i][2:]] = argv[i + 1]
            i += 2
        else:
            pos.append(argv[i])
            i += 1
    return a, pos


def chave(q, por):
    if por == "tag":
        return q["tags"]
    if por == "materia":
        return [q["materia"]]
    if por == "subtema":
        return [f"{q['materia']} › {q['tema']} › {q['subtema']}"]
    return [f"{q['materia']} › {q['tema']}"]


def cmd_validar(qs, temas, erros, a, pos):
    if erros:
        print(f"❌ {len(erros)} problema(s):")
        for e in erros:
            print("  -", e)
        sys.exit(1)
    print(f"✅ {len(qs)} questões, {len({q['edicao'] for q in qs})} edições, tudo dentro de temas.json")


def cmd_edicoes(qs, temas, erros, a, pos):
    por = defaultdict(Counter)
    for q in qs:
        por[q["edicao"]][f"{q['prova']}/{q['materia']}"] += 1
    for e in sorted(por, key=ordem_edicao):
        tot = sum(por[e].values())
        print(f"\n{e} — {tot} itens")
        for k, n in sorted(por[e].items()):
            print(f"   {n:3d}  {k}")


def cmd_ranking(qs, temas, erros, a, pos):
    sel, eds = filtrar(qs, a)
    por = a.get("por", "tema")
    cont, em = Counter(), defaultdict(set)
    for q in sel:
        for k in chave(q, por):
            cont[k] += 1
            em[k].add(q["edicao"])
    tot = len(sel)
    print(f"Base: {tot} questões · edições {', '.join(eds)}" + (f" · matéria {a['materia']}" if a.get("materia") else "") + (f" · prova {a['prova']}" if a.get("prova") else ""))
    print(f"{'#':>3}  {'qtd':>4}  {'%':>5}  {'edições':>8}  item")
    for i, (k, n) in enumerate(cont.most_common(int(a.get("top", 25))), 1):
        print(f"{i:>3}  {n:>4}  {100*n/tot:>4.1f}%  {len(em[k]):>3}/{len(eds):<4}  {k}")


def cmd_tema(qs, temas, erros, a, pos):
    termo = norm(" ".join(pos))
    sel, eds = filtrar(qs, a)
    hit = [q for q in sel if termo in norm(q["tema"]) or termo in norm(q["subtema"])]
    if not hit:
        print("Nada encontrado. Tente `busca`.")
        return
    linha = Counter(q["edicao"] for q in hit)
    print(f"'{' '.join(pos)}': {len(hit)} questões em {len(linha)} de {len(eds)} edições")
    print("Por edição: " + " · ".join(f"{e}: {linha.get(e, 0)}" for e in eds))
    for q in sorted(hit, key=lambda q: (ordem_edicao(q["edicao"]), q["prova"], int(re.sub(r'\D', '', q['numero']) or 0))):
        gab = f" [gab {q['gabarito']}]" if q["gabarito"] else ""
        print(f"  {q['id']:<16} {q['materia']} › {q['tema']} › {q['subtema']}{gab} — {q['resumo']}")


def cmd_busca(qs, temas, erros, a, pos):
    termo = norm(" ".join(pos))
    sel, _ = filtrar(qs, a)
    hit = [q for q in sel if termo in norm(" ".join([q["tema"], q["subtema"], q["resumo"], " ".join(q["tags"])]))]
    print(f"{len(hit)} questões com '{' '.join(pos)}'")
    for q in hit:
        print(f"  {q['id']:<16} {q['materia']} › {q['tema']} › {q['subtema']} — {q['resumo']}")


def cmd_recomendar(qs, temas, erros, a, pos):
    """Peso = frequência com mais peso para edições recentes (a mais nova vale 1, cada anterior vale 0,8x)."""
    eds = sorted({q["edicao"] for q in qs}, key=ordem_edicao)
    peso = {e: 0.8 ** (len(eds) - 1 - i) for i, e in enumerate(eds)}
    ult = eds[-int(a.get("ultimas", 3)):]
    score, n_all, n_ult, em = Counter(), Counter(), Counter(), defaultdict(set)
    sel, _ = filtrar(qs, {k: v for k, v in a.items() if k in ("materia", "prova")})
    for q in sel:
        if q["materia"] == "Redação":
            continue
        k = f"{q['materia']} › {q['tema']}"
        score[k] += peso[q["edicao"]]
        n_all[k] += 1
        em[k].add(q["edicao"])
        if q["edicao"] in ult:
            n_ult[k] += 1
    print(f"Temas por peso (recência 0,8x por edição) · 'últimas' = {', '.join(ult)}")
    print(f"{'#':>3}  {'peso':>5}  {'total':>5}  {'últimas':>7}  {'edições':>7}  tema")
    for i, (k, s) in enumerate(score.most_common(int(a.get("top", 15))), 1):
        print(f"{i:>3}  {s:>5.1f}  {n_all[k]:>5}  {n_ult[k]:>7}  {len(em[k]):>3}/{len(eds):<3}  {k}")


if __name__ == "__main__":
    qs, temas, erros = carregar()
    a, pos = args(sys.argv[2:])
    cmd = sys.argv[1] if len(sys.argv) > 1 else "edicoes"
    fn = globals().get(f"cmd_{cmd}")
    if not fn:
        print(__doc__)
        sys.exit(1)
    if erros and cmd != "validar":
        print(f"⚠️  {len(erros)} problema(s) no banco — rode `validar`.\n")
    fn(qs, temas, erros, a, pos)
