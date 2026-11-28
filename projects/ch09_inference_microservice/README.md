# Project (Chapter 9): Async Inference Gateway & Background Worker Microservice

Build a decoupled FastAPI Gateway + async background worker queue with `TestClient` tests.

## Architecture Steps

1. Define shared Pydantic schemas.
2. Build Gateway endpoints + SSE stream.
3. Build async worker loop and test with `TestClient`.

## Milestones

- [ ] Create Pydantic contracts
- [ ] Build FastAPI gateway + SSE endpoint
- [ ] Build async worker & pass TestClient pytest
