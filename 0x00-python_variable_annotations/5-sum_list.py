#!/usr/bin/env python3
"""
This type-annotated function sum_list takes
A list input_list of floats as argument and
Returns their sum as a float
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Parameters:
    - input_list (List[float]): The input list of floating-point numbers.

    Returns:
    float: The sum of the numbers in the input list.
    """
    result = sum(input_list)
    return result
