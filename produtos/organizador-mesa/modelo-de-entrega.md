# Modelo de entrega: organizador de mesa (porta-lápis)

Interno. Nada daqui vai pra marketing. Não revela o segredo: aqui só se fala de peças e parâmetros.

Este é o MODELO. Só vira `final/ficha-producao.md` depois dos dois portões humanos. Campos `____` são preenchidos na entrega. Valores entre parênteses são o ponto de partida de `parametros-impressao.md` (estimativa, não testado).

## 0. Pré-requisitos (sem isso, não preenche)
- [ ] 1º portão humano (seleção): aprovado em ____/____/____
- [ ] Cupom da rosca impresso e resultado registrado em `03-validacao.md`
- [ ] Folga da rosca confirmada: ____ mm (adotada 0,4; presa 0,5; frouxa 0,3)
- [ ] Protótipo do corpo inteiro impresso (ponte de 62 mm com suporte): ok / não ok
- [ ] 2º portão humano (validação): aprovado em ____/____/____ por ________
- [ ] Versão final fechada: corpo v__ + tampa v__

## 1. Arquivos finais (em `final/`)
| Peça | Arquivo STL | Origem (script) | Versão | Hash/data |
|---|---|---|---|---|
| Corpo | ______________ | ______________ | v__ | ______ |
| Tampa | ______________ | ______________ | v__ | ______ |

Regra: copiar o STL aprovado pra `final/`. Nunca apagar versões antigas em `modelo/`.

## 2. Parâmetros de impressão por peça
| Item | Corpo | Tampa |
|---|---|---|
| Material | PETG (fixo) | PETG (fixo) |
| Marca/lote do filamento | ______ | ______ |
| Cor | ______ | preta (definido) |
| Bico | 0,6 mm (fixo) | 0,6 mm (fixo) |
| Altura de camada | ____ (0,3) | ____ (0,2) |
| Paredes | ____ (3) | ____ (3) |
| Topo / base (camadas) | ____ (5) | ____ (5) |
| Infill | ____ (10-15%, gyroid) | ____ (25-100%) |
| Temp. bico / mesa | ____ / ____ | ____ / ____ |
| Velocidade (parede ext.) | ____ | ____ |
| Orientação | em pé, borda da rosca na mesa | face da ranhura na mesa, bolso pra cima |
| Brim / aba | ____ | ____ |
| Suporte | só na cavidade (enforcer), bloqueado na rosca | sem |

### Suporte da cavidade (só corpo)
- Distância vertical ao teto: ____ (0,3 mm)
- Camadas de interface: ____ (2 a 3)
- Densidade: ____ (10-15%)
- Retirada pela boca da rosca, depois de esfriar. Resultado: teto cedeu? ____ marca? ____ saiu inteiro? ____

## 3. Tempo e filamento por peça
| Peça | Tempo de impressão | Filamento (g) | Filamento (m) | Custo de material (R$) |
|---|---|---|---|---|
| Corpo | ____ h ____ min | ____ | ____ | ____ |
| Tampa | ____ h ____ min | ____ | ____ | ____ |
| Suporte (incluso acima?) | ____ | ____ | ____ | ____ |
| **Total** | ____ | ____ (meta ~165) | ____ | ____ |

- Real vs estimado: ____ (estimativa pré-impressão: ~165 g corpo + tampa)
- Taxa de falha observada: ____ de ____ impressões
- Custo de energia (opcional): ____
- Preço de venda: NÃO definido aqui (decisão humana).

## 4. Pós-processamento e montagem
1. Esfriar na mesa, soltar a peça: ____
2. Remover suporte pela boca da rosca: ____
3. Remover fios (stringing) e rebarbas, sobretudo na rosca: ____
4. Lixar teto da cavidade se áspero (fica escondido): ____
5. Testar a rosca: entra sem forçar, gira fluido, sem folga visível: ____
6. Limpeza final (pano seco, sem solvente): ____

## 5. Checklist de qualidade (por unidade)
Unidade/lote nº ____ Data ____ Responsável ____
- [ ] Sem empenamento: base plana na mesa
- [ ] Sem delaminação nas paredes e nas caneluras
- [ ] Caneluras limpas, sem fios nem gotas
- [ ] Acabamento externo uniforme, cor igual entre corpo e tampa
- [ ] Rosca limpa: crista inteira, sem rebarba
- [ ] Rosca fecha e abre suave (folga ____ mm), sem prender, sem balançar
- [ ] Tampa fecha por completo e alinha com o corpo
- [ ] Cavidade interna: sem restos de suporte
- [ ] Dimensões conferidas: 80 x 150 mm (tolerância ± ____)
- [ ] Peso dentro de ± ____ g do padrão
- [ ] Estabilidade: peça em pé sem tombar vazia e com lápis
- [ ] Sem cheiro forte nem resíduos
- [ ] Teste de uso: ____ lápis cabem e saem sem prender
- [ ] Nada na aparência denuncia o que há dentro (olhar de fora, de perto, com a peça fechada)
- [ ] Aprovada / Reprovada (motivo: ____)

Reprovada: registrar causa e peça de reposição. Não entra no estoque.

## 6. Embalagem sugerida (discreta)
- Caixa de papelão kraft lisa, sem logotipo grande e sem foto do produto.
- Papel de seda ou papel kraft amassado como proteção. Evitar plástico bolha solto na vista.
- Selo/etiqueta única e pequena, só com o nome "Faixa Preta" (faixa preta simples). Sem texto explicativo sobre o interior.
- Cartão curto dentro, no tom da marca. Sugere, não entrega. Texto final a cargo do agent de Marketing/Copy e aprovação humana.
- Nada na caixa, no cartão ou na etiqueta descreve como a peça funciona. Instruções de uso, se houver, só no essencial (limpar, não lavar em água quente: PETG amolece).
- Dimensões da caixa: ____ x ____ x ____ mm. Peso embalado: ____ g. Custo da embalagem: R$ ____.
- Frete e transportadora: NÃO definidos (decisão humana).

## 7. Registro e rastreio
- Histórico das versões usadas no lote: ____
- Fotos da peça final guardadas em: ____ (interno, sem expor o segredo)
- Ocorrências e ajustes pro próximo lote: ____

## 8. Escalar pro humano
- Falta alguma aprovação ou teste no histórico.
- Folga da rosca fora do esperado ou peça reprovada sem causa clara.
- Qualquer gasto, compra de filamento/embalagem ou venda: só com aprovação humana.
