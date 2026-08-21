import asyncio

async def main():
    await asyncio.sleep(10)
    print("Hello")
    await asyncio.sleep(5)
    print("World")

asyncio.run(main())