"""Porta-lápis Faixa Preta, v1: fundo falso com trava de baioneta.

Tudo em milímetros. Rode: python porta-lapis_v1.py
Gera: corpo_v1.stl, base_v1.stl, montado_v1.stl (base travada, só pra preview).
ESTIMATIVA: nenhuma medida foi validada com impressão real.
"""
import math
import os
import cadquery as cq

OUT = os.path.dirname(os.path.abspath(__file__))

# ---- Parâmetros ----
H = 100.0          # altura do corpo
OD = 80.0          # diâmetro externo
BORE_TOP = 74.0    # furo visível (onde vão os lápis)
FLOOR_Z0 = 18.0    # fundo falso: de z=18 a z=21
FLOOR_Z1 = 21.0
BORE_BOT = 70.0    # cavidade secreta (por baixo do fundo falso)
GROOVE_R = 37.0    # raio externo do canal da baioneta
GROOVE_Z0, GROOVE_Z1 = 4.0, 7.0
TWIST = 32.0       # ângulo total do canal (graus)
LUG_W = 12.0       # largura angular do pino
CLEAR = 1.0        # folga angular na entrada (graus)
N_LUGS = 3
FLANGE_T = 3.0     # espessura do disco da base
COLLAR_OD = 69.4   # folga radial ~0,3 mm
COLLAR_ID = 65.0
COLLAR_H = 8.0
LUG_R = 36.6       # raio externo do pino (folga 0,4 mm no canal)
LUG_Z0, LUG_Z1 = 4.3, 6.7
LOCK_ANGLE = 20.0  # base gira até aqui pra travar


def sector(r_in, r_out, a0, a1, z0, h, steps=24):
    """Fatia de anel entre os ângulos a0 e a1 (graus)."""
    pts = []
    for i in range(steps + 1):
        a = math.radians(a0 + (a1 - a0) * i / steps)
        pts.append((r_out * math.cos(a), r_out * math.sin(a)))
    for i in range(steps, -1, -1):
        a = math.radians(a0 + (a1 - a0) * i / steps)
        pts.append((r_in * math.cos(a), r_in * math.sin(a)))
    return cq.Workplane("XY").workplane(offset=z0).polyline(pts).close().extrude(h)


def make_corpo():
    body = cq.Workplane("XY").circle(OD / 2).extrude(H)
    # furo de cima, termina no fundo falso
    body = body.cut(
        cq.Workplane("XY").workplane(offset=FLOOR_Z1).circle(BORE_TOP / 2).extrude(H)
    )
    # cavidade secreta por baixo
    body = body.cut(cq.Workplane("XY").circle(BORE_BOT / 2).extrude(FLOOR_Z0))
    # canal da baioneta (entrada vertical + trilho circular), 3 vezes
    for k in range(N_LUGS):
        base = 360.0 / N_LUGS * k
        entrada = sector(BORE_BOT / 2 - 0.5, GROOVE_R, base - CLEAR,
                         base + LUG_W + CLEAR, 0, GROOVE_Z1)
        trilho = sector(BORE_BOT / 2 - 0.5, GROOVE_R, base - CLEAR,
                        base + TWIST, GROOVE_Z0, GROOVE_Z1 - GROOVE_Z0)
        body = body.cut(entrada).cut(trilho)
    return body


def make_base():
    # disco (fica por baixo do corpo, z de -3 a 0)
    base = cq.Workplane("XY").workplane(offset=-FLANGE_T).circle(OD / 2).extrude(FLANGE_T)
    collar = (cq.Workplane("XY").circle(COLLAR_OD / 2).circle(COLLAR_ID / 2)
              .extrude(COLLAR_H))
    base = base.union(collar)
    for k in range(N_LUGS):
        a0 = 360.0 / N_LUGS * k
        lug = sector(COLLAR_OD / 2 - 0.5, LUG_R, a0, a0 + LUG_W, LUG_Z0, LUG_Z1 - LUG_Z0)
        base = base.union(lug)
    return base


def export(shape, name):
    path = os.path.join(OUT, name)
    cq.exporters.export(shape, path, tolerance=0.05, angularTolerance=0.1)
    print("ok", name)


if __name__ == "__main__":
    corpo = make_corpo()
    base = make_base()
    export(corpo, "corpo_v1.stl")
    export(base, "base_v1.stl")
    # montado: base girada até o fim do canal (travada)
    travada = base.rotate((0, 0, 0), (0, 0, 1), LOCK_ANGLE)
    export(corpo.union(travada), "montado_v1.stl")
