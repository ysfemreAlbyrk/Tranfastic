# Tranfastic Installer Build Script
# Builds Windows installer using PyInstaller + NSIS

param(
    [string]$BuildType = "installer",  # "portable" or "installer"
    [switch]$Clean = $false
)

# Set paths
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$InstallerDir = $PSScriptRoot
$DistDir = Join-Path $ProjectRoot "dist"
$BuildDir = Join-Path $ProjectRoot "build"

# Clean previous builds if requested
if ($Clean) {
    Write-Host "Cleaning previous builds..." -ForegroundColor Yellow
    if (Test-Path $DistDir) { Remove-Item $DistDir -Recurse -Force }
    if (Test-Path $BuildDir) { Remove-Item $BuildDir -Recurse -Force }
}

# Change to project root
Set-Location $ProjectRoot

try {
    # Build executable with PyInstaller
    Write-Host "Building executable with PyInstaller..." -ForegroundColor Cyan
    
    if ($BuildType -eq "portable") {
        # Build portable version
        & pyinstaller build.spec --clean --noconfirm
    } else {
        # Build for installer (without UPX for better compatibility)
        $spec_content = Get-Content "build.spec"
        $spec_content = $spec_content -replace "upx=True", "upx=False"
        $spec_content | Set-Content "build_installer.spec"
        
        & pyinstaller build_installer.spec --clean --noconfirm
        Remove-Item "build_installer.spec" -Force
    }
    
    if ($LASTEXITCODE -ne 0) {
        throw "PyInstaller build failed"
    }
    
    # Check if executable was created
    $ExePath = Join-Path $DistDir "Tranfastic.exe"
    if (!(Test-Path $ExePath)) {
        throw "Executable not found: $ExePath"
    }
    
    Write-Host "Executable built successfully: $ExePath" -ForegroundColor Green
    
    if ($BuildType -eq "installer") {
        # Build installer with NSIS
        Write-Host "Building installer with NSIS..." -ForegroundColor Cyan
        
        # Check if NSIS is installed
        $NSISPath = ""
        $PossiblePaths = @(
            "${env:ProgramFiles}\NSIS\makensis.exe",
            "${env:ProgramFiles(x86)}\NSIS\makensis.exe",
            "C:\Program Files\NSIS\makensis.exe",
            "C:\Program Files (x86)\NSIS\makensis.exe"
        )
        
        foreach ($Path in $PossiblePaths) {
            if (Test-Path $Path) {
                $NSISPath = $Path
                break
            }
        }
        
        if ($NSISPath -eq "") {
            Write-Host "NSIS not found. Installing NSIS..." -ForegroundColor Yellow
            Write-Host "Please download and install NSIS from: https://nsis.sourceforge.io/Download" -ForegroundColor Red
            Write-Host "Or install via Chocolatey: choco install nsis" -ForegroundColor Yellow
            throw "NSIS is required to build installer"
        }
        
        # Build installer
        $NSIScript = Join-Path $InstallerDir "tranfastic_installer.nsi"
        Set-Location $InstallerDir
        
        & $NSISPath $NSIScript
        
        if ($LASTEXITCODE -ne 0) {
            throw "NSIS build failed"
        }
        
        # Check if installer was created (dynamic version detection)
        $InstallerPattern = Join-Path $InstallerDir "Tranfastic-*-Setup.exe"
        $InstallerPath = Get-ChildItem $InstallerPattern -ErrorAction SilentlyContinue | Select-Object -First 1 -ExpandProperty FullName
        
        if ($InstallerPath -and (Test-Path $InstallerPath)) {
            Write-Host "Installer built successfully: $InstallerPath" -ForegroundColor Green
            
            # Move installer to dist directory
            $InstallerName = Split-Path $InstallerPath -Leaf
            $FinalInstallerPath = Join-Path $DistDir $InstallerName
            Move-Item $InstallerPath $FinalInstallerPath -Force
            Write-Host "Installer moved to: $FinalInstallerPath" -ForegroundColor Green
        } else {
            throw "Installer not found matching pattern: $InstallerPattern"
        }
    }
    
    # Show file sizes
    Write-Host "`nBuild Summary:" -ForegroundColor Magenta
    $ExeSize = [math]::Round((Get-Item $ExePath).Length / 1MB, 2)
    Write-Host "  Executable: $ExeSize MB" -ForegroundColor White
    
    if ($BuildType -eq "installer") {
        $InstallerFile = Get-ChildItem (Join-Path $DistDir "Tranfastic-*-Setup.exe") -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($InstallerFile) {
            $InstallerSize = [math]::Round($InstallerFile.Length / 1MB, 2)
            Write-Host "  Installer: $InstallerSize MB" -ForegroundColor White
        }
    }
    
    Write-Host "`nBuild completed successfully!" -ForegroundColor Green
    
} catch {
    Write-Host "Build failed: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
} finally {
    Set-Location $ProjectRoot
}

# Optional: Test the executable
if ($BuildType -eq "portable") {
    Write-Host "`nWould you like to test the portable executable? (y/n): " -ForegroundColor Yellow -NoNewline
    $TestResponse = Read-Host
    if ($TestResponse -eq "y" -or $TestResponse -eq "Y") {
        Write-Host "Starting Tranfastic..." -ForegroundColor Cyan
        Start-Process $ExePath
    }
}
