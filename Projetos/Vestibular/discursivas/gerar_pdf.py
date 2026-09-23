#!/usr/bin/env python3
"""Gera o PDF de correção de uma questão discursiva a partir de uma ficha JSON.

Uso:
  python3 gerar_pdf.py <ficha.json> [saida.pdf]      # saída padrão: mesmo nome, .pdf
  A ficha pode ser um objeto (uma questão) ou uma lista (várias questões num PDF só,
  com página de resumo na frente).
  python3 gerar_pdf.py --exemplo                     # imprime uma ficha de exemplo

Marcação dentro de "resposta_marcada" (o texto da Laura, palavra por palavra):
  {-trecho-}        riscado em vermelho  → tirar
  {+trecho+}        verde                → colocar
  [[trecho]]        grifo amarelo        → trecho comentado
  Qualquer uma aceita |n no fim para ligar a um comentário: {-trecho|2-}  {+trecho|2+}  [[trecho|3]]
  Linha em branco separa parágrafos.
"""
import json
import os
import re
import sys
from datetime import date

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (KeepTogether, PageBreak, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

# ---------- fontes (com acento garantido) ----------
FONTES = "/System/Library/Fonts/Supplemental/"
try:
    pdfmetrics.registerFont(TTFont("Texto", FONTES + "Georgia.ttf"))
    pdfmetrics.registerFont(TTFont("Texto-B", FONTES + "Georgia Bold.ttf"))
    pdfmetrics.registerFont(TTFont("Texto-I", FONTES + "Georgia Italic.ttf"))
    pdfmetrics.registerFont(TTFont("Texto-BI", FONTES + "Georgia Bold Italic.ttf"))
    pdfmetrics.registerFont(TTFont("Rotulo", FONTES + "Arial.ttf"))
    pdfmetrics.registerFont(TTFont("Rotulo-B", FONTES + "Arial Bold.ttf"))
    pdfmetrics.registerFontFamily("Texto", normal="Texto", bold="Texto-B", italic="Texto-I", boldItalic="Texto-BI")
    pdfmetrics.registerFontFamily("Rotulo", normal="Rotulo", bold="Rotulo-B", italic="Rotulo", boldItalic="Rotulo-B")
    TX, RT, RTB = "Texto", "Rotulo", "Rotulo-B"
except Exception:  # fora do Mac: fontes padrão do PDF
    TX, RT, RTB = "Times-Roman", "Helvetica", "Helvetica-Bold"

# ---------- cores ----------
TINTA = colors.HexColor("#1f2328")
MUDO = colors.HexColor("#5b6470")
LINHA = colors.HexColor("#d9dce1")
MARINHO = colors.HexColor("#1b3a5c")
VERMELHO = colors.HexColor("#b42318")
VERDE = colors.HexColor("#1e7d45")
AMBAR = colors.HexColor("#a15c07")
GRIFO = "#fff0a3"
FUNDO_CINZA = colors.HexColor("#f4f4f3")
FUNDO_AZUL = colors.HexColor("#eef4fb")
FUNDO_VERDE = colors.HexColor("#ecf7f0")

COR_TIPO = {"gramatica": VERMELHO, "conteudo": AMBAR, "elogio": VERDE}
NOME_TIPO = {"gramatica": "Gramática", "conteudo": "Conteúdo", "elogio": "Ponto forte"}

# ---------- estilos ----------
def est(nome, **kw):
    base = dict(fontName=TX, fontSize=10.5, leading=15, textColor=TINTA, alignment=TA_LEFT)
    base.update(kw)
    return ParagraphStyle(nome, **base)

S = {
    "selo": est("selo", fontName=RTB, fontSize=8, leading=10, textColor=MARINHO),
    "titulo": est("titulo", fontName=TX, fontSize=19, leading=23),
    "meta": est("meta", fontName=RT, fontSize=8.5, leading=11, textColor=MUDO),
    "h2": est("h2", fontName=RTB, fontSize=10, leading=13, textColor=MARINHO, spaceBefore=14, spaceAfter=6, keepWithNext=1),
    "corpo": est("corpo"),
    "resposta": est("resposta", fontSize=11.5, leading=19),
    "peq": est("peq", fontSize=9, leading=12.5),
    "peqmudo": est("peqmudo", fontName=RT, fontSize=8, leading=10.5, textColor=MUDO),
    "cel": est("cel", fontSize=9, leading=12.5),
    "celb": est("celb", fontName=RTB, fontSize=8, leading=10.5, textColor=MUDO),
    "nota": est("nota", fontName=TX, fontSize=26, leading=28),
    "veredito": est("veredito", fontSize=10.5, leading=15),
}


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def num(n):
    return f'<super><font name="{RTB}" size="7" color="#1b3a5c">{n}</font></super>' if n else ""


def marcar(texto):
    """Converte a marcação da resposta em XML do reportlab."""
    t = esc(texto)
    t = re.sub(r"\{-(.+?)(?:\|(\d+))?-\}",
               lambda m: f'<strike><font color="#b42318">{m.group(1)}</font></strike>{num(m.group(2))}', t, flags=re.S)
    t = re.sub(r"\{\+(.+?)(?:\|(\d+))?\+\}",
               lambda m: f'<font color="#1e7d45"><b>{m.group(1)}</b></font>{num(m.group(2))}', t, flags=re.S)
    t = re.sub(r"\[\[(.+?)(?:\|(\d+))?\]\]",
               lambda m: f'<span backColor="{GRIFO}">{m.group(1)}</span>{num(m.group(2))}', t, flags=re.S)
    return t


def paragrafos(texto, estilo, marcado=False):
    out = []
    for bloco in re.split(r"\n\s*\n", (texto or "").strip()):
        if not bloco.strip():
            continue
        x = marcar(bloco) if marcado else esc(bloco)
        out.append(Paragraph(x.replace("\n", "<br/>"), estilo))
        out.append(Spacer(1, 5))
    return out


def caixa(conteudo, fundo, borda=None, pad=10):
    t = Table([[conteudo]], colWidths=[LARG])
    st = [("BACKGROUND", (0, 0), (-1, -1), fundo),
          ("LEFTPADDING", (0, 0), (-1, -1), pad), ("RIGHTPADDING", (0, 0), (-1, -1), pad),
          ("TOPPADDING", (0, 0), (-1, -1), pad - 2), ("BOTTOMPADDING", (0, 0), (-1, -1), pad - 2)]
    if borda:
        st.append(("LINEBEFORE", (0, 0), (0, -1), 3, borda))
    t.setStyle(TableStyle(st))
    return t


def pct(nivel):
    m = re.search(r"(\d{1,3}(?:[.,]\d+)?)\s*%", str(nivel or ""))
    return float(m.group(1).replace(",", ".")) if m else None


def cor_nivel(p):
    if p is None:
        return MUDO
    return VERDE if p >= 75 else AMBAR if p >= 50 else VERMELHO


def regua(nivel_pct):
    """Régua 0-25-50-75-100 da grade, com o nível da Laura pintado."""
    niveis = [0, 25, 50, 75, 100]
    cel = [Paragraph(f'<font name="{RTB}" size="8.5" color="{"#ffffff" if n == nivel_pct else "#5b6470"}">{n}%</font>',
                     est(f"r{n}", alignment=1)) for n in niveis]
    t = Table([cel], colWidths=[LARG / 5] * 5, rowHeights=[18])
    st = [("GRID", (0, 0), (-1, -1), 0.6, colors.white), ("BACKGROUND", (0, 0), (-1, -1), FUNDO_CINZA),
          ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]
    if nivel_pct in niveis:
        i = niveis.index(nivel_pct)
        st.append(("BACKGROUND", (i, 0), (i, 0), cor_nivel(nivel_pct)))
    t.setStyle(TableStyle(st))
    return t


def tabela(cabecalho, linhas, larguras):
    dados = [[Paragraph(h.upper(), S["celb"]) for h in cabecalho]]
    for l in linhas:
        dados.append([c if not isinstance(c, str) else Paragraph(c, S["cel"]) for c in l])
    t = Table(dados, colWidths=[LARG * w for w in larguras], repeatRows=1)
    t.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, MARINHO),
        ("LINEBELOW", (0, 1), (-1, -1), 0.4, LINHA),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


LARG = A4[0] - 4 * cm


def rodape(canvas, doc):
    canvas.saveState()
    canvas.setFont(RT, 7.5)
    canvas.setFillColor(MUDO)
    canvas.drawString(2 * cm, 1.2 * cm, "Correção do Brain pela grade da FGV Direito SP — estimativa de estudo, não é nota oficial.")
    canvas.drawRightString(A4[0] - 2 * cm, 1.2 * cm, f"{doc.page}")
    canvas.restoreState()


def validar(f):
    faltam = [k for k in ("materia", "enunciado", "gabarito", "resposta_marcada", "nota") if not f.get(k)]
    avisos = []
    refs = set(re.findall(r"\|(\d+)(?:-\}|\+\}|\]\])", f.get("resposta_marcada", "")))
    coms = {str(c.get("n")) for c in f.get("comentarios", [])}
    if refs - coms:
        avisos.append(f"marcação aponta para comentário inexistente: {sorted(refs - coms)}")
    return faltam, avisos


def historia(f):
    story = []
    # ----- cabeçalho -----
    story.append(Paragraph("CORREÇÃO DE DISCURSIVA · FGV DIREITO SP", S["selo"]))
    story.append(Spacer(1, 4))
    story.append(Paragraph(esc(f.get("titulo") or f["materia"]), S["titulo"]))
    meta = [f.get("data") or date.today().isoformat(), f["materia"]]
    if f.get("origem"):
        meta.append(f["origem"])
    if f.get("valor"):
        meta.append(f"valor da questão: {f['valor']}")
    story.append(Spacer(1, 3))
    story.append(Paragraph(esc(" · ".join(meta)), S["meta"]))
    story.append(Spacer(1, 12))

    # ----- nota -----
    n = f["nota"]
    p = pct(n.get("percentual"))
    placar = f'{esc(n.get("obtida", "—"))}<font size="13" color="#5b6470"> / {esc(n.get("maxima", "—"))}</font>'
    lado = [Paragraph(f'<font color="{cor_nivel(p).hexval().replace("0x", "#")}">{placar}</font>', S["nota"]),
            Spacer(1, 2),
            Paragraph(f'<font name="{RTB}" size="8.5" color="#5b6470">{esc(n.get("percentual", ""))}</font>', S["peq"])]
    veredito = [Paragraph(f'<b>{esc(n.get("criterio", ""))}</b>', S["veredito"])]
    if f.get("de_acordo"):
        veredito += [Spacer(1, 4), Paragraph(esc(f["de_acordo"]), S["peq"])]
    t = Table([[lado, veredito]], colWidths=[LARG * 0.30, LARG * 0.70])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (-1, -1), FUNDO_CINZA),
                           ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                           ("TOPPADDING", (0, 0), (-1, -1), 10), ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                           ("LINEAFTER", (0, 0), (0, 0), 0.6, LINHA)]))
    story.append(t)
    escala = Paragraph("Régua da grade FGV: 100% completa e bem escrita · 75% completa com desvio de redação · "
                       "50% parcial e bem escrita · 25% parcial com desvio · 0% não atende.", S["peqmudo"])
    niveis_grade = f.get("tipo_grade", "niveis") == "niveis"
    if niveis_grade and p in (0, 25, 50, 75, 100):
        story += [Spacer(1, 6), regua(p), Spacer(1, 3), escala]

    # ----- enunciado e gabarito -----
    story.append(Paragraph("ENUNCIADO", S["h2"]))
    story.append(caixa(paragrafos(f["enunciado"], S["peq"]), FUNDO_CINZA))
    story.append(Paragraph("RESPOSTA INDICADA (GABARITO)", S["h2"]))
    bloco = paragrafos(f["gabarito"], S["peq"])
    if f.get("grade"):
        bloco += [Spacer(1, 4), Paragraph('<font name="Rotulo-B" size="8" color="#1b3a5c">GRADE OFICIAL</font>', S["peq"]),
                  Spacer(1, 2)] + paragrafos(f["grade"], S["peq"])
    story.append(caixa(bloco, FUNDO_AZUL, borda=MARINHO))

    # ----- resposta corrigida -----
    story.append(Paragraph("SUA RESPOSTA, CORRIGIDA", S["h2"]))
    legenda = ('<font color="#b42318"><strike>riscado</strike></font> = tirar · '
               '<font color="#1e7d45"><b>verde</b></font> = colocar · '
               f'<span backColor="{GRIFO}">grifo</span> = ver comentário · '
               f'número = comentário abaixo')
    story.append(Paragraph(legenda, S["peqmudo"]))
    story.append(Spacer(1, 6))
    story.append(caixa(paragrafos(f["resposta_marcada"], S["resposta"], marcado=True), colors.white, borda=LINHA, pad=12))

    # ----- comentários -----
    if f.get("comentarios"):
        story.append(Paragraph("COMENTÁRIOS", S["h2"]))
        linhas = []
        for c in f["comentarios"]:
            tipo = c.get("tipo", "conteudo")
            cor = COR_TIPO.get(tipo, MUDO).hexval().replace("0x", "#")
            linhas.append([Paragraph(f'<font name="{RTB}" color="#1b3a5c">{c.get("n", "")}</font>', S["cel"]),
                           Paragraph(f'<font name="{RTB}" size="7.5" color="{cor}">{NOME_TIPO.get(tipo, tipo).upper()}</font>', S["cel"]),
                           Paragraph(esc(c.get("texto", "")), S["cel"])])
        t = Table(linhas, colWidths=[LARG * 0.05, LARG * 0.15, LARG * 0.80])
        t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), 0.4, LINHA),
                               ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                               ("LEFTPADDING", (0, 0), (-1, -1), 2)]))
        story.append(t)

    # ----- avaliação pela grade -----
    if f.get("itens"):
        story.append(Paragraph("AVALIAÇÃO PELA GRADE", S["h2"]))
        linhas = []
        for it in f["itens"]:
            pi = pct(it.get("nivel"))
            cor = cor_nivel(pi).hexval().replace("0x", "#")
            nivel = f'<font name="{RTB}" color="{cor}">{esc(it.get("nivel", ""))}</font>'
            if it.get("pontos"):
                nivel += f'<br/><font size="8" color="#5b6470">{esc(it["pontos"])}</font>'
            linhas.append([f'<b>{esc(it.get("item", ""))}</b>', esc(it.get("esperado", "")), esc(it.get("voce", "")), nivel])
        story.append(tabela(["Item", "O que a grade pede", "O que você fez", "Nível"], linhas, [0.08, 0.37, 0.40, 0.15]))
        if niveis_grade:
            story += [Spacer(1, 4), escala]

    # ----- gramática -----
    if f.get("gramatica"):
        story.append(Paragraph("CORREÇÃO DE LÍNGUA", S["h2"]))
        linhas = [[f'<font color="#b42318">{esc(g.get("trecho", ""))}</font>',
                   f'<font color="#1e7d45"><b>{esc(g.get("correcao", ""))}</b></font>',
                   esc(g.get("regra", ""))] for g in f["gramatica"]]
        story.append(tabela(["Você escreveu", "Forma correta", "Por quê"], linhas, [0.30, 0.30, 0.40]))

    # ----- o que melhorar -----
    if f.get("melhorar"):
        story.append(Paragraph("O QUE MELHORAR", S["h2"]))
        for i, m in enumerate(f["melhorar"], 1):
            story.append(Paragraph(f'<font name="{RTB}" color="#1b3a5c">{i}.</font>&nbsp; {esc(m)}',
                                   est(f"m{i}", leftIndent=14, firstLineIndent=-14, spaceAfter=4)))

    # ----- versão revisada -----
    if f.get("reescrita"):
        bloco = [Paragraph("SUA RESPOSTA, REVISADA", S["h2"]),
                 Paragraph("As suas ideias, com as correções aplicadas — é o padrão para copiar na próxima.", S["peqmudo"]),
                 Spacer(1, 6),
                 caixa(paragrafos(f["reescrita"], S["corpo"]), FUNDO_VERDE, borda=VERDE)]
        story.append(KeepTogether(bloco))
    return story


def resumo(fichas):
    """Página de abertura quando o PDF tem mais de uma questão."""
    story = [Paragraph("CORREÇÃO DE DISCURSIVAS · FGV DIREITO SP", S["selo"]), Spacer(1, 4),
             Paragraph(f"{len(fichas)} questões corrigidas", S["titulo"]), Spacer(1, 3),
             Paragraph(esc(fichas[0].get("data") or date.today().isoformat()), S["meta"]),
             Paragraph("RESUMO", S["h2"])]
    linhas = []
    for i, f in enumerate(fichas, 1):
        n = f["nota"]
        p = pct(n.get("percentual"))
        cor = cor_nivel(p).hexval().replace("0x", "#")
        linhas.append([f"<b>{i}</b>", esc(f.get("titulo") or f["materia"]),
                       f'<font name="{RTB}" color="{cor}">{esc(n.get("obtida", ""))} / {esc(n.get("maxima", ""))}</font>'
                       f'<br/><font size="8" color="#5b6470">{esc(n.get("percentual", ""))}</font>',
                       esc(n.get("criterio", ""))])
    story.append(tabela(["#", "Questão", "Nota", "Resumo da correção"], linhas, [0.05, 0.35, 0.15, 0.45]))
    return story


def montar(fichas, saida):
    story = []
    if len(fichas) > 1:
        story += resumo(fichas) + [PageBreak()]
    for i, f in enumerate(fichas):
        if i:
            story.append(PageBreak())
        story += historia(f)
    titulo = fichas[0].get("titulo") or f"Correção — {fichas[0]['materia']}"
    if len(fichas) > 1:
        titulo = f"Correção de {len(fichas)} discursivas"
    doc = SimpleDocTemplate(saida, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                            topMargin=1.8 * cm, bottomMargin=1.8 * cm, title=titulo, author="Brain da Laura")
    doc.build(story, onFirstPage=rodape, onLaterPages=rodape)


EXEMPLO = {
    "titulo": "História — CLT e corporativismo",
    "data": "2026-09-22",
    "materia": "História",
    "origem": "FGV 2025.1 · Ciências Humanas · questão 2",
    "valor": "1,0",
    "tipo_grade": "niveis",
    "enunciado": "a) Aponte quatro medidas presentes na CLT de 1943.\nb) Explique a relação entre a CLT e a perspectiva corporativista do Estado Novo.",
    "gabarito": "a) Jornada de 8 horas, férias remuneradas, salário mínimo, carteira de trabalho...\nb) Sindicatos únicos subordinados ao Ministério do Trabalho; conciliação de classes sob tutela do Estado.",
    "grade": "",
    "resposta_marcada": "a) A CLT criou o salário mínimo, as férias remuneradas{+,|1+} a jornada de 8 horas e a carteira de trabalho.\n\nb) [[A CLT tinha haver com o corporativismo|2]] porque o Estado controlava os sindicatos.",
    "comentarios": [
        {"n": 1, "tipo": "gramatica", "texto": "Enumeração: separe os itens com vírgula."},
        {"n": 2, "tipo": "conteudo", "texto": "“Tinha haver” não existe (é “tinha a ver”). E falta explicar a ideia de conciliação de classes."},
    ],
    "itens": [
        {"item": "a)", "esperado": "Quatro medidas corretas", "voce": "Quatro medidas corretas", "nivel": "100%", "pontos": "0,5 / 0,5"},
        {"item": "b)", "esperado": "Sindicato único sob controle estatal + conciliação de classes", "voce": "Só o controle dos sindicatos", "nivel": "25%", "pontos": "0,125 / 0,5"},
    ],
    "nota": {"obtida": "0,625", "maxima": "1,0", "percentual": "62,5%", "criterio": "Item a completo; item b parcial e com desvio de redação."},
    "de_acordo": "O item a) está de acordo com o pedido, mesmo citando medidas em outra ordem que o gabarito.",
    "gramatica": [{"trecho": "tinha haver com", "correcao": "tinha a ver com", "regra": "“Ter a ver” = ter relação. “Haver” é outro verbo."}],
    "melhorar": ["No item b), feche a explicação com a finalidade: evitar a luta de classes.", "Revise expressões fixas antes de entregar."],
    "reescrita": "a) A CLT criou o salário mínimo, as férias remuneradas, a jornada de 8 horas e a carteira de trabalho.\n\nb) A CLT tinha a ver com o corporativismo porque o Estado controlava os sindicatos, buscando conciliar patrões e empregados e evitar a luta de classes.",
}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    if sys.argv[1] == "--exemplo":
        print(json.dumps(EXEMPLO, ensure_ascii=False, indent=2))
        sys.exit(0)
    dados = json.load(open(sys.argv[1], encoding="utf-8"))
    fichas = dados if isinstance(dados, list) else [dados]
    erro = False
    for i, ficha in enumerate(fichas, 1):
        faltam, avisos = validar(ficha)
        if faltam:
            print(f"❌ questão {i}: faltam campos obrigatórios: {', '.join(faltam)}")
            erro = True
        for a in avisos:
            print(f"⚠️  questão {i}: {a}")
    if erro:
        sys.exit(1)
    saida = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(sys.argv[1])[0] + ".pdf"
    montar(fichas, saida)
    print(f"✅ PDF gerado: {saida}")
