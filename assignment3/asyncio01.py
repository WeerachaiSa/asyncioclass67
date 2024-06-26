# check the type of a coroutine
import asyncio
# definie a coroutine
async def custom_coro():
    #await another coroutine
    await asyncio.sleep(1)

# create a new coroutine
coro = custom_coro()
#check the type of the coroutine
print(type(coro))

