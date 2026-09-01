from cqg_test.main import main


def test_cli(fixtures_dir, monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.argv",
        [
            "cqg-test",
            str(fixtures_dir / "conf.txt"),
            str(fixtures_dir / "sample_text.txt"),
        ],
    )

    main()

    output = capsys.readouterr()
    assert (
        output.out.splitlines()
        == (fixtures_dir / "expected_result.txt").read_text().splitlines()
    )
