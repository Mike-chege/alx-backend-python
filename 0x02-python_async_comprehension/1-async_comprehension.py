#!/usr/bin/env python3
"""
Returns 10 random numbers
"""


from typing import List
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that yields a random number between 0 and 10
    After waiting for 1 second,
    Repeated 10 times.
    """
    result = [i async for i in async_generator()]
    return result
