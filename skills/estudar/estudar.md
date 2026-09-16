---
skill: estudar
tema: aprendizado
fonte: própria (Claude Mestre Neutro)
tags:
  - skill
  - aprendizado
  - propria
---

# estudar

> Uma sessão de estudo que deixa rastro: diagnóstico, um mecanismo por vez, exercício que **você**
> roda, perguntas de recordação sem consulta, e a data da próxima revisão calculada por script.

**Invocar:** `/estudar`  ·  **Tema:** [[_16-aprendizado|aprendizado]]  ·  **Origem:** própria, 2026-09-13

## Por que ela existe

Ler uma explicação boa dá a sensação de ter entendido, e a sensação some em semanas. As três fontes
de método da trilha chegam à mesma regra por caminhos diferentes: o coding-interview-university
(resolver problema *enquanto* estuda), o developer-roadmap (refazer o projeto sem olhar, depois
variar) e o freeCodeCamp (o lab sem guia é o que prova). Nesta skill **quem produz é a pessoa**; o
Claude explica, pergunta, confere e registra.

**Os três modos:**

| Modo | Quando | O que sai |
|---|---|---|
| aprender | "me ensina X" | exercício feito + nota registrada na fila |
| revisar | "o que tenho pra revisar" | notas vencidas revisadas e reagendadas |
| roteiro | "o que devo estudar para o projeto Y" | `90-progresso/plano-<slug>.md` no Cérebro |

**A parte determinística:** `scripts/revisao.py` calcula as datas numa escada de intervalos (1, 3,
7, 14, 30 e 60 dias). A conta fica fora do modelo, no espírito do WAT: etapa repetitiva é da
ferramenta. Testado em 2026-09-12 com o caminho feliz e 7 casos de erro. O teste achou e corrigiu um
bug: data inválida gerava traceback em vez de mensagem.

```bash
python "scripts/revisao.py" pendentes
python "scripts/revisao.py" registrar complexidade-big-o --acertos 5 --total 6
python "scripts/revisao.py" diario "aprender · [[complexidade-big-o]] · firmou amortizado"
python "scripts/revisao.py" fila
```

Saída 0 = feito · 1 = feito com aviso (nota não existe na trilha) · 2 = erro, nada gravado.

## Conecta com — dentro de *aprendizado*

- [[construir-do-zero]] — de onde vem a escada de dicas
- [[algoritmos-na-pratica]] — o treino registra no mesmo diário
- [[ler-repositorio]] — de onde vêm as notas que viram currículo

## Arquivos desta skill

- [SKILL.md](SKILL.md)
- [scripts/revisao.py](scripts/revisao.py)

---
[[00-INDICE|← Índice da biblioteca]] · [[_16-aprendizado|← aprendizado]]
