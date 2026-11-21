# Auditoria do repo (2026-11-20)

Agent Documentação. Só leitura + este arquivo. Nada existente foi editado. Nada commitado.
Base: `git ls-files` (45 arquivos) + não rastreados: `agents/juridico.md`, `docs/plano-simulacao.md`, `loja/` (4 .md), `marketing-teste/` (copy-final, revisao, 4 PNG, 1 MP4), `produtos/organizador-mesa/ficha-cupom.md`, `modelo-de-entrega.md`. `CLAUDE.md` está modificado (seção "Arquitetura") e ainda não commitado.

## 1. Links quebrados
Conferi todo caminho entre crases em todos os `.md`. Nenhum link real quebrado.
Falsos positivos (não precisa corrigir):
- `CLAUDE.md` cita `atendimento.md`, `documentacao.md`, `loja.md` sem prefixo `agents/` (ambíguo, mas existem). Sugestão: usar `agents/loja.md` etc.
- `README.md` cita `materiais-3d.md` (existe em `pesquisa/`).
- `produtos/organizador-mesa/README.md` cita `_v2.py`, `_v3.py`, `_v5.py` e `preview*.html` abreviados (existem).
- `modelo-de-entrega.md` cita `final/ficha-producao.md`: pasta `final/` ainda não existe, é o esperado (só nasce após 2º portão).
- `docs/plano-simulacao.md` lista saídas futuras (`conferencia.md`, `seo-produto.md`, `estado-loja.md`, `concorrentes.md`, `dominio-perfis.md`, `analise-processo.md`, `video_v2_RENDER.mp4`, `calendario-4-semanas.md`, `atendimento-respostas.md`) que ainda não existem. Normal, é rascunho de rodada.

## 2. Docs desatualizados (fato = arquivo no repo)
| Onde | Problema | Evidência |
|---|---|---|
| `README.md` | Estrutura não lista `loja/`, `marketing-teste/`, `docs/plano-simulacao.md`. Agents sem Jurídico. Status ignora loja e marketing de teste | `ls` |
| `CLAUDE.md` | Estrutura sem `loja/`, `marketing-teste/`; agents sem `juridico.md`. `src/` "(a criar)" segue verdadeiro | `ls` |
| `CLAUDE.md` | Seção "Arquitetura" nova está só no disco (não commitada). OK, mas confirmar que o João quer | `git status` |
| `docs/CONTEXTO.md` | "Loja: toda desconfigurada, auditoria ainda não feita" está velho: a loja foi resetada e há rascunho (produto Porta-lápis draft R$ 0,00, coleção "Mesa (oculta)", páginas Sobre e FAQ e Trocas não publicadas) | `loja/pendencias.md` |
| `docs/CONTEXTO.md` | Não cita Jurídico, `loja/`, `marketing-teste/`, preço simulado, HyperFrames | grep |
| `docs/CONTEXTO.md` | "Marketing: nada executado" está velho: há 4 renders de foto + 1 vídeo v1 (reprovado), `copy-final.md`, `revisao.md` | `marketing-teste/` |
| `docs/CONTEXTO.md` | Pendência "questão jurídica" não aponta `loja/juridico-checklist.md` | arquivo |
| `docs/CONTEXTO.md` | Mapa dos agents sem Jurídico | `agents/juridico.md` |
| `agents/README.md` | Lista de agents sem `juridico.md` | `ls agents` |
| `produtos/README.md` | Estrutura do produto sem `01b-demanda-br.md`, `parametros-impressao.md`, `ficha-cupom.md`, `modelo-de-entrega.md`, `preview/`. Fala "porta-lápis" (ok) | `ls` |
| `produtos/organizador-mesa/README.md` | Índice sem `ficha-cupom.md` e `modelo-de-entrega.md` (novos) | `ls` |
| `produtos/organizador-mesa/README.md` / `03-validacao.md` | Dizem que a validação/cupom usa `tampa_v4.stl`, mas a vigente é v5. Já explicado no README; checar se `ficha-cupom.md` resolve | leitura |
| `agents/documentacao.md` | Escopo cita "agents e pastas que existem" mas não menciona `loja/` e `marketing-teste/` como pastas de trabalho | leitura |

HyperFrames: aparece só nas skills do ambiente e em `docs/plano-simulacao.md` (tarefa 4). Nenhum `.md` de `agents/marketing/video.md` ou CONTEXTO diz que é a ferramenta de vídeo. Se for decisão, registrar.

## 3. Contradições
1. **Produto: "porta-lápis" x "porta-canetas duplo" (Drive).** Dentro do repo não achei "porta-canetas duplo" em lugar nenhum; o repo é coerente: "porta-lápis" (arquivos, README, loja, Shopify). Só `01b-demanda-br.md` fala "porta-caneta" como concorrente (pneu F1). Não consegui conferir o Drive aqui (leitura externa fora do escopo). Hipótese: o Drive tem nome antigo ou outro produto. **Escalar pro João.**
2. **Domínio.** Repo não fixa domínio. Só existe `faixapretabr.myshopify.com` (CONTEXTO) e a tarefa 11 do plano checa `faixapreta.shop`/`.com.br` (nada registrado). `loja/pendencias.md` diz "Domínio próprio" como pendência. Sem contradição, mas nenhum arquivo é dono do dado. Sugestão: uma linha no CONTEXTO "domínio: _(a definir)_, `faixapretabr.myshopify.com` é provisório".
3. **Preço.** `loja/simulacao-preco-frete.md` diz R$ 89,90 (SIMULAÇÃO, tudo CHUTE). `loja/pendencias.md` diz produto no Shopify a R$ 0,00. Não é contradição (R$ 0,00 é rascunho), mas precisa de nota: preço de verdade é pendência do João. Cuidado pra o 89,90 não virar "fato" em outro doc.
4. **Tampa vigente.** README do produto: tampa v5. `03-validacao.md` ainda avalia tampa v4. Já sinalizado no README; manter.
5. **Hook de commit x "nunca commitar".** `plano-simulacao.md` (tarefa 13) cita conflito. Em `CLAUDE.md` e `.vscode/settings.json` não achei hook. Provável hook de ambiente (fora do repo). Escalar.
6. **Imagens de teste.** `marketing-teste/revisao.md` diz que as 4 fotos mostram objetos de proporção diferente. Não é contradição de doc, é risco: não usar como "foto do produto" na loja.
7. **Segredo.** Jurídico e marketing trabalham só com "objeto com compartimento". Conferi `loja/` e `marketing-teste/` por vazamento: só aparece "tampa de rosca" (descrição pública discreta, `loja/estado-loja.md`) e "objeto com compartimento" (genérico). O mecanismo em si (`02-segredo.md`) não aparece. Atenção: "tampa de rosca" na página pública é decisão de copy pro João aprovar. Obs.: `loja/atendimento-respostas.md` e `loja/estado-loja.md` surgiram durante a auditoria (outros agents da rodada) e não foram revisados a fundo.

## 4. STL sem script
Nenhum. Todos os 22 STL saem de algum script:
- v1: `base_v1`, `corpo_v1`, `montado_v1` ← `porta-lapis_v1.py`
- v2: `corpo_v2`, `tampa_v2`, `montado_v2`, `corpo_v2b_80x150`, `montado_v2b_80x150` ← `porta-lapis_v2.py`
- v3/v4: `tampa_v3`, `tampa_v4`, `corpo_v3_lisa/canelura/aneis`, `corpo_v4_canelura_80x150` ← `porta-lapis_v3.py`
- `tampa_v5` ← `porta-lapis_v5.py`; `cupom_anel_v4` ← `cupom_rosca_v4.py`
Obs.: `porta-lapis_v1.py` e `_v2.py` não estão no bloco "Comandos" do CLAUDE.md (são histórico, ok). Os STL são estimativas: nenhum foi impresso.

## 5. Outros achados
- `.gitignore` cobre `__pycache__/` e `*.pyc`. `marketing-teste/` tem PNG e MP4 (binários): decidir se entram no git (peso) ou ficam ignorados.
- `src/` "(a criar)": segue verdadeiro.
- Dados de cliente: nenhum encontrado.
- O repo GitHub ser privado segue sem confirmação (pendência antiga). Como agora há `loja/` com rascunho de CNPJ/LGPD (sem dado real), o risco subiu um pouco.

## 6. Diffs propostos (só texto, não aplicados)

### docs/CONTEXTO.md
```diff
-Última atualização: 2026-11-20. Fato = confirmado no repo ou dito pelo humano. O resto leva marca.
+Última atualização: 2026-11-20 (pós-simulação). Fato = confirmado no repo ou dito pelo humano. O resto leva marca.
@@ Mapa dos agents
 | Atendimento | `agents/atendimento.md` | dúvidas de cliente |
+| Jurídico | `agents/juridico.md` | rascunhos e riscos legais da loja. Não substitui advogado |
 | Documentação | `agents/documentacao.md` | mantém os `.md` verdadeiros |
@@ Estado atual por frente
-- **Loja Shopify:** a conta existe. ... Segundo o humano está toda desconfigurada. A auditoria só de leitura ainda não foi feita.
+- **Loja Shopify:** conta `faixapretabr.myshopify.com` (provisório), plano Basic, BRL. A loja foi resetada e subiu só rascunho: produto Porta-lápis (draft, R$ 0,00, sem estoque), coleção "Mesa (oculta)", páginas Sobre e FAQ e Trocas, nada publicado. Gateway, frete, impostos e domínio não configurados. Pendências em `loja/pendencias.md`.
+- **Preço e frete (SIMULAÇÃO):** R$ 89,90 e tabela de frete por região são chute pra teste (`loja/simulacao-preco-frete.md`). Não é decisão. Preço real: pendência do João.
-- **Marketing:** departamento criado (agents definidos). Nada executado.
+- **Marketing:** departamento criado. Teste interno em `marketing-teste/`: 4 fotos RENDER (aprovadas só como referência), vídeo TikTok v1 reprovado (22 s), `copy-final.md` e `revisao.md`. Vídeo feito com HyperFrames _(a confirmar como ferramenta oficial)_. Nada publicado. Peças são render, não o produto real.
+- **Jurídico:** agent definido. Rascunhos em `loja/politicas-rascunho.md` e `loja/juridico-checklist.md`, marcados "REVISAR COM JURÍDICO". Sem advogado humano ainda.
@@ Pendências de negócio
-- Questão jurídica no Brasil (venda de objeto com compartimento). Ver `produtos/organizador-mesa/01b-demanda-br.md`.
+- Questão jurídica no Brasil (venda de objeto com compartimento). Ver `01b-demanda-br.md` e `loja/juridico-checklist.md`.
-- Preço, frete, política de troca: não definidos.
+- Preço, frete, política de troca: não definidos (só simulados).
+- Domínio próprio: _(a definir)_.
+- Nome do produto: confirmar "porta-lápis" x o nome no Drive.
@@ Índice
-`README.md` (raiz), `CLAUDE.md`, `agents/README.md`, `produtos/README.md`, `pesquisa/materiais-3d.md`.
+`README.md` (raiz), `CLAUDE.md`, `agents/README.md`, `produtos/README.md`, `pesquisa/materiais-3d.md`, `loja/pendencias.md`, `docs/plano-simulacao.md`, `docs/auditoria.md`.
```

### README.md
```diff
-- `agents/`: agents autônomos (atendimento, documentação, loja Shopify e os departamentos de Produto e Marketing)
+- `agents/`: agents autônomos (atendimento, documentação, jurídico, loja Shopify e os departamentos de Produto e Marketing)
+- `loja/`: rascunhos da loja Shopify (pendências, políticas, jurídico, simulação de preço)
+- `marketing-teste/`: peças de teste em render e revisão de marca. Nada publicado
+- `docs/`: ficha de retomada, plano de simulação, auditoria
@@ Status
-🚧 Em construção. Primeiro produto ... Detalhes no README da pasta.
+🚧 Em construção. Primeiro produto (`produtos/organizador-mesa/`) em modelagem, ainda sem protótipo impresso nem aprovação final. Loja em rascunho (nada publicado, preço simulado). Detalhes em `docs/CONTEXTO.md`.
```

### CLAUDE.md
```diff
-- `agents/` — definições dos agents autônomos (`atendimento.md`, `documentacao.md`, `loja.md`, `produto/` = Produto, `marketing/` = Marketing e Conteúdo)
+- `agents/` — definições dos agents autônomos (`agents/atendimento.md`, `agents/documentacao.md`, `agents/juridico.md`, `agents/loja.md`, `produto/` = Produto, `marketing/` = Marketing e Conteúdo)
 - `produtos/` — um produto por pasta (hoje: `organizador-mesa/`). Conteúdo interno
+- `loja/` — rascunhos da loja Shopify (pendências, políticas, jurídico, simulação de preço)
+- `marketing-teste/` — peças de teste em render e revisão. Não são o produto real
 - `pesquisa/` — pesquisas de apoio (ex.: materiais 3D)
```
Obs.: a seção "Arquitetura" nova do CLAUDE.md está coerente com os scripts (v5 carrega v3 via `importlib`; conferi a lista de STL). Nada a corrigir.

## 7. Decisões pro João
1. Nome do produto: "porta-lápis" (repo) x "porta-canetas duplo" (Drive). Recomendo manter "porta-lápis" no repo e corrigir o Drive, até haver segundo produto.
2. Binários de `marketing-teste/` (PNG e MP4): recomendo não commitar (adicionar ao `.gitignore`) até decidir quais peças ficam.
