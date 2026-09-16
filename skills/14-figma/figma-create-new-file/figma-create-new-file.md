---
skill: figma-create-new-file
tema: figma
fonte: figma/mcp-server-guide
tags:
  - skill
  - figma
  - criacao-de-sites
---

# figma-create-new-file

> **MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `create_new_file` tool call. NEVER call `create_new_file` directly without loading this skill first. Trigger whenever the user wants a new blank Figma file — a new design, FigJam, or Slides file — or when you need a fresh file before calling `use_figma`. Usage — /figma-create-new-file [editorType] [fileName] (e.g.…

**Invocar:** `/figma-create-new-file`  ·  **Tema:** [[_14-figma|figma]]  ·  **Origem:** `figma/mcp-server-guide`

**Etapa no fluxo:** 2. Definir — ver [[00-CRIACAO-DE-SITES]]

> ⚠️ **Precisa do servidor MCP da Figma conectado** e de assento Dev ou Full num plano pago da Figma. Sem isso, a skill carrega e a chamada de ferramenta falha. Ver [[figma]] para o diagnóstico.

## Conecta com — dentro de *figma*

- [[figma-use]]
- [[figma-design-to-code]]
- [[figma-implement-motion]]
- [[figma-use-motion]]

## Arquivos desta skill

- [SKILL.md](SKILL.md)

---
[[00-INDICE|← Índice da biblioteca]] · [[_14-figma|← figma]]
