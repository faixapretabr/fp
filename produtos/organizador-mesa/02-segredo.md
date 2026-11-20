# Segredo: organizador de mesa

Interno. Nada daqui vai pra marketing.

**Status:** proposta do agent. Aguarda escolha do humano (mecanismo e formato).
**Nota (superado):** esta proposta é histórica. O desenho que seguiu pra modelagem é tampa roscada com fundo falso (corpo v4 + tampa v5), não a baioneta A. Ver `03-validacao.md` e o `README.md` desta pasta. A escolha do humano não está registrada aqui _(confirmar e registrar)_.
**Atenção:** todos os números são ESTIMATIVA (assumido porta-lápis ~Ø80x100 mm, PLA/PETG). Nada foi medido nem impresso.

## Mecanismos propostos

### A) Fundo falso por rotação (baioneta)
- Base é um disco separado com 3 garras que giram ~20° no corpo e travam. Por dentro, um disco falso fica acima do fundo real, então quem olha o copo vê um fundo normal.
- Volume: cavidade ~Ø70x18 mm = ~69 cm³ bruto, útil ~45-50 cm³.
- Peças: 3 impressas (corpo, base, disco falso). Sem ímã nem mola.
- Tolerâncias críticas: folga das garras ~0,2-0,3 mm; ressalto de trava ~0,3-0,5 mm pra dar um clique leve; encaixe do disco falso ~0,2 mm.
- Sem suporte: corpo imprime boca pra cima, base deitada, garras com chanfro de 45°.
- Risco de ficar óbvio: peso baixo (~20-30 g a mais, compensável); chocalho (forrar com feltro/EVA); linha da base é o ponto fraco (esconder com chanfro ou faixa de textura); interior ~18 mm mais raso, quem medir percebe.
- Montagem: fácil, sem cola.

### B) Base deslizante tipo gaveta com trava magnética
- Gaveta fina desliza na base, 2 ímãs seguram fechada.
- **Depende de ímã** (atrai chaves e cartões com tarja, pode descolar ou rachar a peça). Regra do agent: exige aprovação humana explícita.
- Volume: ~60x50x12 mm = ~36 cm³ bruto, útil ~25 cm³.
- Peças: 2 impressas + 2 a 4 ímãs.
- Tolerâncias críticas: folga da gaveta ~0,25 mm; bolso do ímã ~0,1-0,2 mm; parede sobre o ímã ~0,6-1 mm.
- Sem suporte: túnel da gaveta exige ponte de ~60 mm (imprimir o teto separado ou colar).
- Risco de ficar óbvio: fresta da gaveta muito visível; peso maior.
- Montagem: média (polaridade dos ímãs).

### C) Painel traseiro deslizante rabo-de-andorinha (suporte de celular)
- Suporte oco; o painel de trás desliza num trilho cônico e prende por fricção.
- Volume: ~60x50x8 mm = ~24 cm³ bruto, útil ~15 cm³.
- Peças: 2 impressas, sem ímã.
- Tolerâncias críticas: folga do cone ~0,25 mm, sensível à calibração (justo trava, folgado cai).
- Risco de ficar óbvio: fresta do painel visível; vibração com o celular em cima; volume pequeno.
- Montagem: fácil, mas exige calibrar a folga.

## Recomendação do agent: A, formato porta-lápis puro
- Maior volume útil (~45-50 cm³ contra ~15-25): cabe chave, cartão, pendrive, anel.
- Sem ímã nem peça frágil.
- 3 peças, sem cola.
- A linha de fecho some numa faixa decorativa; em B e C a fresta entrega o segredo.
- Combo (porta-lápis + celular) não vale agora: o encaixe rouba espaço, aumenta a peça e deixa mais óbvio. Suporte de celular fica como variante v2.

## Posicionamento
Privacidade e pequenos valores (chave reserva, cartão, pendrive, anel). Nunca insinuar droga ou arma.

## Pendências
- [ ] Humano escolhe mecanismo e formato (a seleção aprovada era porta-lápis OU suporte).
- [ ] Protótipo de teste da baioneta em PLA pra validar folga e clique.
- [ ] Esboço dimensional da baioneta.
- [ ] Demanda e questão legal no Brasil (ver `01b-demanda-br.md`).
