# 📘 Guia das skills — o que cada uma faz e quanto gasta

> Gerado em **2026-09-13** a partir dos arquivos que estão instalados nesta máquina.
> **223 skills** no total: 131 globais da biblioteca, 49 locais do agente,
> 13 do plugin Cloudflare, 1 de projeto, 10 de Figma desligadas,
> 17 embutidas no Claude Code e 2 comandos do plugin.
>
> Os números de tamanho foram **medidos** nos arquivos. Os níveis de gasto são **classificação
> minha**, com o critério explicado abaixo e o motivo escrito em cada skill.

---

## Como ler este guia

### Os dois jeitos de uma skill gastar

1. **Custo fixo — você paga sem usar.** A descrição de toda skill instalada entra na lista que o
   Claude recebe no começo de **toda** sessão, para ele saber que ela existe. Hoje isso soma
   **~13,9 mil tokens** só com as globais e o plugin, e mais **~5,7 mil tokens** quando
   você trabalha dentro do projeto do agente.
2. **Custo de uso — você paga quando ela roda.** A instrução da skill (o `SKILL.md`) entra inteira
   no contexto; as referências entram só se a skill mandar ler; e o que ela **faz** (abrir
   navegador, disparar agentes, repetir) é o que mais pesa.

### A escala do custo de uso

| Nível | Nome | O que caracteriza |
|---|---|---|
| 🟢 1 | Mínimo | Instrução curta (até ~2 mil tokens) e nada caro acontece. Ou um script faz o trabalho fora do modelo |
| 🟢 2 | Leve | Instrução média (2 a 6 mil tokens), trabalho de conversa ou texto, ou script local |
| 🟡 3 | Médio | Instrução grande, referências longas, leitura de muitos arquivos do projeto ou web pontual |
| 🟠 4 | Alto | Navegador real com capturas de tela, varredura do projeto inteiro, rodadas de verificação ou um subagente |
| 🔴 5 | Muito alto | Vários subagentes em paralelo ou loop autônomo que se repete sozinho |

**Duas medidas reais que sustentam a escala:**

- **Um subagente é uma sessão inteira.** Nesta própria máquina, em 13/09/2026, cada um dos 6
  agentes que completaram as notas da trilha de aprendizado gastou **entre 208 mil e 291 mil
  tokens** (medido pelo próprio Claude Code ao fim de cada um). Antes deles, oito agentes em
  paralelo estouraram o limite de uso da sessão duas vezes seguidas.
- **Imagem custa caro.** Pela documentação da Anthropic, uma imagem custa ⌈largura ÷ 28⌉ ×
  ⌈altura ÷ 28⌉ tokens. Uma captura de tela Full HD (1920×1080) custa **2.691 tokens** no Opus 5,
  o equivalente a umas 2 mil palavras de texto. Skill que tira uma captura por estado de tela
  multiplica isso.

### Os símbolos

| Símbolo | Significa |
|---|---|
| 💲 | Gasta **dinheiro fora da assinatura do Claude** (API paga de outra empresa, assento pago) |
| 🔌 | Só funciona com um serviço ou servidor MCP externo conectado |
| 🖥️ | O trabalho pesado roda **na sua máquina** (ffmpeg, Python, GPU): quase não gasta token |
| 📍 | Só vale dentro de um projeto (aparece quando você trabalha naquela pasta) |

### O que "Medido" quer dizer

- **Instrução:** tamanho do `SKILL.md` em tokens, estimado como caracteres ÷ 4 (margem de uns 25%;
  texto em português costuma render um pouco mais de tokens).
- **Referências:** soma dos outros `.md` da pasta da skill. É o **teto**: ela só lê o que a
  situação pede.
- **Custo fixo por sessão:** tamanho da descrição, também em tokens estimados.
- O custo **real** de uma execução depende da tarefa: ler um repositório gigante ou um projeto
  enorme custa mais que qualquer instrução.

---

## Resumo em números

**Distribuição pelo pior caso de cada skill** (as 205 que carregam; as 10 de Figma
desligadas ficam fora):

| Nível | Quantas |
|---|---|
| 🟢 1 · Mínimo | 52 |
| 🟢 2 · Leve | 60 |
| 🟡 3 · Médio | 58 |
| 🟠 4 · Alto | 21 |
| 🔴 5 · Muito alto | 14 |

**🔴 As que chegam ao nível 5** — use quando o resultado vale, e prefira ondas pequenas:
`/code-review`, `/criar-skill`, `/deep-dive`, `/design-loop`, `/dispatching-parallel-agents`, `/ler-repositorio`, `/loop`, `/pesquisa-profunda`, `/product-showcase`, `/schedule`, `/subagent-driven-development`, `/ux-audit`, `/ux-extract`, `/writing-skills`.

**💲 As que gastam dinheiro fora da assinatura:** `/ai-image-generator` (cada imagem é cobrada
pela Google ou pela OpenAI), `/figma` e as 10 de Figma (exigem assento Dev ou Full em plano pago
da Figma) e `/code-review` no modo `ultra` (revisão na nuvem cobrada à parte). Para imagem sem
custo, a `/criar-imagem` gera localmente pelo Fooocus.

**As 12 instruções mais longas** (entram inteiras quando a skill roda):

| Skill | Instrução |
|---|---|
| `/criar-skill` | ~9,3 mil tokens |
| `/ux-audit` | ~8,6 mil tokens |
| `/humanizer` | ~8,5 mil tokens |
| `/turnstile-spin` | ~7,2 mil tokens |
| `/subagent-driven-development` | ~7,0 mil tokens |
| `/writing-skills` | ~6,6 mil tokens |
| `/long-horizon-prompting` | ~6,4 mil tokens |
| `/react-three-fiber` | ~5,7 mil tokens |
| `/lightweight-3d-effects` | ~5,7 mil tokens |
| `/animated-component-libraries` | ~5,6 mil tokens |
| `/apple-design` | ~5,6 mil tokens |
| `/cloudflare-one` | ~5,6 mil tokens |

**As 10 descrições mais longas** (pagas em toda sessão, usando ou não):

| Skill | Custo fixo por sessão |
|---|---|
| `/reels-estrategista` | ~250 tokens |
| `/ler-repositorio` | ~240 tokens |
| `/algoritmos-na-pratica` | ~240 tokens |
| `/offers` | ~240 tokens |
| `/estudar` | ~240 tokens |
| `/desenhar-sistema` | ~240 tokens |
| `/ux-audit` | ~240 tokens |
| `/construir-do-zero` | ~240 tokens |
| `/ia-local` | ~220 tokens |
| `/fundacao-app-web` | ~210 tokens |

> As 5 skills novas de aprendizado estão entre as descrições mais longas (~950 caracteres cada).
> É uma troca consciente: descrição detalhada faz o Claude acionar a skill na hora certa, e isso
> custa uns 240 tokens por skill em toda sessão.

---

## 🎓 As 5 skills novas, em detalhe

Criadas em 13/09/2026 a partir da trilha `A:\Claude\02-cerebro\70-aprendizado\`. As duas
primeiras da lista abaixo já rodaram em caso real.

### `/algoritmos-na-pratica` — 🟡 3 · Médio
**O que faz.** Dois modos.
- **Consertar:** acha no seu código o que fica lento quando os dados crescem (laço dentro de laço,
  `includes` ou `filter` dentro de laço, `shift()`, cópia de array a cada volta, ordenação
  repetida, consulta ao banco por item). Mede em pelo menos 3 tamanhos, antes e depois, e prova
  com um teste de equivalência que o resultado não mudou. Se o número real de itens é pequeno,
  recomenda **não** mexer.
- **Treinar:** passa um problema e conduz os 6 passos (esclarecer, exemplos, força bruta,
  otimizar, codar, testar) com dica graduada, sem entregar a resposta.

**Custo medido no teste real (enquetes do Trindade):** 3 arquivos lidos, uma bancada escrita e
rodada no Node. Achou uma listagem quadrática que leva 173 ms com 1.000 enquetes num canal e cai
para 0,7 ms com a troca.

**Quando usar:** "isso tá lento", "trava com muitos itens", "Map ou objeto?", "quero treinar
algoritmo". **Não é para** página lenta por rede ou renderização (aí é `/performance-optimization`).

### `/desenhar-sistema` — 🟡→🟠 3 a 4 · Médio a alto
**O que faz.** Aplica o método de 4 passos do System Design Primer a um projeto seu, na escala
verdadeira dele:
1. casos de uso, o que fica de fora e suposições com faixa;
2. estimativa com as contas à vista, na unidade que o provedor cobra (linhas lidas, CPU por
   requisição);
3. desenho de alto nível e componentes;
4. decisões de banco, cache, fila, consistência e ponto único de falha, cada uma com trade-off e
   "o que faria mudar".

Entrega um documento de design com a lista do que **não** fazer agora.

**Custo medido no teste real (Bene):** leu cerca de 10 arquivos do projeto e 3 páginas da
documentação da Cloudflare, e rodou 2 bancadas (D1 local e CPU). Achou o risco de 7 buscas por dia esgotarem o
banco gratuito.

**Quando usar:** "isso aguenta X usuários?", "preciso de cache/fila?", "SQL ou NoSQL?", antes de
começar um backend.

### `/estudar` — 🟢→🟡 2 a 3 · Leve a médio
**O que faz.** Três modos:
- **aprender** um tema: diagnóstico, um mecanismo por vez, exercício que você roda, pegadinha,
  perguntas sem consulta;
- **revisar** o que venceu hoje na fila de revisão espaçada;
- **roteiro**: plano de estudo para um objetivo ou projeto.

As datas da revisão são calculadas pelo script `revisao.py`, não pelo modelo.

**Custo:** instrução de ~2,5 mil tokens mais a nota da trilha estudada (de 3 a 12 mil tokens). O
modo revisar é o mais barato.

### `/ler-repositorio` — 🟡→🔴 3 a 5 · Médio a muito alto
**O que faz.** Estuda um repositório do GitHub sem executar nada:
1. confere os metadados na API;
2. clona raso em quarentena;
3. **neutraliza as instruções para agentes que vêm dentro dele** (`CLAUDE.md`, `.claude/`,
   `AGENTS.md`);
4. lê na ordem certa e segue uma funcionalidade de ponta a ponta com arquivo e linha;
5. escreve a nota de fonte.

**Custo:** 3 para um repositório pequeno; 4 para um monorepo gigante; 5 quando é uma lista
dividida entre agentes. A própria skill limita a ondas de 3 agentes.

### `/construir-do-zero` — 🟢→🟡 2 a 3 · Leve a médio
**O que faz.** Reconstrói uma tecnologia (Git, React, servidor HTTP, motor de template, navegador,
compilador) em marcos que rodam, cada um com teste. **Você escreve o código**; o Claude explica,
revisa e dá dica em 6 degraus. Fecha comparando com a ferramenta real e com uma nota de
aprendizado.

**Custo:** barato por sessão. O projeto inteiro soma várias sessões, e esse é o objetivo.

---
# Parte 1 — Biblioteca global

Valem em **qualquer** projeto. Moram em `30-sistema/biblioteca-skills/` e chegam ao Claude por junction em `~/.claude/skills/`.

## 🧱 Estrutura e layout — 4 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/design-loop` | 🔴 5 · Muito alto | Constrói um site de várias páginas sozinho: cada volta gera uma página em HTML/Tailwind, integra… |
| `/landing-page` | 🟡 3 · Médio | Gera uma landing page completa num único HTML com Tailwind, responsiva, com modo escuro, SEO básico… |
| `/product-showcase` | 🔴 5 · Muito alto | Gera um site de marketing de várias páginas para um app, navegando no app rodando e capturando… |
| `/web-artifacts-builder` | 🟡 3 · Médio | Monta artifacts HTML elaborados para o claude.ai com React, Tailwind e shadcn/ui, empacotados num… |

#### `/design-loop` — 🔴 5 · Muito alto

- **O que faz:** Constrói um site de várias páginas sozinho: cada volta gera uma página em HTML/Tailwind, integra, confere visualmente e escreve a próxima tarefa.
- **Quando usar:** 'Constrói o site todo', 'segue fazendo as páginas'.
- **Por que esse gasto:** Loop autônomo com verificação visual a cada página. Cresce com o número de páginas.
- **Medido:** instrução ~5,2 mil tokens · custo fixo por sessão: ~130 tokens

#### `/landing-page` — 🟡 3 · Médio

- **O que faz:** Gera uma landing page completa num único HTML com Tailwind, responsiva, com modo escuro, SEO básico e seções prontas.
- **Quando usar:** Página de lançamento, página de captura, 'em breve'.
- **Por que esse gasto:** Instrução curta, mas a saída é um arquivo HTML grande.
- **Medido:** instrução ~1,6 mil tokens · custo fixo por sessão: ~120 tokens

#### `/product-showcase` — 🔴 5 · Muito alto

- **O que faz:** Gera um site de marketing de várias páginas para um app, navegando no app rodando e capturando telas e GIFs dos fluxos.
- **Quando usar:** Explicar e vender um app complexo.
- **Por que esse gasto:** Navega o app, captura muitas telas e sequências e gera várias páginas. Imagem custa caro (uma tela Full HD ≈ 2,7 mil tokens).
- **Medido:** instrução ~5,0 mil tokens · custo fixo por sessão: ~130 tokens

#### `/web-artifacts-builder` — 🟡 3 · Médio

- **O que faz:** Monta artifacts HTML elaborados para o claude.ai com React, Tailwind e shadcn/ui, empacotados num arquivo.
- **Quando usar:** Artifact com estado, rotas ou componentes shadcn.
- **Por que esse gasto:** Instala dependências e builda um bundle.
- **Medido:** instrução ~770 tokens · custo fixo por sessão: ~70 tokens · 2 script(s)
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina

---

## 🎨 Design visual — 13 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/apple-design` | 🟡 3 · Médio | A abordagem da Apple para interface e movimento físico, traduzida para a web: gestos, springs… |
| `/better-colors` | 🟢 2 · Leve | Cor em OKLCH: conversão, paletas, contraste, gamut, temas no Tailwind v4 e cor com significado. |
| `/better-interface` | 🟠 4 · Alto | Revisão de interface que coordena seis outras skills (acessibilidade, layout, escrita, tipografia… |
| `/better-layout` | 🟢 2 · Leve | Estrutura de layout: agrupamento, alinhamento, ordem de leitura, divulgação progressiva e… |
| `/better-typography` | 🟡 3 · Médio | Tipografia web completa: escolha e par de fontes, variáveis, escala, hierarquia, quebra de linha e… |
| `/better-ui` | 🟢 2 · Leve | Detalhes que fazem a interface parecer polida: estados de hover, sombras, bordas, microinterações… |
| `/color-palette` | 🟡 3 · Médio | Gera paleta acessível completa a partir de um hex: 11 tons, tokens semânticos, modo escuro, CSS do… |
| `/design-first-ui-prompting` | 🟢 1 · Mínimo | Estrutura de prompt 'design primeiro' para gerar UI consistente. |
| `/design-review` | 🟠 4 · Alto | Revisão visual de página ou app (layout, tipografia, espaço, cor, hierarquia, responsivo), com… |
| `/design-system` | 🟠 4 · Alto | Extrai o design system de um site ou captura para um DESIGN.md: cores, tipografia, componentes… |
| `/frontend-design` | 🟢 2 · Leve | Direção visual intencional para UI nova, fugindo do visual de template. |
| `/frontend-design-anchors` | 🟢 2 · Leve | Direção visual sustentada por paleta, tipografia, estrutura e textura, com textos que nomeiam… |
| `/theme-factory` | 🟢 1 · Mínimo | Aplica um de 10 temas prontos (cores e fontes) a slides, documentos, relatórios ou páginas. |

#### `/apple-design` — 🟡 3 · Médio

- **O que faz:** A abordagem da Apple para interface e movimento físico, traduzida para a web: gestos, springs, materiais, tipografia.
- **Quando usar:** Interface com arrasto, folhas, springs e profundidade.
- **Por que esse gasto:** Instrução grande (~5,6 mil tokens).
- **Medido:** instrução ~5,6 mil tokens · custo fixo por sessão: ~110 tokens

#### `/better-colors` — 🟢 2 · Leve

- **O que faz:** Cor em OKLCH: conversão, paletas, contraste, gamut, temas no Tailwind v4 e cor com significado.
- **Quando usar:** Paleta, contraste, tokens de cor, modo escuro.
- **Por que esse gasto:** Instrução curta com referências sob demanda.
- **Medido:** instrução ~1,9 mil tokens · referências lidas sob demanda: até ~4,3 mil tokens · custo fixo por sessão: ~110 tokens

#### `/better-interface` — 🟠 4 · Alto

- **O que faz:** Revisão de interface que coordena seis outras skills (acessibilidade, layout, escrita, tipografia, cor, UI).
- **Quando usar:** Só quando você pede uma revisão holística da tela ou do fluxo.
- **Por que esse gasto:** Carrega várias skills numa revisão só.
- **Medido:** instrução ~2,0 mil tokens · custo fixo por sessão: ~110 tokens

#### `/better-layout` — 🟢 2 · Leve

- **O que faz:** Estrutura de layout: agrupamento, alinhamento, ordem de leitura, divulgação progressiva e breakpoints.
- **Quando usar:** Organizar uma página ou componente.
- **Por que esse gasto:** Instrução média com referências sob demanda.
- **Medido:** instrução ~2,1 mil tokens · referências lidas sob demanda: até ~3,2 mil tokens · custo fixo por sessão: ~150 tokens

#### `/better-typography` — 🟡 3 · Médio

- **O que faz:** Tipografia web completa: escolha e par de fontes, variáveis, escala, hierarquia, quebra de linha e acessibilidade.
- **Quando usar:** Escolher fontes, montar escala tipográfica, revisar texto na tela.
- **Por que esse gasto:** Instrução média com ~24 KB de referências.
- **Medido:** instrução ~3,8 mil tokens · referências lidas sob demanda: até ~6,3 mil tokens · custo fixo por sessão: ~190 tokens

#### `/better-ui` — 🟢 2 · Leve

- **O que faz:** Detalhes que fazem a interface parecer polida: estados de hover, sombras, bordas, microinterações, ícones.
- **Quando usar:** 'Tá estranho', 'deixa mais refinado'.
- **Por que esse gasto:** Instrução média com referências.
- **Medido:** instrução ~2,4 mil tokens · referências lidas sob demanda: até ~7,0 mil tokens · custo fixo por sessão: ~120 tokens

#### `/color-palette` — 🟡 3 · Médio

- **O que faz:** Gera paleta acessível completa a partir de um hex: 11 tons, tokens semânticos, modo escuro, CSS do Tailwind v4 e checagem WCAG.
- **Quando usar:** Você tem a cor da marca e precisa do sistema de cores.
- **Por que esse gasto:** Instrução média e saída longa de tokens.
- **Medido:** instrução ~3,8 mil tokens · custo fixo por sessão: ~100 tokens

#### `/design-first-ui-prompting` — 🟢 1 · Mínimo

- **O que faz:** Estrutura de prompt 'design primeiro' para gerar UI consistente.
- **Quando usar:** Antes de pedir geração de interface.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~760 tokens · referências lidas sob demanda: até ~1,4 mil tokens · custo fixo por sessão: ~50 tokens

#### `/design-review` — 🟠 4 · Alto

- **O que faz:** Revisão visual de página ou app (layout, tipografia, espaço, cor, hierarquia, responsivo), com capturas de tela.
- **Quando usar:** 'Isso tá bonito?', 'tá com cara de amador'.
- **Por que esse gasto:** Usa navegador e analisa capturas de tela.
- **Medido:** instrução ~2,1 mil tokens · custo fixo por sessão: ~120 tokens

#### `/design-system` — 🟠 4 · Alto

- **O que faz:** Extrai o design system de um site ou captura para um DESIGN.md: cores, tipografia, componentes, espaço, atmosfera.
- **Quando usar:** 'Qual design esse site usa', 'cria o DESIGN.md'.
- **Por que esse gasto:** Automação de navegador e inspeção de HTML.
- **Medido:** instrução ~2,2 mil tokens · custo fixo por sessão: ~120 tokens

#### `/frontend-design` — 🟢 2 · Leve

- **O que faz:** Direção visual intencional para UI nova, fugindo do visual de template.
- **Quando usar:** Criar ou redesenhar interface.
- **Por que esse gasto:** Instrução média.
- **Medido:** instrução ~2,1 mil tokens · custo fixo por sessão: ~50 tokens

#### `/frontend-design-anchors` — 🟢 2 · Leve

- **O que faz:** Direção visual sustentada por paleta, tipografia, estrutura e textura, com textos que nomeiam informação real em vez de dados de enfeite.
- **Quando usar:** Construir ou reestilizar um front.
- **Por que esse gasto:** Instrução média.
- **Medido:** instrução ~2,6 mil tokens · custo fixo por sessão: ~60 tokens

#### `/theme-factory` — 🟢 1 · Mínimo

- **O que faz:** Aplica um de 10 temas prontos (cores e fontes) a slides, documentos, relatórios ou páginas.
- **Quando usar:** Dar identidade rápida a um artifact.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~780 tokens · referências lidas sob demanda: até ~1,3 mil tokens · custo fixo por sessão: ~70 tokens

---

## ⚛️ Componentes e código — 8 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/animated-component-libraries` | 🟡 3 · Médio | Coleções de componentes animados prontos: Magic UI (150+) e React Bits (90+). |
| `/build-awwwards-quality-sites` | 🟠 4 · Alto | Direção de arte e implementação de sites premiados: hero marcante, GSAP, scroll suave, shaders… |
| `/frontend-ui-engineering` | 🟢 2 · Leve | UI de produção acessível e responsiva: componentes, layouts, estado e WCAG. |
| `/react-native` | 🟢 2 · Leve | Padrões de React Native e Expo: listas, Reanimated, navegação, código por plataforma. |
| `/react-patterns` | 🟢 2 · Leve | Padrões de desempenho do React 19 para Vite + Cloudflare: 50+ regras por impacto. |
| `/shadcn-ui` | 🟢 2 · Leve | Instala e configura componentes shadcn/ui com tokens semânticos e receitas comuns. |
| `/tailwind-theme-builder` | 🟡 3 · Médio | Configura Tailwind v4 + shadcn/ui com tema e modo escuro, instala e verifica. |
| `/tailwindcss-patterns` | 🟢 1 · Mínimo | Receitas rápidas de Tailwind para layout, tipografia, responsivo e temas. |

#### `/animated-component-libraries` — 🟡 3 · Médio

- **O que faz:** Coleções de componentes animados prontos: Magic UI (150+) e React Bits (90+).
- **Quando usar:** Landing ou dashboard com componentes animados sem escrever do zero.
- **Por que esse gasto:** Instrução grande com ~50 KB de referências.
- **Medido:** instrução ~5,6 mil tokens · referências lidas sob demanda: até ~12,8 mil tokens · custo fixo por sessão: ~140 tokens · 2 script(s)

#### `/build-awwwards-quality-sites` — 🟠 4 · Alto

- **O que faz:** Direção de arte e implementação de sites premiados: hero marcante, GSAP, scroll suave, shaders opcionais, acessibilidade.
- **Quando usar:** Site cinematográfico, com muito movimento, para portfólio ou marca.
- **Por que esse gasto:** Projeto grande, com muito código e verificação visual.
- **Medido:** instrução ~1,8 mil tokens · custo fixo por sessão: ~120 tokens

#### `/frontend-ui-engineering` — 🟢 2 · Leve

- **O que faz:** UI de produção acessível e responsiva: componentes, layouts, estado e WCAG.
- **Quando usar:** Construir ou alterar telas e componentes.
- **Por que esse gasto:** Instrução média.
- **Medido:** instrução ~2,7 mil tokens · custo fixo por sessão: ~80 tokens

#### `/react-native` — 🟢 2 · Leve

- **O que faz:** Padrões de React Native e Expo: listas, Reanimated, navegação, código por plataforma.
- **Quando usar:** Só se você fizer app em React Native/Expo.
- **Por que esse gasto:** Instrução média.
- **Medido:** instrução ~2,4 mil tokens · custo fixo por sessão: ~110 tokens

#### `/react-patterns` — 🟢 2 · Leve

- **O que faz:** Padrões de desempenho do React 19 para Vite + Cloudflare: 50+ regras por impacto.
- **Quando usar:** Escrever ou revisar React.
- **Por que esse gasto:** Instrução média.
- **Medido:** instrução ~2,3 mil tokens · custo fixo por sessão: ~130 tokens

#### `/shadcn-ui` — 🟢 2 · Leve

- **O que faz:** Instala e configura componentes shadcn/ui com tokens semânticos e receitas comuns.
- **Quando usar:** Montar UI React com shadcn.
- **Por que esse gasto:** Instrução curta com referências.
- **Medido:** instrução ~1,4 mil tokens · referências lidas sob demanda: até ~4,3 mil tokens · custo fixo por sessão: ~100 tokens

#### `/tailwind-theme-builder` — 🟡 3 · Médio

- **O que faz:** Configura Tailwind v4 + shadcn/ui com tema e modo escuro, instala e verifica.
- **Quando usar:** Começar o tema de um projeto Tailwind v4.
- **Por que esse gasto:** Instala dependências, configura e confere.
- **Medido:** instrução ~3,2 mil tokens · referências lidas sob demanda: até ~1,7 mil tokens · custo fixo por sessão: ~100 tokens · 2 script(s)

#### `/tailwindcss-patterns` — 🟢 1 · Mínimo

- **O que faz:** Receitas rápidas de Tailwind para layout, tipografia, responsivo e temas.
- **Quando usar:** Dúvida pontual de Tailwind.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~700 tokens · referências lidas sob demanda: até ~750 tokens · custo fixo por sessão: ~50 tokens

---

## 📐 Responsividade e qualidade — 10 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/better-accessibility` | 🟡 3 · Médio | Engenharia de acessibilidade: foco, teclado, ARIA, formulários, leitor de tela. |
| `/browser-testing-with-devtools` | 🟠 4 · Alto | Testa no navegador real pelo MCP do Chrome DevTools: DOM, console, rede, desempenho, visual. |
| `/onboarding-ux` | 🟠 4 · Alto | Navega o app para achar onde o usuário novo trava e produz o conteúdo e o código de onboarding… |
| `/performance-optimization` | 🟡 3 · Médio | Otimização de desempenho de front, back, consultas e banco (Web Vitals, N+1, perfis). |
| `/responsiveness-check` | 🟠 4 · Alto | Passa uma página por várias larguras, captura cada uma e aponta onde o layout quebra. |
| `/ux-audit` | 🔴 5 · Muito alto | Percorre o app como um usuário real (digita, clica, envia) para achar bugs de usabilidade e… |
| `/ux-compare` | 🟡 3 · Médio | Compara padrões de UX entre apps de referência a partir das bibliotecas geradas pela ux-extract. |
| `/ux-extract` | 🔴 5 · Muito alto | Extrai exaustivamente os padrões de UX de um app de referência: todas as telas, estados, textos… |
| `/vitest` | 🟢 2 · Leve | Configura o Vitest no projeto (Workers, React, Node) com config, setup, utilitários e teste de… |
| `/webapp-testing` | 🟡 3 · Médio | Testa app web local com Playwright do Python: verifica o front, captura tela e lê logs do navegador. |

#### `/better-accessibility` — 🟡 3 · Médio

- **O que faz:** Engenharia de acessibilidade: foco, teclado, ARIA, formulários, leitor de tela.
- **Quando usar:** Componente com modal, menu ou formulário; 'deixa acessível'.
- **Por que esse gasto:** Instrução média com ~27 KB de referências.
- **Medido:** instrução ~3,1 mil tokens · referências lidas sob demanda: até ~7,1 mil tokens · custo fixo por sessão: ~160 tokens

#### `/browser-testing-with-devtools` — 🟠 4 · Alto

- **O que faz:** Testa no navegador real pelo MCP do Chrome DevTools: DOM, console, rede, desempenho, visual.
- **Quando usar:** Depurar algo que roda no navegador com dados reais.
- **Por que esse gasto:** Exige o servidor MCP chrome-devtools; inspeções e capturas custam tokens.
- **Medido:** instrução ~3,5 mil tokens · custo fixo por sessão: ~80 tokens
- **Atenção:** 🔌 exige serviço ou MCP externo

#### `/onboarding-ux` — 🟠 4 · Alto

- **O que faz:** Navega o app para achar onde o usuário novo trava e produz o conteúdo e o código de onboarding, estados vazios e dicas.
- **Quando usar:** App que confunde quem chega.
- **Por que esse gasto:** Navega o app com capturas e gera conteúdo.
- **Medido:** instrução ~3,1 mil tokens · custo fixo por sessão: ~130 tokens

#### `/performance-optimization` — 🟡 3 · Médio

- **O que faz:** Otimização de desempenho de front, back, consultas e banco (Web Vitals, N+1, perfis).
- **Quando usar:** Lentidão medida ou suspeita de regressão.
- **Por que esse gasto:** Instrução média e medições.
- **Medido:** instrução ~3,7 mil tokens · custo fixo por sessão: ~70 tokens

#### `/responsiveness-check` — 🟠 4 · Alto

- **O que faz:** Passa uma página por várias larguras, captura cada uma e aponta onde o layout quebra.
- **Quando usar:** 'Confere o responsivo', teste de breakpoints.
- **Por que esse gasto:** Uma captura de tela por largura; imagem custa caro.
- **Medido:** instrução ~1,7 mil tokens · referências lidas sob demanda: até ~1,5 mil tokens · custo fixo por sessão: ~110 tokens

#### `/ux-audit` — 🔴 5 · Muito alto

- **O que faz:** Percorre o app como um usuário real (digita, clica, envia) para achar bugs de usabilidade e comportamento, com prova de interação.
- **Quando usar:** Auditoria de UX antes de lançar.
- **Por que esse gasto:** Instrução enorme (~8,6 mil tokens), muitas capturas e revisão das capturas por subagente.
- **Medido:** instrução ~8,6 mil tokens · referências lidas sob demanda: até ~7,9 mil tokens · custo fixo por sessão: ~240 tokens

#### `/ux-compare` — 🟡 3 · Médio

- **O que faz:** Compara padrões de UX entre apps de referência a partir das bibliotecas geradas pela ux-extract.
- **Quando usar:** Decidir se segue a convenção ou quebra de propósito.
- **Por que esse gasto:** Lê documentos longos; não precisa navegar de novo.
- **Medido:** instrução ~2,2 mil tokens · referências lidas sob demanda: até ~1,3 mil tokens · custo fixo por sessão: ~140 tokens

#### `/ux-extract` — 🔴 5 · Muito alto

- **O que faz:** Extrai exaustivamente os padrões de UX de um app de referência: todas as telas, estados, textos, atalhos e movimento.
- **Quando usar:** Estudar a fundo um app que é referência.
- **Por que esse gasto:** Captura cada estado de cada tela. É das mais caras em imagem.
- **Medido:** instrução ~3,1 mil tokens · referências lidas sob demanda: até ~5,4 mil tokens · custo fixo por sessão: ~140 tokens

#### `/vitest` — 🟢 2 · Leve

- **O que faz:** Configura o Vitest no projeto (Workers, React, Node) com config, setup, utilitários e teste de exemplo.
- **Quando usar:** Projeto sem testes que precisa de uma base.
- **Por que esse gasto:** Instrução média e alguns arquivos.
- **Medido:** instrução ~3,0 mil tokens · custo fixo por sessão: ~100 tokens

#### `/webapp-testing` — 🟡 3 · Médio

- **O que faz:** Testa app web local com Playwright do Python: verifica o front, captura tela e lê logs do navegador.
- **Quando usar:** Conferir se uma tela funciona de verdade.
- **Por que esse gasto:** Escreve e roda scripts de navegador. Sobe para 4 quando depende de muitas capturas de tela.
- **Medido:** instrução ~970 tokens · custo fixo por sessão: ~50 tokens · 4 script(s)
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina

---

## 🖼️ Assets e marca — 5 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/ai-image-generator` | 🟢 2 · Leve | Gera imagens pelas APIs do Gemini e do GPT Image: cenas, ícones, OG images, pôsteres, variações. |
| `/algorithmic-art` | 🟡 3 · Médio | Arte generativa com p5.js: aleatoriedade com semente, campos de fluxo, partículas, parâmetros… |
| `/favicon-gen` | 🟢 2 · Leve | Gera favicon completo (SVG, ICO, apple-touch, 192/512, manifest) a partir de logo, texto ou cor. |
| `/icon-set-generator` | 🟡 3 · Médio | Gera conjunto coerente de ícones SVG próprio para o projeto. |
| `/image-processing` | 🟢 1 · Mínimo | Redimensiona, recorta, converte (PNG/WebP/JPG), otimiza e gera thumbnails e OG images com Pillow. |

#### `/ai-image-generator` — 🟢 2 · Leve

- **O que faz:** Gera imagens pelas APIs do Gemini e do GPT Image: cenas, ícones, OG images, pôsteres, variações.
- **Quando usar:** Imagem de produção para site ou marketing, quando vale pagar.
- **Por que esse gasto:** Poucos tokens do Claude, mas cada imagem é cobrada na conta da Google ou da OpenAI. Para grátis, use criar-imagem (local).
- **Medido:** instrução ~3,9 mil tokens · referências lidas sob demanda: até ~1,1 mil tokens · custo fixo por sessão: ~180 tokens
- **Atenção:** 💲 gasta dinheiro fora da assinatura

#### `/algorithmic-art` — 🟡 3 · Médio

- **O que faz:** Arte generativa com p5.js: aleatoriedade com semente, campos de fluxo, partículas, parâmetros interativos.
- **Quando usar:** Arte feita por código.
- **Por que esse gasto:** Instrução grande e código gerado.
- **Medido:** instrução ~4,9 mil tokens · custo fixo por sessão: ~80 tokens · 1 script(s)

#### `/favicon-gen` — 🟢 2 · Leve

- **O que faz:** Gera favicon completo (SVG, ICO, apple-touch, 192/512, manifest) a partir de logo, texto ou cor.
- **Quando usar:** Site precisando de favicon.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~1,0 mil tokens · referências lidas sob demanda: até ~3,6 mil tokens · custo fixo por sessão: ~100 tokens
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina

#### `/icon-set-generator` — 🟡 3 · Médio

- **O que faz:** Gera conjunto coerente de ícones SVG próprio para o projeto.
- **Quando usar:** Ícones personalizados que combinem entre si.
- **Por que esse gasto:** Muitos SVGs escritos pelo modelo; a saída pesa.
- **Medido:** instrução ~2,0 mil tokens · referências lidas sob demanda: até ~3,1 mil tokens · custo fixo por sessão: ~180 tokens

#### `/image-processing` — 🟢 1 · Mínimo

- **O que faz:** Redimensiona, recorta, converte (PNG/WebP/JPG), otimiza e gera thumbnails e OG images com Pillow.
- **Quando usar:** Preparar imagens para a web.
- **Por que esse gasto:** O Pillow faz o trabalho na sua máquina.
- **Medido:** instrução ~1,8 mil tokens · custo fixo por sessão: ~100 tokens
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina

---

## 🔍 Conteúdo e SEO — 2 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/seo-local-business` | 🟢 2 · Leve | SEO completo para negócio local: meta tags, JSON-LD LocalBusiness, robots.txt e sitemap. |
| `/wordpress-elementor` | 🟠 4 · Alto | Edita páginas Elementor e templates no WordPress por automação de navegador ou WP-CLI. |

#### `/seo-local-business` — 🟢 2 · Leve

- **O que faz:** SEO completo para negócio local: meta tags, JSON-LD LocalBusiness, robots.txt e sitemap.
- **Quando usar:** Site de clínica, prestador, comércio local. Atenção: vem otimizada para a Austrália (+61, ABN); adapte para o Brasil.
- **Por que esse gasto:** Instrução média.
- **Medido:** instrução ~2,5 mil tokens · custo fixo por sessão: ~100 tokens

#### `/wordpress-elementor` — 🟠 4 · Alto

- **O que faz:** Edita páginas Elementor e templates no WordPress por automação de navegador ou WP-CLI.
- **Quando usar:** Mudar texto ou estrutura de página Elementor.
- **Por que esse gasto:** Automação de navegador no editor visual.
- **Medido:** instrução ~2,2 mil tokens · custo fixo por sessão: ~90 tokens

---

## 🤖 IA e agentes — 13 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/agent-harness-construction` | 🟢 1 · Mínimo | Desenho do espaço de ações, das ferramentas e das observações de um agente de IA. |
| `/agent-introspection-debugging` | 🟢 1 · Mínimo | Autodepuração estruturada de falhas de agente: captura, diagnóstico, recuperação contida e… |
| `/agent-self-evaluation` | 🟢 2 · Leve | O agente se dá nota em 5 eixos (precisão, completude, clareza, ação, concisão), com evidência e… |
| `/deep-dive` | 🔴 5 · Muito alto | Pesquisa profunda com plano de consultas em grafo, subagentes em paralelo e novas rodadas para… |
| `/eval-harness` | 🟢 2 · Leve | Framework de avaliação formal de sessões do Claude Code (desenvolvimento guiado por evals). |
| `/llm-integration` | 🟢 1 · Mínimo | Padrões de integração com LLM: API, streaming, function calling, RAG e custo. |
| `/mcp-builder` | 🟡 3 · Médio | Guia para criar servidores MCP de qualidade (Python FastMCP ou Node/TypeScript). |
| `/prompt-engineering` | 🟢 1 · Mínimo | Padrões de prompt: estrutura, cadeia de raciocínio, poucos exemplos, system prompt. |
| `/prompt-optimizer` | 🟢 2 · Leve | Analisa um prompt cru, acha lacunas e devolve uma versão otimizada pronta para colar. Não executa a… |
| `/safety-guard` | 🟢 1 · Mínimo | Travas contra operação destrutiva em produção ou em agente autônomo (modos cuidado, congelar… |
| `/search-first` | 🟠 4 · Alto | Pesquisa antes de codar: procura ferramenta, biblioteca ou padrão existente e decide entre adotar… |
| `/senior-prompt-engineer` | 🟡 3 · Médio | Otimização de prompts com avaliação: templates, conjuntos de teste, qualidade de RAG, contratos de… |
| `/skill-scout` | 🟡 3 · Médio | Procura skills existentes (local, marketplace, GitHub, web) antes de criar uma nova. |

#### `/agent-harness-construction` — 🟢 1 · Mínimo

- **O que faz:** Desenho do espaço de ações, das ferramentas e das observações de um agente de IA.
- **Quando usar:** Construir ou afinar um agente.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~500 tokens · custo fixo por sessão: ~30 tokens

#### `/agent-introspection-debugging` — 🟢 1 · Mínimo

- **O que faz:** Autodepuração estruturada de falhas de agente: captura, diagnóstico, recuperação contida e relatório.
- **Quando usar:** Agente travando ou errando em loop.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~1,4 mil tokens · custo fixo por sessão: ~30 tokens

#### `/agent-self-evaluation` — 🟢 2 · Leve

- **O que faz:** O agente se dá nota em 5 eixos (precisão, completude, clareza, ação, concisão), com evidência e sugestões.
- **Quando usar:** Depois de uma entrega não trivial.
- **Por que esse gasto:** Instrução curta, uma avaliação escrita.
- **Medido:** instrução ~1,9 mil tokens · referências lidas sob demanda: até ~4,8 mil tokens · custo fixo por sessão: ~70 tokens · 1 script(s)

#### `/deep-dive` — 🔴 5 · Muito alto

- **O que faz:** Pesquisa profunda com plano de consultas em grafo, subagentes em paralelo e novas rodadas para cobrir lacunas.
- **Quando usar:** Pergunta de pesquisa grande sem API externa.
- **Por que esse gasto:** Subagentes em paralelo e iteração por lacunas. Para ter checkpoint em disco, a pesquisa-profunda do agente é mais controlada.
- **Medido:** instrução ~1,5 mil tokens · custo fixo por sessão: ~30 tokens

#### `/eval-harness` — 🟢 2 · Leve

- **O que faz:** Framework de avaliação formal de sessões do Claude Code (desenvolvimento guiado por evals).
- **Quando usar:** Medir se um fluxo ou skill melhora de verdade.
- **Por que esse gasto:** Instrução curta; o custo cresce com o número de casos avaliados.
- **Medido:** instrução ~1,6 mil tokens · custo fixo por sessão: ~30 tokens

#### `/llm-integration` — 🟢 1 · Mínimo

- **O que faz:** Padrões de integração com LLM: API, streaming, function calling, RAG e custo.
- **Quando usar:** App que chama um modelo de linguagem.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~1,5 mil tokens · custo fixo por sessão: ~30 tokens

#### `/mcp-builder` — 🟡 3 · Médio

- **O que faz:** Guia para criar servidores MCP de qualidade (Python FastMCP ou Node/TypeScript).
- **Quando usar:** Integrar um serviço externo ao Claude via MCP.
- **Por que esse gasto:** Instrução média, ~80 KB de referências e busca da documentação do SDK na web.
- **Medido:** instrução ~2,3 mil tokens · referências lidas sob demanda: até ~20,7 mil tokens · custo fixo por sessão: ~70 tokens

#### `/prompt-engineering` — 🟢 1 · Mínimo

- **O que faz:** Padrões de prompt: estrutura, cadeia de raciocínio, poucos exemplos, system prompt.
- **Quando usar:** Escrever um prompt melhor.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~1,1 mil tokens · custo fixo por sessão: ~30 tokens

#### `/prompt-optimizer` — 🟢 2 · Leve

- **O que faz:** Analisa um prompt cru, acha lacunas e devolve uma versão otimizada pronta para colar. Não executa a tarefa.
- **Quando usar:** 'Melhora meu prompt'.
- **Por que esse gasto:** Instrução média (~3,9 mil tokens).
- **Medido:** instrução ~3,9 mil tokens · custo fixo por sessão: ~180 tokens

#### `/safety-guard` — 🟢 1 · Mínimo

- **O que faz:** Travas contra operação destrutiva em produção ou em agente autônomo (modos cuidado, congelar, guarda).
- **Quando usar:** Mexer em sistema real ou deixar agente rodando sozinho.
- **Por que esse gasto:** Instrução curta. Protege mais do que custa.
- **Medido:** instrução ~490 tokens · custo fixo por sessão: ~30 tokens

#### `/search-first` — 🟠 4 · Alto

- **O que faz:** Pesquisa antes de codar: procura ferramenta, biblioteca ou padrão existente e decide entre adotar, estender, compor ou construir.
- **Quando usar:** Antes de escrever algo que talvez já exista.
- **Por que esse gasto:** Aciona um agente pesquisador e buscas na web.
- **Medido:** instrução ~1,7 mil tokens · custo fixo por sessão: ~40 tokens

#### `/senior-prompt-engineer` — 🟡 3 · Médio

- **O que faz:** Otimização de prompts com avaliação: templates, conjuntos de teste, qualidade de RAG, contratos de saída estruturada.
- **Quando usar:** Prompt de produção que precisa ser medido.
- **Por que esse gasto:** Instrução média, ~47 KB de referências e scripts.
- **Medido:** instrução ~2,5 mil tokens · referências lidas sob demanda: até ~12,2 mil tokens · custo fixo por sessão: ~110 tokens · 3 script(s)

#### `/skill-scout` — 🟡 3 · Médio

- **O que faz:** Procura skills existentes (local, marketplace, GitHub, web) antes de criar uma nova.
- **Quando usar:** Antes de criar skill.
- **Por que esse gasto:** Buscas na web e no GitHub.
- **Medido:** instrução ~1,1 mil tokens · custo fixo por sessão: ~40 tokens

---

## 🗄️ Dados e backend — 4 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/d1-migration` | 🟢 1 · Mínimo | Fluxo de migração do Cloudflare D1 com Drizzle: gerar, inspecionar, aplicar local e remoto… |
| `/database-schema-designer` | 🟢 2 · Leve | Desenha schema: diagrama ER, normalização, relações e plano de migração. |
| `/db-seed` | 🟢 2 · Leve | Gera script de seed com dados realistas respeitando chaves estrangeiras e limites do D1. |
| `/sql-database-assistant` | 🟡 3 · Médio | Escreve e otimiza SQL, gera migrações, explora schema e ORMs (Prisma, Drizzle, SQLAlchemy). |

#### `/d1-migration` — 🟢 1 · Mínimo

- **O que faz:** Fluxo de migração do Cloudflare D1 com Drizzle: gerar, inspecionar, aplicar local e remoto, destravar.
- **Quando usar:** Rodar ou consertar migração D1.
- **Por que esse gasto:** Instrução curta; o custo é rodar os comandos.
- **Medido:** instrução ~1,1 mil tokens · custo fixo por sessão: ~60 tokens

#### `/database-schema-designer` — 🟢 2 · Leve

- **O que faz:** Desenha schema: diagrama ER, normalização, relações e plano de migração.
- **Quando usar:** Modelar tabelas.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~1,9 mil tokens · referências lidas sob demanda: até ~2,6 mil tokens · custo fixo por sessão: ~30 tokens

#### `/db-seed` — 🟢 2 · Leve

- **O que faz:** Gera script de seed com dados realistas respeitando chaves estrangeiras e limites do D1.
- **Quando usar:** Popular banco de dev, demo ou teste.
- **Por que esse gasto:** Instrução curta; a saída pode ser longa.
- **Medido:** instrução ~1,9 mil tokens · custo fixo por sessão: ~110 tokens

#### `/sql-database-assistant` — 🟡 3 · Médio

- **O que faz:** Escreve e otimiza SQL, gera migrações, explora schema e ORMs (Prisma, Drizzle, SQLAlchemy).
- **Quando usar:** Trabalho de banco no dia a dia.
- **Por que esse gasto:** Instrução média com ~32 KB de referências e scripts.
- **Medido:** instrução ~4,0 mil tokens · referências lidas sob demanda: até ~8,3 mil tokens · custo fixo por sessão: ~50 tokens · 3 script(s)

---

## 🔧 Engenharia de software — 5 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/git-workflow` | 🟢 1 · Mínimo | Fluxos de git guiados: preparar PR, limpar branches, resolver conflitos, tags de release. |
| `/systematic-debugging` | 🟢 2 · Leve | Depuração pela causa-raiz antes de propor conserto (a 'Lei de Ferro'). |
| `/test-driven-development` | 🟢 2 · Leve | Teste antes do código da implementação: vermelho, verde, refatorar. |
| `/verification-before-completion` | 🟢 1 · Mínimo | Obriga a rodar a verificação e mostrar a saída antes de dizer 'pronto' ou 'passa'. |
| `/writing-plans` | 🟢 2 · Leve | Escreve um plano de implementação em etapas antes de mexer no código. |

#### `/git-workflow` — 🟢 1 · Mínimo

- **O que faz:** Fluxos de git guiados: preparar PR, limpar branches, resolver conflitos, tags de release.
- **Quando usar:** Arrumar o git antes de publicar.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~960 tokens · custo fixo por sessão: ~50 tokens

#### `/systematic-debugging` — 🟢 2 · Leve

- **O que faz:** Depuração pela causa-raiz antes de propor conserto (a 'Lei de Ferro').
- **Quando usar:** Qualquer bug, teste falhando ou comportamento inesperado.
- **Por que esse gasto:** Instrução média; o custo é a investigação.
- **Medido:** instrução ~2,4 mil tokens · referências lidas sob demanda: até ~3,1 mil tokens · custo fixo por sessão: ~20 tokens · 2 script(s)

#### `/test-driven-development` — 🟢 2 · Leve

- **O que faz:** Teste antes do código da implementação: vermelho, verde, refatorar.
- **Quando usar:** Implementar funcionalidade ou corrigir bug.
- **Por que esse gasto:** Instrução média.
- **Medido:** instrução ~2,2 mil tokens · referências lidas sob demanda: até ~2,1 mil tokens · custo fixo por sessão: ~20 tokens

#### `/verification-before-completion` — 🟢 1 · Mínimo

- **O que faz:** Obriga a rodar a verificação e mostrar a saída antes de dizer 'pronto' ou 'passa'.
- **Quando usar:** Antes de declarar qualquer coisa concluída.
- **Por que esse gasto:** Instrução curta; o custo é rodar os testes, que você pagaria de qualquer jeito.
- **Medido:** instrução ~900 tokens · custo fixo por sessão: ~60 tokens

#### `/writing-plans` — 🟢 2 · Leve

- **O que faz:** Escreve um plano de implementação em etapas antes de mexer no código.
- **Quando usar:** Tarefa de várias etapas com spec ou requisitos.
- **Por que esse gasto:** Instrução curta; gera um documento.
- **Medido:** instrução ~1,7 mil tokens · referências lidas sob demanda: até ~430 tokens · custo fixo por sessão: ~20 tokens

---

## 💸 Eficiência de contexto — 12 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/context-budget` | 🟡 3 · Médio | Audita o que ocupa a janela de contexto (agentes, skills, MCP, regras) e recomenda cortes por… |
| `/context-compression` | 🟡 3 · Médio | Compressão de contexto em sessões longas: resumo estruturado e passagem de bastão que preserva… |
| `/context-degradation` | 🟡 3 · Médio | Diagnostica degradação de contexto: perdido-no-meio, envenenamento, conflito, confusão. |
| `/context-fundamentals` | 🟢 2 · Leve | Fundamentos de engenharia de contexto: anatomia da janela, atenção, curva em U. |
| `/context-optimization` | 🟢 2 · Leve | Eficiência de contexto: orçamento, mascaramento de saídas, cache de prefixo, particionamento… |
| `/dispatching-parallel-agents` | 🔴 5 · Muito alto | Divide 2 ou mais tarefas independentes entre agentes que trabalham ao mesmo tempo. |
| `/filesystem-context` | 🟢 2 · Leve | Contexto em arquivos: rascunhos duráveis, descarga de saídas grandes em disco, passagem entre… |
| `/long-horizon-prompting` | 🟡 3 · Médio | Escreve o prompt de lançamento de um agente de longa duração ou de uma orquestração multiagente. |
| `/memory-systems` | 🟢 2 · Leve | Memória semântica persistente para agentes: entidades, validade no tempo, grafo ou vetor… |
| `/multi-agent-patterns` | 🟡 3 · Médio | Quando e como usar vários agentes: supervisor, enxame, passagem de bastão e se vale a pena. |
| `/token-budget-advisor` | 🟢 2 · Leve | Oferece escolha de profundidade da resposta antes de responder, para controlar gasto. |
| `/tool-design` | 🟡 3 · Médio | Desenho da camada de ferramentas de agente: descrições, schemas, nomes, mensagens de erro, MCP. |

#### `/context-budget` — 🟡 3 · Médio

- **O que faz:** Audita o que ocupa a janela de contexto (agentes, skills, MCP, regras) e recomenda cortes por prioridade.
- **Quando usar:** Sessões pesadas ou lentas; desconfiança de excesso de skills.
- **Por que esse gasto:** Varre a configuração inteira; com 200+ skills a varredura pesa. Em troca, aponta onde economizar.
- **Medido:** instrução ~1,3 mil tokens · custo fixo por sessão: ~50 tokens

#### `/context-compression` — 🟡 3 · Médio

- **O que faz:** Compressão de contexto em sessões longas: resumo estruturado e passagem de bastão que preserva decisões e riscos.
- **Quando usar:** Sessão enorme que precisa continuar.
- **Por que esse gasto:** Instrução grande (~4,5 mil tokens). O objetivo é reduzir o custo depois.
- **Medido:** instrução ~4,5 mil tokens · referências lidas sob demanda: até ~2,1 mil tokens · custo fixo por sessão: ~60 tokens · 2 script(s)

#### `/context-degradation` — 🟡 3 · Médio

- **O que faz:** Diagnostica degradação de contexto: perdido-no-meio, envenenamento, conflito, confusão.
- **Quando usar:** Agente que piora conforme a conversa cresce.
- **Por que esse gasto:** Instrução grande; é teoria aplicada.
- **Medido:** instrução ~4,8 mil tokens · referências lidas sob demanda: até ~2,5 mil tokens · custo fixo por sessão: ~60 tokens · 1 script(s)

#### `/context-fundamentals` — 🟢 2 · Leve

- **O que faz:** Fundamentos de engenharia de contexto: anatomia da janela, atenção, curva em U.
- **Quando usar:** Aprender ou explicar o assunto.
- **Por que esse gasto:** Instrução média; é material de estudo.
- **Medido:** instrução ~4,2 mil tokens · referências lidas sob demanda: até ~2,0 mil tokens · custo fixo por sessão: ~170 tokens · 1 script(s)

#### `/context-optimization` — 🟢 2 · Leve

- **O que faz:** Eficiência de contexto: orçamento, mascaramento de saídas, cache de prefixo, particionamento, recuperação enxuta.
- **Quando usar:** Reduzir custo de token sem perder qualidade.
- **Por que esse gasto:** Instrução média; paga-se para economizar depois.
- **Medido:** instrução ~3,9 mil tokens · referências lidas sob demanda: até ~2,3 mil tokens · custo fixo por sessão: ~60 tokens · 1 script(s)

#### `/dispatching-parallel-agents` — 🔴 5 · Muito alto

- **O que faz:** Divide 2 ou mais tarefas independentes entre agentes que trabalham ao mesmo tempo.
- **Quando usar:** Tarefas sem estado compartilhado que podem correr em paralelo.
- **Por que esse gasto:** Cada agente é uma sessão inteira. Nesta própria sessão, cada agente de pesquisa gastou de 208 a 291 mil tokens. Use ondas de no máximo 3.
- **Medido:** instrução ~1,5 mil tokens · custo fixo por sessão: ~30 tokens

#### `/filesystem-context` — 🟢 2 · Leve

- **O que faz:** Contexto em arquivos: rascunhos duráveis, descarga de saídas grandes em disco, passagem entre agentes.
- **Quando usar:** Trabalho de agente que estoura o contexto.
- **Por que esse gasto:** Instrução média; reduz o custo das tarefas longas.
- **Medido:** instrução ~4,0 mil tokens · referências lidas sob demanda: até ~4,6 mil tokens · custo fixo por sessão: ~60 tokens · 1 script(s)

#### `/long-horizon-prompting` — 🟡 3 · Médio

- **O que faz:** Escreve o prompt de lançamento de um agente de longa duração ou de uma orquestração multiagente.
- **Quando usar:** Antes de disparar um trabalho autônomo de horas.
- **Por que esse gasto:** Instrução grande (~6,4 mil tokens). O trabalho que o prompt dispara é que custa nível 5.
- **Medido:** instrução ~6,4 mil tokens · referências lidas sob demanda: até ~7,1 mil tokens · custo fixo por sessão: ~210 tokens

#### `/memory-systems` — 🟢 2 · Leve

- **O que faz:** Memória semântica persistente para agentes: entidades, validade no tempo, grafo ou vetor, consolidação.
- **Quando usar:** Projetar memória de agente.
- **Por que esse gasto:** Instrução média.
- **Medido:** instrução ~4,1 mil tokens · referências lidas sob demanda: até ~4,5 mil tokens · custo fixo por sessão: ~90 tokens · 1 script(s)

#### `/multi-agent-patterns` — 🟡 3 · Médio

- **O que faz:** Quando e como usar vários agentes: supervisor, enxame, passagem de bastão e se vale a pena.
- **Quando usar:** Decidir arquitetura multiagente.
- **Por que esse gasto:** Instrução grande; é teoria.
- **Medido:** instrução ~4,6 mil tokens · referências lidas sob demanda: até ~3,1 mil tokens · custo fixo por sessão: ~50 tokens · 1 script(s)

#### `/token-budget-advisor` — 🟢 2 · Leve

- **O que faz:** Oferece escolha de profundidade da resposta antes de responder, para controlar gasto.
- **Quando usar:** Quando você quer controlar o tamanho ou o custo da resposta.
- **Por que esse gasto:** Instrução curta que ajuda a gastar menos.
- **Medido:** instrução ~1,5 mil tokens · custo fixo por sessão: ~200 tokens

#### `/tool-design` — 🟡 3 · Médio

- **O que faz:** Desenho da camada de ferramentas de agente: descrições, schemas, nomes, mensagens de erro, MCP.
- **Quando usar:** Criar ou revisar ferramentas para agente.
- **Por que esse gasto:** Instrução grande com referências.
- **Medido:** instrução ~5,0 mil tokens · referências lidas sob demanda: até ~4,7 mil tokens · custo fixo por sessão: ~140 tokens · 1 script(s)

---

## ✍️ Copy e conversão — 8 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/better-writing` | 🟢 2 · Leve | Escrita de interface: rótulos de botão, mensagens de erro, estados vazios, placeholders, voz e tom. |
| `/content-strategy` | 🟡 3 · Médio | Planeja estratégia de conteúdo: temas, pilares, clusters, calendário editorial, com pesquisa de… |
| `/copy-editing` | 🟡 3 · Médio | Edita e atualiza copy existente, pontuando por personas e refazendo até todas darem nota alta. |
| `/copywriting` | 🟢 2 · Leve | Escreve ou reescreve copy de páginas (home, landing, preços, sobre, produto). |
| `/cro` | 🟢 2 · Leve | Otimização de conversão de páginas e formulários. |
| `/marketing-psychology` | 🟡 3 · Médio | Princípios de psicologia e ciência do comportamento aplicados ao marketing. |
| `/offers` | 🟡 3 · Médio | Desenho da oferta: valor, bônus, garantia, escassez, nome e forma de pagamento. |
| `/ogilvy-copywriting` | 🟢 2 · Leve | Os princípios de David Ogilvy para copy que vende. |

#### `/better-writing` — 🟢 2 · Leve

- **O que faz:** Escrita de interface: rótulos de botão, mensagens de erro, estados vazios, placeholders, voz e tom.
- **Quando usar:** Qualquer texto que o usuário lê na tela.
- **Por que esse gasto:** Instrução média.
- **Medido:** instrução ~2,5 mil tokens · custo fixo por sessão: ~120 tokens

#### `/content-strategy` — 🟡 3 · Médio

- **O que faz:** Planeja estratégia de conteúdo: temas, pilares, clusters, calendário editorial, com pesquisa de ideias.
- **Quando usar:** 'Sobre o que eu escrevo', planejar blog ou redes.
- **Por que esse gasto:** Instrução média e pesquisa na web quando usada.
- **Medido:** instrução ~3,0 mil tokens · referências lidas sob demanda: até ~2,2 mil tokens · custo fixo por sessão: ~160 tokens

#### `/copy-editing` — 🟡 3 · Médio

- **O que faz:** Edita e atualiza copy existente, pontuando por personas e refazendo até todas darem nota alta.
- **Quando usar:** 'Revisa meu texto', 'dá um polimento'.
- **Por que esse gasto:** Rodadas de revisão até a nota mínima.
- **Medido:** instrução ~3,7 mil tokens · referências lidas sob demanda: até ~3,2 mil tokens · custo fixo por sessão: ~150 tokens

#### `/copywriting` — 🟢 2 · Leve

- **O que faz:** Escreve ou reescreve copy de páginas (home, landing, preços, sobre, produto).
- **Quando usar:** Texto de página que precisa converter.
- **Por que esse gasto:** Instrução curta com referências.
- **Medido:** instrução ~1,9 mil tokens · referências lidas sob demanda: até ~3,5 mil tokens · custo fixo por sessão: ~190 tokens

#### `/cro` — 🟢 2 · Leve

- **O que faz:** Otimização de conversão de páginas e formulários.
- **Quando usar:** 'Essa página não converte'.
- **Por que esse gasto:** Instrução curta com ~18 KB de referências.
- **Medido:** instrução ~1,5 mil tokens · referências lidas sob demanda: até ~4,7 mil tokens · custo fixo por sessão: ~160 tokens

#### `/marketing-psychology` — 🟡 3 · Médio

- **O que faz:** Princípios de psicologia e ciência do comportamento aplicados ao marketing.
- **Quando usar:** Persuasão, vieses, 'por que as pessoas compram'.
- **Por que esse gasto:** Instrução grande (~5,5 mil tokens).
- **Medido:** instrução ~5,5 mil tokens · custo fixo por sessão: ~150 tokens

#### `/offers` — 🟡 3 · Médio

- **O que faz:** Desenho da oferta: valor, bônus, garantia, escassez, nome e forma de pagamento.
- **Quando usar:** Montar ou melhorar o que você vende.
- **Por que esse gasto:** Instrução média com ~60 KB de referências.
- **Medido:** instrução ~2,3 mil tokens · referências lidas sob demanda: até ~15,5 mil tokens · custo fixo por sessão: ~240 tokens

#### `/ogilvy-copywriting` — 🟢 2 · Leve

- **O que faz:** Os princípios de David Ogilvy para copy que vende.
- **Quando usar:** Headlines, anúncios, descrições de produto.
- **Por que esse gasto:** Instrução média.
- **Medido:** instrução ~2,7 mil tokens · custo fixo por sessão: ~100 tokens

---

## 🎬 Motion e interação — 21 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/animation-on-scroll` | 🟢 1 · Mínimo | Animação ao entrar na tela com IntersectionObserver e classes compatíveis com Tailwind. |
| `/animation-systems` | 🟢 1 · Mínimo | Sistema de movimento de produto no nível de Stripe, Linear, Apple e Vercel: princípios, curvas… |
| `/animejs` | 🟢 1 · Mínimo | Anime.js dentro de composições HyperFrames (vídeo feito em HTML). |
| `/barba-js` | 🟡 3 · Médio | Transições suaves entre páginas com Barba.js, integráveis ao GSAP. |
| `/beautiful-shadows` | 🟢 1 · Mínimo | Utilitários exatos de sombra do Tailwind para elevação refinada. |
| `/css-animations` | 🟢 1 · Mínimo | Animações CSS dentro de composições HyperFrames. |
| `/framer-motion-core` | 🟢 2 · Leve | API central do Framer Motion: componentes motion, valores, springs. |
| `/framer-motion-gestures` | 🟢 1 · Mínimo | Gestos no Framer Motion: arrastar, tocar, hover, foco. |
| `/framer-motion-layout` | 🟢 1 · Mínimo | Animações de layout no Framer Motion: layoutId, saída, AnimatePresence. |
| `/framer-motion-react` | 🟢 1 · Mínimo | Integração do Framer Motion com React e Next. |
| `/framer-motion-scroll` | 🟢 1 · Mínimo | Animações ligadas ao scroll no Framer Motion: useScroll, parallax. |
| `/framer-motion-variants` | 🟢 1 · Mínimo | Variants no Framer Motion: estados, stagger, sequência. |
| `/gsap` | 🟢 1 · Mínimo | Animações profissionais com GSAP: timelines, ScrollTrigger, stagger. |
| `/locomotive-scroll` | 🟡 3 · Médio | Scroll suave com Locomotive Scroll: parallax e detecção de viewport. |
| `/lottie` | 🟢 1 · Mínimo | Lottie e dotLottie dentro de composições HyperFrames. |
| `/make-interfaces-feel-better` | 🟢 2 · Leve | Princípios de engenharia de design para interface polida: hover, sombras, bordas, microinterações. |
| `/optimize-web-animations` | 🟠 4 · Alto | Perfila e otimiza desempenho de páginas com animação: vazamento de memória, loops de canvas, 'só… |
| `/progressive-blur` | 🟢 1 · Mínimo | Desfoque progressivo em camadas com backdrop-filter. |
| `/react-spring-physics` | 🟡 3 · Médio | Animação por física com React Spring e Popmotion. |
| `/scroll-progress-timeline` | 🟢 1 · Mínimo | Linha do tempo guiada pelo scroll para processos em etapas, com fallback acessível. |
| `/scroll-reveal-libraries` | 🟡 3 · Médio | Revelação no scroll com AOS (Animate On Scroll). |

#### `/animation-on-scroll` — 🟢 1 · Mínimo

- **O que faz:** Animação ao entrar na tela com IntersectionObserver e classes compatíveis com Tailwind.
- **Quando usar:** Revelar elementos no scroll.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~890 tokens · referências lidas sob demanda: até ~500 tokens · custo fixo por sessão: ~60 tokens

#### `/animation-systems` — 🟢 1 · Mínimo

- **O que faz:** Sistema de movimento de produto no nível de Stripe, Linear, Apple e Vercel: princípios, curvas, coreografia.
- **Quando usar:** Definir o movimento de um produto.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~1,3 mil tokens · referências lidas sob demanda: até ~510 tokens · custo fixo por sessão: ~70 tokens

#### `/animejs` — 🟢 1 · Mínimo

- **O que faz:** Anime.js dentro de composições HyperFrames (vídeo feito em HTML).
- **Quando usar:** Só se usar HyperFrames.
- **Por que esse gasto:** Instrução curta; uso de nicho.
- **Medido:** instrução ~830 tokens · custo fixo por sessão: ~70 tokens

#### `/barba-js` — 🟡 3 · Médio

- **O que faz:** Transições suaves entre páginas com Barba.js, integráveis ao GSAP.
- **Quando usar:** Site com transição de página estilo SPA.
- **Por que esse gasto:** Instrução grande com ~82 KB de referências.
- **Medido:** instrução ~4,9 mil tokens · referências lidas sob demanda: até ~21,0 mil tokens · custo fixo por sessão: ~110 tokens · 2 script(s)

#### `/beautiful-shadows` — 🟢 1 · Mínimo

- **O que faz:** Utilitários exatos de sombra do Tailwind para elevação refinada.
- **Quando usar:** Cards, painéis e popovers com sombra bonita.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~640 tokens · referências lidas sob demanda: até ~870 tokens · custo fixo por sessão: ~70 tokens

#### `/css-animations` — 🟢 1 · Mínimo

- **O que faz:** Animações CSS dentro de composições HyperFrames.
- **Quando usar:** Só se usar HyperFrames.
- **Por que esse gasto:** Instrução curta; uso de nicho.
- **Medido:** instrução ~970 tokens · custo fixo por sessão: ~60 tokens

#### `/framer-motion-core` — 🟢 2 · Leve

- **O que faz:** API central do Framer Motion: componentes motion, valores, springs.
- **Quando usar:** Animar em React com Framer Motion.
- **Por que esse gasto:** Instrução média.
- **Medido:** instrução ~2,0 mil tokens · custo fixo por sessão: ~160 tokens

#### `/framer-motion-gestures` — 🟢 1 · Mínimo

- **O que faz:** Gestos no Framer Motion: arrastar, tocar, hover, foco.
- **Quando usar:** Elementos interativos com gesto.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~1,3 mil tokens · custo fixo por sessão: ~70 tokens

#### `/framer-motion-layout` — 🟢 1 · Mínimo

- **O que faz:** Animações de layout no Framer Motion: layoutId, saída, AnimatePresence.
- **Quando usar:** Transições de elemento compartilhado, listas reordenáveis.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~1,5 mil tokens · custo fixo por sessão: ~70 tokens

#### `/framer-motion-react` — 🟢 1 · Mínimo

- **O que faz:** Integração do Framer Motion com React e Next.
- **Quando usar:** Padrões de uso no React.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~1,0 mil tokens · custo fixo por sessão: ~70 tokens

#### `/framer-motion-scroll` — 🟢 1 · Mínimo

- **O que faz:** Animações ligadas ao scroll no Framer Motion: useScroll, parallax.
- **Quando usar:** Parallax e indicadores de progresso.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~1,1 mil tokens · custo fixo por sessão: ~70 tokens

#### `/framer-motion-variants` — 🟢 1 · Mínimo

- **O que faz:** Variants no Framer Motion: estados, stagger, sequência.
- **Quando usar:** Entradas orquestradas.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~970 tokens · custo fixo por sessão: ~70 tokens

#### `/gsap` — 🟢 1 · Mínimo

- **O que faz:** Animações profissionais com GSAP: timelines, ScrollTrigger, stagger.
- **Quando usar:** Adicionar ou depurar animação GSAP.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~770 tokens · referências lidas sob demanda: até ~680 tokens · custo fixo por sessão: ~50 tokens

#### `/locomotive-scroll` — 🟡 3 · Médio

- **O que faz:** Scroll suave com Locomotive Scroll: parallax e detecção de viewport.
- **Quando usar:** Site com scroll suave e parallax.
- **Por que esse gasto:** Instrução média com ~32 KB de referências.
- **Medido:** instrução ~3,1 mil tokens · referências lidas sob demanda: até ~8,4 mil tokens · custo fixo por sessão: ~140 tokens · 3 script(s)

#### `/lottie` — 🟢 1 · Mínimo

- **O que faz:** Lottie e dotLottie dentro de composições HyperFrames.
- **Quando usar:** Só se usar HyperFrames.
- **Por que esse gasto:** Instrução curta; uso de nicho.
- **Medido:** instrução ~850 tokens · custo fixo por sessão: ~60 tokens

#### `/make-interfaces-feel-better` — 🟢 2 · Leve

- **O que faz:** Princípios de engenharia de design para interface polida: hover, sombras, bordas, microinterações.
- **Quando usar:** 'Deixa mais refinado'. Quase igual à better-ui.
- **Por que esse gasto:** Instrução curta com ~24 KB de referências. Redundante com better-ui.
- **Medido:** instrução ~1,5 mil tokens · referências lidas sob demanda: até ~6,1 mil tokens · custo fixo por sessão: ~110 tokens

#### `/optimize-web-animations` — 🟠 4 · Alto

- **O que faz:** Perfila e otimiza desempenho de páginas com animação: vazamento de memória, loops de canvas, 'só animar quando visível'.
- **Quando usar:** Página que esquenta o PC ou fica lenta com o tempo.
- **Por que esse gasto:** Perfilamento em navegador real.
- **Medido:** instrução ~2,1 mil tokens · referências lidas sob demanda: até ~3,6 mil tokens · custo fixo por sessão: ~140 tokens

#### `/progressive-blur` — 🟢 1 · Mínimo

- **O que faz:** Desfoque progressivo em camadas com backdrop-filter.
- **Quando usar:** Borda de tela com blur gradual.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~1,5 mil tokens · referências lidas sob demanda: até ~740 tokens · custo fixo por sessão: ~60 tokens

#### `/react-spring-physics` — 🟡 3 · Médio

- **O que faz:** Animação por física com React Spring e Popmotion.
- **Quando usar:** UI com movimento natural e gestos.
- **Por que esse gasto:** Instrução média com ~44 KB de referências.
- **Medido:** instrução ~2,8 mil tokens · referências lidas sob demanda: até ~11,5 mil tokens · custo fixo por sessão: ~140 tokens · 2 script(s)

#### `/scroll-progress-timeline` — 🟢 1 · Mínimo

- **O que faz:** Linha do tempo guiada pelo scroll para processos em etapas, com fallback acessível.
- **Quando usar:** Onboarding, checkout, roadmap, receita.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~1000 tokens · referências lidas sob demanda: até ~590 tokens · custo fixo por sessão: ~100 tokens

#### `/scroll-reveal-libraries` — 🟡 3 · Médio

- **O que faz:** Revelação no scroll com AOS (Animate On Scroll).
- **Quando usar:** Efeitos simples de fade e slide em landing.
- **Por que esse gasto:** Instrução média com ~46 KB de referências para algo simples.
- **Medido:** instrução ~4,3 mil tokens · referências lidas sob demanda: até ~11,8 mil tokens · custo fixo por sessão: ~120 tokens · 2 script(s)

---

## 🎭 Estilos visuais — 12 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/estilo-bento` | 🟢 1 · Mínimo | Direção visual Bento: grade modular de cards com hierarquia clara. |
| `/estilo-brutalism` | 🟢 1 · Mínimo | Direção visual brutalista: crua, sem enfeite, layout desconfortável de propósito. |
| `/estilo-claymorphism` | 🟢 1 · Mínimo | Direção visual claymorphism: formas macias e 'infladas', coloridas. |
| `/estilo-corporate` | 🟢 1 · Mínimo | Direção visual corporativa: grade estruturada, minimalista, padrão empresarial. |
| `/estilo-editorial` | 🟢 1 · Mínimo | Direção visual editorial: revista, serifas refinadas, leitura elegante. |
| `/estilo-glassmorphism` | 🟢 1 · Mínimo | Direção visual glassmorphism: vidro fosco, camadas translúcidas, blur. |
| `/estilo-minimal` | 🟢 1 · Mínimo | Direção visual minimalista: espaço em branco, tipografia limpa, cor contida. |
| `/estilo-neobrutalism` | 🟢 1 · Mínimo | Direção visual neobrutalista: bordas grossas, cores vivas, alto contraste. |
| `/estilo-neumorphism` | 🟢 1 · Mínimo | Direção visual neumorphism: elementos em relevo suave com sombras internas e externas. |
| `/estilo-premium` | 🟢 1 · Mínimo | Direção visual premium inspirada na Apple: espaço preciso, tipografia moderna. |
| `/estilo-retro` | 🟢 1 · Mínimo | Direção visual retrô: tipografia vintage e paletas nostálgicas. |
| `/estilo-vibrant` | 🟢 1 · Mínimo | Direção visual vibrante: colorida, tipografia divertida, energia. |

#### `/estilo-bento` — 🟢 1 · Mínimo

- **O que faz:** Direção visual Bento: grade modular de cards com hierarquia clara.
- **Quando usar:** Painéis e páginas de recursos organizadas.
- **Por que esse gasto:** Instrução curta com tokens prontos.
- **Medido:** instrução ~880 tokens · referências lidas sob demanda: até ~600 tokens · custo fixo por sessão: ~30 tokens

#### `/estilo-brutalism` — 🟢 1 · Mínimo

- **O que faz:** Direção visual brutalista: crua, sem enfeite, layout desconfortável de propósito.
- **Quando usar:** Marca que quer chocar.
- **Por que esse gasto:** Instrução curta com tokens prontos.
- **Medido:** instrução ~900 tokens · referências lidas sob demanda: até ~620 tokens · custo fixo por sessão: ~30 tokens

#### `/estilo-claymorphism` — 🟢 1 · Mínimo

- **O que faz:** Direção visual claymorphism: formas macias e 'infladas', coloridas.
- **Quando usar:** Produto lúdico.
- **Por que esse gasto:** Instrução curta com tokens prontos.
- **Medido:** instrução ~890 tokens · referências lidas sob demanda: até ~610 tokens · custo fixo por sessão: ~30 tokens

#### `/estilo-corporate` — 🟢 1 · Mínimo

- **O que faz:** Direção visual corporativa: grade estruturada, minimalista, padrão empresarial.
- **Quando usar:** Empresa, B2B.
- **Por que esse gasto:** Instrução curta com tokens prontos.
- **Medido:** instrução ~990 tokens · referências lidas sob demanda: até ~610 tokens · custo fixo por sessão: ~30 tokens

#### `/estilo-editorial` — 🟢 1 · Mínimo

- **O que faz:** Direção visual editorial: revista, serifas refinadas, leitura elegante.
- **Quando usar:** Blog, portfólio de conteúdo.
- **Por que esse gasto:** Instrução curta com tokens prontos.
- **Medido:** instrução ~920 tokens · referências lidas sob demanda: até ~600 tokens · custo fixo por sessão: ~30 tokens

#### `/estilo-glassmorphism` — 🟢 1 · Mínimo

- **O que faz:** Direção visual glassmorphism: vidro fosco, camadas translúcidas, blur.
- **Quando usar:** Interface moderna com profundidade.
- **Por que esse gasto:** Instrução curta com tokens prontos.
- **Medido:** instrução ~950 tokens · referências lidas sob demanda: até ~640 tokens · custo fixo por sessão: ~30 tokens

#### `/estilo-minimal` — 🟢 1 · Mínimo

- **O que faz:** Direção visual minimalista: espaço em branco, tipografia limpa, cor contida.
- **Quando usar:** Foco total no conteúdo.
- **Por que esse gasto:** Instrução curta com tokens prontos.
- **Medido:** instrução ~850 tokens · referências lidas sob demanda: até ~600 tokens · custo fixo por sessão: ~30 tokens

#### `/estilo-neobrutalism` — 🟢 1 · Mínimo

- **O que faz:** Direção visual neobrutalista: bordas grossas, cores vivas, alto contraste.
- **Quando usar:** Marca jovem e ousada.
- **Por que esse gasto:** Instrução curta com tokens prontos.
- **Medido:** instrução ~850 tokens · referências lidas sob demanda: até ~600 tokens · custo fixo por sessão: ~30 tokens

#### `/estilo-neumorphism` — 🟢 1 · Mínimo

- **O que faz:** Direção visual neumorphism: elementos em relevo suave com sombras internas e externas.
- **Quando usar:** Interface tátil e monocromática.
- **Por que esse gasto:** Instrução curta com tokens prontos.
- **Medido:** instrução ~950 tokens · referências lidas sob demanda: até ~620 tokens · custo fixo por sessão: ~30 tokens

#### `/estilo-premium` — 🟢 1 · Mínimo

- **O que faz:** Direção visual premium inspirada na Apple: espaço preciso, tipografia moderna.
- **Quando usar:** Produto de alto valor.
- **Por que esse gasto:** Instrução curta com tokens prontos.
- **Medido:** instrução ~840 tokens · referências lidas sob demanda: até ~590 tokens · custo fixo por sessão: ~30 tokens

#### `/estilo-retro` — 🟢 1 · Mínimo

- **O que faz:** Direção visual retrô: tipografia vintage e paletas nostálgicas.
- **Quando usar:** Marca com apelo nostálgico.
- **Por que esse gasto:** Instrução curta com tokens prontos.
- **Medido:** instrução ~840 tokens · referências lidas sob demanda: até ~600 tokens · custo fixo por sessão: ~30 tokens

#### `/estilo-vibrant` — 🟢 1 · Mínimo

- **O que faz:** Direção visual vibrante: colorida, tipografia divertida, energia.
- **Quando usar:** Público jovem, entretenimento.
- **Por que esse gasto:** Instrução curta com tokens prontos.
- **Medido:** instrução ~860 tokens · referências lidas sob demanda: até ~590 tokens · custo fixo por sessão: ~20 tokens

---

## 🎯 Figma — 1 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/figma` | 🟢 1 · Mínimo | A cabeça do Figma: confere se o MCP da Figma está conectado e se o assento da conta permite, antes… |

#### `/figma` — 🟢 1 · Mínimo

- **O que faz:** A cabeça do Figma: confere se o MCP da Figma está conectado e se o assento da conta permite, antes de qualquer outra skill de Figma.
- **Quando usar:** Qualquer coisa com Figma, ou quando uma skill de Figma falhou.
- **Por que esse gasto:** Instrução curta de diagnóstico. As outras dez exigem MCP e assento pago (Dev ou Full).
- **Medido:** instrução ~1,5 mil tokens · custo fixo por sessão: ~180 tokens
- **Atenção:** 💲 gasta dinheiro fora da assinatura · 🔌 exige serviço ou MCP externo

---

## 🧊 3D e WebGL — 6 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/lightweight-3d-effects` | 🟡 3 · Médio | Efeitos 3D leves e decorativos com Zdog, Vanta.js e Vanilla-Tilt. |
| `/react-three-fiber` | 🟡 3 · Médio | Cenas 3D declarativas em React com React Three Fiber. |
| `/rive-interactive` | 🟢 2 · Leve | Animação vetorial com máquina de estados Rive e controle em tempo de execução. |
| `/spline-interactive` | 🟡 3 · Médio | Cenas 3D feitas no editor visual Spline e exportadas para web e React. |
| `/threejs-webgl` | 🟡 3 · Médio | Desenvolvimento 3D com Three.js: cenas, WebGL/WebGPU, visualizações. |
| `/web3d-integration-patterns` | 🟡 3 · Médio | Meta-skill para combinar Three.js, GSAP, R3F, Motion e React Spring num mesmo projeto. |

#### `/lightweight-3d-effects` — 🟡 3 · Médio

- **O que faz:** Efeitos 3D leves e decorativos com Zdog, Vanta.js e Vanilla-Tilt.
- **Quando usar:** Profundidade sutil sem Three.js completo.
- **Por que esse gasto:** Instrução grande com ~103 KB de referências.
- **Medido:** instrução ~5,7 mil tokens · referências lidas sob demanda: até ~26,5 mil tokens · custo fixo por sessão: ~120 tokens · 3 script(s)

#### `/react-three-fiber` — 🟡 3 · Médio

- **O que faz:** Cenas 3D declarativas em React com React Three Fiber.
- **Quando usar:** Configurador de produto, experiência 3D em React.
- **Por que esse gasto:** Instrução grande com ~41 KB de referências.
- **Medido:** instrução ~5,7 mil tokens · referências lidas sob demanda: até ~10,6 mil tokens · custo fixo por sessão: ~80 tokens · 3 script(s)

#### `/rive-interactive` — 🟢 2 · Leve

- **O que faz:** Animação vetorial com máquina de estados Rive e controle em tempo de execução.
- **Quando usar:** Animação interativa feita por designer.
- **Por que esse gasto:** Instrução média com referências.
- **Medido:** instrução ~3,9 mil tokens · referências lidas sob demanda: até ~2,3 mil tokens · custo fixo por sessão: ~120 tokens · 2 script(s)

#### `/spline-interactive` — 🟡 3 · Médio

- **O que faz:** Cenas 3D feitas no editor visual Spline e exportadas para web e React.
- **Quando usar:** 3D sem escrever código de cena.
- **Por que esse gasto:** Instrução grande com referências.
- **Medido:** instrução ~4,9 mil tokens · referências lidas sob demanda: até ~5,4 mil tokens · custo fixo por sessão: ~120 tokens · 2 script(s)

#### `/threejs-webgl` — 🟡 3 · Médio

- **O que faz:** Desenvolvimento 3D com Three.js: cenas, WebGL/WebGPU, visualizações.
- **Quando usar:** Experiência 3D completa na web.
- **Por que esse gasto:** Instrução média com ~35 KB de referências.
- **Medido:** instrução ~3,9 mil tokens · referências lidas sob demanda: até ~9,2 mil tokens · custo fixo por sessão: ~90 tokens · 2 script(s)

#### `/web3d-integration-patterns` — 🟡 3 · Médio

- **O que faz:** Meta-skill para combinar Three.js, GSAP, R3F, Motion e React Spring num mesmo projeto.
- **Quando usar:** Projeto 3D com várias bibliotecas de animação.
- **Por que esse gasto:** Instrução grande (~5,3 mil tokens).
- **Medido:** instrução ~5,3 mil tokens · custo fixo por sessão: ~120 tokens

---

## 🎓 Aprendizado (as 5 novas) — 5 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/algoritmos-na-pratica` | 🟡 3 · Médio | Acha custo algorítmico ruim em código real medindo antes e depois, com prova de equivalência; e… |
| `/construir-do-zero` | 🟢→🟡 2 a 3 · Leve a médio | Reconstrói uma tecnologia em marcos testados, com você escrevendo o código e o Claude explicando e… |
| `/desenhar-sistema` | 🟡→🟠 3 a 4 · Médio a alto | System design na escala real do projeto: casos de uso, estimativa com contas, desenho, decisões com… |
| `/estudar` | 🟢→🟡 2 a 3 · Leve a médio | Sessão de estudo com método: diagnóstico, um mecanismo por vez, exercício que você roda, perguntas… |
| `/ler-repositorio` | 🟡→🔴 3 a 5 · Médio a muito alto | Estuda um repositório desconhecido em quarentena, neutraliza instruções de agente que vêm junto e… |

#### `/algoritmos-na-pratica` — 🟡 3 · Médio

- **O que faz:** Acha custo algorítmico ruim em código real medindo antes e depois, com prova de equivalência; e treina problemas.
- **Quando usar:** 'Isso tá lento', 'trava com muitos itens', 'qual estrutura usar', treino de lógica.
- **Por que esse gasto:** Lê o código, escreve e roda uma bancada. No teste com o Trindade: 3 arquivos lidos e uma bancada.
- **Medido:** instrução ~2,6 mil tokens · custo fixo por sessão: ~240 tokens
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina

#### `/construir-do-zero` — 🟢→🟡 2 a 3 · Leve a médio

- **O que faz:** Reconstrói uma tecnologia em marcos testados, com você escrevendo o código e o Claude explicando e revisando.
- **Quando usar:** 'Quero entender como X funciona por dentro', 'próximo marco'.
- **Por que esse gasto:** Por sessão é barata: explicar, revisar e dar dica. O projeto inteiro soma várias sessões.
- **Medido:** instrução ~2,1 mil tokens · custo fixo por sessão: ~240 tokens
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina

#### `/desenhar-sistema` — 🟡→🟠 3 a 4 · Médio a alto

- **O que faz:** System design na escala real do projeto: casos de uso, estimativa com contas, desenho, decisões com trade-off.
- **Quando usar:** 'Isso aguenta X usuários?', 'preciso de cache/fila?', antes de backend ou app com banco.
- **Por que esse gasto:** Lê as notas do método e os documentos do projeto; sobe para 4 quando mede com bancada. No teste com o Bene, leu ~10 arquivos do projeto, 3 páginas de documentação e rodou 2 bancadas.
- **Medido:** instrução ~2,9 mil tokens · custo fixo por sessão: ~240 tokens

#### `/estudar` — 🟢→🟡 2 a 3 · Leve a médio

- **O que faz:** Sessão de estudo com método: diagnóstico, um mecanismo por vez, exercício que você roda, perguntas de recordação e fila de revisão espaçada.
- **Quando usar:** 'Quero estudar X', 'o que tenho pra revisar', 'monta um plano de estudo'.
- **Por que esse gasto:** Instrução de ~2,5 mil tokens + a nota da trilha estudada (de 3 a 12 mil tokens). As datas da revisão ficam com o script revisao.py.
- **Medido:** instrução ~2,6 mil tokens · custo fixo por sessão: ~240 tokens · 1 script(s)
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina

#### `/ler-repositorio` — 🟡→🔴 3 a 5 · Médio a muito alto

- **O que faz:** Estuda um repositório desconhecido em quarentena, neutraliza instruções de agente que vêm junto e escreve a nota de fonte.
- **Quando usar:** Link de repo para entender ou avaliar; lista de repos para aprender.
- **Por que esse gasto:** Um repo pequeno: 3. Um monorepo gigante: 4. Uma lista dividida entre agentes: 5.
- **Medido:** instrução ~2,8 mil tokens · referências lidas sob demanda: até ~980 tokens · custo fixo por sessão: ~240 tokens

---

## 📚 Escrita de ficção (instaladas em ~/.agents) — 2 skill(s)

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/creative-writing-craft` | 🟢 2 · Leve | Referências de ofício para ficção: prosa, cenas, estilo, voz, técnicas de gênero. |
| `/fiction-workshop` | 🟠 4 · Alto | Oficina de ficção: edição de desenvolvimento e de linha, voz de personagem, furos de enredo, com… |

#### `/creative-writing-craft` — 🟢 2 · Leve

- **O que faz:** Referências de ofício para ficção: prosa, cenas, estilo, voz, técnicas de gênero.
- **Quando usar:** Precisar de técnica de escrita, não de produção.
- **Por que esse gasto:** Instrução curta, mas ~15 KB de referências sob demanda.
- **Medido:** instrução ~260 tokens · referências lidas sob demanda: até ~4,1 mil tokens · custo fixo por sessão: ~50 tokens

#### `/fiction-workshop` — 🟠 4 · Alto

- **O que faz:** Oficina de ficção: edição de desenvolvimento e de linha, voz de personagem, furos de enredo, com teste de leitor por subagente sem contexto.
- **Quando usar:** Escrever ou editar romance e conto.
- **Por que esse gasto:** Instrução média, ~38 KB de referências e um subagente-leitor.
- **Medido:** instrução ~3,8 mil tokens · referências lidas sob demanda: até ~9,7 mil tokens · custo fixo por sessão: ~60 tokens

---

# Parte 2 — Skills locais do agente

## ⚙️ Claude Mestre Neutro — 49 skills

Aparecem quando você trabalha dentro de `A:\Claude\01-agente-wat\Projeto 9 Claude Mestre Neutro\`. Seis delas têm uma cópia igual na biblioteca global.

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/As10leis` | 🟢 2 · Leve | Liga a postura de trabalho autônomo: decide e segue no que é seguro e reversível, classifica o… |
| `/analisar-dados` | 🟢 1 · Mínimo | Raio-x de um arquivo de dados (CSV, TSV, JSON, XLSX): colunas, tipos, faltantes, duplicados… |
| `/auditar-seguranca` | 🟢 2 · Leve | Portão de entrada de código de terceiro: roda o scanner verificar_seguranca.py (43 regras +… |
| `/brainstorming` | 🟢 2 · Leve | Explora intenção, requisitos e desenho antes de construir: faz perguntas, levanta opções e só… |
| `/brevidade-inteligente` | 🟢 1 · Mínimo | Reescreve texto de trabalho no método Axios: uma pessoa, uma ideia, o ponto na frente. |
| `/colorir-video` | 🟢 1 · Mínimo | Aplica um look de cor num vídeo por preset (teal & orange, quente, frio, vibrante, film fade, P&B)… |
| `/cortar-silencio` | 🟢 1 · Mínimo | Remove silêncios e pausas de um vídeo (jump cut automático) e gera o MP4 cortado. |
| `/criar-imagem` | 🟢 2 · Leve | Gera imagem por texto localmente e de graça pelo Fooocus (Stable Diffusion XL): referência 3D… |
| `/criar-skill` | 🔴 5 · Muito alto | Cria, refaz ou melhora skills com o método da skill-creator: triagem, escrita, testes, avaliação e… |
| `/dialogos-vivos` | 🟢 2 · Leve | Escreve e revisa diálogo de ficção com subtexto, voz própria por personagem e escalada de tensão. |
| `/dispatching-parallel-agents` | 🔴 5 · Muito alto | Divide 2 ou mais tarefas independentes entre agentes que trabalham ao mesmo tempo. |
| `/documentation-and-adrs` | 🟢 2 · Leve | Registra decisões de arquitetura (ADR) e documentação de contexto para quem vier depois. |
| `/encerrar-sessao` | 🟡 3 · Médio | Colhe a sessão: relê a conversa, separa aprendizados (memória, doc, skill), atualiza os documentos… |
| `/executing-plans` | 🟡 3 · Médio | Executa um plano já escrito, em etapas com pontos de revisão. |
| `/fable-mode` | 🟠 4 · Alto | Loop de 6 fases (entender, aterrissar, planejar, executar com causa-raiz, atacar o próprio… |
| `/finalizar-projeto` | 🟠 4 · Alto | Fecha um projeto sem quebrá-lo: mede o estado antes, varre segurança, organiza, revalida e compara… |
| `/find-skills` | 🟢 2 · Leve | Procura skills no ecossistema aberto (npx skills) para uma necessidade. |
| `/finishing-a-development-branch` | 🟢 2 · Leve | Decide como integrar uma branch pronta: merge, PR ou limpeza. |
| `/front_god` | 🟠 4 · Alto | 'WEB ARCHITECT CEO PRO': conduz a construção de um produto web inteiro, do porquê à entrega… |
| `/fundacao-app-web` | 🟡 3 · Médio | Monta a fundação rodável de um app Vite + React: scaffold, tokens de design, moldura mobile… |
| `/humanizer` | 🟡 3 · Médio | Tira a cara de texto gerado por IA (33 padrões típicos: símbolos inflados, 'não só X mas Y'… |
| `/ia-local` | 🟢 2 · Leve | Mede o PC antes de prometer IA local e decide entre tarefa local, agente de código local ou nuvem. |
| `/iniciar-sessao` | 🟢 2 · Leve | Descobre data e hora reais, sincroniza o git, lê os documentos de estado e diz a próxima ação. |
| `/inteligencia-web` | 🟢 2 · Leve | Filtro de 3 regras antes de decidir com base em pesquisa: o que não dá para validar sai rotulado… |
| `/legenda-video` | 🟢 1 · Mínimo | Queima legenda estilo Reels em 6 estilos, transcrevendo a fala com IA local. |
| `/local-llm-agentic-coding` | 🟢 2 · Leve | Instala o Ollama e liga o Claude Code ou o OpenCode a um modelo local, com aviso honesto de… |
| `/local-models` | 🟢 1 · Mínimo | CLI 'lm' para tarefas offline baratas (resumir, classificar, extrair JSON, anonimizar, traduzir)… |
| `/mobile_mode` | 🟢 2 · Leve | Protocolo do ciclo completo de app de celular: safe area, teclado, toque, permissões, offline e os… |
| `/organizar-repo` | 🟢 1 · Mínimo | Faxina dos arquivos soltos na raiz do projeto do agente, em simulação por padrão e sem apagar nada. |
| `/pesquisa-profunda` | 🔴 5 · Muito alto | Pesquisa multi-fonte com verificação adversarial, checkpoint em disco e retomada. |
| `/receiving-code-review` | 🟢 1 · Mínimo | Recebe revisão de código com rigor técnico: verifica antes de aceitar, sem concordar por educação. |
| `/reels-estrategista` | 🟠 4 · Alto | A cabeça da edição de Reels: analisa o vídeo bruto, decide o tratamento para prender a audiência e… |
| `/requesting-code-review` | 🟠 4 · Alto | Pede revisão ao terminar uma tarefa, despachando um subagente revisor com o contexto certo. |
| `/responsivar-mobile` | 🟡 3 · Médio | Deixa um HTML responsivo no celular mexendo só em CSS @media, num loop que mede o overflow em 5… |
| `/revisar-capitulo` | 🟡 3 · Médio | Escreve e revisa capítulo de ficção com a checklist de melhorias, os erros a nunca repetir e… |
| `/revisar-vulnerabilidades` | 🟡 3 · Médio | Revisão de segurança do código do próprio projeto (injeção, XSS, autenticação, autorização… |
| `/sangue-sintetico` | 🟠 4 · Alto | Continua o romance Sangue Sintético coerente com o cânone, carregando a bíblia inteira da história… |
| `/security-best-practices` | 🟡 3 · Médio | Boas práticas de segurança por linguagem e framework (Python, JS/TS, Go), com relatório e sugestões. |
| `/subagent-driven-development` | 🔴 5 · Muito alto | Executa um plano de implementação despachando um subagente por tarefa, com revisão entre elas. |
| `/systematic-debugging` | 🟢 2 · Leve | Depuração pela causa-raiz antes de propor conserto (a 'Lei de Ferro'). |
| `/test-driven-development` | 🟢 2 · Leve | Teste antes do código da implementação: vermelho, verde, refatorar. |
| `/tratar-audio` | 🟢 1 · Mínimo | Conserta o áudio de um vídeo: canal L/R desbalanceado, ruído e volume, sem reencodar a imagem. |
| `/using-git-worktrees` | 🟢 1 · Mínimo | Cria um espaço de trabalho isolado (git worktree) para uma funcionalidade. |
| `/using-superpowers` | 🟢 1 · Mínimo | Meta-skill: estabelece como achar e usar as outras skills antes de responder. |
| `/vercel-react-best-practices` | 🟡 3 · Médio | Regras de desempenho de React e Next.js da Vercel (componentes, busca de dados, bundle). |
| `/verification-before-completion` | 🟢 1 · Mínimo | Obriga a rodar a verificação e mostrar a saída antes de dizer 'pronto' ou 'passa'. |
| `/webapp-testing` | 🟡 3 · Médio | Testa app web local com Playwright do Python: verifica o front, captura tela e lê logs do navegador. |
| `/writing-plans` | 🟢 2 · Leve | Escreve um plano de implementação em etapas antes de mexer no código. |
| `/writing-skills` | 🔴 5 · Muito alto | Cria e testa skills com cenários de pressão rodados por subagentes (do pacote superpowers). |

#### `/As10leis` — 🟢 2 · Leve

- **O que faz:** Liga a postura de trabalho autônomo: decide e segue no que é seguro e reversível, classifica o risco de cada ação em 4 níveis e para no que é irreversível.
- **Quando usar:** Trabalho longo sem você por perto; 'toca o projeto', 'não me pergunta a cada passo'.
- **Por que esse gasto:** Instrução média, sem ação cara por si só. O custo real é o do trabalho que ela autoriza a continuar.
- **Medido:** instrução ~2,3 mil tokens · custo fixo por sessão: ~180 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/analisar-dados` — 🟢 1 · Mínimo

- **O que faz:** Raio-x de um arquivo de dados (CSV, TSV, JSON, XLSX): colunas, tipos, faltantes, duplicados, estatística e alertas de qualidade.
- **Quando usar:** 'Analisa essa planilha', 'o que tem nessa base', antes de importar ou limpar dados.
- **Por que esse gasto:** Quem faz a conta é o script analisar_dados.py, fora do modelo. O Claude só lê o relatório.
- **Medido:** instrução ~1,1 mil tokens · custo fixo por sessão: ~200 tokens
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina · 📍 só vale dentro de um projeto

#### `/auditar-seguranca` — 🟢 2 · Leve

- **O que faz:** Portão de entrada de código de terceiro: roda o scanner verificar_seguranca.py (43 regras + conteúdo oculto) e ajuda a decidir.
- **Quando usar:** Antes de instalar skill, plugin, MCP, script ou repositório baixado.
- **Por que esse gasto:** O scanner é determinístico e barato. Sobe para 3 quando há muitos achados para ler um a um.
- **Medido:** instrução ~2,0 mil tokens · custo fixo por sessão: ~210 tokens
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina · 📍 só vale dentro de um projeto

#### `/brainstorming` — 🟢 2 · Leve

- **O que faz:** Explora intenção, requisitos e desenho antes de construir: faz perguntas, levanta opções e só depois implementa.
- **Quando usar:** Começo de qualquer funcionalidade ou mudança criativa.
- **Por que esse gasto:** Instrução média. É conversa; o custo é o tempo de perguntas e respostas.
- **Medido:** instrução ~2,5 mil tokens · referências lidas sob demanda: até ~3,8 mil tokens · custo fixo por sessão: ~50 tokens · 3 script(s)
- **Atenção:** 📍 só vale dentro de um projeto

#### `/brevidade-inteligente` — 🟢 1 · Mínimo

- **O que faz:** Reescreve texto de trabalho no método Axios: uma pessoa, uma ideia, o ponto na frente.
- **Quando usar:** 'Enxuga esse e-mail', 'isso tá comprido', aviso para equipe.
- **Por que esse gasto:** Instrução curta, só reescrita de texto.
- **Medido:** instrução ~1,2 mil tokens · referências lidas sob demanda: até ~430 tokens · custo fixo por sessão: ~130 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/colorir-video` — 🟢 1 · Mínimo

- **O que faz:** Aplica um look de cor num vídeo por preset (teal & orange, quente, frio, vibrante, film fade, P&B) com controle de intensidade.
- **Quando usar:** 'Dá um look nesse vídeo', 'deixa cinematográfico'.
- **Por que esse gasto:** Instrução curta; o ffmpeg faz o trabalho na sua máquina.
- **Medido:** instrução ~380 tokens · custo fixo por sessão: ~140 tokens
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina · 📍 só vale dentro de um projeto

#### `/cortar-silencio` — 🟢 1 · Mínimo

- **O que faz:** Remove silêncios e pausas de um vídeo (jump cut automático) e gera o MP4 cortado.
- **Quando usar:** 'Corta os silêncios', 'tira as pausas'.
- **Por que esse gasto:** Instrução curta; o ffmpeg faz o trabalho na sua máquina.
- **Medido:** instrução ~350 tokens · custo fixo por sessão: ~110 tokens
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina · 📍 só vale dentro de um projeto

#### `/criar-imagem` — 🟢 2 · Leve

- **O que faz:** Gera imagem por texto localmente e de graça pelo Fooocus (Stable Diffusion XL): referência 3D, textura, thumbnail, concept.
- **Quando usar:** 'Cria uma imagem de X' sem pagar API.
- **Por que esse gasto:** Instrução média; quem gera é a sua GPU. Zero custo de API por imagem.
- **Medido:** instrução ~2,5 mil tokens · referências lidas sob demanda: até ~930 tokens · custo fixo por sessão: ~180 tokens
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina · 📍 só vale dentro de um projeto

#### `/criar-skill` — 🔴 5 · Muito alto

- **O que faz:** Cria, refaz ou melhora skills com o método da skill-creator: triagem, escrita, testes, avaliação e otimização da descrição.
- **Quando usar:** 'Cria uma skill pra X', 'melhora a skill Y'.
- **Por que esse gasto:** Instrução enorme e, no caminho completo, roda subagentes com e sem a skill para comparar. Skill de processo simples cai para 3 pela triagem do Passo 0.
- **Medido:** instrução ~9,3 mil tokens · referências lidas sob demanda: até ~10,1 mil tokens · custo fixo por sessão: ~120 tokens · 10 script(s)
- **Atenção:** 📍 só vale dentro de um projeto

#### `/dialogos-vivos` — 🟢 2 · Leve

- **O que faz:** Escreve e revisa diálogo de ficção com subtexto, voz própria por personagem e escalada de tensão.
- **Quando usar:** 'Melhora esse diálogo', 'essa conversa tá morta'.
- **Por que esse gasto:** Instrução média, trabalho de texto.
- **Medido:** instrução ~2,1 mil tokens · custo fixo por sessão: ~140 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/dispatching-parallel-agents` — 🔴 5 · Muito alto

- **O que faz:** Divide 2 ou mais tarefas independentes entre agentes que trabalham ao mesmo tempo.
- **Quando usar:** Tarefas sem estado compartilhado que podem correr em paralelo.
- **Por que esse gasto:** Cada agente é uma sessão inteira. Nesta própria sessão, cada agente de pesquisa gastou de 208 a 291 mil tokens. Use ondas de no máximo 3.
- **Medido:** instrução ~1,5 mil tokens · custo fixo por sessão: ~30 tokens

#### `/documentation-and-adrs` — 🟢 2 · Leve

- **O que faz:** Registra decisões de arquitetura (ADR) e documentação de contexto para quem vier depois.
- **Quando usar:** Decisão técnica importante, mudança de API, entrega de funcionalidade.
- **Por que esse gasto:** Instrução média; escreve um documento.
- **Medido:** instrução ~2,4 mil tokens · custo fixo por sessão: ~60 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/encerrar-sessao` — 🟡 3 · Médio

- **O que faz:** Colhe a sessão: relê a conversa, separa aprendizados (memória, doc, skill), atualiza os documentos de estado e sincroniza o git.
- **Quando usar:** Fim de toda sessão de trabalho no agente.
- **Por que esse gasto:** Relê a conversa inteira e edita vários arquivos. Sessão longa = encerramento caro.
- **Medido:** instrução ~1,7 mil tokens · referências lidas sob demanda: até ~370 tokens · custo fixo por sessão: ~100 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/executing-plans` — 🟡 3 · Médio

- **O que faz:** Executa um plano já escrito, em etapas com pontos de revisão.
- **Quando usar:** Quando existe um plano pronto para ser seguido em outra sessão.
- **Por que esse gasto:** Instrução curta, mas executa o plano inteiro: o custo é o do trabalho planejado.
- **Medido:** instrução ~580 tokens · custo fixo por sessão: ~30 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/fable-mode` — 🟠 4 · Alto

- **O que faz:** Loop de 6 fases (entender, aterrissar, planejar, executar com causa-raiz, atacar o próprio trabalho, entregar) para entregas de risco.
- **Quando usar:** 'Modo fable', 'qualidade máxima', entrega definitiva ou diagnóstico difícil.
- **Por que esse gasto:** Cada entrega passa por autoataque e verificação. Com subagentes disponíveis em tarefa grande, sobe para 5.
- **Medido:** instrução ~2,5 mil tokens · referências lidas sob demanda: até ~1,5 mil tokens · custo fixo por sessão: ~160 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/finalizar-projeto` — 🟠 4 · Alto

- **O que faz:** Fecha um projeto sem quebrá-lo: mede o estado antes, varre segurança, organiza, revalida e compara o diff.
- **Quando usar:** 'Finaliza o projeto', 'prepara pro GitHub', 'tem arquivo suspeito?'.
- **Por que esse gasto:** Varre o projeto inteiro, roda testes e scanner, compara antes e depois.
- **Medido:** instrução ~1,8 mil tokens · custo fixo por sessão: ~180 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/find-skills` — 🟢 2 · Leve

- **O que faz:** Procura skills no ecossistema aberto (npx skills) para uma necessidade.
- **Quando usar:** 'Tem skill que faz X?'. Sempre seguida de auditar-seguranca antes de instalar.
- **Por que esse gasto:** Busca e leitura de resultados; instalação passa pelo portão.
- **Medido:** instrução ~1,5 mil tokens · referências lidas sob demanda: até ~250 tokens · custo fixo por sessão: ~80 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/finishing-a-development-branch` — 🟢 2 · Leve

- **O que faz:** Decide como integrar uma branch pronta: merge, PR ou limpeza.
- **Quando usar:** Implementação concluída e testes passando.
- **Por que esse gasto:** Instrução curta, alguns comandos git.
- **Medido:** instrução ~1,7 mil tokens · custo fixo por sessão: ~30 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/front_god` — 🟠 4 · Alto

- **O que faz:** 'WEB ARCHITECT CEO PRO': conduz a construção de um produto web inteiro, do porquê à entrega, orquestrando 18 especialidades.
- **Quando usar:** 'Quero um site pra X', 'refaz essa landing' quando o que fazer ainda não está decidido.
- **Por que esse gasto:** Sessão longa que puxa várias outras skills em sequência. O custo é o do produto inteiro.
- **Medido:** instrução ~2,2 mil tokens · custo fixo por sessão: ~200 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/fundacao-app-web` — 🟡 3 · Médio

- **O que faz:** Monta a fundação rodável de um app Vite + React: scaffold, tokens de design, moldura mobile, componentes e rotas, a partir de um template testado.
- **Quando usar:** Começar um app web a partir de uma spec.
- **Por que esse gasto:** Copia template, instala dependências e builda; muitos arquivos gerados.
- **Medido:** instrução ~1,5 mil tokens · custo fixo por sessão: ~210 tokens · 1 script(s)
- **Atenção:** 📍 só vale dentro de um projeto

#### `/humanizer` — 🟡 3 · Médio

- **O que faz:** Tira a cara de texto gerado por IA (33 padrões típicos: símbolos inflados, 'não só X mas Y', excesso de travessão, trios).
- **Quando usar:** Revisar texto que vai ser publicado ou enviado.
- **Por que esse gasto:** Instrução enorme (~8,5 mil tokens) carregada inteira.
- **Medido:** instrução ~8,5 mil tokens · referências lidas sob demanda: até ~3,3 mil tokens · custo fixo por sessão: ~110 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/ia-local` — 🟢 2 · Leve

- **O que faz:** Mede o PC antes de prometer IA local e decide entre tarefa local, agente de código local ou nuvem.
- **Quando usar:** 'Quero IA rodando no meu PC', 'qual modelo cabe na minha placa'.
- **Por que esse gasto:** Um script faz o diagnóstico; a decisão é curta.
- **Medido:** instrução ~1,6 mil tokens · custo fixo por sessão: ~220 tokens
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina · 📍 só vale dentro de um projeto

#### `/iniciar-sessao` — 🟢 2 · Leve

- **O que faz:** Descobre data e hora reais, sincroniza o git, lê os documentos de estado e diz a próxima ação.
- **Quando usar:** Começo de sessão no agente.
- **Por que esse gasto:** Lê CLAUDE.md, WORKFLOW.md e PROXIMA_SESSAO.md; custo proporcional ao tamanho deles.
- **Medido:** instrução ~940 tokens · referências lidas sob demanda: até ~350 tokens · custo fixo por sessão: ~90 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/inteligencia-web` — 🟢 2 · Leve

- **O que faz:** Filtro de 3 regras antes de decidir com base em pesquisa: o que não dá para validar sai rotulado como INCERTO.
- **Quando usar:** Escolher biblioteca, ler benchmark, fonte desconhecida, 'isso é verdade?'.
- **Por que esse gasto:** Instrução curta; o custo é o da pesquisa que ela filtra.
- **Medido:** instrução ~1,9 mil tokens · custo fixo por sessão: ~180 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/legenda-video` — 🟢 1 · Mínimo

- **O que faz:** Queima legenda estilo Reels em 6 estilos, transcrevendo a fala com IA local.
- **Quando usar:** 'Legenda esse reels'.
- **Por que esse gasto:** A transcrição e a queima rodam na sua máquina (whisper + ffmpeg).
- **Medido:** instrução ~440 tokens · custo fixo por sessão: ~150 tokens
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina · 📍 só vale dentro de um projeto

#### `/local-llm-agentic-coding` — 🟢 2 · Leve

- **O que faz:** Instala o Ollama e liga o Claude Code ou o OpenCode a um modelo local, com aviso honesto de hardware.
- **Quando usar:** 'Rodar agente de código offline e sem custo de API'.
- **Por que esse gasto:** Guia de instalação com scripts; o modelo roda na sua máquina.
- **Medido:** instrução ~2,1 mil tokens · referências lidas sob demanda: até ~3,3 mil tokens · custo fixo por sessão: ~190 tokens · 6 script(s)
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina · 📍 só vale dentro de um projeto

#### `/local-models` — 🟢 1 · Mínimo

- **O que faz:** CLI 'lm' para tarefas offline baratas (resumir, classificar, extrair JSON, anonimizar, traduzir) com os modelos que o Ollama já baixou.
- **Quando usar:** Tarefa em lote, sensível ou de baixo risco que não precisa do Claude.
- **Por que esse gasto:** Economiza: tira trabalho do Claude e põe na sua máquina. Nasceu no macOS; no Windows os caminhos mudam.
- **Medido:** instrução ~1,4 mil tokens · referências lidas sob demanda: até ~800 tokens · custo fixo por sessão: ~120 tokens · 1 script(s)
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina · 📍 só vale dentro de um projeto

#### `/mobile_mode` — 🟢 2 · Leve

- **O que faz:** Protocolo do ciclo completo de app de celular: safe area, teclado, toque, permissões, offline e os 11 estados de toda tela.
- **Quando usar:** App Android/iOS, React Native, Expo, PWA instalável, APK.
- **Por que esse gasto:** Instrução média. O custo real é o do app que ela conduz, e ela exige teste em aparelho de verdade.
- **Medido:** instrução ~2,1 mil tokens · custo fixo por sessão: ~190 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/organizar-repo` — 🟢 1 · Mínimo

- **O que faz:** Faxina dos arquivos soltos na raiz do projeto do agente, em simulação por padrão e sem apagar nada.
- **Quando usar:** 'Organiza o repo', 'arruma a raiz'.
- **Por que esse gasto:** O script organizar_repo.py faz o trabalho.
- **Medido:** instrução ~1,1 mil tokens · custo fixo por sessão: ~190 tokens
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina · 📍 só vale dentro de um projeto

#### `/pesquisa-profunda` — 🔴 5 · Muito alto

- **O que faz:** Pesquisa multi-fonte com verificação adversarial, checkpoint em disco e retomada.
- **Quando usar:** 'Pesquisa profunda sobre X' em decisão que precisa de fontes cruzadas.
- **Por que esse gasto:** Dispara 4 agentes de busca e lê até 10 fontes por rodada. Bem mais barata que a deep-research oficial, que ela mesma diz disparar ~100 agentes, mas continua sendo multiagente.
- **Medido:** instrução ~1,2 mil tokens · referências lidas sob demanda: até ~690 tokens · custo fixo por sessão: ~110 tokens · 1 script(s)
- **Atenção:** 📍 só vale dentro de um projeto

#### `/receiving-code-review` — 🟢 1 · Mínimo

- **O que faz:** Recebe revisão de código com rigor técnico: verifica antes de aceitar, sem concordar por educação.
- **Quando usar:** Quando chegou feedback de revisão.
- **Por que esse gasto:** Instrução curta; o custo é o das correções.
- **Medido:** instrução ~1,5 mil tokens · custo fixo por sessão: ~60 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/reels-estrategista` — 🟠 4 · Alto

- **O que faz:** A cabeça da edição de Reels: analisa o vídeo bruto, decide o tratamento para prender a audiência e orquestra as ferramentas de vídeo na ordem certa.
- **Quando usar:** 'Edita esse reels pra prender', quando a decisão do que fazer ainda não foi tomada.
- **Por que esse gasto:** Olha 3 a 5 quadros do vídeo no diagnóstico e mais um depois de cada etapa visual; cada quadro vertical 1080×1920 custa até ~2,7 mil tokens. Lê também a transcrição. O processamento em si roda no ffmpeg local.
- **Medido:** instrução ~2,3 mil tokens · custo fixo por sessão: ~250 tokens
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina · 📍 só vale dentro de um projeto

#### `/requesting-code-review` — 🟠 4 · Alto

- **O que faz:** Pede revisão ao terminar uma tarefa, despachando um subagente revisor com o contexto certo.
- **Quando usar:** Antes de fazer merge ou declarar uma funcionalidade pronta.
- **Por que esse gasto:** Um subagente revisor = uma sessão extra focada.
- **Medido:** instrução ~740 tokens · referências lidas sob demanda: até ~1,3 mil tokens · custo fixo por sessão: ~30 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/responsivar-mobile` — 🟡 3 · Médio

- **O que faz:** Deixa um HTML responsivo no celular mexendo só em CSS @media, num loop que mede o overflow em 5 larguras num navegador real.
- **Quando usar:** 'Tá vazando a tela no celular', 'arruma o mobile dessa página'.
- **Por que esse gasto:** Loop de medição com Playwright; mede números (scrollWidth), não tira captura de tela a cada volta.
- **Medido:** instrução ~2,3 mil tokens · referências lidas sob demanda: até ~720 tokens · custo fixo por sessão: ~200 tokens · 1 script(s)
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina · 📍 só vale dentro de um projeto

#### `/revisar-capitulo` — 🟡 3 · Médio

- **O que faz:** Escreve e revisa capítulo de ficção com a checklist de melhorias, os erros a nunca repetir e revisão adversarial em várias lentes.
- **Quando usar:** Fechar ou revisar um capítulo.
- **Por que esse gasto:** Instrução média e várias passadas de revisão sobre um texto longo.
- **Medido:** instrução ~2,7 mil tokens · custo fixo por sessão: ~170 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/revisar-vulnerabilidades` — 🟡 3 · Médio

- **O que faz:** Revisão de segurança do código do próprio projeto (injeção, XSS, autenticação, autorização, criptografia), com relatório por confiança.
- **Quando usar:** 'Tem falha de segurança nesse código?'.
- **Por que esse gasto:** Instrução média, mas as referências somam ~208 KB; lê só as da linguagem do projeto.
- **Medido:** instrução ~2,9 mil tokens · referências lidas sob demanda: até ~53,4 mil tokens · custo fixo por sessão: ~80 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/sangue-sintetico` — 🟠 4 · Alto

- **O que faz:** Continua o romance Sangue Sintético coerente com o cânone, carregando a bíblia inteira da história antes de escrever.
- **Quando usar:** Escrever ou revisar este livro, e só ele.
- **Por que esse gasto:** Carrega o mundo, os personagens e a estrutura inteiros antes da primeira linha.
- **Medido:** instrução ~1,2 mil tokens · custo fixo por sessão: ~130 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/security-best-practices` — 🟡 3 · Médio

- **O que faz:** Boas práticas de segurança por linguagem e framework (Python, JS/TS, Go), com relatório e sugestões.
- **Quando usar:** Só quando você pede revisão ou orientação de segurança.
- **Por que esse gasto:** Instrução média; as referências somam ~391 KB, e ela lê apenas a do stack em uso.
- **Medido:** instrução ~2,2 mil tokens · referências lidas sob demanda: até ~100,3 mil tokens · custo fixo por sessão: ~100 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/subagent-driven-development` — 🔴 5 · Muito alto

- **O que faz:** Executa um plano de implementação despachando um subagente por tarefa, com revisão entre elas.
- **Quando usar:** Plano com tarefas independentes, na mesma sessão.
- **Por que esse gasto:** Instrução grande (~7,0 mil tokens) e um subagente por tarefa.
- **Medido:** instrução ~7,0 mil tokens · referências lidas sob demanda: até ~4,5 mil tokens · custo fixo por sessão: ~20 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/systematic-debugging` — 🟢 2 · Leve

- **O que faz:** Depuração pela causa-raiz antes de propor conserto (a 'Lei de Ferro').
- **Quando usar:** Qualquer bug, teste falhando ou comportamento inesperado.
- **Por que esse gasto:** Instrução média; o custo é a investigação.
- **Medido:** instrução ~2,4 mil tokens · referências lidas sob demanda: até ~6,1 mil tokens · custo fixo por sessão: ~20 tokens · 2 script(s)

#### `/test-driven-development` — 🟢 2 · Leve

- **O que faz:** Teste antes do código da implementação: vermelho, verde, refatorar.
- **Quando usar:** Implementar funcionalidade ou corrigir bug.
- **Por que esse gasto:** Instrução média.
- **Medido:** instrução ~2,2 mil tokens · referências lidas sob demanda: até ~2,1 mil tokens · custo fixo por sessão: ~20 tokens

#### `/tratar-audio` — 🟢 1 · Mínimo

- **O que faz:** Conserta o áudio de um vídeo: canal L/R desbalanceado, ruído e volume, sem reencodar a imagem.
- **Quando usar:** 'O som tá só de um lado', 'tira o chiado'.
- **Por que esse gasto:** O ffmpeg faz o trabalho na sua máquina.
- **Medido:** instrução ~350 tokens · custo fixo por sessão: ~130 tokens
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina · 📍 só vale dentro de um projeto

#### `/using-git-worktrees` — 🟢 1 · Mínimo

- **O que faz:** Cria um espaço de trabalho isolado (git worktree) para uma funcionalidade.
- **Quando usar:** Antes de trabalho que precisa ficar separado da pasta atual.
- **Por que esse gasto:** Instrução curta, poucos comandos.
- **Medido:** instrução ~1,7 mil tokens · custo fixo por sessão: ~50 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/using-superpowers` — 🟢 1 · Mínimo

- **O que faz:** Meta-skill: estabelece como achar e usar as outras skills antes de responder.
- **Quando usar:** Começo de conversa (é assim que o pacote superpowers se ativa).
- **Por que esse gasto:** Instrução curta, mas faz consultar skills com mais frequência, o que soma leituras.
- **Medido:** instrução ~760 tokens · referências lidas sob demanda: até ~2,3 mil tokens · custo fixo por sessão: ~40 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/vercel-react-best-practices` — 🟡 3 · Médio

- **O que faz:** Regras de desempenho de React e Next.js da Vercel (componentes, busca de dados, bundle).
- **Quando usar:** Escrever ou revisar React/Next com foco em desempenho.
- **Por que esse gasto:** Instrução curta; as regras detalhadas somam ~217 KB e são lidas conforme o caso.
- **Medido:** instrução ~1,8 mil tokens · referências lidas sob demanda: até ~55,6 mil tokens · custo fixo por sessão: ~80 tokens
- **Atenção:** 📍 só vale dentro de um projeto

#### `/verification-before-completion` — 🟢 1 · Mínimo

- **O que faz:** Obriga a rodar a verificação e mostrar a saída antes de dizer 'pronto' ou 'passa'.
- **Quando usar:** Antes de declarar qualquer coisa concluída.
- **Por que esse gasto:** Instrução curta; o custo é rodar os testes, que você pagaria de qualquer jeito.
- **Medido:** instrução ~900 tokens · custo fixo por sessão: ~60 tokens

#### `/webapp-testing` — 🟡 3 · Médio

- **O que faz:** Testa app web local com Playwright do Python: verifica o front, captura tela e lê logs do navegador.
- **Quando usar:** Conferir se uma tela funciona de verdade.
- **Por que esse gasto:** Escreve e roda scripts de navegador. Sobe para 4 quando depende de muitas capturas de tela.
- **Medido:** instrução ~970 tokens · custo fixo por sessão: ~50 tokens · 4 script(s)
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina

#### `/writing-plans` — 🟢 2 · Leve

- **O que faz:** Escreve um plano de implementação em etapas antes de mexer no código.
- **Quando usar:** Tarefa de várias etapas com spec ou requisitos.
- **Por que esse gasto:** Instrução curta; gera um documento.
- **Medido:** instrução ~1,7 mil tokens · referências lidas sob demanda: até ~430 tokens · custo fixo por sessão: ~20 tokens

#### `/writing-skills` — 🔴 5 · Muito alto

- **O que faz:** Cria e testa skills com cenários de pressão rodados por subagentes (do pacote superpowers).
- **Quando usar:** Criar ou editar skill. No seu agente, prefira a criar-skill.
- **Por que esse gasto:** Instrução grande e testes com subagentes. É redundante com a criar-skill.
- **Medido:** instrução ~6,6 mil tokens · referências lidas sob demanda: até ~17,5 mil tokens · custo fixo por sessão: ~20 tokens · 1 script(s)
- **Atenção:** 📍 só vale dentro de um projeto

---

# Parte 3 — Plugin Cloudflare

## ☁️ Plugin cloudflare@cloudflare (ligado) — 13 skills

O único plugin ligado (`settings.json` → `enabledPlugins`). Útil para o Bene e para a sala do Trindade.

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/agents-sdk` | 🟡 3 · Médio | Constrói agentes de IA no Cloudflare Workers com o Agents SDK: estado, workflows duráveis… |
| `/cloudflare` | 🟡 3 · Médio | Skill geral da plataforma Cloudflare: Workers, Pages, KV, D1, R2, IA, rede, segurança, Terraform. |
| `/cloudflare-email-service` | 🟢 2 · Leve | Envio e recebimento de e-mail transacional com o Email Service da Cloudflare. |
| `/cloudflare-one` | 🟡 3 · Médio | Zero Trust e SASE na Cloudflare One: Access, Gateway, WARP, Tunnel, DLP, postura de dispositivo. |
| `/cloudflare-one-migrations` | 🟢 2 · Leve | Planeja migração de Zscaler, Palo Alto, VPN legada ou SASE para a Cloudflare One. |
| `/durable-objects` | 🟢 2 · Leve | Cria e revisa Durable Objects: coordenação com estado, RPC, SQLite, alarmes, WebSockets. |
| `/sandbox-migrate-to-next` | 🟢 2 · Leve | Migra app do Cloudflare Sandbox da versão estável para a 1.0 (@next). |
| `/sandbox-next` | 🟢 2 · Leve | Apps no Cloudflare Sandbox SDK 1.0 (@next): execução de código, terminais, arquivos, túneis. |
| `/sandbox-stable` | 🟢 2 · Leve | Apps no Cloudflare Sandbox estável: comandos, sessões, arquivos, portas. |
| `/turnstile-spin` | 🟠 4 · Alto | Configura o Turnstile (anti-robô) de ponta a ponta: varre o código, cria o widget pela API, embute… |
| `/web-perf` | 🟠 4 · Alto | Analisa desempenho web pelo MCP do Chrome DevTools: LCP, INP, CLS, recursos bloqueantes, cache. |
| `/workers-best-practices` | 🟢 2 · Leve | Revisa e escreve código de Workers contra as boas práticas de produção. |
| `/wrangler` | 🟡 3 · Médio | CLI da Cloudflare: deploy e gestão de Workers, KV, R2, D1, filas, segredos. |

#### `/agents-sdk` — 🟡 3 · Médio

- **O que faz:** Constrói agentes de IA no Cloudflare Workers com o Agents SDK: estado, workflows duráveis, WebSocket, tarefas agendadas, MCP.
- **Quando usar:** Agente, chat ou app de tempo real na Cloudflare.
- **Por que esse gasto:** Instrução média com ~50 KB de referências.
- **Medido:** instrução ~3,0 mil tokens · referências lidas sob demanda: até ~12,9 mil tokens · custo fixo por sessão: ~110 tokens

#### `/cloudflare` — 🟡 3 · Médio

- **O que faz:** Skill geral da plataforma Cloudflare: Workers, Pages, KV, D1, R2, IA, rede, segurança, Terraform.
- **Quando usar:** Qualquer tarefa na Cloudflare (Bene, sala do Trindade).
- **Por que esse gasto:** Instrução média, mas as referências somam ~1,4 MB; ela prioriza buscar a doc atual em vez de ler tudo.
- **Medido:** instrução ~2,2 mil tokens · referências lidas sob demanda: até ~362,4 mil tokens · custo fixo por sessão: ~90 tokens

#### `/cloudflare-email-service` — 🟢 2 · Leve

- **O que faz:** Envio e recebimento de e-mail transacional com o Email Service da Cloudflare.
- **Quando usar:** E-mail de recuperação de senha do Bene, por exemplo.
- **Por que esse gasto:** Instrução curta com referências.
- **Medido:** instrução ~2,0 mil tokens · referências lidas sob demanda: até ~9,3 mil tokens · custo fixo por sessão: ~130 tokens

#### `/cloudflare-one` — 🟡 3 · Médio

- **O que faz:** Zero Trust e SASE na Cloudflare One: Access, Gateway, WARP, Tunnel, DLP, postura de dispositivo.
- **Quando usar:** Proteger acesso a sistemas internos.
- **Por que esse gasto:** Instrução grande (~5,6 mil tokens), buscando a documentação atual.
- **Medido:** instrução ~5,6 mil tokens · custo fixo por sessão: ~80 tokens

#### `/cloudflare-one-migrations` — 🟢 2 · Leve

- **O que faz:** Planeja migração de Zscaler, Palo Alto, VPN legada ou SASE para a Cloudflare One.
- **Quando usar:** Migração corporativa de segurança de rede.
- **Por que esse gasto:** Instrução média. Uso de nicho para o seu trabalho.
- **Medido:** instrução ~3,1 mil tokens · custo fixo por sessão: ~50 tokens

#### `/durable-objects` — 🟢 2 · Leve

- **O que faz:** Cria e revisa Durable Objects: coordenação com estado, RPC, SQLite, alarmes, WebSockets.
- **Quando usar:** A 'sala' do Trindade usa Durable Object.
- **Por que esse gasto:** Instrução curta com ~22 KB de referências.
- **Medido:** instrução ~1,5 mil tokens · referências lidas sob demanda: até ~5,9 mil tokens · custo fixo por sessão: ~100 tokens

#### `/sandbox-migrate-to-next` — 🟢 2 · Leve

- **O que faz:** Migra app do Cloudflare Sandbox da versão estável para a 1.0 (@next).
- **Quando usar:** Só se usar o Sandbox SDK.
- **Por que esse gasto:** Instrução média.
- **Medido:** instrução ~2,0 mil tokens · custo fixo por sessão: ~70 tokens

#### `/sandbox-next` — 🟢 2 · Leve

- **O que faz:** Apps no Cloudflare Sandbox SDK 1.0 (@next): execução de código, terminais, arquivos, túneis.
- **Quando usar:** Só se usar o Sandbox SDK em preview.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~1,8 mil tokens · referências lidas sob demanda: até ~990 tokens · custo fixo por sessão: ~90 tokens

#### `/sandbox-stable` — 🟢 2 · Leve

- **O que faz:** Apps no Cloudflare Sandbox estável: comandos, sessões, arquivos, portas.
- **Quando usar:** Só se usar o Sandbox SDK.
- **Por que esse gasto:** Instrução média.
- **Medido:** instrução ~2,2 mil tokens · custo fixo por sessão: ~90 tokens

#### `/turnstile-spin` — 🟠 4 · Alto

- **O que faz:** Configura o Turnstile (anti-robô) de ponta a ponta: varre o código, cria o widget pela API, embute e liga a verificação no servidor.
- **Quando usar:** Proteger formulário ou endpoint contra robôs.
- **Por que esse gasto:** Instrução enorme (~7,2 mil tokens), varredura do código e chamadas à API da Cloudflare.
- **Medido:** instrução ~7,2 mil tokens · referências lidas sob demanda: até ~9,8 mil tokens · custo fixo por sessão: ~140 tokens · 4 script(s)
- **Atenção:** 🔌 exige serviço ou MCP externo

#### `/web-perf` — 🟠 4 · Alto

- **O que faz:** Analisa desempenho web pelo MCP do Chrome DevTools: LCP, INP, CLS, recursos bloqueantes, cache.
- **Quando usar:** 'Por que meu site tá lento'.
- **Por que esse gasto:** Exige o MCP chrome-devtools; várias medições no navegador.
- **Medido:** instrução ~2,0 mil tokens · custo fixo por sessão: ~110 tokens
- **Atenção:** 🔌 exige serviço ou MCP externo

#### `/workers-best-practices` — 🟢 2 · Leve

- **O que faz:** Revisa e escreve código de Workers contra as boas práticas de produção.
- **Quando usar:** Escrever ou revisar um Worker.
- **Por que esse gasto:** Instrução curta com ~24 KB de referências.
- **Medido:** instrução ~1,8 mil tokens · referências lidas sob demanda: até ~6,3 mil tokens · custo fixo por sessão: ~90 tokens

#### `/wrangler` — 🟡 3 · Médio

- **O que faz:** CLI da Cloudflare: deploy e gestão de Workers, KV, R2, D1, filas, segredos.
- **Quando usar:** Antes de rodar comandos wrangler.
- **Por que esse gasto:** Instrução grande (~4,6 mil tokens).
- **Medido:** instrução ~4,6 mil tokens · custo fixo por sessão: ~80 tokens

### Comandos do plugin (sem arquivo de skill)

#### `/cloudflare:build-agent` — 🟡 3 · Médio

- **O que faz:** Comando guiado para construir um agente de IA na Cloudflare com o Agents SDK.
- **Quando usar:** Começar um agente na Cloudflare.
- **Por que esse gasto:** Guia de construção; usa a skill agents-sdk.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
#### `/cloudflare:build-mcp` — 🟡 3 · Médio

- **O que faz:** Comando guiado para construir um servidor MCP na Cloudflare.
- **Quando usar:** Publicar um MCP na Cloudflare.
- **Por que esse gasto:** Guia de construção.
- **Medido:** embutida no Claude Code, sem arquivo local para medir

---

# Parte 4 — Skill de projeto

## 🚀 Trindade

Só aparece quando você trabalha em `A:\Claude\03-projetos\trindade\`.

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/instalar` | 🟡 3 · Médio | Põe o Trindade para funcionar para alguém do grupo: confere e instala Git, Node, pnpm, Docker e… |

#### `/instalar` — 🟡 3 · Médio

- **O que faz:** Põe o Trindade para funcionar para alguém do grupo: confere e instala Git, Node, pnpm, Docker e Tailscale, monta o .env e liga o servidor.
- **Quando usar:** Hospedar o Trindade em casa ou entrar no de um amigo.
- **Por que esse gasto:** Instalação guiada, longa, com vários comandos e conferências. Os downloads são grandes, mas grátis.
- **Medido:** instrução ~2,8 mil tokens · custo fixo por sessão: ~110 tokens
- **Atenção:** 🖥️ o trabalho pesado roda na sua máquina · 📍 só vale dentro de um projeto

---

# Parte 5 — Figma (desligadas de propósito)

## 🎯 As 10 skills de Figma sem junction

Existem na biblioteca, mas **não carregam**: sem o servidor MCP da Figma e um assento Dev ou Full em plano pago, elas carregariam e falhariam. A `/figma` (ligada) explica como ativar. Não custam nada enquanto desligadas.

| Comando | Gasto ao usar | Em uma linha |
|---|---|---|
| `/figma-code-connect` | 🟡 3 · Médio | Cria e mantém arquivos Code Connect que ligam componentes do Figma a trechos de código. |
| `/figma-create-new-file` | 🟢 1 · Mínimo | Pré-requisito para criar arquivo novo no Figma (design, FigJam, Slides). |
| `/figma-design-to-code` | 🟡 3 · Médio | Implementa um design do Figma como código, lendo o contexto do design pelo MCP. |
| `/figma-extract` | 🟢 2 · Leve | Extrai tokens, assets e especificações do Figma de forma padronizada. |
| `/figma-generate-design` | 🟠 4 · Alto | Traduz uma página ou tela do app para dentro do Figma. |
| `/figma-generate-library` | 🟠 4 · Alto | Constrói um design system profissional no Figma a partir do código: variáveis, componentes… |
| `/figma-implement-motion` | 🟡 3 · Médio | Traduz o movimento e as animações do Figma em código de produção. |
| `/figma-review` | 🟢 2 · Leve | Revisa um design do Figma e deixa comentários presos aos elementos. |
| `/figma-use` | 🟡 3 · Médio | Pré-requisito obrigatório de toda escrita no Figma pelo MCP (use_figma). |
| `/figma-use-motion` | 🟢 2 · Leve | Contexto de animação para o use_figma: keyframes, estilos de animação, easing, duração. |

#### `/figma-code-connect` — 🟡 3 · Médio

- **O que faz:** Cria e mantém arquivos Code Connect que ligam componentes do Figma a trechos de código.
- **Quando usar:** Mapear componentes do Figma para o código.
- **Por que esse gasto:** Instrução grande (~6,6 mil tokens) com referências. Exige MCP e assento pago.
- **Medido:** instrução ~6,6 mil tokens · referências lidas sob demanda: até ~8,7 mil tokens · custo fixo por sessão: ~60 tokens
- **Atenção:** 💲 gasta dinheiro fora da assinatura · 🔌 exige serviço ou MCP externo

#### `/figma-create-new-file` — 🟢 1 · Mínimo

- **O que faz:** Pré-requisito para criar arquivo novo no Figma (design, FigJam, Slides).
- **Quando usar:** Criar arquivo em branco no Figma.
- **Por que esse gasto:** Instrução curta. Exige MCP e assento pago.
- **Medido:** instrução ~980 tokens · custo fixo por sessão: ~120 tokens
- **Atenção:** 💲 gasta dinheiro fora da assinatura · 🔌 exige serviço ou MCP externo

#### `/figma-design-to-code` — 🟡 3 · Médio

- **O que faz:** Implementa um design do Figma como código, lendo o contexto do design pelo MCP.
- **Quando usar:** 'Implementa esse Figma'.
- **Por que esse gasto:** Chamadas ao MCP e código gerado. Funciona com assento Dev (só leitura).
- **Medido:** instrução ~1,2 mil tokens · custo fixo por sessão: ~130 tokens
- **Atenção:** 💲 gasta dinheiro fora da assinatura · 🔌 exige serviço ou MCP externo

#### `/figma-extract` — 🟢 2 · Leve

- **O que faz:** Extrai tokens, assets e especificações do Figma de forma padronizada.
- **Quando usar:** Exportar cores, SVGs, specs.
- **Por que esse gasto:** Instrução curta; chamadas de leitura ao MCP.
- **Medido:** instrução ~1,4 mil tokens · custo fixo por sessão: ~60 tokens
- **Atenção:** 💲 gasta dinheiro fora da assinatura · 🔌 exige serviço ou MCP externo

#### `/figma-generate-design` — 🟠 4 · Alto

- **O que faz:** Traduz uma página ou tela do app para dentro do Figma.
- **Quando usar:** 'Leva essa tela pro Figma'.
- **Por que esse gasto:** Instrução enorme (~8,3 mil tokens) e muitas escritas no arquivo. Exige assento Full.
- **Medido:** instrução ~8,3 mil tokens · referências lidas sob demanda: até ~1,6 mil tokens · custo fixo por sessão: ~210 tokens
- **Atenção:** 💲 gasta dinheiro fora da assinatura · 🔌 exige serviço ou MCP externo

#### `/figma-generate-library` — 🟠 4 · Alto

- **O que faz:** Constrói um design system profissional no Figma a partir do código: variáveis, componentes, variantes, temas.
- **Quando usar:** Montar biblioteca de componentes no Figma.
- **Por que esse gasto:** Instrução grande, ~170 KB de referências e dezenas de chamadas de escrita.
- **Medido:** instrução ~5,6 mil tokens · referências lidas sob demanda: até ~43,7 mil tokens · custo fixo por sessão: ~180 tokens · 8 script(s)
- **Atenção:** 💲 gasta dinheiro fora da assinatura · 🔌 exige serviço ou MCP externo

#### `/figma-implement-motion` — 🟡 3 · Médio

- **O que faz:** Traduz o movimento e as animações do Figma em código de produção.
- **Quando usar:** 'Anima igual ao Figma'.
- **Por que esse gasto:** Instrução grande com ~44 KB de referências.
- **Medido:** instrução ~5,8 mil tokens · referências lidas sob demanda: até ~11,4 mil tokens · custo fixo por sessão: ~90 tokens
- **Atenção:** 💲 gasta dinheiro fora da assinatura · 🔌 exige serviço ou MCP externo

#### `/figma-review` — 🟢 2 · Leve

- **O que faz:** Revisa um design do Figma e deixa comentários presos aos elementos.
- **Quando usar:** 'Revisa esse design' com link do Figma.
- **Por que esse gasto:** Instrução curta.
- **Medido:** instrução ~1,4 mil tokens · custo fixo por sessão: ~90 tokens
- **Atenção:** 💲 gasta dinheiro fora da assinatura · 🔌 exige serviço ou MCP externo

#### `/figma-use` — 🟡 3 · Médio

- **O que faz:** Pré-requisito obrigatório de toda escrita no Figma pelo MCP (use_figma).
- **Quando usar:** Qualquer alteração em arquivo do Figma.
- **Por que esse gasto:** Instrução enorme (~8,5 mil tokens) com ~212 KB de referências.
- **Medido:** instrução ~8,5 mil tokens · referências lidas sob demanda: até ~54,4 mil tokens · custo fixo por sessão: ~140 tokens · 1 script(s)
- **Atenção:** 💲 gasta dinheiro fora da assinatura · 🔌 exige serviço ou MCP externo

#### `/figma-use-motion` — 🟢 2 · Leve

- **O que faz:** Contexto de animação para o use_figma: keyframes, estilos de animação, easing, duração.
- **Quando usar:** Animar nós no Figma.
- **Por que esse gasto:** Instrução curta e iterações até o movimento ficar certo.
- **Medido:** instrução ~1,7 mil tokens · referências lidas sob demanda: até ~6,3 mil tokens · custo fixo por sessão: ~60 tokens
- **Atenção:** 💲 gasta dinheiro fora da assinatura · 🔌 exige serviço ou MCP externo

---

# Parte 6 — Embutidas no Claude Code

Vêm com o Claude Code; não há arquivo local para medir.

| Comando | Gasto ao usar |
|---|---|
| `/code-review` | 🟡→🔴 3 a 5 · Médio a muito alto |
| `/security-review` | 🟡 3 · Médio |
| `/simplify` | 🟡 3 · Médio |
| `/init` | 🟡 3 · Médio |
| `/run` | 🟡 3 · Médio |
| `/loop` | 🔴 5 · Muito alto |
| `/schedule` | 🔴 5 · Muito alto |
| `/fewer-permission-prompts` | 🟡 3 · Médio |
| `/update-config` | 🟢 1 · Mínimo |
| `/keybindings-help` | 🟢 1 · Mínimo |
| `/claude-api` | 🟢 2 · Leve |
| `/artifact-design` | 🟢 2 · Leve |
| `/artifact-diagramming` | 🟢 2 · Leve |
| `/artifact-capabilities` | 🟢 2 · Leve |
| `/dataviz` | 🟢 2 · Leve |
| `/design` | 🟠 4 · Alto |
| `/workflow-authoring` | 🟢 2 · Leve |

#### `/code-review` — 🟡→🔴 3 a 5 · Médio a muito alto

- **O que faz:** Revisa o diff atual (ou um PR) procurando bugs e simplificações, no nível de esforço escolhido. Com --fix aplica; com --comment comenta no PR.
- **Quando usar:** Antes de fazer merge.
- **Por que esse gasto:** Níveis low/medium: 3. high/max: 4. O modo ultra roda uma revisão multiagente na nuvem e é cobrado à parte.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
- **Atenção:** 💲 gasta dinheiro fora da assinatura
#### `/security-review` — 🟡 3 · Médio

- **O que faz:** Revisão de segurança das mudanças pendentes da branch.
- **Quando usar:** Antes de publicar mudança sensível.
- **Por que esse gasto:** Lê o diff e o código em volta.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
#### `/simplify` — 🟡 3 · Médio

- **O que faz:** Revisa o código alterado por reuso, simplificação e eficiência, e aplica as correções. Não caça bugs.
- **Quando usar:** Depois de terminar uma funcionalidade.
- **Por que esse gasto:** Lê e edita o diff.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
#### `/init` — 🟡 3 · Médio

- **O que faz:** Lê o projeto e escreve o CLAUDE.md inicial.
- **Quando usar:** Projeto novo sem CLAUDE.md.
- **Por que esse gasto:** Varre a base de código.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
#### `/run` — 🟡 3 · Médio

- **O que faz:** Sobe e opera o app do projeto para ver uma mudança funcionando de verdade.
- **Quando usar:** 'Roda o app', 'tira print'.
- **Por que esse gasto:** Sobe servidor e, se for web, pode usar navegador.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
#### `/loop` — 🔴 5 · Muito alto

- **O que faz:** Repete um prompt ou comando num intervalo (ou no ritmo que o Claude escolher).
- **Quando usar:** Vigiar deploy, repetir uma checagem.
- **Por que esse gasto:** Cada repetição é uma nova rodada de trabalho; o gasto multiplica pelo número de voltas.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
#### `/schedule` — 🔴 5 · Muito alto

- **O que faz:** Cria agentes na nuvem que rodam por agenda (cron) ou uma vez num horário.
- **Quando usar:** Tarefa recorrente sem você abrir o Claude.
- **Por que esse gasto:** Cada execução agendada é uma sessão inteira de agente.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
#### `/fewer-permission-prompts` — 🟡 3 · Médio

- **O que faz:** Lê suas transcrições e sugere uma lista de comandos de leitura para liberar sem pedir permissão.
- **Quando usar:** Cansou de aprovar os mesmos comandos.
- **Por que esse gasto:** Varre o histórico de sessões.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
#### `/update-config` — 🟢 1 · Mínimo

- **O que faz:** Configura o settings.json do Claude Code: permissões, variáveis de ambiente, hooks.
- **Quando usar:** 'Sempre que X, faça Y', 'libera o comando Z'.
- **Por que esse gasto:** Instrução curta, edição de um arquivo.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
#### `/keybindings-help` — 🟢 1 · Mínimo

- **O que faz:** Personaliza atalhos de teclado do Claude Code.
- **Quando usar:** Trocar ou criar atalho.
- **Por que esse gasto:** Instrução curta.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
#### `/claude-api` — 🟢 2 · Leve

- **O que faz:** Referência da API da Anthropic: modelos, preços, parâmetros, streaming, ferramentas, cache, contagem de tokens.
- **Quando usar:** Construir app que usa o Claude.
- **Por que esse gasto:** Consulta de referência.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
#### `/artifact-design` — 🟢 2 · Leve

- **O que faz:** Orientação de design para páginas publicadas como Artifact.
- **Quando usar:** Antes de publicar uma página.
- **Por que esse gasto:** Instrução média.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
#### `/artifact-diagramming` — 🟢 2 · Leve

- **O que faz:** Como desenhar diagramas SVG legíveis dentro de Artifacts.
- **Quando usar:** Página com diagrama.
- **Por que esse gasto:** Instrução média.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
#### `/artifact-capabilities` — 🟢 2 · Leve

- **O que faz:** Capacidades de runtime de um Artifact: dados ao vivo, estado compartilhado, salvar versões.
- **Quando usar:** Página que precisa lembrar ou compartilhar dados.
- **Por que esse gasto:** Instrução média.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
#### `/dataviz` — 🟢 2 · Leve

- **O que faz:** Método para qualquer gráfico ou dashboard: forma, cor, marcas, acessibilidade.
- **Quando usar:** Antes de criar gráfico.
- **Por que esse gasto:** Instrução média.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
#### `/design` — 🟠 4 · Alto

- **O que faz:** Cria um canvas de design com várias pranchetas, publicado como Artifact editável.
- **Quando usar:** Mockup, landing, pôster, peça gráfica.
- **Por que esse gasto:** Várias pranchetas geradas de uma vez.
- **Medido:** embutida no Claude Code, sem arquivo local para medir
#### `/workflow-authoring` — 🟢 2 · Leve

- **O que faz:** Referência para escrever scripts de Workflow multiagente.
- **Quando usar:** Só depois de você pedir um workflow.
- **Por que esse gasto:** A referência é barata; o workflow que ela ajuda a montar é nível 5.
- **Medido:** embutida no Claude Code, sem arquivo local para medir

---

# Onde dá para economizar

## 1. O custo fixo está alto, e já tem efeito colateral

São **~19,6 mil tokens de descrições** carregados em toda sessão dentro do
agente. Nesta sessão de 12 e 13/09/2026, **dezenas de skills apareceram na lista só com o nome, sem
a descrição**, provavelmente porque a lista tem limite de espaço. Skill sem descrição **não é
acionada sozinha**: só funciona se você digitar `/nome`.

Desligar o que você não usa reduz o custo de toda sessão **e** devolve a descrição às skills que
importam.

## 2. Redundâncias conferidas

| Skill | Faz o mesmo que | Por quê |
|---|---|---|
| `make-interfaces-feel-better` | `better-ui` | descrições praticamente idênticas |
| `writing-skills` | `criar-skill` | o próprio CLAUDE.md do agente manda usar a criar-skill |
| `deep-dive` | `pesquisa-profunda` | a do agente tem checkpoint em disco e retomada |
| `systematic-debugging, test-driven-development, verification-before-completion, writing-plans, dispatching-parallel-agents, webapp-testing` | `(mesmo nome)` | existem duas cópias: uma global e uma local do agente |

## 3. Skills de nicho para o seu trabalho de hoje

| Skill | Por quê |
|---|---|
| `animejs, css-animations, lottie` | são adaptadores para HyperFrames (vídeo feito em HTML); fora disso não servem |
| `seo-local-business` | vem otimizada para a Austrália (+61, ABN) |
| `react-native` | só vale se você fizer app em React Native/Expo |
| `cloudflare-one, cloudflare-one-migrations, sandbox-next, sandbox-stable, sandbox-migrate-to-next` | Zero Trust corporativo e Sandbox SDK, fora do que seus projetos usam hoje |

## 4. Como desligar uma skill da biblioteca sem apagar nada

A skill continua no repositório; só a junction do perfil sai. **Nunca use `Remove-Item -Recurse`
numa junction**: no PowerShell 5.1 isso apaga o conteúdo do alvo. O jeito seguro, registrado no
`LEIA-ME.md` da raiz:

```powershell
[System.IO.Directory]::Delete("C:\Users\alexs\.claude\skills\NOME-DA-SKILL", $false)
```

Para religar tudo: `python 30-sistema\tools\scripts\ligar_biblioteca_skills.py --apply` (ele recria
todas; para manter uma desligada, é preciso marcá-la no script, como já é feito com as de Figma).

## 5. Hábitos que cortam gasto sem desligar nada

- **Agentes em ondas de no máximo 3**, cada um gravando o resultado assim que termina.
- **Tarefa em lote, sensível ou sem risco** (resumir, classificar, anonimizar): `/local-models`
  roda no seu PC.
- **Capturas de tela só quando precisam ser vistas.** Medir número (largura, overflow) custa bem
  menos que analisar imagem; é o que a `/responsivar-mobile` faz.
- **Pesquisa:** `/pesquisa-profunda` salva em disco e retoma; refazer uma pesquisa perdida é o
  gasto mais caro que existe.
- **`/context-budget`** audita o que ocupa o contexto e sugere cortes com números.

---

## Método e limites

- **Medido:** tamanho do `SKILL.md`, das referências e da descrição de cada uma das skills com
  arquivo, lidos do disco em 13/09/2026 (script de inventário, só leitura).
- **Classificado:** o nível de gasto é julgamento sobre o que a instrução manda fazer. Os sinais
  (subagente, navegador, web, API paga, loop) foram achados por busca no texto e **conferidos um a
  um**: vários eram falso positivo (a palavra "billing" num exemplo não quer dizer API paga).
- **Tokens estimados** por caracteres ÷ 4. Contagem exata exigiria a API de contagem de tokens:
  **NÃO FOI POSSÍVEL VALIDAR** nesta máquina.
- **Não medido:** o custo real de cada execução, que depende da tarefa. As duas medições reais
  estão na seção das 5 novas.
- **Embutidas do Claude Code:** classificadas pela descrição, sem arquivo para medir.
