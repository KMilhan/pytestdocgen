from pathlib import Path

from pytestdocgen.object import TestDir, TestFile
from pytestdocgen.parse import find_all_test_files

here = Path(__file__).parent


def test_file_model():
    """Test if file model is created"""
    compos_file = (
        here
        / ".."
        / "test_package"
        / "tests"
        / "integration"
        / "test_composite.py"
    )

    test_root = here / ".." / "test_package" / "tests"

    assert TestFile(compos_file, test_root) is not None
    assert (
        TestFile(compos_file, test_root).test_cases[2].decorators[0]
        == "@pytest.mark.asyncio"
    )
    assert len(TestFile(compos_file, test_root).test_cases[3].decorators) == 2


def test_dir_model():
    """Test if directory model is created"""
    test_root = here / ".." / "test_package" / "tests"
    td = TestDir(test_root)
    assert td is not None
    assert td.test_cases is not None


def test_find_all_files():
    """Test if all test files with a given pattern are found"""
    test_root = here / ".." / "test_package" / "tests"
    assert len([x for x in find_all_test_files(test_root)]) == 4
