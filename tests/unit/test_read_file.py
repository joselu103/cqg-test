import pytest

from cqg_test.tools import read_file_to_list


@pytest.mark.parametrize(
    "file_name, expected_result",
    [
        ("conf.txt", ["a=z", "bb=y", "c=x"]),
        (
            "sample_text.txt",
            [
                "jgrebbk6hnae",
                "cnhjrfyjvth3nxr",
                "b#sjcf_ansbbbbbvo!",
                "dajf#aemfaocfna%",
            ],
        ),
        (
            "expected_result.txt",
            ["b#sjxf_znsyybvo!", "dzjf#zemfzoxfnz%", "jgreyk6hnze", "xnhjrfyjvth3nxr"],
        ),
    ],
)
def test_read_file_to_list(file_name, expected_result, fixtures_dir):
    assert read_file_to_list(fixtures_dir / file_name) == expected_result
