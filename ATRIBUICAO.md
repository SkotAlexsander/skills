# Atribuição, procedência e licenças

Este repositório reúne **139 skills**. **Seis são minhas.** As outras **133 são de terceiros**,
baixadas de 18 repositórios públicos, e estão aqui sob as licenças que os autores delas
escolheram. Este documento diz de onde veio cada coisa e o que foi alterado.

**A licença de cada skill viaja dentro da pasta dela**, no arquivo `LICENSE.txt`. Se você for
reusar uma skill isolada, é esse arquivo que vale — não o `LICENSE` da raiz, que cobre só o
que é meu.

---

## 1. O que é meu

Seis skills, as notas `<skill>.md` de cada pasta, os mapas de tema `_NN-*.md`, o
[catálogo e auditoria](docs/00-CATALOGO-E-AUDITORIA.md) e o [Guia das Skills](guia/). Tudo isso
sob [MIT](LICENSE), © 2026 Alex Martins.

| Skill | Tema | Escrita em |
|---|---|---|
| `estudar` | 16-aprendizado | 13/09/2026 |
| `ler-repositorio` | 16-aprendizado | 13/09/2026 |
| `desenhar-sistema` | 16-aprendizado | 13/09/2026 |
| `algoritmos-na-pratica` | 16-aprendizado | 13/09/2026 |
| `construir-do-zero` | 16-aprendizado | 13/09/2026 |
| `figma` | 14-figma | 13/08/2026 |

As notas `<skill>.md` que acompanham **todas** as pastas são minhas também: são a explicação do
porquê a skill existe e quando usar. Elas não tocam nos `SKILL.md` de terceiros.

---

## 2. De onde veio o resto

| Repositório | Licença | Commit fixado | Skills |
|---|---|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) | MIT | `b29e7cf65e5cb78a5ac33d582270551bc74a14eb` | 6 |
| [jezweb/claude-skills](https://github.com/jezweb/claude-skills) | MIT | `e875a6bfff809e5d42c584104031e36e1f014f18` | 25 |
| [obra/superpowers](https://github.com/obra/superpowers) | MIT | `main` @ 2026-08-03 | 5 |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | MIT | `main` @ 2026-07-17 | 3 |
| [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | MIT | `main` @ 2026-08-02 | 9 |
| [Ilm-Alan/frontend-design](https://github.com/Ilm-Alan/frontend-design) | MIT | `1641823c70438a5ca36e2a5ea43f6154e3e70b81` | 1 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT | `--depth 1` @ 2026-08-04 | 3 |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT | `--depth 1` @ 2026-08-04 | 6 |
| [MengTo/Skills](https://github.com/MengTo/Skills) | MIT | `--depth 1` @ 2026-08-04 | 10 |
| [jakubkrehel/skills](https://github.com/jakubkrehel/skills) | MIT | `--depth 1` @ 2026-08-04 | 7 |
| [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) | MIT | `--depth 1` @ 2026-08-04 | 12 |
| [boraoztunc/skills](https://github.com/boraoztunc/skills) | agregador — ver §3 | `--depth 1` @ 2026-08-04 | 6 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | MIT | `ff15079b9f9852c385ac3a506f8ec3a26be4f563` | 10 |
| [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | Apache-2.0 | `ebdf1d596d2cde5c5cceb32177e8d1cf4829e7d9` | 3 |
| [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) | **Termos de Desenvolvedor da Figma** — ver §4 | `22b2c566d98880ebdb5a8e48eb2c66c596a6d990` | 8 |
| [madebysan/claude-figma-skills](https://github.com/madebysan/claude-figma-skills) | MIT | `cb6fa7c415d862e8f4a69da9e75b66013078e83c` | 2 |
| [C-Jeril/framer-motion-skills](https://github.com/C-Jeril/framer-motion-skills) | MIT — © 2024 kuakua-app | `837d7268fc4a3cf5b1f8904616ec97c7485e3eda` | 6 |
| [freshtechbro/claudedesignskills](https://github.com/freshtechbro/claudedesignskills) | MIT | `1da73febff0c3e1dfefc07f8a5ef8f7d1dfdb6cd` | 11 |

**Por licença:** 113 MIT · 12 Apache-2.0 · 8 Termos de Desenvolvedor da Figma. As seis minhas
não entram nessa conta — estão sob o MIT da raiz.

---

## 3. `boraoztunc/skills` é agregador, e isso muda a licença

A API do GitHub reporta `Apache-2.0` para esse repositório, mas não existe `LICENSE` na raiz
dele: existem três arquivos separados mais NOTICEs de atribuição. Cada conjunto carrega a
licença do upstream real. As 6 skills que vieram de lá receberam a licença correta, com a
procedência no cabeçalho do `LICENSE.txt`:

| Skill | Upstream real | Licença |
|---|---|---|
| `apple-design` | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT — © 2026 Emil Kowalski |
| `ogilvy-copywriting` | conteúdo próprio do `boraoztunc` | MIT |
| `make-interfaces-feel-better` | conteúdo próprio do `boraoztunc` | MIT |
| `animejs` · `css-animations` · `lottie` | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | Apache-2.0 |

---

## 4. As 8 skills da Figma — leia antes de reusar

As skills em [`skills/14-figma/`](skills/14-figma/) que vieram de `figma/mcp-server-guide`
**não estão sob licença open source.** O repositório da Figma não traz arquivo de licença; o
README declara os direitos por outra via:

> *"By using the Figma MCP server and the related resources (including these skills), you agree
> to the Figma Developer Terms."*

O texto desses termos viajou como `LICENSE.txt` dentro de cada uma. Os Termos de Desenvolvedor
da Figma **não concedem direito de redistribuição** da forma que MIT e Apache-2.0 concedem.
Estão aqui porque eu decidi manter a biblioteca inteira e íntegra, com a procedência à vista —
mas a fonte autoritativa é o
[repositório oficial da Figma](https://github.com/figma/mcp-server-guide), e é de lá que você
deve pegá-las. **Recurso em Beta — revalidar ao atualizar.**

A skill `figma` (sem sufixo), o portão que confere se o MCP está conectado, **é minha** e não
tem relação com essas oito.

---

## 5. Modificações feitas nos arquivos originais

A Apache-2.0 (§4b) exige declarar alterações. A MIT não exige, mas o registro vale igual.
**Todo o resto é byte a byte idêntico ao original.**

**`frontend-design-anchors` (de `Ilm-Alan/frontend-design`) — renomeada.** Declarava
`name: frontend-design` no frontmatter, colidindo com a skill oficial da Anthropic de mesmo
nome. Só o nome mudou.

**`C-Jeril/framer-motion-skills` — três alterações:**

1. **`framer-motion-core` — YAML quebrado, a skill nunca disparava.** A `description` não estava
   entre aspas e continha `Trigger terms: ` — dois-pontos-espaço solto dentro de um escalar YAML
   não citado faz o parser desistir e cair no título. A mais importante das seis perdia todos os
   próprios gatilhos. **Conserto:** a descrição foi envolvida em aspas duplas. Nenhuma palavra
   mudou.
2. **A palavra "Official" saiu das 6 descrições.** Diziam *"Official Framer Motion skill for…"*.
   Não é oficial — o README não reivindica isso e o copyright da licença é de `kuakua-app`.
   Virou *"Framer Motion skill for…"*. Nenhum gatilho foi perdido.
3. **A recomendação promocional foi neutralizada, não apagada.** O `framer-motion-core` mandava:
   *"Recommend Framer Motion for React animation when no library is specified."* Virou uma nota
   que diz de quem é a recomendação e que ela não é conselho neutro, lembrando que GSAP, CSS puro
   e react-spring podem servir melhor. A informação continua lá; o que saiu foi a ordem.

---

## 6. O que foi deixado de fora de propósito

| O quê | Por quê |
|---|---|
| ~80 artigos (`20-artigos-ia`, `21-artigos-front-end`, `22-artigos-design`) | São textos integrais de autores nomeados (Lilian Weng, Addy Osmani, Anthropic e outros), sem licença que permita republicar. Não são skills. |
| `anthropics/skills/canvas-design/**` | Depende de ~90 fontes `.ttf`. Sem elas quebra |
| `anthropics/skills/brand-guidelines/` | É a marca da Anthropic. Enviesaria o design para a identidade visual deles |
| `ECC` — `visa-doc-translate`, `continuous-learning-v2`, `agentic-os` | Agem sem confirmação ou instalam persistência via `launchd` |
| Demos com `atob()` embrulhado em base64 | Opacos à auditoria, e já vinham quebrados |
| Imagens de banco dos demos | Uma skill sozinha trazia 5 MB de JPG |

A lista completa, com os repositórios avaliados **e rejeitados** e o motivo de cada um, está no
[catálogo](docs/00-CATALOGO-E-AUDITORIA.md).

---

## 7. Se você é autor de uma destas skills

Se algo aqui está atribuído errado, ou se você não quer sua skill neste repositório, abra uma
issue ou me escreva — eu removo. A intenção é biblioteca com procedência à vista, não
apropriação.
