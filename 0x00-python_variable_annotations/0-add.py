#!/usr/bin/env python3
"""
This type-annotated function takes a float a
And a float b as arguments and returns their
Sum as a float
"""


def add(a: float, b: float) -> float:
    """
    Add two floating-point numbers and return the result.

    Parameters:
    - a (float): The first floating-point number.
    - b (float): The second floating-point number.

    Returns:
    float: The sum of the two input numbers.
    """
    result = a + b
    return result
