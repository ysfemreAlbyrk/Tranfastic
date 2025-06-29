@echo off
echo Building Tranfastic...

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found! Download from: https://python.org
    pause
    exit 1
)

:: Install PyInstaller if needed
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

:: Clean previous builds
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"

:: Build
echo Building...
pyinstaller build.spec --clean --noconfirm

:: Check result
if exist "dist\Tranfastic.exe" (
    echo.
    echo Build successful!
    echo File: dist\Tranfastic.exe
    for %%f in (dist\Tranfastic.exe) do echo Size: %%~zf bytes
) else (
    echo.
    echo Build failed!
    echo Try: pip install -r requirements.txt
)

pause 