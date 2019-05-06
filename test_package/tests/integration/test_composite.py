import pytest

from mock_package import add, sub, sigma


def test_addition_and_subtraction_is_the_opposite():
    """
    Test if addition and subtraction are the opposite operation

    Long description following the summary explaining the various stuffs

    Precondition:
        All inputs are integers
    """
    assert sub(add(1, 2), 2) == 1


@pytest.mark.parametrize("test_input", [x for x in range(-2, 3)])
def test_add_is_part_of_sigma(test_input: int):
    """
    Test if addition is a part of summation

    Steps:
        * Add 0 in each iteration
        * Finish the iteration
        * Check if summation is zero

    Precondition:
        All inputs are integers

    Input:
        Any Integer

    Expected Output:
        Summation

    Note:
        This test is not enough to test summation

    Return:
        None as this is a test
    """
    add_res = 0
    for x in range(test_input):
        add_res += 1
    assert add_res == sigma([1 for _ in range(test_input)])


@pytest.mark.asyncio
async def test_asyncio_coro(x):
    """Async coro"""

    assert bool(x)


@pytest.mark.asyncio
@pytest.mark.parametrize("x", [x for x in range(1, 3)])
async def test_asyncio_coro_para(x):
    assert bool(x)
