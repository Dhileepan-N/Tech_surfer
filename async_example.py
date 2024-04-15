import asyncio
import time
async def workout():
    print('Working out')
    await asyncio.sleep(5)
    print('Workout Complete')
    return "Work Done"
async def sleep():
    print('Sleeping')
    await asyncio.sleep(4)
    print('Awake')
    return "slept"
async def main():
    start_time = time.time()
    # batch = asyncio.gather(workout(),sleep())
    # print(type(batch))
    # result_workout, result_sleep = await batch
    workout_task = asyncio.create_task(workout())
    sleep_task = asyncio.create_task(sleep())
    result_workout = await workout_task
    result_sleep = await  sleep_task
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(result_workout)
    print(result_sleep)
    print(elapsed_time)
if __name__ == '__main__':
    asyncio.run(main())
