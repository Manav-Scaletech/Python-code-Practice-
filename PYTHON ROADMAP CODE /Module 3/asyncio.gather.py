import asyncio

async def task1():
    print("Task 1 Started")
    await asyncio.sleep(3)
    print("Task 1 Finished")
    return "Result 1"

async def task2():
    print("Task 2 Started")
    await asyncio.sleep(2)
    print("Task 2 Finished")
    return "Result 2"

async def main():
    results = await asyncio.gather(
        task2(),
        task1()
    )

    print(results)

asyncio.run(main())