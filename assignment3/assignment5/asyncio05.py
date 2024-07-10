import asyncio
import random

async def cook_dish(dish_name):
    cooking_time = random.uniform(1, 2)
    await asyncio.sleep(cooking_time)
    print(f"{dish_name} Cooking Finish ({cooking_time:.2f} seconds)")
    return dish_name, cooking_time

async def main():
    task = [asyncio.create_task(cook_dish("Fried Rice"))
    ,asyncio.create_task(cook_dish("Noodle"))
    ,asyncio.create_task(cook_dish("Curry"))
    ]
    done, pending = await asyncio.wait(task, return_when=asyncio.FIRST_COMPLETED)

    dishes = []
    for task in done:
        dish,result_time = task.result()
        dishes.append([dish,result_time])

    first_dish = min(dishes, key=lambda x: x[1])[0]
    print(f"Student A will get first dish with cooking finish: {dishes[0][0]} after {dishes[0][1]} Second")

    for dish,result_time in dishes:
        print(f'{dish} was complete in {result_time:.2f} second')
    print(f'Done, {len(done)} tasks completed in time')
    print(f'UnDone, {len(pending)} tasks')

# Start the asyncio program
asyncio.run(main())




