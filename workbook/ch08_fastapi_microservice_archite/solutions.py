"""Reference solutions with explanations."""


# --- 8.1: Pydantic Contract & FastAPI `/tokenize` Endpoint ---
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


# --- 8.2: Microservice Pattern: Async Job Queue & Worker ---
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
