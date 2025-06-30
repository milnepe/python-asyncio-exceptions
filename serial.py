import asyncio
import time

from utils import FooError, foo

async def main():
    start_t = time.monotonic()
    try:
        result1 = await foo(1)          # wait for the result of foo(1)
        print(f"coro 1 finish: {time.monotonic() - start_t}")
    except FooError as e:
        result1 = e

    try:
        result2 = await foo(2)          # wait for the result of foo(2)
        print(f"coro 2 finish: {time.monotonic() - start_t}")
    except FooError as e:
        result2 = e

    print(f"coros finished: {time.monotonic() - start_t}")    
    print(f"foo 1 result: {result1}")
    print(f"foo 2 result: {result2}")


if __name__ == "__main__":
    asyncio.run(main())
