import asyncio
from contextlib import asynccontextmanager
from pathlib import Path
from typing import AsyncGenerator


# Using @asynccontextmanager decorator
@asynccontextmanager
async def open_file_decorated(filename: str, mode: str = 'r') -> AsyncGenerator:
    loop = asyncio.get_event_loop()
    file = await loop.run_in_executor(None, open, filename, mode)

    try:
        yield file  # This is where __aenter__ returns the value
    finally:
        await loop.run_in_executor(None, file.close)  # This runs in __aexit__


# Manual implementation (what the decorator does under the hood)
class AsyncFileContextManager:
    def __init__(self, filename: str, mode: str = 'r'):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.gen = None

    async def __aenter__(self):
        loop = asyncio.get_event_loop()
        self.file = await loop.run_in_executor(None, open, self.filename, self.mode)
        return self.file

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, self.file.close)
        return False  # Don't suppress exceptions


def open_file_manual(filename: str, mode: str = 'r'):
    return AsyncFileContextManager(filename, mode)


# Manual implementation using async generator (closer to decorator)
class _AsyncGeneratorContextManager:
    def __init__(self, gen_func, *args, **kwargs):
        self.gen_func = gen_func
        self.args = args
        self.kwargs = kwargs
        self.gen = None

    async def __aenter__(self):
        self.gen = self.gen_func(*self.args, **self.kwargs)
        return await self.gen.__anext__()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # Continue execution after yield (cleanup)
        try:
            await self.gen.__anext__()  # This should raise StopAsyncIteration
        except StopAsyncIteration:
            pass
        return False


async def _open_file_generator(filename: str, mode: str = 'r'):
    loop = asyncio.get_event_loop()
    file = await loop.run_in_executor(None, open, filename, mode)

    try:
        yield file
    finally:
        await loop.run_in_executor(None, file.close)


def open_file_generator_based(filename: str, mode: str = 'r'):
    return _AsyncGeneratorContextManager(_open_file_generator, filename, mode)


async def main():
    test_file = str(Path(__file__).parent / 'test_file.txt')

    print("Using @asynccontextmanager decorator")
    async with open_file_decorated(test_file) as file:
        loop = asyncio.get_event_loop()
        content = await loop.run_in_executor(None, file.read)
        print(f'Content: {content}')

    print("Using manual class-based implementation")
    async with open_file_manual(test_file) as file:
        loop = asyncio.get_event_loop()
        content = await loop.run_in_executor(None, file.read)
        print(f'Content: {content}')

    print("Using generator-based manual implementation")
    async with open_file_generator_based(test_file) as file:
        loop = asyncio.get_event_loop()
        content = await loop.run_in_executor(None, file.read)
        print(f'Content: {content}')


if __name__ == '__main__':
    asyncio.run(main())

