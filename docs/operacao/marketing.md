# Operação do departamento Marketing e Conteúdo

PROPOSTA. Não é política aprovada; só vale o que o João gravar. Tudo local: nada publicado, agendado, gasto ou commitado. `produtos/organizador-mesa/02-segredo.md` não foi aberto.
Rótulos: FATO (página oficial lida em 2026-11-20, com link e trecho) | HIPÓTESE | SIMULAÇÃO (número chutado) | NÃO VERIFICADO | `[REAL]` (caso do repo) | `[SIMULADO]` (exemplo inventado pra treino, não é fato nem peça).
Limite do método: o WebFetch resume a página com modelo pequeno. Os trechos abaixo são do resumo, não cópia literal; número crítico se reconfere na tela da fonte antes de implementar.

## Revisão 2026-11-20 (após cobrança do Cláudio)
| O que estava errado | O que mudou |
|---|---|
| Listas de "o que não mostrar" (base, fundo, emenda, peça virada) e um exemplo de comentário com termo do mecanismo: somadas, viram mapa de onde olhar (alerta Q6 em `qualidade.md`) | Removi as enumerações e o exemplo. O doc remete à "lista de zonas restritas" mantida só pelo Produto, sem dizer quais são |
| R$ 89,90 e "entrega em 5 dias" apareciam sem rótulo em exemplo | Rotulados SIMULAÇÃO; prazo e garantia ficam "não definido" |
| Fontes sem trecho; afirmações sobre ferramentas sem separar o que foi lido do que foi suposto | Cada fonte agora tem link, data, trecho resumido e rótulo; o que não li está NÃO VERIFICADO |
| Seção 3.5 repetia `copy-final.md`; checklists repetiam itens; seção 8 tinha item "Teto" sem sentido | Duplicação cortada; 3.5 só aponta o arquivo; item removido |
| Faltava: metadado C2PA nos renders, voto de plataforma de loja (pixel), conflitos com outros deptos | Incluídos (9.4, 9.5 e fim do doc) |
| T8 assumia perfil privado publicável por API | Marcado NÃO VERIFICADO |

---

## 1. Contexto operacional e quem depende de nós
**Estado (FATO do repo, `CONTEXTO.md`):** nada impresso; sem 2º portão; loja desconfigurada; preço, frete, troca e prazos indefinidos; parecer jurídico (P3) e loja/pagamento testados (P4) pendentes. Marketing "só começa a executar com produto validado e loja pronta". Todo material de `marketing-teste/` é RENDER de IA e rascunho. Hoje quem redige também revisa a marca (`revisao.md`): é o buraco que a seção 8 fecha.

| Quem | Depende de Marketing pra | Marketing depende dele pra |
|---|---|---|
| João | Marca viva sem queimar o diferencial; decidir publicar | Toda aprovação |
| Cláudio | Consolidar; subir no máx. 3 decisões/ciclo | Fila `docs/decisoes.md` |
| Produto | Não ver o mecanismo vazar por imagem, vídeo ou comentário | Peça validada (P2); lista de zonas restritas |
| Loja / Atendimento | Copy, foto, SEO, respostas-base | Loja pronta (P4); prazos e política (indefinidos) |
| Jurídico | Claims e peças pra revisar | Parecer (P3) |
| Qualidade (`docs/operacao/qualidade.md`, agent ainda não criado) | Peça pra conferir | Existir como agente separado |

## 2. Riscos específicos
Prob. e impacto são HIPÓTESE (julgamento sem histórico), pra a fase atual (sem peça real, loja ou conta ativa).

| # | Risco | Como acontece aqui | Prob. | Impacto | Mitigação |
|---|---|---|---|---|---|
| R1 | Conteúdo incorreto publicado | Render como foto real; legenda de outra peça; v1 reprovado subido; versão errada agendada | M | A | Cartão de peça com origem e versão; só `aprovado/` publica |
| R2 | Informação comercial não comprovada | Preço, frete, prazo, garantia, "grátis", "esgotado", seguidores, resistência/material sem teste | A | A | Só claim com fonte do repo; "não definido" = não dizer |
| R3 | Vazamento do segredo (imagem, vídeo, legenda, alt, nome de arquivo, metadado, transcrição, legenda automática, comentário) | Ângulo ou detalhe em zona restrita; resposta que confirma; nome ou texto alternativo descritivo; transcrição automática | M | Crítico | Checklist 5, grep, dois olhares independentes, resposta neutra única |
| R4 | Uso indevido da marca | Conta falsa; marca quase igual (`faixapretabr`/`faixapreta3d.com.br`, INPI não consultado); domínio `faixapreta.shop` sem dono confirmado; parceiro usando logo; música ou fonte sem licença | M | M a A | Reserva de handle com aprovação; consulta INPI pelo João/Jurídico; registro de licenças |
| R5 | Render como produto real | Fotos 1 a 4 e `video_v2_RENDER.mp4` são IA e o objeto muda de proporção. Os PNGs trazem manifesto C2PA de IA, segundo `qualidade.md` (NÃO VERIFICADO por mim) | M | A | Marca d'água; bloqueio até peça filmada; rótulo de IA da plataforma; não remover metadado |
| R6 | Depoimento, avaliação ou número inventado | Agent "completa" prova social; simulações têm cifras chutadas | B a M | A | Cifra com fonte ou SIMULAÇÃO; depoimento só de cliente real com consentimento escrito |
| R7 | Automação publica sozinha | Conector ou rotina mal escrita agenda/posta | B hoje, M depois | Crítico | Ferramentas de publicação fora das rotinas até "grava" (seção 7) |
| R8 | Dado de cliente/comentarista vai pra ferramenta externa | Transcrever DM; análise de sentimento; lista pro Descript/OpusClip | B | A | Regra do CLAUDE.md; lista de ferramentas permitidas |
| R9 | Golpe por DM/comentário | Falso suporte, parceria, código de verificação | M | A (perda de conta) | Seção 4 |
| R10 | Restrição de plataforma | Termo sensível em anúncio; automação | M | M | Vocabulário controlado; humano antes de anúncio |
| R11 | Vazamento por ferramenta externa | Projeto subido ao Descript, OpusClip, Figma, cloud render | B | A | Só peça aprovada e sem segredo sobe |

## 3. Biblioteca DO / DON'T
Regra mãe: sugerir, não entregar. A peça tem que funcionar como "um porta-lápis" pra quem não sabe e não dar apoio a quem tenta deduzir. Lista de termos proibidos: `marketing-teste/revisao.md`.

| Tema | CORRETO | INCORRETO |
|---|---|---|
| Vídeo | `[REAL]` v2: 18 s, "segunda, 7h40", sans fina branca sem sombra, minúscula, fecho "faixa preta" pequeno (`video_v2_notas.md`) | `[REAL]` v1 reprovado: 22 s, serifa com sombra, 3 objetos diferentes, "Nada demais", fecho em caixa alta (`revisao.md`) |
| Enquadramento | `[REAL]` só os planos do roteiro v2 | `[SIMULADO]` plano fora do roteiro "pra mostrar o acabamento" ou ruído de mecanismo; qualquer plano em zona restrita do Produto |
| Frase final | `[REAL]` "faixa preta" minúsculo, 2 s; lema em caixa alta só na bio do Instagram (decisão pendente do João) | `[REAL]` "NADA É SÓ O QUE PARECE" em caixa alta no último plano; `[SIMULADO]` lema repetido em legenda, story e anúncio |
| Teaser | `[REAL]` "segunda, 7h40", "mesa de manhã", "janela, caneca, caderno" | `[REAL]` "Nada demais"; `[SIMULADO]` "Parece normal, né?", "Só os curiosos percebem" |
| Fotos com proporção variável | `[REAL]` fotos 1 e 2 em `referencia/`, aprovadas só como referência; `[SIMULADO]` medir a peça real e conferir altura e rosca em todas as fotos de um post | `[REAL]` carrossel misturando fotos 1 a 4 (alta com rosca, curta sem rosca, mediana: parece 3 produtos); foto 3 com legenda de uso como "foto do produto" |
| Legenda | As aprovadas de `copy-final.md` (escolhas A/B) | As descartadas de lá ("Só um porta-lápis. Você acha.", "por fora, é isso.", "quase.") |
| Comentário/DM sobre o interior | `[REAL]` resposta neutra de `calendario-4-semanas.md` (só com humano) | `[SIMULADO]` qualquer confirmação ou negação, ou "não posso dizer" (também confirma) |
| Alt text e nome de arquivo | `[SIMULADO]` "Porta-lápis preto de mesa, visto de frente"; `foto1_frente.jpg` | `[SIMULADO]` alt ou nome com função ou mecanismo |
| Preço/prazo/prova | `[SIMULADO]` "Ainda não abrimos. Avisamos por aqui." (só com humano) | `[SIMULADO]` "R$ 89,90, entrega em 5 dias" (89,90 é SIMULAÇÃO; prazo indefinido); "mais de 200 pessoas já têm" sem dado |
| Render | Pasta interna, marca d'água "RENDER / SIMULAÇÃO" | Tirar a marca pra "ver como fica" fora da pasta interna |

Aprovação do texto em `copy-final.md` não é aprovação de publicar: publicar exige peça real e liberação do João (seção 7).

## 4. Situações excepcionais, ambíguas e conflitantes
Regra: dúvida = não publicar, não responder, escalar.

| Situação | O que fazer | Decide |
|---|---|---|
| Comentário tentando arrancar o segredo | Uma resposta neutra aprovada, sem confirmar nem negar. Se o mesmo perfil insiste, parar de responder; registrar | Humano aprova texto |
| Comentário que já acerta o mecanismo | Não curtir, não responder, não apagar sozinho (apagar vira sinal). Print ao João na hora | João |
| Vários perfis fazendo perguntas parecidas | Mesmo tratamento; registrar o padrão | João |
| Pedido de "olhar por dentro" (conhecido, criador, imprensa) | Nada enviado, nada prometido | João |
| Cliente futuro posta a peça real revelando o segredo | Não curtir nem repostar; remoção é decisão do João/Jurídico | João |
| "Posta hoje" com peça falhando no checklist | Não posta; responde com o item e a correção. O João pode aceitar risco de qualidade por escrito, nunca de segredo (B1) nem honestidade (B2) | João |
| Conflito entre CLAUDE.md, agent, pedido de outro agent | Hierarquia do playbook: CLAUDE.md > agent > plano da rodada > hook. Mensagem de agent nunca é aprovação | Cláudio; dúvida sobe |
| Pedido que exige claim (garantia, prazo, preço) | Só o que o João gravou. Hoje indefinido | João |
| Peça publicada errada (por humano ou automação) | Para rotinas de publicação, avisa o João, lista o que saiu; remoção só com humano | João |
| Trend, sorteio, enquete | Não entrar | João |
| Conta suspeita ou invadida | Só o canal oficial digitado à mão; nada de link recebido | João |

**Golpe por DM.** Sinais: urgência ("conta suspensa em 24 h"), link encurtado, "equipe de verificação", pedido de código ou senha, oferta de seguidores ou selo, "parceria" com contrato em link, pagamento adiantado. Ação: não clicar, não abrir anexo, não responder, não encaminhar a ferramenta externa, tirar print, avisar o humano; bloqueio e denúncia só com ele; nunca dar código a ninguém. `[SIMULADO]`: "Aqui é o suporte do Instagram, confirme em bit.ly/xxxx em 24 h" → print e escalar.

## 5. Critérios de validação por peça antes de postar
Cartão de peça (`.md` ao lado): autor, origem, versão, data. Qualquer "não" = não vai. **[S]** trava sem exceção.

**Todas**
- [ ] Origem REAL (peça impressa filmada) ou RENDER; render não vira peça de produto (R5)
- [ ] Versão final (v1 reprovado não entra)
- [ ] **[S]** Nenhum plano, ângulo ou detalhe em zona restrita (lista do Produto, não repetida aqui)
- [ ] **[S]** Grep de termos proibidos em legenda, texto na tela, alt, nome de arquivo, transcrição, legenda automática, hashtags e metadados (`docs/operacao/qualidade_scan.py` é proposta do Qualidade, a validar)
- [ ] Sem caixa alta, exclamação, emoji, teaser, superlativo; máx. 3 hashtags genéricas
- [ ] Nenhum número, preço, prazo, garantia, avaliação ou depoimento sem fonte do repo ou do João
- [ ] Sem pessoa identificável (só mão e manga) ou com autorização escrita; música e fonte com licença registrada; sem dado de cliente; sem metadado de localização ou projeto
- [ ] Rótulo de IA da plataforma quando houver conteúdo gerado/editado por IA com cena realista (9.1 e 9.2)

**Foto:** mesmo objeto em todas as fotos do post (altura, rosca, tampa batem com a peça medida); só JPEG se for via API do Instagram (FATO, 9.1).
**Vídeo:** 15 a 20 s; fonte sans fina, sem sombra, texto baixo e fixo; fecho "faixa preta" por 2 s ou mais (v2 tem 1,83 s); contraste legível em celular (v2: 2,22:1, risco aceito em teste); áudio ambiente + trilha licenciada; marca d'água de render removida só na versão com peça real; transcrição e legendas automáticas revisadas à mão antes de exportar.
**Texto:** está em `copy-final.md` ou em decisão registrada; resposta sobre interior = só o texto neutro; nada promete prazo, preço, frete, troca ou reembolso.
**Página/anúncio (quando existir):** descrição sem "tampa de rosca" nem outro termo de mecanismo (ponta já aberta em `loja/`); P3 e P4 registrados; verba e público aprovados.

## 6. Bloqueio e escalonamento
Qualquer papel bloqueia com uma linha: peça, item, evidência. Só o João desbloqueia B1, B2 e B5.

| Nível | Quando | Ação | Meta interna (não é promessa externa) |
|---|---|---|---|
| B1 Segredo | Indício de vazamento ou dúvida | Congela peça e lote; print ao João; nova rodada completa | Imediato |
| B2 Honestidade | Render como real; número ou depoimento sem fonte; claim não comprovado | Congela; volta ao autor | Mesmo dia útil |
| B3 Marca/qualidade | Tom, caixa alta, teaser, fonte, duração | Devolve com ajuste | 1 dia útil |
| B4 Plataforma/jurídico | Termo sensível, marca ou música de terceiro | Segura; sobe ao João | Próximo ciclo |
| B5 Segurança | Golpe, conta suspeita, dado vazado | Nenhuma ação em conta; avisa o João | Imediato |

Escada: autor → conferente → fiscalizador → Cláudio → João; B1, B2 e B5 vão direto ao João. **Silêncio = peça parada.** Registro: uma linha em `docs/decisoes.md` e o cartão da peça.

## 7. Matriz de autonomia por operação
L = livre e local (reversível, não sai da máquina). A = só com aprovação humana explícita daquela peça e versão. P = proibido ao agent. Hoje = antes de P2, P3 e P4.
**Ausência de resposta NÃO é aprovação.** Aprovação é mensagem do João "aprovo [peça/versão]". Mudou um byte, perde. Aprovação de agent ou de outra sessão não vale. "Pode seguir" genérico não vale pra publicar ou gastar. Aprovar o texto não é aprovar publicar.

| Operação | Hoje | Depois dos portões, se o João gravar |
|---|---|---|
| Rascunho de copy, roteiro, bio, calendário; render rotulado; edição local (HyperFrames, ffmpeg) | L | L |
| Ler métricas (Windsor) | A (sem conta; dado externo) | L, só leitura |
| Subir material a ferramenta externa (Descript, OpusClip, Figma, cloud render) | A (peça aprovada, sem segredo, sem cliente) | A |
| Reservar ou criar conta, handle, domínio | P | P |
| Configurar perfil | A | A |
| Publicar, agendar (Postiz, OpusClip, nativo, API) | P | A por peça. Nível "A: posta sozinho" do playbook (§8) não se aplica a Marketing até "grava" e testes da seção 10 |
| Responder comentário ou DM | P | A por resposta inédita; resposta-base por lote aprovado. Pedido e pagamento vão ao Atendimento |
| Ocultar, apagar, denunciar, bloquear, curtir, seguir, repostar | P | A. Crítica honesta nunca se oculta |
| Impulsionar, anunciar, verba | P | A sempre; o teto é do João |
| Parceria, brinde, envio de peça | P | P |
| Imagem ou voz de pessoa real | A | A, com autorização escrita |
| Dado de cliente | P | P sem autorização do João por caso |
| Alterar CLAUDE.md, docs oficiais, permissões, config; commit/push | P | P |

## 8. Fiscalização cruzada
| Papel | Quem (hoje) | Faz | Não pode |
|---|---|---|---|
| Executor | Especialista (Copy, Social, Vídeo, Web, SEO, Tráfego) | Produz a peça e o cartão com a fonte de cada claim | Conferir a própria peça |
| Conferente | Outro especialista do depto, rodando a seção 5 | Marca cada item com evidência (frame, linha) | Ter escrito ou editado a peça |
| Fiscalizador | Agent Qualidade (a criar). Enquanto não existir: Coordenação de Marketing por amostragem + grep, com a fraqueza dita | Revê o conferente, reconfere 1 em cada 3 peças já postadas e os comentários | Ter executado ou conferido |
| Liberador | João | Aprova a peça específica e a publicação; liga e desliga rotinas de publicação | Delegar a agent |

Regras: (1) segredo exige dois olhares com métodos diferentes (um quadro a quadro, outro em texto, metadado e transcrição); dois agents com o mesmo prompt contam como um; (2) se só houver um agent, a conferência vira humana; (3) trilha por peça: quem executou, conferiu, fiscalizou, versão, hora, mensagem do João; sem trilha a peça não existe; (4) Cláudio consolida e não substitui nenhum dos quatro.

## 9. Inventário e fontes oficiais (consulta 2026-11-20, WebFetch)

### 9.1 Instagram / Meta, Content Publishing
Fontes: https://developers.facebook.com/docs/instagram-platform/content-publishing e https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/content-publishing
| Afirmação | Rótulo | Trecho |
|---|---|---|
| Só conta profissional; sem PPA concluído pode não publicar | FATO | página cobre "Instagram professional accounts"; Página com PPA "can't publish until PPA is complete" |
| Permissões `instagram_content_publish` (Facebook) ou `instagram_business_content_publish` (Instagram Login); acesso Standard ou Advanced | FATO | tabela de permissões |
| Fluxo: `POST /<IG_ID>/media`, depois `/media_publish`; `GET /<IG_ID>/content_publishing_limit` mostra o uso | FATO | seção Endpoints |
| Imagem única só JPEG; Reels (`REELS`), carrossel até 20, Stories | FATO | "JPEG only"; "up to 20" |
| Mídia em servidor público no momento de publicar; sem tags de compra nem filtros; `alt_text` só em imagem | FATO | seção Limitations |
| `is_ai_generated=true` marca conteúdo de IA (no carrossel, só no container) | FATO | seção AI-generated label |
| Limite de posts por API em 24 h | **conflito na própria doc** | uma seção diz 100, a de carrossel diz 50: NÃO VERIFICADO qual vale; medir com `content_publishing_limit` |
| Duração, proporção e tamanho de vídeo; prazo de App Review; efeito no alcance; política de anúncios | NÃO VERIFICADO | a página não lista |

### 9.2 TikTok, Content Posting API e regras
Fontes: https://developers.tiktok.com/doc/content-posting-api-get-started, https://developers.tiktok.com/doc/content-posting-api-reference-direct-post, https://developers.tiktok.com/doc/content-sharing-guidelines, https://www.tiktok.com/community-guidelines/en/integrity-authenticity
| Afirmação | Rótulo | Trecho |
|---|---|---|
| Direct Post exige app registrado, produto Content Posting API, Direct Post habilitado, escopo `video.publish` aprovado, autorização do usuário | FATO | seção Requirements |
| Cliente sem auditoria só posta privado | FATO | "All content posted by unaudited clients will be restricted to private viewing mode"; erro `unaudited_client_can_only_post_to_private_accounts` |
| 6 requisições por minuto por token; existe teto diário de posts e cota de usuários ativos | FATO (números do teto diário: NÃO VERIFICADO) | `spam_risk_too_many_posts`, `reached_active_user_cap` |
| Upload MP4, QuickTime, WebM; tamanho e duração máximos | formatos FATO; limites NÃO VERIFICADO | estão em outra página |
| Usuário escolhe a privacidade sem padrão; prévia; consentimento antes de enviar; toggle comercial desligado por padrão (rótulos "Promotional content", "Paid partnership"); app não pode pôr marca d'água ou logo promocional | FATO | Content Sharing Guidelines |
| Rotular conteúdo gerado ou muito editado por IA com cena realista; sem rótulo pode ser removido, restrito ou rotulado; automação que contorna sistemas, engajamento falso e personificação são proibidos | FATO | Community Guidelines, "we require creators to label AI-generated or significantly edited content" |
| Uma rotina autônoma poder postar no TikTok | NÃO VERIFICADO | Caminho seguro: João posta manualmente |

### 9.3 HyperFrames
Fontes: https://github.com/heygen-com/hyperframes, https://hyperframes.heygen.com/introduction, https://hyperframes.heygen.com/faq
| Afirmação | Rótulo | Trecho |
|---|---|---|
| Open source, Apache 2.0; HTML/CSS/mídia → MP4 | FATO | página do repo |
| Requer Node.js 22+ e FFmpeg; `npx hyperframes doctor` checa a máquina | FATO | repo e FAQ |
| Render local mantém o projeto na máquina; cloud render e conector sobem o projeto à HeyGen | FATO | FAQ, Network use |
| CLI envia telemetria de uso e "never sends project names or video content"; desligar com `npx hyperframes telemetry disable` | FATO (a página do repo não cita telemetria; vale o FAQ) | FAQ |
| Mídia que adicionamos (fonte, música) mantém a licença própria | FATO | FAQ |
| Render determinístico frame a frame | NÃO VERIFICADO | a intro afirma, o FAQ não confirma; só o teste T7 responde |
| Depende de rede no render | NÃO VERIFICADO | `video_v2_notas.md` registra uso de CDN para o GSAP; termos do GSAP não conferidos |

Regra interna proposta: render sempre local, telemetria desligada, sem cloud render de material sensível.

### 9.4 Políticas de plataforma, anúncios, loja e Brasil
| Item | Estado |
|---|---|
| Meta Community Standards (https://transparency.meta.com/policies/community-standards/) | FATO só do índice: seções Spam, Misinformation, Third-Party IP, Authentic Identity Representation, Account Integrity, Inauthentic Behavior, Prohibited Commercial Practices. Conteúdo das seções NÃO LIDO. A página diz valer pra conteúdo de IA |
| Política de comércio e anúncios da Meta | NÃO VERIFICADO: a URL tentada (`/policies/commerce-policies/`) deu 404; link morto |
| Política de anúncios do TikTok | NÃO VERIFICADO: não consultada |
| Pixel de compra da loja | Nuvemshop: FATO, evento Purchase, inclusive por API de Conversões (https://atendimento.nuvemshop.com.br/pt_BR/pixel-do-facebook/quais-eventos-a-nuvemshop-envia-para-o-pixel-e-como-eles-funcionam, 2026-11-20, via `t13-plataformas.md`, não reaberta por mim). Shopify: NÃO VERIFICADO. Voto de plataforma é do João; resumo em `t13-plataformas.md` |
| CDC, CONAR, publicidade e "publi" | NÃO VERIFICADO por Marketing; ver `juridico.md`. Nada afirmado sobre legalidade |

### 9.5 Inventário de ferramentas
Fonte do inventário: `agents/marketing/*.md` e a lista de ferramentas do ambiente (FATO de que existem; capacidade e permissão reais: NÃO VERIFICADO).
| Ferramenta | Uso declarado | Risco | Estado |
|---|---|---|---|
| Windsor.ai | Métricas (leitura) | Dado sai a terceiro | Não testado; sem conta social |
| Postiz | Agendamento | Agenda e publica | Não testado; fora das rotinas até "grava" |
| OpusClip | Cortes; o ambiente expõe também ferramentas de agendar e publicar | Agenda, publica, sobe vídeo | Não testado; só corte, sem conta conectada |
| Descript, Picsart, Figma | Edição, motion, design | Material em serviço externo; transcrição | Não testado |
| TikTok for Business | Campanha (leitura e rascunho) | Criar campanha gasta | Só leitura |
| HyperFrames | Montagem local | CDN, telemetria | Rodou uma vez (v2, nota 7/10 em `video_v2_notas.md`) |
| ffmpeg | Montagem v1 | nenhum especial | Rodou |

## 10. Plano de testes
Material fictício, sem peça nem segredo; conta de teste privada e liberação do João a cada passo que sai da máquina. Nenhum teste publica, agenda ou gasta sem ele.

| # | Teste | Aprovação | Sucesso |
|---|---|---|---|
| T1 | Grep de termos proibidos, com caso positivo plantado fora do repo | Não | Acha o plantado |
| T2 | Checklist 5 sobre as 5 peças de `marketing-teste/` | Não | Bate com `revisao.md` (v1 reprovado, 3 e 4 com ressalva, v2 não publicável) |
| T3 | `ffprobe`/`exiftool` nos arquivos | Não | Sem metadado sensível; registrar o C2PA dos PNGs |
| T4 | Silêncio: peça sem resposta | Não | Fica parada |
| T5 | Conflito: "posta hoje" com checklist falho | Não | Bloqueia e cita o item |
| T6 | 10 casos `[SIMULADOS]` de comentário-caça e golpe, só em rascunho | Não | 10/10 sem confirmar ou negar; golpe nunca clicado |
| T7 | HyperFrames: renderizar 2 vezes, comparar hash dos frames; testar sem rede e com telemetria desligada | Não | Hash igual ou dependência anotada |
| T8 | Instagram API em conta profissional de teste: 1 JPEG fictício, ler `content_publishing_limit` (50 ou 100?), testar `is_ai_generated`. Se conta privada pode publicar por API: NÃO VERIFICADO | João cria a conta | Número real e comportamento documentados |
| T9 | TikTok: 1 post manual fictício em conta de teste privada, conferir rótulo de IA; sem pedir acesso à API | João | Rótulo entendido; decisão sobre auditoria registrada |
| T10 | Confirmar (leitura) que Postiz, OpusClip e TikTok não têm conta ligada e nenhuma rotina os chama | João liga conectores | Zero conta conectada |
| T11 | Rodada com peça `[SIMULADA]` e erro plantado, conferente e fiscalizador separados | Não | Pelo menos um pega; se nenhum, rever método |
| T12 | Com cupom e peça real: refazer T2 e T11 e refilmar o v2 | João (P2) | Seção 5 verde; só então propor a 1ª postagem |

Ordem: T1 a T7 e T11 já (locais); T8 a T10 com decisão do João; T12 depende do cupom impresso.

---

## Conflitos com outros departamentos (listados, não editados)
| # | Conflito | Onde | Quem resolve |
|---|---|---|---|
| 1 | Preço: R$ 0,00 em `loja/pendencias.md` x 89.90 na loja (SIMULAÇÃO) | `docs/operacao/ecommerce.md` itens 1 e 5 | Loja/João |
| 2 | Handle: `porta-lapis` na loja x `porta-lapis-preto-3d` em `loja/seo-produto.md` | `ecommerce.md` item 2 | Loja/SEO |
| 3 | "tampa de rosca" na descrição pública do rascunho e em `loja/seo-produto.md` (título, meta, alt, JSON-LD) | `ecommerce.md`, `anuncios.md` T2, playbook | Loja/Qualidade; ver também termo "rosca" |
| 4 | Defeito "em até 7 dias" em `loja/politicas-rascunho.md` x CDC 90 dias (aparente) e 30 para sanar; 7 dias é só arrependimento | `juridico.md` caso A | Jurídico/João |
| 5 | Teto semanal R$ 150 (playbook) x teste Meta de ~R$ 315 | `anuncios.md` linha 201 | João |
| 6 | Limite de 100 x 50 posts por API: contradição interna da doc da Meta, não de depto | 9.1 | Teste T8 |
| 7 | Lista de "não mostrar" em vários docs forma mapa de inferência (Q6) | `qualidade.md`, `anuncios.md`, `revisao.md` | Produto/Qualidade; o meu doc já não enumera |

## Pendências do João
Lema na bio do Instagram e "tudo no lugar" puro (decisões 1 e 2 de `copy-final.md`): sem resposta = não decidido. Gravar qualquer coisa deste arquivo exige "grava". Nada aqui altera CLAUDE.md, playbook, agents ou configuração.
