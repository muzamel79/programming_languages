import pytest
from typing import List, Tuple

from list_comprehensions_and_generators.list_comprehensions_and_generators import list_of_squares_divisible_by_three
from list_comprehensions_and_generators.list_comprehensions_and_generators import list_of_squares_divisible_by_three2
from list_comprehensions_and_generators.list_comprehensions_and_generators import cartesian_product


@pytest.mark.parametrize('input_value, expected_list', [
    [0, [0]],
    [1, [0]],
    [2, [0]],
    [3, [0, 9]],
    [4, [0, 9]],
    [5, [0, 9]],
    [6, [0, 9, 36]],
])
def test_squares_divisible_by_three(input_value: int, expected_list: int) -> None:
    output_list = list_of_squares_divisible_by_three(input_value)
    assert output_list == expected_list
    output_list = list_of_squares_divisible_by_three2(input_value)
    assert output_list == expected_list


@pytest.mark.parametrize('input_list1, input_list2, expected_cartesian_product', [
    [['a', 'b'], [1, 2], [('a', 1), ('a', 2), ('b', 1), ('b', 2)]],
    [[], ['a', 'b'], []],
    [[1, 2], [], []],
    [['apple', 'peach'], [1], [('apple', 1), ('peach', 1)]]
])
def test_cartesian_product(input_list1: List, input_list2: List, expected_cartesian_product: List[Tuple]) -> None:
    output_list = cartesian_product(input_list1, input_list2)
    assert output_list == expected_cartesian_product
