#!/usr/bin/env python3
"""
A coroutine called async_generator
That takes no arguments
"""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous coroutine that yields a random number between 0 and 10
    After waiting for 1 second,
    repeated 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
