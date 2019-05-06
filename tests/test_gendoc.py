from pathlib import Path

from pytestdocgen.gendoc import td_to_markdown, tc_to_markdown
from pytestdocgen.object import TestFile, TestDir

here = Path(__file__).parent


def test_tc_to_markdown():
    """Convert a test case to markdown string"""
    compos_file = (
        here
        / ".."
        / "test_package"
        / "tests"
        / "integration"
        / "test_composite.py"
    )
    test_root = here / ".." / "test_package" / "tests"
    tc = TestFile(compos_file, test_root).test_cases[1]
    assert tc_to_markdown(tc) is not None


def test_gendoc():
    """Convert a test directory to markdown document"""
    test_root = here / ".." / "test_package" / "tests"
    td = TestDir(test_root)
    md = td_to_markdown(td)
    assert md is not None
