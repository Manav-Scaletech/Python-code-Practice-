import asyncio

async def hello():
    print("Start first one ")
    await asyncio.sleep(2)
    print("End of the one ")

async def helo():
    print("Start second one ")
    await asyncio.sleep(3)
    print("End of the second ")

async def main():
    print("Main Running 1")
    
    task1 = asyncio.create_task(helo())
    await asyncio.sleep(4)
    task = asyncio.create_task(hello())
    await asyncio.sleep(4)

    # await task
    await task
    await task1
    
    print("Main Running 2")
    print("Main Running 3")

asyncio.run(main())