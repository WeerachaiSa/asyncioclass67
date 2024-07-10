# ตัวอย่างการรอให้งานทั้งหมดเสร็จ
import asyncio
import random

# coroutine
async def task_coro(arg):
    # สร้างค่าสุ่มระหว่าง 0 ถึง 1
    value = random.random()
    await asyncio.sleep(value)
    # รอสักครู่
    print(f'task {arg} done with {value}')

# ฟังก์ชันหลัก
async def main():
    # สร้างงานหลายๆ งาน
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    done, pending = await asyncio.wait(tasks)
    # รอให้งานทั้งหมดเสร็จ
    print('All done')

# เริ่มโปรแกรม asyncio
asyncio.run(main())
