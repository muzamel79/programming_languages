#!/usr/bin/env python3

from typing import Tuple, List


def list_of_squares_divisible_by_three(max_sqr_base: int) -> int:
    return [i**2 for i in range(max_sqr_base + 1) if i**2 % 3 == 0]


def square_divisible_by_three_generator() -> Tuple[int, int]:
    i = -1
    while True:
        i += 1
        if i**2 % 3 == 0:
            yield (i, i**2)


def list_of_squares_divisible_by_three2(max_sqr_base: int) -> int:
    output_list = []
    for i, sqr in square_divisible_by_three_generator():
        if i < max_sqr_base + 1:
            output_list.append(sqr)
        else:
            return output_list


def cartesian_product(list1: List, list2: List) -> List[Tuple]:
    return [(a, b) for a in list1 for b in list2]
