# Workbook — Chapter 5: Concurrency, Async Programming & Event Loops


---

## 5.1 Async Concurrency: Bounded Batch Runner with Semaphore (`Foundation` · Async)

Write `async def run_bounded(items: list[str], worker, max_concurrent: int) -> list[str]` preserving input order and allowing at most `max_concurrent` workers simultaneously.

### Thinking Blueprint

- Create `sem = asyncio.Semaphore(max_concurrent)`.
- Wrap each item in `async with sem: return await worker(item)` and gather all tasks.

### Progressive Hints

1. `asyncio.gather` preserves input order even if later tasks finish first.

### Dry-Run Trace
With `max_concurrent=2`, tasks 0 & 1 enter together; task 2 waits until one releases the semaphore.

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

**High-Level Blocks:** `async with sem:` acts as an automatic concurrency gate, releasing even on exceptions, while `gather` overlaps all awaits.


---

## 5.2 Async Retries with Exponential Backoff (`Intermediate` · Async)

Write `async def retry_async(fn, max_retries: int = 3, base_delay: float = 0.01)` trying up to `1 + max_retries` times.

### Thinking Blueprint

- Loop `attempt` from `0..max_retries`.
- Try `return await fn()`; on error re-raise on last attempt, else `await asyncio.sleep(base_delay * (2 ** attempt))`.

### Progressive Hints

1. Always use `await asyncio.sleep(...)`, never `time.sleep(...)`.

### Dry-Run Trace
Attempt 0 fails -> sleep 0.01s; Attempt 1 fails -> sleep 0.02s; Attempt 2 succeeds -> return value.

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

**High-Level Blocks:** Non-blocking exponential backoff lets other coroutines keep working on the event loop while waiting to retry.
