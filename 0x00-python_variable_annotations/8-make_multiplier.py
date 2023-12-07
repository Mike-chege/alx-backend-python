#!/usr/bin/env python3
"""
Returns a function that multiplies a float by multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Parameters:
    - multiplier (float): The multiplier value.

    Returns:
    Callable[[float], float]: A function that multiplies a float
    By the specified multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
