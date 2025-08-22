"""
Tranfastic Translator Module
Handles translation operations using Google Translate API
"""

import asyncio
from typing import Optional, Tuple
from googletrans import Translator, LANGUAGES
import logging
from pathlib import Path
from datetime import datetime

class TranslationEngine:
    """Google Translate API wrapper for Tranfastic"""
    
    def __init__(self):
        self.translator = Translator()
        self.logger = logging.getLogger(__name__)
        self._connection_status = False
        self._test_connection()
    
    def _test_connection(self) -> bool:
        """Test connection to Google Translate API"""
        try:
            # Simple test translation
            result = self.translator.translate("test", dest="en")
            self._connection_status = True
            self.logger.info("Google Translate API connection successful")
            return True
        except Exception as e:
            self._connection_status = False
            self.logger.error(f"Google Translate API connection failed: {e}")
            return False
    
    @property
    def is_connected(self) -> bool:
        """Check if translation service is connected"""
        return self._connection_status
    
    def translate(self, text: str, source_lang: str = "auto", target_lang: str = "en") -> Tuple[str, Optional[str], bool]:
        """
        Translate text from source language to target language
        
        Args:
            text: Text to translate
            source_lang: Source language code (default: "auto")
            target_lang: Target language code (default: "en")
            
        Returns:
            Tuple of (translated_text, detected_language, success)
        """
        if not text.strip():
            return "", None, False
        
        try:
            # Handle auto-detect properly
            if source_lang == "auto":
                # For auto-detect, don't pass src parameter at all
                result = self.translator.translate(text, dest=target_lang)
                detected_lang = result.src
                self.logger.info(f"Auto-detected language: {detected_lang}")
            else:
                # For specific source language, pass it explicitly
                result = self.translator.translate(text, src=source_lang, dest=target_lang)
                detected_lang = source_lang
            
            translated_text = result.text
            
            # Verify we got a valid translation
            if not translated_text or translated_text.strip() == "":
                self.logger.error("Empty translation result received")
                return "", detected_lang, False
            
            self.logger.info(f"Translation successful: {text[:50]}... -> {translated_text[:50]}...")
            return translated_text, detected_lang, True
            
        except AttributeError as e:
            self.logger.error(f"Translation failed - Attribute error (likely googletrans internal issue): {e}")
            self._connection_status = False
            return "", None, False
        except Exception as e:
            self.logger.error(f"Translation failed: {e}")
            self._connection_status = False
            return "", None, False
    
    def get_language_name(self, lang_code: str) -> str:
        """Get language name from language code"""
        return LANGUAGES.get(lang_code, lang_code.upper())
    
    def detect_language(self, text: str) -> Optional[str]:
        """Detect language of given text"""
        try:
            result = self.translator.detect(text)
            return result.lang
        except Exception as e:
            self.logger.error(f"Language detection failed: {e}")
            return None
    
    def get_supported_languages(self) -> dict:
        """Get all supported languages"""
        return LANGUAGES.copy()

def save_translation_history(source_text, translated_text, source_lang, target_lang):
    history_dir = Path.home() / ".tranfastic" / "history"
    history_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    history_file = history_dir / f"{today}.txt"
    timestamp = datetime.now().strftime("%H:%M:%S")
    line = f"[{timestamp}] {source_lang} -> {target_lang} | {source_text} => {translated_text}\n"
    with open(history_file, "a", encoding="utf-8") as f:
        f.write(line)

# Global translator instance
translator_engine = TranslationEngine() 