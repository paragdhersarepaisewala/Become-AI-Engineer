# Chapter 7: Concurrency, Async Programming & Event Loops

*Waiting vs computing, async def, await, asyncio.gather, Semaphores, and exponential backoff retries.*

**Why It Matters:** Calling LLM APIs, fetching documents, and serving web users spend most of their time *waiting* on network replies. `asyncio` overlaps all those waits so 100 API calls finish in ~1 second instead of 100 seconds.

**Skills Covered:** I/O vs CPU, async def / await, asyncio.gather, Semaphore, Retries


---

## 7.1 `async def`, `await`, `gather` & `Semaphore` From Scratch

> **Before You Start:** When boiling water (3 min wait) and chopping onions, you don't stand frozen staring at the kettle—you start the kettle, then chop while waiting!

### 1. Definition
- **Asynchronous (`asyncio`):** Lets one Python thread juggle many *waiting* I/O tasks by switching tasks whenever one hits `await`.
- **Event Loop:** The scheduler started by `asyncio.run(...)` that switches between paused tasks.

### 2. Exact Syntax — Core `asyncio` Syntax
```python
import asyncio

async def fetch(i: int) -> str:
    await asyncio.sleep(1.0)             # pauses & yields to other tasks!
    return f'ok-{i}'

async def main():
    res = await asyncio.gather(fetch(1), fetch(2))  # runs both together!
    print(res)

asyncio.run(main())
```

- `async def` creates a pauseable coroutine function.
- `await` means: *"Pause here until this wait finishes; let other tasks run in the meantime."*
- `asyncio.gather(...)` launches multiple coroutines concurrently and returns results in original order.
- `asyncio.Semaphore(N)` limits concurrency so at most `N` tasks run at once (prevents API rate-limit bans!).

### 3. Tiny Example (Line-by-Line) — Two 1-Second Tasks Finishing in ~1 Second Total
```python
import asyncio, time

async def task(name):
    await asyncio.sleep(0.2)
    return name

async def main():
    t0 = time.perf_counter()
    out = await asyncio.gather(task('A'), task('B'), task('C'))
    print(out, f'in {time.perf_counter() - t0:.2f}s')

asyncio.run(main())
```

1. `gather` starts A, B, and C immediately—all three sleep for 0.2s *at the same time*.
2. Total time is `~0.20s` instead of `0.60s`!

**Try the interactive Asyncio Event Loop Simulator below** to compare Sequential `for await` vs `gather` vs `Semaphore(2)`!


### 4. Practical Example — Capping Concurrency With `asyncio.Semaphore`

```python
import asyncio

async def bounded_worker(sem: asyncio.Semaphore, item_id: int) -> str:
    async with sem:
        await asyncio.sleep(0.05)
        return f'done-{item_id}'

async def run_batch() -> list[str]:
    sem = asyncio.Semaphore(3)
    return list(await asyncio.gather(*(bounded_worker(sem, i) for i in range(6))))

print(asyncio.run(run_batch()))
```

### Common Mistakes to Avoid

- Calling `time.sleep(1)` or `requests.get()` inside `async def` (freezes the whole event loop!). Use `await asyncio.sleep()` / `httpx.AsyncClient`.
- Writing `for x in items: await task(x)` (runs sequentially instead of using `asyncio.gather`).

**Key Takeaway:** Use `async def` + `await` for waiting I/O, `asyncio.gather` to overlap tasks, and `Semaphore` to limit concurrent requests.


---

## Hands-On Project: Async Rate-Limited API Batch Harvester

Fetch batches concurrently using `asyncio.Semaphore` and exponential backoff retries.

1. Write `retry_async` with exponential sleep backoff.
2. Bound batch execution with `asyncio.Semaphore` and `gather`.
3. Verify speedup & failure handling with `pytest`.
