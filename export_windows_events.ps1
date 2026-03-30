$logs = @('Application','System','Security','Setup')
$timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$outDir = "C:\Temp\EventLogs\$timestamp"

New-Item -ItemType Directory -Path $outDir -Force | Out-Null

foreach ($log in $logs) {
    $dest = Join-Path $outDir "$log.evtx"
    wevtutil epl $log $dest /ow:true
}
