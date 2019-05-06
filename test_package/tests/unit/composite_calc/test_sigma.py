from mock_package import sigma


def test_sum_of_zero_is_zero():
    assert sigma([0 for _ in range(1024)]) == 0


def test_sigma_same_values_with_opposite_sign_returns_zero():
    assert sigma([x for x in range(-2, 3)]) == 0
