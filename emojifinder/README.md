# Emojifinder

Search for emoji characters by their Unicode names using an inverted index.  
This is an example on how to implement servers with `asyncio`.  

## Overview

Emojifinder provides two interfaces for searching emoji characters (Unicode range U+1F600 to U+1F64F) by their names:

- **TCP Server**: Interactive command-line interface over TCP
- **Web API**: RESTful HTTP API with web interface

## Building

### Requirements

- Python 3.7+
- `fastapi` (for web interface)
- `pydantic` (for web API)

### Installation

```bash
pip install fastapi pydantic uvicorn
```

## APIs

### Core Library

**`EmojiInvertedIndex`** (`emojiindex.py`)

- `search(query: str) -> set[Emoji]`: Searches for emojis matching the query string. The query is tokenized and matched against Unicode character names.

### TCP Server

**`tcp_mojifinder.py`**

Interactive TCP server that accepts connections and provides a search prompt.

**Usage:**
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

### Web API

**`web_mojifinder.py`**

FastAPI application with REST endpoint and web interface.

**Usage:**
```bash
uvicorn emojifinder.web_mojifinder:app --reload
```

**Endpoints:**

- `GET /search?q=<query>`: Returns JSON array of matching emojis
  ```json
  [
    {"char": "😀", "name": "GRINNING FACE"},
    {"char": "😃", "name": "GRINNING FACE WITH BIG EYES"}
  ]
  ```

- `GET /`: HTML search interface

**Example:**
```bash
curl "http://localhost:8000/search?q=grinning"
```

