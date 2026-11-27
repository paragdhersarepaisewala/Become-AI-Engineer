# Workbook — Chapter 8: FastAPI & Microservice Architecture


---

## 8.1 Pydantic Contract & FastAPI `/tokenize` Endpoint (`Foundation` · FastAPI)

Build `app = FastAPI()` with `POST /tokenize` accepting `{'text': str, 'lowercase': bool = True}` (reject blank strings via HTTP 422) and returning `{'tokens': list[str], 'count': int}`.

### Thinking Blueprint

- Block 1: Pydantic `BaseModel` with `@field_validator('text')` rejecting whitespace-only text.
- Block 2: Route handler transforms and returns structured dict.

### Progressive Hints

1. Raise `ValueError` inside `@field_validator` to trigger FastAPI's automatic 422 response.

### Dry-Run Trace
`{'text': 'Hello AI'}` -> `200 {'tokens': ['hello', 'ai'], 'count': 2}`. `{'text': '   '}` -> `422`.

### Answer & Explanation
```python
from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

class TokenizeRequest(BaseModel):
    text: str = Field(min_length=1, max_length=500)
    lowercase: bool = True

    @field_validator('text')
    @classmethod
    def must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('text cannot be blank')
        return v

@app.post('/tokenize')
def tokenize_endpoint(req: TokenizeRequest) -> dict:
    raw = req.text.lower() if req.lowercase else req.text
    tokens = raw.split()
    return {'tokens': tokens, 'count': len(tokens)}
```

**High-Level Blocks:** Input validation sits cleanly inside the Pydantic contract so endpoint code stays focused on business logic.


---

## 8.2 Microservice Pattern: Async Job Queue & Worker (`Intermediate` · FastAPI)

Implement `JobBroker` with `submit(payload: str) -> str` and `async def process_one() -> bool`.

### Thinking Blueprint

- `submit` generates `job-1`, sets status `'queued'`, and enqueues without blocking.
- `process_one` returns `False` if empty, else processes one job to `'done'` and returns `True`.

### Progressive Hints

1. Use `self.queue.put_nowait((job_id, payload))` inside synchronous `submit()`.

### Dry-Run Trace
`submit('train')` -> `'queued'` -> `await process_one()` -> `{'status': 'done', 'result': 'TRAIN'}`.

### Answer & Explanation
```python
import asyncio

class JobBroker:
    def __init__(self) -> None:
        self.queue: asyncio.Queue[tuple[str, str]] = asyncio.Queue()
        self.jobs: dict[str, dict] = {}
        self._counter = 0

    def submit(self, payload: str) -> str:
        self._counter += 1
        job_id = f'job-{self._counter}'
        self.jobs[job_id] = {'status': 'queued', 'result': None}
        self.queue.put_nowait((job_id, payload))
        return job_id

    async def process_one(self) -> bool:
        if self.queue.empty():
            return False
        job_id, payload = await self.queue.get()
        self.jobs[job_id]['status'] = 'processing'
        await asyncio.sleep(0)
        self.jobs[job_id]['result'] = payload.upper()
        self.jobs[job_id]['status'] = 'done'
        self.queue.task_done()
        return True
```

**High-Level Blocks:** Separating job intake (`submit`) from execution (`process_one`) models the exact Redis + Worker microservice pattern.
