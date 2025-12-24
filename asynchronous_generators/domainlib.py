import asyncio
import socket
from collections.abc import Iterable, AsyncIterator
from typing import NamedTuple, Optional
from keyword import kwlist

class Result(NamedTuple):
    domain: str
    found: bool

async def multi_probe(domains: Iterable[str]) -> AsyncIterator[Result]:
    coros = [probe(domain) for domain in domains]

    for coro in asyncio.as_completed(coros):
        yield await coro

async def probe(
    domain: str,
    loop: Optional[asyncio.AbstractEventLoop] = None
) -> AsyncIterator[Result]:
    if loop is None:
        loop = asyncio.get_event_loop()

    try:
        await loop.getaddrinfo(domain, None)
    except socket.gaierror:
        return Result(domain, False)
    else:
        return Result(domain, True)

async def main():
    domains = (f'{kw}-python.org' for kw in kwlist)

    async for result in multi_probe(domains):
        print(f'> {result.domain} is {"found" if result.found else "not found"}')

if __name__ == '__main__':
    asyncio.run(main())