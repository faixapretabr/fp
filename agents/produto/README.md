# Departamento de Produto

Vai da escolha do objeto até o STL final pronto pra produção.

## Fluxo
```
1. selecao    → escolhe o objeto        ──► 🧑 aprova
2. segredo    → desenha o compartimento
3. modelagem  → gera o modelo 3D (código → STL)
4. validacao  → checa a peça            ──► 🧑 aprova
5. entrega    → STL final + ficha de produção
```

## Regras do departamento
- Nenhum produto vai pra produção sem as 2 aprovações humanas (depois do 1 e depois do 4).
- Só dá pra ter certeza de que o compartimento funciona imprimindo e testando. A validação do agent não substitui o teste físico.
- O segredo nunca aparece em texto de marketing. Fica só nos arquivos internos de produto.
- Cada produto vive em `produtos/<nome>/`.

## Agents
- `selecao.md`
- `segredo.md`
- `modelagem.md`
- `validacao.md`
- `entrega.md`
