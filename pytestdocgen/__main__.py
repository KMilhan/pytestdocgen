"""
Welcome to PyTestDocGen 🎴

Usage:
  pytestdocgen [--src-dir=SRC_DIR] [--format=FORMAT] [--test-dir=TEST_DIR] [--output=FILE] [--test-prefix=PREFIX] [--header=<str>] [--footer=<str>]
  pytestdocgen (-h | --help)

Options:
  -h --help                 Show this screen.
  -s --src-dir=SRC_DIR      Working directory, usually a root of source code [default: .]
  -f --format=FORMAT        Format of the output file [default: markdown]
  -t --test-dir=TEST_DIR    Directory of tests, relative to SRC_DIR [default: tests]
  -o --output=FILE          Output file path [default: TEST_DOC.md]
  -p --test-prefix=PREFIX      Custom test file prefix [default: test_]

  --header=<str>            Custom header to provide
  --footer=<str>            Custom footer to provide
"""

import sys
from copy import copy
from pathlib import Path
from typing import Optional, Dict

import toml as toml
from docopt import docopt

from pytestdocgen.gendoc import td_to_markdown
from pytestdocgen.object import TestDir


def get_args() -> dict:
    """Parse arguments with `docopt`"""
    return docopt(__doc__)


def read_pyproject_toml(working_dir: Path) -> Dict[str, Optional[str]]:
    """
    Read project's `pyproject.toml` file

    Args:
        working_dir: CWD. Usually a root of source code

    Returns:
        Configurations described in toml file

    Raises:
        toml.TomlDecodeError: Failed to decode
        OSError: Failed to read a file

    """
    pyproject_toml_path: Path = working_dir / "pyproject.toml"
    if not pyproject_toml_path.is_file():
        return dict()

    pyproject_toml = toml.load(pyproject_toml_path)
    config_d = pyproject_toml.get("tool", {}).get("pytestdocgen", {})
    config = dict()

    for k in config_d:
        config[f"--{str(k)}"] = config_d[k]

    return config


def override_args_over_config(
        args: dict, config: dict
) -> Dict[str, Optional[str]]:
    """
    Merge two options with priority.

    If a configuration with higher priority has a `None` value on with a
    certain key, it is considered as None. But if configuration holds fallback
    value, it is preserved
    Args:
        args: Options with higher priority
        config: Options with less priority

    Returns:
        Merged conf

    """
    res = copy(config)
    # Override config file by argument
    for k in args:
        if args[k] is not None:
            res[k] = args[k]
        if args[k] is None and config.get(k) is None:
            # is explicit None
            res[k] = None

    return res


def run():
    """Run pytestdocgen"""
    arguments = get_args()
    # Read a configuration in pyproject.toml file
    config = read_pyproject_toml(Path(arguments["--src-dir"]))
    config = override_args_over_config(arguments, config)

    src_dir_path = Path(config["--src-dir"]).absolute()
    test_dir_path = (
        src_dir_path / Path(config["--test-dir"])
        if not Path(config["--test-dir"]).is_absolute()
        else Path(config["--test-dir"])
    ).absolute()
    output_file_path = (
        Path.cwd() / Path(config["--output"])
        if not Path(config["--output"]).is_absolute()
        else Path(config["--output"])
    ).absolute()

    if not test_dir_path.is_dir():
        print(
            f"Given test dir {test_dir_path} is not a directory",
            file=sys.stderr,
        )
        return -1
    td = TestDir(test_dir_path, test_file_prefix=config["--test-prefix"])

    md_str = td_to_markdown(
        td, custom_header=config["--header"], custom_footer=config["--footer"]
    )

    output_file_path.write_text(md_str)

    return 0


if __name__ == "__main__":
    """Entry point of module"""
    sys.exit(run())
