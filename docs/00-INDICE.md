---
titulo: Índice da biblioteca de skills
tipo: indice
tags:
  - indice
  - moc
---

# 📚 Biblioteca de Skills

**139 skills · 80 artigos · 16 temas · 18 repositórios de origem**
Atualizada em 2026-08-13 · Local: **`30-sistema/biblioteca-skills/`, dentro do repo**

> **Mudou de casa em 13/08/2026.** Antes vivia em `~/.claude/skills/biblioteca/` — solta no
> perfil do usuário, fora de qualquer git. Agora mora no repositório: versionada, com
> histórico e backup. Os atalhos `/` continuam funcionando igual, porque as junctions em
> `~/.claude/skills/` foram refeitas apontando pra cá.
>
> **Em máquina nova, depois de clonar, rode:**
> ```bash
> python 30-sistema/tools/scripts/ligar_biblioteca_skills.py --apply
> ```
> Junction não é arquivo — mora no perfil do usuário e **não vai no git**. Sem esse comando
> o repo tem a biblioteca e o Claude não enxerga skill nenhuma.

> **Lote 6 (13/08/2026)** — entraram **Figma** (tema novo), **Framer Motion**, rolagem
> e transição de página, e **3D/WebGL** (tema novo). Detalhe e auditoria em
> [[00-CATALOGO-E-AUDITORIA]] §2 nota (h).

> **Lote 7 (13/09/2026)** — tema novo **Aprendizado**, com 5 skills **próprias** nascidas da
> trilha `A:\Claude\02-cerebro\70-aprendizado\` (13 repositórios do GitHub lidos em quarentena).
> Procedência e hashes em [[00-CATALOGO-E-AUDITORIA]] §2 nota (i).

> **Fluxo de trabalho:** [[00-CRIACAO-DE-SITES]] — o hub de criação de site (estrutura → design → responsividade → auditoria), com qual skill usar em cada etapa.
> **Artigos:** [[00-BIBLIOTECA-DE-ARTIGOS]] — 80 artigos de fonte primária sobre IA, front-end e design, ligados às skills que executam o assunto.
> **Procedência e segurança:** [[00-CATALOGO-E-AUDITORIA]] — de onde veio cada arquivo, licença, commit, hashes e o resultado da auditoria.

---

## Os 16 temas

| Tema | Skills | Para quê |
|---|---|---|
| 🧱 [[_01-estrutura-e-layout\|Estrutura e layout]] | 4 | O esqueleto da página — o que existe e em que ordem |
| 🎨 [[_02-design-visual\|Design visual]] | 13 | Direção estética, paleta, tipografia, layout, tokens de tema |
| ⚛️ [[_03-componentes-e-codigo\|Componentes e código]] | 8 | Tailwind, shadcn/ui, React, engenharia de UI, biblioteca de componente animado |
| 📐 [[_04-responsividade-e-qualidade\|Responsividade e qualidade]] | 10 | Breakpoints, UX audit, a11y, performance, testes |
| 🖼️ [[_05-assets-e-marca\|Assets e marca]] | 5 | Ícones, favicon, imagens, arte generativa |
| 🔍 [[_06-conteudo-e-seo\|Conteúdo e SEO]] | 2 | SEO local com JSON-LD, WordPress/Elementor |
| 🤖 [[_07-ia-e-agentes\|IA e agentes]] | 13 | MCP, engenharia de prompt, RAG, avaliação de LLM |
| 🗄️ [[_08-dados-e-backend\|Dados e backend]] | 4 | SQL, schema, migration, seed |
| 🔧 [[_09-engenharia-de-software\|Engenharia de software]] | 5 | Debugging, TDD, verificação, planos, git |
| 💸 [[_10-eficiencia-de-contexto\|Eficiência de contexto]] | 12 | Impedir gasto de token desnecessário |
| ✍️ [[_11-copy-e-conversao\|Copy e conversão]] | 8 | Headline, oferta, CRO, psicologia de decisão, revisão de texto |
| 🎬 [[_12-motion-e-interacao\|Motion e interação]] | 21 | Animação com propósito, GSAP, Framer Motion, física, scroll, transição de página |
| 🎭 [[_13-estilos-visuais\|Estilos visuais]] | 12 | Doze direções estéticas prontas, com regra + tokens |
| 🎯 [[_14-figma\|Figma]] | 11 | Design → código, token, movimento, revisão. **Exige o MCP da Figma** — comece por [[figma]] |
| 🧊 [[_15-3d-e-webgl\|3D e WebGL]] | 6 | Three.js, R3F, Spline, Rive e efeito 3D leve — profundidade no site, não jogo |
| 🎓 [[_16-aprendizado\|Aprendizado]] | 5 | Estudar com revisão espaçada, ler repositório em quarentena, system design na escala real, algoritmo medido, construir do zero. **Próprias** |

## As 3 áreas de artigo

| Área | Artigos | O que tem lá |
|---|---|---|
| 🤖 [[_20-artigos-ia\|IA e agentes]] | 26 | Contexto, ferramenta, harness, avaliação, código gerado |
| ⚡ [[_21-artigos-front-end\|Front-end]] | 28 | CSS moderno, layout, animação, React, performance |
| 🎨 [[_22-artigos-design\|Design e UX]] | 26 | Usabilidade, pesquisa, tipografia, acessibilidade, marca |

---

## Como as conexões funcionam

Cada nota de skill tem uma seção **"Conecta com"** que lista **apenas skills do mesmo tema**. Isso mantém cada tema como um cluster fechado e legível no grafo do Obsidian, em vez de uma teia onde tudo aponta para tudo.

As relações **entre** temas moram em [[00-CRIACAO-DE-SITES]], organizadas por etapa do trabalho.

Cada nota de **artigo** tem sua própria seção "Conecta com", e essa aponta para **skills** — é a ponte entre as duas metades da biblioteca. O artigo explica *por que*; a skill executa.

```text
grafo do Obsidian:
  13 clusters de skill (um por tema, ligados pelo MOC do tema)
  + 3 clusters de artigo
  + 4 nós centrais que atravessam tudo: índice, hub de sites, hub de artigos, catálogo

  cada cluster tem cor própria — já configurado em .obsidian/graph.json
```

---

## Todas as 139 skills

### 🧱 Estrutura e layout
[[design-loop]] · [[landing-page]] · [[product-showcase]] · [[web-artifacts-builder]]

### 🎨 Design visual
[[frontend-design]] · [[frontend-design-anchors]] · [[design-system]] · [[design-review]] · [[color-palette]] · [[theme-factory]] · [[better-typography]] · [[better-colors]] · [[better-layout]] · [[better-ui]] · [[better-interface]] · [[apple-design]] · [[design-first-ui-prompting]]

### ⚛️ Componentes e código
[[shadcn-ui]] · [[tailwind-theme-builder]] · [[tailwindcss-patterns]] · [[react-patterns]] · [[react-native]] · [[frontend-ui-engineering]] · [[build-awwwards-quality-sites]] · [[animated-component-libraries]]

### 📐 Responsividade e qualidade
[[responsiveness-check]] · [[ux-audit]] · [[ux-compare]] · [[ux-extract]] · [[onboarding-ux]] · [[webapp-testing]] · [[vitest]] · [[better-accessibility]] · [[performance-optimization]] · [[browser-testing-with-devtools]]

### 🖼️ Assets e marca
[[icon-set-generator]] · [[favicon-gen]] · [[image-processing]] · [[ai-image-generator]] · [[algorithmic-art]]

### 🔍 Conteúdo e SEO
[[seo-local-business]] · [[wordpress-elementor]]

### 🤖 IA e agentes
[[mcp-builder]] · [[senior-prompt-engineer]] · [[prompt-engineering]] · [[prompt-optimizer]] · [[llm-integration]] · [[agent-harness-construction]] · [[agent-introspection-debugging]] · [[agent-self-evaluation]] · [[eval-harness]] · [[deep-dive]] · [[search-first]] · [[skill-scout]] · [[safety-guard]]

### 🗄️ Dados e backend
[[sql-database-assistant]] · [[database-schema-designer]] · [[d1-migration]] · [[db-seed]]

### 🔧 Engenharia de software
[[systematic-debugging]] · [[test-driven-development]] · [[verification-before-completion]] · [[writing-plans]] · [[git-workflow]]

### 💸 Eficiência de contexto
[[context-fundamentals]] · [[context-optimization]] · [[context-compression]] · [[context-degradation]] · [[filesystem-context]] · [[tool-design]] · [[multi-agent-patterns]] · [[dispatching-parallel-agents]] · [[memory-systems]] · [[long-horizon-prompting]] · [[context-budget]] · [[token-budget-advisor]]

### ✍️ Copy e conversão
[[copywriting]] · [[copy-editing]] · [[ogilvy-copywriting]] · [[better-writing]] · [[marketing-psychology]] · [[offers]] · [[cro]] · [[content-strategy]]

### 🎬 Motion e interação
[[animation-systems]] · [[animation-on-scroll]] · [[gsap]] · [[optimize-web-animations]] · [[css-animations]] · [[animejs]] · [[lottie]] · [[make-interfaces-feel-better]] · [[scroll-progress-timeline]] · [[progressive-blur]] · [[beautiful-shadows]] · [[framer-motion-core]] · [[framer-motion-react]] · [[framer-motion-variants]] · [[framer-motion-scroll]] · [[framer-motion-gestures]] · [[framer-motion-layout]] · [[react-spring-physics]] · [[locomotive-scroll]] · [[barba-js]] · [[scroll-reveal-libraries]]

### 🎭 Estilos visuais
[[estilo-minimal]] · [[estilo-editorial]] · [[estilo-bento]] · [[estilo-premium]] · [[estilo-corporate]] · [[estilo-brutalism]] · [[estilo-neobrutalism]] · [[estilo-glassmorphism]] · [[estilo-claymorphism]] · [[estilo-neumorphism]] · [[estilo-retro]] · [[estilo-vibrant]]

### 🎯 Figma
**Comece sempre por [[figma]]** — ela confere o MCP antes de qualquer coisa.

[[figma]] · [[figma-use]] · [[figma-design-to-code]] · [[figma-implement-motion]] · [[figma-use-motion]] · [[figma-generate-design]] · [[figma-generate-library]] · [[figma-create-new-file]] · [[figma-code-connect]] · [[figma-review]] · [[figma-extract]]

> ⚠️ **Só a [[figma]] está ligada como atalho `/`.** As outras dez existem na biblioteca
> mas **sem junction**, de propósito: sem o servidor MCP conectado elas não conseguem
> executar, e dez descrições carregando em toda sessão é contexto jogado fora. A
> [[figma]] explica como ligar — e o `claude plugin install figma@claude-plugins-official`
> traz o MCP **e** as oficiais de uma vez, já atualizadas.

### 🧊 3D e WebGL
[[threejs-webgl]] · [[react-three-fiber]] · [[spline-interactive]] · [[rive-interactive]] · [[lightweight-3d-effects]] · [[web3d-integration-patterns]]

### 🎓 Aprendizado
[[estudar]] · [[ler-repositorio]] · [[desenhar-sistema]] · [[algoritmos-na-pratica]] · [[construir-do-zero]]

---

## Como isto está montado

São **dois lugares**, e só um deles guarda arquivo.

**1. No repositório — o vault. É aqui que tudo mora e é isto que o git versiona:**

```
A:\Claude\01-agente-wat\Projeto 9 Claude Mestre Neutro\30-sistema\biblioteca-skills\
├── .obsidian/                        ← configuração do vault (grafo colorido, CSS, favoritos)
│   └── snippets/biblioteca.css       ← o visual — ative em Aparência → Snippets CSS
├── 00-INDICE.md                      ← este arquivo
├── 00-CRIACAO-DE-SITES.md            ← hub do fluxo de site (cruza temas)
├── 00-BIBLIOTECA-DE-ARTIGOS.md       ← hub dos 80 artigos
├── 00-CATALOGO-E-AUDITORIA.md        ← procedência + auditoria de segurança
├── _manifest-sha256.txt              ← hash de todos os arquivos
├── 01-… até 16-…                     ← os 16 temas de skill
│   └── <skill>/
│       ├── SKILL.md                  ← a skill (arquivo original, não modificado)
│       ├── <skill>.md                ← a nota Obsidian, com os wikilinks
│       └── LICENSE.txt
└── 20-, 21-, 22-…                    ← os 80 artigos, um .md por artigo
```

**2. No perfil do usuário — só atalhos. Nada de conteúdo, e nada disso vai no git:**

```
~/.claude/skills/
└── <129 junctions>   ← cada uma aponta pra dentro de 30-sistema/biblioteca-skills/
```

**Por que as junctions:** o Claude Code só enxerga skill em `~/.claude/skills/<nome>/SKILL.md`
— **um** nível de profundidade. A biblioteca organizada por tema tem **três**. A junção do
Windows (`mklink /J`) resolve isso: o Claude vê 129 pastas planas, você vê 16 temas
organizados. É o **mesmo arquivo**, não é cópia — editar num lugar edita no outro.

> ⚠️ **Junction não é arquivo e não vai no git.** Em máquina nova, depois de clonar, o repo
> tem a biblioteca inteira e o Claude não enxerga skill nenhuma até você rodar:
> `python 30-sistema/tools/scripts/ligar_biblioteca_skills.py --apply`
>
> O mesmo comando conserta atalho quebrado. `--conferir` audita sem mexer em nada.

## Abrir no Obsidian

Abra `30-sistema/biblioteca-skills/` como vault. A configuração já vem pronta:

1. **Grafo colorido** — cada tema tem sua cor, definida em `.obsidian/graph.json`. Abra o grafo (`Ctrl+G`) e os 19 clusters aparecem separados.
2. **Snippet visual** — vá em *Configurações → Aparência → Snippets CSS* e ligue `biblioteca`. Ele estiliza tabela de MOC, citação, tag e põe a barrinha de cor do tema no explorador de arquivos.
3. **Favoritos** — os 4 hubs e os 16 MOCs já estão em *Bookmarks* (`Ctrl+P` → "Bookmarks: show").

**Aviso:** as pastas das skills contêm `SKILL.md` — todas com o mesmo nome. No Obsidian, prefira sempre a nota `<nome-da-skill>.md` para navegar; ela linka para o `SKILL.md` correspondente por caminho relativo, sem ambiguidade.
