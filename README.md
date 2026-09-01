# cqg-test

CLI text-replacement and sorting utility built as an SDET technical challenge.

## Overview

This project implements a small command-line tool that:

- reads a configuration lookup table from a file
- parses key/value entries such as `key = value`
- replaces matching tokens in a sample text
- orders the output lines by the number of replacements performed

The implementation is structured around a matcher abstraction and a set of text-processing utilities.

## Project structure

- `src/cqg_test/main.py` — CLI entry point
- `src/cqg_test/matcher.py` — parsing logic and matcher object
- `src/cqg_test/tools.py` — regex matching and replacement helpers
- `tests/` — automated tests

## Requirements

- Python 3.14+
- `uv` (recommended) or `pip`

## Installation

With `uv`:

```bash
git clone https://github.com/joselu103/cqg-test
cd cqg-test
uv sync

# For running tests, install the test dependencies as well:
uv sync --extra test
```

With `pip`:

```bash
git clone https://github.com/joselu103/cqg-test
cd cqg-test

# Create and activate the virtual environment
python3 -m venv venv
source venv/bin/activate  # In Windows (Git Bash / CMD): venv\Scripts\activate

# Install the package
python -m pip install -e .

# For running tests, install the test dependencies as well:
python -m pip install -e '.[test]'
```

## Usage

# Direct command (if virtual environment is active or installed with pip)
```bash
cqg-test path/to/conf.txt path/to/sample_text.txt
```

Or using uv
```bash
uv run cqg-test path/to/conf.txt path/to/sample_text.txt
```

### Example

Given a `conf.txt`:
```text
FOO = bar
BAZ = qux
```

And a `sample_text.txt`:
```text
No matches here
One match: FOO
Two matches: FOO and BAZ
```

Command:
```bash
uv run cqg-test tests/fixtures/conf.txt tests/fixtures/sample_text.txt

# or without uv:
cqg-test tests/fixtures/conf.txt tests/fixtures/sample_text.txt
```

Output (sorted by replacement count):
```text
Two matches: bar and qux
One match: bar
No matches here
```

## Running Tests & Quality Checks

Run the test suite with coverage:

```bash
uv run pytest

# or without uv:
pytest
```

*Check code style and linting:*

```bash
uv run ruff check

# or without uv:
ruff check
```

*Format code and apply automatic fixes:*
```bash
uv run ruff check --fix
uv run ruff format

# or without uv:
ruff check --fix
ruff format
```

## Author

José Luis Cambil