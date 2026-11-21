# Playbook Faixa Preta v2: como o time trabalha

Rascunho para o João aprovar. 2026-11-20. Base: auditoria da rodada de 16 agents, `docs/analise-processo.md` e `docs/auditoria.md`.

## 1. Auditoria: o que a rodada mostrou
**Funcionou**
- 16 agents em paralelo, 16 entregas em arquivo, ~1.600 linhas, tudo local e sem vazar segredo (conferido por grep: as palavras sensíveis só aparecem em listas de "evitar" e na revisão interna).
- Limites respeitados: nada publicado, pago, apagado fora do combinado, nem commitado.
- Relatórios com decisão e recomendação. A maioria eu resolvi sem subir pro João.

**Não funcionou / risco**
1. **O gargalo é físico, não de texto.** Nada foi impresso. Calendário, anúncio, vídeo e loja dependem da peça real. A rodada produziu papel; o caminho crítico não andou. Cupom impresso > fotos reais > parecer jurídico > loja.
2. **Tudo é simulação em cima de chute** (110 g, 9 h, R$ 2/h, 6%, preço R$ 89,90, frete). Vale como moldura, não como número.
3. **Hook de commit x regra "nunca commitar".** Disparou em todo fim de turno e custou tokens. A regra do CLAUDE.md vence.
4. **Dependências ignoradas.** Vídeo precisou da Copy, SEO e Atendimento da Loja e do Jurídico. Rodar tudo junto gerou retrabalho (ex.: Loja escreveu SEO antes do arquivo de SEO existir).
5. **Docs defasados.** README, CLAUDE.md e CONTEXTO.md não citam loja, jurídico, marketing-teste. Diffs prontos em `docs/auditoria.md`, esperando o "aplica".
6. **Pontas soltas:** "tampa de rosca" na descrição pública do produto (Shopify, rascunho) sugere mecanismo; domínio `faixapreta.shop` sem dono confirmado; marca quase igual (`faixapreta3d.com.br`) e INPI não consultado; políticas com garantia errada (corrigida no checklist, falta nas políticas).
7. **Qualidade das ferramentas:** foto de IA não mantém a peça (moodboard, nota 7/10). Vídeo por IA não rodou (Weave sem vínculo). HyperFrames: 7/10, Apache 2.0, ok pra montagem; pra 5 fotos o ffmpeg quase empata.

## 2. Modelo novo de trabalho
**Princípio:** o time só gasta energia no que destrava o caminho crítico. O resto fica em fila.

**Camadas**
- **João:** dono. Decide dinheiro, publicação, jurídico, produto e prazo.
- **Cláudio (coordenação):** monta a onda, resolve o que é interno e reversível, consolida, sobe no máximo 3 decisões por ciclo.
- **Agents (squads):** executam uma tarefa com escopo fechado e devolvem 5 linhas.

**Squads (agrupam os 16 + novos)**
| Squad | Agents | Foco |
|---|---|---|
| Produto | seleção, segredo, modelagem, validação, entrega | do objeto ao STL final |
| Marca e Conteúdo | coordenação, copy, social, vídeo, web design, SEO, tráfego | só rascunho até haver peça real |
| Loja e Cliente | loja, atendimento | catálogo e suporte |
| Risco | jurídico, **qualidade** | termos, marca, segredo |
| Inteligência | **pesquisa**, **finanças**, **dados** | mercado, custo e números |
| Fábrica | **produção** | impressão e custo real |
| Base | documentação | repo fiel ao estado |

## 3. Novos subagentes propostos (5)
| Agent | Por que existe | Entrega |
|---|---|---|
| **Qualidade (guarda da marca)** | Hoje a revisão de marca e a checagem de vazamento do segredo são feitas por quem escreve. Separa quem faz de quem confere. | Roda o checklist de marca e o grep de termos proibidos em todo arquivo fora de `produtos/` antes de ir ao João |
| **Produção** | Impressão é o gargalo. Ninguém cuida da fila, do filamento e dos resultados reais. | Fila de impressão, registro de peso/tempo reais, falhas, custo por peça |
| **Finanças** | Preço, frete, CAC e margem estão em chute e espalhados. | Planilha única de custo, preço, frete, imposto e CAC máximo, atualizada com número real |
| **Pesquisa** | Concorrente, mercado e novos produtos sem dono fixo. | Radar mensal (concorrentes, preço, termos de plataforma, tendências) |
| **Dados** | Pós-lançamento precisa de leitura de números (loja, social, anúncio). | Relatório semanal curto: venda, visita, custo por compra, o que mudar |

Não criar agora: Dados (só quando houver loja aberta) e Finanças completa (começa como aba de custos até haver número real). Criar já: **Qualidade**, **Produção** e **Pesquisa**.

## 4. Fluxo por onda
1. **Onda 0 (humano/físico):** imprimir o cupom, medir, registrar em `03-validacao.md`.
2. **Onda 1 (sem dependência):** modelagem, validação, jurídico, pesquisa, finanças.
3. **Onda 2:** loja, copy, produção.
4. **Onda 3:** SEO, atendimento, vídeo, social, web design, tráfego (só se houver peça real).
5. **Fechamento:** qualidade confere tudo, documentação atualiza o CONTEXTO, coordenação consolida.

**Portões**
- P1: aprovação do produto escolhido (João).
- P2: aprovação pós-validação com a peça na mão (João).
- P3: parecer do advogado antes de publicar ou anunciar (João contrata).
- P4: loja pronta + pagamento testado antes de qualquer verba.

## 5. Regras de operação
- **Contexto mínimo:** cada agent lê `agents/_contexto-base.md` (15 linhas) + o seu arquivo + os arquivos da tarefa. Não lê CONTEXTO inteiro.
- **Saída:** 1 arquivo novo + 5 linhas (feito, pendente, bloqueio, decisão com recomendação, próximo passo).
- **Decisões:** `docs/decisoes.md`, uma linha cada: contexto, recomendação, dono, prazo. João responde em lote (S/N). Sem resposta = parado, ninguém decide por ele.
- **Autonomia do Cláudio:** reversível e local = age. Sai da máquina, custa dinheiro ou fala com cliente = pergunta.
- **Hierarquia de regras:** CLAUDE.md > definição do agent > plano da rodada > hook do ambiente.
- **Simulação:** tudo em `marketing-teste/` e `loja/` com número chutado leva marca SIMULAÇÃO até haver dado real.
- **Git:** um commit por ciclo, só quando o João mandar.

## 6. Métricas por rodada
Tempo total, tokens por agent, tarefas fechadas sem retrabalho, decisões que subiram pro João, itens do caminho crítico que andaram. Meta: rodada com pelo menos 1 item do caminho crítico avançando (não só papel).

## 7. Próximos 7 dias
1. João imprime o cupom (anel + tampa v5, folga 0,4). Eu entrego a ficha.
2. Aplicar diffs de documentação (precisa do "aplica").
3. Tirar "tampa de rosca" da descrição pública (rascunho Shopify).
4. João escolhe advogado; eu monto o pacote de 19 perguntas sem segredo.
5. João confirma domínio e handle.
6. Criar Qualidade, Produção e Pesquisa (arquivos em `agents/`) e `agents/_contexto-base.md`, `docs/decisoes.md`.
7. Rodada seguinte em ondas, já com número real do cupom.

## 8. Autonomia do dia a dia (proposta, vale só depois dos portões P2, P3 e P4)
| Nível | O que o time faz | Exemplos |
|---|---|---|
| A. Sozinho, sem avisar | Rotina com receita pronta | Postar o que está no calendário aprovado, moderar comentário, responder cliente pela biblioteca, publicar produto já aprovado, otimizar campanha dentro do teto |
| B. Sozinho, avisa depois | Ajuste de rotina | Trocar criativo, pausar anúncio ruim, rastreio e reposição, relatório semanal |
| C. Só com o João | Rumo do negócio | Preço, frete, política de troca, produto novo, subir verba, reembolso acima do limite, Procon, dúvida sobre o segredo |

**Freios fixos:** teto de verba semanal, vocabulário proibido, Qualidade confere antes de postar, anúncio reprovado = pausa e aviso.
**Números a definir pelo João:** teto de verba por semana (sugestão R$ 150) e reembolso máximo resolvido sozinho (sugestão R$ 90).
Gravar isso no CLAUDE.md só com o "grava" do João.

## 9. Rotinas recorrentes (o que dá pra automatizar)
**Como roda:** o ambiente tem agendador de tarefas (cada disparo abre uma sessão nova com o prompt guardado, em horário fixo, no mínimo de hora em hora) e também lembrete dentro da sessão. Cada rotina precisa de prompt autossuficiente e dos conectores liberados. Rotina que publica, paga ou fala com cliente só liga depois do portão e do "grava". Antes disso, só rotina interna e de leitura.

| Rotina | Quando | O que faz | Liga quando |
|---|---|---|---|
| Resumo da manhã | Diária, 7h30 | Lê pendências, pedidos, mensagens e decisões abertas; manda 5 linhas | Já pode (só leitura) |
| Fila de decisões | Diária | Atualiza `docs/decisoes.md` e cobra o que está parado | Já pode |
| Relatório da semana | Segunda, 8h | Números de loja, social e anúncio, custo, o que mudar | Quando houver loja aberta |
| Checagem de marca e segredo | Antes de cada post e semanal | Grep de termos proibidos e checklist de marca | Já pode |
| Calendário de conteúdo | Diária | Posta o que está aprovado e modera comentários | Depois de P2, P3 e P4 |
| Atendimento | A cada hora | Responde pela biblioteca, escala o que for do nível C | Depois de P4 |
| Otimização de campanha | Diária | Pausa ruim, troca criativo, respeita o teto | Depois de P4 e do teto definido |
| Auditoria do repo | Semanal | Links, docs defasados, CONTEXTO fiel | Já pode |
| Radar de mercado | Mensal | Concorrentes, preço, regras de plataforma | Já pode (leitura) |
| Fila de impressão e custo real | Por impressão | Registra peso e tempo, atualiza a planilha de custo | Quando começar a imprimir |

**Limites honestos:** não tenho certeza do que cada conector permite postar sozinho, então isso se confirma rotina por rotina. Instagram e TikTok pedem login seu. Tudo roda numa sessão em nuvem com o que estiver conectado.

## 10. Decisões pro João
1. **Aprovar este playbook** e os 3 agents novos (Qualidade, Produção, Pesquisa). Recomendo sim.
2. **"Aplica"** nos diffs de README, CLAUDE.md e CONTEXTO. Recomendo sim.
3. **"Grava"** a autonomia por níveis, com os dois números. Recomendo sim.
4. **Ligar já as 5 rotinas internas** (resumo da manhã, fila de decisões, checagem de marca, auditoria do repo, radar). Recomendo sim, não gastam nada e não publicam.
5. **Imprimir o cupom.** É o que destrava todo o resto.
