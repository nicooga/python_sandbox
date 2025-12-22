# TCP Server with asyncio

Example implementation of an asynchronous TCP server using Python's `asyncio` module.

## Concepts Demonstrated

- `asyncio.start_server()` for creating TCP servers
- `StreamReader` and `StreamWriter` for async I/O
- Connection handling with proper cleanup using try/finally
- `await writer.drain()` to ensure data is sent
- Handling client disconnections and encoding errors

## Usage

```bash
python tcp_mojifinder.py
```

The server listens on `127.0.0.1:8000` by default. Connect using `telnet` or `nc`:

```bash
telnet 127.0.0.1 8000
# or
nc 127.0.0.1 8000
```

**Protocol:**
- Server sends `?> ` prompt
- Client sends a search query (one per line)
- Server responds with count and matching emojis
- Connection remains open for multiple queries

