from collections import OrderedDict
from os import PathLike
from pathlib import Path
from typing import List, Optional, Tuple, Union

import parso
from parso.python.tree import Function, Module, PythonNode

from pytestdocgen.gdocstring import RelaxedGoogleDocstring
from pytestdocgen.parse import (
    bfs_test_cases_in_module,
    find_all_decorators,
    find_all_test_files,
    read_with_utf8,
)


class TestFile:
    """Represents a single test file"""

    def __init__(self, path: Path, test_root: Path, prefix: str):
        """
        Args:
            path: A file's path
            test_root: The root directory of test suite
        """
        self.code = read_with_utf8(path)  # code in utf-8
        self.file = path.relative_to(path.cwd())  # file path relative to cwd
        self.root_dir = test_root  # The root directory of test suite
        self.test_cases: List[TestCase] = list()  # List of test cases
        self.parsed_tree = parso.parse(self.code)  # AST
        self.rel_dir: Tuple[str] = tuple(
            self.file.absolute().relative_to(self.root_dir).parent.parts
        )  # Relative directory

        self._prefix = prefix  # File name prefix

        # Find all test cases and add it
        for node in bfs_test_cases_in_module(self.parsed_tree):
            self.test_cases.append(TestCase(node, self, self.rel_dir))

    @property
    def file_name(self) -> str:
        """Name part of file's path"""
        return str(self.file.name)

    @property
    def page_name(self) -> str:
        """Page name part of file's path"""
        name = self.file_name
        if self.file_name.startswith(self._prefix):
            name = name[len(self._prefix) :]
        if self.file_name.endswith(".py"):
            name = name[: -len(".py")]
        return name


class TestDir:
    """Represents directory containing test or directory of tests"""

    def __init__(
        self, path: Union[Path, PathLike], test_file_prefix: str = "test_"
    ):
        """
        Args:
            path: Path to this directory
            test_file_prefix: File name convention to mark a file as a test file
        """
        self.dir_path = Path(path)  # Path to the directory
        self.test_files: List[
            TestFile
        ] = list()  # List of test files under `self`
        self._sorted_tc: Optional[
            OrderedDict
        ] = None  # Sorted test cases under `self`

        # Find all test cases under `self`
        for file in find_all_test_files(self.dir_path, test_file_prefix):
            self.test_files.append(
                TestFile(file, self.dir_path, test_file_prefix)
            )

    @property
    def test_cases(self) -> OrderedDict:
        """Decisively ordered test cases under this directory"""
        if self._sorted_tc:
            return self._sorted_tc
        rel_dirs = list({x.rel_dir for x in self.test_files})
        rel_dirs.sort(key=lambda x: "".join(x))
        self._sorted_tc = OrderedDict.fromkeys(rel_dirs)
        for tf in self.test_files:
            for tc in tf.test_cases:
                tcs = self._sorted_tc.get(tf.rel_dir)
                if not tcs:
                    tcs = list()
                tcs.append(tc)
                self._sorted_tc[tf.rel_dir] = tcs

        return self._sorted_tc


class TestCase:
    """Represents a single test case"""

    def __init__(
        self,
        node: Union[PythonNode, Function],
        test_file: TestFile,
        rel_dir: Tuple[str],
    ):
        """
        Args:
            node: AST of code block
            test_file: A TestFile containing this
            rel_dir: Relative directory from test suite root
        """
        self.python_node: Union[PythonNode, Function] = node  # AST

        self.name: str = str(node.name.value[len("test_") :]).replace(
            "_", " "
        )  # Name of the test
        self.rel_dir: Tuple[
            str
        ] = rel_dir  # Relative directories from the root of the test suite
        self.file: TestFile = test_file  # A test file contains this

        self.pos: Tuple[Tuple[int, int], Tuple[int, int]] = (
            node.start_pos,
            node.end_pos,
        )  # A specfic position where this AST block starts and ends in code

        self.raw_doc: str  # Untouched docstring block
        try:
            self.raw_doc = str(node.get_doc_node().value)
        except AttributeError:
            self.raw_doc = ""
        self.code = node.get_code()  # Untouched code block
        self._parsed_gdoc: Optional[RelaxedGoogleDocstring] = None

    @property
    def decorators(self) -> Optional[List[str]]:
        """List of decorators of this test case"""
        if isinstance(self.python_node.parent, Module):
            return None

        try:
            deco_block_node: PythonNode = self.python_node.parent
            if deco_block_node.type == "async_funcdef":
                # Async test case has one more node
                deco_block_node = deco_block_node.parent
            if deco_block_node.type != "decorated":
                return None
            return [
                str(node.get_code()).strip()
                for node in find_all_decorators(deco_block_node)
            ]
        except AttributeError:
            # Not having `parent`, `children`, either `type` is
            # expected behavior in case there's no decorator
            return None

    @property
    def parsed_doc(self) -> RelaxedGoogleDocstring:
        """Parsed and populated Docstring object"""
        if not self._parsed_gdoc:
            self._parsed_gdoc = RelaxedGoogleDocstring(self.raw_doc)

        return self._parsed_gdoc
