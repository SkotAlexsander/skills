<#
    Copia as skills deste repositorio para ~\.claude\skills\.

      .\instalar.ps1                    # todos os temas
      .\instalar.ps1 16-aprendizado     # so os temas citados

    As skills aqui estao agrupadas por tema; o Claude Code espera cada skill
    direto em ~\.claude\skills\. Este script faz essa planificacao.

    Nada e apagado. Uma skill que ja exista no destino e PULADA, com aviso.
#>

param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Temas)

$ErrorActionPreference = 'Stop'

$raiz   = Split-Path -Parent $MyInvocation.MyCommand.Path
$origem = Join-Path $raiz 'skills'
$destino = if ($env:CLAUDE_SKILLS_DIR) { $env:CLAUDE_SKILLS_DIR }
           else { Join-Path $env:USERPROFILE '.claude\skills' }

if (-not (Test-Path $origem)) {
    Write-Error "nao achei $origem. Rode a partir da raiz do repositorio."
}

if ($Temas) {
    $pastas = foreach ($t in $Temas) {
        $p = Join-Path $origem $t
        if (-not (Test-Path $p)) {
            Write-Host "erro: tema '$t' nao existe. Temas disponiveis:" -ForegroundColor Red
            Get-ChildItem $origem -Directory | ForEach-Object { Write-Host "  $($_.Name)" }
            exit 2
        }
        Get-Item $p
    }
} else {
    $pastas = Get-ChildItem $origem -Directory
}

if (-not (Test-Path $destino)) { New-Item -ItemType Directory -Path $destino -Force | Out-Null }

$instaladas = 0
$puladas    = 0

foreach ($tema in $pastas) {
    foreach ($skill in Get-ChildItem $tema.FullName -Directory) {
        if (-not (Test-Path (Join-Path $skill.FullName 'SKILL.md'))) { continue }
        $alvo = Join-Path $destino $skill.Name
        if (Test-Path $alvo) {
            Write-Host "  pulada    $($skill.Name) (ja existe)" -ForegroundColor DarkYellow
            $puladas++
            continue
        }
        Copy-Item $skill.FullName $alvo -Recurse
        Write-Host "  instalada $($skill.Name)" -ForegroundColor Green
        $instaladas++
    }
}

Write-Host ""
Write-Host "$instaladas instalada(s), $puladas pulada(s), em $destino"

if ($instaladas -gt 0) {
    Write-Host @"

Antes de usar as cinco de 16-aprendizado: elas leem uma trilha de estudo em
A:\Claude\02-cerebro\70-aprendizado\, que e um vault privado e nao veio junto.
Troque esse caminho pela sua pasta de notas. Para achar as 30 ocorrencias:

  Select-String -Path "$destino\*\*.md" -Pattern '02-cerebro' -Recurse

Skill instalada custa contexto mesmo sem ser usada: a descricao de cada uma entra
na lista que o modelo recebe no comeco de toda sessao. Instale so o que for usar.
Ver guia\GUIA-DAS-SKILLS.md.
"@ -ForegroundColor Cyan
}
