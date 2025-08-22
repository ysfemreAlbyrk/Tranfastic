# WriteLate - Build Automation Makefile
# Cross-platform compatible with PowerShell

.PHONY: help install build clean test lint format run dev-install build-exe build-portable

# Default target
help:
	@echo "WriteLate - Build Commands"
	@echo "=========================="
	@echo "install        - Install package in development mode"
	@echo "build          - Build package distribution"
	@echo "clean          - Clean build artifacts"
	@echo "test           - Run tests"
	@echo "lint           - Run linting checks"
	@echo "format         - Format code with black"
	@echo "run            - Run the application"
	@echo "dev-install    - Install development dependencies"
	@echo "build-exe      - Build executable with PyInstaller"
	@echo "build-portable - Build portable executable"
	@echo ""

# Install package in development mode
install:
	pip install -e .

# Build package distribution
build:
	python -m build

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	@if exist build rmdir /s /q build
	@if exist dist rmdir /s /q dist
	@if exist *.egg-info rmdir /s /q *.egg-info
	@if exist __pycache__ rmdir /s /q __pycache__
	@for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
	@echo "Clean completed!"

# Run tests
test:
	pytest

# Run linting checks
lint:
	flake8 src/ tests/
	black --check src/ tests/

# Format code with black
format:
	black src/ tests/

# Run the application
run:
	python main.py

# Install development dependencies
dev-install:
	pip install -e ".[dev]"

# Build executable with PyInstaller
build-exe:
	pyinstaller build.spec

# Build portable executable
build-portable:
	pyinstaller build.spec --distpath dist/portable

# Install build dependencies
build-install:
	pip install -e ".[build]"

# Quick development setup
dev-setup: dev-install
	@echo "Development environment setup completed!"
	@echo "Run 'make run' to start the application"

# Full build process
full-build: clean build-install build-exe
	@echo "Full build process completed!"

# Windows-specific commands
windows-clean:
	@echo "Cleaning build artifacts (Windows)..."
	@if exist build rmdir /s /q build
	@if exist dist rmdir /s /q dist
	@if exist *.egg-info rmdir /s /q *.egg-info
	@if exist __pycache__ rmdir /s /q __pycache__
	@for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
	@echo "Clean completed!"

# PowerShell compatible commands
ps-clean:
	powershell -Command "if (Test-Path build) { Remove-Item -Recurse -Force build }"
	powershell -Command "if (Test-Path dist) { Remove-Item -Recurse -Force dist }"
	powershell -Command "if (Test-Path *.egg-info) { Remove-Item -Recurse -Force *.egg-info }"
	powershell -Command "Get-ChildItem -Recurse -Directory -Name '__pycache__' | ForEach-Object { Remove-Item -Recurse -Force $_ }"
	@echo "Clean completed (PowerShell)!"

# Check if running on Windows
is-windows:
	@echo "Detected OS: Windows"
	@echo "Use 'make ps-clean' for PowerShell compatibility"
