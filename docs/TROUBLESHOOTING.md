# Troubleshooting Guide

This guide helps you resolve common issues with Tranfastic.

## 🚀 Quick Fixes

Before diving into specific issues, try these common solutions:

1. **Restart the application** - Close from system tray and reopen
2. **Run as administrator** - Right-click and "Run as administrator"
3. **Check your internet connection** - Translation requires internet access
4. **Restart Windows** - Sometimes resolves system-level conflicts
5. **Check antivirus settings** - See [Antivirus Issues](#antivirus-false-positives)
6. **Check if the hotkey is already in use** - See [Hotkey Not Working](#hotkey-not-working)

## 🐛 Common Issues

### Application Doesn't Start

**Symptoms:**

- Double-clicking the .exe does nothing
- No system tray icon appears
- Process doesn't show in Task Manager

**Solutions:**

- Check Windows Defender/Antivirus settings (see [Antivirus Issues](#antivirus-false-positives))
- Ensure Windows 10/11 compatibility
- Try running as administrator
- Check if previous instance is still running in Task Manager
- Download the latest version from [Releases](https://github.com/ysfemreAlbyrk/Tranfastic/releases)

### Hotkey Not Working

**Symptoms:**

- Pressing hotkey combination doesn't open translation window
- Hotkey works sometimes but not always

**Solutions:**

- Check if hotkey conflicts with other applications
- Try a different hotkey combination in settings
- Restart application after changing hotkey
- Make sure application is running (check system tray)

### Translation Fails

**Symptoms:**

- "Translation failed" message appears
- Window shows "Not Connected" status
- Empty translation results

**Solutions:**

- Check your internet connection
- Try different source/target language combination
- Wait a few minutes and try again (rate limiting)
- Restart the application

### Settings Not Saving

**Symptoms:**

- Changes in settings don't persist after restart
- Default settings keep returning

**Solutions:**

- Run application as administrator
- Check if `%USERPROFILE%\.tranfastic\` folder exists and is writable
- Manually delete config file and restart: `%USERPROFILE%\.tranfastic\config.json`

### System Tray Icon Missing

**Symptoms:**

- Application is running but no tray icon visible
- Can't access settings or close application

**Solutions:**

- Check Windows notification area settings
- Show hidden icons in system tray
- Restart Windows Explorer process
- End process in Task Manager and restart application

## 📊 Performance Issues

### High Memory Usage

**Symptoms:**

- Application uses more RAM than expected
- System becomes slower after running Tranfastic

**Solutions:**

- Normal memory usage is 50-100MB
- Restart application if memory usage exceeds 200MB
- Report issue with memory usage details

### Slow Translation

**Symptoms:**

- Translation takes longer than 5 seconds

**Potential Causes:**

- Slow internet connection
- Google Translate API rate limiting
- Large text input

**Solutions:**

- Check internet speed
- Translate shorter text segments
- Wait and try again later

## 🚀 Reporting Bugs

When reporting bugs, please include:

**Template:**

```
**Environment:**
- OS: Windows 11 22H2
- App Version: v1.0.0

**Issue:**
Brief description of the problem

**Steps to Reproduce:**
1. Step one
2. Step two
3. Error occurs

**Describe the bug:**
What happens
```
