---
skill: figma
tema: figma
fonte: própria (Claude Mestre Neutro)
tags:
  - skill
  - figma
  - criacao-de-sites
  - propria
---

# figma

> A **cabeça** de tudo que envolve Figma. Confere primeiro se o servidor MCP está conectado e se o assento da conta permite — porque sem isso nenhuma das outras dez funciona — e só então roteia. Quando não há MCP, entrega o caminho manual em vez de prometer automação que não roda.

**Invocar:** `/figma`  ·  **Tema:** [[_14-figma|figma]]  ·  **Origem:** própria, 2026-08-13

**Etapa no fluxo:** 2. Definir — ver [[00-CRIACAO-DE-SITES]]

## Por que ela existe

As dez skills de Figma da biblioteca são **inúteis sozinhas**: todas chamam ferramentas
do servidor MCP da Figma. Sem MCP, cada uma carrega, tenta chamar e falha — e o erro não
diz que o problema é assento de conta.

Esta skill é o portão: **mede antes de prometer**. Mesmo padrão da `ia-local`, que vive no
repo do projeto (`A:\Claude-agente-wat\Projeto 9 Claude Mestre Neutro`) e faz isso com hardware — não é nota
deste vault, por isso sem wikilink.

**Os dois degraus que precisam ser verdade ao mesmo tempo:**

1. Servidor MCP `figma` conectado → `claude plugin install figma@claude-plugins-official`
2. Assento **Dev** ou **Full** em plano pago. Starter / View / Collab = **6 chamadas por mês**

E ainda: assento **Dev** é só leitura fora de rascunho — lê design, não escreve nele.

## Conecta com — dentro de *figma*

- [[figma-use]]
- [[figma-design-to-code]]
- [[figma-extract]]
- [[figma-review]]

## Arquivos desta skill

- [SKILL.md](SKILL.md)

---
[[00-INDICE|← Índice da biblioteca]] · [[_14-figma|← figma]]
