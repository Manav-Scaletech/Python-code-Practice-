import asyncio
import time

# 1. This is the COROUTINE function
async def brew_coffee():
    print("  Coffee: Starting to brew...")
    await asyncio.sleep(2)  # Pauses here to simulate brewing
    print("  Coffee: Done brewing!")
    return "Warm Espresso"

async def main():
    start_time = time.time()
    
    # 2. Creating a TASK schedules the coroutine to run instantly in the background
    coffee_task = asyncio.create_task(brew_coffee())
    
    # 3. The main program keeps moving and does other work concurrently
    print("Main: Doing the morning dishes while coffee brews...")
    await asyncio.sleep(1) 
    print("Main: Finished the dishes!")
    
    # 4. Now we wait ("await") for the background task to give us its final result
    coffee_result = await coffee_task
    print(output := f"Main: Drinking my {coffee_result}!")
    
    print(f"Total time taken: {round(time.time() - start_time)} seconds")

# Run the event loop
asyncio.run(main())
import asyncio
import time

# 1. This is the COROUTINE function
async def brew_coffee():
    print("  Coffee: Starting to brew...")
    await asyncio.sleep(2)  # Pauses here to simulate brewing
    print("  Coffee: Done brewing!")
    return "Warm Espresso"

async def main():
    start_time = time.time()
    
    # 2. Creating a TASK schedules the coroutine to run instantly in the background
    coffee_task = asyncio.create_task(brew_coffee())
    
    # 3. The main program keeps moving and does other work concurrently
    print("Main: Doing the morning dishes while coffee brews...")
    await asyncio.sleep(1) 
    print("Main: Finished the dishes!")
    
    # 4. Now we wait ("await") for the background task to give us its final result
    coffee_result = await coffee_task
    print(output := f"Main: Drinking my {coffee_result}!")
    
    print(f"Total time taken: {round(time.time() - start_time)} seconds")

# Run the event loop
asyncio.run(main())
