"""Porta-lápis Faixa Preta, v5: tampa oca por cima (economiza filamento).

Tudo em milímetros. Rode: python porta-lapis_v5.py
Gera: tampa_v5.stl. Corpo e anel do cupom continuam os do v4
(corpo_v4_canelura_80x150.stl, cupom_anel_v4.stl).
A rosca e a ranhura são idênticas à tampa v4. Só entra um bolso aberto pra cima,
que também aumenta a cavidade. Imprima com a ranhura na mesa e o bolso pra cima
(sem overhang).
ESTIMATIVA: nada foi impresso nem validado.
"""
import importlib.util as u
import os
import cadquery as cq

here = os.path.dirname(os.path.abspath(__file__))
s = u.spec_from_file_location("v3", os.path.join(here, "porta-lapis_v3.py"))
v3 = u.module_from_spec(s)
s.loader.exec_module(v3)

POCKET_R = 28.0          # bolso Ø56, deixa 5 mm de parede até o núcleo da rosca
POCKET_Z0 = 6.0          # piso do bolso (ranhura vai até z=3,6, sobra 2,4 mm)


def make_tampa_v5():
    lid = v3.make_tampa()
    pocket = (cq.Workplane("XY").workplane(offset=POCKET_Z0)
              .circle(POCKET_R).extrude(v3.LID_Z1 - POCKET_Z0 + 0.01))
    return lid.cut(pocket)


if __name__ == "__main__":
    out = os.path.join(here, "tampa_v5.stl")
    cq.exporters.export(make_tampa_v5(), out, tolerance=0.05, angularTolerance=0.1)
    print("ok tampa_v5.stl")
