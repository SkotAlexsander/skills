---
skill: desenhar-sistema
tema: aprendizado
fonte: própria (Claude Mestre Neutro)
tags:
  - skill
  - aprendizado
  - propria
---

# desenhar-sistema

> O método de 4 passos do System Design Primer aplicado a um projeto **real e na escala dele**:
> casos de uso → estimativa com as contas à vista → desenho → componentes → decisões com trade-off
> e "o que faria mudar". Resultado: um `docs/design-<tema>.md`.

**Invocar:** `/desenhar-sistema`  ·  **Tema:** [[_16-aprendizado|aprendizado]]  ·  **Origem:** própria, 2026-09-13

## Por que ela existe

O primer foi escrito para entrevista em big tech, mas a lição dele é outra: **tudo é trade-off, e
só dá para escolher o trade-off depois de saber o tamanho do problema.** Aplicado ao Trindade (nota
`estudo-de-caso-trindade` do Cérebro), o método mostrou que o único número grande do projeto é a
banda de vídeo, e que fila, cache e sharding não têm lugar na escala de um grupo de amigos.

A skill leva essa disciplina para qualquer projeto: **nenhuma peça entra sem número ou medição**,
custo e esforço de operação contam como restrição, e todo documento traz a lista do que *não*
fazer agora.

**Cuidados herdados da leitura:** a tabela dos "noves" do primer erra 99,99% (dá ~1 min 0,5 s por
semana, não 1 min 5 s); os números de latência não batem com a origem; o pseudocódigo de
cache-aside monta SQL com `.format()`. Tudo isso está anotado nas notas da trilha.

## Conecta com — dentro de *aprendizado*

- [[algoritmos-na-pratica]] — quando o gargalo é o código, não a arquitetura
- [[ler-repositorio]] — ler a arquitetura de um sistema de referência
- [[estudar]] — estudar a nota de uma decisão antes de tomá-la

## Arquivos desta skill

- [SKILL.md](SKILL.md)

---
[[00-INDICE|← Índice da biblioteca]] · [[_16-aprendizado|← aprendizado]]
