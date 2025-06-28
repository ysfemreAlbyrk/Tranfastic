"""
Tranfastic Translator Module
Handles translation operations using Google Translate API
"""

import asyncio
from typing import Optional, Tuple
from googletrans import Translator, LANGUAGES
import logging

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
            # Perform translation
            result = self.translator.translate(
                text, 
                src=source_lang if source_lang != "auto" else None,
                dest=target_lang
            )
            
            translated_text = result.text
            detected_lang = result.src if source_lang == "auto" else source_lang
            
            self.logger.info(f"Translation successful: {text[:50]}... -> {translated_text[:50]}...")
            return translated_text, detected_lang, True
            
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

# Global translator instance
translator_engine = TranslationEngine() 