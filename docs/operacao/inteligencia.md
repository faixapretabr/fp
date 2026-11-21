# Inteligência e Pesquisa: arquitetura operacional (PROPOSTA)

> PROPOSTA do departamento. Não é política aprovada; só o João aprova (itens C). Tudo local: sem commit, sem publicar, sem gastar, sem registrar nada. `02-segredo.md` não foi aberto; nada aqui descreve o mecanismo do produto.
> Rótulos: **FATO** (fonte oficial lida, com link e data) | **ESTIMATIVA** (cálculo ou inferência com base declarada) | **CHUTE** (sem medição) | **NÃO VERIFICADO** (sem prova ou teste).
> Limite do método: WebFetch resume a página com um modelo pequeno. Os trechos entre aspas são os que a ferramenta devolveu como literais; reconferir na tela antes de decidir.

## Revisão 2026-11-20

**O que estava errado na versão anterior (autocrítica):**
1. Várias linhas da seção 9 afirmavam "o que a doc diz" a partir de resumo de busca, sem trecho e sem ter aberto a página oficial (Meta, TikTok, Search Console, INPI, IBGE). Violava a regra de verificação do `agents/_contexto-base.md`.
2. Rich Results Test, "busca do INPI é gratuita" e "TikTok: atraso de 11 h/48 h" foram escritos como se fossem fato. Eram terceiros ou memória.
3. `.shop`: o RDAP agregador deu 403 e eu escrevi "NÃO reproduzido" sem tentar o servidor RDAP oficial do TLD. Era possível e agora foi feito.
4. Citei "itens 35 e 110" de `docs/auditoria.md`; eram números de linha.
5. Regras de amostra e validade (seção 5) estavam sem etiqueta clara de que são critérios do departamento, não norma.
6. Não usei os fatos novos de `t13-*.md` (plataformas, custos, fiscal).
7. Texto repetido (resumo, decisões e mesma lista de riscos em duas seções).

**O que mudou:**
- Seção 9 refeita: cada linha traz link, data, trecho devolvido e o que NÃO foi lido. Fontes que falharam estão listadas, com a alternativa tentada.
- `faixapreta.shop` agora reproduzido pelo RDAP oficial do TLD (FATO, seção 3.2).
- Incorporados os fatos de `t13-custos.md`, `t13-fiscal-taxas.md` e `t13-plataformas.md` (seções 2, 3, 4 e 8).
- Enxugado: um único resumo no fim, no máximo 2 decisões.
- Contradições com outros departamentos listadas na seção 8.3 (não editei nada deles).

## 1. Contexto operacional e quem depende de nós

Entregamos fato, estimativa ou chute, sempre rotulado, com fonte e data. Não decidimos, não publicamos, não gastamos.

**Estado (FATO, lido nos arquivos em 2026-11-20):** nada impresso; loja Shopify `faixapretabr.myshopify.com` com 1 produto em DRAFT (`docs/operacao/ecommerce.md`); `pesquisa/concorrentes.md` declara "busca web rasa" e "inferido"; `loja/simulacao-preco-frete.md` é simulação em cima de chute; `loja/seo-produto.md` admite "sem volume de busca".

| Consumidor | Usa de nós | Se o dado vier ruim |
|---|---|---|
| João | preço, frete, plataforma, domínio, marca, 2º produto | decide dinheiro com chute |
| Loja e Atendimento | custo, preço, prazos, taxas | publica prazo/preço sem lastro |
| Anúncios/Tráfego | margem, CAC máximo, teto | queima verba em margem inventada |
| Marketing e SEO | tendência, termos, concorrentes | copy em cima de inferência |
| Produto | demanda, preço-alvo | modela nicho não provado |
| Jurídico e Qualidade | levantamento de marca/domínio | falso "livre" vira prejuízo |
| Finanças/Produção | premissas de custo | planilha nasce em chute |

## 2. Riscos específicos

Probabilidade e impacto são ESTIMATIVA (julgamento do departamento, sem medição).

| # | Risco | Caso real | P | I | Controle |
|---|---|---|---|---|---|
| R1 | Fonte desatualizada | Preços de `concorrentes.md` ("podem estar desatualizados"); fonte de 2021 usada para dizer que a Shopify não tem NF-e nativa (`t13-fiscal-taxas.md`, post de 31/08/2021) | A | M | Validade por tipo de dado (5.3) |
| R2 | Informação sem comprovação | "Tom: inferido" nas 5 referências; "poucos vendem 'comum com algo mais'" sem lista; "Placar 6 a 0 Shopify" (`CONSOLIDADO.md`) vindo de opinião, não de doc oficial; o T13 depois mostrou vantagem da Nuvemshop em Pix, NF-e e custo | A | A | Voto sem fato não conta (`_contexto-base.md`) |
| R3 | Interpretação equivocada | Pontuação 1 a 5 do 2º produto é "julgamento do agent" e vira "Recomendação: vaso"; Shopify Basic "US$ 19" de terceiro x US$ 39 oficial (`t13-custos.md`) | M | A | Julgamento não vira ranking sem a nota "sem dado de demanda" |
| R4 | Dados conflitantes | Preço do objeto 3D: R$ 19,90 a 29,90 (item 2), "R$ 20 a 50" (Padrões), R$ 25,71 a 58,48 (Next 3D); Basic anual US$ 29 vs. US$ 19 em terceiros | A | M | Regras de conflito (4.3) |
| R5 | Amostra insuficiente | 4 lojas, 1 anúncio cada; Flip Dock = 1 campanha, 136 apoiadores | A | A | Piso de amostra (5.2) |
| R6 | Premissa de custo em chute tratada como fato | R$ 89,90 e "margem ~46%" saem de 110 g, 9 h, R$ 2/h, 6%, 10% de perda; câmbio R$ 5,50 e mix 50/50 de `t13-custos.md` também são chute | A | A | Herda o pior rótulo; sensibilidade obrigatória (3.3) |
| R7 | Falso "livre" (domínio, marca, handle) | RDAP "sem registro" lido como "livre"; INPI não consultado; Instagram/YouTube não confirmados | M | A | Só chamar de livre com consulta oficial na data (5.3) |
| R8 | Dado de cliente em ferramenta externa | ShopifyQL com nome/e-mail exige acesso nível 2 a dados protegidos | B | A | Proibido sem autorização do João |
| R9 | Vazamento do segredo em pesquisa | termos de busca ou relatório descrevendo o mecanismo | B | A | Pesquisa não usa nem descreve o mecanismo |
| R10 | Ferramenta tida como capaz sem prova | "Indexing API serve para produto" (não serve, 9 abaixo); conector Shopify de analytics não testado | M | M | Capacidade só com doc lida ou teste (seção 9) |

(A = alta, M = média, B = baixa.)

## 3. Biblioteca DO / DON'T

Casos reais citam o arquivo. Exemplos escritos por mim levam **(EXEMPLO SIMULADO)**.

### 3.1 Concorrentes rasos e com inferência (`pesquisa/concorrentes.md`)
| | Exemplo |
|---|---|
| INCORRETO (real) | "Ninguém vende curiosidade ou cumplicidade" e "Gap: poucos vendem 'comum com algo mais'", apoiados em 4 páginas e na linha "Tom: inferido" |
| CORRETO (EXEMPLO SIMULADO) | "ESTIMATIVA: em 5 páginas lidas, nenhuma usa esse posicionamento; amostra pequena, Shopee e Instagram não cobertos. NÃO VERIFICADO como lacuna de mercado." |
| INCORRETO (real) | Flip Dock listado como "faz bem" com "1.006% da meta" |
| CORRETO (EXEMPLO SIMULADO) | "FATO (Kicktraq): 136 apoiadores, ticket médio US$ 74. Não mostra demanda no Brasil nem recompra; n = 1 campanha." |

Regra: "não achei" nunca vira "não existe". A lacuna "nenhuma pesquisa de preço ao vivo" do próprio arquivo deve ficar no topo e travar conclusões.

### 3.2 `faixapreta.shop` com dono desconhecido (`pesquisa/dominio-perfis.md`)
- FATO reproduzido hoje (RDAP do registry do TLD, https://rdap.gmoregistry.net/rdap/domain/faixapreta.shop, 2026-11-20): registration 2026-11-14T07:38:38Z, expiration 2027-11-14T23:59:59Z, status "client transfer prohibited", nameservers `orbit.dns-parking.com` e `horizon.dns-parking.com`. Dados do titular omitidos pela ferramenta.
- ESTIMATIVA: nameservers de "parking" indicam domínio estacionado (indício, não prova de dono).
- NÃO VERIFICADO: quem é o titular. Só o João, no painel do registrador, confirma.
- CORRETO (EXEMPLO SIMULADO): "Domínio registrado há 6 dias, titular não confirmado; não citar em nada público. Decisão do João."
- INCORRETO: "Se o .shop for do João, usar faixapreta.shop" virar escolha de SEO ou deixar o domínio no JSON-LD. `seo-produto.md` já usa `[DOMINIO A DEFINIR]`; manter.
- Contra-exemplo de "livre": `faixapreta.com.br` NÃO está livre. RDAP oficial (https://rdap.registro.br/domain/faixapreta.com.br, 2026-11-20): status active, registro 2000-01-28, expiração 2029-01-28. Já `faixapretabr.com.br` deu 404 no RDAP do registro.br em 2026-11-20: indício de "sem registro", não reserva; confirmar no registro.br antes de agir.

### 3.3 Chutes de 110 g, 9 h, R$ 2/h, 6% (`loja/simulacao-preco-frete.md`)
Conta refeita: 110 g x R$ 120/kg = R$ 13,20; 9 h x R$ 2 = R$ 18,00; embalagem R$ 4,00; perda 10% (~R$ 3,52); custo R$ 38,70; taxa 4% + R$ 0,40 = R$ 4,00; imposto 6% = R$ 5,39; sobra R$ 41,81. A aritmética fecha; as entradas são CHUTE.

| Cenário (ESTIMATIVA, só sensibilidade) | Máquina | Custo | Margem |
|---|---|---|---|
| Arquivo: 9 h x R$ 2 | R$ 18,00 | R$ 38,70 | R$ 41,81 (~46%) |
| 14 h x R$ 3 | R$ 42,00 | ~R$ 65,12 | ~R$ 15,39 (~17%) |

- CORRETO: "Margem simulada vai de ~17% a ~46%; ambas CHUTE. Não usar como base de verba."
- INCORRETO: repetir "margem ~46%" em anúncio, SEO ou CAC sem a palavra SIMULAÇÃO.
- Novo (`t13-custos.md`, SIMULAÇÃO): a taxa de 4% + R$ 0,40 do arquivo era chute de gateway. Hoje há taxa oficial do Nuvem Pago (Pix 0,99%; cartão à vista 4,19% a 4,69% + R$ 0,35 conforme o plano, recebimento em 30 dias), mas o gateway da Faixa Preta não foi decidido; continua sendo premissa.
- Gatilho para virar FATO: peso na balança, tempo do fatiador e do relógio, recibo do filamento, em 3 impressões (T-CUSTO-1).

### 3.4 "Porta-lápis" x "porta-canetas duplo"
Origem real (`docs/auditoria.md`, linhas 35 e 110): o repo só tem "porta-lápis"; "porta-canetas duplo" aparece no Drive e não foi conferido.
- CORRETO (EXEMPLO SIMULADO): "NÃO VERIFICADO: nome no Drive. Repo, loja e Shopify: 'porta-lápis'. Volume de busca de 'porta-lápis' e 'porta-caneta' NÃO MEDIDO. Não otimizar página para termo que pode mudar."
- INCORRETO: escolher o termo de SEO por palpite de volume, ou tratar "porta-canetas duplo" como outro produto sem confirmar.

### 3.5 Regras rápidas
| Situação | Correto | Incorreto |
|---|---|---|
| Volume de busca | "NÃO MEDIDO" até o Search Console ter dados | "tem alto volume" |
| Preço de concorrente | valor, link, data, vendedor, n | "preço médio R$ 25" sem n |
| Tendência | termo, série, data | "está em alta" |
| Imposto | "regime não definido; 6% CHUTE" | "imposto 6%" |
| Marca | "busca feita em [data], sem certidão" | "marca livre" |
| Dado de cliente | não sai do repo | colar pedidos em ferramenta externa |

## 4. Hierarquia de fontes

### 4.1 Níveis (PROPOSTA)
| Nível | Tipo | Exemplos | Sustenta |
|---|---|---|---|
| N1 oficial primário | quem produz a regra ou o dado | docs do Google, Shopify, Meta, Nuvemshop; RDAP do registro; INPI; IBGE; tabela de taxas do gateway; medição real | FATO |
| N2 dado próprio | exportação nossa com data | painel da loja, extrato, recibo, balança | FATO |
| N3 secundário | cita o primário | Agência IBGE, blogs de fabricante, ferramenta de SEO, Kicktraq, páginas de marketplace, espelhos de OpenAPI | ESTIMATIVA, cruzar com N1 |
| N4 fraco | sem autoria ou data | fórum, "dizem", blog isolado, resumo sem link | só pista |
| N5 inaceitável | proibido como base | número inventado; screenshot sem URL e data; ferramenta não testada; dado de cliente de fora do repo; fonte que exige burlar login ou termos | descartar |

### 4.2 Por tipo de afirmação
- Regra, lei, política, prazo de API, taxa de plataforma: só N1, na data.
- Preço de concorrente, volume, tendência: N1 da plataforma ou N3 com data; sempre ESTIMATIVA.
- Custo do nosso produto: só N2. Antes disso, CHUTE.
- Domínio, marca, handle: só N1 (registro, INPI, rede logada). Antes disso, NÃO VERIFICADO.

### 4.3 Dados conflitantes (PROPOSTA)
1. Não fazer média; listar lado a lado com fonte, data e nível.
2. Vence o maior nível; empate, o mais recente; ainda empate, mostrar faixa e dizer que há conflito.
3. Fonte nossa x N1: N1 vence até prova em contrário.
4. Conflito que muda decisão do João sobe em `docs/decisoes.md` com as duas versões, sem escolher por ele.
5. Registrar: "CONFLITO: A (fonte, data) x B (fonte, data). Tratado como: ... Motivo: ...".
6. Conflito aberto bloqueia o número em Anúncios e Loja.

Caso aplicado (real, `t13-custos.md`): "CONFLITO: Shopify Basic US$ 19 (terceiros) x US$ 39 mensal / US$ 29 anual (https://www.shopify.com/br/precos, 2026-11-20). Tratado como: oficial vence; US$ 19 não se confirma." Caso aberto (real): `t13-plataformas.md` diz que o Brasil não está na lista do Shopify Payments, enquanto `t13-custos.md` registra "Cartão Shopify Payments 2,9% + 30¢ (Basic)" na página de preços. NÃO RESOLVIDO; ver 8.3.

## 5. Critérios de validação e rótulos

### 5.1 Rótulos obrigatórios
| Rótulo | Quando | Exige |
|---|---|---|
| FATO | N1/N2 visto na data | link ou arquivo, data, trecho |
| ESTIMATIVA | cálculo ou inferência | base declarada, faixa, n |
| CHUTE | sem medição | aviso; trocar no primeiro dado real; nunca em material público |
| NÃO VERIFICADO | sem prova ou teste | o que falta e quem faz |

Regras: sem rótulo o número não sai do departamento; derivado herda o pior rótulo dos insumos; "inferido" solto vira ESTIMATIVA com base ou NÃO VERIFICADO.

### 5.2 Amostra mínima (critérios do departamento, ESTIMATIVA de bolso, não norma estatística)
| Conclusão | Mínimo para afirmar | Abaixo disso |
|---|---|---|
| Faixa de preço de concorrente | 10 anúncios, 3 vendedores, 2 canais | "indício", escrever n |
| Posicionamento da concorrência | 8 marcas com texto citado | NÃO VERIFICADO |
| Volume de busca | Search Console com 90 dias e 100+ impressões por consulta | "NÃO MEDIDO" |
| Custo real | 3 impressões do mesmo item; média e pior caso | CHUTE |
| Taxa de falha | 20 impressões | "observado em n" |
| Conversão/CAC | 30 conversões por variação ou 2 semanas | "ruído": sem regra de pausa/escala |
| Avaliação de cliente | só real e com origem | proibido inventar |

### 5.3 Validade da fonte (PROPOSTA)
| Tipo | Validade |
|---|---|
| Preço de concorrente, frete, taxa de gateway | 30 dias |
| Regra de plataforma e API | 90 dias ou na primeira falha |
| Domínio, handle, marca | 7 dias antes de agir |
| Volume/Trends | 90 dias |
| Custo medido | até mudar material, bico ou fornecedor |
| Jurídico | só o parecer do advogado vale |

## 6. Bloqueio e escalonamento

**Bloqueio automático** quando: número sem rótulo, ou CHUTE indo para material público, preço, política ou JSON-LD; conflito aberto que muda decisão; ação exigiria dado de cliente ou conta externa sem autorização; fonte exige burlar login/termos; pesquisa tocaria o mecanismo; ferramenta não testada seria base de decisão.

| Gravidade | Exemplo | Para quem | Prazo |
|---|---|---|---|
| Informativo | fonte antiga | dono do arquivo | mesma rodada |
| Atenção | CHUTE entrando em material de Anúncios | Cláudio + Qualidade | antes de publicar |
| Decisão | domínio, marca, plataforma, preço | João em `docs/decisoes.md` (máx. 3 por ciclo, com recomendação) | próximo ciclo |
| Jurídico | marca parecida (`faixapreta3d.com.br`) | Jurídico e João | imediato |

Ausência de resposta NÃO é aprovação: o item fica parado e visível; ninguém decide pelo João.

## 7. Matriz de autonomia (PROPOSTA; vale após o "grava" do João)
| Atividade | Nível |
|---|---|
| Ler repo e fontes públicas sem login | A |
| Escrever arquivo novo em `pesquisa/` ou `docs/operacao/` | A |
| Rotular, apontar conflito, pedir revisão de premissa | A |
| Radar mensal de mercado (leitura) | B |
| Atualizar arquivo existente do departamento (diff curto) | B; vários arquivos existentes: C |
| Corrigir arquivo de outro departamento | C (propõe diff ao dono) |
| Painel logado (Search Console, Shopify, Ads) | C na 1ª vez; depois B, só leitura |
| Cadastrar ferramenta, token, webhook; comprar dado; assinar | C |
| Registrar domínio, handle ou marca | C |
| Enviar dado de cliente a ferramenta externa | C (regra do `CLAUDE.md`) |
| Publicar relatório fora do repo | C |
| Preço, verba, produto, plataforma | C (só o João) |

## 8. Fiscalização cruzada

### 8.1 Quem confere o quê
Executor não confere o próprio trabalho (`_contexto-base.md`).

| Quem usa | Premissa | Conferente | O que confere |
|---|---|---|---|
| Anúncios | margem, CAC máximo, conversão | Inteligência (+ Finanças) | rótulo; presença de CHUTE; amostra (5.2) |
| Loja | preço, frete, prazo, taxa, imposto | Inteligência + Produção | origem e rótulo; "SIMULAÇÃO" no arquivo |
| Marketing/Conteúdo | tendência, concorrentes, "ninguém faz" | Inteligência; Qualidade confere marca | FATO com data; sem universal não provado |
| SEO | volumes, termos | Inteligência; Qualidade (termos proibidos) | termo medido ou NÃO MEDIDO |
| Produto | demanda, preço-alvo | Inteligência | dado de venda ou só inferência |
| Inteligência | o que produzimos | Qualidade e Documentação | rótulo, fonte, data, sem segredo |

Checklist de 5 itens: rótulo; fonte e data na validade; amostra no piso; conflitos listados; nada descreve o mecanismo. Falhou: devolve ao dono com a lacuna. Todo FATO precisa de link ou arquivo reproduzível; Qualidade amostra 20% por ciclo (PROPOSTA).

### 8.2 Premissas do T13 que a Inteligência marca (não são decisão de plataforma)
| Premissa | Origem | Rótulo |
|---|---|---|
| Ticket R$ 89,90 | simulação | CHUTE |
| Mix 50% Pix / 50% cartão | `t13-custos.md` | CHUTE |
| Câmbio R$ 5,50 por US$ | `t13-custos.md` | CHUTE (não consultado) |
| Volumes 10/50/200 por mês | `t13-custos.md` | CHUTE |
| Pagar.me sem tarifa fixa (assumido R$ 0) | `t13-custos.md` | CHUTE, favorece a Shopify na conta |
| Nuvem Pago: Pix 0,99%, boleto R$ 2,39, cartão à vista Começo 4,69% / Essencial 4,19% + R$ 0,35 | `t13-fiscal-taxas.md`, Central do Nuvem Pago, 2026-11-20 | FATO (reconferir na tela) |
| NF-e Nuvemshop: R$ 1,49 (Começo) / R$ 0,99 (Essencial) por nota; exige MEI ou Simples, IE e certificado A1 | `t13-fiscal-taxas.md` | FATO com divergência interna: o simulador diz "5 primeiras notas ou declarações são grátis" sem "primeiro mês" |
| Custo do certificado A1 | `t13-fiscal-taxas.md` | NÃO VERIFICADO |
| Parcelado sem juros e antecipação (Começo/Essencial) | idem | NÃO VERIFICADO (só suporte/painel) |
| NF-e na Shopify "não nativa" | post de staff de 31/08/2021 | FATO fraco (fonte antiga); página oficial atual NÃO achada |
| Totais de 12 meses (ex.: Shopify R$ 3.399 x Nuvemshop Começo R$ 506 com 10 vendas/mês) | `t13-custos.md` | ESTIMATIVA: herda os chutes acima; não usar como decisão |

### 8.3 Contradições com arquivos de outros departamentos (listadas, não editadas)
| # | Contradição | Onde | Para quem |
|---|---|---|---|
| C1 | Preço R$ 89,90 (Shopify, `ecommerce.md`) x R$ 0,00 (`loja/pendencias.md`) | Loja | Cláudio/Loja; FATO só da leitura de `ecommerce.md` |
| C2 | Garantia: política com "até 7 dias corridos" para defeito x CDC art. 26 (30/90 dias) e art. 49 (7 dias é arrependimento) | `loja/politicas-rascunho.md` x `docs/operacao/juridico.md` | Jurídico |
| C3 | Handle `porta-lapis` (Shopify) x `porta-lapis-preto-3d` (`loja/seo-produto.md`) | Loja x SEO | Cláudio |
| C4 | "tampa de rosca" em título, meta, alt, JSON-LD e "Fatos usados" de `loja/seo-produto.md`, e na descrição do rascunho Shopify | SEO/Loja x regra da marca | Qualidade e Cláudio |
| C5 | `seo-produto.md` pressupõe 80 x 150 mm sem confirmar se 80 é diâmetro ou largura | SEO | Produto |
| C6 | `CONSOLIDADO.md`: "Placar 1: 6 a 0 Shopify" x T13: vantagem da Nuvemshop em Pix, NF-e e custo; o próprio T13 diz que Shopify leva em tema, API e automação | Gestão | Cláudio |
| C7 | `t13-plataformas.md`: Shopify Payments indisponível no Brasil x `t13-custos.md`: "Cartão Shopify Payments 2,9% + 30¢ (Basic)" na página de preços | Gestão | Gestão |
| C8 | `t13-plataformas.md` (cartão Nuvem Pago "NÃO VERIFICADO por plano") x `t13-fiscal-taxas.md` (confirmado: 4,69% / 4,19% + R$ 0,35) | Gestão | Gestão atualizar |
| C9 | `dominio-perfis.md` dizia "aparenta livre" para `faixapretabr.com.br` apenas por RDAP sem registro | Pesquisa (nosso) | Inteligência: corrigir para "NÃO VERIFICADO" quando editarmos |

## 9. Inventário e FONTES OFICIAIS (consulta em 2026-11-20)

Tudo por WebFetch/WebSearch, só leitura, sem login. Nenhuma funcionalidade foi executada por nós; "trecho" é o que a ferramenta devolveu.

| # | Fonte | Link | Trecho / resultado | Não lido, limite ou incerteza |
|---|---|---|---|---|
| 1 | Google: conteúdo útil | https://developers.google.com/search/docs/fundamentals/creating-helpful-content | Resumo: E-E-A-T "não é fator de ranqueamento específico"; autoria fabricada é enganosa; sem promessa de posição | Resumo, sem trecho literal |
| 2 | Google: Merchant listing (Product) | https://developers.google.com/search/docs/appearance/structured-data/merchant-listing | Obrigatórios: `Product` `name`, `image`, `offers`; `Offer` `price` e `priceCurrency`; para merchant listings o preço precisa ser maior que zero. `review` e `aggregateRating` são "recomendadas", não obrigatórias | Últimos 4.759 caracteres não lidos. Implica que preço R$ 0,00 (C1) invalida o markup; confirmar na página |
| 3 | Google: Product (visão geral) | https://developers.google.com/search/docs/appearance/structured-data/product | Merchant listings x product snippets; queda de preço "não garantida" | Campos exatos estão nas subpáginas (item 2) |
| 4 | Search Console API `searchanalytics.query` | https://developers.google.com/webmaster-tools/v1/searchanalytics/query | `rowLimit` 1 a 25.000 (padrão 1.000); API retorna "the top ones"; `dataState` final/all/hourly_all; `brandedClassification` com dados desde 2026-02-21 | Retenção não consta na página |
| 5 | Ajuda do Search Console | https://support.google.com/webmasters/answer/7576553 e https://support.google.com/webmasters/answer/96568 | Padrão de 3 meses no relatório; dados recentes podem mudar; "not all queries beyond anonymized queries will be shown" | Tempo de retenção em meses NÃO achado nas duas páginas: NÃO VERIFICADO |
| 6 | Google Indexing API | https://developers.google.com/search/apis/indexing-api/v3/quickstart | Resumo: só para páginas de vaga (`JobPosting`) e transmissão ao vivo (`BroadcastEvent` em `VideoObject`); lote até 100 | Não serve para produto: descartada |
| 7 | RDAP `.shop` (registry) | https://rdap.gmoregistry.net/rdap/domain/faixapreta.shop (servidor indicado por https://data.iana.org/rdap/dns.json) | registration 2026-11-14T07:38:38Z; expiration 2027-11-14T23:59:59Z; "client transfer prohibited"; nameservers dns-parking | Titular omitido. `rdap.org` deu 403 (agregador); `rdap.registro.br/domain/faixapreta.shop` deu 404 (esperado, só atende `.br`) |
| 8 | RDAP `.br` (registro.br) | https://rdap.registro.br/domain/faixapreta.com.br e `.../faixapretabr.com.br` | `faixapreta.com.br`: active, registro 2000-01-28, expira 2029-01-28. `faixapretabr.com.br`: 404 | 404 é indício, não reserva. Página whois do registro.br veio vazia no fetch (não lida) |
| 9 | INPI: marcas | https://www.gov.br/inpi/pt-br/servicos/marcas | Página oficial: "Base de dados de marcas" e "Busca de processos" | Gratuidade e limites NÃO constam na página. Busca indicou, via Manual de Marcas (N3 até abrir): modalidade gratuita no portal e certidão por classe paga; o PDF oficial deu 503 hoje. Busca de colidência é análise de similaridade, exige jurídico |
| 10 | IBGE: Pesquisa Mensal de Comércio | https://www.ibge.gov.br/estatisticas/economicas/comercio/9075-pesquisa-mensal-de-comercio.html | Resultado de busca: série desde 1995, no SIDRA; caderno 09/2026 (13/11/2026) | Página não aberta por nós. API de agregados `servicodados.ibge.gov.br/api/docs` deu 403 em duas URLs. Mede varejo agregado, não objeto 3D |
| 11 | Shopify: ShopifyQL | https://shopify.dev/docs/api/shopifyql | Resumo: linguagem de consulta; usável no admin, na `shopifyqlQuery`, SDK Python e metric card; exige `FROM` e `SHOW`/`VISUALIZE` | Limites de linhas e taxa NÃO constam |
| 12 | Shopify: `shopifyqlQuery` | https://shopify.dev/docs/api/admin-graphql/latest/queries/shopifyqlQuery | Escopo `read_reports`; nome, endereço, telefone e e-mail exigem acesso nível 2 a dados protegidos de clientes | Plano e rate limit não citados. Não pedir dado de cliente |
| 13 | Shopify: limites da Admin API | https://shopify.dev/docs/api/usage/limits | Trecho: "Calculated query cost, by plan"; não menciona ShopifyQL | Valores estão em página de rate limits não aberta |
| 14 | Shopify Analytics via conector (`run-analytics-query`) | ferramenta local | Existe no ambiente | NÃO chamada; escopo e dados NÃO VERIFICADOS |
| 15 | Meta: Ads Insights API | https://developers.facebook.com/docs/marketing-api/insights | Trecho: "The Ads Insights API provides performance data and statistics for Meta ads."; permissão "ads_read"; acesso por `access_token` | Rate limit: a página só remete a "Limits and Best Practices", não lida |
| 16 | TikTok Marketing API | https://business-api.tiktok.com/portal/docs | Página aberta devolveu só o título "TikTok API for Business" | Endpoint `report/integrated/get` e atrasos (11 h, 48 h) vêm de espelhos e conectores de terceiros (N3): NÃO VERIFICADOS |
| 17 | Nuvem Pago e NF-e (via `t13-fiscal-taxas.md`) | https://atendimento.nuvemshop.com.br/pt_BR/informacoes-gerais-nuvem-pago/quais-sao-as-taxas-e-tarifas-do-nuvem-pago | Citado de lá, não reaberto por mim: "Todos os valores abaixo terão um acréscimo de R$0,35"; Pix 0,99%; boleto R$ 2,39 | Dado de segunda mão (outro departamento); reconferir |

**Conectores que exigem autorização e não foram usados:** Ahrefs, Similarweb, Supermetrics, Nimble. Nada foi assumido sobre o que entregam. Uso: nível C, com custo a aprovar.

## 10. Plano de testes (PROPOSTA; locais ou só leitura; nenhum gasta ou publica)

| ID | Hipótese | Passo | Passa se | Aprova |
|---|---|---|---|---|
| T-DOM-1 | O `.shop` é do João; `faixapretabr.com.br` está livre | João vê o painel do registrador e o registro.br; repetimos os RDAP dos itens 7 e 8 em 2 datas separadas por 24 h | titular confirmado; resultados idênticos | João |
| T-MARCA-1 | Há colidência de marca na classe do produto | João ou advogado busca "FAIXA PRETA" e variantes no portal do INPI; nós organizamos a lista | lista com data e print; decisão do jurídico | João + Jurídico |
| T-CUSTO-1 | 110 g, 9 h e R$ 2/h batem | 3 impressões do cupom/corpo; peso, tempo, recibo | desvio calculado; CHUTE vira ESTIMATIVA ou FATO com faixa | João imprime |
| T-CONC-1 | Faixa de preço atinge a amostra mínima | 10 anúncios de vaso/porta-lápis 3D em Mercado Livre, Shopee e Magalu, com data e vendedor | n >= 10, 3 vendedores, 2 canais, <= 30 dias | João ou navegador só leitura |
| T-CONF-1 | O processo de conflito funciona | aplicar 4.3 aos preços de `concorrentes.md` | valores listados e resolvidos ou escalados | nenhuma |
| T-SEO-1 | Rascunho sem avaliação inventada e sem termo proibido | `searchfit-seo:seo-audit` no HTML local, comparando com itens 1 e 2 | zero `review` falsa; zero termo proibido | nenhuma |
| T-SEO-2 | JSON-LD de Product válido | validar localmente contra os campos do item 2; ferramenta oficial de teste de rich results só depois da loja no ar e só se a doc dela for lida (NÃO VERIFICADO que seja a ferramenta certa) | sem erro; avisos listados | João |
| T-SEO-3 | Search Console devolve volume útil | com loja no ar e propriedade verificada, exportar o período; medir retenção na prática | 100+ impressões por consulta; retenção medida | João |
| T-MERC-1 | PMC do IBGE serve de contexto macro | baixar tabela pela página oficial, manualmente | número com tabela e data; "contexto, não demanda" | nenhuma |
| T-LOJA-1 | ShopifyQL responde sem expor cliente | só com pedidos de teste: métricas agregadas no editor do admin | `parseErrors` vazio; sem campo de cliente | João |
| T-ADS-1 | APIs de Meta/TikTok entregam as métricas | só após P4: ler a doc primária e puxar 7 dias de uma campanha de teste em leitura | métricas e atraso documentados | João |
| T-GW-1 | O gateway escolhido tem taxa oficial | para cada gateway candidato, abrir a tabela oficial (Mercado Pago deu 403; tentar painel) | taxa com link e data | João |

Ordem: T-DOM-1, T-MARCA-1, T-CUSTO-1; depois T-CONC-1, T-CONF-1 e T-GW-1; o resto só com loja e anúncios no ar.

## Resumo e decisões
Feito: doc refeito com fontes lidas, trechos e limites; `.shop` reproduzido pelo RDAP oficial do TLD; fatos do T13 incorporados. Pendente: titular do `.shop`, INPI, custos reais, retenção do Search Console, APIs de TikTok e IBGE. Bloqueio: acesso a painéis e registrador depende do João. Próximo passo: T-DOM-1, T-MARCA-1, T-CUSTO-1.

1. **Tornar obrigatórios os rótulos FATO/ESTIMATIVA/CHUTE/NÃO VERIFICADO** em todo número de mercado e custo que sair do repo. Recomendo sim: custo zero e barra R2 e R6.
2. **Autorizar T-DOM-1 e T-MARCA-1 agora** (João confere registrador e INPI; nós organizamos). Recomendo sim: domínio e marca travam Loja, SEO e Jurídico.
