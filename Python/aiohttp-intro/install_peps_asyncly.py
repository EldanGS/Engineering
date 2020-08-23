import aiohttp
import time
import asyncio

"""
The code is looking more complex than when we’re doing it synchronously, using 
requests. But you got this. Now that you know how to download an online resource 
using aiohttp, now you can download multiple pages asynchronously.
Let’s take the next 10-15 minutes to write the script for downloading PEPs 8010 - 8016 using aiohttp.
"""


async def download_content(pep_number: int) -> bytes:
    url = f"https://www.python.org/dev/peps/pep-{pep_number}/"
    print(f"Begin downloading {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            print(f"Finished downloading {url}")
            return content


async def write_to_file(pep_number: int, content: bytes) -> None:
    filename = f"async_{pep_number}.html"
    with open(filename, "wb") as pep_file:
        print(f"Begin writing {filename}")
        pep_file.write(content)
        print(f"Finished writing {filename}")


async def web_scrap_task(pep_number: int) -> None:
    content = await download_content(pep_number)
    await write_to_file(pep_number, content)


async def main():
    tasks = [web_scrap_task(number) for number in range(8010, 8017)]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Execution time {elapsed:0.2f} seconds.")
    # Execution time 0.33 seconds.
