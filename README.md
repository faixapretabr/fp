# Faixa Preta · Agents & Skills

Repositório com o mapa dos **agents** (quem decide e executa) e das **skills** (como cada tarefa é feita) da operação da Faixa Preta.

## Estrutura

- `agents/` — papéis da operação, com responsabilidades e limites de cada um
- `skills/` — catálogo das skills disponíveis, agrupadas por área

## Como usar

1. Antes de começar uma tarefa, veja em `skills/README.md` se já existe skill para ela.
2. Se a tarefa mexe com decisão de negócio, siga o que está em `agents/README.md`.
3. Só o que exige decisão do João sobe para ele, em fila de no máximo 3 itens, com recomendação na frente.

## Regras gerais

- Entregar pronto e conferido, não rascunho.
- Seguir a identidade da marca que está no Drive.
- Pensar mobile first.
- Ações difíceis de reverter ou que saem para fora (publicar, enviar, pagar, apagar) pedem confirmação.
