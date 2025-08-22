#!/usr/bin/env python3
"""
Tranfastic - Instant Translator Application
Main entry point
"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from src.app import TranfasticApp

def main():
    """Main entry point"""
    try:
        # Create and run application
        app = TranfasticApp()
        return app.run()
        
    except KeyboardInterrupt:
        print("\nApplication interrupted by user")
        return 0
        
    except Exception as e:
        print(f"Fatal error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 