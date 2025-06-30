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
  <a href="#-configuration" style="color: #0366d6">Configuration</a>
  .
  <a href="#-troubleshooting" style="color: #0366d6">Troubleshooting</a>
  .
  <a href="#-contributing" style="color: #0366d6">Contributing</a>
  .
  <a href="#%EF%B8%8F-development-roadmap" style="color: #0366d6">Roadmap</a>
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

<img src="assets/howto.gif" alt="Tranfastic" style="border-radius: 16px;" />

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
- **🔒 Privacy Focused:** Does not store any translation history or sensitive information.
- **🎨 Clean Interface:** Minimalist design that doesn't distract from your work.

## 🚀 Quick Start

### 📥 Download

> No installation required! Works on any Windows 10/11 machine.

1. Download `Tranfastic.exe` from [Releases](../../releases/latest)
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

## ⚙️ Configuration

- **Language Settings:** Set your preferred source and destination languages in the settings menu.
- **Shortcut Customization:** Modify the hotkey to suit your workflow.
- **Launch on Startup (Windows):** Optionally enable Tranfastic to start when your computer boots.

### 📁 User Data

Application creates user data in:

```
%USERPROFILE%\.tranfastic\
├── config.json          # User settings
└── logs\                # Translation logs (if enabled)
    ├── 2024-01-01.log
    └── ...
```

## 🐛 Troubleshooting

### Common Issues

**Application doesn't start**

- Check Windows Defender/Antivirus settings
- Run as administrator if needed
- Ensure Windows 10/11 compatibility

**Hotkey not working**

- Check if hotkey conflicts with other applications
- Try different hotkey combination in settings
- Restart application after changing hotkey

**Translation fails**

- Check internet connection
- Google Translate service might be temporarily unavailable
- Try different source/target language combination

### Antivirus False Positives

Some antivirus software may flag PyInstaller executables. This is a known false positive. The application:

- Does not modify system files
- Only accesses clipboard and creates user data folder
- Is open source - you can verify the code

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

**Current features and future updates organized by phases:**

### ~~✅ Phase 1: Core Foundation (Completed)~~

- [x] Global hotkey and logging implementation
- [x] System tray integration with custom icon and menu
- [x] Minimalist, modern, frameless translation window
- [x] Customizable language and hotkey settings
- [x] Local translation history (optional, per day)
- [x] Dark theme and custom font integration
- [x] Paste translation to previously focused input
- [x] About section in settings
- [x] Portable executable build system
- [x] Windows startup option

### 🔄 Phase 2: User Experience Improvements (In Progress)

- [ ] Prevent focus stealing on initial open
- [ ] Capture text directly from selected fields
- [ ] Add user notifications for translations
- [ ] Quick language switcher in tray menu
- [ ] Customizable window size and transparency
- [ ] Keyboard navigation for all UI
- [ ] Auto-detect and translate clipboard content
- [ ] **Translation History Management:**
  - [ ] Modern GUI interface to view, search, and manage translation history
  - [ ] Database structure with metadata (timestamp, language pairs, frequency)
  - [ ] Star/favorite translations for quick access
  - [ ] Search & filter by text, date, or language pairs
  - [ ] Categories & tags for organization
  - [ ] Bulk operations (delete, export, categorize)
  - [ ] Backup & sync capabilities

### 🚀 Phase 3: Advanced Features

- [ ] Update checker (from GitHub releases)
- [ ] OCR: Translate text from images
- [ ] Voice input and translation
- [ ] Multi-API support (Google, DeepL, Yandex, etc.)
- [ ] Export/import translation history
- [ ] Theming (light/dark/custom themes)
- [ ] In-app feedback and bug reporting

### 🤖 Phase 4: AI & Machine Learning

- [ ] Offline translation (local ML model)
- [ ] Machine learning-based translation improvements
- [ ] Ollama integration for local AI-powered translation
- [ ] Context-aware translations

### 🌍 Phase 5: Platform Expansion

- [ ] Cross-platform support (Linux, macOS)

**Have an idea? Open an issue or pull request!**

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
