#!/usr/bin/env python3
"""
Version information for Tranfastic application
"""

__version__ = "1.2.0"
VERSION_INFO = (1, 2, 0, 0)

def get_version():
    """Get the version string"""
    return __version__

def get_version_tuple():
    """Get the version as a tuple"""
    return VERSION_INFO

def get_version_info():
    """Get detailed version information"""
    return {
        "version": __version__,
        "major": VERSION_INFO[0],
        "minor": VERSION_INFO[1],
        "patch": VERSION_INFO[2],
        "build": VERSION_INFO[3]
    }

if __name__ == "__main__":
    print(f"Tranfastic v{__version__}")
    print(f"Version tuple: {VERSION_INFO}")
