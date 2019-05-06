import pytest

from mock_package import sub


def test_sub_operation_returns_addition():
    assert sub(1, 2) == 1 - 2


@pytest.mark.parametrize("test_input", [x for x in range(-2, 3)])
def test_sub_same_values_returns_zero(test_input: int):
    assert sub(test_input, test_input) == 0
