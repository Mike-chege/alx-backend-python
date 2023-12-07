#!/usr/bin/env python3
"""
This type-annotated function concat that takes
A string str1 and a string str2 as arguments
And returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings and return the result.

    Parameters:
    - str1 (str): The first string.
    - str2 (str): The second string.

    Returns:
    str: The concatenated string of str1 and str2.
    """
    result = str1 + str2
    return result
