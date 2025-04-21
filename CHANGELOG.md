# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/).

## [v1.0.0] - 2025-04-21

### Fixed
- ✅ Fixed an issue where passwords were not displaying correctly when retrieving stored accounts.

### Added
- 🎉 First official stable release of the project.
- 🔐 Secure password generation feature with customizable length.
- 🧾 Functionality to add, update, retrieve, and delete accounts.
- 🗄️ Local database integration using SQLite.
- 💻 Command-line interface (CLI) via `argparse`.

### 📜 **Ajout dans le CHANGELOG.md** (si tu en maintiens un) :

## [v1.0.1] - 2025-04-21

### Added
- Initial `setup.py` for PyPI packaging.
- GitHub Actions workflow for automatic PyPI publishing.

### Fixed
- Workflow now properly triggers on new releases with packaging metadata.

### Note
This is a technical release focused on packaging; no feature changes were made.
