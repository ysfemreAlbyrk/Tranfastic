# Tranfastic Installer

This directory contains the necessary files to create Windows installers for Tranfastic.

## 🛠️ Installer Types

### 1. **NSIS Installer (Recommended)**

- **File**: `tranfastic_installer.nsi`
- **Output**: `Tranfastic-Setup.exe`
- **Features**:
  - Professional Windows installer
  - Start Menu and Desktop shortcuts
  - Uninstaller included
  - Registry integration
  - Program Files installation

### 2. **cx_Freeze MSI**

- **File**: `installer_config.py`
- **Output**: `Tranfastic.msi`
- **Features**:
  - Windows MSI package
  - Suitable for system administrators
  - Deployable via Group Policy

## 🚀 Building Installer

### Automated Build (Recommended)

```powershell
# Build all installers
.\make.ps1 build-installer

# Or run installer script directly
.\installer\build_installer.ps1 -BuildType installer -Clean
```

### Manual Build

#### NSIS Installer

```powershell
# 1. Create executable
pyinstaller build.spec --clean

# 2. Create NSIS installer (NSIS must be installed)
cd installer
makensis tranfastic_installer.nsi
```

#### cx_Freeze MSI

```powershell
# Create MSI with cx_Freeze
python installer/installer_config.py bdist_msi
```

## 📋 Requirements

### For NSIS Installer

- **NSIS**: [Download](https://nsis.sourceforge.io/Download)
- **Install via Chocolatey**: `choco install nsis`

### For cx_Freeze MSI

- **cx_Freeze**: `pip install cx_Freeze`

## 🔧 Configuration

### Editing NSIS Script

Edit `tranfastic_installer.nsi` to:

- Update version number
- Add additional files
- Modify registry settings
- Add custom installation steps

### cx_Freeze Settings

In `installer_config.py`:

- Update package dependencies
- Specify files to include
- Configure MSI properties

## 📁 Output Files

After build process in `dist/` directory:

- `Tranfastic.exe` - Portable executable
- `Tranfastic-Setup.exe` - NSIS installer
- `Tranfastic.msi` - MSI package (if created)
- `*.sha256` - Checksum files

## 🔒 Security

- SHA256 checksums are automatically generated for all files
- Code signing certificate can be added
- May trigger false positive warnings from virus scanners

## 🚀 GitHub Releases

The `.github/workflows/release.yml` workflow automatically:

1. Triggers on tag push
2. Builds on Windows
3. Creates GitHub Release
4. Uploads assets
5. Adds checksums

## 🐛 Troubleshooting

### NSIS Not Found

```powershell
# Install NSIS with Chocolatey
choco install nsis

# Or download manually and add to PATH
```

### PyInstaller Error

```powershell
# Clear cache
pyinstaller --clean build.spec

# Or clean all build files
.\make.ps1 clean
```

### Executable Not Working

- Check antivirus software
- Add Windows Defender exclusion
- Verify dependencies

## 📞 Support

For installer-related issues:

- [GitHub Issues](https://github.com/ysfemrealbyrk/tranfastic/issues)
- [Troubleshooting Guide](../docs/TROUBLESHOOTING.md)
