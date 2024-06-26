# example of running a coroutine
import asyncio
#defind a coroutine
async def custom_coro():
    #await another coroutine
    await asyncio.sleep(1)

# main coroutine
async def main():
    #execute my custom coroutine
    await custom_coro()

# start the coroutine program
asyncio.run(main())

