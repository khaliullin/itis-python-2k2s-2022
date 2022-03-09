import os
import time

import requests

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


def run_tasks():
    for symbol in symbols:
        response = requests.get(url.format(symbol, API_KEY))
        results.append(response.json())


start = time.time()
run_tasks()
end = time.time()
print(f"It took {end - start}")
