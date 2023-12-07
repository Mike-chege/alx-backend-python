#!/usr/bin/env python3
"""
Duck-typing
"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieve the first element from a non-empty list.
    """
    if lst:
        return lst[0]
    else:
        return None
