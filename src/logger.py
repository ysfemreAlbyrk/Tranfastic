"""
Tranfastic Logging Module
Handles application logging configuration
"""

import logging
import sys
from pathlib import Path
from datetime import datetime

def setup_logging(log_level: str = "INFO") -> logging.Logger:
    """
    Setup application logging
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        
    Returns:
        Configured logger instance
    """
    # Create logs directory
    log_dir = Path.home() / ".tranfastic" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Create log filename with date
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = log_dir / f"{today}.log"
    
    # Configure logging
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Get logger
    logger = logging.getLogger("Tranfastic")
    
    # Log startup
    logger.info("=" * 50)
    logger.info("Tranfastic Application Started")
    logger.info(f"Log file: {log_file}")
    logger.info(f"Log level: {log_level}")
    logger.info("=" * 50)
    
    return logger

def get_logger(name: str) -> logging.Logger:
    """
    Get logger for specific module
    
    Args:
        name: Module name
        
    Returns:
        Logger instance
    """
    return logging.getLogger(f"Tranfastic.{name}")

def log_translation(source_text: str, translated_text: str, source_lang: str, target_lang: str, success: bool):
    """
    Log translation operation
    
    Args:
        source_text: Original text
        translated_text: Translated text
        source_lang: Source language
        target_lang: Target language
        success: Whether translation was successful
    """
    logger = get_logger("Translation")
    
    if success:
        logger.info(f"Translation: {source_lang} → {target_lang}")
        logger.info(f"Source: {source_text}")
        logger.info(f"Result: {translated_text}")
    else:
        logger.error(f"Translation failed: {source_lang} → {target_lang}")
        logger.error(f"Source: {source_text}")

def log_error(error: Exception, context: str = ""):
    """
    Log error with context
    
    Args:
        error: Exception object
        context: Additional context information
    """
    logger = get_logger("Error")
    
    if context:
        logger.error(f"{context}: {error}")
    else:
        logger.error(f"Error: {error}")
    
    # Log full traceback for debugging
    import traceback
    logger.debug(f"Traceback: {traceback.format_exc()}")

def cleanup_old_logs(days_to_keep: int = 7):
    """
    Clean up old log files
    
    Args:
        days_to_keep: Number of days to keep log files
    """
    try:
        log_dir = Path.home() / ".tranfastic" / "logs"
        if not log_dir.exists():
            return
        
        cutoff_date = datetime.now().timestamp() - (days_to_keep * 24 * 60 * 60)
        
        for log_file in log_dir.glob("*.log"):
            if log_file.stat().st_mtime < cutoff_date:
                log_file.unlink()
                get_logger("Cleanup").info(f"Deleted old log file: {log_file}")
                
    except Exception as e:
        get_logger("Cleanup").error(f"Failed to cleanup old logs: {e}") 