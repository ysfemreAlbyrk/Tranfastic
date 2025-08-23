"""
About Tab Module
Contains application information, version, author and license details
"""

import webbrowser
from pathlib import Path

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from ...utils.config import COLORS, APP_NAME, APP_VERSION, APP_AUTHOR, GITHUB_URL, APP_ICON_PATH
from ...utils.runtime import get_display_version


class AboutTab(QWidget):
    """About tab widget"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        """Setup about tab UI"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(12)

        # Top area: left (title + version/author) and right (icon)
        top_layout = QHBoxLayout()
        top_layout.setSpacing(0)

        # Left block (title and version/author)
        left_box = QVBoxLayout()
        left_box.setSpacing(20)
        title_label = QLabel(f"<p style='font-size:48px; font-weight:bold; font-family:Inter; color: #fff;'>{APP_NAME}</p>")
        left_box.addWidget(title_label)
        info_label = QLabel(
            f"<span style='font-size:12px; font-weight:600;'>Version:</span> "
            f"<span style='font-size:12px; font-style:italic;'>v{get_display_version()}</span> "
            f"<span style='font-size:12px; font-weight:600;'>&nbsp;&nbsp;&nbsp;&nbsp;Author:</span> "
            f"<span style='font-size:12px;'>{APP_AUTHOR}</span>"
        )
        info_label.setStyleSheet("QLabel { margin-left: 5px; }")
        left_box.addWidget(info_label)
        left_box.addStretch()
        top_layout.addLayout(left_box, stretch=1)

        # Right block (icon)
        icon_label = QLabel()
        icon_path = str((Path(__file__).parent.parent.parent.parent / APP_ICON_PATH).resolve())
        pixmap = QPixmap(icon_path)
        pixmap = pixmap.scaled(96, 96, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_label.setPixmap(pixmap)
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setStyleSheet("margin: 0px;")
        top_layout.addWidget(icon_label, stretch=0)

        main_layout.addLayout(top_layout)

        # Bottom line
        hr = QFrame()
        hr.setFrameShape(QFrame.HLine)
        hr.setFrameShadow(QFrame.Sunken)
        hr.setFixedHeight(1)
        hr.setStyleSheet(f"background-color: {COLORS['border']}; color: {COLORS['border']}; height: 1px;")
        main_layout.addWidget(hr)

        # Other content (github button, description, license etc.)
        main_layout.addSpacing(10)
        desc_label = QLabel(
            f"<b>About {APP_NAME}</b><br>"
            f"{APP_NAME} is a lightweight Python application for instant, real-time translation while you work."
        )
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("font-size: 13px; margin-bottom: 8px;")
        main_layout.addWidget(desc_label)

        github_btn = QPushButton("GitHub Repository")
        github_btn.setCursor(Qt.PointingHandCursor)
        github_btn.setStyleSheet("font-weight: bold; padding: 8px 18px; font-size: 13px;")
        github_btn.clicked.connect(lambda: webbrowser.open(GITHUB_URL))
        main_layout.addWidget(github_btn, alignment=Qt.AlignLeft)

        # Add vertical spacing
        main_layout.addSpacing(50)

        license_label = QLabel(
            "<b>License:</b> MIT License<br>"
            "<span style='font-size:11px;color:#aaa;'>A short and simple permissive license with conditions only requiring preservation of copyright and license notices.</span>"
        )
        license_label.setStyleSheet(f"background:{COLORS['secondary']};padding:10px 14px;border-radius:6px;font-size:12px;")
        license_label.setWordWrap(True)
        main_layout.addWidget(license_label)

        # Google Translate service note
        service_note = QLabel(
            "<span style='color:rgba(255, 119, 0, 1);'><b>This tool uses Google Translate™ services with py-googletrans.</b><br></span>"
            "<span style='font-size:11px;color:rgba(255, 119, 0, 1);'>If translation does not work, it may be due to issues with Google Translate services or connectivity.</span>"
        )
        service_note.setStyleSheet("background:rgba(255, 119, 0, 0.1);padding:5px 10px;border-radius:6px;border: 2px dashed #ff7700;font-size:12px;")
        service_note.setWordWrap(True)
        service_note.setAlignment(Qt.AlignBottom)
        main_layout.addWidget(service_note)

        main_layout.addStretch()
        self.setLayout(main_layout)
