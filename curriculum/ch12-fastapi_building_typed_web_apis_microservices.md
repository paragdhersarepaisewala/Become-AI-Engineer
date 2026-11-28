# Chapter 12: FastAPI — Building Typed Web APIs & Microservices

*GET/POST routes, Pydantic request contracts, path/query params, TestClient, SSE streaming, and Gateway + Worker microservices.*

**Why It Matters:** Now that you know **Pydantic** (Ch 10) and how clients call APIs with **`requests`** (Ch 11), `FastAPI` connects both: you build the server side that receives JSON, validates it with Pydantic, and streams answers back.

**Skills Covered:** FastAPI, @app.get / @app.post, Pydantic Contracts, TestClient, SSE Streaming, Microservices


---

## 12.1 FastAPI Routes, Pydantic Contracts & Microservices

> **Before You Start:** An API endpoint is just a Python function attached to a URL (`@app.post('/analyze')`) using your Chapter 10 Pydantic models.

### 1. Definition
- **FastAPI:** Turns typed Python functions into fast HTTP APIs with automatic `/docs` swagger UI.
- **Microservice Split:** Keeping a lightweight **API Gateway** separate from heavy **Worker** processes connected by a queue.

### 2. Exact Syntax — FastAPI + Pydantic Schema Template
```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class InputData(BaseModel):
    text: str = Field(min_length=1)

@app.post('/analyze')
def analyze(payload: InputData) -> dict:
    return {'length': len(payload.text)}
```

- `@app.post('/analyze')` links HTTP POST `/analyze` to `analyze`.
- FastAPI automatically parses incoming JSON into `InputData` and returns `422` if invalid!
- Use `def` for CPU/blocking work (runs in a threadpool); use `async def` when `await`-ing non-blocking I/O.

### 3. Tiny Example (Line-by-Line) — Testing FastAPI Endpoints With `TestClient`
```python
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
@app.get('/ping')
def ping() -> dict:
    return {'ok': True}

client = TestClient(app)
resp = client.get('/ping')
print(resp.status_code, resp.json())
```

1. `TestClient(app)` tests your API in memory without starting uvicorn.
2. Prints `200 {'ok': True}`.

### Streaming Tokens (`SSE`) & Gateway-Worker Queues
`StreamingResponse` yields LLM tokens word-by-word as they generate, while slow batch jobs go onto a queue (`asyncio.Queue` / Redis) for background workers.


### 4. Practical Example — Streaming Words via Server-Sent Events (SSE)

```python
import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get('/stream')
async def stream_words() -> StreamingResponse:
    async def token_generator():
        for word in ['AI', 'engineers', 'ship', 'systems.']:
            yield f'data: {word}\n\n'
            await asyncio.sleep(0.02)
    return StreamingResponse(token_generator(), media_type='text/event-stream')
```

### Common Mistakes to Avoid

- Running slow blocking CPU/PyTorch calls directly inside `async def` without `await` (freezes the server!).

**Key Takeaway:** Validate payloads with Pydantic, test with `TestClient`, stream tokens via SSE, and offload heavy work to workers.


---

## Hands-On Project: Async Inference Gateway & Background Worker Microservice

Build a decoupled FastAPI Gateway + async background worker queue with `TestClient` tests.

1. Define shared Pydantic schemas.
2. Build Gateway endpoints + SSE stream.
3. Build async worker loop and test with `TestClient`.
