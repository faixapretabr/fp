# Contexto: ficha de retomada

Pra quem chega do zero (outro dispositivo, outro Claude). O contexto vem só do repo.
Última atualização: 2026-11-20. Fato = confirmado no repo ou dito pelo humano. O resto leva marca.

## O que é
Faixa Preta: objetos comuns e cotidianos com um segredo. Produção por impressão 3D. Marca discreta, curiosa, cúmplice. Lema: "NADA É SÓ O QUE PARECE". Operada por agents de IA; vender, publicar e pagar só com aprovação humana. Regras completas no `CLAUDE.md`.

## Regras de trabalho do humano (valem pra qualquer Claude neste repo)
- Português do Brasil, tom informal e direto.
- Ser proativo: sugerir melhorias sem esperar pedido.
- SEMPRE terminar propondo o próximo passo.
- Nunca commitar nem dar push sem o humano pedir.
- Só mexer no que foi pedido. Alterar vários arquivos existentes: perguntar antes.
- Mudança pequena: mostrar só o diff.
- Segredo do produto fica só em `produtos/<nome>/`. Fora dali, só se sugere.

## Mapa dos agents
| Frente | Onde | Papel |
|---|---|---|
| Produto | `agents/produto/` | do objeto ao STL final (seleção, segredo, modelagem, validação, entrega) |
| Marketing e Conteúdo | `agents/marketing/` | coordenação, social, tráfego, copy, vídeo, web design, SEO |
| Loja | `agents/loja.md` | loja Shopify (catálogo, tema, pedidos, dados) |
| Atendimento | `agents/atendimento.md` | dúvidas de cliente |
| Documentação | `agents/documentacao.md` | mantém os `.md` verdadeiros |

## Estado atual por frente
- **Produto (organizador-mesa):** corpo v4 + tampa v5 (oca) + cupom da rosca. Nada impresso ainda. O cupom aguarda impressão. A v6 depende do resultado do cupom. 2º portão humano pendente. Detalhes: `produtos/organizador-mesa/README.md`.
- **Loja Shopify:** a conta existe. Nome "Faixa Preta", `faixapretabr.myshopify.com`, plano Basic, moeda BRL, Brasil. Segundo o humano está toda desconfigurada. A auditoria só de leitura ainda não foi feita.
- **Marketing:** departamento criado (agents definidos). Nada executado.
- **Atendimento:** agent definido. Prazos em aberto (ver pendências).
- **Documentação:** agent definido; faz auditoria do repo.

## Decisões já tomadas pelo humano (organizador-mesa)
- Material PETG, bico 0,6 mm (definido em 2026-11-20).
- Formato 80x150 mm, caneluras verticais, sem divisórias.
- Suporte só dentro da cavidade (teto plano).
- Tampa oca (v5), folga da rosca 0,4 mm, cor preta, 2 peças.
- Regras de modelagem que vêm do bico 0,6: paredes em múltiplos de ~0,6 mm, folga de rosca mínima 0,4 mm, camada 0,2 a 0,3 mm, evitar pontes longas. Ver `produtos/organizador-mesa/parametros-impressao.md`.
- Duas aprovações humanas antes de produção (depois da seleção e depois da validação).

## Pendências de negócio (só o humano responde)
- Prazos do atendimento (entrega, resposta de reembolso): `_(a definir)_`.
- Mecanismo escolhido registrado em `produtos/organizador-mesa/02-segredo.md`.
- O repo no GitHub é privado? Não confirmado. A pasta `produtos/` é interna.
- Questão jurídica no Brasil (venda de objeto com compartimento). Ver `produtos/organizador-mesa/01b-demanda-br.md`.
- Preço, frete, política de troca: não definidos.

## Como rodar os scripts
Precisa de CadQuery (`pip install cadquery`). De dentro de `produtos/organizador-mesa/modelo/`:
- `python porta-lapis_v3.py v4`: corpo v4 e tampa v4.
- `python porta-lapis_v5.py`: tampa v5.
- `python cupom_rosca_v4.py`: anel do cupom.
Os STL saem na mesma pasta. Preview: `produtos/organizador-mesa/preview/preview-v4.html`.

## Próximos passos, em ordem
1. Imprimir o cupom (anel + tampa) e registrar o resultado em `03-validacao.md`.
2. Ajustar a folga da rosca (v6 se precisar) conforme o cupom.
3. Protótipo do corpo inteiro (ponte de 62 mm com suporte). Depois 2º portão humano e `final/`.
4. Loja: auditoria só de leitura (agent Loja) e arrumar a configuração, com aprovação.
5. Humano fecha as pendências de negócio acima.
6. Marketing só começa a executar com produto validado e loja pronta.

## Índice
`README.md` (raiz), `CLAUDE.md`, `agents/README.md`, `produtos/README.md`, `pesquisa/materiais-3d.md`.
