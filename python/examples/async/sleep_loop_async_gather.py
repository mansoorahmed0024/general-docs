import time
import asyncio

async def sleep(cnt, sec):
    print(f"Start {cnt}")
    await asyncio.sleep(sec)
    print(f"End {cnt}")

async def main():
    tasks = []
    for i in range(4):
        tasks.append(asyncio.create_task(sleep(i, 1)))

    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
end = time.time()
print(f"Elapsed {end-start}")
