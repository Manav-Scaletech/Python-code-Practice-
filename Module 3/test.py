async def task():
    a = 10
    b = 20

    await asyncio.sleep(5)

    c = a + b

    print(c)
    
task()