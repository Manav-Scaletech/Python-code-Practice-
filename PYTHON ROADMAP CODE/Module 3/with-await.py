import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(7)
    print("World")
    print("another")
    

asyncio.run(hello())
    