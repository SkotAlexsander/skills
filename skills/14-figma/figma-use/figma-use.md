---
skill: figma-use
tema: figma
fonte: figma/mcp-server-guide
tags:
  - skill
  - figma
  - criacao-de-sites
---

# figma-use

> **MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up…

**Invocar:** `/figma-use`  ·  **Tema:** [[_14-figma|figma]]  ·  **Origem:** `figma/mcp-server-guide`

**Etapa no fluxo:** 2. Definir — ver [[00-CRIACAO-DE-SITES]]

> ⚠️ **Precisa do servidor MCP da Figma conectado** e de assento Dev ou Full num plano pago da Figma. Sem isso, a skill carrega e a chamada de ferramenta falha. Ver [[figma]] para o diagnóstico.

## Conecta com — dentro de *figma*

- [[figma-design-to-code]]
- [[figma-implement-motion]]
- [[figma-use-motion]]
- [[figma-generate-design]]

## Arquivos desta skill

- [SKILL.md](SKILL.md)
- [references/api-reference.md](references/api-reference.md)
- [references/common-patterns.md](references/common-patterns.md)
- [references/component-patterns.md](references/component-patterns.md)
- [references/effect-style-patterns.md](references/effect-style-patterns.md)
- [references/gotchas.md](references/gotchas.md)
- [references/plugin-api-patterns.md](references/plugin-api-patterns.md)
- [references/plugin-api-standalone.d.ts](references/plugin-api-standalone.d.ts)
- [references/plugin-api-standalone.index.md](references/plugin-api-standalone.index.md)
- [references/text-style-patterns.md](references/text-style-patterns.md)
- [references/validation-and-recovery.md](references/validation-and-recovery.md)
- [references/variable-patterns.md](references/variable-patterns.md)

---
[[00-INDICE|← Índice da biblioteca]] · [[_14-figma|← figma]]
