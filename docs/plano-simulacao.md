# Plano de simulação: todos os agents ao mesmo tempo

Rascunho. Rodada única, em paralelo. Regras valem pra todos: tudo local, nada de commit/push, nada de publicar, pagar ou gastar, segredo do produto nunca aparece fora de `produtos/`, saída em arquivo novo e relatório de no máximo 10 linhas.

| # | Agent | Tarefa | Saída |
|---|---|---|---|
| 1 | Modelagem | Rodar `porta-lapis_v3.py v4`, `porta-lapis_v5.py` e `cupom_rosca_v4.py` (CadQuery), conferir medidas dos STL (80x150, rosca, folga 0,4) | `produtos/organizador-mesa/modelo/conferencia.md` |
| 2 | Validação | Ficha de impressão do cupom: orientação, camada, suporte, o que medir depois | `produtos/organizador-mesa/ficha-cupom.md` |
| 3 | Copy | Fechar legendas e roteiro v2 do TikTok pelo checklist de marca (sem teaser forçado) | `marketing-teste/copy-final.md` |
| 4 | Vídeo (HyperFrames) | Renderizar o TikTok v2 de 15-20 s, vertical, marcado RENDER, usando as fotos de teste | `marketing-teste/video_v2_RENDER.mp4` |
| 5 | SEO | Ficha da página do produto (título, meta, alt, JSON-LD), vocabulário sem termos proibidos | `loja/seo-produto.md` |
| 6 | Social | Calendário de 4 semanas em rascunho, 9:16 primeiro | `marketing-teste/calendario-4-semanas.md` |
| 7 | Atendimento | FAQ e respostas prontas (prazo, troca, arrependimento) usando as políticas simuladas | `loja/atendimento-respostas.md` |
| 8 | Loja | Montar produto, coleção e páginas em rascunho completos (descrição, SEO, variante); só leitura de frete e pagamento | relatório + `loja/estado-loja.md` |
| 9 | Jurídico | Ler o Decreto 10.030/2019 inteiro e fechar o checklist pro advogado | `loja/juridico-checklist.md` (atualizado) |
| 10 | Pesquisa: concorrentes | 5 concorrentes de objeto 3D "comum com função extra": preço, tom, canais, o que fazem de bom | `pesquisa/concorrentes.md` |
| 11 | Pesquisa: domínio e nome | Checar disponibilidade de `faixapreta.shop`/`.com.br` e de perfis (só consulta, não registrar nada) | `pesquisa/dominio-perfis.md` |
| 12 | Documentação | Auditar o repo: links quebrados, docs desatualizados, `CONTEXTO.md` fiel ao estado atual | `docs/auditoria.md` |
| 13 | Coordenação (processo) | Analisar a nossa forma de trabalhar: o que gastou token à toa, onde travou, regras que conflitam (ex.: hook de commit x regra "não commitar"), propor 5 melhorias | `docs/analise-processo.md` |

## Depois da rodada
- Eu junto os 13 relatórios e levo ao João no máximo 3 decisões, com recomendação.
- Medir: tempo total, tokens por agent, quantas tarefas fecharam sem retrabalho.

## Fica de fora (precisa do João)
- Commit/push, publicar loja, ativar pagamento, anúncio, registrar domínio, advogado, imprimir peça.
