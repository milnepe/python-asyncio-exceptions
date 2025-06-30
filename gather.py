"""
Example using gather where both coros run conurrently but must finish
before reurning to main.

If one coro fails then all the other coros in the gather are cancelled.

By adding return_exceptions=True the other coros can continue
"""

import asyncio
import time

from utils import foo
# from utils import FooError


async def main():
    start_t = time.monotonic()

    # result1 = None
    # result2 = None
    # try:
    # adding return_exceptions=True passes the exception in result
    # and stops foo2 from being cancelled
    results = await asyncio.gather(foo(1), foo(2), return_exceptions=True)

    # without the return_exceptions=True even if we wrap the gather in try, except
    # foo2 is still cancelled
    # It may be that we want all the other tasks in the gather to cancel if one fails

    # results = await asyncio.gather(foo(1),foo(2))

    result1 = results[0]
    result2 = results[1]
    # except FooError as exc:
    #     print(f"Exception: {exc}")

    print(f"coro 1 finish: {time.monotonic() - start_t}")
    print(f"foo 1 result: {result1}")

    print(f"coro 2 finish: {time.monotonic() - start_t}")
    print(f"foo 2 result: {result2}")

    print(f"coros finished: {time.monotonic() - start_t}")


# Let's do exception handling next
if __name__ == "__main__":
    asyncio.run(main())
