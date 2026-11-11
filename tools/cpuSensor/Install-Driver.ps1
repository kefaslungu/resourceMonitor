# Explicit, optional system installation; never invoked by the add-on's startup.
param([string]$InstallerPath = "$PSScriptRoot\..\..\addon\globalPlugins\resourceMonitor\sensors\PawnIO-2.2.0-setup.exe")
$ErrorActionPreference = 'Stop'
$installer = (Resolve-Path -LiteralPath $InstallerPath).Path
if ((Get-FileHash -LiteralPath $installer -Algorithm SHA256).Hash -ne
    '1f519a22e47187f70a1379a48ca604981c4fcf694f4e65b734aaa74a9fba3032') {
    throw 'Unexpected PawnIO installer hash.'
}
if ((Get-AuthenticodeSignature -LiteralPath $installer).Status -ne 'Valid') {
    throw 'PawnIO installer signature verification failed.'
}
$installation = Start-Process -FilePath $installer -ArgumentList @('-install', '-silent') -Verb RunAs -WindowStyle Hidden -Wait -PassThru
if ($installation.ExitCode -eq 3010) {
    Write-Output 'PawnIO installed. Windows reports a restart is required; no restart was performed.'
}
elseif ($installation.ExitCode -eq 0) {
    Write-Output 'PawnIO signed driver installation completed.'
}
elseif ($installation.ExitCode -eq 183) {
    Write-Output 'PawnIO is already installed. Run Test-Sensor.ps1 to verify actual device access.'
}
else {
    throw "PawnIO installer returned exit code $($installation.ExitCode)."
}
