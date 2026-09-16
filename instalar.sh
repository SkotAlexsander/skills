#!/usr/bin/env bash
# Copia as skills deste repositorio para ~/.claude/skills/.
#
#   bash instalar.sh                      # todos os temas
#   bash instalar.sh 16-aprendizado       # so os temas citados
#
# As skills aqui estao agrupadas por tema; o Claude Code espera cada skill
# direto em ~/.claude/skills/. Este script faz essa planificacao.
#
# Nada e apagado. Uma skill que ja exista no destino e PULADA, com aviso.

set -euo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ORIGEM="$RAIZ/skills"
DESTINO="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

if [ ! -d "$ORIGEM" ]; then
  echo "erro: nao achei $ORIGEM. Rode a partir da raiz do repositorio." >&2
  exit 2
fi

if [ "$#" -gt 0 ]; then
  temas=()
  for t in "$@"; do
    if [ -d "$ORIGEM/$t" ]; then
      temas+=("$ORIGEM/$t")
    else
      echo "erro: tema '$t' nao existe. Temas disponiveis:" >&2
      (cd "$ORIGEM" && ls -d */ | tr -d '/') >&2
      exit 2
    fi
  done
else
  temas=("$ORIGEM"/*/)
fi

mkdir -p "$DESTINO"
instaladas=0; puladas=0

for tema in "${temas[@]}"; do
  for skill in "$tema"/*/; do
    [ -f "$skill/SKILL.md" ] || continue
    nome="$(basename "$skill")"
    if [ -e "$DESTINO/$nome" ]; then
      echo "  pulada   $nome (ja existe em $DESTINO)"
      puladas=$((puladas + 1))
      continue
    fi
    cp -r "$skill" "$DESTINO/$nome"
    echo "  instalada $nome"
    instaladas=$((instaladas + 1))
  done
done

echo
echo "$instaladas instalada(s), $puladas pulada(s), em $DESTINO"

if [ "$instaladas" -gt 0 ]; then
  cat <<'AVISO'

Antes de usar as cinco de 16-aprendizado: elas leem uma trilha de estudo em
A:\Claude\02-cerebro\70-aprendizado\, que e um vault privado e nao veio junto.
Troque esse caminho pela sua pasta de notas. Para achar as 30 ocorrencias:

  grep -rn 'A:\\Claude\\02-cerebro' "$HOME/.claude/skills/"

Skill instalada custa contexto mesmo sem ser usada: a descricao de cada uma entra
na lista que o modelo recebe no comeco de toda sessao. Instale so o que for usar.
Ver guia/GUIA-DAS-SKILLS.md.
AVISO
fi
