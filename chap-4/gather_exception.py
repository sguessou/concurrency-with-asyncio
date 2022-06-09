import asyncio
import importlib

import aiohttp

from util import async_timed

chap_4 = importlib.import_module("chap-4")

@async_timed()
async def main():
    async with aiohttp.ClientSession as session:
        urls = ['https://example.com', 'python://example.com']
        tasks = [chap_4.fetch_status_code(session, url) for url in urls]
        status_codes = await asyncio.gather(*tasks)
        print(status_codes)

asyncio.run(main())
