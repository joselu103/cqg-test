import re
from collections.abc import Iterator


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
