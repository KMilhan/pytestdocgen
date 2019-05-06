from pathlib import Path

import pytestdocgen.__main__


def test_pyproject_toml():
    """
    Test load and parsing of pyproject.toml configuration file

    """
    config = pytestdocgen.__main__.read_pyproject_toml(
        Path(__file__).parent.parent
    )
    assert config["--format"] == "markdown"
