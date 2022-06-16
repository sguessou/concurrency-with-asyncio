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
            asyncio.create_task(
                chap_4.fetch_status(session, "https://www.example.com")
            ),
            asyncio.create_task(
                chap_4.fetch_status(session, "https://www.example.com")
            ),
        ]

        done, pending = await asyncio.wait(fetchers)
        print(f"Done task count: {len(done)}")
        print(f"Pending task count: {len(pending)}")

        for done_task in done:
            result = await done_task
            print(result)


asyncio.run(main())
