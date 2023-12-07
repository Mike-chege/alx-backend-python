#!/usr/bin/env python3
"""
Returning values with the appropriate types
"""


from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in a list of strings.
    """
    return [(i, len(i)) for i in lst]
