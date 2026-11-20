# Parâmetros de impressão: organizador de mesa

Interno. Definido pelo humano: **PETG, bico 0,6 mm**. Valores abaixo são ponto de partida (estimativa), não testados.

## Fixo
- Material: PETG.
- Bico: 0,6 mm. Largura de linha ~0,6 a 0,7 mm.

## Sugerido (estimativa, confirmar no protótipo)
| Item | Corpo | Tampa (rosca) |
|---|---|---|
| Altura de camada | 0,3 mm | 0,2 mm |
| Paredes (perímetros) | 3 (~2 mm) | 3 |
| Topo/base | 5 camadas | 5 camadas |
| Infill | 15% | 100% (peça pequena, rosca) |
| Temp. bico / mesa | conforme o filamento (PETG costuma ficar em 230-250 / 70-85) | idem |
| Orientação | em pé, borda da rosca na mesa | face da ranhura na mesa |

Definido pelo humano em 2026-11-20. Regras de modelagem que decorrem disso:
- Paredes em múltiplos de ~0,6 mm.
- Folga de rosca mínima de 0,4 mm.
- Camada de 0,2 a 0,3 mm.
- Evitar pontes longas.

## O que o bico 0,6 muda no desenho
- Divisórias de 2 mm: ok (≈3 linhas).
- Fundo falso de 3 mm: ok (10 camadas de 0,3).
- Rosca: folga de 0,3 mm é pouca pra PETG com bico 0,6. Proposta: 0,4 mm (decidir no v3).
- Detalhe fino (crista da rosca de 1,2 mm) sai arredondado. Imprimir a tampa com camada de 0,2.

## Problemas conhecidos a resolver na Validação
- **Ponte de 62 mm**: o fundo falso fecha a cavidade no meio do tubo. Imprimindo em pé, o teto da cavidade é uma ponte de Ø62. PETG com bico 0,6 faz ponte média, e 62 mm é muito. Opções: teto em cone ou cúpula de 45° (sem suporte), ou suporte só ali.
- PETG tende a fazer fio (stringing) e a colar demais: testar a rosca com folga maior.
- Sem vedação: não é à prova de água.

## Economia de filamento (v5)
- `tampa_v5.stl`: bolso Ø56 aberto por cima, piso a 2,4 mm da ranhura. -19,7 cm³ (-46%) contra a tampa v4. Rosca e ranhura idênticas. Imprimir com a ranhura na mesa e o bolso pra cima.
- Fatiador (estimativa): corpo com infill 10% gyroid, 3 paredes, 4 camadas de topo e fundo. Tampa v5 com 3 paredes e infill ~25%.
- Meta: de ~205 g pra ~165 g (corpo + tampa). Cupom (anel + tampa v5): ~40 g.

## Suporte da cavidade (decisão do humano)
Teto plano do v4 (Ø62 em z=45), com suporte só dentro da cavidade. Pontos de partida (estimativa, ajustar no protótipo):
- Suporte **só onde pintado/forçado** (support enforcer) na cavidade. Bloquear no resto, em especial na rosca: suporte nos flancos estragaria o perfil.
- Coluna sobe da mesa (a cavidade é aberta por baixo pela boca da rosca), mantendo folga do canal da rosca (raio ≤ ~30 mm).
- Distância vertical do suporte ao teto: 0,3 mm (PETG gruda em PETG; folga maior solta mais fácil).
- Camadas de interface no topo: 2 a 3. Densidade do suporte: ~10-15%.
- Retirada pela boca da rosca depois de esfriar. Lixar o teto se ficar áspero (fica escondido dentro da cavidade).
- Medir no protótipo: o teto cedeu? Sobrou marca? O suporte saiu inteiro?

## Pendências
- [ ] Folga da rosca: 0,4 mm adotada, a confirmar no cupom (presa: 0,5; frouxa: 0,3).
- [x] Teto da cavidade: suporte (decidido).
- [ ] Imprimir um anel de teste da rosca antes da peça inteira.
