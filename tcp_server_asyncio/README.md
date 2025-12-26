# TCP Server with asyncio

## Usage

Run from the project root directory:

```bash
python -m tcp_server_asyncio.tcp_mojifinder
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

