# Title Case Agent for GitHub Copilot

A custom GitHub Copilot agent that converts HTML heading elements (title, h1-h5) to proper title case while preserving attributes and sub-elements.

## Features

- ✅ Converts text in `<title>`, `<h1>`, `<h2>`, `<h3>`, `<h4>`, and `<h5>` elements to title case
- ✅ Preserves HTML attributes (classes, IDs, styles, etc.)
- ✅ Preserves nested sub-elements within headings
- ✅ Follows standard title case rules (capitalizes major words, lowercases minor words like "the", "and", "of")
- ✅ Handles special cases like acronyms and hyphenated words
- ✅ Works with any HTML file

## Title Case Rules

Title case follows these conventions:

- **Always capitalize**: First word, last word, and all major words
- **Lowercase**: Minor words like articles (a, an, the), short prepositions (of, to, in, for), and conjunctions (and, but, or)
- **Preserve**: Acronyms (NASA, AI, HTML) remain in uppercase
- **Hyphenated words**: Each part is typically capitalized

### Examples

**Input:**

```html
<h1>welcome to github copilot</h1>
<h1>how to build a custom agent</h1>
<h1>introduction to machine learning</h1>
```

**Output:**

```html
<h1>Welcome to GitHub Copilot</h1>
<h1>How to Build a Custom Agent</h1>
<h1>Introduction to Machine Learning</h1>
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/arulkkumar1/title-case.git
   cd title-case
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line

Convert an HTML file and save to a new file:

```bash
python agent/title_case_agent.py input.html output.html
```

Convert an HTML file in place (overwrites original):

```bash
python agent/title_case_agent.py input.html
```

### Python API

```python
from agent.title_case_agent import TitleCaseConverter

# Create converter instance
converter = TitleCaseConverter()

# Convert HTML string
html_input = "<h1>welcome to github copilot</h1>"
html_output = converter.convert_html(html_input)
print(html_output)  # <h1>Welcome to GitHub Copilot</h1>

# Convert HTML file
converter.convert_html_file("input.html", "output.html")

# Convert just text to title case
text = converter.to_title_case("introduction to machine learning")
print(text)  # Introduction to Machine Learning
```

## Testing

Run the test suite:

```bash
pytest tests/test_title_case.py -v
```

Run tests with coverage:

```bash
pytest tests/test_title_case.py --cov=agent --cov-report=html
```

## Project Structure

```
title-case/
├── agent/
│   └── title_case_agent.py      # Main agent implementation
├── tests/
│   └── test_title_case.py       # Unit tests
├── examples/
│   ├── sample.html              # Example input HTML
│   └── expected_output.html     # Expected output
├── .github/
│   └── copilot/
│       └── agent.json           # GitHub Copilot agent configuration
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## How It Works

1. **HTML Parsing**: Uses BeautifulSoup to parse HTML while preserving structure
2. **Element Identification**: Finds all `<title>`, `<h1>`, `<h2>`, `<h3>`, `<h4>`, and `<h5>` elements
3. **Text Conversion**: Applies title case rules to text content
4. **Preservation**: Maintains all HTML attributes and nested elements
5. **Output**: Returns properly formatted HTML

## GitHub Copilot Integration

This agent is configured to work with GitHub Copilot. The configuration is in `.github/copilot/agent.json`.

### Agent Configuration

- **Supported file types**: HTML, HTM
- **Command**: `convert-to-title-case`
- **Runtime**: Python 3.8+

## Examples

### Example 1: Simple Heading

```html
<!-- Input -->
<h1>welcome to github copilot</h1>

<!-- Output -->
<h1>Welcome to GitHub Copilot</h1>
```

### Example 2: Heading with Attributes

```html
<!-- Input -->
<h1 class="title" id="main">how to build a custom agent</h1>

<!-- Output -->
<h1 class="title" id="main">How to Build a Custom Agent</h1>
```

### Example 3: Heading with Nested Elements

```html
<!-- Input -->
<h2>Welcome to <span class="highlight">github</span> copilot</h2>

<!-- Output -->
<h2>Welcome to <span class="highlight">GitHub</span> Copilot</h2>
```

### Example 4: Multiple Heading Levels

```html
<!-- Input -->
<h1>introduction to machine learning</h1>
<h2>what is machine learning?</h2>
<h3>types of machine learning</h3>

<!-- Output -->
<h1>Introduction to Machine Learning</h1>
<h2>What Is Machine Learning?</h2>
<h3>Types of Machine Learning</h3>
```

## Testing the Agent

Try the agent with the sample file:

```bash
# Copy sample to test
cp examples/sample.html examples/test.html

# Run the agent
python agent/title_case_agent.py examples/test.html

# View the result
cat examples/test.html
```

Compare with the expected output:

```bash
diff examples/test.html examples/expected_output.html
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this project for any purpose.

## Author

Created by arulkkumar1

## Troubleshooting

### ImportError: No module named 'bs4'

Run `pip install -r requirements.txt` to install dependencies.

### HTML structure changed unexpectedly

BeautifulSoup may reformat HTML. Use the `lxml` parser for better preservation: `BeautifulSoup(html, 'lxml')`

### Title case not applied correctly

Check that your HTML elements are properly closed and formatted. The agent only processes `<title>`, `<h1>`, `<h2>`, `<h3>`, `<h4>`, and `<h5>` tags.

## Future Enhancements

- [ ] Add support for custom title case rules
- [ ] Add option to exclude certain elements
- [ ] Add batch processing for multiple files
- [ ] Add GUI interface
- [ ] Add VS Code extension integration

---

**Happy coding with GitHub Copilot! 🚀**
