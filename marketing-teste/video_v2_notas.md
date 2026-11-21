# Vídeo v2 (HyperFrames): notas (RENDER)

Arquivo: `video_v2_RENDER.mp4`. 1080x1920, 30 fps, 18 s, H.264, sem áudio, 15,4 MB. Local e gratuito. Nada publicado. Projeto-fonte fora do repo (scratchpad da sessão); o roteiro é o v2 de `revisao.md`.

## O que tem
5 planos com as fotos RENDER (mesa, tampa solta, mão usando, close do corpo, peça sozinha no cinza), fusões de 0,5 s e empurrão lento de câmera. Texto: "segunda, 7h40" (0,6-3,8 s), "tudo no lugar" (9-12 s), "faixa preta" (16-18 s). Sans fina (Inter 400), branca, sem sombra, minúscula; a frase final é pequena (28 px). Nenhum plano mostra base ou fundo. "NADA É SÓ O QUE PARECE" fora do vídeo. Marca d'água "render / simulação" fina e discreta o tempo todo (honestidade de render).

## v1 (ffmpeg) vs v2 (HyperFrames)
| | v1 | v2 |
|---|---|---|
| Duração | 22 s (fora de 15-20) | 18 s |
| Texto | serifa com sombra grossa, caixa alta | sans fina, sem sombra, minúscula |
| Fecho | "NADA É SÓ O QUE PARECE" | "faixa preta" pequeno |
| Teaser "Nada demais" | sim | removido |
| Consistência do objeto | 3 objetos diferentes | ainda varia (fotos 1/2 altas com rosca; 3 e 4 curtas) |
| Áudio | nenhum | nenhum |
| Render | rápido | 58 s (captura por screenshot, GPU por software) |

Limite que continua: são fotos paradas com zoom, não filmagem. A inconsistência do objeto vem das fotos, não da ferramenta. Só a peça real filmada resolve.

## Nota HyperFrames
7/10 pra este uso. Pontos bons: timeline determinística, `check` útil (pegou contraste, tamanho de texto, hold da frase final), CLI simples, saída limpa. Pontos fracos: o linter empurra pra sub-composições (7 avisos de estrutura, ignorados aqui por ser vídeo curto); o render caiu em modo screenshot (sem chrome-headless-shell), mais lento; ainda precisa de CDN jsdelivr pro GSAP (rede no render/preview); o corte por fusão com Ken Burns é básico, mesmo resultado que ffmpeg faria. Valor real aparece com texto animado e edição frequente; pra 5 fotos, ffmpeg dava quase igual.

## Avisos do check que aceitei de propósito
- Contraste 2,22:1 (branco fino sem sombra sobre fundo claro): é o estilo discreto pedido. Risco real de leitura em tela de celular com sol. Alternativa: escurecer levemente a base das fotos no trecho do texto.
- Marca d'água 22 px (abaixo do piso de 28): é textura, intencional.
- "faixa preta" fica 1,83 s (pede 2 s): trocar por 2 s é fácil.
- Sem som: pedido era sem áudio ou trilha grátis e local; nenhuma trilha livre local disponível aqui.

## Licença (heygen-com/hyperframes)
LICENSE do repo: Apache 2.0 (texto padrão, lido em raw.githubusercontent.com, branch main). Permite uso comercial, modificação e distribuição; exige manter aviso de licença/atribuição ao redistribuir o código (não ao publicar vídeos). Vídeos renderizados são seus. Ressalvas: (1) licença cobre o código do repo; a CLI usa telemetria (beacon, opt-out disponível); (2) GSAP tem licença própria da Webflow (gratuita, inclusive comercial, não é open source OSI); (3) fotos são renders de IA nossos. Não é conselho jurídico; vale conferir termos do GSAP antes de escalar.

## Pendente (humano)
Aprovar antes de qualquer uso. Não postar: é RENDER e o roteiro v2 pede peça real filmada.
