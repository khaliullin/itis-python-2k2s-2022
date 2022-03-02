import asyncio


# FIXME (need to run in parallel)!
import time


async def func1():
    print('1 - Before')
    await asyncio.sleep(3)
    print('1 - After')


async def func2():
    print('2 - Before')
    await asyncio.sleep(3)
    print('2 - After')


async def main():
    await asyncio.gather(func1(), func2())
    # await func1()
    # await func2()


if __name__ == '__main__':
    s = time.perf_counter()

    asyncio.run(main())

    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
