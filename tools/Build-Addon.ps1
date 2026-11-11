param([string]$Version = '26.11.1-cpu4')
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path -LiteralPath "$PSScriptRoot\..").Path
$python = Join-Path $root '.venv\Scripts\python.exe'
if (!(Test-Path -LiteralPath $python)) {
    throw 'Run uv sync --only-group build --python 3.13 first.'
}
& "$PSScriptRoot\cpuSensor\Build-Sensor.ps1"
$gettext = Join-Path $root '.build\gettext'
New-Item -ItemType Directory -Path $gettext -Force | Out-Null
$msgfmt = Join-Path $gettext 'msgfmt.py'
if (!(Test-Path -LiteralPath $msgfmt)) {
    # Build tool only: official CPython's gettext compiler (PSF license).
    Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/python/cpython/v3.13.0/Tools/i18n/msgfmt.py' -OutFile $msgfmt
}
$wrapper = '@"' + $python + '" "' + $msgfmt + '" %*'
Set-Content -LiteralPath "$gettext\msgfmt.cmd" -Value $wrapper -Encoding ascii
$originalPath = $env:PATH
Push-Location $root
try {
    $env:PATH = "$gettext;$originalPath"
    & $python -m SCons "version=$Version"
    if ($LASTEXITCODE -ne 0) { throw 'Add-on build failed.' }
    New-Item -ItemType Directory -Path "$root\dist" -Force | Out-Null
    Move-Item -LiteralPath "$root\resourceMonitor-$Version.nvda-addon" -Destination "$root\dist\resourceMonitor-$Version.nvda-addon" -Force
}
finally {
    $env:PATH = $originalPath
    Pop-Location
}
