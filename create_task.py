"""
Example of 2 tasks executing consecutively
The tasks are independant and if one fails the other task is unaffected
"""

import asyncio
import time

from utils import FooError, foo


async def main():
    start_t = time.monotonic()
    task_1 = asyncio.create_task(foo(1))  # task 1 starts running
    task_2 = asyncio.create_task(foo(2))  # task 2 starts running

    try:
        # will fail
        result1 = await task_1  # wait for task_1 to finish
    except FooError as exc:
        result1 = exc
    finally:
        # will print even on failure
        print(f"task 1 finish: {time.monotonic() - start_t}")
        print(f"foo 1 result: {result1}")

    try:
        # doesn't get cancelled if task 1 fails
        result2 = await task_2  # wait for task_2 to finish
    except FooError as exc:
        result2 = exc
    finally:
        print(f"task 2 finish: {time.monotonic() - start_t}")
        print(f"foo 2 result: {result2}")

    print(f"tasks finished: {time.monotonic() - start_t}")


if __name__ == "__main__":
    asyncio.run(main())
