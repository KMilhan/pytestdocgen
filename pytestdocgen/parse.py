from collections import deque
from os import PathLike
from pathlib import Path
from typing import Iterable, Union

import cchardet
from parso.python.tree import Module, PythonNode


def read_with_utf8(path: Union[PathLike, Path]) -> str:
    """Read and decode source code file with utf"""
    with open(path, "rb") as src_file:
        content = src_file.read()
        guess = cchardet.detect(content)
        code = content.decode(guess["encoding"])
        return code


def bfs_test_cases_in_module(module: Module) -> Iterable[PythonNode]:
    """
    Visit all AST in BFS fashion and find TCs
    Args:
        module: AST node, `Module`

    Yields:
        AST with a single test case under it, within 1 depth

    """
    to_visit = deque(module.children)

    while to_visit:
        node: PythonNode = to_visit.popleft()
        try:
            if (node.type == "funcdef" or node.type == "async_funcdef") and str(
                node.name.value
            ).startswith("test_"):
                # Is test case
                yield node
        except AttributeError:
            # node has no name, which is fine
            pass

        try:
            for child in node.children:
                to_visit.append(child)
        except AttributeError:
            # Node has no child, which is fine
            pass


def find_all_decorators(node: PythonNode) -> Iterable[PythonNode]:
    """
    Find all decorators a node has
    Args:
        node: AST representing function or coroutine

    Yields:
        AST of decorator

    """
    to_visit = deque(node.children)

    while to_visit:
        node: PythonNode = to_visit.popleft()
        try:
            if node.type == "decorator":
                yield node
            for child in node.children:
                if child.type == "decorator" or child.type == "decorators":
                    to_visit.append(child)
        except AttributeError:
            pass


def find_all_test_files(test_dir: Path, prefix: str = "test_"):
    """
    Find all test files
    Args:
        test_dir: A root of test suite
        prefix: Naming convention for the testing file

    Yields:
        Test file

    """
    yield from test_dir.glob(f"**/{prefix}*.py")
