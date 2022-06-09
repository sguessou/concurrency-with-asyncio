import asyncio

import aiohttp
from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url, timeout=.8) as result:
        return result.status

async def main():
    session_timeout = aiohttp.ClientTimeout(total=1, connect=.8)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        url = 'https://example.com'
        await fetch_status(session, url)

asyncio.run(main())
