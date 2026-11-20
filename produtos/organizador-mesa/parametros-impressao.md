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

## O que o bico 0,6 muda no desenho
- Divisórias de 2 mm: ok (≈3 linhas).
- Fundo falso de 3 mm: ok (10 camadas de 0,3).
- Rosca: folga de 0,3 mm é pouca pra PETG com bico 0,6. Proposta: 0,4 mm (decidir no v3).
- Detalhe fino (crista da rosca de 1,2 mm) sai arredondado. Imprimir a tampa com camada de 0,2.

## Problemas conhecidos a resolver na Validação
- **Ponte de 62 mm**: o fundo falso fecha a cavidade no meio do tubo. Imprimindo em pé, o teto da cavidade é uma ponte de Ø62. PETG com bico 0,6 faz ponte média, e 62 mm é muito. Opções: teto em cone ou cúpula de 45° (sem suporte), ou suporte só ali.
- PETG tende a fazer fio (stringing) e a colar demais: testar a rosca com folga maior.
- Sem vedação: não é à prova de água.

## Pendências
- [ ] Decidir folga da rosca (0,3 ou 0,4).
- [ ] Decidir teto da cavidade (cone, cúpula ou suporte).
- [ ] Imprimir um anel de teste da rosca antes da peça inteira.
