# Chapter 5: Concurrency, Async Programming & Event Loops

*Waiting vs computing, the GIL, async def, await, asyncio.gather, Semaphores, and safe retries.*

**Why It Matters:** Calling LLM APIs, fetching web pages, and handling FastAPI users spend 95% of their time *waiting* on the network. `asyncio` lets one Python process handle hundreds of waiting tasks at once instead of stalling one-by-one.

**Skills Covered:** I/O vs CPU, async def / await, asyncio.gather, Semaphore, Retries


---

## 5.1 `async def`, `await` & `asyncio.gather` From Scratch

> **Before You Start:** Imagine cooking pasta and boiling tea: you don't stare frozen at the kettle for 3 minutes before starting the pasta—you start the kettle, then chop vegetables while it heats!

### 1. Definition
- **Synchronous (normal) code:** Waits idly for Task 1 to finish completely before starting Task 2.
- **Asynchronous (`asyncio`):** When Task 1 hits a network/timer wait (`await`), Python pauses Task 1 and works on Task 2 immediately.
- **Event Loop:** The traffic controller inside `asyncio.run(...)` that switches between paused tasks whenever one is ready.

### 2. Exact Syntax — Core `asyncio` Keywords
```python
import asyncio

async def fetch_data(idx: int) -> str:      # 1. `async def` defines a coroutine
    await asyncio.sleep(1.0)                # 2. `await` pauses & yields to other tasks
    return f'done-{idx}'

async def main():
    results = await asyncio.gather(         # 3. `gather` runs all concurrently!
        fetch_data(1), fetch_data(2)
    )

asyncio.run(main())                         # 4. starts the event loop
```

- `async def`: marks a function as pauseable (calling it creates a coroutine object; it doesn't run until `await`ed).
- `await`: *"Pause THIS task while waiting, and let the Event Loop run other tasks until this finishes."*
- `asyncio.gather(t1, t2, ...)`: starts all given coroutines together and returns their results in the same order.

### 3. Tiny Example (Line-by-Line) — 2 Tasks Taking 1s Total Instead of 2s
```python
import asyncio

async def greet(name):
    await asyncio.sleep(1)
    return f'hi {name}'

async def main():
    res = await asyncio.gather(greet('A'), greet('B'))
    print(res)

asyncio.run(main())
```

1. `asyncio.run(main())` boots the Event Loop.
2. `gather(greet('A'), greet('B'))` starts `'A'`—it hits `await asyncio.sleep(1)` and pauses.
3. Immediately (0ms later!), the loop starts `'B'`—it also pauses for 1s.
4. After 1 second total, both wake up and `print(res)` outputs `['hi A', 'hi B']`!

### Limiting Concurrency with `asyncio.Semaphore`
Firing 1,000 API calls at once gets you blocked (`429 Too Many Requests`). Wrap calls in `sem = asyncio.Semaphore(5)` and `async with sem:` so **at most 5** run at any moment.

**Test the Asyncio Event Loop Simulator below** to see Sequential vs `gather` vs `Semaphore(2)` timelines!


### 4. Practical Example — Bounded Async Worker with Semaphore

```python
import asyncio

async def safe_fetch(sem: asyncio.Semaphore, item_id: int) -> str:
    # Block 1: Wait here if 3 workers are already active
    async with sem:
        await asyncio.sleep(0.1)
        return f'ok-{item_id}'

async def run_batch() -> list[str]:
    # Block 2: Cap concurrent tasks to 3
    sem = asyncio.Semaphore(3)
    tasks = [safe_fetch(sem, i) for i in range(10)]
    return list(await asyncio.gather(*tasks))
```

### Common Mistakes to Avoid

- Calling `time.sleep(2)` or `requests.get()` inside `async def`—that freezes the ENTIRE event loop! Use `await asyncio.sleep(2)` or `httpx.AsyncClient`.
- Writing `for x in items: await fetch(x)`—that runs one-by-one sequentially! Use `asyncio.gather(...)`.

**Key Takeaway:** Use `async def` + `await` for waiting/network I/O, `asyncio.gather` to overlap tasks, and `Semaphore` to avoid rate limits.


---

## Hands-On Project: Async Rate-Limited API Batch Harvester

Fetch batches concurrently with `asyncio.Semaphore` caps and exponential backoff retries.

1. Write `retry_async` with exponential sleep backoff.
2. Bound batch execution with `asyncio.Semaphore` and `gather`.
3. Verify speedup & failure handling with `pytest`.
