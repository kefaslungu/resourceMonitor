param(
    [string]$HelperPath = "$PSScriptRoot\..\..\.build\cpu-temperature\libre\ResourceMonitor.CpuSensor.exe"
)
$ErrorActionPreference = 'Stop'
$helper = (Resolve-Path -LiteralPath $HelperPath).Path
$pipeName = 'ResourceMonitor.CpuSensor.test.' + [Guid]::NewGuid().ToString('N')
$sensorProcess = Start-Process -FilePath $helper -ArgumentList @('--serve', $PID, $pipeName) -Verb RunAs -WindowStyle Hidden -PassThru
try {
    & $helper --read $pipeName
    if ($LASTEXITCODE -ne 0) { throw 'CPU sensor query failed.' }
}
finally {
    & $helper --stop $pipeName
    $sensorProcess.WaitForExit(5000) | Out-Null
}
