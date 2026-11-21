# Plano de teste de tráfego pago (Meta e TikTok)

> RASCUNHO. Nada criado, ativado ou gasto. Agent Tráfego Pago, 2026-11-20. Qualquer campanha, orçamento ou peça passa pelo João.
> Legenda: **FATO** = vem do repo. **CHUTE** = número inventado pra planejar, sem medição. Preço e custos vêm de `loja/simulacao-preco-frete.md` e são SIMULAÇÃO (custos já são chute lá).

## 0. Portão: não ligar nada antes disso
1. Peça física impressa e filmada de verdade. Os renders (`revisao.md`) não saem em anúncio.
2. Loja Shopify auditada e configurada (hoje "toda desconfigurada", segundo o João), com pixel/API de conversões do Meta e do TikTok instalados e testados.
3. Preço, frete, prazos, gateway e regime tributário fechados pelo João (hoje tudo simulado).
4. Questão jurídica da venda no Brasil resolvida (pendência em `docs/CONTEXTO.md`).
5. Revisão de marca em cada peça.

Sem os 5, este plano fica na gaveta. É planejamento, não ordem de subir.

## 1. CAC máximo (conta)
Base (FATO da simulação): preço R$ 89,90, custo estimado R$ 38,70, taxa R$ 4,00, imposto R$ 5,39. **Sobra por pedido: R$ 41,81 (~46%), sem frete.** Frete é pago pelo cliente e fica fora da conta.

| Conceito | Valor | Status |
|---|---|---|
| CAC de empate (lucro zero no 1º pedido) | **R$ 41,81** | derivado da simulação; herda os chutes dela |
| ROAS de empate | 89,90 / 41,81 = **2,15** | derivado |
| **CAC máximo de teste (teto de pausa)** | **R$ 42** | = empate, arredondado. No teste aceito empatar pra aprender, não perder |
| **CAC alvo pra escalar** | **R$ 25** (ROAS ~3,6) | CHUTE: deixa ~R$ 17 por pedido (~40% da sobra) pra imprevisto e lucro |
| Recompra / indicação | 0 | Não conta. Não há dado. Produto de compra única até provar o contrário |

Ressalvas que mexem no teto:
- Se o frete real for maior que o cobrado, ou se houver frete grátis, a sobra cai e o teto cai junto. Frete grátis em Norte/Nordeste (R$ 34 a R$ 42) comeria quase tudo: **não oferecer frete grátis no teste**.
- Troca, devolução e reembolso não estão na conta (política não definida). CHUTE: reservar 5% (R$ 4,50) e usar teto efetivo de **R$ 37** até medir.
- Se o custo real medido (peso, horas) mudar, recalcular tudo. Fórmula: CAC máx = preço - custo - taxa - imposto.

## 2. Verba
Sem verba definida. Regra proposta em vez de valor fixo: **a verba é um múltiplo do CAC máximo.**
- Cada variação de anúncio (criativo) precisa de ~**2,5x o CAC máx** de gasto antes de ser julgada = ~R$ 105. CHUTE.
- Teste mínimo: 2 plataformas x 3 criativos x R$ 105 = ~R$ 630 de aprendizado. Um teste só no Meta: 3 x R$ 105 = **~R$ 315**.
- Verba diária de cada campanha: R$ 15 a R$ 25 (CHUTE; abaixo disso a plataforma mal sai da fase de aprendizado).
- Teto total do teste e duração: **decisão do João** (ver fim).

Aviso honesto: com ticket de R$ 89,90 e público frio, é plausível o CAC real ficar acima de R$ 42 (CHUTE; sem benchmark validado). O teste serve pra descobrir isso barato. Não prometer retorno.

## 3. Estrutura de campanha

### Meta (Instagram + Facebook)
- **Fase 1, criativo (R$ 15/dia, 5 a 7 dias).** 1 campanha Vendas (conversão: compra), 1 conjunto com público amplo, 3 anúncios (criativos A, B, C). Posicionamentos automáticos, depois ver Reels e Feed.
- **Fase 2, público.** Só com sinal do criativo vencedor: 1 conjunto amplo, 1 conjunto de interesses, 1 de remarketing.
- Otimizar pra compra. Se faltarem eventos, cair pra Adicionar ao carrinho nas primeiras semanas (CHUTE: sem ~50 compras/semana o algoritmo aprende mal; é limitação conhecida de ticket baixo e verba baixa).

### TikTok
- 1 campanha de conversão (compra via pixel do site), 1 grupo de anúncios, 3 vídeos nativos 9:16. Sem Smart+ no começo: queremos ler qual criativo ganha, e Smart+ embaralha isso.
- Vídeo com cara de conteúdo orgânico (o roteiro v2 de `revisao.md` serve de base). Som e legenda obrigatórios.
- Orçamento mínimo da plataforma costuma ser maior que o do Meta (CHUTE, conferir no gerenciador na hora). Se o mínimo estourar o teto do teste, começa só pelo Meta.

### Convenção de nome (pra leitura de dados)
`FP_[plataforma]_[objetivo]_[público]_[criativo]_[data]`. Ex.: `FP_META_CONV_AMPLO_A_2611`.

## 4. Públicos
Tudo sem dado de cliente. Público que use lista de clientes exige aprovação do João e autorização (regra do CLAUDE.md).

| Público | Plataforma | Uso | Obs |
|---|---|---|---|
| Amplo, Brasil, 25 a 54 | Meta, TikTok | Fase 1 | Deixa a plataforma achar. Melhor ponto de partida pra leitura de criativo |
| Interesses: organização de mesa, home office, papelaria, design de objetos, impressão 3D, "gadgets" | Meta, TikTok | Fase 2 | Pequeno e específico. Atenção a sobreposição entre conjuntos |
| Presente: pessoas que presenteiam colegas (sazonal: amigo secreto, fim de ano) | Meta | Fase 2 | Tese: porta-lápis discreto presenteia bem. Hipótese, não FATO |
| Remarketing: visitou produto, adicionou ao carrinho (30 dias) | Meta, TikTok | Fase 2 | Pixel próprio, sem lista de cliente. Verba pequena (~20% do total) |
| Lookalike | Meta | **Só depois de ~100 compras** | Sem base, não existe. Não usar agora |

Excluir: compradores recentes (pelo pixel) do prospecting.

## 5. Criativos necessários (precisam da peça real)
Mínimo pro teste: **3 criativos por plataforma, 1 mensagem cada**. Tudo depois de peça física filmada. Tom: discreto, cúmplice, sem entregar.

| ID | Formato | Ideia | Nota |
|---|---|---|---|
| A | Vídeo 9:16, 15 a 18 s | Rotina de mesa (roteiro v2 de `revisao.md`: "segunda, 7h40", fecha em "faixa preta") | Nenhum plano mostra base, fundo ou giro |
| B | Vídeo 9:16, ~10 s | Detalhe do objeto: material, estrias, preto fosco, impressão 3D, o peso na mão | Só fato. Mostra qualidade e deixa a curiosidade pro olhar atento |
| C | Imagem estática 4:5 + 1:1 | Foto limpa de fundo neutro, uma linha de texto ("Só um porta-lápis. Você acha.") | Controle barato pra comparar contra vídeo |
| D (opcional) | Carrossel 4:5, 3 cards | Objeto, contexto, preço/prazo | Só se C ganhar; nunca misturar render e peça real |

Regras:
- Peça real, nunca render como "foto do produto".
- Sem rosto sem aprovação do João. Sem depoimento, avaliação ou número inventado. Só entra prova social quando existir de verdade.
- Texto de venda mostra o que é: porta-lápis, PETG, impresso em 3D, preto fosco, prazo. O mistério fica no tom ("faixa preta"), não numa promessa.
- Landing: página de produto da loja (cuidar da mesma regra de vocabulário na página).

## 6. Política de vocabulário (anúncio reprova com "compartimento oculto")
Duas razões pra evitar: (1) regra da marca, nunca entregar o segredo; (2) risco de reprovação ou conta restrita (Meta e TikTok olham itens de "ocultar", "esconder", "compartimento", e o assunto de objeto que guarda coisa pode puxar revisão de política de armas, drogas ou "bens ocultos". CHUTE sobre o gatilho exato; conferir nas políticas vigentes na hora de subir).

**Proibido em anúncio, copy da página, nome do produto, legenda, hashtag, nome de arquivo e nome de campanha:**
esconder, escondido, oculto, compartimento, secreto, segredo, fundo falso, falso fundo, "tem algo dentro", "adivinha o que tem dentro", stash, cofre disfarçado, discreto pra guardar (algo), "ninguém vai saber", "ninguém desconfia".

**Também evitar** (sinal de risco, não só de marca): menção a esconder dinheiro, joias, documentos, chaves, remédios, ou "proteger" contra visita, filho, colega. Nada de cena de alguém guardando algo fora de vista.

**Pode:** "porta-lápis", "organizador", "impresso em 3D", "PETG", "preto fosco", "caneluras", "acabamento limpo", "feito sob demanda", "faixa preta", o lema só em formato discreto (minúsculo, sem caixa alta, último plano).

Exemplos:
| Em vez de | Usar |
|---|---|
| "O porta-lápis com compartimento secreto" | "Só um porta-lápis. Você acha." |
| "Esconde o que você quiser" | "Preto fosco, estrias finas, impresso em 3D." |
| Cena virando a base da peça | Cena de rotina (tampa, lápis, caderno) |

Processo:
1. Antes de subir, checar cada peça com o agent de Marketing/Copy e a lista acima.
2. Se uma peça for reprovada, **não** reenviar variando a palavra pra "enganar" o revisor (risco de banir a conta). Trocar a mensagem e avisar o João.
3. Se reprovar por política, registrar motivo em `marketing-teste/` e escalar. Não abrir conta nova pra contornar.
4. Não usar a palavra proibida nem em comentário respondido, nome de pasta pública ou DM de atendimento a partir do anúncio.

## 7. Métricas e critérios de pausa e escala
Ordem de importância: compra e CAC > custo por carrinho > CTR e custo por clique.

### Métricas
| Métrica | Referência de leitura | Status |
|---|---|---|
| CAC (gasto / compras) | teto R$ 42, alvo R$ 25 | derivado, seção 1 |
| ROAS (receita sem frete / gasto) | empate 2,15, alvo ~3,6 | derivado |
| CTR (link) | ruim abaixo de ~0,8%; bom acima de ~1,5% | CHUTE |
| CPC (link) | observar; sinal só junto de CVR | sem referência firme |
| Taxa de conversão do site (clique → compra) | observar; abaixo de ~0,5% aponta problema de página, não de anúncio | CHUTE |
| Hook rate vídeo (3s / impressões) | bom acima de ~25% | CHUTE |
| Frequência | atenção acima de ~2,5 na semana | CHUTE |
| Carrinho abandonado, início de checkout | diagnóstico de página/frete | sem meta |

### Pausar (precisa de aprovação do João pra agir)
- Anúncio com gasto >= **R$ 105** (2,5x CAC máx) e **zero compra**: pausar.
- Anúncio com gasto >= R$ 105, compras >= 1 e **CAC > R$ 42**: pausar, ou manter só se houver carrinho forte (diagnóstico de página).
- Campanha com gasto total >= R$ 210 e zero compra: pausa geral e revisão de página, preço e frete antes de mexer em criativo.
- Qualquer reprovação por política, aviso de conta, ou comentário que exponha o segredo: pausa imediata e escalar.
- CTR < 0,5% depois de ~R$ 50 gastos: trocar criativo, não esperar.

### Manter e observar
- CAC entre R$ 25 e R$ 42, 3 ou mais compras: manter, trocar um criativo por vez, esperar mais 3 a 5 dias.

### Escalar
- CAC <= R$ 25 por **3 dias seguidos e >= 5 compras no total**: subir verba em passos de **até +20% a cada 2 a 3 dias** (CHUTE; subir mais reinicia o aprendizado).
- Depois de 10 compras com CAC dentro do alvo: abrir conjunto novo (interesse, presente, remarketing) em vez de só empilhar verba.
- Nunca escalar antes de checar capacidade: produção é 5 dias úteis por peça, em impressora própria. Vender além da fila quebra o prazo prometido.
- Lookalike só depois de ~100 compras.

### Cadência
Leitura diária nos 3 primeiros dias (só pra ver anomalia), depois a cada 2 dias. Relatório semanal com `marketing:performance-report`. Decisão de pausa/escala sempre registrada e aprovada.

Observação: com poucas compras, os números são ruído. Se o teste terminar com 0 a 2 compras, a conclusão é "sem evidência", não "o produto não vende".

## 8. Riscos
- Pixel mal instalado: sem compra registrada, a otimização cega e o CAC não é calculável. Testar eventos antes de gastar.
- Prazo longo (produção 5 dias + entrega 3 a 15 dias úteis) pesa na conversão e aumenta pedido de reembolso. Deixar o prazo claro no anúncio e na página.
- Sazonalidade: fim de ano pode barateá-lo ou encarecê-lo (leilão mais caro em nov/dez; CHUTE). Ter isso em mente no calendário do teste.
- Conta nova, sem histórico, com produto "diferente": revisão de política mais rígida. Preparar a página e as peças limpas.
- Dados de cliente: nada vai pra ferramenta externa sem autorização.

## 9. Passos (quando o portão da seção 0 abrir)
1. João define teto e duração do teste.
2. Revisão de marca e de vocabulário dos 3 criativos.
3. Agent monta as campanhas como rascunho e o João aprova antes de qualquer ativação.
4. Rodar fase 1 (criativo), ler, decidir pausa/escala.
5. Relatório e reunião de decisão: segue, muda ou encerra.
