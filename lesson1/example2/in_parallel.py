import asyncio
import time


async def db_query(n):
    await asyncio.sleep(n)
    return [f"Firstname Lastname{i}" for i in range(n)]


async def get_users(n):
    users = await db_query(n)
    print(users)


async def main():
    await get_users(2)
    await get_users(3)
    # await get_users(5)
    # await asyncio.gather(
    #     get_users(2),
    #     get_users(3),
    #     get_users(5),
    # )


if __name__ == '__main__':
    asyncio.run(main())
