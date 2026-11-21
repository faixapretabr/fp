# T13: verificação fiscal e taxas (Nuvemshop x Shopify)

**Revisão 2026-11-20.** Reescrito: tirei a tabela de veredito que misturava FATO com resumo; cada linha agora traz link e trecho literal ou o rótulo NÃO VERIFICADO; marquei a divergência interna da Nuvemshop sobre as notas grátis. Departamento: Gestão e Operações. Local, sem commit. Não é decisão (plataforma, regime e certificado são do João e do contador).

Método: cada página foi aberta por WebFetch na própria URL em 2026-11-20. O WebFetch resume com modelo pequeno e limita a citação; os trechos entre aspas são os que a ferramenta devolveu como literais. **Reconferir na tela antes de decidir.** Sem trecho = NÃO VERIFICADO.

## 1. Nuvemshop: nota fiscal
| Item | Veredito | Trecho literal | Link |
|---|---|---|---|
| Emissão pelo painel | FATO (parcial) | "emitir Notas Fiscais pela Nuvemshop"; menu "Configurações > Documentos fiscais > NF-e". A página de funcionamento **não diz expressamente** que o painel emite NF-e; o menu NF-e e o simulador de custo de NF-e sim | [como funciona](https://atendimento.nuvemshop.com.br/pt_BR/minhas-vendas/como-funciona-a-emissao-de-nota-fiscal-pelo-painel-da-nuvemshop), [simular custo](https://atendimento.nuvemshop.com.br/pt_BR/minhas-vendas/como-simular-o-custo-mensal-de-nf-e-e-dc-e-na-minha-loja-nuvemshop) |
| Só MEI ou Simples? | FATO | "Ser MEI ou Simples Nacional. A emissão ainda não está disponível para outros regimes." / "Ter loja com CNPJ MEI ou do Simples Nacional" | como funciona; [ativar](https://atendimento.nuvemshop.com.br/pt_BR/minhas-vendas/como-ativar-a-emissao-de-notas-fiscais-pelo-painel-da-nuvemshop) |
| Inscrição Estadual | FATO | "Inscrição estadual válida no estado de origem da sua empresa"; "CNPJ ativo e regular na Receita Federal" | ativar |
| Certificado A1 | FATO na ativação | "Certificado digital válido para assinatura das notas fiscais eletrônicas"; passo 7: enviar "o seu certificado digital A1 no formato .pfx". A página "como funciona" diz só "Certificado Digital válido" | ativar; como funciona |
| Custo por nota | FATO | "5 primeiras notas fiscais são totalmente grátis no primeiro mês". Depois: Começo R$ 1,49; Essencial R$ 0,99; Impulso R$ 0,49; Escala R$ 0,25; Next R$ 0,10. "cancelamento de uma NF não gera custo" | como funciona |
| Divergência interna | NÃO RESOLVIDA | O simulador diz "As 5 primeiras notas ou declarações são grátis" (sem "no primeiro mês") e **não traz valores em R$** | simular custo |
| Integração Bling/Tiny | FATO (parcial) | Sem integração nativa citada; sugere "usar um emissor externo (NFe.io, Bling, Tiny, etc.)" para pedidos fora das regras | como funciona |
| Custo do certificado A1 | NÃO VERIFICADO | Só vi preço de parceiro em resultado de busca; página do parceiro não aberta; não usado | n/a |

Não abri: "como escolher entre NF-e, NFC-e e DC-e" e "como acompanhar o custo de documentos fiscais".

## 2. Nuvem Pago: cartão, parcelado, antecipação e prazo
Fonte: [taxas e tarifas](https://atendimento.nuvemshop.com.br/pt_BR/informacoes-gerais-nuvem-pago/quais-sao-as-taxas-e-tarifas-do-nuvem-pago).
| Item | Veredito | Trecho literal |
|---|---|---|
| Cartão à vista por plano e prazo | FATO | "Todos os valores abaixo terão um acréscimo de R$0,35". Começo: 30 dias 4,69%, 14 dias 5,19%, 2 dias 5,69%. Essencial: 4,19% / 4,69% / 5,19%. Impulso: 3,69% / 4,19% / 4,69%. Escala: 3,29% / 3,69% / 3,99% |
| Prazos de recebimento do cartão | FATO | "oferecemos três prazos de recebimentos diferentes: 2, 14 e 30 dias." (taxa maior para prazo menor) |
| Pix | FATO | "feita na mesma hora"; "taxa de transação de 0,99%"; "o mesmo para todos os planos" |
| Boleto | FATO | "até 2 dias com uma taxa de transação de R$2,39" |
| Parcelado sem juros (lojista assume) | **NÃO VERIFICADO (valor)** | Página de [parcelamento](https://atendimento.nuvemshop.com.br/pt_BR/configuracao-nuvem-pago/como-configurar-o-parcelamento-no-nuvem-pago): "o lojista assume o pagamento das taxas"; "Para consultar os valores, entrar em contato com a equipe de suporte." Percentuais não constam |
| Parcelado com juros (cliente paga) | FATO | "o cliente assume todos os juros da compra" acima do limite sem juros; o lojista paga "apenas as taxas do plano de recebimento (D30, D14 ou D2)". A tabela "taxas fixas para consumidores finais" (2x 16,65% a 12x 23,44%) é do comprador |
| Antecipação (Começo e Essencial) | **NÃO VERIFICADO** | Não consta na página de taxas. Só consta em [plano pagamento no fluxo](https://atendimento.nuvemshop.com.br/pt_BR/sacar-o-saldo/conheca-o-plano-pagamento-no-fluxo-do-nuvem-pago), "apenas para lojas Next": juros compostos de 2,29% ao mês, mesmo dia só se pedida ao suporte "até as 9h" |
| 2,99% à vista / 3,29% 2x a 6x / 3,79% 7x a 12x | FATO, **só Next** | Mesma página do plano no fluxo. Não usar para Começo e Essencial |

As taxas de cartão à vista que o `t13-custos.md` usa (Começo 4,69% e Essencial 4,19%, mais R$ 0,35, recebimento em 30 dias) coincidem com esta tabela.

## 3. Shopify: nota fiscal
| Item | Veredito | Trecho ou dado | Link |
|---|---|---|---|
| NF-e nativa | FATO, fonte antiga | Staff Shopify: "A emissão de nota fiscal ainda não é uma funcionalidade nativa da nossa plataforma". Autor Fran_6, 31/08/2021 (5 anos). Não achei página de ajuda atual dizendo o contrário nem confirmando | [comunidade](https://community.shopify.com/t/emissao-de-nota-fiscal/62743) |
| App na Shopify App Store | FATO | **Bling** (dev. "Bling ERP"): "permite ainda a emissão de notas fiscais eletrônicas"; "From $9.57/month. Free trial available."; nota 2,4 de 5 com 5 avaliações. **Notasy** (dev. Notasy, Florianópolis): "Emita suas notas fiscais (NF-e & NFS-e) de forma automática para cada venda realizada"; "From $5/month"; Starter US$ 5 (30 notas), Bootstrap US$ 19 (120), Scale US$ 34 (500), Professional US$ 56 (2.000); nota 5,0 com 4 avaliações | [Bling](https://apps.shopify.com/app76902), [Notasy](https://apps.shopify.com/notasy) |
| App "oficial" da Shopify | NÃO ENCONTRADO | Nenhum selo "Built for Shopify" nem de app oficial nos dois anúncios; são apps de terceiros | idem |
| Tiny, Spedy | NÃO VERIFICADO na App Store | A resposta de 2021 diz que Bling e Tiny ficavam fora da loja; hoje o Bling está listado. Spedy aparece em resposta de usuário de 29/04/2025, não staff | comunidade |
| Qualidade dos apps | HIPÓTESE de risco | Bling 2,4 de 5; Notasy só 4 avaliações | idem |
Preços da App Store são em US$ (mesmo ponto de atenção do câmbio).

## 4. O que depende do contador
1. Regime da Faixa Preta (MEI ou Simples Nacional). Outro regime: a emissão nativa da Nuvemshop não vale ("ainda não está disponível para outros regimes").
2. Se a venda exige **NF-e** e se há dispensa ou regra própria para o enquadramento (NÃO VERIFICADO).
3. Inscrição Estadual: obrigatoriedade e como obter (a Nuvemshop exige IE válida).
4. Certificado A1: tipo, emissor, custo e prazo (a plataforma exige A1 em .pfx).
5. Impostos por venda (ICMS, Simples), não incluídos em nenhuma conta nossa.
6. Contribuinte de ICMS e a mudança de DC-e para NF-e citada em `docs/operacao/t13-plataformas.md` (não reverifiquei).

## 5. Pendências
- Parcelado sem juros e antecipação para Começo e Essencial: suporte do Nuvem Pago ou painel (Configurações > Nuvem Pago).
- Reconferir os trechos na tela (o WebFetch resume).
- Página de ajuda atual da Shopify sobre nota fiscal: não achei; a prova mais recente é de 2025, em fórum.
