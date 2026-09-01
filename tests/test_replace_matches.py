import pytest

from cqg_test.matcher import Matcher
from cqg_test.tools import replace_matches


@pytest.fixture
def matcher():
    conf_lut = [
        "hello=hi",
        "world=earth",
        "ab=123",
        "c=9",
        "zzz=z",
    ]
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
