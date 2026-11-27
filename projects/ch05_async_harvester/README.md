# Project (Chapter 5): Async Rate-Limited API Batch Harvester

Fetch batches concurrently with `asyncio.Semaphore` caps and exponential backoff retries.

## Architecture Steps

1. Write `retry_async` with exponential sleep backoff.
2. Bound batch execution with `asyncio.Semaphore` and `gather`.
3. Verify speedup & failure handling with `pytest`.

## Milestones

- [ ] Implement exponential backoff retry coroutine
- [ ] Add Semaphore concurrency cap
- [ ] Pass pytest async speedup checks
