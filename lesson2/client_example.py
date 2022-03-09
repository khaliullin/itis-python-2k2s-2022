import asyncio

import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://python.org") as response:
            print(await response.text())
            print(response.status)
            print(response.headers['content-type'])


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
asyncio.run(main())