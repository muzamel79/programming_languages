import pytest

from unit_testing.sut.factorial import factorial


@pytest.mark.parametrize('input_value, expected_factorial_value', [
    [0, 1],
    [1, 1],
    [2, 2],
    [3, 6],
    [4, 24],
    [5, 120],
])
def test_factorial(input_value: int, expected_factorial_value: int) -> None:
    output_value = factorial(input_value)

    assert output_value == expected_factorial_value
