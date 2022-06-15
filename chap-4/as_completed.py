import asyncio
import importlib
import aiohttp
from aiohttp import ClientSession
from util import async_timed

chap_4 = importlib.import_module("chap-4")


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            chap_4.fetch_status(session, "https://www.example.com", 1),
            chap_4.fetch_status(session, "https://www.example.com", 1),
            chap_4.fetch_status(session, "https://www.example.com", 10),
        ]

        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)


asyncio.run(main())
