# Tranfastic Development Roadmap

This document outlines the planned features and improvements for Tranfastic.

## Version: _v1.1_

## ~~✅ Phase 1: Core Foundation~~

All foundational features have been implemented and are stable:

- [x] Global hotkey and logging implementation
- [x] System tray integration with custom icon and menu
- [x] Minimalist, modern, frameless translation window
- [x] Customizable language and hotkey settings
- [x] Local translation history (optional, per day)
- [x] Dark theme and custom font integration
- [x] Paste translation to previously focused input
- [x] About section in settings
- [x] Portable executable build system
- [x] Windows startup option

## 🖼️ Phase 2: User Experience Improvements

- [ ] Popup window DPI scaling
- [ ] Popup window position and size customization
- [ ] Quick language switcher in tray menu
- [ ] Auto-detect and translate clipboard content
- [ ] Setup installer (MSI installer for Windows)
- [ ] Auto-update system (from GitHub releases)
- [ ] Popup window icon rework for status indication
- [ ] Customizable window size and transparency

### Translation History Management

- [ ] Modern GUI interface to view, search, and manage translation history
- [ ] Database structure with metadata (timestamp, language pairs, frequency)
- [ ] Star/favorite translations for quick access
- [ ] Search & filter by text, date, or language pairs
- [ ] Categories & tags for organization
- [ ] Bulk operations (delete, export, categorize)

## 🔄 Phase 3: Extra Features

- [ ] Voice input and translation
- [ ] Multi-API support (Google, DeepL, Yandex, etc.)
- [ ] Export/import translation history
- [ ] Theming system (light/dark/custom themes)

## 🤖 Phase 4: AI & Machine Learning

- [ ] Offline translation (local ML model)
- [ ] Machine learning-based translation improvements
- [ ] Ollama integration for local AI-powered translation
- [ ] Context-aware translations
- [ ] Auto-correction for common mistakes
- [ ] Personalized translations based on user preferences
- [ ] Translation language style (formal, informal, etc.)

## 🧠 Phase 5: Intelligent Word Discovery

**Concept**: When you know what you want to say but can't remember the exact word, describe it and get suggestions.

- [ ] Reverse Translation Engine: Input descriptions/definitions to find the exact word
- [ ] Context-aware Word Suggestions: Multiple relevant options based on your description

### Example Use Cases

```
Input: "A place where football matches are played"
Output: Stadium, Arena, Field, Ground, Pitch

Input: "Feeling happy and excited about something"
Output: Enthusiastic, Thrilled, Elated, Excited, Joyful

Input: "A tool for writing that uses ink"
Output: Pen, Fountain pen, Ballpoint pen, Marker
```

### Technical Implementation

- [ ] AI-powered Definition Matching: Use language models to understand descriptions
- [ ] Semantic Search Database: Build/integrate word-definition databases
- [ ] Confidence Scoring: Rank suggestions by relevance
- [ ] Learning System: Improve suggestions based on user choices
- [ ] Offline Capability: Local word database for basic functionality

### User Interface

- [ ] Quick Description Mode: Special input mode for word discovery
- [ ] Suggestion Cards: Visual cards showing word + definition + usage
- [ ] One-click Selection: Easy selection and insertion of chosen word
- [ ] Save Discoveries: Remember words you've discovered for future reference

### Advanced Features

- [ ] Contextual Suggestions: Consider current document/application context
- [ ] Synonym Exploration: Show related and similar words
- [ ] Language Style Adaptation: Formal vs informal word suggestions
- [ ] Personal Dictionary: Build user's personalized word preference database

## 🌍 Phase 6: Platform Expansion

- [ ] **Linux support** (Ubuntu, Fedora, Arch)
- [ ] **macOS support** (Intel & Apple Silicon)
