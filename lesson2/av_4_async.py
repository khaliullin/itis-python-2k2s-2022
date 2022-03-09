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


async def get_symbols():
    async with aiohttp.ClientSession() as session:
        for symbol in symbols:
            response = await asyncio.create_task(
                session.get(url.format(symbol, API_KEY))
            )
            results.append(await response.json())


start = time.time()
asyncio.run(get_symbols())
end = time.time()
print(f"It took {end - start}")
