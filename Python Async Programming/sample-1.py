import asyncio

async def counter():
    print("Start Counter....")
    for i in range(5):
        await asyncio.sleep(1.5)
        print("count = {}".format(i))
    print("Counter stopped")

async def fetch_data():
    print("Start fetching data...")
    await asyncio.sleep(5.8)
    print("Data fetched")
    return('ABC')

async def main():
    # method 1: asyncio.gather
    print("Method 1 : asyncio.gather")
    counter_return, fetch_data_return = await asyncio.gather(counter(), fetch_data())
    print("The fetched data is: {}".format(fetch_data_return))

    # method 2: asyncio.create_task
    print("Method 2 : asyncio.create_task")
    counter_task = asyncio.create_task(counter())
    fetch_data_task = asyncio.create_task(fetch_data())
    await counter_task
    await fetch_data_task
    print("The fetched data is: {}".format(fetch_data_return))
    return

asyncio.run(main())