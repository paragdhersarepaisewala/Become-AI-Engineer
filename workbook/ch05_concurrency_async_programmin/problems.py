"""Starter exercises — implement each function and run pytest on test_problems.py."""


# --- 5.1: Async Concurrency: Bounded Batch Runner with Semaphore ---
import asyncio

async def run_bounded(items: list[str], worker, max_concurrent: int) -> list[str]:
    # TODO: bound concurrent worker calls with Semaphore
    pass


# --- 5.2: Async Retries with Exponential Backoff ---
import asyncio

async def retry_async(fn, max_retries: int = 3, base_delay: float = 0.01):
    # TODO: retry with exponential backoff
    pass
