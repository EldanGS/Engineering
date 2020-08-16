import asyncio
from asyncio import FIRST_COMPLETED, CancelledError
from time import time
from dataclasses import dataclass
from loguru import logger

import aiohttp
from aiohttp import ClientSession
from typing import Union


@dataclass
class Service:
    name: str
    url: str
    ip_attr: str


SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query'),
)


async def fetch(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_ip(service: Service) -> str:
    start = time()
    logger.info("Fetching IP from {!r}", service.name)
    my_ip = "Not found"
    try:
        async with aiohttp.ClientSession() as session:
            response_json = await fetch(session, service.url)
    except CancelledError as exc:
        logger.debug("Cancelled fetching {!r}, {}", service.name, exc)
        return f"{service.name}s is unresponsive"
    except Exception:
        logger.exception("Error with {}", service)
        return "error"

    try:
        my_ip = response_json[service.ip_attr]
    except KeyError:
        logger.exception("Couldn't get ip from {} using field {}",
                         response_json, service.ip_attr)

    return f"{service.name} finished with result: {my_ip}, took: {round(time() - start, 3)}"


async def queries(timeout: Union[int, float]) -> None:
    futures = [fetch_ip(service) for service in SERVICES]
    done, pending = await asyncio.wait(
        futures,
        timeout=timeout,
        return_when=FIRST_COMPLETED,
    )

    for future in pending:
        future.cancel()

    for future in done:
        logger.info("result: {!r}", future.result())
        break
    else:
        logger.warning("Could not fetch any result in time {}s", timeout)


if __name__ == '__main__':
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(queries(1))
    ioloop.close()
