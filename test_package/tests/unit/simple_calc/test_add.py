import pytest

from mock_package import add


def test_addition_operation_returns_addition():
    assert add(1, 2) == 1 + 2


@pytest.mark.parametrize("test_input", [x for x in range(-2, 3)])
def test_add_same_values_with_negative_sign_returns_zero(test_input: int):
    assert add(test_input, -test_input) == 0
