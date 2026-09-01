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
python -m pip install -e .

# For running tests, install the test dependencies as well:
python -m pip install -e '.[test]'
```

## Usage

Run the CLI by passing a configuration file and a sample text file:

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
```

*Check code style and linting:*

```bash
uv run ruff check
```

*Format code and apply automatic fixes:*
```bash
uv run ruff check --fix
uv run ruff format
```

## Author

José Luis Cambil