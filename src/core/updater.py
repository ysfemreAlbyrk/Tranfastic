#!/usr/bin/env python3
"""
Auto-update system for Tranfastic
Checks GitHub releases for updates and handles downloading/installing
"""

import json
import os
import sys
import subprocess
import tempfile
import hashlib
from pathlib import Path
from typing import Dict, Optional, Tuple
import requests
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtWidgets import QMessageBox, QProgressDialog, QApplication

from ..utils.logger import get_logger
from ..version import __version__, get_version_tuple

logger = get_logger(__name__)

class UpdateChecker(QThread):
    """Background thread for checking updates"""
    update_available = pyqtSignal(dict)  # Emits release info
    update_error = pyqtSignal(str)  # Emits error message
    no_update = pyqtSignal()  # No update available
    
    def __init__(self, repo_owner="ysfemrealbyrk", repo_name="tranfastic"):
        super().__init__()
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
        
    def run(self):
        """Check for updates in background"""
        try:
            logger.info("Checking for updates...")
            
            # Make API request with timeout
            response = requests.get(
                self.api_url, 
                timeout=10,
                headers={'Accept': 'application/vnd.github.v3+json'}
            )
            
            if response.status_code == 200:
                release_data = response.json()
                
                # Parse version from tag (e.g., "v1.2.0" -> "1.2.0")
                latest_version = release_data['tag_name'].lstrip('v')
                current_version = __version__
                
                if self._is_newer_version(latest_version, current_version):
                    logger.info(f"Update available: {current_version} -> {latest_version}")
                    self.update_available.emit(release_data)
                else:
                    logger.info(f"Already up to date: {current_version}")
                    self.no_update.emit()
                    
            elif response.status_code == 404:
                self.update_error.emit("Repository not found")
            else:
                self.update_error.emit(f"API request failed: {response.status_code}")
                
        except requests.exceptions.Timeout:
            self.update_error.emit("Update check timed out")
        except requests.exceptions.RequestException as e:
            self.update_error.emit(f"Network error: {str(e)}")
        except Exception as e:
            logger.error(f"Update check failed: {e}")
            self.update_error.emit(f"Update check failed: {str(e)}")
    
    def _is_newer_version(self, latest: str, current: str) -> bool:
        """Compare version strings (semantic versioning)"""
        try:
            latest_parts = [int(x) for x in latest.split('.')]
            current_parts = [int(x) for x in current.split('.')]
            
            # Pad shorter version with zeros
            max_len = max(len(latest_parts), len(current_parts))
            latest_parts.extend([0] * (max_len - len(latest_parts)))
            current_parts.extend([0] * (max_len - len(current_parts)))
            
            return latest_parts > current_parts
        except (ValueError, AttributeError):
            return False


class UpdateDownloader(QThread):
    """Background thread for downloading updates"""
    download_progress = pyqtSignal(int)  # Progress percentage
    download_completed = pyqtSignal(str)  # Downloaded file path
    download_error = pyqtSignal(str)  # Error message
    
    def __init__(self, download_url: str, filename: str):
        super().__init__()
        self.download_url = download_url
        self.filename = filename
        self.temp_dir = tempfile.gettempdir()
        self.file_path = os.path.join(self.temp_dir, filename)
        
    def run(self):
        """Download update file"""
        try:
            logger.info(f"Downloading update: {self.download_url}")
            
            response = requests.get(self.download_url, stream=True, timeout=30)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            
            with open(self.file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        
                        if total_size > 0:
                            progress = int((downloaded / total_size) * 100)
                            self.download_progress.emit(progress)
            
            logger.info(f"Download completed: {self.file_path}")
            self.download_completed.emit(self.file_path)
            
        except Exception as e:
            logger.error(f"Download failed: {e}")
            self.download_error.emit(str(e))


class AutoUpdater:
    """Main auto-update manager"""
    
    def __init__(self, parent_widget=None):
        self.parent = parent_widget
        self.check_thread = None
        self.download_thread = None
        self.progress_dialog = None
        
    def check_for_updates(self, silent: bool = False):
        """Check for updates (silent = no UI feedback if no updates)"""
        if self.check_thread and self.check_thread.isRunning():
            return
            
        self.check_thread = UpdateChecker()
        self.check_thread.update_available.connect(
            lambda release: self._on_update_available(release, silent)
        )
        self.check_thread.update_error.connect(
            lambda error: self._on_update_error(error, silent)
        )
        self.check_thread.no_update.connect(
            lambda: self._on_no_update(silent)
        )
        
        self.check_thread.start()
        
    def _on_update_available(self, release_data: Dict, silent: bool):
        """Handle when update is available"""
        version = release_data['tag_name'].lstrip('v')
        release_notes = release_data.get('body', 'No release notes available.')
        
        # Find the installer asset (MSI or EXE)
        installer_asset = None
        for asset in release_data.get('assets', []):
            name = asset['name'].lower()
            if name.endswith('.msi') or (name.endswith('.exe') and 'installer' in name):
                installer_asset = asset
                break
        
        if not installer_asset:
            # Fallback to portable EXE
            for asset in release_data.get('assets', []):
                if asset['name'].lower().endswith('.exe'):
                    installer_asset = asset
                    break
        
        if not installer_asset:
            self._show_error("No installer found in the latest release.")
            return
            
        # Show update dialog
        msg = QMessageBox(self.parent)
        msg.setWindowTitle("Update Available")
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Tranfastic v{version} is available!")
        msg.setInformativeText(
            f"Current version: v{__version__}\n"
            f"New version: v{version}\n\n"
            "Would you like to download and install the update?"
        )
        msg.setDetailedText(f"Release Notes:\n\n{release_notes}")
        
        download_btn = msg.addButton("Download & Install", QMessageBox.AcceptRole)
        skip_btn = msg.addButton("Skip This Version", QMessageBox.RejectRole)
        later_btn = msg.addButton("Remind Me Later", QMessageBox.DestructiveRole)
        
        msg.exec_()
        
        if msg.clickedButton() == download_btn:
            self._download_update(installer_asset)
        elif msg.clickedButton() == skip_btn:
            # TODO: Save skipped version to config
            pass
            
    def _on_update_error(self, error: str, silent: bool):
        """Handle update check error"""
        if not silent:
            self._show_error(f"Failed to check for updates:\n{error}")
            
    def _on_no_update(self, silent: bool):
        """Handle no update available"""
        if not silent:
            msg = QMessageBox(self.parent)
            msg.setWindowTitle("No Updates")
            msg.setIcon(QMessageBox.Information)
            msg.setText("You're running the latest version!")
            msg.setInformativeText(f"Tranfastic v{__version__} is up to date.")
            msg.exec_()
            
    def _download_update(self, asset: Dict):
        """Download and install update"""
        download_url = asset['browser_download_url']
        filename = asset['name']
        
        # Show progress dialog
        self.progress_dialog = QProgressDialog(
            "Downloading update...", "Cancel", 0, 100, self.parent
        )
        self.progress_dialog.setWindowTitle("Updating Tranfastic")
        self.progress_dialog.setWindowModality(2)  # ApplicationModal
        self.progress_dialog.show()
        
        # Start download
        self.download_thread = UpdateDownloader(download_url, filename)
        self.download_thread.download_progress.connect(
            self.progress_dialog.setValue
        )
        self.download_thread.download_completed.connect(
            self._on_download_completed
        )
        self.download_thread.download_error.connect(
            self._on_download_error
        )
        
        self.progress_dialog.canceled.connect(self._cancel_download)
        self.download_thread.start()
        
    def _on_download_completed(self, file_path: str):
        """Handle download completion"""
        if self.progress_dialog:
            self.progress_dialog.close()
            
        # Install the update
        try:
            if file_path.lower().endswith('.msi'):
                self._install_msi(file_path)
            elif file_path.lower().endswith('.exe'):
                self._install_exe(file_path)
        except Exception as e:
            self._show_error(f"Installation failed:\n{str(e)}")
            
    def _on_download_error(self, error: str):
        """Handle download error"""
        if self.progress_dialog:
            self.progress_dialog.close()
        self._show_error(f"Download failed:\n{error}")
        
    def _cancel_download(self):
        """Cancel download"""
        if self.download_thread and self.download_thread.isRunning():
            self.download_thread.terminate()
            self.download_thread.wait()
            
    def _install_msi(self, msi_path: str):
        """Install MSI package"""
        msg = QMessageBox(self.parent)
        msg.setWindowTitle("Install Update")
        msg.setIcon(QMessageBox.Question)
        msg.setText("Update downloaded successfully!")
        msg.setInformativeText(
            "The installer will now run. Tranfastic will close during installation.\n\n"
            "Click 'Install Now' to proceed."
        )
        
        install_btn = msg.addButton("Install Now", QMessageBox.AcceptRole)
        cancel_btn = msg.addButton("Cancel", QMessageBox.RejectRole)
        msg.exec_()
        
        if msg.clickedButton() == install_btn:
            try:
                # Run MSI installer
                subprocess.Popen([
                    'msiexec', '/i', msi_path, '/qb', '/norestart'
                ], shell=True)
                
                # Close application
                QApplication.quit()
                
            except Exception as e:
                self._show_error(f"Failed to start installer:\n{str(e)}")
                
    def _install_exe(self, exe_path: str):
        """Install EXE (portable update)"""
        msg = QMessageBox(self.parent)
        msg.setWindowTitle("Update Ready")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Update downloaded successfully!")
        msg.setInformativeText(
            "For portable installations, you need to manually replace the executable.\n\n"
            f"Downloaded file: {exe_path}\n"
            f"Replace your current Tranfastic.exe with this file."
        )
        
        open_folder_btn = msg.addButton("Open Download Folder", QMessageBox.AcceptRole)
        ok_btn = msg.addButton("OK", QMessageBox.AcceptRole)
        msg.exec_()
        
        if msg.clickedButton() == open_folder_btn:
            # Open folder containing the download
            folder_path = os.path.dirname(exe_path)
            os.startfile(folder_path)  # Windows-specific
            
    def _show_error(self, message: str):
        """Show error dialog"""
        msg = QMessageBox(self.parent)
        msg.setWindowTitle("Update Error")
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Update Error")
        msg.setInformativeText(message)
        msg.exec_()
        
    def schedule_periodic_check(self, interval_hours: int = 24):
        """Schedule periodic update checks"""
        timer = QTimer()
        timer.timeout.connect(lambda: self.check_for_updates(silent=True))
        timer.start(interval_hours * 60 * 60 * 1000)  # Convert to milliseconds
        return timer


def check_for_updates_startup():
    """Check for updates at startup (non-blocking)"""
    try:
        updater = AutoUpdater()
        updater.check_for_updates(silent=True)
    except Exception as e:
        logger.error(f"Startup update check failed: {e}")
