#!/usr/bin/env python3
"""
Executing async_comprehension four times
In parallel using asyncio.gather
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executing async_comprehension four times
    In parallel using asyncio.gather
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    stop = time.perf_counter()
    return stop - start
