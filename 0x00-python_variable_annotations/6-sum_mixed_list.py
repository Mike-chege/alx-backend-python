#!/usr/bin/env python3
"""
This type-annotated function sum_mixed_list
Takes a list mxd_lst of integers and floats
And returns their sum as a float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats.

    Parameters:
    - mxd_lst (List[Union[int, float]]): The input list of integers and floats.

    Returns:
    float: The sum of the numbers in the input list.
    """
    result = sum(mxd_lst)
    return float(result)
