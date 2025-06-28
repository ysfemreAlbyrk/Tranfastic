"""
Tranfastic Configuration Module
Handles application settings and constants
"""

import json
import os
from pathlib import Path
from typing import Dict, Any

#TODO: Add a way to change the start on boot.
class Config:
    """Application configuration manager"""
    
    def __init__(self):
        self.config_dir = Path.home() / ".tranfastic"
        self.config_file = self.config_dir / "config.json"
        self.default_config = {
            "source_language": "auto",
            "target_language": "en",
            "hotkey": "shift+alt+d",
            "start_on_boot": False,
            "save_history": False,
            "theme": "dark"
        }
        self.config = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return self.create_default_config()
        except Exception:
            return self.create_default_config()
    
    def create_default_config(self) -> Dict[str, Any]:
        """Create default configuration file"""
        self.config_dir.mkdir(exist_ok=True)
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.default_config, f, indent=2, ensure_ascii=False)
        return self.default_config.copy()
    
    def save_config(self):
        """Save current configuration to file"""
        self.config_dir.mkdir(exist_ok=True)
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
    
    def get(self, key: str, default=None):
        """Get configuration value"""
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set configuration value"""
        self.config[key] = value
        self.save_config()

# Supported languages
SUPPORTED_LANGUAGES = {
    "auto": "Auto Detect",
    "en": "English",
    "tr": "Turkish", 
    "de": "German",
    "es": "Spanish",
    "ja": "Japanese"
}

# Application constants
APP_NAME = "Tranfastic"
APP_VERSION = "1.0"
APP_AUTHOR = "Yusuf Emre Albayrak"
GITHUB_URL = "https://github.com/ysfemreAlbyrk/Tranfastic"

# UI Colors (Dark theme)
COLORS = {
    "background": "#353535",
    "text": "#FFFFFF",
    "accent": "#4A90E2",
    "secondary": "#2C2C2C",
    "border": "#555555"
} 