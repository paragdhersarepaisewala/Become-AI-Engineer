$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "Starting AI Engineer Academy..." -ForegroundColor Cyan

$backendJob = Start-Process -FilePath "python" `
  -ArgumentList "-m", "uvicorn", "app.main:app", "--reload", "--port", "8050" `
  -WorkingDirectory (Join-Path $root "backend") `
  -PassThru

$frontendJob = Start-Process -FilePath "npm.cmd" `
  -ArgumentList "run", "dev" `
  -WorkingDirectory (Join-Path $root "frontend") `
  -PassThru

Write-Host "Backend API running on http://localhost:8050 (PID $($backendJob.Id))" -ForegroundColor Green
Write-Host "Frontend UI running on http://localhost:5175 (PID $($frontendJob.Id))" -ForegroundColor Green
Write-Host "Press Enter to stop both servers..." -ForegroundColor Yellow
Read-Host

Stop-Process -Id $backendJob.Id -ErrorAction SilentlyContinue
Stop-Process -Id $frontendJob.Id -ErrorAction SilentlyContinue
Write-Host "Stopped servers." -ForegroundColor Gray
