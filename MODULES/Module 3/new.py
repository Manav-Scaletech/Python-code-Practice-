import asyncio

# First async task
async def task1():
    print("Task 1 Started")
    # Pause for 2 seconds
    await asyncio.sleep(2)
    print("Task 1 Finished")

# Second async task
async def task2():
    print("Task 2 Started")
    # Pause for 1 second
    await asyncio.sleep(1)
    print("Task 2 Finished")

# Main coroutine
async def main():
    t1 =  asyncio.create_task(task1())
    t2 =  asyncio.create_task(task2())

    await t2
    await t1
   
# Start event loop
asyncio.run(main())



### 


name = "select * from user "

def do_work(name: str):
    users = connection.execute(f"SELECT * from users where name = ${name}")
    return users