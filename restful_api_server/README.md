# RESTful API Server

Example implementation of a RESTful web API using FastAPI.

## Concepts Demonstrated

- FastAPI application setup and routing
- Pydantic models for request/response validation
- Async route handlers
- HTML response serving
- Application state management

## Requirements

```bash
pip install fastapi pydantic uvicorn
```

## Usage

```bash
uvicorn restful_api_server.web_mojifinder:app --reload
```

## Endpoints

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

