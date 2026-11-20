"""Porta-lápis Faixa Preta, v2: 2 peças, tampa-disco de rosca na base.

Tudo em milímetros. Rode: python porta-lapis_v2.py
Gera: corpo_v2.stl, tampa_v2.stl, montado_v2.stl.
ESTIMATIVA: nenhuma medida foi validada com impressão real.

Peça 1, corpo: Ø80 x 140, com divisórias em cruz por dentro e, por baixo,
uma rosca onde entra a tampa, recuada 2 mm pra não encostar na mesa.
Peça 2, tampa: disco rosqueado com ranhura pra moeda. Girar abre a cavidade secreta.
Rosca: passo 6, perfil trapezoidal de flancos a 45° (imprime sem suporte
com o eixo na vertical).
"""
import math
import os
import cadquery as cq

OUT = os.path.dirname(os.path.abspath(__file__))

# ---- Corpo ----
H = 140.0
OD = 80.0
BORE_TOP = 74.0          # furo de cima (onde vão os lápis)
FLOOR_Z0, FLOOR_Z1 = 45.0, 48.0   # fundo falso
DIV_T = 2.0              # espessura das divisórias
DIV_TOP = 130.0          # divisórias vão até 10 mm abaixo da borda

# ---- Cavidade secreta e rosca ----
CAV_D = 62.0             # cavidade
SHOULDER_Z = 14.0        # onde a tampa encosta
PITCH = 6.0
R_BORE = 33.4            # raio do furo da rosca (crista do dente do corpo)
R_GROOVE = 35.0          # raio do fundo do canal no corpo (parede restante 5 mm)
R_CORE = 33.1            # raio do núcleo da tampa (folga 0,3)
R_CREST = 34.7           # raio da crista da rosca da tampa (folga 0,3)

# ---- Tampa ----
LID_Z0 = 2.0             # recuo da base
LID_Z1 = SHOULDER_Z      # topo da tampa encosta no ombro
SLOT_W, SLOT_D = 3.0, 1.6


def helix_profile(points, z0, length):
    """Varre um perfil (r, dz) ao longo de uma hélice de passo PITCH.
    A hélice começa em z0 e sobe `length`."""
    helix = cq.Wire.makeHelix(PITCH, length, R_CORE, center=cq.Vector(0, 0, z0))
    prof = cq.Workplane("XZ", origin=(0, 0, z0)).polyline(points).close()
    return prof.sweep(cq.Workplane(obj=helix), isFrenet=True)


def ridge(z0, length):
    # perfil do dente da tampa: largura 4,4 na raiz, 1,2 na crista (45°)
    pts = [(R_CORE - 0.3, -2.5), (R_CORE, -2.2), (R_CREST, -0.6),
           (R_CREST, 0.6), (R_CORE, 2.2), (R_CORE - 0.3, 2.5)]
    return helix_profile(pts, z0, length)


def groove(z0, length):
    # canal do corpo: 45° também, 0,3 mm maior que o dente
    pts = [(R_BORE - 0.6, -2.95), (R_BORE, -2.35), (R_GROOVE, -0.75),
           (R_GROOVE, 0.75), (R_BORE, 2.35), (R_BORE - 0.6, 2.95)]
    return helix_profile(pts, z0, length)


def make_corpo(h=H, dividers=True):
    DIV_TOP = h - 10.0
    body = cq.Workplane("XY").circle(OD / 2).extrude(h)
    # furo de cima, até o fundo falso
    body = body.cut(
        cq.Workplane("XY").workplane(offset=FLOOR_Z1).circle(BORE_TOP / 2).extrude(h)
    )
    # cavidade secreta
    body = body.cut(cq.Workplane("XY").circle(CAV_D / 2).extrude(FLOOR_Z0))
    # boca da rosca por baixo
    body = body.cut(cq.Workplane("XY").circle(R_BORE).extrude(SHOULDER_Z))
    # canal helicoidal (começa abaixo de z=0 pra abrir na base)
    g = groove(-PITCH, SHOULDER_Z + PITCH)
    clip = cq.Workplane("XY").workplane(offset=-0.01).circle(R_GROOVE + 1).extrude(SHOULDER_Z + 0.01)
    body = body.cut(g.intersect(clip))
    # divisórias em cruz
    for ang in ((0, 90) if dividers else ()):
        wall = (cq.Workplane("XY").workplane(offset=FLOOR_Z1 - 0.5)
                .rect(BORE_TOP, DIV_T).extrude(DIV_TOP - FLOOR_Z1 + 0.5)
                .rotate((0, 0, 0), (0, 0, 1), ang))
        wall = wall.intersect(
            cq.Workplane("XY").workplane(offset=FLOOR_Z1 - 0.5)
            .circle(BORE_TOP / 2 + 0.5).extrude(DIV_TOP))
        body = body.union(wall)
    return body


def make_tampa():
    h = LID_Z1 - LID_Z0
    lid = cq.Workplane("XY").workplane(offset=LID_Z0).circle(R_CORE).extrude(h)
    # mesma fase do canal do corpo (começa em z=-PITCH, ângulo 0)
    r = ridge(-PITCH, LID_Z1 + 2 * PITCH)
    clip = cq.Workplane("XY").workplane(offset=LID_Z0).circle(R_CREST + 1).extrude(h)
    lid = lid.union(r.intersect(clip), tol=1e-3)
    # ranhura pra moeda na face de baixo
    slot = (cq.Workplane("XY").workplane(offset=LID_Z0 - 0.01)
            .rect(2 * R_CORE + 4, SLOT_W).extrude(SLOT_D + 0.01))
    return lid.cut(slot)


def export(shape, name):
    path = os.path.join(OUT, name)
    cq.exporters.export(shape, path, tolerance=0.05, angularTolerance=0.1)
    print("ok", name)


if __name__ == "__main__":
    tampa = make_tampa()
    export(tampa, "tampa_v2.stl")  # a mesma tampa serve nas duas versões
    # A: 80x140 com divisórias em cruz
    corpo = make_corpo(140.0, True)
    export(corpo, "corpo_v2.stl")
    export(corpo.union(tampa), "montado_v2.stl")
    # B: 80x150 sem divisórias
    corpo_b = make_corpo(150.0, False)
    export(corpo_b, "corpo_v2b_80x150.stl")
    export(corpo_b.union(tampa), "montado_v2b_80x150.stl")
