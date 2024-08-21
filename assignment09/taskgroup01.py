# example of asyncio task group
import asyncio

# coroutine task
async def task1():

# report a message
    print('Hello from coroutine 1')
    # sleep to simulate waiting
    await asyncio.sleep(1)

# coroutine task
async def task2():
# report a message
    print('Hello from coroutine 2')
    # sleep to simulate waiting
    await asyncio.sleep(1)
