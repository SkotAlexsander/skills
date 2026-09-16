# Seis skills para o Claude Code — e um guia que mede o que cada skill custa

Skills que eu escrevi, em português, para o [Claude Code](https://claude.com/claude-code).
Cinco são de **aprendizado** (estudar de verdade, ler repositório alheio, desenhar sistema,
treinar algoritmo, reconstruir uma tecnologia do zero) e uma é o **portão do Figma**.

Junto vai o [**Guia das skills**](guia/GUIA-DAS-SKILLS.md) — um levantamento de 223 skills
instaladas numa máquina real, com o tamanho de cada uma **medido em tokens** e uma
classificação de custo de uso de 1 a 5. É a parte deste repositório que serve para quem
nunca vai instalar nenhuma das seis.

---

## As seis

| Skill | O que ela faz | Como ela se comporta |
|---|---|---|
| [`/estudar`](skills/estudar/) | Conduz uma sessão de estudo: diagnostica, explica pelo mecanismo, passa exercício que **você** roda, fecha com perguntas de recordação sem consulta e calcula a data da próxima revisão. | Fila de revisão espaçada com degraus de 1, 3, 7, 14, 30 e 60 dias, calculada por script, não pelo modelo. |
| [`/ler-repositorio`](skills/ler-repositorio/) | Estuda a fundo um repositório que você não conhece e vira nota. Confere metadados, clona raso **em quarentena sem executar nada**, neutraliza instruções para agentes que vêm no clone, acha os pontos de entrada e segue uma funcionalidade de ponta a ponta com arquivo e linha. | Para uma lista de repositórios, faz triagem e divide em ondas de 3 agentes. |
| [`/desenhar-sistema`](skills/desenhar-sistema/) | Aplica o método do System Design Primer a um projeto real, **na escala verdadeira dele**: casos de uso, o que fica fora, estimativa de carga com as contas à vista, e só então banco, cache, fila e ponto único de falha. | Cada decisão sai com critério, trade-off e o que faria ela mudar. |
| [`/algoritmos-na-pratica`](skills/algoritmos-na-pratica/) | Acha e conserta custo algorítmico ruim em código real — laço dentro de laço, `includes` dentro de laço, N+1, estrutura de dados errada. | **Mede antes e depois** com tamanhos crescentes e prova que o resultado não mudou. |
| [`/construir-do-zero`](skills/construir-do-zero/) | Guia a reconstrução de uma tecnologia para entendê-la por dentro (Git, React, servidor HTTP, compilador): define o recorte mínimo, fatia em marcos que rodam, cada um com teste. | **Você** escreve o código. O Claude explica, revisa e dá dica graduada — não entrega a resposta. |
| [`/figma`](skills/figma/) | O portão de tudo que envolve Figma. Confere **primeiro** se o servidor MCP da Figma está conectado e explica exatamente o que falta quando não está. | Existe porque nenhuma skill de Figma funciona sem o MCP, e o modo de falha sem ela é confuso. |

A ideia que atravessa as cinco de aprendizado: **entender não é reconhecer.** Ler uma
explicação boa dá a sensação de ter entendido, e a sensação some em semanas. O que prova o
entendimento é recuperar da memória e usar. Por isso, nessas skills, quem produz é a pessoa.

---

## Instalar

```bash
git clone https://github.com/SkotAlexsander/skills.git
cp -r skills/skills/* ~/.claude/skills/
```

No Windows, o destino é `C:\Users\<você>\.claude\skills\`. Depois disso, `/estudar`,
`/ler-repositorio`, `/desenhar-sistema`, `/algoritmos-na-pratica`, `/construir-do-zero` e
`/figma` aparecem na sessão.

### ⚠️ O que você precisa adaptar antes de usar

**As cinco de aprendizado leem e escrevem numa base de conhecimento que é minha.** Elas
apontam para uma trilha de estudo em `A:\Claude\02-cerebro\70-aprendizado\` — um vault
Obsidian privado que **não está neste repositório**. Instaladas cru, elas vão procurar notas
que não existem na sua máquina.

Para usar, troque esse caminho pela sua pasta de notas nos arquivos `SKILL.md` de cada uma.
São poucas ocorrências:

| Skill | Arquivos com o caminho | Ocorrências |
|---|---|---|
| `estudar` | `SKILL.md`, `estudar.md`, `scripts/revisao.py` | 13 |
| `ler-repositorio` | `SKILL.md`, `references/spec-agentes.md` | 7 |
| `construir-do-zero` | `SKILL.md` | 5 |
| `algoritmos-na-pratica` | `SKILL.md` | 3 |
| `desenhar-sistema` | `SKILL.md` | 2 |

São **30 ocorrências no total**. Para achar todas de uma vez:

```bash
grep -rn 'A:\Claude\02-cerebro' ~/.claude/skills/
```

O script [`estudar/scripts/revisao.py`](skills/estudar/scripts/revisao.py) tem o caminho
como **padrão**, não como constante: `--arquivo <caminho>` sobrescreve. Ele é stdlib pura,
sem rede e sem `subprocess`, e grava sempre em UTF-8 (no Windows o `open()` padrão do
Python 3.10 é cp1252 e estraga acento em silêncio).

A `/figma` não depende de nota nenhuma, mas depende do **servidor MCP da Figma** estar
conectado. Sem ele, a skill funciona — e a única coisa que ela faz é te dizer isso.

---

## O guia

[`guia/GUIA-DAS-SKILLS.md`](guia/GUIA-DAS-SKILLS.md) · [mesmo conteúdo em PDF](guia/GUIA-DAS-SKILLS.pdf) (4,9 MB)

Gerado em 13/09/2026 a partir dos arquivos instalados numa máquina real. **223 skills:** 131
globais de uma biblioteca curada, 49 locais de um projeto, 13 de plugin, 17 embutidas no
Claude Code, e o resto desligado ou de nicho. Para cada uma: o que faz em uma linha, o
tamanho medido da instrução, e um nível de custo de uso de 🟢 1 a 🔴 5 **com o motivo escrito**.

O que ele estabelece, com número:

- **Skill instalada custa mesmo sem ser usada.** A descrição de toda skill entra na lista que
  o modelo recebe no começo de **toda** sessão. Na máquina medida isso somava ~13,9 mil tokens
  só com as globais e o plugin, e mais ~5,7 mil ao trabalhar dentro do projeto do agente.
- **Um subagente é uma sessão inteira.** Seis agentes medidos gastaram entre **208 e 291 mil
  tokens** cada. Antes deles, oito em paralelo estouraram o limite de uso duas vezes seguidas.
  Daí a regra de rodar em ondas de 3.
- **Imagem custa caro.** Uma captura Full HD custa **2.691 tokens** — umas 2 mil palavras.
  Skill que tira uma captura por estado de tela multiplica isso.

**Duas ressalvas honestas sobre o guia.** Ele descreve 223 skills, e **a maioria não é minha e
não está aqui** — são skills de terceiros (MIT, Apache-2.0 e Termos de Desenvolvedor da Figma)
que eu instalei, auditei e catalogei; o guia é minha análise delas, não uma cópia delas. E os
tamanhos são medidos, mas os **níveis de custo são classificação minha**, com o critério
explicado na abertura do documento.

---

## Licença

[MIT](LICENSE) — © 2026 Alex Martins. Vale para as seis skills e para o guia.
