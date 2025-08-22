# UTF-8
# Auto-generated version info file
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx

import sys
import os
from pathlib import Path

# Add src to path to import version
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from version import VERSION_INFO

VSVersionInfo(
  ffi=FixedFileInfo(
    # filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
    # Set not needed items to zero 0.
    filevers=VERSION_INFO,
    prodvers=VERSION_INFO,
    # Contains a bitmask that specifies the valid bits 'flags'r
    mask=0x3f,
    # Contains a bitmask that specifies the Boolean attributes of the file.
    flags=0x0,
    # The operating system for which this file was designed.
    # 0x4 - NT and there is no need to change it.
    OS=0x40004,
    # The general type of file.
    # 0x1 - the file is an application.
    fileType=0x1,
    # The function of the file.
    # 0x0 - the function is not defined for this fileType
    subtype=0x0,
    # Creation date and time stamp.
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Yusuf Emre Albayrak'),
        StringStruct(u'FileDescription', u'Tranfastic - Instant Translator'),
        StringStruct(u'FileVersion', u'.'.join(map(str, VERSION_INFO))),
        StringStruct(u'InternalName', u'Tranfastic'),
        StringStruct(u'LegalCopyright', u'MIT License - Open Source Project'),
        StringStruct(u'OriginalFilename', u'Tranfastic.exe'),
        StringStruct(u'ProductName', u'Tranfastic'),
        StringStruct(u'ProductVersion', u'.'.join(map(str, VERSION_INFO))),
        StringStruct(u'Comments', u'System tray translation app with global hotkeys')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
) 