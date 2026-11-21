# Conferência dos modelos (2026-11-20)

Interno. Agent Modelagem. Cadquery 2.8.0 + trimesh 5.2.1 instalados via pip.

## Como foi feito
Os 3 scripts rodaram numa **cópia** em pasta temporária. Os STL da pasta `modelo/` **não foram sobrescritos**. Comparei original x novo (extensão, volume, nº de triângulos).

## Resultado da comparação
| STL | Extensão (mm) | Volume cm³ | Watertight | Original x novo |
|---|---|---|---|---|
| corpo_v4_canelura_80x150 | 80,0 x 80,0 x 150,0 | 161,12 | sim | geometria idêntica (bytes diferem) |
| tampa_v4 | 69,2 x 69,2 x 12,0 (z 2 a 14) | 42,61 | sim | geometria idêntica |
| tampa_v5 | 69,2 x 69,2 x 12,0 | 22,91 | sim | geometria idêntica |
| cupom_anel_v4 | 76,0 x 76,0 x 14,0 | 12,00 | sim | idêntica (3836 x 3832 triângulos, volume igual) |

Os bytes mudam só por ordem/tessellação. Nada a avisar sobre geometria: os STL existentes continuam válidos.
Winding consistente em todos.

## Medidas conferidas
- Formato 80x150: ok (corpo 80 x 150).
- Folga da rosca 0,4 mm, medida no STL:
  - boca do corpo/anel r 33,39 (nominal 33,4) x núcleo da tampa r 32,99 (33,0): **0,4 radial**.
  - crista da tampa r 34,6 x fundo da ranhura r 35,0: **0,4 radial**.
- Paredes (bico 0,6):
  - Corpo, furo de cima Ø74 (r 37) até r 40: 3,0 mm = 5 x 0,6. Com canelura (0,6 de fundo): mín. 2,4 = 4 x 0,6. Ok.
  - Fundo falso z45 a 48: 3,0 = 5 x 0,6. Ok.
  - Corpo na rosca (r 33,4 a 40): 6,6 = 11 x 0,6. Ok.
  - Anel do cupom (r 33,4 a 38): 4,6 = 7,67 x 0,6. **Não é múltiplo** (4,2 ou 4,8 seria).
  - Tampa v5, parede do bolso (r 28 a 33): 5,0 = 8,33 x 0,6. **Não é múltiplo** (4,8 seria).
  - Tampa v5, piso do bolso: 2,4 = 4 x 0,6. Ok.
- Teto da cavidade: plano (Ø62 em z45), suporte só ali, como decidido.

## Observações
- Peças não impressas; tudo é estimativa até o cupom.
- Seção da rosca confere nos dois lados (corpo e tampa) pelos raios acima.

## Decisões pra você
1. Paredes fora de múltiplo (anel do cupom 4,6; tampa v5 5,0). Recomendo **deixar assim no cupom** (já vai imprimir; o fatiador completa com 1 linha de ajuste) e corrigir só no v6 (bolso r 28,2 -> parede 4,8).
2. Cupom: manter folga 0,4 nominal. Recomendo **imprimir como está** e só mexer na folga depois do resultado.
