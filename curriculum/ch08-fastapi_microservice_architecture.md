# Chapter 8: FastAPI & Microservice Architecture

*HTTP endpoints, Pydantic validation, async vs sync routes, SSE token streaming, and Gateway + Worker microservices.*

**Why It Matters:** FastAPI turns Python functions into web APIs with automatic data validation and interactive docs. Splitting heavy GPU inference into a background worker prevents slow model calls from freezing the API.

**Skills Covered:** FastAPI, Pydantic BaseModel, @app.post, SSE Streaming, Microservices


---

## 8.1 FastAPI Endpoints, Pydantic Contracts & Microservices

> **Before You Start:** An API endpoint is just a Python function attached to a URL (like `POST /tokenize`) that receives JSON and returns JSON.

### 1. Definition
- **FastAPI:** A Python web framework that turns typed functions into fast HTTP APIs.
- **Pydantic (`BaseModel`):** Automatically checks incoming JSON types/constraints and rejects bad inputs with HTTP `422` before your code runs.
- **Microservice Split:** Keeping a fast lightweight **API Gateway** separate from heavy **Worker** processes connected by a queue.

### 2. Exact Syntax — FastAPI + Pydantic Schema Template
```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class InputData(BaseModel):
    text: str = Field(min_length=1)   # rejects empty string automatically!

@app.post('/analyze')
def analyze(payload: InputData) -> dict:
    return {'length': len(payload.text)}
```

- `@app.post('/analyze')` is a decorator linking HTTP POST `/analyze` to the `analyze` function.
- Passing `payload: InputData` makes FastAPI parse and validate the request JSON automatically.
- Use `def` for CPU/blocking work (FastAPI runs it in a threadpool); use `async def` only when `await`-ing non-blocking I/O!

### 3. Tiny Example (Line-by-Line) — Testing an Endpoint Without Starting a Server (`TestClient`)
```python
from fastapi.testclient import TestClient
# assuming `app` from above:
client = TestClient(app)
resp = client.post('/analyze', json={'text': 'hello'})
print(resp.status_code, resp.json())
```

1. `TestClient(app)` lets you send fake HTTP requests directly in `pytest`.
2. `resp.status_code` is `200`, and `resp.json()` is `{'length': 5}`.
3. Sending `{'text': ''}` automatically returns `422` because `min_length=1` failed!

### Streaming Tokens (`SSE`) & Gateway-Worker Queues
When an LLM generates 200 words, waiting until the end feels slow. `StreamingResponse` yields tokens one-by-one as they generate, while heavy batch jobs go onto a queue (`asyncio.Queue` / Redis) for background workers.


### 4. Practical Example — Streaming Tokens via Server-Sent Events (SSE)

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
            await asyncio.sleep(0.05)
    return StreamingResponse(token_generator(), media_type='text/event-stream')
```

### Common Mistakes to Avoid

- Running slow synchronous PyTorch/CPU code directly inside `async def` without `await` (blocks the entire server!).

**Key Takeaway:** Let Pydantic validate inputs at the boundary, use `TestClient` for instant tests, and offload heavy work to workers.


---

## Hands-On Project: Async Inference Gateway & Background Worker Microservice

Build a decoupled FastAPI Gateway + async background worker queue with `TestClient` tests.

1. Define shared Pydantic schemas.
2. Build Gateway endpoints + SSE stream.
3. Build async worker loop and test with `TestClient`.
