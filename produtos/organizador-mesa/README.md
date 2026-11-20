# Organizador de mesa (porta-lápis)

Interno. Nada daqui vai pra marketing.

## Status
- **Modelagem.** Nada foi impresso nem testado fisicamente. Validação: NÃO APROVADO pra produção (falta o teste físico).
- **Versão vigente:** corpo v4 (`corpo_v4_canelura_80x150.stl`) + tampa v5 (`tampa_v5.stl`, oca por cima) + cupom da rosca (`cupom_anel_v4.stl`).
- `tampa_v4.stl` é a tampa cheia, ainda citada na validação e no cupom.
- **Versões antigas (v1 a v3):** ficam como histórico. Não apagar.
- Preview atual: `preview/preview-v4.html` (corpo v4 + tampa v5). Os outros são de versões antigas.

## Índice
| Arquivo | O que é |
|---|---|
| `01-selecao.md` | escolha do objeto (1º portão humano, aprovado) |
| `01b-demanda-br.md` | pesquisa rasa de demanda e preços no Brasil |
| `02-segredo.md` | mecanismos propostos. Histórico: o desenho seguido foi tampa roscada |
| `03-validacao.md` | checklist, riscos e estimativas do v4, plano do cupom |
| `parametros-impressao.md` | PETG, bico 0,6, fatiador, suporte da cavidade |
| `modelo/` | scripts CadQuery e STL numerados |
| `preview/` | visualizadores HTML por versão |

## modelo/
- Scripts: `porta-lapis_v1.py`, `_v2.py`, `_v3.py` (também gera o v4 com `python porta-lapis_v3.py v4`), `_v5.py` (tampa v5), `cupom_rosca_v4.py`.
- Não há script `porta-lapis_v4.py`: o v4 sai do v3 com o argumento `v4`.
- STL v1 a v3: `base_v1`, `corpo_v1`, `montado_v1`, `corpo_v2`, `corpo_v2b_80x150`, `montado_v2`, `montado_v2b_80x150`, `tampa_v2`, `tampa_v3`, `corpo_v3_lisa`, `corpo_v3_canelura`, `corpo_v3_aneis`.
- STL v4/v5: `corpo_v4_canelura_80x150`, `tampa_v4`, `tampa_v5`, `cupom_anel_v4`.
- Rodar: ver "Comandos" no `CLAUDE.md` da raiz.

## preview/
- `preview.html` (v1), `preview-v2.html`, `preview-v3.html`, `preview-v4.html` (atual).

## Pendências
- [ ] Imprimir o cupom (anel + tampa) e preencher o resultado em `03-validacao.md`.
- [ ] Folga da rosca: 0,4 mm adotada, a confirmar no cupom (presa: 0,5; frouxa: 0,3).
- [ ] Protótipo do corpo inteiro (ponte de 62 mm com suporte).
- [ ] Registrar em `02-segredo.md` a escolha do humano (mecanismo e formato).
- [ ] Segundo portão humano (aprovação do modelo). Só depois `final/`.
- [ ] Demanda e questão legal no Brasil (ver `01b-demanda-br.md`).
