# TransWrite
Instant Translator App with GUI

## 📖 About

TransWrite is a lightweight Python application designed for instant, real-time translation while you work. It sits discreetly in your system tray, and a quick hotkey opens a window for text input, making translated text readily available for copying or inserting.

## ✨ Features

- **🌐 Real-time Translation:** Provides on-the-fly translations as you type.
- **⚡ Hotkey Activation:** Opens translation window instantly with a customizable keyboard shortcut.
- **🖥️ System Tray Integration:** Operates silently in the background to minimize clutter.
- **⚙️ Customizable Settings:** Lets you configure source and destination languages.
- **🔔 Notifications:** Option to notify you when translations are ready.
- **🔒 Privacy Focused:** Does not store any translation history or sensitive information.

## 🚀 Getting Started

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/TransWrite.git
    cd TransWrite
    ```
2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Run the Application

1. **Start TransWrite:**
    ```bash
    python main.py
    ```
    The TransWrite icon will appear in your system tray.

2. **Using the Hotkey:**
   - Press `Shift+Alt+D` (default) or set your preferred hotkey in the settings.
   
3. **Input & Translate:**
   - Type or paste text into the pop-up window and press Enter to receive your translation.

4. **Close with Ease:**
   - Press `Esc` to quickly close the pop-up window.

## ⚙️ Configuration

- **Language Settings:** Set your preferred source and destination languages in the settings menu.
- **Shortcut Customization:** Modify the hotkey to suit your workflow.
- **Launch on Startup (Windows):** Optionally enable TransWrite to start when your computer boots.

## 🤝 Contributing

We welcome contributions! To contribute:
1. **Fork the repository** and create a new branch for your feature or bug fix.
2. **Test your changes** to ensure stability.
3. **Submit a pull request**, explaining the changes and any added features.

For bug reports, please open an issue with:
- A clear description of the issue.
- Steps to reproduce the problem.
- The `app.log` file content (located in the application's directory) if available.

## 🛠️ Development Roadmap

**Current features and future updates:**
- [x] Hotkey and logging implementation
- [ ] Prevent focus-stealing on initial open
- [ ] Capture text directly from selected fields
- [ ] Finalize translation function
- [ ] Add user notifications for translations
- [ ] Redesign settings screen for improved usability
- [ ] Enable launch on Windows startup with customizable delay

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
