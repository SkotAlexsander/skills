---
skill: algoritmos-na-pratica
tema: aprendizado
fonte: própria (Claude Mestre Neutro)
tags:
  - skill
  - aprendizado
  - propria
---

# algoritmos-na-pratica

> Consertar código que fica lento quando os dados crescem **medindo antes e depois**, e provando que
> a saída não mudou. E treinar resolução de problemas com o método de 6 passos e dica graduada.

**Invocar:** `/algoritmos-na-pratica`  ·  **Tema:** [[_16-aprendizado|aprendizado]]  ·  **Origem:** própria, 2026-09-13

## Por que ela existe

**Análise é hipótese, medição é evidência.** A nota `complexidade-big-o` da trilha mediu nesta
máquina (Node 24.18.0, 12/09/2026): `a.filter(x => b.includes(x))` foi de 55 ms para 709 ms
enquanto o `n` ia de 10 mil para 40 mil; com `new Set(b)`, de 1,0 ms para 3,0 ms. Um `reduce` com
`[...acc, x]` em 20 mil itens levou ~1.974 ms; com `push`, ~2 ms.

E o outro lado, que é igualmente parte da skill: **saber o n real decide se vale mexer.** O
`gateway.ts` do Trindade escolhe conscientemente não criar índice por canal com cinco pessoas
conectadas.

**A tabela de sinais** (laço com `includes`, `filter` dentro de `map`, cópia em `reduce`, `shift`,
`pop(0)`, ordenação repetida, recursão sem memória, N+1) vem das notas `complexidade-big-o`,
`estruturas-de-dados` e `paradigmas-de-algoritmo`. O passo de **equivalência** existe porque as
trocas mudam semântica em silêncio: `Set` compara objeto por referência e trata `NaN` como igual a
`NaN`.

## Conecta com — dentro de *aprendizado*

- [[estudar]] — o treino registra no diário da fila de revisão
- [[construir-do-zero]] — de onde vem a escada de dicas
- [[desenhar-sistema]] — quando o gargalo é de arquitetura, não de laço

## Arquivos desta skill

- [SKILL.md](SKILL.md)

---
[[00-INDICE|← Índice da biblioteca]] · [[_16-aprendizado|← aprendizado]]
