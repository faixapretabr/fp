"""Cupom de teste da rosca v4: anel curto com a rosca do corpo + a tampa v4.
Imprima o anel em pé (z=0 na mesa) e a tampa com a ranhura na mesa.
Gera cupom_anel_v4.stl. A tampa é a própria tampa_v4.stl.
"""
import importlib.util as u, os, cadquery as cq
here = os.path.dirname(os.path.abspath(__file__))
s = u.spec_from_file_location("m", os.path.join(here, "porta-lapis_v3.py"))
m = u.module_from_spec(s); s.loader.exec_module(m)
ring = cq.Workplane("XY").circle(38.0).circle(m.R_BORE).extrude(m.SHOULDER_Z)
g = m.groove(-m.PITCH, m.SHOULDER_Z + m.PITCH)
clip = cq.Workplane("XY").workplane(offset=-0.01).circle(m.R_GROOVE + 1).extrude(m.SHOULDER_Z + 0.01)
ring = ring.cut(g.intersect(clip))
cq.exporters.export(ring, os.path.join(here, "cupom_anel_v4.stl"), tolerance=0.05, angularTolerance=0.1)
print("ok cupom_anel_v4.stl")
