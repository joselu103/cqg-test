import re
from dataclasses import dataclass

# Matches "key = value" entries with optional surrounding whitespace.
# Group 1 is the key and group 2 is the value.
PARSE_REGEX = r"^\s*([^\s=]+)\s*=\s*([^\s=]+)\s*$"


@dataclass(frozen=True)
class Matcher:
    """Immutable matcher built from a configuration lookup table.

    This object keeps the parsed key/value mapping together with the
    regex pattern derived from the same keys, so both values remain
    synchronized.
    """

    lut: dict[str, str]
    pattern: str

    @classmethod
    def from_conf_lut(cls, conf_lut: list[str]) -> Matcher:
        """Build a matcher from configuration lines.

        Each non-empty line is expected to follow the form "key = value".
        Valid entries are stored in a dictionary and their keys are
        combined into a single regex alternation pattern.

        Args:
            conf_lut: Configuration lines, one per item in the list.

        Returns:
            A Matcher instance containing the parsed lookup table and
            the regex pattern derived from its keys.
        """
        lut = {}
        pattern = ""

        for line in conf_lut:
            match = re.match(PARSE_REGEX, line)
            if not match:
                continue
            key = match.group(1)
            value = match.group(2)

            lut[key] = value

        pattern = "|".join(lut)

        return cls(lut=lut, pattern=pattern)
