# Validação: organizador de mesa v4

Interno. Modelo avaliado: `modelo/corpo_v4_canelura_80x150.stl` + `modelo/tampa_v4.stl`. Material: PETG, bico 0,6 (ver `parametros-impressao.md`).

**Resultado:** NÃO APROVADO PRA PRODUÇÃO. Falta o teste físico (regra do departamento). Nenhuma reprovação de geometria, mas há 1 risco alto e 3 médios.
Medidas das malhas são calculadas. Tempo, massa e custo são **estimativa**.

## Checklist
| Item | Resultado |
|---|---|
| Malhas fechadas (sem furo) | OK: corpo e tampa |
| Parede do furo de cima | 3,0 mm, 2,4 mm nos vales das caneluras. OK (≥3 linhas de 0,66) |
| Parede na zona da rosca | 5,0 mm (lisa até z=16). OK |
| Parede da cavidade | ~8,4 mm. OK |
| Fundo falso | 3 mm, 10 camadas de 0,3. OK |
| Interferência rosca × tampa | NÃO MEDIDA no v4 (a conta travou). No v2, mesma geometria com folga 0,3: ~0. Medir no cupom |
| Caneluras (1,6 mm de passo, 0,6 de profundidade) | Risco médio: perfil do tamanho da linha do bico pode sair suavizado. Slicer com resolução ≤0,1 mm |

## Orientação e suporte
- **Corpo em pé** (rosca na mesa): overhang >45° de 42 cm². Desses, **~30 cm² são o teto plano da cavidade (Ø62, z=45)**, ponte de 62 mm. O resto é pouco (flancos da rosca no limite de 45°).
- Corpo de cabeça pra baixo: ~43 cm² de ponte no teto do furo de cima (Ø74). Pior. Descartado.
- **Tampa** com a ranhura na mesa: só ~3 cm² de flancos a 45° (no limite). O resto é face de apoio.
- Cupom (anel): ~5 cm² de flancos a 45°. No limite, aceitável.

## Problemas
1. **ALTO: ponte de 62 mm** no teto da cavidade. PETG com bico 0,6 tende a ceder ou ficar com fios. Recomendação: suporte só dentro da cavidade (retirado pela boca da rosca) ou voltar ao cone de 45° (v3). Decidir antes de imprimir o corpo.
2. MÉDIO: folga da rosca (0,4 mm) é estimativa. PETG pode ficar justo ou frouxo. Por isso o cupom.
3. MÉDIO: flancos da rosca em exatamente 45°. Pode ficar áspero. Tampa com camada de 0,2.
4. MÉDIO: caneluras podem sair suavizadas com bico 0,6.
5. BAIXO: sem vedação, não é à prova de água.

## Estimativas (não medidas)
Premissas: PETG a 1,27 g/cm³, R$ 110/kg (valor assumido, sem fonte), camada de 0,3 (corpo) e 0,2 (tampa).
| Peça | Volume do modelo | Massa | Tempo |
|---|---|---|---|
| Corpo 80×150 | 161 cm³ | ~150 g | ~6 a 9 h |
| Tampa (100% preenchida) | 43 cm³ | ~54 g | ~2 a 3 h |
| Anel do cupom | 12 cm³ | ~13 g | ~1 h |
| **Corpo + tampa** | | ~205 g | ~8 a 12 h |
| **Cupom (anel + tampa)** | | ~67 g | ~3 a 4 h |
- Custo de filamento: corpo + tampa ~R$ 23. Cupom ~R$ 7.

## Cupom de teste (próximo passo físico)
Imprimir `modelo/cupom_anel_v4.stl` (em pé, z=0 na mesa) e `modelo/tampa_v4.stl` (ranhura na mesa).
O que anotar:
- [ ] A tampa entra sem forçar? Quantas voltas até assentar? (esperado ~2)
- [ ] Fica folgada ou presa? Anotar a folga sentida.
- [ ] A rosca sai áspera nos flancos? A camada de 0,2 resolveu?
- [ ] Abre com uma moeda na ranhura?
- Se ficar presa: subir a folga pra 0,5. Se ficar frouxa: voltar pra 0,3.
Resultado do teste físico: _(preencher depois da impressão)_

## Próximos passos
- [ ] Resultado do cupom.
- [ ] Decidir teto da cavidade: suporte ou cone.
- [ ] Protótipo do corpo inteiro.
- [ ] Segundo portão humano (aprovação do modelo).
