import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(7)
    print("World")
    print("another")
    
async def helo():
    print("here new function ")
    await asyncio.sleep(2)
    print("World end here ")
    
async def func():
    task1 = asyncio.create_task(hello())
        
    # 2. Create a background task for the helo function
    task2 = asyncio.create_task(helo())
    
    # 3. Wait for BOTH tasks to finish before closing the program
    await task1
    await task2
    
asyncio.run(func())

