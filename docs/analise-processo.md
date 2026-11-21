# Análise de processo: como a gente trabalha

Autor: Coordenação (Marketing). Data: 2026-11-20. Base: CLAUDE.md, CONTEXTO.md, plano-simulacao.md, hook de parada do ambiente (`~/.claude/stop-hook-git-check.sh`) e estado do git. Fato = visto nos arquivos. O resto leva "(hipótese)".

## 1. O que gasta token à toa
- **Releitura de contexto por agent.** Cada um dos 13 agents da rodada lê CLAUDE.md + CONTEXTO.md + plano + a própria definição (~15 KB, só de ler). Em 13 agents são ~200 KB repetidos. CONTEXTO.md e CLAUDE.md repetem as mesmas regras (nunca commitar, só o pedido, pt-BR, próximo passo, segredo). (hipótese: ~30% do contexto lido é redundante)
- **Skills e MCPs carregados sem uso.** A sessão lista centenas de skills (Shopify, Cloudflare, brightdata etc.) e dezenas de MCPs que o projeto não usa. Pesa no prompt de todo agent, toda vez.
- **Relatório e arquivo dizendo a mesma coisa.** Cada agent escreve o `.md` e depois resume de novo no relatório. O resumo tem que ser só ponteiro pro arquivo.
- **CONTEXTO.md duplica o README dos produtos e dos agents** (estado, decisões, comandos aparecem em 3 lugares). Cada um que muda gera um agent de Documentação pra reconciliar.
- **Agent sem escopo de leitura.** O plano manda "ler tudo" em vez de "leia só estes 2 arquivos". Agent de Copy não precisa de CONTEXTO inteiro.

## 2. Onde trava
- **Hook de parada x regra de commit (conflito direto).** O hook do ambiente (`stop-hook-git-check.sh`) sai com erro e manda "commit and push" sempre que há mudança não commitada ou arquivo novo não rastreado. O CLAUDE.md manda "nunca commitar sem eu pedir". Hoje o repo tem `CLAUDE.md` modificado e `agents/juridico.md`, `docs/`, `loja/`, `marketing-teste/` não rastreados, então o hook dispara em todo fim de turno. Resultado: o agent ou desobedece o CLAUDE.md, ou fica em loop pedindo pro João commitar. (O hook só age se existir remote; vale confirmar com `git remote`.)
- **Rodada em paralelo suja a árvore.** 13 agents criando arquivo novo = árvore sempre suja = o hook acima gritando 13 vezes.
- **Aprovação em fila.** Tudo que é externo (publicar, pagar, domínio, advogado, imprimir) espera o João, e o plano só junta decisões depois da rodada inteira. Um bloqueio no passo 3 só aparece no passo 13.
- **Dependências escondidas.** Vídeo (#4) depende de Copy (#3). SEO (#5) e Atendimento (#7) dependem da Loja (#8) e do Jurídico (#9). Rodar tudo "ao mesmo tempo" faz agents trabalharem em cima de rascunho que muda.
- **Pendências de negócio sem dono nem prazo** (preço, frete, troca, prazos de atendimento, repo privado?). Travam Atendimento, Loja e Marketing e não têm data.

## 3. Regras que conflitam ou se contradizem
| # | Regra A | Regra B | Efeito | Decisão proposta |
|---|---|---|---|---|
| 1 | "Nunca commitar sem eu pedir" (CLAUDE.md) | Hook exige commit + push no fim do turno | Loop ou desobediência | CLAUDE.md vence. Registrar que o hook é do ambiente e o agent responde "há mudanças locais, aguardando commit do João" sem commitar |
| 2 | "Seja proativo: sugira melhorias" | "Só mexa no que eu pedi" | Agent não sabe se sugere ou age | Proativo = sugerir em texto, nunca editar fora do escopo |
| 3 | "Sempre terminar propondo o próximo passo" | Relatório de no máx. 8-10 linhas e máx. 2-3 decisões | Estoura o limite | O próximo passo conta como uma das linhas, não soma |
| 4 | "Mudança pequena: só o diff" | Agents escrevem arquivos inteiros novos | Sem conflito real, mas ambíguo | Vale só pra edição de arquivo existente |
| 5 | "Alterar vários arquivos existentes: perguntar antes" | Agent de Documentação existe pra mexer em vários arquivos | Documentação trava toda vez | Pergunta única por lote, com lista dos arquivos |
| 6 | CLAUDE.md: segredo só em `produtos/` | Plano: "NÃO abra 02-segredo.md" e Jurídico/Loja precisam saber o que é o produto | Agents sem informação pública do produto | Criar ficha pública de 5 linhas (nome, uso, materiais), sem o mecanismo |
| 7 | CONTEXTO diz "Marketing só começa com produto validado e loja pronta" | Plano roda Copy, Vídeo, Social e SEO agora | Parece contradição | Marcar tudo de `marketing-teste/` como SIMULAÇÃO, nunca usável |

## 4. 5 melhorias concretas
1. **Resolver o conflito do hook.** Escrever 3 linhas no CLAUDE.md ("hook de commit do ambiente: não obedecer; responder com status") e, se o João quiser, pedir pra desligar o stop hook neste repo. Alternativa melhor: o João faz 1 commit só no fim da rodada, e a árvore fica limpa pro próximo ciclo. Ganho: acaba o loop em todo agent.
2. **Pacote de contexto mínimo por agent.** Criar `agents/_contexto-base.md` (15 linhas: marca, limites, regras de ouro, pt-BR) e cada definição de agent lista no topo "leia só: base + o seu arquivo + os arquivos da tarefa". CONTEXTO.md passa a ser só pra humano e pra dispositivo novo. Ganho estimado: -50% de leitura por agent (hipótese).
3. **Rodar em ondas, não tudo junto.** Onda 1: Modelagem, Validação, Jurídico, Pesquisa (sem dependência). Onda 2: Loja, Copy. Onda 3: SEO, Atendimento, Vídeo, Social. Fecha com Documentação e Coordenação. Ganho: menos retrabalho e bloqueio descoberto cedo.
4. **Formato único de saída.** Todo agent entrega: arquivo + relatório de 5 linhas (feito / pendente / bloqueio / decisão pro João com recomendação / próximo passo). Template em `agents/_template.md`. Coordenação consolida sem reler tudo.
5. **Fila de decisões do João em um arquivo.** `docs/decisoes.md`, uma linha por decisão: contexto, recomendação, prazo, dono. Agents só acrescentam, nunca decidem. João responde em lote (S/N). Ganho: sai a aprovação em fila e as pendências de negócio ganham dono e data.

Bônus de baixo custo: desligar plugins e MCPs sem uso no projeto (Shopify app, Cloudflare, brightdata) nas sessões de agents. Medir o antes e depois.

## 5. O que automatizar (um agent resolve?)
- Checagem de segredo antes de entregar: grep dos termos proibidos nos arquivos fora de `produtos/`. Script simples, roda no fim de cada tarefa.
- Revisão de marca: lista de termos proibidos + checklist em um único arquivo, usada por Copy, SEO e Social.
- Consolidação da rodada: Coordenação lê só os relatórios de 5 linhas e monta `docs/decisoes.md`.
- Auditoria de links e índices: Documentação, 1 vez por rodada, não por mudança.
- Métricas da rodada (tempo, tokens, retrabalho): planilha ou linha por agent no fim do relatório.

## 6. Protocolo de operação autônoma

**Cláudio (Coordenação) decide sozinho:**
- Ordem e divisão das ondas, e quem faz o quê.
- Escopo de leitura de cada agent e formato dos relatórios.
- Aprovar ou devolver peça interna (rascunho, ficha, calendário) conforme o checklist de marca.
- Criar arquivo novo dentro do que foi pedido (regra do CLAUDE.md).
- Reescrever dentro de um arquivo que ele mesmo criou na rodada.
- Resolver conflito entre regras pela hierarquia: CLAUDE.md > definição do agent > plano da rodada > hook do ambiente.
- Marcar item como SIMULAÇÃO, pendente ou bloqueado.

**Sobe pro João (sempre, com recomendação, no máximo 2 a 3 por rodada):**
- Commit, push, qualquer coisa que saia do local.
- Publicar, vender, pagar, anúncio, verba, registrar domínio, imprimir peça, contratar advogado.
- Preço, frete, política de troca, prazos de atendimento, posicionamento.
- Dúvida se a peça entrega o segredo, risco jurídico ou de plataforma.
- Alterar vários arquivos existentes (uma pergunta por lote).
- Mudar regra do CLAUDE.md ou configuração de hook.
- Dado de cliente indo pra ferramenta externa.

**Rotina de cada ciclo:**
1. Cláudio lê CLAUDE.md + `docs/decisoes.md`, monta a onda.
2. Agents trabalham só no escopo, escrevem em arquivo novo, devolvem 5 linhas.
3. Cláudio consolida, fecha tudo que é interno, escreve em `docs/decisoes.md` o que sobe.
4. João responde em lote. Sem resposta = item fica parado, ninguém decide por ele.
5. Fim do ciclo: `CONTEXTO.md` atualizado (Documentação) e um commit único se o João pedir.

Regra de ouro do protocolo: na dúvida entre agir e perguntar, se for reversível e local, aja; se sair da máquina ou custar dinheiro, pergunte.
