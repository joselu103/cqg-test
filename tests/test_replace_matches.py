import pytest

from cqg_test.matcher import Matcher
from cqg_test.tools import replace_and_order, replace_matches


@pytest.fixture
def conf_lut():
    return [
        "hello=hi",
        "world=earth",
        "ab=123",
        "c=9",
        "zzz=z",
    ]


@pytest.fixture
def matcher(conf_lut):
    return Matcher.from_conf_lut(conf_lut)


@pytest.mark.parametrize(
    "original, modified, mod_count",
    [
        ("helloworld_abc_zzz", "hiearth_1239_z", 16),
        ("zzzz_ababc_test", "zz_1231239_test", 8),
        ("c_hello_c_world", "9_hi_9_earth", 12),
    ],
)
def test_replace_matches(original, modified, mod_count, matcher):
    assert replace_matches(original, matcher) == (modified, mod_count)


@pytest.mark.parametrize(
    "input_lines, expected_output",
    [
        # Standard case: lines reordered by total replacement count (16, 12, 8)
        (
            [
                "zzzz_ababc_test",  # 8 replacements
                "c_hello_c_world",  # 12 replacements
                "helloworld_abc_zzz",  # 16 replacements
            ],
            [
                "hiearth_1239_z",  # 16 replacements
                "9_hi_9_earth",  # 12 replacements
                "zz_1231239_test",  # 8 replacements
            ],
        ),
        # Lines with equal counts retain their original relative order
        (
            [
                "hello",  # 5 replacements
                "world",  # 5 replacements
            ],
            [
                "hi",  # 5 replacements (appears first)
                "earth",  # 5 replacements (appears second)
            ],
        ),
        # No matches present in any lines
        (
            ["plain_string", "another_plain_string"],
            ["plain_string", "another_plain_string"],
        ),
        # Empty input list
        (
            [],
            [],
        ),
    ],
)
def test_replace_and_order(input_lines, expected_output, conf_lut):
    assert replace_and_order(input_lines, conf_lut) == expected_output
