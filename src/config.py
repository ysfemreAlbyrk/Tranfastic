"""
Tranfastic Configuration Module
Handles application settings and constants
"""

import json
import os
from pathlib import Path
from typing import Dict, Any
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
            "restore_clipboard": False,
            "theme": "dark"
        }
        self.config = self.load_config()
        self._sync_startup_setting()
    
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
        
        # Handle startup setting special case
        if key == "start_on_boot":
            self._handle_startup_setting(value)
        
        self.save_config()
    
    def _sync_startup_setting(self):
        """Sync startup setting with Windows registry on app start"""
        try:
            from .startup_manager import startup_manager
            
            # Check current Windows registry status
            registry_enabled = startup_manager.is_startup_enabled()
            config_enabled = self.config.get("start_on_boot", False)
            
            # If they don't match, use the config setting as source of truth
            if registry_enabled != config_enabled:
                startup_manager.set_startup(config_enabled)
                
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Failed to sync startup setting: {e}")
    
    def _handle_startup_setting(self, enabled: bool):
        """Handle changes to startup setting"""
        try:
            from .startup_manager import startup_manager
            
            success = startup_manager.set_startup(enabled)
            if not success:
                # If registry update failed, revert the config value
                self.config["start_on_boot"] = not enabled
                raise Exception("Failed to update Windows startup registry")
                
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Failed to handle startup setting: {e}")
            raise

# Supported languages
SUPPORTED_LANGUAGES = {
    "auto": "Auto Detect",
    "en": "English",
    "tr": "Turkish", 
    "de": "German",
    "es": "Spanish",
    "ja": "Japanese",
    "fr": "French",
    "it": "Italian",
    "ru": "Russian",
    "ar": "Arabic",
    "hi": "Hindi",
    "pt": "Portuguese",
    "nl": "Dutch",
    "pl": "Polish",
    "ro": "Romanian",
    "sv": "Swedish",
    "uk": "Ukrainian"
}

# Application constants
APP_NAME = "Tranfastic"
APP_VERSION = "1.0"
APP_AUTHOR = "Yusuf Emre Albayrak"
GITHUB_URL = "https://github.com/ysfemreAlbyrk/Tranfastic"

# UI Colors (Dark theme)
COLORS = {
    "background": "#222222",
    "text": "#FFFFFF",
    "accent": "#4A90E2",
    "secondary": "#333333",
    "border": "#444444"
} 