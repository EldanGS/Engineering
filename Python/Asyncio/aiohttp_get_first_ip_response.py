import asyncio
import time
from dataclasses import dataclass
from loguru import logger
import aiohttp
from concurrent.futures import FIRST_COMPLETED


@dataclass
class Service:
    name: str
    url: str
    ip_attr: str


SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)


async def fetch(session, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_ip(service: Service) -> str:
    start = time.time()
    print(f"Fetching IP from {service.name}")

    async with aiohttp.ClientSession() as session:
        response_json = await fetch(session, service.url)

    ip = response_json[service.ip_attr]

    return f"{service.name} finished with result: {ip}, took: {time.time() - start}"


async def queries() -> None:
    futures = [fetch_ip(service) for service in SERVICES]
    done, pending = await asyncio.wait(
        futures, return_when=FIRST_COMPLETED
    )
    logger.info("result: {}", done.pop().result())

    for future in pending:
        future.cancel()

if __name__ == '__main__':
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(queries())
    ioloop.close()
