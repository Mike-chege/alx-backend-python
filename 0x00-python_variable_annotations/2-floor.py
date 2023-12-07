#!/usr/bin/env python3
"""
This type-annotated function floor takes
A float n as argument and returns the floor
Of the float
"""


from math import floor


def floor(n: float) -> int:
    """
    Return the floor of a floating-point number.

    Parameters:
    - n (float): The input floating-point number.

    Returns:
    int: The floor of the input number.
    """
    result = int(n)
    return result
