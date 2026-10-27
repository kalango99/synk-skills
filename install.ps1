# Synk Skills: instalador para Windows (PowerShell)
# Uso: irm https://raw.githubusercontent.com/kalango99/synk-skills/main/install.ps1 | iex
$ErrorActionPreference = "Stop"
$repo = "https://github.com/kalango99/synk-skills/archive/refs/heads/main.zip"
$destino = Join-Path $HOME ".claude\skills"
$tmp = Join-Path $env:TEMP ("synk-skills-" + [guid]::NewGuid().ToString("N"))

Write-Host "Baixando as Synk Skills..." -ForegroundColor Green
New-Item -ItemType Directory -Force -Path $tmp, $destino | Out-Null
Invoke-WebRequest -Uri $repo -OutFile "$tmp\pacote.zip" -UseBasicParsing
Expand-Archive "$tmp\pacote.zip" -DestinationPath $tmp -Force

$origem = Get-ChildItem $tmp -Directory | Where-Object { Test-Path (Join-Path $_.FullName "skills") } | Select-Object -First 1
foreach ($skill in Get-ChildItem (Join-Path $origem.FullName "skills") -Directory) {
  $alvo = Join-Path $destino $skill.Name
  if (Test-Path $alvo) { Remove-Item $alvo -Recurse -Force }
  Copy-Item $skill.FullName $alvo -Recurse
  Write-Host "  ok  $($skill.Name)"
}
Remove-Item $tmp -Recurse -Force

Write-Host ""
Write-Host "Pronto. Skills instaladas em $destino" -ForegroundColor Green
Write-Host "Feche e abra o Claude Code para ele enxergar as skills novas."
