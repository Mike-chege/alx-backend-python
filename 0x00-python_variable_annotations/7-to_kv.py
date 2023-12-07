#!/usr/bin/env python3
"""
Returning a tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the string k and the square of the int/float v.

    Parameters:
    - k (str): The input string.
    - v (Union[int, float]): The input integer or float.

    Returns:
    Tuple[str, float]: A tuple containing the string k and the square of v as a float.
    """
    result = (k, float(v ** 2))
    return result
