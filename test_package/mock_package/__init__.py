"""Mock package to be used in tests"""
from typing import Iterable


def add(a: int, b: int) -> int:
    """Returns added int"""
    return a + b


def sub(a: int, b: int) -> int:
    """Returns subtracted int"""
    return a - b


def sigma(a: Iterable[int]) -> int:
    """Returns sum of the list of int"""
    return sum(a)
