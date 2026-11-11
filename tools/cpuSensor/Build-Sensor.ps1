param([switch]$Download)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path -LiteralPath "$PSScriptRoot\..\..").Path
$cache = Join-Path $root '.build\cpu-temperature'
$archive = Join-Path $cache 'LibreHardwareMonitor-0.9.6.zip'
$unpacked = Join-Path $cache 'libre'
$destination = Join-Path $root 'addon\globalPlugins\resourceMonitor\sensors'
$sourceUrl = 'https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases/download/v0.9.6/LibreHardwareMonitor.zip'
New-Item -ItemType Directory -Path $cache, $destination -Force | Out-Null
if ($Download -or !(Test-Path -LiteralPath $archive)) {
    Invoke-WebRequest -Uri $sourceUrl -OutFile $archive
}
$expected = '086d9f1b5a99e643edc2cfaaac16051685b551e4c5ac0b32a57c58c0e529c001'
if ((Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash -ne $expected) {
    throw 'LibreHardwareMonitor archive hash does not match the official release digest.'
}
Expand-Archive -LiteralPath $archive -DestinationPath $unpacked -Force
Get-ChildItem -LiteralPath $unpacked -Filter '*.dll' -File | Copy-Item -Destination $destination -Force
Copy-Item -LiteralPath "$unpacked\LibreHardwareMonitor.exe.config" -Destination "$destination\ResourceMonitor.CpuSensor.exe.config" -Force
$compiler = Join-Path $env:WINDIR 'Microsoft.NET\Framework64\v4.0.30319\csc.exe'
$source = Join-Path $PSScriptRoot 'Program.cs'
$output = Join-Path $destination 'ResourceMonitor.CpuSensor.exe'
$reference = Join-Path $destination 'LibreHardwareMonitorLib.dll'
& $compiler /nologo /target:exe /platform:x64 "/out:$output" "/reference:$reference" /reference:System.Web.Extensions.dll $source
if ($LASTEXITCODE -ne 0) { throw 'CPU sensor compilation failed.' }
foreach ($notice in @('LICENSE', 'THIRD-PARTY-NOTICES.txt')) {
    $target = Join-Path $destination "LibreHardwareMonitor-$notice.txt"
    if ($Download -or !(Test-Path -LiteralPath $target)) {
        Invoke-WebRequest -Uri "https://raw.githubusercontent.com/LibreHardwareMonitor/LibreHardwareMonitor/v0.9.6/$notice" -OutFile $target
    }
}
Copy-Item -LiteralPath $source -Destination "$destination\ResourceMonitor.CpuSensor.cs" -Force
$driverInstaller = Join-Path $cache 'PawnIO-2.2.0-setup.exe'
if ($Download -or !(Test-Path -LiteralPath $driverInstaller)) {
    Invoke-WebRequest -Uri 'https://github.com/namazso/PawnIO.Setup/releases/download/2.2.0/PawnIO_setup.exe' -OutFile $driverInstaller
}
if ((Get-FileHash -LiteralPath $driverInstaller -Algorithm SHA256).Hash -ne
    '1f519a22e47187f70a1379a48ca604981c4fcf694f4e65b734aaa74a9fba3032') {
    throw 'PawnIO installer hash does not match the official release digest.'
}
if ((Get-AuthenticodeSignature -LiteralPath $driverInstaller).Status -ne 'Valid') {
    throw 'PawnIO installer signature is not valid.'
}
Copy-Item -LiteralPath $driverInstaller -Destination "$destination\PawnIO-2.2.0-setup.exe" -Force
Write-Output "Built CPU sensor: $output"
