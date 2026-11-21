# Qualidade: auditoria cruzada dos departamentos

> Revisão 2026-11-20, a pedido do João via Cláudio. PROPOSTA/RELATÓRIO, não política. Tudo local; nenhum arquivo de outro departamento foi editado. `02-segredo.md` não foi aberto.
> Base: `agents/_contexto-base.md` (regra de verificação: link + data; sem fonte oficial lida = NÃO VERIFICADO; consenso entre agentes não é prova) e `docs/operacao/qualidade_scan.py` rodado em todo o repo hoje.

## 0. Como medi, e o que isto NÃO prova
- **Scan** (`python3 -I docs/operacao/qualidade_scan.py .`): termos proibidos, metadado, números sem rótulo. Resultado do repo inteiro: `BLOQUEIO 17 | REVISAR 13 | ALERTA 29 | INFO 461`, código de saída 2. Os 17 bloqueios são os mesmos de antes (nenhum foi corrigido ainda): `loja/seo-produto.md` (4), `loja/estado-loja.md` (3), `loja/atendimento-respostas.md` (5), `marketing-teste/calendario-4-semanas.md` (5). Os 4 PNG agora estão **sem** chunk C2PA (conferi chunk a chunk: 0 `caBX` em 4/4; ver `qualidade.md` §9). O MP4 `video_v2` segue com `hyperframes_version`/`hyperframes_renderer`.
- **Números sem rótulo e afirmação sem fonte**: contagem por heurística (script de rascunho, fora do repo) + leitura manual de amostras. A heurística acusa falso positivo (exemplo de golpe "reembolse R$ 400" é contraexemplo, não número do negócio). Os números abaixo são **candidatos**, e cada veredito diz se conferi à mão.
- **Não reverifiquei** os links dos outros departamentos; contei presença de link e data. Quem diz "FATO, lido hoje" não foi reaberto por mim.
- **Regra de verificação**: foi adicionada ao contexto-base **depois** dos docs de 12:39 a 12:42 (arquivos dos departamentos) e dos T13 de ~19:07 a 19:17 (esses já nascem com a regra). Cobrar retroativamente "NÃO VERIFICADO na primeira linha" seria injusto; cobro o que dava pra cumprir (link, data, rótulo de incerteza, não promover hipótese).
- Auditoria de mim mesma (Qualidade): feita, mas conflito de interesse: quem confere é Documentação (§5).

## 1. Quadro por departamento

Legenda de veredito: **CUMPRE** (rótulos e fontes consistentes), **PARCIAL** (falhas pontuais listadas), **NÃO CUMPRE**.
"Rótulos de incerteza" = ocorrências de *hipótese* + *NÃO VERIFICADO* (indicador, não prova). "Links" = URLs distintas no arquivo.

| Depto (arquivo) | Números sem rótulo (candidatos → real) | Afirmação sem fonte (manual) | Rótulos de incerteza / links / datas | Verificação |
|---|---|---|---|---|
| **Anúncios** (`anuncios.md`, 343 l.) | 14 → **probabilidades "Baixa (10%)" etc. nas linhas 41-43**: a legenda do topo cobre CHUTE, mas a linha não diz; baixo risco. Valores R$ 105/315/42 herdam o CHUTE do `plano-trafego.md` (ok) | **Sim, relevante:** linha 201 compara "R$ 150/semana é **menor** que R$ 315" (taxa semanal x total). Ver §3-A | hip 0, NV 1 / 8 links / 2 datas | **PARCIAL.** Bons links oficiais (Meta, TikTok, Google) e tabela "FATO, lido hoje" (linha 279, não reconferida). Mas gerou o conflito de verba por conta própria e a "3 semanas" nasceu aqui como hipótese |
| **Atendimento** (`atendimento.md`, 333 l.) | 4 → 0 reais (R$ 400 e R$ 50/90/91/200 são casos de teste; R$ 90 é proposta rotulada) | Prazos legais ("caduca em 30 dias", linha 210) com link do CDC no corpo, mas sem trecho citado | hip **0**, NV **0** / 10 links / 2 datas | **PARCIAL.** Nenhum "não sei" em 333 linhas. Incerteza só aparece como SIMULAÇÃO. Recomendação de reembolso R$ 0 diverge do playbook (R$ 90) com motivo declarado (bom) |
| **Ecommerce/Loja** (`ecommerce.md`, 296 l.) | 0 | Sem achado. "Rate limit Shopify e escopos Nuvemshop não confirmados" (linha 289) declarado | hip 13, NV 1 / 10 links / 9 datas | **CUMPRE** (melhor do grupo em honestidade de lacuna). É o doc que mais apontou divergências reais (preço 0 x 89,90, handle, rosca) |
| **Gestão** (`gestao.md` + `t13-*`) | gestão 0; `t13-custos` 26 → tabelas de taxa por cenário (taxas = fonte oficial, volumes = SIMULAÇÃO declarada no topo); `t13-fiscal` 1; `t13-plataformas` 1 | `gestao.md:18` "remote origin = github.com/faixapretabr/fp (FATO)": **conferi, é verdade** (`git remote -v`). Isso reabre a pendência "repo privado?" | gestão: hip 6, NV 3, 15 datas; T13: NV 2 a 12 por arquivo, 5 a 15 links | **CUMPRE** nos T13 (trecho literal, limite do WebFetch declarado, NÃO VERIFICADO explícito). `t13-custos` apresenta taxas sem repetir a fonte por linha: reconferir contra `t13-fiscal-taxas` |
| **Inteligência** (`inteligencia.md`) | 1 → 0 (R$ 25 é exemplo INCORRETO) | Trata `faixapreta.shop` como "dono desconhecido" (`pesquisa/dominio-perfis.md`). **A base do Drive (FP_BASE 02 e 09) diz que o .shop foi registrado na Hostinger e apontado para a Nuvemshop em 14/11, com titularidade a confirmar pelo João.** Inteligência não usou a base | hip 3, NV **15** / 13 links / 10 datas | **PARCIAL.** Melhor disciplina de rótulo (N1 a N4), mas ignorou fonte interna que resolve a dúvida |
| **Jurídico** (`juridico.md`) | 0 | Marca "FATO hoje" na garantia (art. 26, II) com link do Planalto; `juridico-parecer-previo.md` ainda diz "de memória" em parte. **Não reabri o texto da lei.** `juridico.md:63` afirma que `politicas-rascunho.md` não tem seção de garantia: **conferi, é verdade** | hip 4, NV 0 / 15 links / 3 datas | **PARCIAL.** Fontes primárias em abundância, mas "FATO hoje" sem trecho citado e advogado humano ainda ausente (P3) |
| **Marketing** (`marketing.md`) | 2 → 0 (horário "8h" de legenda) | "v2 ainda varia o objeto" é fato do repo; claims de ferramenta (HyperFrames) têm link e "Não comprovado: determinismo frame a frame" (linha 313) | hip 0, NV 1 / 10 links / 5 datas | **CUMPRE com ressalva:** declara limite do que não testou, mas `calendario-4-semanas.md` e `copy-final.md` (peças antigas dele) ainda têm "rosca" e lema em caixa alta |
| **Produto** (`produto.md`) | 4 → 0 (tolerâncias ±0,5% de critério) | Sem achado (tudo aponta pra arquivo do repo) | hip 0, NV 0 / 7 links / 3 datas | **CUMPRE** (fonte é o próprio repo; links de CadQuery/Bambu). Lacuna: não responde se os termos do segredo poderiam ser hasheados para eu conferir (pedido em `qualidade.md` §4.4) |
| **CONSOLIDADO** (Cláudio) | 1 | **Várias (§3):** "R$ 315 em 3 semanas" como fato; "garantia 7 dias" sem link; cita `loja/politicas-v2-rascunho.md` que **não existe** (conferi) | hip 1, NV 1 / **0 links** / **0 datas** | **NÃO CUMPRE.** Resume sem fonte; contradiz a regra "consenso não é prova". Foi o ponto onde hipótese virou fato |
| **Qualidade** (`qualidade.md`) | 0 reais | **Sim, minhas:** (a) tratei "/collections/mesa-oculta" como fato (era hipótese); (b) "quase todos prazo legal" veio de amostra, não de varredura; (c) citei resumo do WebFetch como se fosse literal; (d) repeti "tampa de rosca" 6 vezes. Corrigidos na reescrita | hip 8, NV 4 / 9 links / 3 datas | **PARCIAL** (antes da revisão). Autoauditoria, ver §5 |
| **loja/ e marketing-teste/** (rascunhos pré-rodada) | `wireframe-mobile.html` 4 → CSS, falso positivo | "tampa de rosca" em 5 lugares do rascunho público; `plano-trafego.md:135` "impressora própria" | n/a | Peças públicas em potencial; nada corrigido ainda (decisão 6 da fila do João) |

## 2. Achados do scan por departamento (zona pública: o que bloqueia)

| Arquivo | Regra | Linhas | Nota |
|---|---|---|---|
| `loja/seo-produto.md` | P2 (sugere mecanismo) | 4, 8, 22, 36 | descrição, meta description, alt text, JSON-LD. Dono: Loja/SEO |
| `loja/estado-loja.md` | P1, P2 | 7, 12, 31 | "tampa de rosca", coleção "Mesa (oculta)", "cupom da rosca". Dono: Loja |
| `marketing-teste/calendario-4-semanas.md` | P2 + falso positivo "ocultar" | 36, 87 (P2); 114, 122, 133 (moderação, FP) | Dono: Social/Marketing |
| `loja/atendimento-respostas.md` | P1/P2 | 102, 105, 165, 191, 198 | 191 e 198 são a pergunta do cliente (aceitável); 102/105 mencionam rosca ao cliente (revisar) |
| `marketing-teste/video_v2_RENDER.mp4` | M4 | n/a | tags de ferramenta; remover só no arquivo final real |
| `README.md` | P3/T4 | 5, 9, 28 | "com um segredo" é a tese da marca, mas **o remote existe** e a privacidade do repo segue não confirmada |
Zona OPERACAO (`docs/operacao/*.md`): só INFO (listas de "evitar" e contraexemplos), 461 no total do repo. Maiores volumes: `qualidade.md` 74, `juridico.md` 47, `ecommerce.md` 32, `atendimento.md` 25, `anuncios.md` 21, `marketing.md` 20, `gestao.md` 18, `produto.md` 14. Volume alto = doc que lista muito o proibido, não vazamento. **Vazamento do segredo propriamente dito: não detectado**, com o limite de eu não conhecer o vocabulário do mecanismo.
**Risco agregado (não é grep):** 8 arquivos listam o que "não mostrar" (base, fundo, emenda, juntas, interior, peça virada, "abre embaixo?"): `qualidade.md` 4, `revisao.md` 2, `plano-trafego.md` 2, `marketing.md` 2, `video_v2_notas.md`, `calendario`, `juridico.md`, `anuncios.md`. Juntos formam um mapa do que o mecanismo **não** é. Quem sabe se bate é o Produto/João. Recomendo concentrar essa lista em um arquivo só.

## 3. Hipótese promovida a fato (propagação rastreada)

**A. "Teste Meta de R$ 315 em 3 semanas" e o "conflito" de verba**
1. `marketing-teste/plano-trafego.md:33-34`: ~R$ 105 por criativo (2,5x o CAC máx. de R$ 42, CHUTE) x 3 criativos = **~R$ 315 no total**. **Sem duração.**
2. `anuncios.md:201`: "R$ 150/semana é **menor** que ~R$ 315 ... ou o teste dura ~3 semanas". Compara taxa semanal com total, e **"3 semanas" entra como possibilidade**.
3. `CONSOLIDADO.md:33`: "~R$ 315 em 3 semanas ... vs R$ 150/semana. Decisão aberta."
4. `docs/decisoes.md` #8: "Teto de teste de anúncio: R$ 315 em 3 semanas, sem subir verba": **duração virou fato** e o item pede "Sim" ao João.
Leitura correta com os números do repo: R$ 315 total. Com teto de R$ 150/semana, o teste cabe em ~2,1 semanas (315 / 150); com R$ 15/dia por campanha (`anuncios.md:197`) são R$ 105/semana, abaixo do teto. **Não há conflito de números:** há um total de teste e um teto semanal que são grandezas diferentes. O que falta é o João decidir o total e o teto (nível C). Tudo isso é CHUTE (herdado). A linha 8 de `decisoes.md` precisa trocar "em 3 semanas" por "total, duração livre sob teto semanal".

**B. "Impressora própria"**: `plano-trafego.md:135` e `anuncios.md:173` tratam a produção como impressora própria. A base 09 do Drive diz que **a pendência é do João** ("confirmar se há A1 mini própria ou se a produção fica no fornecedor") e que o [04] foi enviado a fornecedor externo. O CONTEXTO diz "nada impresso". Sem fonte: **NÃO VERIFICADO**.

**C. "Garantia 7 dias"**: `CONSOLIDADO.md:43,47` fala em "garantia errada nas políticas (7 dias vs 30/90)". Conferido: `politicas-rascunho.md` **não tem seção de garantia**; a linha 15 diz "Produto com defeito ... até 7 dias corridos (SIMULAÇÃO)" e o arrependimento (art. 49) é 7 dias. O erro real é **confundir defeito com arrependimento**, não "garantia de 7 dias" (Jurídico descreve certo em `juridico.md:63`). E `loja/politicas-v2-rascunho.md` citado no consolidado **não existe**. Prazos 30/90 do CDC: link no Jurídico, texto da lei **não reaberto por mim** (hipótese até o advogado).

**D. "Dono do .shop desconhecido"**: ver quadro, Inteligência. A base 02/09 resolve em parte (registrado em 14/11 pela operação, titularidade a confirmar).

## 4. Contradições entre documentos

| Tema | Doc A | Doc B | Situação | Quem decide |
|---|---|---|---|---|
| **Preço** | R$ 89,90 (SIMULAÇÃO): `simulacao-preco-frete.md`, `estado-loja.md:6`, `plano-trafego.md` | R$ 0,00 no produto draft: `pendencias.md`, `ecommerce.md:72`, `CONSOLIDADO.md:49` | Não é erro: 0,00 é rascunho. Risco: o 89,90 virar fato (toda a verba e o CAC derivam dele) | João (nível C) |
| **Garantia/defeito** | `politicas-rascunho.md:15`: defeito em 7 dias (SIMULAÇÃO) | CDC (Jurídico, de memória/link): 30 dias para sanar, 90 de garantia legal durável | Rascunho confunde defeito com arrependimento. Corrigir só com Jurídico (+ advogado P3) | Jurídico → João |
| **Handle do produto** | `ecommerce.md:11`: `porta-lapis` (no Shopify) | `seo-produto.md:9`: `porta-lapis-preto-3d` | Aberta. Handle muda URL e SEO | João/Loja |
| **Handle social/domínio** | `pesquisa/dominio-perfis.md`: .shop "ocupado, dono desconhecido"; `faixapretabr.com.br` "aparenta livre" | Drive 02/09: .shop é o domínio da marca, registrado na Hostinger, titularidade a confirmar | Fontes divergem; só o João confirma o titular | João |
| **"Tampa de rosca"** | Proibida: `ecommerce.md:64`, `marketing.md:185`, `gestao.md:95`, `decisoes.md` #6 | Ainda no ar nos rascunhos: `seo-produto.md:4,8,22,36`, `estado-loja.md:7` | Regra concordada, correção **não feita**. Nada foi aplicado na loja | João aprova (decisão 6); Loja executa |
| **Teto de verba** | Playbook/decisoes #3: R$ 150/semana | decisoes #8 / CONSOLIDADO: R$ 315 "em 3 semanas" | Falso conflito (§3-A). Duas decisões distintas misturadas | João |
| **Reembolso solo** | Playbook/decisoes #3: R$ 90 | `atendimento.md:332`: recomenda R$ 0 por 30 dias | Divergência declarada e justificada. Pendente | João |
| **Impressora** | `plano-trafego.md:135`, `anuncios.md:173`: própria | Drive 09: a confirmar; [04] externo | Sem fonte (§3-B) | João |
| **Plataforma** | Repo: loja Shopify em rascunho | Drive 09: decisão Shopify x Nuvemshop pendente (fila do João, item 2); DNS na Nuvemshop | T13 em curso; sem decisão | João |
| **Lema em caixa alta** | `revisao.md`: minúsculo e pequeno | Drive 02-MARCA: lema em sentence case; títulos em caixa alta | Regra é de posição/volume, não de caixa. Dúvida de tom | João |
| **Nome do produto** | "porta-lápis" (repo) | "porta-canetas" (Drive) | Já levantado em `auditoria.md`; segue aberto | João |
| **Quem publica** | Drive 09 (15/11): palavra do Cláudio vale como a do João, inclusive publicar | `CLAUDE.md`/playbook: publicar só com João e portões P1 a P4 | Conflito de regra; vale a mais restritiva até o João decidir | João |

## 5. Quem descumpriu mais, e o que cobrar

Critério: hipótese virando fato + falta de fonte + propagação. **Não é ranking de esforço.**
1. **CONSOLIDADO (Cláudio)**: 0 links, 0 datas, 3 afirmações sem fonte ou inexistentes (duração "3 semanas", "garantia 7 dias", arquivo v2 que não existe). O erro já foi reconhecido pela gerência; falta refazer com fonte por linha.
2. **Anúncios**: originou a comparação inválida da verba e a "3 semanas"; "impressora própria" sem fonte. Pontos fortes: links oficiais e limites honestos de ferramenta.
3. **Atendimento**: nenhum marcador de incerteza em 333 linhas; recomendações fortes sem NÃO VERIFICADO.
4. **Inteligência**: melhor rotulagem do grupo, mas desconsiderou a base do Drive sobre o domínio.
5. **Qualidade (eu)**: quatro falhas minhas listadas no quadro e corrigidas em `qualidade.md`.
Cumprem melhor: **Ecommerce** e **Gestão (T13)**.

**Como a Qualidade fica confiável (conflito de interesse):** esta auditoria foi feita por quem escreveu `qualidade.md` e o scan. Proposta: Documentação confere os números do §1; Produto confere a cobertura do hash (§4.4 de `qualidade.md`); o Cláudio não confere (é parte). Até lá, os vereditos acima são **do fiscalizador, ainda não conferidos por outro**.

## 6. Para o Cláudio (nada aplicado)
1. Corrigir `decisoes.md` #8 ("em 3 semanas") e o consolidado (§3-A, §3-C), com fonte por linha.
2. Decidir quem refaz `CONSOLIDADO.md` com link e data por afirmação.
3. Mandar Loja/SEO limpar "tampa de rosca", "oculta", "cupom da rosca" quando o João disser "grava" (decisão 6); Qualidade reconfere por hash.
4. Levar ao João: titularidade do `.shop`, impressora própria ou fornecedor, handle do produto, quem publica (§4).
5. Concentrar numa só lista a regra "não mostrar", fora dos docs que atendimento e anúncios leem.
