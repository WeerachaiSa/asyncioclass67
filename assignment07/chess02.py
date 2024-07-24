import asyncio
import time

judit_compute_time = 0.1  # seconds
opponent_compute_time = 0.5 # seconds
move_pairs = 30
opponents = 24

async def game(x):
    start_board_time = asyncio.get_event_loop().time()
    for i in range(move_pairs):
        time.sleep(judit_compute_time)
        print(f"Board {x+1} {i+1} Judit made a move")
        print("Opponent Turn")
        await asyncio.sleep(opponent_compute_time)
        print(f"Board {x+1} {i+1} Opponent made a move")
    print(f'Board-{x+1}- >>>>>>>>>>> Finished - in {round(asyncio.get_event_loop().time() - start_board_time)} secs\n')
    return round(asyncio.get_event_loop().time() - start_board_time)

async def main():
    start_time = asyncio.get_event_loop().time()
    tasks = [game(board) for board in range(opponents)]
    total_time = await asyncio.gather(*tasks)
    print(f'Board exhibition finished in {sum(total_time)} secs.')
    print(f'Total time: {round(time.perf_counter() - start_time)} secs')

if __name__ == "__main__":
    asyncio.run(main())
