import asyncio
from async_generators.domainlib import probe, multi_probe

DOMAINS = 'python.org rust-lang.org golang.org no-lang.invalid'.split()

async def main():
    # Async comprehension expression exist so we can rewrite this rather verbose code:
    found_domains = []

    async for result in multi_probe(DOMAINS):
        if result.found:
            found_domains.append(result.domain)

    print(f"Verbose code result: {found_domains}")

    print_separator()

    # ... into a single line:
    found_domains = [result.domain async for result in multi_probe(DOMAINS) if result.found]
    print(f"Single line code result: {found_domains}")

    print_separator()

    # Async comprehension expressions also allow us to use the await keyword inside the comprehension expression
    found_domains = [result.domain async for result in (await probe(domain) for domain in DOMAINS) if result.found]
    print(f"Await keyword result: {found_domains}")

    print_separator()

    # NOTE: The last example almsot the same as asyncio.gather(), except gather provides more control over exceptions.
    # It's recommended to always set return_exceptions=True when using gather.
    found_domains = await asyncio.gather(*[probe(domain) for domain in DOMAINS], return_exceptions=True)
    print(f"Gather result: {found_domains}")

    print_separator()


    # async/await can be used in dict comprehension expressions too:
    found_domains = {
        result.domain: result.found
        async for result in (await probe(domain) for domain in DOMAINS)
    }

    print(f"Dict comprehension result: {found_domains}")

    print_separator()

    # ... and set comprehension expressions too:
    found_domains = {result.domain async for result in (await probe(domain) for domain in DOMAINS) if result.found}
    print(f"Set comprehension result: {found_domains}")

def print_separator():
    print("-" * 80)
    print()

if __name__ == '__main__':
    asyncio.run(main())