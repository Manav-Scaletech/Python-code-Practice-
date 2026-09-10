import asyncio

async def hello():
    print("Hello")
    
    print("World")
    print("another")
    
result = hello()
print(result)


#without await, the function is not executed, it just returns a coroutine object.
#  To execute the function, you need to use await or run it in an event loop.