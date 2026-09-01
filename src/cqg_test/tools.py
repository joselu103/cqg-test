import re
from collections.abc import Iterator

# Matches "key = value" entries with optional surrounding whitespace.
# Group 1 is the key and group 2 is the value.
PARSE_REGEX = r"^\s*([^\s=]+)\s*=\s*([^\s=]+)\s*$"

LookupTable = dict[str, str]


def find_matches(text: str, pattern: str) -> Iterator[re.Match[str]]:
    """Find all non-overlapping regex matches in the text.

    Matches are returned in the order they are found in the text.

    Args:
        text: The original string to search.
        pattern: The regex pattern to match.

    Returns:
        An iterator of `re.Match` objects produced by `re.finditer`.
    """
    return re.finditer(pattern=pattern, string=text)


def parse_conf_lookup_table(conf_lut: list[str]) -> tuple[LookupTable, str]:
    """Parse configuration lines into a lookup table and a regex pattern.

    Each non-empty line is expected to follow the form "key = value".
    Valid entries are stored in a dictionary and their keys are combined
    into a regex alternation pattern.

    Args:
        conf_lut: Configuration lines, one per item in the list.

    Returns:
        A tuple containing:
        - the parsed key/value mapping
        - a regex pattern built from the keys
    """
    lut_dict = {}
    pattern = ""

    for line in conf_lut:
        match = re.match(PARSE_REGEX, line)
        if not match:
            continue
        key = match.group(1)
        value = match.group(2)

        lut_dict[key] = value

        if pattern:
            pattern += "|"
        pattern += key

    return lut_dict, pattern
