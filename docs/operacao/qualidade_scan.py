#!/usr/bin/env python3
"""Faixa Preta - Qualidade: varredura LOCAL de marca e vazamento (PROPOSTA, nao e politica aprovada).
Somente leitura. Nao edita, nao envia, nao usa rede. Uso:
  python3 -I docs/operacao/qualidade_scan.py [raiz]   (raiz padrao: .)
Zonas: PUBLICA (loja/, marketing-teste/, README.md) = achado vale como bloqueio.
       INTERNA (docs/, agents/, pesquisa/, CLAUDE.md) = termo em lista de 'evitar' e esperado -> so informativo.
       produtos/ NAO e varrido por texto (o segredo mora la; quem vigia e o dono do produto).
Saida: uma linha por achado: SEV|zona|arquivo:linha|regra|trecho (trecho curto).
Codigo de saida: 0 sem BLOQUEIO, 2 com BLOQUEIO.
"""
import os, re, sys, json, struct, subprocess, shutil
RAIZ = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
TXT = {".md", ".html", ".txt", ".json", ".csv", ".py", ".liquid", ".css", ".js"}
IMG = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".tif", ".tiff"}
VID = {".mp4", ".mov", ".m4v", ".webm"}
# Manifesto: arquivos cujo texto pode SAIR (loja, legenda, resposta a cliente, politica). Todo o resto e trabalho interno.
# Manter atualizado pelo Qualidade; arquivo novo em loja/ ou marketing-teste/ sem estar aqui cai em INTERNA (lacuna conhecida).
_mt = os.path.join(RAIZ, "marketing-teste")
PUBLICOS = {"loja/seo-produto.md","loja/estado-loja.md","loja/politicas-rascunho.md","loja/atendimento-respostas.md",
            "loja/wireframe-mobile.html","loja/wireframe-mobile.png","marketing-teste/copy-final.md",
            "marketing-teste/calendario-4-semanas.md"}
if os.path.isdir(_mt):
    PUBLICOS |= {f"marketing-teste/{n}" for n in os.listdir(_mt) if n.lower().endswith((".png", ".jpg", ".mp4", ".mov"))}
EVITAR = re.compile(r"evit|proibid|nunca|n[aã]o (usar|fazer|dizer)|palavras? que|n[aã]o menciona|reprova|risco|checklist|vocabul[aá]rio|n[aã]o confirma|\bn[aã]o\b.{0,25}\b(diz|cit)", re.I)
def zona(rel):
    p = rel.split(os.sep)
    if p[0] == "produtos": return "PRODUTO"
    if rel in PUBLICOS or rel == "README.md": return "PUBLICA"
    if rel.startswith("docs/operacao/") and rel.endswith(".md"): return "OPERACAO"
    return "INTERNA"
# (sev em zona publica, regex, regra)  -- lista de TERMOS DE MARCA/LOJA conhecidos (revisao.md, parecer juridico, base 02-MARCA)
TERMOS = [
 ("BLOQUEIO", r"\b(escond\w+|ocult\w+|camufl\w+|esconderijo)\b", "P1 vocabulario de ocultacao"),
 ("BLOQUEIO", r"\bcompartiment\w*", "P1 'compartimento'"),
 ("BLOQUEIO", r"\b(secret[oa]s?|fundo falso|cofre|ningu[eé]m vai ver|[aà] prova de)\b", "P1 termo proibido"),
 ("BLOQUEIO", r"tem um segredo|adivinha o que tem dentro", "P1 frase proibida"),
 ("BLOQUEIO", r"#(segredo|escondido|compartimento)", "P1 hashtag proibida"),
 ("BLOQUEIO", r"tampa\s+de\s+rosca|rosca\b", "P2 sugere mecanismo em texto publico"),
 ("ALERTA",   r"\bsegredo\b", "P3 palavra 'segredo' fora de produtos/"),
 ("ALERTA",   r"nada\s+de\s*mais|nada demais", "T1 teaser forcado"),
 ("ALERTA",   r"\b(incr[ií]vel|revolucion\w+|exclusiv\w+|premium)\b", "T2 superlativo vazio"),
 ("ALERTA",   r"\bseguro\b|\bseguran[cç]a\b", "J1 alegacao de seguranca"),
 ("ALERTA",   r"\bgadget\b", "T3 'gadget' (marca nao e gadget)"),
]
CAIXA_ALTA = re.compile(r"NADA É SÓ O QUE PARECE")  # lema em caixa alta em peca publica
ach = []
def add(sev, z, loc, regra, trecho=""):
    ach.append((sev, z, loc, regra, trecho.strip()[:90]))
import unicodedata
_LEET = str.maketrans("01345$@", "oieasaa")
def norm(t):
    """anti-evasao: NFKD, tira acento e zero-width, leet simples, hifen/ponto -> espaco, junta letras soltas (e s c o n d e r)."""
    t = unicodedata.normalize("NFKD", t); t = "".join(c for c in t if not unicodedata.combining(c) and c not in "\u200b\u200c\u200d\u2060\ufeff")
    t = t.lower().translate(_LEET); t = re.sub(r"[-_.]+", " ", t)
    return re.sub(r"\b(?:\w ){3,}\w\b", lambda m: m.group(0).replace(" ", ""), t)
def varre_texto(path, rel, z):
    try: txt = open(path, encoding="utf-8", errors="replace").read()
    except Exception as e: add("ERRO", z, rel, "leitura", str(e)); return
    varre_numeros(path, rel, z)
    for n, lin in enumerate(txt.splitlines(), 1):
        for sev, rx, regra in TERMOS:
            m = re.search(rx, lin, re.I) or re.search(rx, norm(lin), re.I)
            if m:
                s = sev if z == "PUBLICA" else "INFO"   # em doc interno e lista de 'evitar' (revisar, nao bloquear)
                if z == "PUBLICA" and EVITAR.search(lin): s = "REVISAR"  # parece lista de 'evitar'/resposta-modelo: humano confere contexto
                add(s, z, f"{rel}:{n}", regra, lin)
        if CAIXA_ALTA.search(lin) and z == "PUBLICA":
            add("ALERTA", z, f"{rel}:{n}", "T4 lema em caixa alta em peca publica", lin)
def png_chunks(path):
    out = []
    with open(path, "rb") as f:
        if f.read(8) != b"\x89PNG\r\n\x1a\n": return out
        while True:
            h = f.read(8)
            if len(h) < 8: break
            ln, tp = struct.unpack(">I4s", h)
            out.append((tp.decode("latin1"), ln)); f.seek(ln + 4, 1)
    return out
ASSINAT = [b"c2pa", b"jumb", b"trainedAlgorithmicMedia", b"DigitalSourceType", b"Midjourney", b"DALL", b"Firefly", b"Stable Diffusion", b"GPS", b"<x:xmpmeta", b"Photoshop", b"iTXt", b"tEXt", b"eXIf", b"caBX"]
ROTULO = re.compile(r"simula|chute|estimativ|hip[oó]tese|a confirmar|a definir|sugest|proposta|exemplo|ilustrativ|fonte:|premissa|meta\b|teto|limite|\(a confirmar|n[aã]o (medido|confirmado)", re.I)
NUM = re.compile(r"R\$\s?\d|\b\d+[,.]?\d*\s?%|\b\d+\s?(g|horas?|h|dias?|min)\b", re.I)
def varre_numeros(path, rel, z):
    """N. numero sem rotulo: R$, %, g, h, dias sem marcador de estimativa/simulacao na linha ou +-2 linhas."""
    if z not in ("PUBLICA", "OPERACAO"): return
    L = open(path, encoding="utf-8", errors="replace").read().splitlines(); n_sem = 0; ex = None
    for i, lin in enumerate(L):
        if NUM.search(lin) and not ROTULO.search(" ".join(L[max(0, i-2):i+3])):
            n_sem += 1; ex = ex or f"{i+1}: {lin}"
    if n_sem: add("ALERTA" if z == "PUBLICA" else "INFO", z, rel, f"Q1 {n_sem} linha(s) com numero sem rotulo SIMULACAO/estimativa", ex or "")
def varre_imagem(path, rel, z):
    if z == "PRODUTO": return
    ext = os.path.splitext(path)[1].lower()
    if ext == ".png":
        for tp, ln in png_chunks(path):
            if tp in ("tEXt", "iTXt", "zTXt", "eXIf", "caBX", "iCCP"):
                add("ALERTA", z, rel, f"M1 chunk PNG {tp} ({ln} B)")
            if tp == "caBX":   # C2PA: decisao do Joao (2026-11-20): remover dos PNG de teste. Aqui so AVISO, nunca bloqueia.
                add("INFO", z, rel, "M7 C2PA presente (aviso: plataforma pode rotular IA sozinha; ver qualidade.md secao 9)")
    raw = open(path, "rb").read()
    for a in ASSINAT[:11]:
        if a in raw and not (ext == ".png" and a in (b"iTXt", b"tEXt", b"eXIf")):
            add("ALERTA", z, rel, f"M2 assinatura '{a.decode()}' nos bytes")
    try:
        from PIL import Image
        im = Image.open(path); ex = im.getexif()
        if len(ex): add("ALERTA", z, rel, "M3 EXIF presente", str(dict(list(ex.items())[:4])))
    except Exception: pass
def varre_video(path, rel, z):
    if shutil.which("ffprobe") is None: add("ERRO", z, rel, "ffprobe ausente"); return
    r = subprocess.run(["ffprobe","-v","error","-show_entries","format_tags:stream_tags","-of","json",path],capture_output=True,text=True)
    try: j = json.loads(r.stdout)
    except Exception: return
    tags = dict(j.get("format", {}).get("tags", {}))
    for s in j.get("streams", []): tags.update({"stream."+k: v for k, v in s.get("tags", {}).items()})
    for k, v in tags.items():
        if k in ("major_brand","minor_version","compatible_brands","language","handler_name","vendor_id","encoder","stream.language","stream.handler_name","stream.vendor_id","stream.encoder"): continue
        add("ALERTA", z, rel, f"M4 tag de video '{k}'", str(v))
    raw = open(path, "rb").read(4_000_000)
    for a in (b"c2pa", b"jumb", b"uuid"):
        if a in raw: add("ALERTA", z, rel, f"M5 box/assinatura '{a.decode()}' no MP4")
def varre_pdf(path, rel, z):
    if shutil.which("pdfinfo"):
        r = subprocess.run(["pdfinfo", path], capture_output=True, text=True)
        for l in r.stdout.splitlines():
            if l.split(":")[0] in ("Author","Creator","Producer","Title","Subject","Keywords"): add("ALERTA", z, rel, "M6 metadado PDF", l)
NOME_RX = re.compile(r"(secret|segred|escond|compart|oculto|hidden|stash|rosca|thread|mecanis)", re.I)
for d, ds, fs in os.walk(RAIZ):
    ds[:] = [x for x in ds if x not in (".git", "__pycache__", "node_modules")]
    for fn in fs:
        path = os.path.join(d, fn); rel = os.path.relpath(path, RAIZ); z = zona(rel); ext = os.path.splitext(fn)[1].lower()
        if z != "PRODUTO" and NOME_RX.search(fn): add("BLOQUEIO" if z=="PUBLICA" else "ALERTA", z, rel, "N1 nome de arquivo sugere mecanismo")
        if z == "PRODUTO": continue
        if ext in TXT: varre_texto(path, rel, z)
        elif ext in IMG: varre_imagem(path, rel, z)
        elif ext in VID: varre_video(path, rel, z)
        elif ext == ".pdf": varre_pdf(path, rel, z)
ordem = {"BLOQUEIO":0,"REVISAR":1,"ALERTA":2,"INFO":3,"ERRO":4}
ach.sort(key=lambda a: (ordem[a[0]], a[2]))
for a in ach: print("|".join(a))
from collections import Counter
c = Counter(a[0] for a in ach); print("\nRESUMO:", dict(c), file=sys.stderr)
sys.exit(2 if c.get("BLOQUEIO") else 0)
