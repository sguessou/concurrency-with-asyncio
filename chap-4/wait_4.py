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
        fetchers = [
            asyncio.create_task(
                chap_4.fetch_status(session, "python://www.example.com")
            ),
            asyncio.create_task(
                chap_4.fetch_status(session, "https://www.example.com", delay=3)
            ),
            asyncio.create_task(
                chap_4.fetch_status(session, "https://www.example.com", delay=3)
            ),
        ]

        done, pending = await asyncio.wait(
            fetchers, return_when=asyncio.FIRST_EXCEPTION
        )

        print(f"Done task count: {len(done)}")
        print(f"Pending task count: {len(pending)}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error(
                    "Request got an exception", exc_info=done_task.exception()
                )

        for pending_task in pending:
            pending_task.cancel()


asyncio.run(main())
