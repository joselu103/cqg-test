from cqg_test.tools import parse_conf_lookup_table


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

    lut_dict, pattern = parse_conf_lookup_table(conf_lut)

    assert lut_dict == {
        "a": "b",
        "3": "c",
        "aaa": "bbb",
        "#@3": "!()",
    }
    assert pattern == "a|3|aaa|#@3"
