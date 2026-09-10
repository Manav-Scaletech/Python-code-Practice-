import asyncio

async def worker(id):

    print(f"Worker {id} Start")
    await asyncio.sleep(2)
    print(f"Worker {id} End")

async def helo():
    tasks = []
    for i in range(5):
        tasks.append(
            asyncio.create_task(worker(i))
        )
    await asyncio.gather(*tasks)

async def hello():
    await asyncio.sleep(2)
    return "Done"

async def main():
    task = asyncio.create_task(hello())
    print(task.done())
    await task
    print(task.done())

asyncio.run(main())