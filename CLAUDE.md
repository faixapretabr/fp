# FAIXA PRETA

> COMUM POR FORA, FAIXA PRETA POR DENTRO

## O que é
A Faixa Preta cria objetos comuns, familiares e cotidianos com um segredo. O diferencial está no projeto: aparência normal, construção cuidadosa e algo que só aparece pra quem sabe onde olhar.

Produção: os objetos são feitos por impressão 3D.

## Marca
- Tom: discreto, curioso, cúmplice. Nunca óbvio, nunca barulhento.
- Nunca revelar o segredo em textos de marketing. Sugerir, não entregar.
- Visual e copy seguem a regra: "NADA É SÓ O QUE PARECE".

## AI FIRST
- Feito com IA: design, copy, código e atendimento nascem com IA.
- Operado por agents autônomos: eles rodam os processos do dia a dia.
- Antes de fazer manual, pergunte: "um agent resolve isso?"
- Agents agem dentro dos limites definidos aqui. Ações externas (vender, publicar, pagar) pedem aprovação humana.
- Dados de clientes nunca vão pra ferramentas externas sem autorização.

## Comandos
- Sem `package.json`. Os modelos 3D são scripts Python com CadQuery (`pip install cadquery`).
- Rodar de dentro de `produtos/organizador-mesa/modelo/` (os STL saem na mesma pasta):
  - `python porta-lapis_v3.py v4` — corpo v4 + tampa v4
  - `python porta-lapis_v5.py` — tampa v5 (usa o v3)
  - `python cupom_rosca_v4.py` — anel do cupom da rosca
- Sem testes nem lint ainda.

## Estrutura
- `README.md` — visão geral pra humanos
- `.vscode/` — config do editor
- `agents/` — definições dos agents autônomos (`produto/` = departamento de Produto)
- `produtos/` — um produto por pasta (hoje: `organizador-mesa/`). Conteúdo interno
- `pesquisa/` — pesquisas de apoio (ex.: materiais 3D)
- `src/` — (a criar) código do produto

## Regras de ouro (o Claude segue isso à risca)
- Responda em português, tom informal e direto.
- Mudança pequena: mostre só o diff, não reescreva o arquivo todo.
- Só mexa no que eu pedi. Vai alterar vários arquivos que já existem? Pergunte antes. Criar arquivos novos dentro do que eu pedi não precisa perguntar.
- Nunca commitar sem eu pedir.
- Seja proativo: sugira melhorias sem esperar eu pedir.
- Sempre termine propondo o próximo passo.    
NADA É SÓ O QUE PARECE.