import argparse
from pathlib import Path

from cqg_test.tools import read_file_to_list, replace_and_order


def _setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="Character Replacement Tool",
        description=(
            "CLI text-replacement and sorting utility built as an SDET technical"
            "challenge."
        ),
    )
    parser.add_argument(
        "configuration",
        type=Path,
        help="Route to the configuration file e.g. 'conf.txt'",
    )

    parser.add_argument(
        "sample_text", type=Path, help="Route to the text file e.g. 'sample_text.txt'"
    )
    return parser


def _parse_args(parser: argparse.ArgumentParser) -> tuple[Path, Path]:
    args = parser.parse_args()

    if not args.configuration.is_file():
        parser.error(f"Configuration file not found: '{args.configuration}'")

    if not args.sample_text.is_file():
        parser.error(f"Sample text file not found: '{args.sample_text}'")

    return args.configuration, args.sample_text


def _print_result(result: list[str]) -> None:
    for line in result:
        print(line)


def main() -> None:
    """Execute the CLI tool.

    Reads configuration and text files from command-line arguments,
    performs replacements based on the configuration lookup table,
    and prints the modified lines sorted by replacement count.
    """
    parser = _setup_parser()
    configuration_path, sample_text_path = _parse_args(parser)

    original_text = read_file_to_list(sample_text_path)
    conf_lut = read_file_to_list(configuration_path)

    result = replace_and_order(original_text, conf_lut)
    _print_result(result)


if __name__ == "__main__":
    main()
