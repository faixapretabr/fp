# Arquitetura operacional: Jurídico e Compliance

> PROPOSTA, não política aprovada. Versão revisada em 2026-11-20. O Jurídico redige e sinaliza risco; NÃO substitui advogado humano e NÃO dá parecer final.
> Tudo local. Nada publicado, enviado ou commitado. Não li `02-segredo.md`: o Jurídico só conhece "objeto com compartimento".
> Rótulos: **FATO** = texto oficial lido em 2026-11-20 (link na seção 9); **HIPÓTESE** = estimativa ou leitura minha; **DE MEMÓRIA** = não lido, advogado confere; **NÃO VERIFICADO** = fonte oficial não aberta ou só resumo de terceiro; **SIMULAÇÃO** = número de exemplo.
> Limite do método: o leitor de páginas devolve resumo, não o texto inteiro. "FATO" aqui significa "trecho confirmado pelo resumo da página oficial"; o advogado confere o texto integral.
> Exceção pro grep da Qualidade: este arquivo contém palavras proibidas porque lista o que evitar. É interno.

## Revisão 2026-11-20 (ordem do Cláudio/João)

**O que estava errado na versão anterior**
1. Vários itens saíam como "DE MEMÓRIA" ou "não lido" sem nova tentativa. CONAR (403), ANPD (404), Meta (parcial) e TikTok (só índice) foram reabertos por outra URL oficial e agora têm FATO.
2. Os 10 entregáveis estavam presentes, mas havia duplicação (decisões e relatório repetidos dentro do doc; regra de prazo em 3 lugares) e notas de severidade sem rótulo de HIPÓTESE.
3. Faltava o risco da **plataforma da loja** (NF-e, transferência internacional). Na conversa eu afirmei que a Nuvemshop era "empresa brasileira": isso **não foi verificado** e está retirado. O doc não trazia essa frase; o erro estava na resposta ao Cláudio.
4. Dois votos sobre plataforma (manter Shopify, depois trocar pra Nuvemshop) saíram com fonte parcial. O que vale está na seção 2 (J13), com o que é FATO e o que não é.

**O que mudou**
- Passaram a FATO: CDC art. 26 §§1 a 3 e art. 49 par. único; Resolução CD/ANPD 2/2022 arts. 2, 3, 11 (portal oficial da ANPD); Código CONAR arts. 1, 23, 27; Lei 9.279/1996 arts. 122, 124, 129; política de armas da Meta (página completa); política de produtos perigosos do TikTok (parcial).
- Continua NÃO VERIFICADO: registro.br (página oficial veio vazia; só resultados de busca), Inmetro, Decreto 8.771/2016, Res. CD/ANPD 15/2024 (citada pela ANPD, não lida), cartão e parcelado da Nuvem Pago, hospedagem dos dados das plataformas.
- Removido: relatório executivo e decisões de dentro do doc (ficam no relatório do turno).
- Conflitos com arquivos de outros departamentos: listados na seção 8.4, **não editados**.

---

## 1. Contexto operacional e quem depende de você

**Estado (fato, repo):** nada impresso; loja Shopify em rascunho; marketing só em rascunho; advogado não escolhido; razão social, CNPJ, encarregado indefinidos; prazos, frete e preço são SIMULAÇÃO. P3 (parecer do advogado antes de publicar ou anunciar) é o portão do Jurídico.

| Departamento | Depende do Jurídico pra | Gatilho |
|---|---|---|
| Loja | Termos, troca, privacidade, envio, rodapé com dados do fornecedor, descrição de produto | Antes de publicar |
| Atendimento | Respostas dentro do CDC e da LGPD; o que escalar | Antes de P4 |
| Marketing (copy, social, vídeo, SEO, tráfego) | Palavras proibidas, claims, regras de plataforma, imagem e marca | Antes de cada peça |
| Produto | Alerta se o formato mudar (arma, réplica, parte de arma); aviso de peça pequena | Mudança de formato, P1 |
| Qualidade | Lista de termos proibidos jurídicos | Todo ciclo |
| Finanças / Gestão | Regime tributário, NF-e, prazo de reembolso | Antes do preço final |
| Produção | Defeito de impressão como vício, rastreabilidade | Antes da 1ª venda |
| Dados / Pesquisa | Pixel, coleta, retenção, destino dos dados | Antes do pixel |
| Documentação | Texto jurídico publicado = fonte única | A cada versão |
| João | Decisões de prazo, valor, frete, CNPJ, encarregado, advogado | Lote S/N em `docs/decisoes.md` |

Princípio: o Jurídico é freio com data. Todo bloqueio diz o que trava, por quê, o que destrava e quem decide.

---

## 2. Riscos específicos

Probabilidade (P) e impacto (I) de 1 a 5; score = P x I. **P, I e score são HIPÓTESE (estimativa minha)**, não medição.

| # | Risco | Base | P | I | Score | Controle |
|---|---|---|---|---|---|---|
| J1 | Copy promete "cofre"/proteção ou sugere esconder bens | CDC art. 37 §1 e art. 6 IV (FATO); CONAR art. 27 "apresentação verdadeira" (FATO); Meta/Google/TikTok vedam armas e produtos perigosos (FATO, seção 9) | 4 | 5 | 20 | Lista mestre (3.3) + revisão antes de toda peça |
| J2 | Garantia legal declarada errada | CDC art. 26 I e II (30/90 dias), art. 18 §1 (30 dias pra sanar) (FATO) | 5 | 4 | 20 | Tabela de Prazos (5.1) como fonte única |
| J3 | Política de troca fora do CDC | CDC art. 49 caput e par. único (FATO); Decreto 7.962 art. 5 (FATO); frete de devolução: DE MEMÓRIA | 4 | 4 | 16 | Separar arrependimento de defeito; pergunta 10 |
| J4 | Dado pessoal fora da LGPD | LGPD arts. 6, 7, 9, 18, 33, 41, 48 (FATO); Res. CD/ANPD 2/2022 arts. 2, 3, 11 (FATO) | 4 | 4 | 16 | Controlador definido, canal do titular, aviso de pixel, salvaguarda do art. 33 |
| J5 | Marca parecida / INPI / domínio | Lei 9.279 arts. 124 XIX, 124 XXIII, 129 (FATO); INPI: busca não feita; registro.br NÃO VERIFICADO | 3 | 5 | 15 | Busca de anterioridade antes de investir em vídeo e anúncio |
| J6 | Publicidade enganosa (geral) | CDC arts. 30, 36, 37, 38 (FATO); CONAR arts. 1, 23, 27 (FATO) | 3 | 4 | 12 | Prova guardada; foto fiel à peça real |
| J7 | Omissão relevante (art. 31) por causa da regra "não revelar o segredo" | CDC art. 31 e 37 §3 (FATO) | 3 | 4 | 12 | Ficha técnica verdadeira; pergunta 7 ao advogado; sem frase tipo "é só um porta-lápis" |
| J8 | Regra de plataforma de anúncio | Meta: não promover armas, acessórios, nem instruções de impressão 3D de arma; TikTok: produtos perigosos; Google: produtos perigosos (FATO, seção 9) | 4 | 3 | 12 | Conferir a política na data de cada campanha |
| J9 | Dados do fornecedor ausentes na oferta | Decreto 7.962 art. 2 (FATO) | 4 | 3 | 12 | Só abrir loja com CNPJ e dados |
| J10 | Objeto enquadrado em controle de arma | Decreto 10.030 Anexo I art. 2 e art. 3 par. único III "b" (FATO); Lei 10.826 art. 26 (FATO, via resumo) | 1 | 5 | 5 | Produto avisa mudança de formato; hoje o formato é porta-lápis |
| J11 | Peça pequena / criança | Inmetro: NÃO VERIFICADO; CDC art. 37 §2 (FATO) | 2 | 3 | 6 | Aviso de idade até checar norma |
| J12 | Número SIMULAÇÃO repetido como oferta real | CDC arts. 30 e 35 (FATO) | 3 | 3 | 9 | SIMULAÇÃO nunca vai pra texto publicado |
| J13 | Plataforma da loja: NF-e e transferência internacional | LGPD art. 33 (FATO); NF-e conforme `docs/operacao/t13-fiscal-taxas.md` (abaixo) | 3 | 3 | 9 | Contador e advogado antes de escolher |

**J13 em detalhe (fonte: `t13-fiscal-taxas.md` do dept. Gestão, que usou WebFetch em 2026-11-20; eu **não reabri** essas páginas):**
- Nuvemshop: emite NF-e pelo painel (Configurações > Documentos fiscais > NF-e); só MEI ou Simples Nacional; exige Inscrição Estadual e certificado A1; custo por nota por plano (Começo R$ 1,49 a Next R$ 0,10). Links no t13.
- Shopify: staff disse em 31/08/2021 que NF-e não é nativa (fórum, fonte antiga); há apps de terceiros (Bling, Notasy) na App Store. Não achei, nem o t13, página de ajuda oficial atual.
- **Não sei onde cada plataforma hospeda os dados.** O art. 33 da LGPD (FATO) exige salvaguarda ou consentimento específico se houver transferência internacional. Qual das duas plataformas se aplica: NÃO VERIFICADO. A origem corporativa da Nuvemshop também: NÃO VERIFICADO.
- Opinião do Jurídico (HIPÓTESE): em fiscal a Nuvemshop parece mais simples pra MEI/Simples; isso não vira decisão sem contador (regime, IE, A1). Plataforma é decisão do João (nível C).

---

## 3. Biblioteca DO / DON'T

Etiquetas: **[REAL]** = existe nos arquivos do repo hoje; **[SIMULADO]** = exemplo inventado pra treino. Exemplos INCORRETOS nunca saem do interno.

### 3.1 [REAL] Garantia: 30 dias x 90 dias x "7 dias"
- Origem: `loja/politicas-rascunho.md` ("Produto com defeito: ... em até 7 dias corridos") e `loja/atendimento-respostas.md` bloco 10 (defeito "até 7 dias ... SIMULAÇÃO"). O checklist e o parecer já corrigiram a conta, mas só no papel do Jurídico.
- INCORRETO: "Produto com defeito: fale com a gente em até 7 dias corridos." (confunde arrependimento com vício; o direito de reclamar de vício aparente de durável é 90 dias, art. 26 II, FATO)
- INCORRETO: "Garantia de 30 dias." (30 dias é o prazo pra sanar o vício, art. 18 §1, e o prazo de não durável)
- CORRETO (rascunho, REVISAR COM ADVOGADO): "Você pode desistir da compra em até 7 dias corridos do recebimento. Se o produto chegar com defeito, você tem 90 dias do recebimento pra avisar e temos até 30 dias pra resolver. Se não resolvermos, você escolhe: troca, reembolso ou abatimento no preço."
- Vício oculto: o prazo começa quando o defeito aparece (art. 26 §3, FATO). A reclamação ao fornecedor suspende a contagem (art. 26 §2 I, FATO).
- PERGUNTA: porta-lápis é bem durável? HIPÓTESE: sim.

### 3.2 [SIMULADO] "Frete grátis"
A expressão "frete grátis" **não existe** no repo (busca feita). O caso abaixo é o risco típico de política genérica copiada de modelo.
- INCORRETO: "Frete grátis em todo o Brasil" enquanto a simulação cobra R$ 22 a R$ 42 (SIMULAÇÃO). Oferta vincula (art. 30) e dá direito ao cumprimento (art. 35); o Decreto 7.962 art. 2 exige discriminar custos de entrega (FATO).
- INCORRETO: "Devolução grátis" sem dizer que vale só no arrependimento.
- CORRETO: "Frete: Sudeste R$ 22 [SIMULAÇÃO]. Se desistir em até 7 dias, o frete de devolução é por nossa conta." Promoção de frete só com condição, vigência e aprovação do João.
- "Grátis" no CONAR: busca sugeriu cuidado especial, mas os anexos do Código não foram lidos. NÃO VERIFICADO.

### 3.3 [REAL] Lista mestre de palavras e temas (fonte: parecer prévio seção 3 + regra da marca)
| Categoria | Evitar sempre (copy, legenda, alt text, nome de arquivo, URL, SEO, hashtag, áudio) |
|---|---|
| Ocultação | cofre, esconderijo, esconder, ocultar, camuflado, disfarçado, "ninguém vai ver", "às escondidas" |
| Segurança | à prova de, seguro, proteção, blindado, trava, "guarde com segurança" |
| Itens de valor | joias, dinheiro, documentos, chaves, qualquer item de valor como exemplo |
| Ilícito | droga, arma, munição, "sem a polícia ver", "sem ninguém saber" |
| Mecanismo | como abre, onde fica, termo de construção que sugira função interna |
| Absolutos sem prova | "o melhor", "único", "inquebrável" |
- INCORRETO [SIMULADO]: "Seu porta-lápis tem um esconderijo. Guarde o que ninguém pode ver."
- INCORRETO [SIMULADO]: "À prova de curiosos. Ideal pra joias e dinheiro."
- CORRETO [SIMULADO]: "Porta-lápis 80 x 150 mm, PETG, impresso em 3D, caneluras verticais, preto."
- ATENÇÃO [SIMULADO]: slogan "Quem presta atenção já sabe" ainda pode insinuar função oculta. Risco médio: só vai ao advogado, nunca liberado por mim.
- A lista é mínima. Teste de intenção: "isso sugere guardar algo que não deveria ser visto, ou promete proteção?"

### 3.4 [REAL] Pista do mecanismo na descrição pública
- Playbook §1.6, `loja/estado-loja.md` e `loja/seo-produto.md` usam um termo de construção que sugere mecanismo (título, meta, alt text, JSON-LD). Regra de marca (segredo) e jurídico (J7: revelar demais quebra a marca; omitir demais é art. 31).
- INCORRETO: descrição que detalha como as partes se encaixam.
- CORRETO: dimensões, material, cor, peso, cuidados de limpeza. Detalhe de construção só no manual dentro da caixa, se o João decidir (pergunta 7).

### 3.5 [REAL] Canal e identificação do fornecedor
- `loja/politicas-rascunho.md` usa um Gmail como canal único e deixa controlador e encarregado "[a definir]".
- INCORRETO: publicar assim. Decreto 7.962 art. 2 exige identificação e contato do fornecedor (FATO); LGPD art. 9 exige identidade e contato do controlador e art. 41 manda divulgar o encarregado (FATO).
- CORRETO: razão social, CNPJ, endereço, e-mail institucional, prazo de resposta (SAC em até 5 dias, Decreto 7.962 art. 4 par. único, FATO). Se não houver encarregado: registrar que é agente de pequeno porte e manter o canal (Res. 2/2022 art. 11, FATO), desde que não haja tratamento de alto risco nem receita acima do limite (art. 3, FATO).

### 3.6 Outros pares curtos [SIMULADO]
| Situação | DON'T | DO |
|---|---|---|
| Prazo de entrega | "Chega em 3 dias" | "Estimativa: Sudeste 3 a 5 dias úteis após postagem [SIMULAÇÃO]" |
| Cartão | "Não guardamos nada seu" | "O pagamento é processado pelo gateway; não armazenamos dados de cartão [conferir com o gateway]" |
| Reembolso | "Em até 10 dias" (SIMULAÇÃO publicada como regra) | Só o prazo aprovado pelo João e conferido pelo advogado; lei fala em devolução "de imediato" (art. 49 par. único, FATO) |
| Foto | Render de IA com peça diferente da real | Foto da peça real, ou "imagem ilustrativa" com fidelidade checada |
| Depoimento | Review inventado | Só real e autorizado |

---

## 4. Situações excepcionais, ambíguas e conflitantes

| # | Situação | O que faço | Quem decide |
|---|---|---|---|
| S1 | Regra da marca x art. 31 CDC | Não resolvo. Copy descritiva e verdadeira, risco médio, escalo | Advogado + João |
| S2 | Slogan ambíguo do Marketing | Só passa se não sugerir ocultar nem proteger; dúvida = devolvo com opção segura | Jurídico bloqueia; João pode levar ao advogado |
| S3 | CLAUDE.md x agent x outro departamento | Hierarquia do playbook; lei vale sobre todos | Cláudio informa o João |
| S4 | Dois departamentos com prazo legal diferente | Vale a Tabela 5.1; aviso os dois | Jurídico corrige, Documentação atualiza |
| S5 | Cliente pede reembolso fora do prazo | Não decido. Alerto que pode ser vício (regime diferente) | João |
| S6 | Cliente pergunta se "dá pra esconder X" ou diz que usou pra algo ilícito | Resposta neutra, sem confirmar nem negar mecanismo; escalo; registro o mínimo | João + advogado |
| S7 | Notificação de Procon, plataforma, advogado ou autoridade | Não respondo. Resumo em 5 linhas e marco o prazo do documento | João + advogado (urgente) |
| S8 | Pedido de titular LGPD | Registro a data de entrada; não envio dados sem validar identidade | João (+ advogado) |
| S9 | Plataforma muda política ou reprova anúncio | Pausa e aviso; registro o texto da política na data | Cláudio + João |
| S10 | Fonte oficial bloqueia | Registro o bloqueio, tento outra URL oficial, depois marco NÃO VERIFICADO | Advogado confere |
| S11 | Acesso a fonte varia entre dias (Planalto bloqueou no parecer prévio, abriu hoje) | Registro data e resultado a cada uso; não presumo | Jurídico |
| S12 | Peça de risco médio ou alto e calendário apertado | Não publica; prazo de calendário não libera | João |
| S13 | Produto novo lembra arma, ferramenta ou item controlado | Parada total até advogado (J10) | Advogado |
| S14 | Público infantil ou produto pra criança | Aviso de idade e peça pequena; marketing não mira criança (art. 37 §2, FATO) | João |
| S15 | Dado de cliente iria pra IA externa | Proibido sem autorização; testes só com dado fictício | João |
| S16 | "Aprovado" que não veio do João | Não vale. Só o João, por escrito, em `docs/decisoes.md` ou mensagem direta | Cláudio |
| S17 | João aprova algo que marquei risco alto | Registro o risco aceito por escrito e sugiro advogado; não finjo que está ok | João |
| S18 | Dois votos de plataforma divergem | Vale o fato com link; voto sem fato não conta (regra `_contexto-base.md`) | João |

---

## 5. Critérios de validação e checklist por tipo de documento/peça

### 5.1 Tabela de Prazos Legais (fonte única; só o Jurídico edita)
| Item | Prazo | Base | Status |
|---|---|---|---|
| Arrependimento (compra fora do estabelecimento, inclui online) | 7 dias da assinatura ou do recebimento | CDC art. 49 | FATO |
| Reembolso do arrependimento | "de imediato", com correção monetária | CDC art. 49 par. único | FATO |
| Reclamar de vício aparente, não durável | 30 dias | CDC art. 26 I | FATO |
| Reclamar de vício aparente, durável | 90 dias, da entrega efetiva | CDC art. 26 II e §1 | FATO |
| Vício oculto | começa quando o defeito aparece | CDC art. 26 §3 | FATO |
| Reclamação ao fornecedor suspende a contagem | até resposta negativa clara | CDC art. 26 §2 I | FATO |
| Prazo pra sanar o vício | 30 dias máx.; depois o consumidor escolhe troca, restituição ou abatimento | CDC art. 18 §1 | FATO |
| Resposta do SAC (e-commerce) | 5 dias | Decreto 7.962 art. 4 par. único | FATO |
| Confirmar imediatamente o pedido de arrependimento | imediato | Decreto 7.962 art. 5 §4 | FATO |
| Guarda de registros de acesso (provedor de aplicação) | 6 meses | Marco Civil art. 15 | FATO (se a loja se enquadra: PERGUNTA) |
| Comunicação de incidente | prazo definido pela ANPD; art. 14 II da Res. 2/2022 dá prazo em dobro a pequeno porte, remetendo à Res. CD/ANPD 15/2024 | LGPD art. 48; Res. 2/2022 | FATO (Res. 15/2024 NÃO lida) |
| Frete de devolução no arrependimento | entendimento de que é do fornecedor | jurisprudência | DE MEMÓRIA, PERGUNTA 10 |

### 5.2 Critérios gerais (toda peça e documento)
1. Afirmação factual verdadeira e com prova guardada (CDC arts. 36 e 38).
2. Nada de promessa de segurança ou ocultação (lista mestre 3.3).
3. Prazo legal só da Tabela 5.1.
4. Número comercial aprovado pelo João, ou marcado SIMULAÇÃO e fora de publicação.
5. Fornecedor identificado onde a lei pede.
6. Segredo do produto ausente (Qualidade confere).
7. Fonte com link e data; DE MEMÓRIA e NÃO VERIFICADO marcados.
8. "REVISAR COM JURÍDICO" até advogado e João aprovarem.

### 5.3 Checklists por tipo
**Termos de uso e venda:** identificação do fornecedor; características sem promessa de segurança; preço, frete discriminado, prazos; sumário do contrato antes da contratação e cópia salvável (Decreto 7.962 art. 4); cláusula de uso lícito (redação do advogado); foro e responsabilidade (só advogado).

**Troca, arrependimento, garantia:** arrependimento 7 dias, no mesmo meio da compra, confirmação imediata (Decreto 7.962 art. 5); defeito separado de arrependimento; 90 dias / 30 dias / escolha do consumidor; garantia contratual, se houver, por escrito e complementar (CDC art. 50, FATO); sem prazo menor que o legal disfarçado de "política da loja".

**Privacidade (LGPD):** controlador (art. 9); finalidade, forma e duração (art. 9); base legal por finalidade (art. 7), com consentimento separado pra marketing; direitos e canal (art. 18); compartilhamento (plataforma, gateway, transportadora, pixels); transferência internacional (art. 33); encarregado ou dispensa com canal (Res. 2/2022 art. 11); plano de incidente (art. 48); aviso de cookies e pixels antes de campanha.

**Envio:** prazo de produção e entrega por região como estimativa; frete discriminado antes do pagamento; extravio e avaria (advogado); rastreio.

**Descrição de produto, ficha técnica, SEO:** só dimensões, material, cor, peso, cuidados; nenhum termo de mecanismo; lista mestre passou em meta description, alt text, arquivo, URL e JSON-LD; aviso de peça pequena até checar Inmetro.

**Copy de marketing:** identificável como publicidade (art. 36); lista mestre passou, inclusive áudio, overlay e hashtag; claim com prova guardada; imagem fiel à peça real; sem marca ou pessoa de terceiro sem autorização; regra da plataforma conferida na data; "grátis", desconto e prazo com condição e vigência; risco médio ou alto vai ao João.

**Atendimento:** prazos só da Tabela 5.1; não promete além do aprovado; não confirma nem nega mecanismo; gatilhos de escalonamento presentes.

**Marca, domínio, identidade:** busca de anterioridade no INPI feita e registrada; domínio com titular identificado (regra do registro.br: NÃO VERIFICADO); análise de colidência com `faixapreta3d.com.br`; classe de registro definida pelo advogado.

**Plataforma e fiscal:** regime (MEI/Simples), IE, certificado A1, NF-e conferidos pelo contador; art. 33 LGPD tratado.

**Contratos com terceiros:** só minuta do advogado; o Jurídico não redige contrato final.

### 5.4 Formato único de revisão
`PASSA | PASSA COM AJUSTE | BLOQUEIA`, severidade (baixo, médio, alto), risco J, trecho exato, motivo, alternativa segura, o que não conferi. "PASSA" nunca significa "está legal": significa "não achei problema nos critérios acima".

---

## 6. Bloqueio e escalonamento (só advogado humano resolve)

**Bloqueio imediato:**
1. Dúvida sobre venda de objeto com compartimento no Brasil (Decreto 10.030, Lei 10.826 e correlatas).
2. Copy que sugira esconder item ilícito, prometa segurança de valores ou use item da lista mestre.
3. Produto que lembre arma, réplica, acessório ou parte de arma.
4. Notificação, ação, Procon, Conar, plataforma, INPI, ANPD, ordem de autoridade.
5. Incidente de segurança com dado de cliente.
6. Pedido de titular LGPD complexo.
7. Conflito entre marca e arts. 31 e 37 CDC que o texto não resolve.
8. CNPJ, tributos, regime, NF-e, contrato, cláusula de responsabilidade.
9. Conta, anúncio ou loja suspensos por tema de ocultação ou produto perigoso.
10. Alegação de dano (corte, queima, criança).
11. Reclamação de marca de terceiro ou colidência no INPI.
12. Variação que mude função ou formato do compartimento.

**Escada**
| Nível | Quem | Como |
|---|---|---|
| 1 | Jurídico revisa e devolve | Formato 5.4, mesmo ciclo |
| 2 | Cláudio consolida e leva ao João | `docs/decisoes.md`, com recomendação e fonte |
| 3 | João decide ou manda ao advogado | Jurídico monta o pacote (seção 10); o João envia |
| 4 | Advogado responde | Vira regra na 5.1 ou na lista mestre |
| Urgente | Documento com prazo legal | Aviso direto ao João, sem esperar o lote |

Nunca envio nada a advogado, órgão ou terceiro. Ausência de resposta mantém o bloqueio.

---

## 7. Matriz de autonomia

Proposta, vale só depois do "grava" do João e dos portões P2, P3 e P4. Níveis do playbook §8.

**Ausência de resposta NÃO é aprovação.** Silêncio, "visto", emoji, mensagem ambígua, prazo vencido ou aprovação de outro agent não contam. Vale só o "sim" explícito do João (ou do advogado, no que é dele), por escrito, citando o item.

| Atividade | Nível |
|---|---|
| Ler lei e política oficial, registrar data e acesso | A |
| Grep da lista mestre em arquivos locais | A |
| Criar rascunhos novos marcados "REVISAR COM JURÍDICO" | A |
| Sobrescrever doc oficial existente | Pergunta antes (CLAUDE.md) |
| Corrigir erro de prazo no meu próprio rascunho, com fonte | B (avisa depois) |
| Revisar copy e devolver PASSA / AJUSTE / BLOQUEIA | A (risco baixo) |
| Copy de risco médio ou alto | **C (só João)**; eu só sinalizo |
| Publicar texto jurídico, definir prazo, valor, frete, razão social, CNPJ, encarregado, plataforma | **C** |
| Enviar algo a advogado, órgão, plataforma ou cliente | **C** (João envia) |
| Responder cliente em tema jurídico | Não faço; Atendimento usa a biblioteca aprovada |
| Montar pacote de consulta (arquivo local, sem segredo, sem dado de cliente) | A |
| Dado de cliente em ferramenta externa de IA | Proibido |
| Parecer final, "está tudo certo", "é legal" | Nunca |
| Pausar peça que viole a lista mestre | B (pausa e avisa; religar é do João) |

---

## 8. Fiscalização cruzada

### 8.1 Quem revisa o Jurídico
| Quem | O que revisa |
|---|---|
| **Advogado humano (a contratar, P3)** | Mérito: Tabela 5.1, lista mestre, textos, riscos aceitos. Único que valida |
| **João** | Decisões de negócio e risco que aceita por escrito |
| **Qualidade** | Formato, vazamento do segredo, palavra proibida fora de arquivo de lista |
| **Documentação** | Texto da loja = texto aprovado; links vivos |
| **Cláudio** | Nenhum outro depto com prazo diferente da Tabela 5.1 |

Qualidade e Documentação conferem forma e fidelidade, não mérito jurídico.

### 8.2 O que o Jurídico revisa dos outros
Marketing (palavra proibida, claim, plataforma, prova, imagem fiel, marca de terceiro); Loja (políticas, rodapé, página de produto, fluxo de checkout); Atendimento (biblioteca e gatilhos); Produto (mudança de formato, aviso de segurança); Produção (rastreabilidade, política de defeito); Finanças/Gestão (só sinalizo regime e NF-e); Dados (pixel, coleta, retenção); Qualidade (lista de termos coerente com a minha). Não reviso estratégia, orçamento, estética, engenharia nem cálculo.

### 8.3 Divergência
Jurídico x Marketing: vale a regra mais restritiva até o João decidir. Jurídico x Qualidade: Cláudio leva os dois argumentos ao João.

### 8.4 Contradições com arquivos de outros departamentos (listadas, NÃO editadas)
| Arquivo | Contradição | Correto segundo fonte |
|---|---|---|
| `loja/politicas-rascunho.md` | Defeito "em até 7 dias corridos" | 90 dias pra reclamar (durável), 30 pra sanar (CDC arts. 26 II, 18 §1) |
| `loja/atendimento-respostas.md` bloco 10 | Defeito "até 7 dias ... (SIMULAÇÃO)" | Idem |
| `loja/juridico-checklist.md` (linha de garantia) e `loja/juridico-parecer-previo.md` seção 0 | Marcam CDC art. 26 e art. 49 como "de memória" e o Planalto como bloqueado | Hoje FATO e Planalto abriu (seção 9). Documentos do próprio Jurídico, atualizar na v2 |
| `loja/estado-loja.md`, `loja/seo-produto.md` | Termo de construção sugerindo mecanismo na descrição, meta, alt, JSON-LD | Fora de `produtos/` não aparece (regra da marca; `docs/operacao/ecommerce.md` DON'T 3 concorda) |
| `loja/seo-produto.md` x `docs/operacao/ecommerce.md` | Handle `porta-lapis-preto-3d` x `porta-lapis` | Dono: Loja/SEO; Jurídico só pede que o handle passe pela lista mestre |
| `docs/operacao/ecommerce.md` | Cita preço "R$ 89,90 vs R$ 0,00" no Shopify | R$ 89,90 é SIMULAÇÃO; R$ 0,00 precisa ser explicado. Dono: Loja |
| `docs/operacao/anuncios.md` | Menciona "R$ 150/semana" x teste Meta ~R$ 315 | Fora da minha área; só aviso que verba é nível C |
| `docs/operacao/CONSOLIDADO.md` | Diz "Jurídico propõe `loja/politicas-v2-rascunho.md`" | O arquivo **ainda não existe**; é só proposta (decisão 2 do relatório) |
| `loja/politicas-rascunho.md` | Gmail único como canal; controlador "[a definir]" | Decreto 7.962 art. 2; LGPD arts. 9 e 41 |

---

## 9. Inventário e fontes oficiais (consulta de 2026-11-20)

Método: WebFetch/WebSearch; resumo do leitor, não o diploma inteiro. Nenhuma lei foi citada de memória sem marca. Reabrir cada fonte antes de usar numa peça nova (rotina sugerida: a cada 90 dias).

| Fonte | Link | Resultado hoje | FATO usado | Não lido / pendente |
|---|---|---|---|---|
| CDC, Lei 8.078/1990 | https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm | Abriu (acentos corrompidos) | Arts. 6 III e IV, 18 §1, 26 I, II, §§1 a 3, 30, 31, 35, 36, 37, 38, 39, 49 caput e par. único, 50 | Demais artigos; texto literal exato (tradução do leitor) |
| Decreto 7.962/2013 | https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/decreto/d7962.htm | Abriu | Arts. 1 a 7 | Versão vigente |
| Marco Civil, Lei 12.965/2014 | https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm | Abriu | Arts. 3, 7, 10, 15, 19, 21 | Decreto 8.771/2016: NÃO VERIFICADO |
| Lei 10.826/2003 | https://www.planalto.gov.br/ccivil_03/leis/2003/l10.826.htm | Abriu | Art. 26 veda réplicas e simulacros de arma de fogo; art. 14 menciona "ocultar arma de fogo, acessório ou munição"; "dissimulação" não aparece | Leitura integral não feita; PERGUNTA 20 |
| Decreto 10.030/2019 | https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/D10030.htm | Abriu; li até o caractere 100.000 de 153.869 | Anexo I art. 2 (PCE); art. 3 par. único III "b": "as armas de fogo dissimuladas, com aparência de objetos inofensivos" (uso proibido) | Últimos 53.869 caracteres; vigência do par. único (Decreto 10.627/2021, art. 4) |
| LGPD, Lei 13.709/2018 | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm | Abriu; li até 100.000 de 125.310 | Arts. 5, 6, 7, 9, 18, 33, 41, 48 | Sanções (art. 52 e seguintes); art. 41 §3 |
| ANPD, Res. CD/ANPD 2/2022 | https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022 | Abriu (a URL antiga deu 404; esta é a oficial achada por busca) | Art. 2 I (pequeno porte inclui ME, EPP, startups); art. 3 (não vale com alto risco, receita acima do limite ou grupo econômico acima); art. 11 (sem obrigação de encarregado, mas com canal; indicação voluntária é boa prática); art. 14 II e art. 10 (incidente) | A página diz que o texto não substitui o DOU de 28/01/2022 e foi alterado pela Res. CD/ANPD 15/2024, **que não li** |
| CONAR, Código | https://www.conar.org.br/codigos?section=codigo (a URL antiga deu 403; esta abriu) | Abriu; li 100.000 de 170.565 caracteres | Art. 1 (anúncio honesto e verdadeiro, conforme a lei); art. 23 (não abusar da confiança do consumidor); art. 27 (apresentação verdadeira; dados e comparações devem ser comprováveis) | Anexos e regras sobre "grátis": NÃO VERIFICADO; a página não traz data de revisão |
| Lei 9.279/1996 (Propriedade Industrial) | https://www.planalto.gov.br/ccivil_03/leis/l9279.htm | Abriu; li 100.000 de 117.708 | Art. 122, art. 124 XIX e XXIII (não registra imitação de marca alheia), art. 129 (propriedade pelo registro; precedência de uso de boa-fé por 6 meses) | Demais artigos |
| INPI, marcas | https://www.gov.br/inpi/pt-br/servicos/marcas | Abriu (atualizada em 2026-07-09 segundo a página) | Existem base pública de marcas, e-Marcas, tabela de retribuições | Busca de anterioridade NÃO feita; valores NÃO lidos |
| registro.br | https://registro.br/dominio/ , /dominio/regras/ , /dominio/contrato/ | **Todas vieram vazias** (provável página dinâmica). Só resultados de busca (indireto): https://registro.br/dominio/saci-adm/ e https://registro.br/dominio/saci-adm/regulamento/ | Nada oficial lido. HIPÓTESE (busca): só CPF ou CNPJ válido pode ser titular .br; titular responde pelo nome e pelo uso | NÃO VERIFICADO. Ler no navegador |
| Meta, armas, munição e explosivos | https://transparency.meta.com/policies/ad-standards/restricted-goods-services/weapons-ammunitions-explosives/ | Abriu, texto completo | "Ads must not promote the sale or use of weapons, ammunition or explosives"; proíbe acessórios que modificam arma; proíbe instruções de impressão 3D ou fabricação assistida de arma ou peças; histórico de versões na página | Políticas "Prohibited Commercial Practices" e de ocultação: NÃO lidas |
| Meta, índice de padrões | https://transparency.meta.com/policies/ad-standards/ | Abriu, parcial | Prática enganosa proibida (resumo) | Detalhes |
| TikTok, produtos perigosos | https://ads.tiktok.com/help/article/tiktok-ads-policy-dangerous-products-or-services | Abriu, truncado; "last updated April 2025" | Anúncio e landing page não podem exibir armas, munição, explosivos, itens que firam; brinquedos e ficção em casos limitados | Seção de "concealment" não consta; políticas de conteúdo enganoso: NÃO lidas; a página de Brasil pode variar |
| Google Ads | https://support.google.com/adspolicy/answer/6008942 | Abriu | Proíbe "dangerous products or services", "enabling dishonest behavior", "misrepresentation" | Detalhe de cada política |

**Nunca verificado:** Inmetro (peça pequena), Decreto 8.771/2016, Res. CD/ANPD 15/2024, jurisprudência (frete de devolução), termos de uso de produto da Shopify e da Nuvemshop, hospedagem dos dados das duas.

---

## 10. Plano de testes e pacote de consulta para o advogado

### 10.1 Testes do Jurídico (locais, dados fictícios)
| Teste | Como | Passa quando |
|---|---|---|
| T1 Lista mestre | Grep da 3.3 em `loja/`, `marketing-teste/`, `agents/`, `docs/`, exceto este arquivo e `produtos/` | Zero ocorrência fora de lista de "evitar" |
| T2 Tabela de Prazos | Grep de "7 dias", "30 dias", "90 dias", "garantia" em `loja/` e `marketing-teste/` | Nenhum número divergente da 5.1. Achado já conhecido: 8.4, duas linhas |
| T3 Conjunto de ouro | 20 frases fictícias (10 corretas, 10 incorretas) com gabarito | 0 falso negativo em bloqueio alto |
| T4 Marca x lei | 5 cenários (slogan ambíguo, ficha incompleta, foto fiel x render...) | Todos escalam |
| T5 Sigilo | Nenhum arquivo meu cita mecanismo ou abre `02-segredo.md` | Zero |
| T6 Ausência de resposta | Decisão pendente por 3 ciclos | Continua bloqueado |
| T7 Fonte | Toda citação legal tem link, data e rótulo | 100% |
| T8 Dado real | Nenhum teste usa dado de cliente | Zero |
| T9 Links | Reabrir a seção 9 | Todos com status |
| T10 Plataforma | Passar cada anúncio rascunho pelos itens de Meta, Google, TikTok da seção 9 | Itens não lidos viram pendência |
| T11 Revisão cruzada | Qualidade roda o checklist de marca sobre este arquivo | Sem vazamento |

### 10.2 Pacote de consulta (sem segredo, sem dado de cliente; só o João envia)
1. Resumo de 10 linhas: objetos cotidianos impressos em 3D, loja online, Brasil, sem CNPJ definido. Descrição genérica "objeto com compartimento".
2. `loja/juridico-parecer-previo.md` (19 perguntas) e `loja/juridico-checklist.md`.
3. `loja/politicas-rascunho.md` com os achados da 3.1 e 8.4.
4. Seções 5.1, 3.3 e 9 deste doc.
5. Copy de exemplo, depois da Qualidade.

**Perguntas novas (somam-se às 19 do parecer)**
20. "Ocultar" e "esconder" na comunicação comercial podem ser lidos junto com o art. 14 da Lei 10.826? A lista mestre está certa?
21. A garantia de 90 dias vale pro porta-lápis impresso? Como tratar delaminação, empenamento e tolerância de rosca: vício ou desgaste?
22. Como colocar juntos "7 dias de arrependimento" e "90 dias pra defeito" sem confundir?
23. "Frete grátis" e "devolução grátis": condições mínimas pra não virar oferta além do pretendido (arts. 30 e 35).
24. Conferir os anexos do CONAR sobre "grátis" e "apresentação verdadeira".
25. Busca de anterioridade no INPI pra "Faixa Preta" e variações, colidência com `faixapreta3d.com.br`, classes de registro, e se vale registrar antes de investir em vídeo e anúncio (Lei 9.279 art. 124 XIX e 129).
26. Domínio `faixapreta.shop` x `.com.br`: titularidade e regras do registro.br (não consegui abrir a página oficial).
27. Transferência internacional (plataforma, gateway, pixels): cláusula e se basta aviso. Onde a plataforma escolhida hospeda os dados?
28. Podemos afirmar "não guardamos dados de cartão" ou só "o gateway processa"?
29. Se agente de pequeno porte, o canal único de e-mail basta? O que registrar internamente? (Res. 2/2022 arts. 3 e 11)
30. Incidente: a Res. CD/ANPD 15/2024 se aplica ao nosso porte? Prazos e modelo.
31. Aviso de peça pequena e faixa etária: norma do Inmetro?
32. Influenciadores: identificação de publicidade e responsabilidade (art. 36).
33. NF-e: MEI ou Simples, IE e certificado A1 são exigidos pra vender produto físico online? Qual plataforma facilita (contador).
34. A política da Meta proíbe instruções de impressão 3D de arma ou peças: nosso anúncio de produto impresso em 3D corre algum risco de ser lido assim?

O João decide antes de enviar: quem envia, qual advogado, escopo (consulta pontual ou acompanhamento), orçamento.

### 10.3 Ciclo
Cada resposta do advogado vira: atualização da 5.1 ou da lista mestre; revisão dos rascunhos; linha em `docs/decisoes.md`; remoção de "REVISAR COM JURÍDICO" só dos trechos que ele aprovou, por escrito.
