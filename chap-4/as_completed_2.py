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
            chap_4.fetch_status(session, "https://www.example.com", 10),
            chap_4.fetch_status(session, "https://www.example.com", 10),
        ]

        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print("We go a timeout error!")

        for task in asyncio.tasks.all_tasks():
            print(task)


asyncio.run(main())
