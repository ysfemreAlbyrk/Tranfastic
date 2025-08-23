# Changelog

All notable changes to this project will be documented in this file.

## v1.2 - 2025-08-23

### Added 🎉

- **Windows Installer**: NSIS-based installer for easy installation
- **Auto-update system**: Automatic version checking and update functionality
- **Appearance settings tab**: New tabbed interface in settings window for better organization
  - **Adding Popup window opening location settings**: You can now choose to where open the popup window. Example: cursor's monitor, cursor's below, always open on primary monitor.
  - **Adding Popup window size settings**: You can now choose the size of the popup window. Example: small, default, large.
- **PowerShell build script**: Simplified build commands with `make.ps1`

### Changed 🔄

- **Project structure refactoring**: Centralized asset paths for icons and fonts
- **Dynamic window sizing**: Translation and settings windows now adjust dynamically
- **Import system optimization**: Refactored to use absolute import paths
- **Configuration module enhancement**: Added application constants and supported languages

### Fixed 🐛

- Enhanced error handling and logging throughout the application
- Improved clipboard management functionality
- Better startup manager and hotkey handling
- Code optimization and performance improvements

### Technical Improvements 🔧

- Updated `build.spec` to include additional paths and binaries
- Enhanced build process with automated installer creation
- Improved version management system

## v1.1 - 2025-07-03

### Added 🎉

- Connection status check on translation window open
- Clipboard restore functionality as optional setting (disabled by default)
- Extended language support: French, Italian, Russian, Arabic, Hindi, Portuguese, Dutch, Polish, Romanian, Swedish, Ukrainian
- Restart application functionality in tray menu

### Changed 🔄

- Improved dark theme colors (darker background, better contrast)
- Enhanced settings UI with visual improvements and info messages
- Auto-detect language functionality now works properly
- Clipboard paste simulation is now optional based on user preference

### Fixed 🐛

- Auto-detect language feature that was causing NoneType errors
- Translation window connection status display

## v1.0 - 2024-12-03

### Added 🎉

- Initial release of Tranfastic
- Global hotkey support (default: Shift+Alt+D)
- Google Translate integration with auto-detect
- System tray integration with context menu
- Frameless translation window with modern UI
- Settings window with tabbed interface (General & About)
- Dark theme with custom color scheme
- Customizable hotkeys and language preferences
- Windows startup integration
- Translation history logging (optional)
- Portable executable build system
- Support for 6 languages: Auto Detect, English, Turkish, German, Spanish, Japanese
- Application logging with automatic cleanup
- PyQt5-based modern GUI
- Inter font family integration
- Material Symbols Rounded icons
- Drag support for translation window
- Multi-monitor and DPI scaling support
- JSON-based configuration storage
- Windows Registry integration for startup management
- Comprehensive error handling
- MIT License open source release

**🎉 Initial Release** First stable release of Tranfastic - a lightweight, portable instant translator application for Windows.
