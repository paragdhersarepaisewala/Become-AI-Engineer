# Workbook — Chapter 6: Concurrency, Async Programming & Event Loops


---

## 6.1 Async Concurrency: Bounded Batch Runner with Semaphore (`Foundation` · Async)

Write `async def run_bounded(items: list[str], worker, max_concurrent: int) -> list[str]`.

### Thinking Blueprint

- Wrap `worker(item)` in `async with sem:` and `asyncio.gather`.

### Progressive Hints

1. `asyncio.gather` preserves original input order.

### Dry-Run Trace
With `max_concurrent=2`, at most 2 workers run at the same instant.

### Answer & Explanation
```python
import asyncio

async def run_bounded(items: list[str], worker, max_concurrent: int) -> list[str]:
    if max_concurrent < 1:
        raise ValueError('max_concurrent must be >= 1')
    sem = asyncio.Semaphore(max_concurrent)
    async def guarded(item: str) -> str:
        async with sem:
            return await worker(item)
    return list(await asyncio.gather(*(guarded(x) for x in items)))
```

**High-Level Blocks:** `Semaphore` acts as a concurrency bouncer while `gather` overlaps waits.


---

## 6.2 Async Retries with Exponential Backoff (`Intermediate` · Async)

Write `async def retry_async(fn, max_retries: int = 3, base_delay: float = 0.01)`.

### Thinking Blueprint

- Loop `0..max_retries`, `await fn()`, on last failure re-raise else sleep exponentially.

### Progressive Hints

1. Never use `time.sleep` inside `async def`!

### Dry-Run Trace
0.01s -> 0.02s -> succeeds.

### Answer & Explanation
```python
import asyncio

async def retry_async(fn, max_retries: int = 3, base_delay: float = 0.01):
    for attempt in range(max_retries + 1):
        try:
            return await fn()
        except Exception:
            if attempt == max_retries:
                raise
            await asyncio.sleep(base_delay * (2 ** attempt))
```

**High-Level Blocks:** Non-blocking exponential backoff protects rate-limited APIs.
