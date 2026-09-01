from cqg_test.tools import find_matches


def test_matches_dont_overlap():
    txt = "bbbb"
    pattern = "(bb)"

    matches = find_matches(txt, pattern)

    assert len(matches) == 2
    assert matches[0].span() == (0, 2)
    assert matches[1].span() == (2, 4)


def test_matches_all_patterns():
    txt = "rbbpiuaaiouc"
    pattern = "bb|a|c"

    matches = find_matches(txt, pattern)

    assert len(matches) == 4
    assert matches[0].span() == (1, 3) and matches[0].group() == "bb"
    assert matches[1].span() == (6, 7) and matches[1].group() == "a"
    assert matches[2].span() == (7, 8) and matches[2].group() == "a"
    assert matches[3].span() == (11, 12) and matches[3].group() == "c"


def test_matches_patterns_in_order():
    txt = "aaaaaaa"
    pattern = "(aaaa|aa|a)"

    matches = find_matches(txt, pattern)

    assert len(matches) == 3
    assert matches[0].span() == (0, 4) and matches[0].group() == "aaaa"
    assert matches[1].span() == (4, 6) and matches[1].group() == "aa"
    assert matches[2].span() == (6, 7) and matches[2].group() == "a"
