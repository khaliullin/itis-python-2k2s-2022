import asyncio
import os
import time
import aiohttp

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'

symbols = [
    "IBM", "AAPL", "GOOG", "TSLA", "MSFT", "SPCE", "GE", "A", "META", "UBER",
    "IBM", "AAPL", "GOOG", "TSLA", "MSFT", "SPCE", "GE", "A", "META", "UBER",
    "IBM", "AAPL", "GOOG", "TSLA", "MSFT", "SPCE", "GE", "A", "META", "UBER",
    "IBM", "AAPL", "GOOG", "TSLA", "MSFT", "SPCE", "GE", "A", "META", "UBER",
    "IBM", "AAPL", "GOOG", "TSLA", "MSFT", "SPCE", "GE", "A", "META", "UBER",
]
results = []


async def get_tasks(session):
    tasks = []
    for symbol in symbols:
        tasks.append(
            session.get(url.format(symbol, API_KEY))
        )
    return tasks


async def run_tasks():
    session = aiohttp.ClientSession()
    tasks = await get_tasks(session)
    responses = await asyncio.gather(*tasks)
    for response in responses:
        results.append(await response.json())
    await session.close()


start = time.time()
asyncio.run(run_tasks())
end = time.time()
print(f"It took {end - start}")
