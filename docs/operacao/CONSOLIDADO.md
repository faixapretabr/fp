# Consolidado: inteligência operacional e fiscalização cruzada

Rascunho local. Nada publicado, gasto ou alterado fora do repo. Detalhe em cada `docs/operacao/<depto>.md` (seções 1 a 10). Números = SIMULAÇÃO até haver dado real. Fonte oficial lida só em parte; o resto é (hipótese).

## 1. Regra central
Ninguém confia cego em agente. Quem executa não confere o próprio trabalho. Silêncio ou falta de conferência nunca é aprovação.

## 2. Papéis (fiscalização cruzada)
| Papel | Quem | Faz |
|---|---|---|
| Executor | departamento dono da tarefa | produz |
| Conferente | outro departamento | checa contra checklist |
| Fiscalizador | Qualidade | marca, segredo, rótulos, vocabulário; pode bloquear |
| Liberador | Cláudio (local, reversível) / João (nível C) | libera |

## 3. Matriz de fiscalização cruzada
| Saída de | Conferente | Fiscalizador | Liberador |
|---|---|---|---|
| Produto (STL, ficha) | Qualidade | Qualidade | João (P1, P2) |
| Marketing/copy/vídeo | Jurídico | Qualidade | João |
| Anúncios | Jurídico + Gestão (verba) | Qualidade | João (verba) |
| Ecommerce/loja | Atendimento | Qualidade | João (P4) |
| Atendimento (respostas) | Jurídico | Qualidade | Cláudio; João se nível C |
| Jurídico | advogado humano | Qualidade | João (P3) |
| Inteligência (números) | Gestão | Qualidade (rótulos) | Cláudio |
| Gestão/Cláudio | Qualidade | João (amostra) | João |
| Qualidade | Gestão (amostra por hash) | João | João |

## 4. Autonomia (A sozinho, B sozinho e avisa, C só João)
- Vale só depois de P2, P3, P4 e do "grava".
- C: preço, frete, troca, produto novo, subir verba, reembolso, dúvida de segredo, trocar plataforma, publicar.
- Reembolso solo: R$ 0 nos primeiros 30 dias (Atendimento); depois até R$ 90 (proposta).
- Verba: teste Meta R$ 315 no total (3 criativos x R$ 105, sem duração definida) vs teto R$ 150/semana do playbook. Não são conflito: um é total, outro é taxa. Decisão aberta: duração.
- Freio de proteção (só pausa, nunca reativa ou sobe verba): proposta Anúncios.

## 5. Política executar / conferir / liberar
1. Executor entrega arquivo + 5 linhas.
2. Conferente roda checklist da seção 5 do próprio depto.
3. Qualidade roda `qualidade_scan.py` + rótulos FATO/ESTIMATIVA/CHUTE/NÃO VERIFICADO.
4. Liberador decide. Sem resposta = parado.

## 6. Protocolo de bloqueio
Qualquer um bloqueia: segredo exposto, termo proibido, número sem rótulo, promessa legal errada (ex.: garantia 7 dias; lei = 30/90), dado de cliente saindo, gasto sem teto. Bloqueio vai para `docs/decisoes.md`; só o liberador desbloqueia.

## 7. Achados que travam
- 17 bloqueios do scan: "tampa de rosca" (loja/SEO), "Mesa (oculta)", "cupom da rosca" (calendário). Troca é local e reversível.
- Política trata defeito em 7 dias; CDC arts. 18 e 26: 30 dias para sanar, 90 para reclamar de bem durável (Jurídico leu a lei; advogado confirma). `loja/politicas-v2-rascunho.md` ainda NÃO existe.
- PNG de teste: C2PA removido a pedido do João (originais em backup local). Marcar "conteúdo de IA" no app da plataforma continua sendo regra da plataforma.
- Divergências: preço R$ 89,90 (Shopify) vs R$ 0,00 (`pendencias.md`); handle `porta-lapis` vs `porta-lapis-preto-3d`.
- Hook de commit conflita com regra do CLAUDE.md. CLAUDE.md vence.

## 8. Plataforma (T13, fontes oficiais em `t13-plataformas.md`, `t13-custos.md`, `t13-fiscal-taxas.md`, `t13-nuvemshop-api-tema.md`)
Votos não valem como prova. Fatos com link, abertos em 2026-11-20:
- Shopify Payments não lista o Brasil; Basic cobra 2% extra com gateway de terceiro (help.shopify.com/en/manual/payments/shopify-payments/supported-countries; shopify.com/br/precos).
- Nuvem Pago: Pix 0,99%, cartão à vista 4,69% (Começo) e 4,19% (Essencial) + R$ 0,35 (atendimento.nuvemshop.com.br, taxas do Nuvem Pago).
- NF-e no painel da Nuvemshop: só MEI/Simples, IE e certificado A1; custo por nota R$ 0,49 a 1,49 (central Nuvemshop).
- Custo 12 meses (SIMULAÇÃO): Nuvemshop mais barata nos 3 cenários.
- NÃO VERIFICADO: reembolso por API, parcelado/antecipação, plano com código no tema, pixel de compra da Shopify no Basic, regime tributário do João.
Recomendação: Nuvemshop Começo, condicionada a contador e T13d.

## 9. Plano de testes (resumo, ordem)
Sem custo primeiro: T1 a T6 locais (scan, vocabulário, rótulos), T13 plataforma. Só em loja de desenvolvimento: T1 a T9 do Ecommerce. Testes com gasto só após P4 e aprovação.

## 10. Plano de implementação
1. João: "sim" nas decisões abaixo.
2. Cláudio: trocar termos proibidos, criar políticas v2, aplicar diffs de `docs/auditoria.md`.
3. Criar agents Qualidade, Produção, Pesquisa em `agents/`.
4. Ligar 5 rotinas de leitura.
5. João imprime o cupom (destrava P2).
6. Advogado (P3) e loja testada (P4).
7. Só então liga autonomia A/B.

## 11. Decisões do João
Ver `docs/decisoes.md`.
