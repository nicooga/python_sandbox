import asyncio
from async_generators.domainlib import multi_probe

async def main():
    domains = 'python.org rust-lang.org golang.org no-lang.invalid'.split()
    found_domains = (name async for name, found in multi_probe(domains) if found)

    # Found domains is now an async generator too
    print(found_domains)

    async for name in found_domains:
        print(f'> {name} is found')

    # But we can have a plain list too, just use square brackets
    found_domains = [name async for name, found in multi_probe(domains) if found]

    # This is a list
    print(found_domains)


if __name__ == '__main__':
    asyncio.run(main())