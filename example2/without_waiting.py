import asyncio


async def db_query(n):
    await asyncio.sleep(n)
    return [f"Firstname Lastname{i}" for i in range(n)]


async def get_users(n):
    users = await db_query(n)
    print(users)


async def main():
    task = asyncio.create_task(get_users(2))
    await get_users(3)
    print("Three users get")
    await task
    print("Two users get")
    # await get_users(5)
    # print("Five users get")

if __name__ == '__main__':
    asyncio.run(main())
