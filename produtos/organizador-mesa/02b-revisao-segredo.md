# Revisão do segredo: organizador de mesa (v4 corpo + v5 tampa)

Interno. Nada daqui vai pra marketing nem sai de `produtos/`.

**Status:** revisão do agent Segredo. Não substitui o `02-segredo.md` (histórico). Aguarda decisão do humano (2 itens no fim).
**Base:** lida dos scripts `porta-lapis_v3.py` (v4), `porta-lapis_v5.py`, dos docs `02`, `03`, `README`, `01b` e `parametros-impressao.md`. Números abaixo são CALCULADOS dos parâmetros dos scripts, não medidos nos STL e nada foi impresso. Tratar como estimativa.

## Mecanismo vigente (em uma linha)
Compartimento na parte de baixo do corpo, fechado por tampa roscada de 2 voltas, aberta com moeda na ranhura. A tampa v5 é oca por cima e aumenta o espaço. O furo de cima (Ø74) tem piso de 3 mm e não mostra nada. A escolha do humano ainda não está registrada no `02` (pendência já listada no README).

## Veredito
Mecanismo **coerente com as medidas** e melhor que o proposto no `02` (mais espaço, sem ímã, sem peça frágil). Dois pontos pra corrigir (capacidade prometida e aparência da base) e um pra testar (ranhura). Nada bloqueia o cupom.

## 1. Consistência com as medidas
| Item | Doc / script | Achado |
|---|---|---|
| Folga da rosca | 0,4 mm | Confere: radial (R33 x R33,4 e R34,6 x R35) e normal aos flancos de 45° dão 0,4. Passo 6 mm, tampa de 12 mm = 2 voltas, bate com "~2 voltas" |
| Parede da zona da rosca | 5,0 mm | Confere (R40 - R35). Base lisa até z=16, as caneluras só começam depois |
| Paredes do bolso da tampa v5 | 5 mm lateral, 2,4 mm sob o bolso | Ok pro bico 0,6. Se aprofundar a ranhura (item 3), sobra menos |
| Espaço útil | `02`: Ø70x18, ~45-50 cm³ | **Desatualizado.** Pelos scripts: Ø62 até z=45, mais o bolso Ø56x8 da tampa. Cerca de 110 cm³ úteis (~94 acima da tampa + ~20 do bolso). Altura livre ~39 mm no centro, ~31 mm nas bordas. Atualizar o `02` quando o humano registrar a escolha |
| "Fundo falso" (03) | piso de 3 mm | Nome confuso: é só o piso do furo de cima, entre o copo e o compartimento. O acesso é por baixo. Sugestão: chamar de "piso interno" nos docs internos |
| Altura do porta-lápis | `02`: ~100 mm | Hoje 150 mm. O `02` ficou pra trás |
| Posicionamento do `02` (chave, cartão, pendrive, anel) | | **Cartão de crédito (85x54) NÃO cabe**: a maior corda é 62 mm e a altura livre é ~39 mm. Pendrive só até ~60 mm. Cabem: chave simples, anel, moedas, cédulas dobradas, SIM, cartão de memória, pendrive pequeno |

## 2. Discrição e inspeção (risco de a peça parecer suspeita)
| Ponto | Risco | Comentário |
|---|---|---|
| Visão de cima | Baixo | Piso liso de 3 mm, sem emenda. Ponto forte |
| **Base vista de baixo** | **Médio** | Tampa fica 2 mm rebaixada, com ranhura de moeda e o começo da rosca visível. Parece tampa de bateria ou pote. É o que mais entrega a peça |
| Frestas | Baixo | Folga de 0,4 mm na linha da tampa. Some se a base estiver coberta |
| Proporção | Baixo a médio | Interior com 102 mm de fundo num corpo de 150 mm: base de ~48 mm. Copos comuns têm base fina. Só quem medir percebe. Aceitar |
| Peso e som | Baixo | Plástico leve é normal pro tipo de objeto. Bater no fundo soa oco, como qualquer peça impressa |
| Chocalho | Médio | Objeto solto balança ao mexer. Forrar o bolso da tampa com EVA/feltro fino (1 mm) |
| Raio-X / correio | Baixo | Vazio de plástico sem metal nem ímã. Nada que chame atenção |

## 3. Facilidade de uso
- Abrir: virar o copo de boca pra baixo (apoia no aro), girar a tampa com moeda. O conteúdo fica à vista, apoiado no piso do compartimento. Bom.
- **Tem que tirar os lápis antes de virar.** Natural, mas o cliente precisa saber. Resolver com cartão dentro da caixa em tom de charada, sem entregar (regra da marca).
- Ranhura de 3,0 x 1,6 mm: largura serve pra moedas brasileiras (1,6 a 2 mm de espessura), mas 1,6 mm de profundidade é raso, pode escorregar em PETG. Testar no cupom. Se escorregar: ranhura 2,0 mm e piso do bolso de 6,0 pra 6,6 mm (perde ~2 cm³).
- Sem trava nem clique: a fricção da rosca segura. Em PETG com folga 0,4 pode afrouxar com vibração. Testar no cupom (balançar, deixar na mesa).
- Sem vedação: não é à prova de água nem de poeira. Não prometer.

## 4. Risco jurídico (sem parecer; só o que aparece nos docs e no bom senso)
- **Sem parecer jurídico.** `01b` diz que nada específico foi achado. O Decreto 10.030/2019 foi citado sobre "armas dissimuladas", mas o texto não foi lido inteiro. Não verificado.
- O espaço (Ø62 x ~40 mm) não comporta arma de fogo. Manter assim. Nunca citar arma, droga ou "esconder de alguém" em nenhum texto.
- CDC: não prometer segurança (não é cofre, não tem fechadura). Descrever com verdade o que é: porta-lápis com medidas e material. Dizer de forma genérica que "tem um segredo" não viola a marca e evita a acusação de omissão. Direito de arrependimento de 7 dias vale normalmente.
- Plataformas: a Shopify, o meio de pagamento e os anúncios (Meta, Google) podem barrar "compartimento secreto". Políticas NÃO verificadas por mim. Chamar de "porta-lápis" e deixar o resto como sugestão. Também ajuda na regra da marca.
- Segurança: PETG sem selo de contato com alimento. Não vender como armazenamento de comida ou remédio. Pecas pequenas soltas: avisar na caixa "não é brinquedo".

## 5. Ajustes sugeridos (sem mexer no modelo agora)
1. Cobrir a base (ver decisão 1).
2. Forrar o bolso da tampa com EVA/feltro de 1 mm.
3. Atualizar o `02-segredo.md` quando o humano registrar a escolha: espaço real, altura 150, tampa v5, remover cartão e pendrive grande da lista de usos.
4. Acrescentar ao cupom: (a) moeda de R$ 1 gira sem escorregar? (b) afrouxa com vibração? (c) 5 voltas de abre/fecha sem desgastar a ranhura?
5. Se a ranhura precisar de mais fundo, só vira v6 depois do cupom.

## Decisões pro humano
1. **Como esconder a base?** Opções: (a) disco de feltro ou EVA de ~2 mm, adesivo fraco, cobrindo o rebaixo; (b) deixar à vista; (c) redesenhar a base (v6). **Recomendo (a):** custa centavos, não mexe no modelo, preenche exatamente os 2 mm do rebaixo, cobre ranhura, rosca e fresta, e o feltro é item comum em porta-lápis (protege a mesa). Descolar o disco vira parte do gesto de abrir.
2. **Parecer jurídico antes de publicar a loja?** **Recomendo sim:** uma consulta curta com advogado de e-commerce antes de listar qualquer item e antes de anúncio. Não bloqueia o protótipo nem o cupom. Só bloqueia publicar. Custo a levantar (ação externa, pede aprovação).

## Próximo passo
Imprimir o cupom já com a ranhura (e anotar os 3 itens novos do cupom). Em paralelo, o humano responde as 2 decisões acima.
