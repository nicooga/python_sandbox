# RESTful API Server

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

