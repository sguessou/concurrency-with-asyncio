import asyncio
import importlib
import aiohttp
from aiohttp import ClientSession
import logging
from util import async_timed

chap_4 = importlib.import_module("chap-4")


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://www.example.com"
        pending = [
            asyncio.create_task(chap_4.fetch_status(session, url)),
            asyncio.create_task(chap_4.fetch_status(session, url, delay=2)),
            asyncio.create_task(chap_4.fetch_status(session, url, delay=3)),
        ]

        while pending:
            done, pending = await asyncio.wait(
                pending, return_when=asyncio.FIRST_COMPLETED
            )

            print(f"Done task count: {len(done)}")
            print(f"Pending task count: {len(pending)}")

            for done_task in done:
                print(await done_task)


asyncio.run(main())
