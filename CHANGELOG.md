# Changelog

All notable changes to the Title Case Agent will be documented in this file.

## [1.0.0] - 2026-02-05

### Added

- Initial release of Title Case Agent for GitHub Copilot
- Core title case conversion functionality
- Support for HTML elements: title, h1, h2, h3, h4, h5
- Preservation of HTML attributes and nested elements
- Standard title case rules implementation
- Support for acronyms (AI, NASA, HTML, etc.)
- Support for mixed-case proper nouns (GitHub, iPhone, etc.)
- Support for hyphenated words
- Command-line interface
- Python API
- Comprehensive test suite (18 tests)
- Example HTML files
- Documentation and guides
- GitHub Copilot agent configuration
- Windows batch script for quick testing

### Features

- ✅ Converts heading text to proper title case
- ✅ Preserves all HTML attributes
- ✅ Maintains nested elements within headings
- ✅ Handles special cases (acronyms, proper nouns, hyphens)
- ✅ Works with any valid HTML file

### Technical Details

- Python 3.8+ support
- Dependencies: beautifulsoup4, lxml, pytest
- Platform: Cross-platform (tested on Windows 11)
- License: MIT
