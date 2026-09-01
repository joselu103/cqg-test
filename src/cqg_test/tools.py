import re
from pathlib import Path

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


def replace_and_order(original_text: list[str], conf_lut: list[str]) -> list[str]:
    """Modify the original text with the key-value pairs in conf_lut and
    orders it by total number of symbols replaced.

    Args:
        original_text: list of strings to modify.
        conf_lut: list of strings with the characters to replace and
            their replacements.

    Returns:
        The lines after modification, ordered by total number of symbols
        replaced.
    """
    mod_lines_with_cnt: list[tuple[str, int]] = []
    matcher = Matcher.from_conf_lut(conf_lut)

    for line in original_text:
        mod_lines_with_cnt.append(replace_matches(text=line, matcher=matcher))

    mod_lines_with_cnt.sort(key=lambda line_with_cnt: line_with_cnt[1], reverse=True)

    return [line[0] for line in mod_lines_with_cnt]


def read_file_to_list(file: Path) -> list[str]:
    """Read a file and divide it in lines.

    Args:
        file: file path

    Returns:
        A list containing each line in order.
    """
    return file.read_text("utf-8").splitlines()
