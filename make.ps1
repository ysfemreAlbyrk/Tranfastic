#!/usr/bin/env pwsh
# Tranfastic - PowerShell Build Script
# Simplified build commands

param(
    [Parameter(Position=0)]
    [string]$Command = "help"
)

function Show-Help {
    Write-Host "Tranfastic - Build Commands" -ForegroundColor Cyan
    Write-Host "==========================" -ForegroundColor Cyan
    Write-Host "install-req    - Install requirements from requirements.txt" -ForegroundColor Green
    Write-Host "build          - Build both portable and installer versions" -ForegroundColor Green
    Write-Host "clean          - Clean build artifacts" -ForegroundColor Green
    Write-Host "run            - Run the application" -ForegroundColor Green
    Write-Host "build-portable - Build only portable executable" -ForegroundColor Green
    Write-Host "build-installer - Build only Windows installer" -ForegroundColor Green
    Write-Host ""
    Write-Host "Usage: .\make.ps1 <command>" -ForegroundColor Yellow
    Write-Host "Example: .\make.ps1 build" -ForegroundColor Yellow
}

function Install-Requirements {
    Write-Host "Installing requirements..." -ForegroundColor Blue
    # Check if virtual environment exists
    if (!(Test-Path ".venv")) {
        Write-Host "Creating virtual environment [.venv]..." -ForegroundColor Yellow
        python -m venv .venv
        
        # Activate virtual environment
        Write-Host "Activating virtual environment [.venv]..." -ForegroundColor Yellow
        .\.venv\Scripts\Activate.ps1
        
        # Upgrade pip in virtual environment
        Write-Host "Upgrading pip..." -ForegroundColor Yellow
        python -m pip install --upgrade pip
    }
    else {
        # Just activate if it exists
        Write-Host "Activating existing virtual environment [.venv]..." -ForegroundColor Yellow
        .\.venv\Scripts\Activate.ps1

        # Upgrade pip in virtual environment
        Write-Host "Upgrading pip..." -ForegroundColor Yellow
        python -m pip install --upgrade pip
    }
    pip install -r requirements.txt
}

function Build-All {
    Write-Host "Building Tranfastic..." -ForegroundColor Blue
    
    # Build portable first
    Write-Host "Building portable executable..." -ForegroundColor Cyan
    pyinstaller build.spec --clean --noconfirm
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Portable build failed!" -ForegroundColor Red
        return
    }
    
    # Copy to portable directory for organization
    if (!(Test-Path "dist/portable")) { New-Item -ItemType Directory -Path "dist/portable" -Force }
    Copy-Item "dist/Tranfastic.exe" "dist/portable/Tranfastic.exe" -Force
    Write-Host "Portable executable: dist/portable/Tranfastic.exe" -ForegroundColor Green
    
    # Build installer
    Write-Host "Building Windows installer..." -ForegroundColor Cyan
    & "installer\build_installer.ps1" -BuildType "installer" -Clean:$false
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Both versions built successfully!" -ForegroundColor Green
        
        # Show summary
        Write-Host "`nBuild Summary:" -ForegroundColor Magenta
        if (Test-Path "dist/portable/Tranfastic.exe") {
            $PortableSize = [math]::Round((Get-Item "dist/portable/Tranfastic.exe").Length / 1MB, 2)
            Write-Host "  Portable: $PortableSize MB" -ForegroundColor White
        }
        
        $InstallerFile = Get-ChildItem "dist/Tranfastic-*-Setup.exe" -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($InstallerFile) {
            $InstallerSize = [math]::Round($InstallerFile.Length / 1MB, 2)
            Write-Host "  Installer: $InstallerSize MB" -ForegroundColor White
        }
    }
}

function Clean-Artifacts {
    Write-Host "Cleaning build artifacts..." -ForegroundColor Blue
    
    Write-Host "Deleting build & dist directories..." -ForegroundColor Blue
    if (Test-Path "build") { Remove-Item -Recurse -Force "build" }
    if (Test-Path "dist") { Remove-Item -Recurse -Force "dist" }
    Write-Host "Deleting .egg-info directories..." -ForegroundColor Blue
    Get-ChildItem -Path . -Filter "*.egg-info" -Directory -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force
    Write-Host "Deleting __pycache__ directory..." -ForegroundColor Blue
    Get-ChildItem -Path . -Recurse -Directory -Name "__pycache__" -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force
    
    Write-Host "Clean completed!" -ForegroundColor Green
}

function Run-Application {
    Write-Host "Running the application..." -ForegroundColor Blue
    python main.py
}

function Build-Portable {
    Write-Host "Building portable executable..." -ForegroundColor Blue
    pyinstaller build.spec --clean --noconfirm
    
    # Copy to portable directory for organization
    if (!(Test-Path "dist/portable")) { New-Item -ItemType Directory -Path "dist/portable" -Force }
    Move-Item "dist/Tranfastic.exe" "dist/portable/Tranfastic.exe" -Force
    Write-Host "Portable executable: dist/portable/Tranfastic.exe" -ForegroundColor Green
}

function Build-Installer {
    Write-Host "Building Windows installer..." -ForegroundColor Blue
    & "installer\build_installer.ps1" -BuildType "installer" -Clean
}

# Command dispatcher
switch ($Command.ToLower()) {
    "help" { Show-Help }
    "install-req" { Install-Requirements }
    "build" { Build-All }
    "clean" { Clean-Artifacts }
    "run" { Run-Application }
    "build-portable" { Build-Portable }
    "build-installer" { Build-Installer }
    default { 
        Write-Host "Unknown command: $Command" -ForegroundColor Red
        Write-Host ""
        Show-Help 
    }
}