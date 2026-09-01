from cqg_test.matcher import Matcher


def test_parse_lookup_table():
    conf_lut = [
        "a = b",
        " 3 =c",
        "aaa = bbb",
        "#@3 = !()",
        "a=sd = fasd",
        "5==4",
        "aa a = b",
        "= d",
        "5 = a = c",
    ]

    matcher = Matcher.from_conf_lut(conf_lut)

    assert type(matcher) == Matcher
    assert matcher.lut == {
        "a": "b",
        "3": "c",
        "aaa": "bbb",
        "#@3": "!()",
    }
    assert matcher.pattern == "a|3|aaa|#@3"
