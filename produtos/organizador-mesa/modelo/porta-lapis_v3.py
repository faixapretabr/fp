"""Porta-lápis Faixa Preta, v3: v2 + textura externa, folga 0,4 e teto cônico.

Tudo em milímetros. Rode: python porta-lapis_v3.py [textura ...]
Texturas: lisa, canelura, aneis, losango (sem argumento gera todas).
Mudanças em relação ao v2 (v2 fica intacto):
  - Folga da rosca 0,4 mm (PETG, bico 0,6).
  - Teto da cavidade em cone de 45° com topo plano de Ø20, sem ponte longa.
  - Textura na parede externa (profundidade 0,6, detalhe >= 1,2 mm pro bico 0,6).
ESTIMATIVA: nada foi impresso nem validado.
"""
import math
import os
import sys
import cadquery as cq

OUT = os.path.dirname(os.path.abspath(__file__))

# ---- Corpo ----
H = 140.0
OD = 80.0
R = OD / 2
BORE_TOP = 74.0
FLOOR_Z0, FLOOR_Z1 = 45.0, 48.0   # fundo falso
DIV_T = 2.0

# ---- Cavidade (teto cônico) ----
CAV_R = 31.0
CONE_Z0 = 24.0            # onde o cone começa
CAV_FLAT_R = 10.0         # topo plano Ø20 (ponte curta)

# ---- Rosca (folga 0,4) ----
SHOULDER_Z = 14.0
PITCH = 6.0
R_BORE = 33.4
R_GROOVE = 35.0
R_CORE = 33.0
R_CREST = 34.6

# ---- Tampa ----
LID_Z0 = 2.0
LID_Z1 = SHOULDER_Z
SLOT_W, SLOT_D = 3.0, 1.6

# ---- Textura ----
TEX_DEPTH = 0.6
TEX_BOTTOM = 16.0         # lisa até aqui (cobre a boca da rosca)
TEX_TOP_MARGIN = 10.0     # lisa nos últimos 10 mm


def helix_profile(points, z0, length):
    helix = cq.Wire.makeHelix(PITCH, length, R_CORE, center=cq.Vector(0, 0, z0))
    prof = cq.Workplane("XZ", origin=(0, 0, z0)).polyline(points).close()
    return prof.sweep(cq.Workplane(obj=helix), isFrenet=True)


def ridge(z0, length):
    pts = [(R_CORE - 0.3, -2.5), (R_CORE, -2.2), (R_CREST, -0.6),
           (R_CREST, 0.6), (R_CORE, 2.2), (R_CORE - 0.3, 2.5)]
    return helix_profile(pts, z0, length)


def groove(z0, length):
    pts = [(R_BORE - 0.6, -2.97), (R_BORE, -2.37), (R_GROOVE, -0.77),
           (R_GROOVE, 0.77), (R_BORE, 2.37), (R_BORE - 0.6, 2.97)]
    return helix_profile(pts, z0, length)


def flute_outline(n, steps=10, phase=0.0):
    pts = []
    for i in range(n * steps):
        a = 2 * math.pi * i / (n * steps)
        r = R - TEX_DEPTH * (1 - math.cos(n * a + phase)) / 2
        pts.append((r * math.cos(a), r * math.sin(a)))
    return pts


def textured_band(kind, z0, z1):
    L = z1 - z0
    if kind == "canelura":
        n = 157  # passo ~1,6 mm na superfície
        return cq.Workplane("XY").workplane(offset=z0).polyline(flute_outline(n)).close().extrude(L)
    if kind == "aneis":
        period, flat, slope = 2.4, 0.6, 0.6
        pts = [(0, z0)]
        z = z0
        prof = [(R, z)]
        while z + period <= z1 + 1e-6:
            prof += [(R, z + flat), (R - TEX_DEPTH, z + flat + slope),
                     (R - TEX_DEPTH, z + flat + slope + flat), (R, z + period)]
            z += period
        prof += [(R, z1)]
        pts = [(0, z0)] + prof + [(0, z1)]
        return (cq.Workplane("XZ").polyline(pts).close()
                .revolve(360, (0, 0, 0), (0, 1, 0)))
    if kind == "losango":
        n = 70  # passo ~3,6 mm
        ang = math.degrees(L / R)
        a = (cq.Workplane("XY").workplane(offset=z0).polyline(flute_outline(n)).close()
             .twistExtrude(L, ang))
        b = (cq.Workplane("XY").workplane(offset=z0).polyline(flute_outline(n)).close()
             .twistExtrude(L, -ang))
        return a.intersect(b)
    raise ValueError(kind)


def make_corpo(h=H, dividers=True, texture="lisa", cone=True):
    div_top = h - 10.0
    if texture == "lisa":
        body = cq.Workplane("XY").circle(R).extrude(h)
    else:
        z0, z1 = TEX_BOTTOM, h - TEX_TOP_MARGIN
        core = cq.Workplane("XY").circle(R - TEX_DEPTH).extrude(h)
        band = textured_band(texture, z0, z1)
        bottom = cq.Workplane("XY").circle(R).extrude(z0)
        top = cq.Workplane("XY").workplane(offset=z1).circle(R).extrude(h - z1)
        body = core.union(band, tol=1e-3).union(bottom, tol=1e-3).union(top, tol=1e-3)
    # furo de cima
    body = body.cut(
        cq.Workplane("XY").workplane(offset=FLOOR_Z1).circle(BORE_TOP / 2).extrude(h))
    # cavidade com teto cônico
    if cone:
        cav = (cq.Workplane("XZ")
               .polyline([(0, 0), (CAV_R, 0), (CAV_R, CONE_Z0), (CAV_FLAT_R, FLOOR_Z0), (0, FLOOR_Z0)])
               .close().revolve(360, (0, 0, 0), (0, 1, 0)))
    else:  # teto plano: ponte de Ø62 na impressão em pé
        cav = cq.Workplane("XY").circle(CAV_R).extrude(FLOOR_Z0)
    body = body.cut(cav)
    # boca da rosca
    body = body.cut(cq.Workplane("XY").circle(R_BORE).extrude(SHOULDER_Z))
    g = groove(-PITCH, SHOULDER_Z + PITCH)
    clip = cq.Workplane("XY").workplane(offset=-0.01).circle(R_GROOVE + 1).extrude(SHOULDER_Z + 0.01)
    body = body.cut(g.intersect(clip))
    for ang in ((0, 90) if dividers else ()):
        wall = (cq.Workplane("XY").workplane(offset=FLOOR_Z1 - 0.5)
                .rect(BORE_TOP, DIV_T).extrude(div_top - FLOOR_Z1 + 0.5)
                .rotate((0, 0, 0), (0, 0, 1), ang))
        wall = wall.intersect(
            cq.Workplane("XY").workplane(offset=FLOOR_Z1 - 0.5)
            .circle(BORE_TOP / 2 + 0.5).extrude(div_top))
        body = body.union(wall)
    return body


def make_tampa():
    h = LID_Z1 - LID_Z0
    lid = cq.Workplane("XY").workplane(offset=LID_Z0).circle(R_CORE).extrude(h)
    r = ridge(-PITCH, LID_Z1 + 2 * PITCH)
    clip = cq.Workplane("XY").workplane(offset=LID_Z0).circle(R_CREST + 1).extrude(h)
    lid = lid.union(r.intersect(clip), tol=1e-3)
    slot = (cq.Workplane("XY").workplane(offset=LID_Z0 - 0.01)
            .rect(2 * R_CORE + 4, SLOT_W).extrude(SLOT_D + 0.01))
    return lid.cut(slot)


def export(shape, name):
    path = os.path.join(OUT, name)
    cq.exporters.export(shape, path, tolerance=0.05, angularTolerance=0.1)
    print("ok", name, flush=True)


if __name__ == "__main__":
    if sys.argv[1:] == ["v4"]:
        # v4 escolhido: 80x150, caneluras, sem divisórias, sem cone
        export(make_tampa(), "tampa_v4.stl")
        c4 = make_corpo(150.0, False, "canelura", cone=False)
        export(c4, "corpo_v4_canelura_80x150.stl")
        sys.exit(0)
    texturas = sys.argv[1:] or ["lisa", "canelura", "aneis", "losango"]
    tampa = make_tampa()
    export(tampa, "tampa_v3.stl")
    for tx in texturas:
        try:
            export(make_corpo(140.0, True, tx), f"corpo_v3_{tx}.stl")
        except Exception as e:  # uma textura falhar não derruba as outras
            print("FALHOU", tx, e, flush=True)
