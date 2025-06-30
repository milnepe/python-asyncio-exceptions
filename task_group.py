import asyncio
import time

from utils import FooError, foo

async def main():
    
    try:
        start_t = time.monotonic()
        async with asyncio.TaskGroup() as tg:
            task_1 = tg.create_task(foo(1))    # task 1 starts running
            task_2 = tg.create_task(foo(2))    # task 2 starts running
        # context waits for all tasks to finish - no need to await them!
    except* FooError as eg:
        for e in eg.exceptions:
            print(e)
    else:
        print(f"task 1 finish: {time.monotonic() - start_t}")
        print(f"foo 1 result: {task_1.result()}")
        print(f"task 2 finish: {time.monotonic() - start_t}")
        print(f"foo 2 result: {task_2.result()}")

        print(f"tasks finished: {time.monotonic() - start_t}")

if __name__ == "__main__":
    asyncio.run(main())
