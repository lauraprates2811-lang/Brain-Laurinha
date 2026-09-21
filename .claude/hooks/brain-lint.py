#!/usr/bin/env python3
"""
brain-lint — o guardiao de formato do Brain da Laura.

Confere a FORMA do Brain, nunca o conteudo. Roda sozinho no fim de toda sessao
(Stop hook) e dentro do /sono e do /otimizar.

  ERRO  = correcao mecanica, sempre a mesma. O Claude corrige antes de encerrar.
  AVISO = precisa de decisao humana. Vira duvida para a Laura.

Modos:
  (sem argumento)        relatorio legivel
  --stop-hook            modo silencioso; sai com codigo 2 se houver ERRO
  --medir                so os numeros, para o /otimizar
  --marcar-otimizacao    registra que a otimizacao semanal rodou hoje

Para desligar temporariamente: criar o arquivo .claude/brain-lint.off
"""

import json
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

# ---------------------------------------------------------------- LIMITES
# Mude aqui. Tudo o que o lint cobra sai destes numeros.
MAX_STATUS_KB          = 20     # tamanho maximo do STATUS.md
MAX_STATUS_ENTRADAS    = 14     # entradas em "Ultimas atualizacoes"
MAX_LINHAS_HISTORICO   = 6      # linhas na tabela de historico de uma ficha
MAX_CELULA_CHARS       = 400    # tamanho de uma celula de tabela do STATUS
MAX_FICHA_KB           = 60     # tamanho de uma ficha de area (aviso)
MAX_REGRAS_KB          = 40     # tamanho de um arquivo de Regras (aviso)
DIAS_ATE_OTIMIZAR      = 7      # dias tolerados sem /otimizar
# -------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]

ARQUIVOS_RAIZ_OK = {
    "CLAUDE.md", "STATUS.md", "STATUS-historico.md", "Calendario.md",
    "README.md", ".gitignore",
}

# Notas que sao indices: memoria e docs de projeto nunca podem linka-las.
INDICES = {"STATUS", "STATUS-historico", "Calendario",
           "decisoes", "decisoes-estudo", "decisoes-tecnicas", "agenda"}

PADROES_SEGREDO = [
    (re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}"),           "chave de API"),
    (re.compile(r"\bghp_[A-Za-z0-9]{20,}"),             "token do GitHub"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"),               "chave da AWS"),
    (re.compile(r"(?i)\b(senha|password|passwd)\s*[:=]\s*\S+"), "senha em texto"),
    (re.compile(r"(?i)\b(api[_-]?key|secret|token)\s*[:=]\s*[\"']?[A-Za-z0-9_\-]{12,}"),
                                                        "token ou segredo"),
    (re.compile(r"(?i)\bBearer\s+[A-Za-z0-9_\-\.]{20,}"), "token Bearer"),
]

RE_WIKILINK = re.compile(r"\[\[([^\]\|#]+)")
RE_DATA_ISO = re.compile(r"^\d{4}-\d{2}-\d{2}$")

erros, avisos, numeros = [], [], {}


def erro(msg):  erros.append(msg)
def aviso(msg): avisos.append(msg)


def notas():
    """Todo .md do Brain, menos o que nao e nota."""
    for p in sorted(ROOT.rglob("*.md")):
        rel = p.relative_to(ROOT)
        if set(rel.parts) & {".git", ".claude", ".obsidian", "node_modules"}:
            continue
        if p.name == "CLAUDE.md" or rel == Path("README.md"):
            continue
        yield p


def ler(p):
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return ""


def areas_conhecidas():
    f = ROOT / "Tarefas" / "dados" / "areas.json"
    ids = set()
    if f.exists():
        try:
            ids = {a["id"] for a in json.loads(ler(f))["areas"]}
        except Exception:
            pass
    return ids | {"sono", "brain"}


# ------------------------------------------------------------- VERIFICACOES

def checa_status():
    p = ROOT / "STATUS.md"
    if not p.exists():
        erro("STATUS.md nao existe.")
        return
    txt = ler(p)
    kb = len(txt.encode()) / 1024
    numeros["status_kb"] = round(kb, 1)
    if kb > MAX_STATUS_KB:
        erro(f"STATUS.md tem {kb:.1f} KB (limite {MAX_STATUS_KB}). "
             f"Rotacione entradas antigas para STATUS-historico.md.")

    m = re.search(r"^##\s*Últimas atualizações\s*$(.*?)(?=^##\s|\Z)",
                  txt, re.M | re.S)
    n = 0
    if m:
        n = len(re.findall(r"^-\s+\*\*\d{4}-\d{2}-\d{2}\*\*", m.group(1), re.M))
    numeros["status_entradas"] = n
    if n > MAX_STATUS_ENTRADAS:
        erro(f"STATUS.md tem {n} entradas em 'Ultimas atualizacoes' "
             f"(limite {MAX_STATUS_ENTRADAS}). Mova as mais antigas para STATUS-historico.md.")

    longas = 0
    for linha in txt.splitlines():
        if linha.strip().startswith("|"):
            for celula in linha.split("|"):
                if len(celula.strip()) > MAX_CELULA_CHARS:
                    longas += 1
    if longas:
        erro(f"STATUS.md tem {longas} celula(s) de tabela acima de {MAX_CELULA_CHARS} "
             f"caracteres. Narrativa mora na memoria, nao no painel.")


def checa_fichas():
    maior = 0
    for p in sorted((ROOT / "Areas").glob("*.md")):
        if p.name.endswith("-historico.md"):
            continue
        txt = ler(p)
        kb = len(txt.encode()) / 1024
        maior = max(maior, kb)
        if kb > MAX_FICHA_KB:
            aviso(f"{p.name} tem {kb:.1f} KB (limite {MAX_FICHA_KB}). "
                  f"Talvez seja hora de dividir a ficha.")

        m = re.search(r"^##\s*Histórico \(últimas entradas\)\s*$(.*?)(?=^##\s|\Z)",
                      txt, re.M | re.S)
        if not m:
            erro(f"{p.name} nao tem a secao '## Histórico (últimas entradas)'.")
            continue
        linhas = [l for l in m.group(1).splitlines()
                  if l.strip().startswith("|") and not re.match(r"^\s*\|[\s\-:|]+\|\s*$", l)]
        linhas = linhas[1:] if linhas else []          # tira o cabecalho
        if len(linhas) > MAX_LINHAS_HISTORICO:
            erro(f"{p.name} tem {len(linhas)} linhas de historico "
                 f"(limite {MAX_LINHAS_HISTORICO}). Mova a mais antiga para "
                 f"Areas/{p.stem}-historico.md.")
        if "## 🔗 Relacionados" not in txt:
            erro(f"{p.name} nao termina com '## 🔗 Relacionados'.")
    numeros["maior_ficha_kb"] = round(maior, 1)


def checa_memoria():
    mem = ROOT / "Memoria"
    if not mem.exists():
        return
    areas = areas_conhecidas()
    indices, partes = {}, []

    for p in sorted(mem.glob("*.md")):
        nome = p.stem
        if RE_DATA_ISO.match(nome):
            indices[nome] = p
        else:
            m = re.match(r"^(\d{4}-\d{2}-\d{2})-(.+)$", nome)
            if not m:
                erro(f"Memoria/{p.name} esta fora do padrao "
                     f"AAAA-MM-DD.md ou AAAA-MM-DD-<area>.md.")
                continue
            dia, area = m.groups()
            if area not in areas:
                erro(f"Memoria/{p.name} usa a area '{area}', que nao existe em "
                     f"Tarefas/dados/areas.json.")
            partes.append((dia, area, p))

    numeros["memorias"] = len(partes)

    for dia, _area, p in partes:
        txt = ler(p)
        if dia not in indices:
            erro(f"Memoria/{p.name} nao tem o indice do dia "
                 f"(falta Memoria/{dia}.md).")
        links = set(RE_WIKILINK.findall(txt))
        if dia not in links:
            erro(f"Memoria/{p.name} nao linka o dia [[{dia}]].")
        if not any(l for l in links if (ROOT / "Areas" / f"{l}.md").exists()):
            erro(f"Memoria/{p.name} nao linka a ficha da area.")
        for l in links:
            if l in INDICES:
                erro(f"Memoria/{p.name} linka o indice [[{l}]]. "
                     f"Memoria nunca linka indice — cite em crase.")

    for dia, p in indices.items():
        corpo = re.sub(r"^#.*$", "", ler(p), count=1, flags=re.M)
        corpo = re.sub(r"^##\s*🔗 Relacionados.*\Z", "", corpo, flags=re.M | re.S)
        sobra = [l for l in corpo.splitlines()
                 if l.strip() and not l.strip().startswith(("-", ">", "|"))]
        if sobra:
            erro(f"Memoria/{p.name} e o indice do dia e deveria ter so a lista "
                 f"das partes, mas tem conteudo proprio ({len(sobra)} linha(s)).")


def checa_projetos():
    for p in sorted((ROOT / "Projetos").rglob("*.md")):
        for l in set(RE_WIKILINK.findall(ler(p))):
            if l in INDICES:
                erro(f"{p.relative_to(ROOT)} linka o indice [[{l}]]. "
                     f"Doc de projeto nunca linka indice — cite em crase.")


def checa_raiz():
    for p in sorted(ROOT.iterdir()):
        if p.is_dir() or p.name.startswith("."):
            continue
        if p.name not in ARQUIVOS_RAIZ_OK:
            erro(f"'{p.name}' esta solto na raiz. Material vai para Projetos/<X>/.")


def checa_nomes():
    for p in sorted(ROOT.rglob("*")):
        partes = set(p.relative_to(ROOT).parts)
        if partes & {".git", ".obsidian", "logs", "node_modules"}:
            continue
        if p.is_dir():
            continue
        if " " in p.name:
            aviso(f"{p.relative_to(ROOT)} tem espaco no nome.")
        if any(c in p.name for c in "áàâãéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ"):
            aviso(f"{p.relative_to(ROOT)} tem acento no nome.")


def checa_links_e_orfas():
    alvos, links_de, linkadas = {}, {}, set()
    for p in notas():
        alvos.setdefault(p.stem, p)
    for p in notas():
        ls = set(RE_WIKILINK.findall(ler(p)))
        links_de[p] = ls
        linkadas |= ls

    quebrados = 0
    for p, ls in links_de.items():
        for l in ls:
            if l not in alvos:
                aviso(f"{p.relative_to(ROOT)} tem link quebrado: [[{l}]].")
                quebrados += 1
    numeros["links_quebrados"] = quebrados

    orfas = 0
    for p in notas():
        rel = p.relative_to(ROOT)
        if rel.parts[0] in ("Memoria",):
            continue
        # indices e READMEs sao portas de entrada, nao orfas
        if p.stem in INDICES or p.name == "README.md":
            continue
        if p.stem not in linkadas:
            aviso(f"{rel} e orfa: nenhuma nota linka para ela.")
            orfas += 1
    numeros["orfas"] = orfas


def checa_segredos():
    for p in sorted(ROOT.rglob("*")):
        partes = set(p.relative_to(ROOT).parts)
        if partes & {".git", "logs", ".obsidian", "node_modules"}:
            continue
        if not p.is_file() or p.suffix not in (".md", ".json", ".sh", ".txt"):
            continue
        for n, linha in enumerate(ler(p).splitlines(), 1):
            for padrao, nome in PADROES_SEGREDO:
                if padrao.search(linha):
                    aviso(f"POSSIVEL SEGREDO ({nome}) em "
                          f"{p.relative_to(ROOT)}:{n}. Confira e remova. "
                          f"O Brain nunca guarda segredo.")
                    break


def checa_git():
    try:
        out = subprocess.run(["git", "ls-files"], cwd=ROOT,
                             capture_output=True, text=True, timeout=20).stdout
    except Exception:
        return
    for f in out.splitlines():
        if f.endswith(".DS_Store") or "/logs/" in f or f.startswith(".claude/logs/"):
            aviso(f"lixo rastreado no git: {f}. Acrescente ao .gitignore e remova do indice.")


def checa_otimizacao():
    marca = ROOT / ".claude" / "ultima-otimizacao"
    if not marca.exists():
        aviso("o /otimizar nunca rodou. Rode uma vez para marcar o ponto de partida.")
        return
    try:
        quando = datetime.strptime(ler(marca).strip(), "%Y-%m-%d").date()
    except ValueError:
        aviso(".claude/ultima-otimizacao tem data invalida.")
        return
    dias = (date.today() - quando).days
    numeros["dias_sem_otimizar"] = dias
    if dias > DIAS_ATE_OTIMIZAR:
        aviso(f"o ultimo /otimizar foi ha {dias} dias (limite {DIAS_ATE_OTIMIZAR}). "
              f"Rode /otimizar.")


def checa_prazos():
    f = ROOT / "Tarefas" / "dados" / "prazos.json"
    if not f.exists():
        return
    try:
        dados = json.loads(ler(f))
    except Exception:
        erro("Tarefas/dados/prazos.json nao e um JSON valido.")
        return
    hoje = date.today()
    vencidos = 0
    for pr in dados.get("prazos", []):
        try:
            d = datetime.strptime(pr["data"], "%Y-%m-%d").date()
        except Exception:
            continue
        if d < hoje:
            vencidos += 1
            aviso(f"prazo vencido em {pr['data']} sem registro: {pr['o_que']}. "
                  f"Registre o que aconteceu e tire do prazos.json.")
    numeros["prazos_vencidos"] = vencidos


def checa_tarefas():
    f = ROOT / "Tarefas" / "dados" / "tarefas.json"
    if not f.exists():
        return
    try:
        dados = json.loads(ler(f))
    except Exception:
        erro("Tarefas/dados/tarefas.json nao e um JSON valido.")
        return
    areas = areas_conhecidas()
    abertas = 0
    for t in dados.get("tarefas", []):
        if t.get("status") == "aberta":
            abertas += 1
        if t.get("area") not in areas:
            erro(f"tarefa {t.get('id')} usa a area '{t.get('area')}', "
                 f"que nao existe em areas.json.")
    numeros["tarefas_abertas"] = abertas


def roda_tudo():
    checa_status()
    checa_fichas()
    checa_memoria()
    checa_projetos()
    checa_raiz()
    checa_nomes()
    checa_links_e_orfas()
    checa_segredos()
    checa_git()
    checa_otimizacao()
    checa_prazos()
    checa_tarefas()


# -------------------------------------------------------------------- MAIN

def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else ""

    if (ROOT / ".claude" / "brain-lint.off").exists():
        if arg != "--stop-hook":
            print("brain-lint desligado (.claude/brain-lint.off existe).")
        return 0

    if arg == "--marcar-otimizacao":
        (ROOT / ".claude" / "ultima-otimizacao").write_text(
            date.today().isoformat() + "\n", encoding="utf-8")
        print(f"otimizacao marcada em {date.today().isoformat()}")
        return 0

    roda_tudo()

    if arg == "--medir":
        print(json.dumps({"numeros": numeros,
                          "erros": len(erros),
                          "avisos": len(avisos)},
                         indent=2, ensure_ascii=False))
        return 0

    if arg == "--stop-hook":
        if erros:
            print("brain-lint encontrou ERRO(s) de formato. "
                  "Corrija antes de encerrar a sessao:", file=sys.stderr)
            for e in erros:
                print(f"  ERRO: {e}", file=sys.stderr)
            return 2
        return 0

    print("=" * 66)
    print("  brain-lint — guardiao de formato do Brain")
    print("=" * 66)
    if numeros:
        print("\nNumeros:")
        for k, v in numeros.items():
            print(f"  {k:22} {v}")
    if erros:
        print(f"\nERROS ({len(erros)}) — correcao mecanica, o Claude conserta:")
        for e in erros:
            print(f"  x {e}")
    if avisos:
        print(f"\nAVISOS ({len(avisos)}) — decisao humana:")
        for a in avisos:
            print(f"  ! {a}")
    if not erros and not avisos:
        print("\nTudo limpo. Nenhum erro, nenhum aviso.")
    elif not erros:
        print("\nNenhum ERRO. So avisos.")
    print()
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
