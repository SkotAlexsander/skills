---
tema: Aprendizado
tipo: moc
tags:
  - moc
  - aprendizado
---

# 🎓 Aprendizado

Estudar de verdade e transformar o estudo em trabalho melhor: sessão com revisão espaçada, leitura
segura de repositório, system design na escala real, algoritmo medido e reconstrução de ferramenta.

**5 skills neste tema.** Todas **próprias**, criadas em 2026-09-13 a partir da trilha
`A:\Claude\02-cerebro\70-aprendizado\`, que por sua vez nasceu da leitura de 13 repositórios do
GitHub (system-design-primer, build-your-own-x, javascript-algorithms, coding-interview-university,
developer-roadmap, freeCodeCamp, free-programming-books, react, bootstrap, awesome, awesome-python,
ohmyzsh e listamaravilhosaopensource).

| Skill | O que faz |
|---|---|
| [[estudar]] | Sessão de estudo com diagnóstico, exercício que você roda, recordação e fila de revisão espaçada (`revisao.py`). Modos aprender, revisar e roteiro |
| [[ler-repositorio]] | Estuda um repositório desconhecido em quarentena, neutraliza instruções para agentes, segue uma funcionalidade de ponta a ponta e escreve a nota de fonte |
| [[desenhar-sistema]] | O método de 4 passos do System Design Primer aplicado a projeto real, com estimativa à vista e decisões com trade-off |
| [[algoritmos-na-pratica]] | Acha custo algorítmico ruim em código real, medindo antes e depois; e treina resolução de problemas com dica graduada |
| [[construir-do-zero]] | Reconstrói uma tecnologia em marcos testáveis; você escreve o código, o Claude explica, revisa e dá dica |

## Como elas se encadeiam

```text
lista de repositórios ──► ler-repositorio ──► notas na trilha do Cérebro
                                                   │
                         ┌─────────────────────────┼─────────────────────────┐
                         ▼                         ▼                         ▼
                      estudar            algoritmos-na-pratica        desenhar-sistema
                  (aprender, revisar,     (código real + treino)     (projeto real, antes
                   roteiro)                        │                  de escolher peça)
                         │                         │
                         └──────────► construir-do-zero ◄───────────┘
                                   (quando "entender por dentro" pede mão na massa)

todas registram o progresso em 90-progresso/progresso-estudos.md pelo revisao.py
```

## Onde cada coisa mora

| O quê | Caminho |
|---|---|
| A trilha (o conhecimento) | `A:\Claude\02-cerebro\70-aprendizado\` — outro vault; abra o Cérebro para navegar |
| O motor da fila de revisão | `estudar/scripts/revisao.py` (stdlib, saída 0/1/2) |
| O modelo de SPEC para vários agentes | `ler-repositorio/references/spec-agentes.md` |
| O código de estudo | `A:\Claude\05-estudos\` |

---
[[00-INDICE|← Índice da biblioteca]] · [[00-CATALOGO-E-AUDITORIA|Catálogo e auditoria]]
