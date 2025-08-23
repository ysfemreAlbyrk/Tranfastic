<p align="center">
  <a href="https://github.com/ysfemreAlbyrk/Tranfastic">
    <img src="./assets/icon.png" alt="Tranfastic Icon" width="150">
  </a>
</p>

<h1 align="center">Tranfastic</h1>

<h4 align="center">Lightweight Portable Instant Translator App with GUI</h4>

<p align="center">
  <br>
  <a href="#-features" style="color: #0366d6">Features</a>
  .
  <a href="#-quick-start" style="color: #0366d6">Quick Start</a>
  .
  <a href="#-development" style="color: #0366d6">Development</a>
  .
  <a href="#-contributing" style="color: #0366d6">Contributing</a>
  .
  <a href="docs/LEGAL.md" style="color: #0366d6">Legal</a>
  .
  <a href="docs/TROUBLESHOOTING.md" style="color: #0366d6">Troubleshooting</a>
  .
  <a href="docs/ROADMAP.md" style="color: #0366d6">Roadmap</a>
  .
  <a href="#-license" style="color: #0366d6">License</a>
  <br>
</p>

<p align="center">
  <a href="docs/readme_tr.md" style="color: #E34C26">🇹🇷 Türkçe</a>
  <br>
</p>

<p align="center">
   <a href="https://www.python.org/downloads/">
      <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python 3.7+" />
   </a>
   <a href="https://www.microsoft.com/windows">
      <img src="https://img.shields.io/badge/Platform-Windows-blue.svg" alt="Windows" />
   </a>
   <a href="https://opensource.org/licenses/MIT">
      <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" />
   </a>
   <a href="../../releases/latest">
      <img src="https://img.shields.io/badge/Download-Portable%20EXE-green.svg" alt="Download Portable" />
   </a>
</p>

<div align="center">

![Tranfastic](docs/assets/howto.gif)

</div>

Tranfastic is a lightweight Python application designed for instant,
real-time translation while you work. It sits discreetly in your
system tray, and a quick hotkey opens a window for text input, making
translated text readily available for copying or inserting.

## ✨ Features

- **🔥 Instant Translation**: Quick translate with global hotkey (`Shift+Alt+D`)
- **⚡ Hotkey Activation:** Opens translation pop up instantly with a customizable keyboard shortcut.
- **🌐 Multiple Languages**: Support for _English_, _Turkish_, _German_, _Spanish_, _Japanese_ and more.
- **📱 System Tray**: Runs quietly in the background.
- **📋 Clipboard Integration**: Automatic paste translated text
- **🔧 Configurable**: Customizable hotkeys and languages
- **🔄 Auto-Update**: Automatic updates
- **🔒 Privacy Focused:** Does not store any translation history or sensitive information.
- **🎨 Clean Interface:** Minimalist design that doesn't distract from your work.

## 🚀 Quick Start

### 📥 Download

Choose your preferred installation method:

#### 🖥️ **Windows Installer (Recommended)**

1. Download `Tranfastic-Setup.exe` from [**Releases**](../../releases/latest)
2. Run the installer as administrator
3. Launch from Start Menu or Desktop shortcut

#### 📦 **Portable Version**

> No installation required! Works on any Windows 10/11 machine. Best for trying out the application.

1. Download `Tranfastic.exe` from [**Releases**](../../releases/latest)
2. Copy to any folder (Desktop, USB drive, etc.)
3. Double-click to run

### 🎯 How to Use

1. **Using the Hotkey:**
   - Press `Shift+Alt+D` (default) or set your preferred hotkey in the settings.
2. **Input & Translate:**

   - Type or paste text into the pop-up window and press Enter to receive your translation.

3. **Close with Ease:**
   - Press `Esc` to quickly close the pop-up window.

## 🛠️ Development

### 📦 Installation

1. **First, clone the repository:**

```bash
git clone https://github.com/your-username/Tranfastic.git
cd Tranfastic
```

2. **Setup virtual envoirement**

```bash

python -m venv venv

# Activate virtual envoirement
./venv/Script/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

### 🏃 Run the Application

1. **Start Tranfastic:**

```bash
python main.py
```

The Tranfastic icon will appear in your system tray.

### 🔨 Build Portable Executable

```bash
# Clone repository
git clone https://github.com/ysfemreAlbyrk/Tranfastic.git
cd Tranfastic

# Install dependencies
pip install -r requirements.txt

# Build portable executable
./build_portable.bat
```

The executable will be created in `dist/Tranfastic.exe`

## 🐛 Need Help?

Having issues? Check our comprehensive [Troubleshooting Guide](docs/TROUBLESHOOTING.md) for solutions to common problems.

## 🤝 Contributing

We welcome contributions! To contribute:

1. **Fork the repository** and create a new branch for your feature or bug fix.
2. **Test your changes** to ensure stability.
3. **Submit a pull request**, explaining the changes and any added features.

For bug reports, please open an issue with:

- A clear description of the issue.
- Steps to reproduce the problem.
- The `logs/[date].log` file content (located in the application's directory) if available.

## 🛠️ Development Roadmap

See our detailed [Development Roadmap](docs/ROADMAP.md) for planned features, timelines, and how to contribute to Tranfastic's future.

**Quick highlights:**

- 🔄 **Phase 2 (In Progress)**: User experience improvements and translation history management
- 🚀 **Phase 3**: Advanced features including OCR, voice input, and multi-API support
- 🤖 **Phase 4**: AI & machine learning integration (via ollama)
- 🌍 **Phase 5**: Cross-platform expansion

## 🙏 Open Source Dependencies

Tranfastic wouldn't be possible without these amazing open source projects:

- **[googletrans](https://github.com/ssut/py-googletrans)** - Google Translate API wrapper that powers our translation engine
- **[PyQt5](https://www.riverbankcomputing.com/software/pyqt/)** - Cross-platform GUI framework for our modern, responsive interface
- **[pystray](https://github.com/moses-palmer/pystray)** - System tray integration that keeps Tranfastic running silently in the background
- **[keyboard](https://github.com/boppreh/keyboard)** - Global hotkey detection for instant translation window activation
- **[Inter Font](https://github.com/rsms/inter)** - Beautiful, modern font family for our clean interface
- **[Material Symbols](https://fonts.google.com/icons)** - Google's Material Design icons for UI elements
- **[pywin32](https://github.com/mhammond/pywin32)** - Windows-specific APIs for seamless Windows integration

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
