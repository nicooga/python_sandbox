import curio
from async_generators.domainlib import Result
from curio import socket, TaskGroup

DOMAINS = 'python.org rust-lang.org golang.org no-lang.invalid'.split()

async def probe(domain: str) -> Result:
    try:
        await socket.getaddrinfo(domain, None)
    except socket.gaierror:
        return Result(domain, False)
    else:
        return Result(domain, True)

async def probe_domains(domains: list[str]) -> None:
    """Probe multiple domains concurrently using curio TaskGroup."""
    async with TaskGroup() as tg:
        for domain in domains:
            await tg.spawn(probe, domain)

        async for task in tg:
            result = task.result
            print(f"> {result.domain} is {'found' if result.found else 'not found'}")