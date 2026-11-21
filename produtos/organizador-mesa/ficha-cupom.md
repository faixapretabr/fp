# Ficha de impressão: cupom da rosca

Interno. Pra levar à impressora. Peças: anel (`modelo/cupom_anel_v4.stl`) + tampa. Objetivo: confirmar a folga da rosca (0,4 mm) antes do corpo inteiro. Resultado final vai pra `03-validacao.md`.

Legenda: **[fato]** definido pelo humano ou medido no modelo. **[estimativa]** ponto de partida, não testado.

## Peças
| Peça | Arquivo | Obs |
|---|---|---|
| Anel | `cupom_anel_v4.stl` | Ø ext. 76, altura 14, rosca do corpo (passo 6 mm) |
| Tampa | `tampa_v5.stl` (recomendado) ou `tampa_v4.stl` | Rosca e ranhura idênticas nas duas. Ver decisão no fim |

## Parâmetros
| Item | Anel | Tampa | Status |
|---|---|---|---|
| Material | PETG | PETG | [fato] |
| Bico | 0,6 mm | 0,6 mm | [fato] |
| Cor | preta (ou qualquer, só pra teste) | preta | [fato] cor da tampa final |
| Altura de camada | 0,2 mm | 0,2 mm | [estimativa] (faixa fixada: 0,2 a 0,3) |
| Largura de linha | 0,6 a 0,7 mm | idem | [estimativa] |
| Paredes | 3 | 3 | [estimativa] |
| Topo/base | 5 camadas | 5 camadas | [estimativa] |
| Infill | 100% | v4: 100% / v5: ~25% | [estimativa] |
| Orientação | em pé, z=0 na mesa | ranhura na mesa, bolso (v5) pra cima | [fato] vem da validação |
| Suporte | nenhum | nenhum | flancos a 45° no limite, aceitável [fato da validação] |
| Aba/brim | sem | sem | [estimativa] |
| Temp. bico | 235 °C | 235 °C | [estimativa] (faixa PETG 230-250, seguir o rótulo do filamento) |
| Temp. mesa | 80 °C | 80 °C | [estimativa] (faixa 70-85) |
| Ventilador | 30 a 50% | 30 a 50% | [estimativa] (flancos limpos, sem perder aderência de camada) |
| Velocidade | ~40 mm/s, paredes externas ~30 | idem | [estimativa] |
| Retração | ligada, ajustar contra fio | idem | [estimativa] |
| Costura (seam) | alinhada fora da rosca se possível | idem | [estimativa] |
| Resolução do slicer | ≤0,1 mm | ≤0,1 mm | [estimativa] |

Mesma configuração de camada nas duas peças: a folga de teste só vale se as duas saírem sob as mesmas condições. Imprimir as duas no mesmo dia, mesmo rolo.
Tempo/massa [estimativa]: anel ~1 h, ~13 g. Tampa v4 ~2-3 h, ~54 g. Tampa v5 ~1-2 h, ~25 g.

## Antes de imprimir
- [ ] Filamento seco (PETG úmido faz fio e estraga flanco). Secar se estalar.
- [ ] Mesa limpa, primeira camada ok.
- [ ] Anotar: filamento (marca/cor/lote), temperaturas reais usadas, versão do slicer.

## Tabela de medição (preencher depois de imprimir)
Paquímetro 0,01 mm. Medir 3 pontos (0°, 120°, 240°) e anotar a média. Esperar o anel e a tampa esfriarem e repousarem ~1 h antes.

### Identificação
| Campo | Valor |
|---|---|
| Data | |
| Impressora / bico | |
| Filamento (marca, cor, lote) | |
| Tampa usada (v4 ou v5) | |
| Temp. bico / mesa reais | |
| Camada / ventilador reais | |

### Dimensões (nominal do modelo [fato])
| Medida | Nominal | Medido 1 | Medido 2 | Medido 3 | Média | Desvio |
|---|---|---|---|---|---|---|
| Anel: Ø interno do furo (entre cristas) | 66,8 mm (raio 33,4) | | | | | |
| Anel: Ø do fundo do canal da rosca | 70,0 mm (raio 35) | | | | | |
| Anel: altura total | 14,0 mm | | | | | |
| Anel: Ø externo | 76,0 mm | | | | | |
| Tampa: Ø do núcleo (fundo do filete) | 66,0 mm (raio 33,0) | | | | | |
| Tampa: Ø da crista | 69,2 mm (raio 34,6) | | | | | |
| Passo (crista a crista) | 6,0 mm | | | | | |

Desvio = média menos nominal. Se o Ø do canal sair >0,2 mm menor ou a crista >0,2 mm maior, a folga some. Anotar.

### Encaixe e uso
| Campo | Resultado |
|---|---|
| Entra sem forçar? (sim/não) | |
| Voltas até assentar (esperado ~2) | |
| Folga sentida: presa / justa ok / frouxa | |
| Folga radial medida (balançar a tampa): mm | |
| Folga axial (jogo pra cima/baixo): mm | |
| Torque pra abrir: só dedos / precisa moeda / precisa ferramenta | |
| Torque pra fechar: só dedos / precisa moeda / precisa ferramenta | |
| Trava no meio da volta? Em que ponto | |
| Abre com moeda na ranhura? | |
| Ruído/atrito (raspa, estala) | |
| Flancos: lisos / ásperos / fios (stringing) | |
| A camada de 0,2 resolveu os flancos 45°? | |
| Abre e fecha 20 vezes: afrouxou/desgastou? | |
| Fotos tiradas (flanco, topo, encaixe) | |

Torque: se tiver, medir com chave de torque ou balança + braço. Sem instrumento, usar a escala acima e não inventar número.

## Critério passa / não passa
**PASSA** (todos):
1. Entra sem forçar e assenta em ~2 voltas (1,5 a 2,5 aceito).
2. Abre e fecha só com os dedos. Moeda na ranhura é o plano B, não o normal.
3. Sem trava, sem raspar, em nenhum ponto da volta.
4. Folga radial perceptível mas pequena (tampa não balança solta). Sem jogo axial grande.
5. Flancos sem fio nem rebarba que atrapalhe. Aspereza leve é aceitável.
6. Resiste a 20 ciclos sem afrouxar nem marcar.

**NÃO PASSA**: qualquer item acima falhar.

## O que fazer em cada caso (v6)
| Resultado | Ação | Mudança no v6 |
|---|---|---|
| Passa | Registrar em `03-validacao.md`, manter folga 0,4. Sem v6 da rosca. Seguir pro protótipo do corpo | nenhuma |
| Presa / justa demais (não entra, ou só com chave) | Subir a folga pra 0,5. Reimprimir só o anel | `GAP` 0,5 no script, gerar cupom v6 |
| Presa só em um ponto da volta | Suspeita de costura ou fio, não de folga. Limpar, reimprimir mudando a posição da costura antes de mexer no modelo | nenhuma até repetir |
| Frouxa (balança, folga axial grande) | Voltar pra 0,3. Reimprimir o anel | `GAP` 0,3, cupom v6 |
| Desvio de medida >0,2 mm consistente | Problema de calibração (fluxo, passos), não de modelo. Compensar no slicer e repetir | nenhuma |
| Flancos ásperos / com fio | Revisar temperatura, ventilador, retração, secar filamento. Se persistir, aumentar o raio de topo do filete | avaliar perfil da rosca |
| Entra, mas torque alto pra abrir | Mesma família de "presa": 0,5 mm | `GAP` 0,5 |

Regra: mudar uma variável por vez e reimprimir só o anel (a tampa serve de calibre). Dois ciclos sem passar: escalar pro humano antes de seguir. Não liberar o corpo inteiro sem cupom aprovado fisicamente.

## Resultado
_(preencher depois da impressão; copiar o resumo pra `03-validacao.md`)_
- Veredito: passa / não passa
- Folga final adotada:
- Notas:

## Decisões pro humano
1. **Tampa do cupom: v5 ou v4?** Recomendo v5 (vigente, menos filamento e tempo, rosca idêntica). A `03-validacao.md` cita a v4, vale atualizar lá.
2. **Imprimir uma segunda rodada já com 0,3/0,4/0,5 num anel só?** Recomendo não: começa em 0,4 (adotada). Só variar se falhar, pra não gastar filamento.
