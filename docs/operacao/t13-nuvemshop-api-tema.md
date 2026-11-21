# T13b: Nuvemshop, API, temas, checkout, pixel (verificação com trecho literal)

> Consulta em 2026-11-20. Cada página foi ABERTA com WebFetch; o resultado é o resumo do WebFetch com trechos entre aspas. Regra: sem trecho literal = NÃO VERIFICADO. Nada alterado em loja. Não é decisão de plataforma (nível C, João).
> Limite do método: o WebFetch usa modelo pequeno; "trecho" é o que ele devolveu entre aspas. Conferir no navegador o que for decisivo.
> Observação: não abri conta, não instalei app, não criei token.

## 1. API Nuvemshop (documentação oficial: https://tiendanube.github.io/api-documentation/, versão "2025-03")

| Item | Status | Trecho literal | Link |
|---|---|---|---|
| Escopos | FATO | "read_content / write_content" (Page); "read_products / write_products" (Product, Product Variant, Product Image, Category); "read_customers / write_customers"; "read_orders / write_orders"; "read_coupons / write_coupons"; "write_scripts"; "write_shipping" | https://tiendanube.github.io/api-documentation/authentication |
| Token só de leitura | FATO (indireto) | "If an app only needs to read products, it should only ask for the `read_products` scope." Também: "If you ask for any write scope, the read scope is implied." A página não diz explicitamente "token read-only", mas o app escolhe os escopos | idem |
| Obtenção/expiração | FATO | Token via POST em https://www.tiendanube.com/apps/authorize/token; "authorization code expires in 5 minutes"; "Our access tokens don't expire. They become invalid only after you get a new one, or if the user uninstalls your app." | idem |
| Rate limit | FATO | "the default bucket size is of 40 requests with a leaky rate of 2 requests per second"; "The rate limit works between each store and app."; "If the store is Next or Evolution (higher plans), the rate limit multiplies by 10." | https://tiendanube.github.io/api-documentation/intro |
| Cabeçalho obrigatório | FATO | "you must include a `User-Agent` header with the name of your application"; sem ele "400 Bad Request" | idem |
| Produtos | FATO | `GET /products`, `GET /products/sku/{sku}`, `POST /products`, `PUT /products/{id}`, `DELETE /products/{id}`, `PATCH /products/stock-price` ("Updates Stock or Price of multiple products and variants."; até 50 variantes por requisição) | https://tiendanube.github.io/api-documentation/resources/product |
| Rascunho/publicação | FATO | `visibility`: visible, unlisted ou hidden; "`published` ... _true_ only when the Product's `visibility` is `visible`."; mandar os dois campos juntos dá "HTTP 422" | idem |
| Estoque e SKU | FATO | `stock` e `sku` ficam na variante; sem múltiplos locais, estoque ilimitado é `"stock": ""`; com mais de um local, "each element must include its `location_id`" em `inventory_levels`; "`stock_management` ... can't be modified via API." | idem |
| Limites de catálogo | FATO | 100.000 produtos por loja; 250 imagens; 1000 variantes; 3 atributos; "Our API returns up to 30 results by default." | idem |
| Pedidos | FATO | `GET /orders`, `GET /orders/{id}`, `POST /orders/`, `PUT /orders/{id}`, `POST /orders/{id}/close`, `/open`, `/cancel` (motivos: "customer", "inventory", "fraud" ou "other"); "In fact, there is no action to pay an order." | https://tiendanube.github.io/api-documentation/resources/order |
| Status de pagamento | FATO (com divergência) | `payment_status`: "authorized", "pending", "paid", "partially_paid", "abandoned", "refunded", "partially_refunded"; a tabela de criação traz outro conjunto (pending, authorized, paid, voided, refunded, abandoned) | idem |
| Reembolso por API | NÃO VERIFICADO | A leitura dos 118.982 caracteres da página não achou endpoint de refund. Só menções: "Actions that may alter an Order's total are either editing or refunding an Order." Conclusão provisória (HIPÓTESE): não há endpoint de reembolso; o reembolso seria pelo painel/gateway. Confirmar | idem (completo, incluindo offset 100000) |
| NF-e por API | FATO | metafields de pedido usados na seção de invoices: `GET /metafields/orders`, `POST /metafields`, `PUT /metafields/METAFIELD_ID` | idem |
| Webhooks | FATO | Order: "created/updated/paid/packed/fulfilled/cancelled"; Product: "created/updated/deleted"; header "x-linkedstore-hmac-sha256" (HMAC-SHA256 do corpo com o secret do app); resposta 2XX em 3 s; 16 tentativas em 48 h | https://tiendanube.github.io/api-documentation/resources/webhook |
| Loja de teste / sandbox | FATO | "Loja demo: utilizada para testar e expor recursos e aplicativos desenvolvidos por parceiros. ... Não é usada como loja real, ou seja, não realiza vendas." "Loja em desenvolvimento: utilizada para projetos entre parceiros e lojistas." Criar exige cadastro no Portal de Parceiros (nome, e-mail, país, CPF/CNPJ do cliente) | https://atendimento.nuvemshop.com.br/pt_BR/parceiros-especialistas/como-criar-lojas-no-portal-de-parceiros |
| Página intro cita parceiro | FATO | "Register as a partner in Tiendanube or Nuvemshop." | https://tiendanube.github.io/api-documentation/intro |

**Respostas diretas**
- Dá para um agent operar com token restrito? SIM em princípio (FATO): o app declara só os escopos que precisa, por exemplo `read_products` + `read_orders` para leitura. Não achei escopo mais fino que "leitura/escrita por recurso" (granularidade por recurso, não por ação). Para escrita em produto sem pedido: `write_products` apenas. (Não existe escopo de reembolso porque não achei endpoint.)
- Comparação com o token Shopify atual (30+ escopos de escrita): a Nuvemshop forçaria mínimo privilégio por desenho, mas só se criarmos o app com poucos escopos. É HIPÓTESE que um app privado/custom seja permitido sem passar por avaliação da Loja de Aplicativos: o texto lido diz que publicar na loja exige avaliação técnica (busca), não que uso próprio exija. NÃO VERIFICADO.
- Sandbox: existe loja demo e loja em desenvolvimento (FATO); a demo não vende, então teste de pedido pago ponta a ponta seria limitado (HIPÓTESE: pagamento real não roda na demo).
- Não verificado nesta rodada: endpoint de eventos/pagamento de Nuvem Pago por API, campo `inventory_levels` em loja de um local só, e se a API aceita tema (não há escopo de tema: a lista de escopos acima não tem). Conclusão (FATO por ausência na lista): agent NÃO edita tema por API; tema é pela CLI/FTP ou painel.

## 2. Temas e checkout

| Item | Status | Trecho literal | Link |
|---|---|---|---|
| Temas oficiais por plano | FATO | Começo: "1 padrão"; Essencial, Impulso, Escala e Next: "+70 gratuitos" | https://www.nuvemshop.com.br/planos-e-precos |
| Acesso ao código-fonte | FATO (plano exato NÃO VERIFICADO) | Central: "O acesso ao código-fonte não está disponível em todos os planos." (procure "Acesso ao código-fonte (HTML/CSS/JS)" na página de planos). A página de planos traz "Acesso ao código-fonte" no card do Impulso, mas a linha de comparação não mostrou valores. Busca/blog divergem (Impulso x Escala) | https://atendimento.nuvemshop.com.br/pt_BR/personalizacao-avancada-do-layout/como-editar-o-codigo-do-layout-da-minha-loja ; planos-e-precos |
| Requisitos de edição | FATO | "HTML, CSS e JavaScript"; "fazer backup ... porque a Nuvemshop não faz backup de layout personalizado" | idem |
| CLI oficial | FATO | "a ferramenta de linha de comando oficial para desenvolver layouts na Nuvemshop"; edita local, sincroniza, `nuvemshop theme preview` gera "um link da loja com o identificador do tema, que você pode compartilhar para aprovação"; "A publicação torna esse tema o tema produtivo da loja"; "No momento, o tema base aceito é o ipanema"; Node.js 24.15 ou superior | https://atendimento.nuvemshop.com.br/pt_BR/para-parceiros-nuvemshop/como-instalar-e-usar-a-cli-da-nuvemshop-para-editar-layouts |
| Plano exigido pela CLI | NÃO VERIFICADO | o artigo "não informa requisitos de plano" | idem |
| Linguagem de template | HIPÓTESE | blog da Nuvemshop apresenta Twig (https://www.nuvemshop.com.br/blog/o-que-e-o-twig-e-como-usar, só via busca, página não aberta). A Central lida não menciona Twig. Não é Liquid (a Shopify usa Liquid) | NÃO aberto |
| Checkout editável | FATO | "Os códigos personalizados no checkout estão disponíveis apenas para lojas do plano Nuvemshop Next."; "Não é possível alterar livremente os campos, os botões ou a estrutura original do checkout com os códigos personalizados."; scripts em JSX da biblioteca Nube SDK | https://atendimento.nuvemshop.com.br/pt_BR/12311-opcoes-de-checkout/como-adicionar-codigos-personalizados-no-checkout-da-minha-loja-nuvemshop |
| Cores/aparência do checkout em planos menores | NÃO VERIFICADO | não abri a página de opções de checkout | — |

**Leitura:** nos planos baixos o tema é do catálogo (+70 gratuitos, edição de código talvez só em plano mais alto); tema próprio via CLI parte do "ipanema". Checkout só customizável (e pouco) no Next. Para a Faixa Preta (1 produto, vitrine discreta), tema do catálogo + CSS pode bastar; a tese "tema 100% próprio" na Shopify é mais livre (HIPÓTESE, não comparei tema a tema).

## 3. Pixel Meta Purchase por plano
| Item | Status | Trecho literal | Link |
|---|---|---|---|
| Purchase | FATO | "O Purchase é disparado quando acontece a conclusão de uma compra, indicada pelo recebimento da confirmação do pedido."; configurável: "quando o checkout é concluído ou somente quando o pedido é marcado como pago" | https://atendimento.nuvemshop.com.br/pt_BR/pixel-do-facebook/quais-eventos-a-nuvemshop-envia-para-o-pixel-e-como-eles-funcionam |
| Prazo/teste | FATO | "O envio do Purchase pode acontecer em até 24 horas após a conclusão da compra."; o Pixel Helper e o Teste de eventos da Meta "não identificam o Purchase" | idem |
| Requisito de plano | NÃO VERIFICADO (sem restrição citada) | "O artigo não menciona nenhum requisito de plano da Nuvemshop, nem para o evento Purchase nem para os demais eventos." Ausência de menção não prova que todos os planos têm. A página de planos também não trata de pixel | idem; https://www.nuvemshop.com.br/planos-e-precos |
| API de Conversões (servidor) | FATO (lida antes) | Purchase também pela API de Conversões | idem |
| TikTok | NÃO VERIFICADO | página de TikTok deu 404 | https://atendimento.nuvemshop.com.br/pt_BR/tiktok |

## 4. O que muda para os agents e para o voto
- Para o agent operar: Shopify tem escopos mais finos mas o token atual é amplo demais; Nuvemshop tem poucos escopos por recurso, token que não expira (risco se vazar) e sem escopo de tema, sem endpoint de reembolso achado e rate limit baixo (2 req/s, balde 40). Cabe ao agent: catálogo, estoque (PATCH em lote de 50), pedidos (leitura, close/cancel), webhooks.
- Reembolso, preço e publicação continuam C. Na Nuvemshop reembolso (provável) só pelo painel, o que reforça o "só o João".
- Se o voto for Nuvemshop, o primeiro passo seria loja em desenvolvimento/demo para testar T13d: criar app com `read_products` e `write_products` apenas e chamar `GET /products`, `PUT` com `visibility:hidden`, `PATCH /products/stock-price`. Resultado esperado (HIPÓTESE): funciona sem aprovação da Loja de Aplicativos para uso próprio; confirmar.

## 5. Pendências de verificação
1. Plano mínimo de "Acesso ao código-fonte" (Impulso ou Escala).
2. Endpoint de reembolso (se existir) e se Nuvem Pago aceita estorno por API.
3. App privado sem passar por avaliação da Loja de Aplicativos.
4. Pixel por plano e TikTok (404).
5. Taxa de boleto e de cartão por plano (já pendentes no t13-custos).
6. Twig na Central oficial (não só blog).
