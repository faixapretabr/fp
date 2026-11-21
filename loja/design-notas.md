# Design da loja: notas do wireframe mobile

Agent Web Design. 2026-11-20. Rascunho local. Nada foi publicado e o tema Shopify não foi tocado.
Arquivos: `wireframe-mobile.html` (390 px primeiro, sem imagem externa) e `wireframe-mobile.png` (screenshot via Playwright).
Fonte da marca: `FP_BASE_COMPLETA_v01` (Drive, só leitura), seção de marca e loja.

## Regras da marca aplicadas
- Paleta 2+1: preto `#000000`, creme `#FEF3E6`, amarelo `#FFC002`. Amarelo = 1 elemento por tela (o botão principal). Sem amarelo em fundo, logo ou texto corrido.
- Frase "NADA É SÓ O QUE PARECE" só no hero da home, uma vez. Sem explicar nada.
- Cantos retos, linhas de 1 px, muito respiro, nada decorativo.
- Foto de produto: fundo neutro, 3/4 de cima, sem props. Só foto real da peça. Os blocos do wireframe são placeholders ("pendente"). Render nunca como foto de produto.
- Vocabulário: nenhuma palavra da lista proibida. O texto do produto usa só o que é fato (preto fosco, estrias finas, PETG, 80 x 150 mm, impresso em 3D).
- Preço R$ 89,90 aparece rotulado "simulação" (vem de `simulacao-preco-frete.md`). Prazo e trocas estão marcados como "a definir".

## Estrutura de seções

### Home (de cima pra baixo)
1. Cabeçalho compacto: logo à esquerda, Sobre, Conta, Cesta. Fundo creme, linha de 1 px embaixo.
2. Hero preto: label "Coleção GEN", título "Nada é só o que parece.", uma linha de apoio, botão amarelo "Ver o porta-lápis".
3. Produto em linha: foto 4:5, uma frase factual, botão contorno "Ver detalhes".
4. Coleção "Em breve": grade 2 colunas com placeholders (some se houver só 1 produto no lançamento).
5. Faixa preta "Como é feito": 2 frases sobre precisão e impressão 3D.
6. Rodapé: logo, Sobre, Entrega e trocas, Contato.

### Produto: Porta-lápis
1. Cabeçalho (Buscar, Cesta) e caminho de volta.
2. Galeria: foto principal quadrada + 4 miniaturas.
3. Bloco de compra: label da coleção, título, preço, nota de frete, frase factual, tabela de 3 linhas (formato, material, cor).
4. Acordeões: Medidas e material, Entrega, Trocas.
5. Faixa preta curta "Repara. Quem usa, percebe." É a única linha que sugere. Revisar com o humano.
6. Mesma coleção (2 cards).
7. Barra fixa embaixo: preço + botão amarelo "Adicionar à cesta" (alvo de toque 52 px).

## Tipografia
| Uso | Fonte | Detalhe |
|---|---|---|
| Títulos e chamadas | Space Grotesk Bold | caixa alta, tracking -0,02em, entrelinha 0,9 |
| Texto e interface | Inter Regular | 15 px no mobile, entrelinha 1,6, tracking 0,01em |
| Labels | Inter Medium | 10 px, caixa alta, tracking 0,14em |
O wireframe usa fallback do sistema (sem fonte externa). No tema, carregar as duas fontes.

Alvos de toque de 44 px ou mais. Margem lateral de 16 px. Sem rolagem horizontal (testado em 390 px).

## O que mudar no tema Rebel (lista pra o agent Loja executar, com aprovação)
Observação: não auditei o tema instalado, só a marca. Itens marcados (confirmar) dependem de abrir o editor de tema e ver o que o Rebel oferece.
1. Cores (configurações do tema): fundo creme `#FEF3E6`, texto preto, botão principal amarelo com texto preto, botão secundário só contorno. Remover qualquer cor de destaque extra. Garantir que o amarelo só apareça no botão principal.
2. Fontes: Space Grotesk (títulos) e Inter (texto). (confirmar se o seletor de fontes do tema aceita as duas. Se não, carregar via CSS personalizado.)
3. Cantos: raio 0 em botões, cards, campos e imagens.
4. Cabeçalho: logo à esquerda, menu enxuto (Sobre, Conta, Cesta, Buscar). Sem barra de anúncio, sem mega menu.
5. Home: usar só estas seções: hero (imagem/vídeo desligados, fundo preto), produto em destaque, coleção, faixa de texto, rodapé. Desligar carrossel, depoimentos, newsletter, redes sociais, selos de confiança.
6. Produto: galeria com miniaturas; acordeões para medidas, entrega e trocas; barra fixa de compra no mobile (confirmar se existe, senão CSS/snippet); desligar "vistos recentemente", avaliações e produtos relacionados automáticos se estiverem ligados.
7. Efeitos: desligar animações de entrada, zoom, sombras e transições chamativas.
8. Logo: versão negativa no fundo preto, principal no creme. Abaixo de 24 px, só o símbolo. Favicon: símbolo.
9. Textos: trocar todo texto padrão do tema pelos desta página. Rodapé sem selos de pagamento exagerados.
10. Proteção da loja: manter com senha até o piloto ser aprovado (regra da base).

## Pendências
- Fotos reais da peça (nenhuma foto de produto existe).
- Políticas de entrega e trocas, prazo e preço finais.
- Revisão de marca e aprovação do humano antes de qualquer mudança no tema.
- Verificar o logo vetorial arquivo a arquivo (a base diz que ainda não foi conferido).

## Decisões
1. Proporção de cor. O pedido citava "80/20/0"; na base, 80/20 é a regra de conteúdo (rotina/função extra) e a paleta é 60/30/10 (preto/creme/amarelo). Segui a paleta 60/30/10 com 1 amarelo por tela. Recomendo manter.
2. Faixa "Repara. Quem usa, percebe." no produto. Sugere sem entregar, mas é a linha mais perto do limite. Recomendo manter e o humano aprovar, ou cortar se achar que passa do ponto.
