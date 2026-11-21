# T13: Shopify x Nuvemshop (Pix, NF-e, checkout, pixel, frete, API, tema) — consolidado

## Revisão 2026-11-20
Erros da versão anterior, corrigidos aqui:
1. Itens que eu tinha como "FATO" a partir de resumo de BUSCA (taxa de Nuvem Pago, NF-e, frete) agora só são FATO onde a página foi aberta (links abaixo). O resto está como TERCEIRO, HIPÓTESE ou NÃO VERIFICADO.
2. NF-e Nuvemshop: eu disse "atende MEI e Simples" sem fonte aberta; agora há trecho (via `t13-fiscal-taxas.md`). Também disse "sem mensalidade, paga por nota conforme o plano": confirmado, com valores. O trecho sobre DC-e/NF-e a partir de 01/11/2026 NÃO foi reverificado.
3. Eu dizia "Nuvemshop sem camada extra de 2%": errado em termos. A página de planos cobra "tarifa por venda sem Nuvem Pago" (Começo e Essencial 2%; Impulso 1%; Escala 0,7%); com Nuvem Pago a tarifa é isenta. Vale só se usar o Nuvem Pago.
4. Cartão Nuvem Pago: antes "não verificado por plano"; agora FATO com tabela (fonte aberta em `t13-fiscal-taxas.md`).
5. Nuvemshop API, tema, sandbox: antes NÃO VERIFICADO; agora FATO com trecho (`t13-nuvemshop-api-tema.md`).
6. A comparação de custo foi dada sem fonte e mal calculada ("4 a 9 vezes"). Pela simulação de `t13-custos.md` (SIMULAÇÃO): com 10 vendas/mês, 12 meses, Shopify R$ 3.069 contra Nuvemshop R$ 327 (Começo) a R$ 1.128 (Essencial): 2,7 a 9,4 vezes. Com 200 vendas/mês: R$ 12.477 contra R$ 6.548 a R$ 6.836 (cerca de 1,8 vez). Premissas (R$ 5,50/US$, mix 50/50, ticket R$ 89,90) são chute.
7. Eu tinha misturado "o que Shopify faz" com "o que o app terceiro faz". Agora cada linha diz de quem é.

Legenda: FATO = página oficial aberta em 2026-11-20 (WebFetch resume; reconferir na tela antes de decidir). TERCEIRO = blog, fórum, vendedor de app. HIPÓTESE = inferência. NÃO VERIFICADO = sem trecho literal após tentar. Não é decisão: plataforma é do João (nível C).

## 1. Pix, boleto, cartão
| Item | Shopify | Nuvemshop |
|---|---|---|
| Gateway nativo no BR | FATO: Brasil não está na lista de 41 países do Shopify Payments; "if your country isn't listed, you need to use a third-party payment provider" (https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries) | FATO: Nuvem Pago |
| Pix | gateway local (Pagar.me: Pix 0,99%, `t13-custos.md`); Mercado Pago: NÃO VERIFICADO (403) | FATO: 0,99%, "o mesmo para todos os planos" (https://atendimento.nuvemshop.com.br/pt_BR/informacoes-gerais-nuvem-pago/quais-sao-as-taxas-e-tarifas-do-nuvem-pago) |
| Boleto | NÃO VERIFICADO (depende do gateway; Pagar.me não informa) | FATO: R$ 2,39, mesma página |
| Cartão à vista | gateway (Pagar.me 4,19%, incompleto) | FATO: + R$ 0,35 por transação; Começo 4,69% (30 dias), 5,19% (14), 5,69% (2); Essencial 4,19/4,69/5,19; Impulso 3,69/4,19/4,69; Escala 3,29/3,69/3,99 |
| Parcelado e antecipação | NÃO VERIFICADO | NÃO VERIFICADO para Começo/Essencial; antecipação "apenas para lojas Next" (2,29% a.m.) |
| Taxa da plataforma sobre gateway externo | FATO: Basic 2%, Grow 1%, Advanced 0,6%, Plus 0,2% (https://www.shopify.com/br/precos); valores em US$ | FATO (página de planos): sem Nuvem Pago, Começo/Essencial 2%, Impulso 1%, Escala 0,7%; com Nuvem Pago isenta |
| Plano | Basic US$ 39 mensal / US$ 29 anual | Começo grátis; Essencial R$ 69; Impulso R$ 164; Escala R$ 449; Next sob consulta (https://www.nuvemshop.com.br/planos-e-precos) |

## 2. Nota fiscal (NF-e)
| | Shopify | Nuvemshop |
|---|---|---|
| Nativa? | Shopify: "A emissão de nota fiscal ainda não é uma funcionalidade nativa" (staff, 31/08/2021, fonte antiga; sem página de ajuda atual achada) https://community.shopify.com/t/emissao-de-nota-fiscal/62743 | FATO: emissão pelo painel (menu Configurações > Documentos fiscais > NF-e), só MEI ou Simples: "A emissão ainda não está disponível para outros regimes." Exige IE e certificado A1 (.pfx). Custo por nota: Começo R$ 1,49; Essencial R$ 0,99; Impulso R$ 0,49; Escala R$ 0,25; Next R$ 0,10; 5 primeiras grátis. Fontes: `docs/operacao/t13-fiscal-taxas.md` |
| Apps | FATO: Bling (a partir de US$ 9,57/mês, nota 2,4/5) e Notasy (US$ 5 a 56/mês) na App Store BR, ambos de terceiros | Bling, Tiny e outros emissores externos para outros regimes (citados na Central) |
| Depende do contador | regime, IE, certificado A1 e se o produto exige NF-e (ver `t13-fiscal-taxas.md` §4) | idem |

## 3. Checkout editável e tema
| Item | Shopify | Nuvemshop |
|---|---|---|
| Checkout | FATO: Thank you e Order status de lojas não Plus editáveis (editor de checkout, blocos, web pixels); scripts adicionais só leitura desde 2025-08-28 (https://help.shopify.com/en/manual/checkout-settings/checkout-extensibility/checkout-upgrade). Etapas Informação/Envio/Pagamento no Basic: TERCEIRO ("só Plus"); NÃO VERIFICADO em página oficial | FATO: "Os códigos personalizados no checkout estão disponíveis apenas para lojas do plano Nuvemshop Next."; "Não é possível alterar livremente os campos, os botões ou a estrutura original do checkout" (https://atendimento.nuvemshop.com.br/pt_BR/12311-opcoes-de-checkout/como-adicionar-codigos-personalizados-no-checkout-da-minha-loja-nuvemshop) |
| Tema | FATO anterior: `themeCreate` exige `write_themes` e isenção Shopify; temas Liquid | FATO: Começo "1 padrão"; demais "+70 gratuitos"; código-fonte "não está disponível em todos os planos" (plano exato NÃO VERIFICADO: Impulso ou Escala); CLI oficial, base "ipanema" (https://atendimento.nuvemshop.com.br/pt_BR/para-parceiros-nuvemshop/como-instalar-e-usar-a-cli-da-nuvemshop-para-editar-layouts). Twig: só blog, HIPÓTESE |

## 4. Pixel Meta/TikTok
- Shopify: NÃO VERIFICADO em página oficial (a página de pixels personalizados lida não trata de `checkout_completed`, plano nem Conversions API). Apps de terceiros existem (US$ 8,99 a 19,79/mês, TERCEIRO).
- Nuvemshop: FATO, Purchase configurável ("quando o checkout é concluído ou somente quando o pedido é marcado como pago"), até 24 h de atraso, também por API de Conversões (https://atendimento.nuvemshop.com.br/pt_BR/pixel-do-facebook/quais-eventos-a-nuvemshop-envia-para-o-pixel-e-como-eles-funcionam). Requisito de plano: a página não menciona nenhum (ausência de menção não prova). TikTok: 404, NÃO VERIFICADO.

## 5. Frete BR
- Shopify FATO (https://www.shopify.com/br/precos): frete calculado por transportadora de terceiros não incluído no Basic. Melhor Envio no Basic: conflito entre fórum (exige CCS, +US$ 20/mês no mensal) e blog do próprio Melhor Envio (março de 2026, todos os planos): NÃO RESOLVIDO. Apps como Frenet e Correios/Melhor Envio: TERCEIRO. Alternativa que funciona: tabela fixa por região (SIMULAÇÃO R$ 22/28/34/42, `loja/simulacao-preco-frete.md`).
- Nuvemshop FATO (https://atendimento.nuvemshop.com.br/pt_BR/informacoes-gerais-2/como-escolher-a-ferramenta-de-frete-perfeita-para-a-minha-loja): Começo só Nuvem Envio (Correios) e retirada; demais planos instalam várias ferramentas (Frenet, Melhor Envio, Jadlog...); apps cobram por entrega ou etiqueta, sem custo fixo.

## 6. API, agents e sandbox
| Item | Shopify | Nuvemshop |
|---|---|---|
| Escopos | token atual com dezenas de escopos de escrita; sem `write_legal_policies` (leitura 2026-11-20) | FATO: por recurso (`read_/write_products`, `orders`, `customers`, `coupons`, `content`; `write_scripts`, `write_shipping`); sem escopo de tema |
| Token | permissões revisáveis no painel | FATO: "Our access tokens don't expire." |
| Rate limit | NÃO VERIFICADO (números); leaky bucket por custo | FATO: balde 40, 2 req/s; Next/Evolution 10x |
| Reembolso por API | token tem `write_orders` e `write_returns`; mutações não testadas | NÃO VERIFICADO (endpoint não achado em 118 mil caracteres) |
| Sandbox | loja de desenvolvimento (conector `create_store`; disponibilidade NÃO VERIFICADA) | FATO: loja demo ("não realiza vendas") e loja em desenvolvimento (https://atendimento.nuvemshop.com.br/pt_BR/parceiros-especialistas/como-criar-lojas-no-portal-de-parceiros) |

## 7. Leitura e recomendação (HIPÓTESE; decide o João)
- Vale nas duas plataformas: regras de segredo, portões P1 a P4, rascunho primeiro, conferência cruzada, checklist.
- Custo (SIMULAÇÃO): a Nuvemshop sai mais barata em todos os cenários de `t13-custos.md`. Pix, boleto e NF-e (se MEI ou Simples) são mais simples nela. A Shopify tem API mais madura, tema Liquid e é onde os agents já operam, mas o token atual é amplo demais.
- Migrar o único produto em rascunho custa pouco (sem foto, SKU, estoque ou pedido).
- Não decidir antes de: (1) contador: regime, IE e certificado A1; (2) T13d (app mínimo na loja demo); (3) plano mínimo com código-fonte; (4) reembolso por API e pixel por plano; (5) Mercado Pago e Pagar.me completos.

## 8. NÃO VERIFICADO (lista única)
Cartão parcelado e antecipação (Começo/Essencial); Mercado Pago; checkout Shopify Basic (etapas); pixel Shopify no Basic; CCS e Melhor Envio no Basic; TikTok Nuvemshop; plano mínimo de código-fonte; Twig em página oficial; reembolso por API Nuvemshop; app próprio sem avaliação; rate limit Shopify (números); DC-e para NF-e em 01/11/2026.
