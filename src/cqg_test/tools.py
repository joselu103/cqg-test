import re

from cqg_test.matcher import Matcher


def find_matches(text: str, pattern: str) -> list[re.Match[str]]:
    """Find all non-overlapping regex matches in the text.

    Matches are returned in the order they are found in the text.

    Args:
        text: The original string to search.
        pattern: The regex pattern to match.

    Returns:
        An iterator of `re.Match` objects produced by `re.finditer`.
    """
    return list(re.finditer(pattern=pattern, string=text))


def replace_matches(text: str, matcher: Matcher) -> tuple[str, int]:
    """Modify the original text with the key-value pairs in the
    matcher's lut.

    Args:
        text: string to modify.
        matcher: Matcher object containing the lut and pattern necessary
            to make the replacement.

    Returns:
        A tuple containing:
        - The modified line
        - The number of characters replaced.
    """
    result_text = text
    result_cnt = 0

    matches = find_matches(text=text, pattern=matcher.pattern)

    for match in reversed(matches):
        matched_str = match.group()

        try:
            replacement_str = matcher.lut[matched_str]

        except KeyError:
            print(f"ERROR: '{matched_str}' not found in LUT:\n{matcher.lut}")
            raise

        result_text = (
            result_text[: match.start()] + replacement_str + result_text[match.end() :]
        )
        result_cnt += len(matched_str)

    return result_text, result_cnt
