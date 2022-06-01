import asyncio


async def hello_world_message() -> str:
    await asyncio.sleep(1)
    return "Hello world!"


async def main() -> None:
    message = await hello_world_message()
    print(message)


asyncio.run(main())
