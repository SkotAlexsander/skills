---
name: figma
description: "A CABEÇA de tudo que envolve Figma — ler um arquivo, extrair token, virar código, implementar o movimento, revisar o design, gerar componente. Confere PRIMEIRO se o servidor MCP da Figma está conectado, porque sem ele nenhuma skill de Figma funciona, e explica exatamente o que falta. Use quando pedirem: 'implementa esse Figma', 'pega o design e vira código', 'extrai as cores/tokens do Figma', 'revisa esse design', 'monta o design system no Figma', 'anima do jeito que está no Figma', ou quando aparecer um link figma.com/design ou figma.com/file. Use TAMBÉM quando alguém disser que uma skill de Figma falhou — o diagnóstico está aqui. NÃO use pra design que não passa pelo Figma (aí é frontend-design, design-system ou ux-audit)."
---

# Figma — a cabeça

Dez skills de Figma estão na biblioteca (`14-figma/`). **Nenhuma delas funciona sozinha:**
todas chamam ferramentas do **servidor MCP da Figma**, que é um serviço externo. Sem ele,
a skill carrega, tenta chamar a ferramenta e falha.

Por isso esta skill vem primeiro. Ela responde à única pergunta que importa antes de
qualquer outra coisa: **dá pra trabalhar com Figma nesta máquina, agora?**

---

## Lei nº 1: conferir o MCP antes de prometer

**Duas coisas precisam ser verdade ao mesmo tempo.** Falha em qualquer uma = nada funciona.

### 1. O servidor MCP está conectado?

Confira se existe um servidor chamado `figma` na configuração de MCP da sessão. Sinais
de que **não** está:

- Nenhuma ferramenta `get_design_context`, `use_figma` ou `get_motion_context` disponível
- A skill de Figma carrega e a chamada seguinte devolve "tool not found"

**Como ligar** — a rota recomendada pela própria Figma instala o MCP **e** as skills
oficiais de uma vez:

```bash
claude plugin install figma@claude-plugins-official
```

Manual, se preferir só o servidor:

```json
{ "mcpServers": { "figma": { "type": "http", "url": "https://mcp.figma.com/mcp" } } }
```

> ⚠️ **A instalação do plugin exige sessão interativa** (`claude mcp` ou `/mcp`). Não dá
> pra fazer por dentro de uma sessão automatizada. Se você é o agente lendo isto numa
> sessão sem terminal interativo: **peça ao usuário**, não tente contornar.

### 2. A conta tem assento que permite?

Este é o degrau que pega todo mundo, e não está em lugar nenhum do erro:

| Plano / assento | O que dá pra fazer |
|---|---|
| **Starter**, ou assento **View / Collab** em plano pago | **6 chamadas de ferramenta por MÊS.** Na prática, nada |
| Assento **Dev** ou **Full** em Professional / Organization / Enterprise | Limite por minuto, igual ao da REST API. Dá pra trabalhar |

Assento **Dev** é **somente leitura** fora de rascunhos — ou seja, `figma-design-to-code`
e `figma-extract` funcionam, mas `figma-generate-design` e `figma-use` (que **escrevem**
no arquivo) não.

**Diga isso ao usuário ANTES de ele instalar o plugin**, não depois de a terceira chamada
falhar.

---

## Lei nº 2: se não tem MCP, ainda dá pra trabalhar — só não automatizado

Não fique de braços cruzados. O caminho manual entrega 80% do valor:

1. **Peça a exportação.** No Figma: selecione o frame → *Export* → SVG (ícone e ilustração)
   ou PNG 2× (imagem). Peça também um print do frame inteiro.
2. **Peça os valores.** O painel direito do Figma mostra cor em hex, tamanho de fonte,
   espaçamento e raio. Um print dele já basta pra montar os tokens.
3. **Aí sim** use as skills que **não** dependem de MCP nenhum:
   [[frontend-design]] e [[design-system]] pra extrair a régua visual,
   [[color-palette]] pra montar a escala a partir de um hex,
   [[better-typography]] e [[better-layout]] pra acertar o resto.

Isso é lento e funciona. Prometer automação que não roda é pior que oferecer o manual.

---

## As dez, e quando cada uma entra

**Oficiais da Figma** (repositório `figma/mcp-server-guide`, Figma Developer Terms):

| Skill | Entra quando |
|---|---|
| [[figma-use]] | **Pré-requisito obrigatório** de qualquer ESCRITA no arquivo. Carregue antes de `use_figma` |
| [[figma-design-to-code]] | **Pré-requisito obrigatório** de `get_design_context`. É o caminho "design vira código" |
| [[figma-implement-motion]] | O nó tem animação e você vai implementar em código |
| [[figma-use-motion]] | Você vai criar/editar animação **dentro** do Figma. Carregue junto com `figma-use` |
| [[figma-generate-design]] | Sentido inverso: pegar uma página que já existe em código e construir no Figma |
| [[figma-generate-library]] | Montar design system no Figma a partir do código — variável, componente, tema |
| [[figma-create-new-file]] | Pré-requisito de `create_new_file` |
| [[figma-code-connect]] | Amarrar componente do Figma ao componente de código (`.figma.ts`) |

**Comunidade** (`madebysan/claude-figma-skills`, MIT):

| Skill | Entra quando |
|---|---|
| [[figma-review]] | Revisar um design e **deixar o comentário fixado no elemento** dentro do Figma |
| [[figma-extract]] | Exportar token, asset e spec de forma padronizada |

> As oficiais dizem, no próprio texto, *"MANDATORY prerequisite — you MUST invoke this
> skill BEFORE every X tool call"*. Isso **é** o formato de uma injeção de prompt, e por
> isso foi olhado com cuidado: aqui é legítimo — a Figma quer que o agente carregue a
> documentação da API antes de chamar a API dela, e a instrução não pede sigilo, não
> pede exfiltração e não estende permissão. Registrado no `00-CATALOGO-E-AUDITORIA`.

---

## Lei nº 3: design não é só Figma

Se a pessoa não tem Figma, ou o design não vive nele, **isto aqui não é o caminho**.
A biblioteca tem 106 outras skills. Vá para [[00-CRIACAO-DE-SITES]] e entre pela etapa:

- Não sei qual é a régua visual → [[frontend-design]], [[design-system]]
- Tenho um site pronto pra copiar a direção → [[ux-extract]], [[design-review]]
- Preciso da paleta → [[color-palette]], [[better-colors]]
- É movimento, não estático → [[_12-motion-e-interacao]]

---

**Tema:** [[_14-figma|figma]]  ·  **Índice:** [[00-INDICE]]  ·  **Fluxo:** [[00-CRIACAO-DE-SITES]]
