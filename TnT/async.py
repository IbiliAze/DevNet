import requests
import json
import asyncio
from aiohttp import ClientSession
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

url = 'http://httpbin.org/'

async def count():
    for i in range(1,100):
        print(i)
        await asyncio.sleep(0.1)




async def get_delay(seconds):
    endpoint = f"/delay/{seconds}"
    print(f"delaying by {seconds} seconds")

    async with ClientSession() as session:
        async with session.get(url+endpoint) as response:
            response = await response.read()
            print(response)


async def main():
    await asyncio.gather(get_delay(5), count())

asyncio.run(main())

print("all finished")

