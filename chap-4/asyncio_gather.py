import asyncio
import importlib

import aiohttp

chap_4 = importlib.import_module("chap-4")
from aiohttp import ClientSession

from util import async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ["https://example.com" for _ in range (1000)]
        requests = [chap_4.fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)

asyncio.run(main())
