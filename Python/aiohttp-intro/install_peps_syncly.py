"""
https://us-pycon-2019-tutorial.readthedocs.io/aiohttp_intro.html
In the previous section, we’ve got a taste of what asynchronous task execution
looks like using asyncio library.
"""
import time
import requests

"""
Exercise Let’s take the next 10-15 minutes to write a script that will 
programmatically download PEPs 8010 to 8016 using requests library 
"""


def download_pep(pep_number: int) -> bytes:
    url = f"https://www.python.org/dev/peps/pep-{pep_number}/"
    print(f"Begin downloading {url}")
    response = requests.get(url)
    print(f"Finished downloading {url}")
    return response.content


def write_to_file(pep_number: int, content: bytes) -> None:
    filename = f"sync_{pep_number}.html"

    with open(filename, 'wb') as pep_file:
        print(f"Begin writing {filename}")
        pep_file.write(content)
        print(f"Finished writing {filename}")


if __name__ == '__main__':
    s = time.perf_counter()

    for number in range(8010, 8017):
        content = download_pep(number)
        write_to_file(number, content)

    elapsed = time.perf_counter() - s
    print(f"Execution time {elapsed:0.2f} seconds.")
    # Execution time 3.87 seconds.

