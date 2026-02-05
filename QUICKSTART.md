# Quick Start Guide

## Installation (5 minutes)

1. **Clone and navigate:**

   ```bash
   cd c:\E\Production\Update\title-case
   ```

2. **Activate virtual environment:**

   ```bash
   .venv\Scripts\activate
   ```

   (Already set up with Python 3.12.2 and all dependencies installed!)

3. **Test it works:**
   ```bash
   python agent\title_case_agent.py examples\sample.html examples\my_output.html
   ```

## Basic Usage

### Option 1: Command Line

```bash
# Convert and save to new file
python agent\title_case_agent.py myfile.html output.html

# Convert in place (overwrites original)
python agent\title_case_agent.py myfile.html
```

### Option 2: Python Script

```python
from agent.title_case_agent import TitleCaseConverter

converter = TitleCaseConverter()

# Convert HTML string
result = converter.convert_html("<h1>hello world</h1>")
print(result)  # <h1>Hello World</h1>

# Convert file
converter.convert_html_file("input.html", "output.html")
```

### Option 3: Quick Test (Windows)

Double-click `run_test.bat` to test with the sample file.

## Important Notes

### Title Case Rules Applied

- **Capitalized**: First word, last word, all major words
- **Lowercase**: Minor words (a, an, the, and, but, or, for, in, of, to, etc.)
- **Preserved**: Acronyms (NASA, AI, HTML), mixed-case brands (GitHub, iPhone)

### Input Requirements

For proper nouns and brand names:

- ✅ Input `GitHub` → Output `GitHub` (preserved)
- ❌ Input `github` → Output `Github` (standard capitalization)

**Tip**: If you want specific capitalization for brand names, ensure they're already properly capitalized in your input HTML!

## Examples

```html
<!-- Input -->
<h1>introduction to machine learning</h1>
<h2>how to use AI in production</h2>
<h3>working with GitHub copilot</h3>

<!-- Output -->
<h1>Introduction to Machine Learning</h1>
<h2>How to Use AI in Production</h2>
<h3>Working With GitHub Copilot</h3>
```

## Testing

Run the full test suite:

```bash
pytest tests\test_title_case.py -v
```

All 18 tests should pass! ✅

## Next Steps

1. Try it on your own HTML files
2. Integrate it into your workflow
3. Customize the minor words list in `agent/title_case_agent.py` if needed
4. Read the full [README.md](README.md) for advanced usage

## Need Help?

- Check [README.md](README.md) for detailed documentation
- Look at [examples/sample.html](examples/sample.html) for input examples
- Look at [examples/output.html](examples/output.html) for expected output
- Review tests in [tests/test_title_case.py](tests/test_title_case.py)

**Happy title casing! 🎉**
