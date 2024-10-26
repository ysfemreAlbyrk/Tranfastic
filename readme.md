# TransWrite
Instant translator app with GUI

## About

TransWrite is a Python application designed to provide instant translations while you work. It sits discreetly in your system tray and, upon triggering a hotkey, pops up a window to input text for translation. The translated text is then ready for immediate use.

## Features

- **Real-time Translation:** Get translations on-the-fly as you type.
- **Hotkey Activation:**  Trigger the translation window with a customizable keyboard shortcut.
- **System Tray Integration:**  Runs silently in the background, minimizing clutter.
- **Customizable Settings:**  Adjust source and destination languages to your preference.

## Getting Started
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
## Usage

1.  **Run the application:**
    
    ```bash
    python main.py 
    ```
    
	TransWrite will appear in your system tray.
2. **Select the field you want to translate:**
	Use the default hotkey (Shift+Alt+D) or customize it in the settings.
3.  **A small window will pop up. Type or paste the text you want to translate.**
4.  **Press enter, the translation is automatically added to the field you selected.**

## Configuration

-   **Language Settings:**  You can change the source and destination languages within the application's settings menu.
# TODO's
- [x] Shortcut implementation
- [x] Logging implementation

- [ ] Prevent focusing when first opened

- [ ] Capture written text
- [ ] Translation implementation
- [ ] Complete translation with (Enter)
- [ ] Close with (Esc)

- [ ] Send notifications

- [ ] Redesign settings screen
    - [ ] Set wait time
    - [ ] Configure shortcut

- [ ] Launch at Windows startup
    - [ ] Add option to settings
