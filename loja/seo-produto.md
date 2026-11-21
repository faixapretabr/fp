# SEO: página do Porta-lápis (rascunho)

> Nada publicado. Aplicar na loja só com aprovação (agent Loja). Sem número, avaliação ou depoimento inventado. Preço, estoque e domínio são placeholders `[A DEFINIR]`. Texto só sugere; não descreve o segredo.
> Fatos usados: PETG, impressão 3D, 80x150 mm, caneluras verticais, tampa de rosca, cor preta (CONTEXTO.md).

## Campos da página
- **Título SEO (até 60):** `Porta-lápis preto de mesa, impresso em 3D | Faixa Preta` (54)
- **Meta description (até 155):** `Porta-lápis de mesa em PETG, impresso em 3D, com caneluras e tampa de rosca. Parece comum. Quem usa todo dia sabe que não é. Faixa Preta.` (aprox. 140)
- **Handle:** `porta-lapis-preto-3d`
- **H1:** Porta-lápis Faixa Preta
- **Slogan sob o H1:** Nada é só o que parece.

## H2 sugeridos
1. Feito pra ficar na mesa e passar batido
2. Impresso em 3D, em PETG
3. Medidas e acabamento
4. Pra quem é
5. Perguntas frequentes

## Alt text das imagens
1. `Porta-lápis preto com caneluras verticais sobre uma mesa de trabalho`
2. `Porta-lápis preto fechado com a tampa de rosca, visto de frente`
3. `Detalhe das caneluras e da textura da impressão 3D em PETG`
4. `Porta-lápis ao lado de canetas e um caderno, mostrando a escala`
5. `Porta-lápis com a tampa ao lado, visto de cima`
Regra: descrever o que se vê. Nunca mencionar interior oculto.

## JSON-LD Product
Preencher `[ ]` só com dado real. Sem `aggregateRating` e sem `review` até existir avaliação verdadeira.

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Porta-lápis Faixa Preta",
  "description": "Porta-lápis de mesa impresso em 3D, em PETG preto, com caneluras verticais e tampa de rosca.",
  "image": ["[URL imagem 1]", "[URL imagem 2]"],
  "brand": { "@type": "Brand", "name": "Faixa Preta" },
  "material": "PETG",
  "color": "Preto",
  "width": { "@type": "QuantitativeValue", "value": 80, "unitCode": "MMT" },
  "height": { "@type": "QuantitativeValue", "value": 150, "unitCode": "MMT" },
  "sku": "[A DEFINIR]",
  "offers": {
    "@type": "Offer",
    "url": "https://[DOMINIO A DEFINIR]/products/porta-lapis-preto-3d",
    "priceCurrency": "BRL",
    "price": "[A DEFINIR]",
    "availability": "https://schema.org/PreOrder",
    "itemCondition": "https://schema.org/NewCondition",
    "shippingDetails": { "@type": "OfferShippingDetails", "shippingDestination": { "@type": "DefinedRegion", "addressCountry": "BR" } }
  }
}
```
Nota: "80x150" aparece no CONTEXTO como formato; confirmar se 80 é diâmetro/largura e 150 altura antes de publicar. `PreOrder` combina com produção sob demanda (a confirmar).

## JSON-LD FAQPage
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "De que material é feito?", "acceptedAnswer": { "@type": "Answer", "text": "PETG, impresso em 3D, na cor preta. É resistente e tem acabamento firme." } },
    { "@type": "Question", "name": "Por que dá pra notar as camadas?", "acceptedAnswer": { "@type": "Answer", "text": "Os objetos são impressos em 3D, então pequenas variações de textura são normais." } },
    { "@type": "Question", "name": "Qual o prazo de produção e entrega?", "acceptedAnswer": { "@type": "Answer", "text": "[A DEFINIR: prazos das políticas ainda são simulação]" } },
    { "@type": "Question", "name": "Posso devolver?", "acceptedAnswer": { "@type": "Answer", "text": "Sim, em até 7 dias corridos do recebimento, conforme o art. 49 do CDC. [REVISAR COM JURÍDICO]" } },
    { "@type": "Question", "name": "Ele é só um porta-lápis?", "acceptedAnswer": { "@type": "Answer", "text": "É um porta-lápis, e dos bons. O resto você descobre com ele na mão." } }
  ]
}
```
A última resposta sugere sem entregar. Dúvida se passa do ponto: escalar pro humano.

## 10 palavras-chave
| # | Palavra-chave | Intenção | Uso |
|---|---|---|---|
| 1 | porta-lápis de mesa | Comercial/transacional | H1, título |
| 2 | porta-lápis preto | Transacional | título, alt |
| 3 | porta-lápis impresso em 3D | Transacional (nicho) | título, H2 |
| 4 | organizador de mesa 3D | Comercial (comparação) | H2, coleção |
| 5 | porta caneta de escritório | Transacional | descrição |
| 6 | organizador de mesa minimalista | Comercial/inspiração | descrição, blog |
| 7 | presente criativo para escritório | Presente | descrição, coleção |
| 8 | presente diferente para quem trabalha em casa | Presente/informacional | blog |
| 9 | objetos impressos em 3D para casa | Informacional/comercial | marca, home |
| 10 | objeto de mesa diferente | Exploratória (alinha ao tom da marca) | blog, social |

Sem volume de busca: não há ferramenta de dados conectada. Validar volumes antes de priorizar (não inventei número).

## Evitar
Palavras que entregam o segredo ou atraem o público errado: esconderijo, compartimento, secreto, camuflado, "esconder" qualquer coisa. Também evitar "faixa preta" sozinho como palavra-chave (disputa com artes marciais).

## Pendências pra publicar
Preço, SKU, medidas confirmadas, fotos, domínio (ver `pesquisa/dominio-perfis.md`), prazos reais, revisão jurídica das respostas e revisão de marca.
