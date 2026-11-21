# T13: custo de plataforma, Shopify x Nuvemshop (SIMULAÇÃO)

**Revisão 2026-11-20.** Reescrito para: (a) trazer trecho literal e link das taxas; (b) unir a atualização fiscal numa tabela só (antes havia duas, com duplicação); (c) tirar texto de conversa. Departamento: Gestão e Operações. Local, sem commit. Não é decisão: plataforma, preço e gateway são nível C (João). Fiscal e taxas em detalhe: `docs/operacao/t13-fiscal-taxas.md`.

Marcas: FATO (página oficial, link, data, trecho), SIMULAÇÃO (premissa minha), NÃO VERIFICADO.
**Os volumes (10, 50, 200 vendas/mês), o mix de pagamento, o ticket de R$ 89,90 e o câmbio são SIMULAÇÃO.** Nada foi vendido nem impresso.

## O que mudou na revisão
| Antes | Agora |
|---|---|
| Duas tabelas de 12 meses (sem nota e com nota), uma refutando a outra | Uma tabela: total sem nota, nota e total com nota |
| Taxas sem trecho literal | Trecho literal por fonte (seção 1) |
| Frase "o que disse antes ao João (US$ 19 a 39)" | Removida; vale só o oficial: Basic US$ 39 mensal / US$ 29 anual |
| Pagar.me: tarifa fixa "assumida R$ 0" sem destaque | Marcada como SIMULAÇÃO e como risco de subestimar o custo Shopify |

## 1. Fontes oficiais (abertas por WebFetch em 2026-11-20; a ferramenta resume, conferir na tela)
| Fonte | Link | Trecho literal devolvido |
|---|---|---|
| Shopify, preços | https://www.shopify.com/br/precos | "Pagamento mensal$ 39 USD/mês"; "Pagamento anual$ 29 USD/mês"; "Taxas de transação de terceiros" 2% (Basic). A página cita Shopify Payments e **não cita Pix**. (A URL `/br/preco` sem "s" dá 404) |
| Nuvemshop, planos | https://www.nuvemshop.com.br/planos-e-precos | "R$69 /mês" (Essencial, com "R$59 /mês" ao lado); Começo "Gratuito"; "No plano anual, você tem 15% de desconto". Sem data de vigência; só `dateModified` 2026-11-16 |
| Nuvem Pago, taxas (Central) | https://atendimento.nuvemshop.com.br/pt_BR/informacoes-gerais-nuvem-pago/quais-sao-as-taxas-e-tarifas-do-nuvem-pago | "Todos os valores abaixo terão um acréscimo de R$0,35"; Começo 30 dias 4,69%; Essencial 30 dias 4,19%; Pix "taxa de transação de 0,99%"; boleto "taxa de transação de R$2,39" |
| Pagar.me | https://pagar.me/precos | Pix "0,99%"; Crédito à vista "4,19%"; recebimento "Dia seguinte\*" (nota de rodapé do asterisco não aparece na página) |
| Mercado Pago | https://www.mercadopago.com.br/costs-section/release-options | **Falhou: HTTP 403.** Nenhum número usado. NÃO VERIFICADO |
| Notasy (app de NF na Shopify App Store) | https://apps.shopify.com/notasy | "From $5/month"; Starter US$ 5 (30 notas), Bootstrap US$ 19 (120), Scale US$ 34 (500) |
| Nota fiscal Nuvemshop (custo por nota) | https://atendimento.nuvemshop.com.br/pt_BR/minhas-vendas/como-funciona-a-emissao-de-nota-fiscal-pelo-painel-da-nuvemshop | Começo R$ 1,49; Essencial R$ 0,99 por nota; "5 primeiras notas fiscais são totalmente grátis no primeiro mês" |

## 2. Incertezas (não esconder)
- Shopify cobra em **US$**; a conversão e eventual IOF no cartão não foram verificados (HIPÓTESE).
- A página da Shopify não lista Pix nem gateway local; usei Pagar.me como gateway de terceiro (SIMULAÇÃO de escolha). Se existir meio local da Shopify sem os 2%, o custo Shopify cai (NÃO VERIFICADO).
- Pagar.me sem tarifa fixa publicada: assumi R$ 0 (SIMULAÇÃO). Se houver, o custo Shopify **sobe**.
- Nuvemshop: os totais anuais da página não batem com 12 x mensal (ex.: Essencial 704 informado x 708 calculado). Usei mensal x 12 (R$ 69 x 12 = R$ 828), conservador.
- Parcelado sem juros e antecipação do Nuvem Pago: sem percentual público para Começo/Essencial (detalhe em `t13-fiscal-taxas.md`). A conta cobre só cartão **à vista** e Pix.
- Fora da conta: frete, imposto sobre venda, domínio, apps além da nota, tema, dev, chargeback, antecipação, certificado A1 (custo NÃO VERIFICADO), Mercado Pago.

## 3. Premissas (todas SIMULAÇÃO)
- Ticket R$ 89,90 (já marcado como chute em `loja/simulacao-preco-frete.md`).
- Mix 50% Pix e 50% cartão à vista. Câmbio R$ 5,50 por US$ (não consultado); cada R$ 0,50 muda o Basic em R$ 19,50 por mês.
- Shopify: Basic mensal (US$ 39 = R$ 214,50 por mês) + Pagar.me (Pix 0,99%, crédito 4,19%) + 2% de terceiro da Shopify + app de nota Notasy (Starter até 30 notas, Bootstrap até 120, Scale até 500).
- Nuvemshop: Nuvem Pago, cartão com recebimento em 30 dias, Pix 0,99%; planos **Começo** (R$ 0/mês, cartão 4,69% + R$ 0,35) e **Essencial** (R$ 69/mês, cartão 4,19% + R$ 0,35); nota R$ 1,49 (Começo) ou R$ 0,99 (Essencial).
- 1 nota fiscal por venda; as 5 notas grátis do 1º mês foram desprezadas (conservador). Volume constante nos 12 meses.

## 4. Custo por venda de R$ 89,90, sem nota (SIMULAÇÃO)
| Plataforma | Pix | Cartão à vista | Mix 50/50 | % do ticket |
|---|---|---|---|---|
| Shopify Basic + Pagar.me | R$ 2,69 (0,99% + 2%) | R$ 5,56 (4,19% + 2%) | **R$ 4,13** | 4,6% |
| Nuvemshop Começo + Nuvem Pago | R$ 0,89 | R$ 4,57 | **R$ 2,73** | 3,0% |
| Nuvemshop Essencial + Nuvem Pago | R$ 0,89 | R$ 4,12 | **R$ 2,50** | 2,8% |
A diferença por venda vem sobretudo dos 2% de terceiro da Shopify.

## 5. Total em 12 meses (SIMULAÇÃO)
Total/mês = vendas x custo por venda (mix) + mensalidade + nota.

| Vendas/mês | Plataforma | Taxas + mensalidade/mês | Nota/mês | Total/mês | **12 meses sem nota** | **12 meses com nota** |
|---|---|---|---|---|---|---|
| 10 | Shopify + Notasy | R$ 255,76 | R$ 27,50 | R$ 283,26 | R$ 3.069 | **R$ 3.399** |
| 10 | Nuvemshop Começo | R$ 27,28 | R$ 14,90 | R$ 42,18 | R$ 327 | **R$ 506** |
| 10 | Nuvemshop Essencial | R$ 94,03 | R$ 9,90 | R$ 103,93 | R$ 1.128 | **R$ 1.247** |
| 50 | Shopify + Notasy | R$ 420,82 | R$ 104,50 | R$ 525,32 | R$ 5.050 | **R$ 6.304** |
| 50 | Nuvemshop Começo | R$ 136,41 | R$ 74,50 | R$ 210,91 | R$ 1.637 | **R$ 2.531** |
| 50 | Nuvemshop Essencial | R$ 194,17 | R$ 49,50 | R$ 243,67 | R$ 2.330 | **R$ 2.924** |
| 200 | Shopify + Notasy | R$ 1.039,78 | R$ 187,00 | R$ 1.226,78 | R$ 12.477 | **R$ 14.721** |
| 200 | Nuvemshop Começo | R$ 545,63 | R$ 298,00 | R$ 843,63 | R$ 6.548 | **R$ 10.124** |
| 200 | Nuvemshop Essencial | R$ 569,68 | R$ 198,00 | R$ 767,68 | R$ 6.836 | **R$ 9.212** |

Leitura (HIPÓTESE sobre os números acima):
- A Nuvemshop sai mais barata nos três cenários. A diferença é grande em volume baixo (mensalidade da Shopify em dólar) e continua relevante em volume alto (2% de terceiro).
- Com nota incluída, em 200 vendas por mês o Essencial passa a ser mais barato que o Começo (R$ 9.212 x R$ 10.124); sem nota era o contrário. A nota por unidade pesa mais no plano gratuito.
- O ponto de virada Começo x Essencial depende do mix de cartão e do volume, que são chute.

## 6. O que esta conta NÃO decide
- Dev e manutenção de tema: Shopify tem mais liberdade; Nuvemshop, menos. Não quantificado.
- A conta Shopify já existe com rascunho (plano Basic, FATO em `docs/CONTEXTO.md`); migrar tem custo de retrabalho não contado.
- Nada foi impresso: volume real hoje é zero. Mensalidade antes da peça validada é o custo mais evitável.
- Nota fiscal depende de contador (regime, IE, certificado A1): ver `t13-fiscal-taxas.md` §4.

## 7. Pendências
1. Taxas do Mercado Pago (403).
2. Se a Shopify tem meio de pagamento local sem a taxa de 2% e como cobra o US$.
3. Tarifa fixa e boleto do Pagar.me.
4. Taxa de parcelado e antecipação do Nuvem Pago para Começo e Essencial (suporte ou painel).
5. O João define mix, ticket e volume reais antes de qualquer decisão de plataforma.
