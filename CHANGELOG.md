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

## [v1.0.1] - 2025-04-21

### Added
- Initial `setup.py` for PyPI packaging.
- GitHub Actions workflow for automatic PyPI publishing.

### Fixed
- Workflow now properly triggers on new releases with packaging metadata.

### Note
This is a technical release focused on packaging; no feature changes were made.

Got it! Here’s your **changelog entry in English** for version `v1.1.0`:

## [v1.1.0] – 2025-04-22

### Major Changes
- **Repository renamed** from `password-manager-python` → `psmgr`
- **Main file renamed**: `main.py` → `psmgr.py` → `psmgr/cli.py`
- **Project structure reorganized** into a Python package layout:
  - Moved code into a `psmgr/` package directory
  - Ensured all internal imports use relative or absolute paths properly
- **Executable module**: Now runs as `python -m psmgr` from any location

### Cleanups & Adjustments
- All references to the old name (`password-manager-python`) updated across:
  - Codebase
  - `README.md`
  - `setup.py`
  - GitHub Actions workflows
- Updated argument parsing logic to support `--version / -v` flag for version display

### Ready for Trusted Publishing
- Workflow updated for **PyPI Trusted Publishing**
- New package name reserved: `psmgr`
