# example of waiting for the first tasks to completed
import asyncio
from random import random

# coroutine to execute in new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random()
    # wait for a moment
    await asyncio.sleep(value)
    # return the value
    return (f'>task {arg} done with {value}')

# main coroutine
async def main():
    # create many task to complete(task)
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for the first task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print('Done')
    # report result
    first = done.pop()
    print(first)

# start of async program
asyncio.run(main())

