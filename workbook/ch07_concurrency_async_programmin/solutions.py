"""Reference solutions with explanations."""


# --- 7.1: Async Concurrency: Bounded Batch Runner with Semaphore ---
import asyncio

async def run_bounded(items: list[str], worker, max_concurrent: int) -> list[str]:
    if max_concurrent < 1:
        raise ValueError('max_concurrent must be >= 1')
    sem = asyncio.Semaphore(max_concurrent)
    async def guarded(item: str) -> str:
        async with sem:
            return await worker(item)
    return list(await asyncio.gather(*(guarded(x) for x in items)))


# --- 7.2: Async Retries with Exponential Backoff ---
import asyncio

async def retry_async(fn, max_retries: int = 3, base_delay: float = 0.01):
    for attempt in range(max_retries + 1):
        try:
            return await fn()
        except Exception:
            if attempt == max_retries:
                raise
            await asyncio.sleep(base_delay * (2 ** attempt))
