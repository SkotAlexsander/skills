---
titulo: Criação de sites — estrutura, responsividade e design
tipo: hub
tags:
  - hub
  - criacao-de-sites
  - frontend
---

# 🏗️ Criação de sites — estrutura, responsividade e design

> **Este é o arquivo primário da biblioteca.** Ele é o mapa do caminho completo de um site: da descoberta da direção visual até a auditoria final. Cada etapa aponta para as skills que fazem o trabalho, e cada skill aponta de volta para cá.

Índice geral em [[00-INDICE]] · Procedência e auditoria em [[00-CATALOGO-E-AUDITORIA]] · Leitura de fundo em [[00-BIBLIOTECA-DE-ARTIGOS]]

---

## O princípio que organiza tudo

Site bom não nasce de escolher fonte bonita. Nasce de resolver as decisões **na ordem certa** — porque cada decisão restringe a próxima. Cor definida antes da estrutura vira retrabalho. Componente montado antes do token de tema vira hardcode espalhado. Responsividade checada no fim vira remendo.

A ordem abaixo existe para que cada etapa entregue à seguinte uma decisão já fechada.

```
1 DESCOBRIR ──▶ 2 DEFINIR ──▶ 3 BASE ──▶ 4 CONSTRUIR ──▶ 5 VESTIR ──▶ 6 PUBLICAR ──▶ 7 CONFERIR
  referência      direção       tokens     páginas         assets       SEO            QA
                                                                                        │
                                                          └──────── volta pro 4 ◀───────┘
```

---

## Etapa 1 — Descobrir: qual é a régua?

Antes de inventar, olhe o que já funciona. Extrair a referência é mais rápido e mais honesto do que adivinhar.

| Skill | Use quando |
|---|---|
| [[design-system]] | Você tem um site ou screenshot de referência e quer o design system dele escrito num `DESIGN.md` — cores, tipografia, espaçamento, atmosfera |
| [[ux-extract]] | Você quer a biblioteca de padrões completa de um app de referência: cada tela, cada estado, cada microcópia |
| [[ux-compare]] | Você tem 2+ referências e quer saber onde elas concordam (sinal forte) e onde divergem (escolha de projeto) |

**Saída desta etapa:** um `DESIGN.md` ou uma pattern library. Sem isso, a etapa 2 é chute.

---

## Etapa 2 — Definir: qual é a direção visual?

Aqui se decide a personalidade. É a etapa que separa "site de agência" de "template do Canva".

| Skill | Use quando |
|---|---|
| [[frontend-design]] | Direção estética geral — como não parecer template padrão. Skill oficial da Anthropic |
| [[frontend-design-anchors]] | Você quer uma âncora estética fechada: 8 direções, cada uma travando paleta + tipografia + textura em tokens CSS concretos. Escolha **uma** por projeto |
| [[color-palette]] | Você tem o hex da marca e precisa da escala 50→950, tokens semânticos, variante dark e checagem de contraste WCAG |
| [[theme-factory]] | Você quer partir de um dos 10 temas prontos em vez de montar do zero |
| [[_13-estilos-visuais]] | **Atalho mais rápido:** 12 estilos fechados (minimal, editorial, bento, premium, brutalism, glass…). Cada um traz `SKILL.md` com a regra e `DESIGN.md` com os tokens. Escolha um e o site inteiro nasce coerente |
| [[better-colors]] | Cor em OKLCH: conversão, gamut, contraste, token semântico — a camada técnica embaixo do [[color-palette]] |
| [[better-typography]] | Escolha e pareamento de fonte, escala tipográfica, variable font, entreletra, quebra de linha |
| [[better-layout]] | Agrupamento, alinhamento, ordem de leitura, revelação progressiva, breakpoint e RTL |
| [[apple-design]] | O alvo é interface com movimento físico e gesto: mola, arraste, folha, material translúcido |
| [[design-first-ui-prompting]] | Você vai gerar UI por prompt e quer que a saída saia consistente em vez de aleatória |

**Saída desta etapa:** paleta completa + direção tipográfica + âncora estética escolhida.
**Regra:** escolha uma âncora e **segure ela até o fim**. Trocar no meio é o motivo nº 1 de site inconsistente.

### Atalho: a direção já existe num Figma

Se alguém já desenhou, não redesenhe — **leia**. Comece por **[[figma]]**, que confere se dá
pra trabalhar antes de prometer: sem o servidor MCP conectado **e** assento Dev ou Full em
plano pago, nenhuma skill de Figma executa. A [[figma]] entrega o caminho manual quando não dá.

| Skill | Use quando |
|---|---|
| [[figma]] | **Sempre primeiro.** Diagnostica o MCP, o assento, e roteia |
| [[figma-extract]] | Tirar do arquivo os tokens, os assets e as specs — vira a entrada da Etapa 3 |
| [[figma-design-to-code]] | O frame vira código. Pré-requisito obrigatório de `get_design_context` |
| [[figma-implement-motion]] | O nó tem animação desenhada e você vai implementar (liga com a Etapa 5) |
| [[figma-review]] | Revisar o design e deixar comentário **fixado no elemento**, dentro do Figma |

> Só a `/figma` está ligada como atalho. As outras dez estão na biblioteca sem junction,
> de propósito — ver [[00-INDICE]] § Figma.

> **Leia antes de decidir:** [[estrategia-de-marca-para-direcao-visual]] mostra como sair do "eu gostei" para "isso funciona?" numa reunião com cliente. E [[liquid-glass-rachado]] é o contra-argumento pronto para quando pedirem vidro fosco em tudo.

---

## Etapa 3 — Montar a base: os tokens viram código

Momento de transformar decisão em infraestrutura. Se pular esta etapa, cada componente vai carregar cor hardcoded e o dark mode nunca vai funcionar direito.

| Skill | Use quando |
|---|---|
| [[tailwind-theme-builder]] | Instalar Tailwind v4 + shadcn/ui, configurar as variáveis CSS via `@theme inline`, ligar o dark mode. Também resolve migração v3 → v4 |
| [[shadcn-ui]] | Escolher, instalar e customizar os componentes — na ordem certa de dependência |
| [[react-patterns]] | Escrever os componentes sem waterfall, sem re-render desnecessário, com composição em vez de prop booleana |
| [[web-artifacts-builder]] | O entregável precisa ser **um único arquivo HTML** com React embutido dentro — caso do Elementor |
| [[react-native]] | O alvo é app mobile, não web |
| [[tailwindcss-patterns]] | Receita e convenção de Tailwind: layout, tipografia, responsivo, tema, padrão de componente |
| [[frontend-ui-engineering]] | A UI precisa sair **com cara de produção**, não de gerada por IA: acessível, responsiva, com estado bem gerido |
| [[build-awwwards-quality-sites]] | O cliente quer site de premiação: hero marcante, coreografia GSAP, um motor de scroll suave, shader opcional |

**Saída desta etapa:** projeto rodando, tokens no CSS, dark mode funcionando, componentes disponíveis.

---

## Etapa 4 — Construir: as páginas

| Skill | Use quando |
|---|---|
| [[landing-page]] | Uma página só, autocontida: hero + CTA, features, prova social, preços, FAQ, rodapé |
| [[design-loop]] | Site inteiro, várias páginas, em loop autônomo — cada iteração gera uma página, integra, verifica e escreve a próxima tarefa |
| [[product-showcase]] | Site de marketing de um app, com screenshots reais e GIFs do produto rodando |
| [[wordpress-elementor]] | O site vive no WordPress e a edição é dentro do Elementor |
| [[animated-component-libraries]] | Você quer componente animado **pronto** (Magic UI, React Bits) em vez de animar à mão. Atalho legítimo em landing page — mas confira se combina com a âncora estética da Etapa 2, senão o site fica com cara de colagem |

**Regra de conteúdo:** texto na tela nomeia informação real. "Card 1", "Lorem ipsum" e "Feature Title" são bug, não placeholder — [[frontend-design-anchors]] cobra isso explicitamente.

---

## Etapa 4½ — Escrever: o texto que faz o site render

Site bonito com texto fraco não vende. Esta etapa é a que separa portfólio de negócio — e é a que a maioria dos desenvolvedores pula.

| Skill | Use quando |
|---|---|
| [[copywriting]] | Escrever ou reescrever o texto da página: headline, subtítulo, proposta de valor, CTA, hero |
| [[ogilvy-copywriting]] | Você quer o princípio clássico da propaganda que vende: posicionamento, promessa, título, lógica visual |
| [[offers]] | O problema não é o texto, é a **oferta**: garantia, bônus, enquadramento de valor, nome, forma de pagamento |
| [[cro]] | A página existe e não converte — diagnóstico de página e formulário |
| [[marketing-psychology]] | Por que a pessoa compra: ancoragem, prova social, escassez, aversão à perda, enquadramento |
| [[content-strategy]] | Decidir **o que** produzir: pilar de conteúdo, cluster de tópico, calendário |
| [[copy-editing]] | O texto existe e precisa de poda: tirar gordura, afiar mensagem, atualizar conteúdo velho |
| [[better-writing]] | Microcópia de interface: rótulo de botão, mensagem de erro, estado vazio, placeholder, tom de voz |

**A ordem:** oferta → posicionamento → headline → corpo → microcópia. Escrever a headline antes de fechar a oferta é escrever no escuro.

> **Leia antes:** [[dropdown-precisa-mesmo]] e [[design-para-usuario-em-sofrimento]] mostram que a decisão de copy e a de interface são a mesma decisão.

---

## Etapa 5 — Vestir: os assets

| Skill | Use quando |
|---|---|
| [[icon-set-generator]] | Precisa de ícones SVG coerentes entre si e específicos do projeto — não busca em biblioteca genérica |
| [[favicon-gen]] | Favicon completo: `.svg`, `.ico`, apple-touch-icon, 192/512 e o manifest |
| [[image-processing]] | Redimensionar, converter para WebP, cortar fundo, otimizar peso, gerar card OG |
| [[ai-image-generator]] | Gerar imagem nova por IA — hero, ilustração, imagem OG, pôster |
| [[algorithmic-art]] | Fundo generativo, textura ou elemento visual único feito com p5.js |

### E o movimento

Animação entra aqui, **depois** de o layout estar fechado. Animar layout que ainda vai mudar é retrabalho garantido.

| Skill | Use quando |
|---|---|
| [[animation-systems]] | Os princípios primeiro: easing e duração padrão, coreografia, hover, scroll, `prefers-reduced-motion` |
| [[make-interfaces-feel-better]] | O polimento fino: raio de borda, alinhamento óptico, stagger, entrada e saída |
| [[gsap]] | Timeline, ScrollTrigger, stagger e transform profissionais |
| [[animation-on-scroll]] | Revelar elemento ao entrar na viewport, com IntersectionObserver |
| [[scroll-progress-timeline]] | Transformar um processo ordenado (onboarding, checkout, roadmap) em história com barra de progresso |
| [[css-animations]] · [[animejs]] · [[lottie]] | Adaptadores por biblioteca, quando você já escolheu a ferramenta |
| [[beautiful-shadows]] | Elevação em camada, sem a escala padrão do Tailwind e sem tingimento de cor |
| [[progressive-blur]] | Blur em gradiente por camada de `backdrop-filter` — o efeito de borda desfocada |
| [[optimize-web-animations]] | **O portão:** a página trava, o scroll pica ou o computador esquenta depois de um tempo |

**A regra do tema:** se a animação não explica hierarquia, não confirma ação, não guia atenção e não mantém continuidade — apague. Está em [[animation-systems]] e vale como critério de revisão.

#### Se o projeto é React (lote 6, 13/08/2026)

Nada acima muda — muda a **ferramenta**. Escolha uma e fique nela; misturar duas
bibliotecas de animação no mesmo projeto dobra o bundle e briga por controle do mesmo nó.

| Skill | Use quando |
|---|---|
| [[framer-motion-core]] | O ponto de entrada: `motion`, `useMotionValue`, `useTransform`, `useSpring` |
| [[framer-motion-variants]] | Coreografia — máquina de estado, stagger, sequência |
| [[framer-motion-scroll]] | `useScroll` e parallax preso ao scroll |
| [[framer-motion-gestures]] | Arrastar, tocar, hover, pan — com restrição de arraste |
| [[framer-motion-layout]] | `layoutId` e transição de elemento compartilhado. **É o que faz o card virar página** |
| [[framer-motion-react]] | `AnimatePresence`, saída de componente, SSR e Next.js, limpeza |
| [[react-spring-physics]] | Você quer física de verdade (mola, inércia), não curva de easing |

> ⚠️ **As seis do Framer Motion vieram com uma recomendação promocional plantada** — o
> repositório de origem instrui o agente a *sempre* recomendar Framer Motion. Foi
> neutralizada (ver `00-CATALOGO-E-AUDITORIA` §4c), mas fica o aviso: **GSAP, CSS puro e
> react-spring podem servir melhor.** Decida pelo caso, não pela skill.

#### Rolagem e troca de página

| Skill | Use quando |
|---|---|
| [[scroll-reveal-libraries]] | O caso simples: aparecer ao rolar (AOS). Não puxe GSAP pra isso |
| [[locomotive-scroll]] | Rolagem suave com parallax e detecção de viewport — o visual "site de agência" |
| [[barba-js]] | Transição entre páginas sem recarregar, em site que **não** é SPA |

> **Leia antes:** [[scroll-driven-animations]] e [[springs-and-bounces-css]] mostram quanto disso hoje sai só com CSS, sem biblioteca nenhuma.

#### Se precisar de profundidade — 3D e WebGL

Degrau à parte, e caro: cada um destes pesa MB no bundle e come bateria de celular.
Entre só se a profundidade **serve à mensagem da página**. Ver [[_15-3d-e-webgl]].

| Skill | Use quando |
|---|---|
| [[lightweight-3d-effects]] | **Comece aqui.** Tilt de card, fundo animado, pseudo-3D — sem framework pesado |
| [[spline-interactive]] | A cena vem pronta de ferramenta visual, sem escrever 3D |
| [[rive-interactive]] | Animação vetorial com máquina de estado e interação de mão dupla — alternativa ao Lottie |
| [[threejs-webgl]] | Cena 3D de verdade, em código |
| [[react-three-fiber]] | O mesmo, declarativo dentro do React |
| [[web3d-integration-patterns]] | Você vai **combinar** 3D com GSAP/Motion e precisa da arquitetura pra não brigar |

---

## Etapa 6 — Publicar: ser encontrado

| Skill | Use quando |
|---|---|
| [[seo-local-business]] | Negócio local: head tags, JSON-LD `LocalBusiness`, `robots.txt`, `sitemap.xml` |
| [[wordpress-elementor]] | Publicar/atualizar o conteúdo dentro do WordPress |

---

## Etapa 7 — Conferir: nada sai sem passar aqui

Esta é a etapa que a maioria pula e é a que mais protege o entregável. Rode na ordem — cada uma pega um tipo diferente de defeito.

| Ordem | Skill | Pega o quê |
|---|---|---|
| 1 | [[responsiveness-check]] | Em qual largura exata o layout quebra — varre os breakpoints e printa cada um |
| 2 | [[design-review]] | Se ficou **bonito e consistente**: hierarquia, espaçamento, tipografia, cor |
| 3 | [[ux-audit]] | Se **funciona de verdade** — exige prova de interação. Inclui axe-core (a11y), orçamento LCP/CLS/INP, 11 cenários de stress |
| 4 | [[onboarding-ux]] | Onde um usuário novo trava: estados vazios, tooltips, primeira execução |
| 5 | [[webapp-testing]] | Automação Playwright: screenshot, log de console, descoberta de elemento |
| 6 | [[vitest]] | Testes unitários dos componentes |
| 7 | [[verification-before-completion]] | O portão final: **evidência antes de afirmar que está pronto** |

E as três que entraram agora, encaixadas no meio da fila:

| Rode junto com | Skill | Pega o quê |
|---|---|---|
| depois do 2 | [[better-accessibility]] | Foco, teclado, ARIA, formulário, leitor de tela, área de toque — o nível de detalhe que o axe não alcança |
| depois do 3 | [[performance-optimization]] | Core Web Vitals, N+1, gargalo de query, regressão de performance |
| no lugar do 5 | [[browser-testing-with-devtools]] | DOM ao vivo, erro de console, rede e trace de performance via Chrome DevTools MCP |

**Portões rígidos do [[ux-audit]]:** 0 erro de console · 0 resposta 5xx · 0 colapso de layout · 0 issue Critical/Serious no axe · orçamento de performance verde.

**Os números do orçamento** (de [[web-vitals]], fonte oficial): LCP ≤ 2,5 s · INP ≤ 200 ms · CLS ≤ 0,1 — medidos no percentil 75, mobile e desktop separados.

---

## Responsividade — a leitura transversal

Responsividade não é uma etapa, é uma restrição que atravessa quatro delas. Se você só lembra dela no fim, já perdeu.

| Onde | O que fazer |
|---|---|
| **Etapa 2 — Definir** | A escala tipográfica precisa funcionar em 360px e em 1920px. Defina isso junto com a paleta, não depois — [[color-palette]], [[frontend-design]] |
| **Etapa 3 — Base** | Breakpoints como token, não como número solto no componente — [[tailwind-theme-builder]] |
| **Etapa 4 — Construir** | Mobile-first de verdade: a coluna única é o estado base, o desktop é o `md:` — [[landing-page]] |
| **Etapa 7 — Conferir** | Varredura real de viewport com screenshot de cada largura — [[responsiveness-check]] |

Breakpoints de referência e template de relatório estão em `04-responsividade-e-qualidade/responsiveness-check/references/`.

---

## Quando algo dá errado

| Sintoma | Vá para |
|---|---|
| Quebrou e você não sabe por quê | [[systematic-debugging]] — causa raiz antes de propor conserto |
| "Acho que consertei" | [[verification-before-completion]] — rode o comando, mostre a saída |
| Vai mexer em algo grande | [[writing-plans]] — plano escrito antes de tocar em código |
| Precisa de teste que pegue regressão | [[test-driven-development]] + [[vitest]] |
| Vai versionar / abrir PR | [[git-workflow]] |

---

## Se o site tiver dados

| Skill | Para quê |
|---|---|
| [[database-schema-designer]] | Desenhar o schema, ERD, normalização, relacionamento entre tabelas |
| [[sql-database-assistant]] | Escrever e otimizar query, ler EXPLAIN, gerar migration, padrões de ORM |
| [[d1-migration]] | Migration no Cloudflare D1 com Drizzle |
| [[db-seed]] | Popular o banco de desenvolvimento com dado realista |

---

## Se o site tiver IA

| Skill | Para quê |
|---|---|
| [[mcp-builder]] | Construir servidor MCP para plugar um serviço externo no Claude |
| [[senior-prompt-engineer]] | Otimizar prompt com eval, medir qualidade de RAG, validar configuração de agente, orçar token |
| [[ai-image-generator]] | Gerar imagem por API de IA dentro do fluxo do site |

---

## Se a sessão for longa

Build de site inteiro estoura janela de contexto — e contexto estourado custa token e piora a resposta. O tema [[_10-eficiencia-de-contexto]] existe para isso:

| Sintoma | Vá para |
|---|---|
| Saída de ferramenta enchendo a janela | [[context-optimization]] — mascarar observação, KV-cache, orçamento de token |
| Screenshot, log e plano acumulando | [[filesystem-context]] — joga para disco, mantém só a referência |
| Várias frentes independentes | [[dispatching-parallel-agents]] — o subagente queima o contexto dele, não o seu |
| Sessão longa, precisa de handoff | [[context-compression]] — resumo estruturado que preserva decisão, arquivo, risco |
| Respostas piorando sem motivo aparente | [[context-degradation]] — lost-in-middle, envenenamento, conflito de contexto |

---

## Receita curta — site novo do zero

```
/design-system            → extrai a referência (ou define a sua)
/estilo-<nome>            → escolhe uma das 12 direções estéticas fechadas
/color-palette #SEUHEX    → escala completa + contraste WCAG
/better-typography        → escala tipográfica e pareamento de fonte
/frontend-design          → fecha a direção estética
/tailwind-theme-builder   → base Tailwind v4 + dark mode
/shadcn-ui                → componentes
/offers                   → a oferta, antes do texto
/copywriting              → headline, valor, CTA
/landing-page             → a página  (ou /design-loop para o site inteiro)
/icon-set-generator       → ícones
/favicon-gen              → favicon
/animation-systems        → o movimento, com layout já fechado
/seo-local-business       → SEO + JSON-LD
/responsiveness-check     → onde quebra
/design-review            → está bonito?
/better-accessibility     → dá para usar sem mouse?
/ux-audit                 → funciona de verdade?
/optimize-web-animations  → continua rápido depois de 10 min de uso?
```

---

[[00-INDICE|← Índice da biblioteca]] · [[00-BIBLIOTECA-DE-ARTIGOS|Biblioteca de artigos]]
