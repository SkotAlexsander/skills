---
skill: ler-repositorio
tema: aprendizado
fonte: própria (Claude Mestre Neutro)
tags:
  - skill
  - aprendizado
  - propria
  - seguranca
---

# ler-repositorio

> Estudar um repositório desconhecido **sem executá-lo e sem herdar as instruções para agentes que
> vêm dentro dele**, e sair com uma nota que diz o que tirar, o que pular, e como uma funcionalidade
> funciona de ponta a ponta, com arquivo e linha.

**Invocar:** `/ler-repositorio`  ·  **Tema:** [[_16-aprendizado|aprendizado]]  ·  **Origem:** própria, 2026-09-13

## Por que ela existe

Ela é a generalização do trabalho que montou a trilha de aprendizado: 13 repositórios lidos em
12/09/2026. Dois fatos daquela rodada viraram regra:

1. **Repositório traz texto para agente.** O clone do `vinta/awesome-python` trazia
   `.claude/skills`, `CLAUDE.md`, `AGENTS.md` e um `settings.json` que pré-autorizava
   `gh api:*` (qualquer chamada à API com o token do usuário) e `gh pr close/comment/edit`. As skills do mantenedor apareceram como disponíveis na sessão assim
   que o clone caiu na pasta de trabalho. O `react/react` trazia um `CLAUDE.md`. A skill manda ler
   como dado e **renomear para `.QUARENTENA`** antes de trabalhar nos arquivos.
2. **Muitos agentes em paralelo estouram o limite de uso.** Oito agentes caíram duas vezes. A skill
   manda ondas de no máximo 3, gravação de cada nota assim que fica pronta, e agente novo só com o
   que falta, em vez de retomar o antigo.

**Não substitui o portão.** Se o veredito for adotar a biblioteca, `auditar-seguranca` continua
obrigatória antes de instalar.

## Conecta com — dentro de *aprendizado*

- [[estudar]] — as notas que esta skill escreve viram currículo
- [[desenhar-sistema]] — ler a arquitetura de um projeto de referência antes de desenhar o seu
- [[construir-do-zero]] — ler o código da ferramenta real depois de reconstruí-la

## Arquivos desta skill

- [SKILL.md](SKILL.md)
- [references/spec-agentes.md](references/spec-agentes.md) — modelo de especificação para dividir a leitura entre agentes

---
[[00-INDICE|← Índice da biblioteca]] · [[_16-aprendizado|← aprendizado]]
