# example of waiting for the first task to fail
import asyncio
from random import random

# coroutine for executing in a task
async def task_coro(arg):
    value = random()
    # generate a random value between 0 and 1
    await asyncio.sleep(value)
    # block for a moment
    print(f'task {arg} slept for {value}')
    # report the value
    if value < 0.05:
        raise Exception(f'Something bad happened in {arg}')

# main entry point of the program
async def main():
    # create ten async tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for first task to fail or all tasks to complete
    done,pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    #report result
    print('Done')
    # get the first task to fail
    first = done.pop()
    print(first)

# start the asyncio program
asyncio.run(main())
