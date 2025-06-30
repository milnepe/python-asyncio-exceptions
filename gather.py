import asyncio
import time

from utils import FooError, foo


async def main():
    start_t = time.monotonic()
    results = await asyncio.gather(foo(1),foo(2),return_exceptions=True)

    result1 = results[0]
    result2 = results[1]

    print(f"coro 1 finish: {time.monotonic() - start_t}")
    print(f"foo 1 result: {result1}")

    print(f"coro 2 finish: {time.monotonic() - start_t}")
    print(f"foo 2 result: {result2}")

    print(f"coros finished: {time.monotonic() - start_t}")  

# Let's do exception handling next
if __name__ == "__main__":
    asyncio.run(main())
