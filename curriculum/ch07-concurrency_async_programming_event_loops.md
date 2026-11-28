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

Next, in **Section 7.2**, we limit concurrency with `Semaphore` and add safe exponential-backoff retries.


### 4. Practical Example — Unpacking Tasks Into `asyncio.gather(*tasks)`

```python
import asyncio

async def double_async(n: int) -> int:
    await asyncio.sleep(0.02)
    return n * 2

async def main() -> None:
    # `*tasks` unpacks a list [t1, t2, t3] into separate arguments gather(t1, t2, t3)
    tasks = [double_async(i) for i in [1, 2, 3, 4]]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
```

### Common Mistakes to Avoid

- Calling `time.sleep(1)` or `requests.get()` inside `async def` (freezes the whole event loop!). Use `await asyncio.sleep()` / `httpx.AsyncClient`.
- Writing `for x in items: await task(x)` (runs sequentially instead of using `asyncio.gather`).

**Key Takeaway:** Use `async def` + `await` for waiting I/O, and `asyncio.gather(*tasks)` to run a list of coroutines concurrently.


---

## 7.2 Limiting Concurrency (`Semaphore`) & Exponential Backoff Retries

> **Before You Start:** Sending 1,000 API requests at the exact same millisecond crashes servers (`429 Too Many Requests`). You need two guardrails: a concurrency cap and smart retries.

### 1. Definition
- **`asyncio.Semaphore(N)`:** A gatekeeper allowing at most `N` coroutines inside `async with sem:` at the same time.
- **Exponential Backoff:** Waiting slightly longer after each failed try (`0.1s -> 0.2s -> 0.4s`) so overloaded APIs recover.

### 2. Exact Syntax — Semaphore + Retry Loop Syntax
```python
sem = asyncio.Semaphore(3)        # max 3 running at once
async with sem:
    await do_work()

# Exponential backoff retry:
for attempt in range(max_retries + 1):
    try:
        return await fn()
    except Exception:
        if attempt == max_retries:
            raise                 # out of retries -> re-raise error!
        await asyncio.sleep(base_delay * (2 ** attempt))
```

- `async with sem:` acquires a slot on entry and **always** releases it on exit (even if an error happens).
- `2 ** attempt` doubles the delay on each retry (`1x, 2x, 4x`).
- Plain `raise` inside `except` re-throws the original exception once all retries are used up.

### 3. Tiny Example (Line-by-Line) — Retrying a Flaky Coroutine Twice Before Succeeding
```python
import asyncio

state = {'tries': 0}
async def flaky_api():
    state['tries'] += 1
    if state['tries'] < 3:
        raise RuntimeError('Temporary 429')
    return 'Success on try 3!'

async def retry(fn, max_retries=3, base_delay=0.01):
    for attempt in range(max_retries + 1):
        try:
            return await fn()
        except Exception:
            if attempt == max_retries:
                raise
            await asyncio.sleep(base_delay * (2 ** attempt))

print(asyncio.run(retry(flaky_api)))
```

1. Try 1 (`attempt=0`): fails -> sleeps `0.01s`.
2. Try 2 (`attempt=1`): fails -> sleeps `0.02s`.
3. Try 3 (`attempt=2`): succeeds and returns `'Success on try 3!'`.

**Try the interactive Asyncio Event Loop Simulator below** to compare Sequential vs `gather` vs `Semaphore(2)`!


### 4. Practical Example — Capping Concurrency With `asyncio.Semaphore`

```python
import asyncio

async def bounded_worker(sem: asyncio.Semaphore, item_id: int) -> str:
    async with sem:
        await asyncio.sleep(0.05)
        return f'done-{item_id}'

async def run_batch() -> list[str]:
    sem = asyncio.Semaphore(3)
    tasks = [bounded_worker(sem, i) for i in range(6)]
    return list(await asyncio.gather(*tasks))

print(asyncio.run(run_batch()))
```

### Common Mistakes to Avoid

- Creating a brand-new `asyncio.Semaphore(3)` *inside* the worker function (each task gets its own semaphore, so zero limiting happens!). Create `sem` **once** outside and pass it in.

**Key Takeaway:** Create one `Semaphore` outside workers to cap concurrency, and use `await asyncio.sleep(base_delay * 2**attempt)` for non-blocking retries.


---

## Hands-On Project: Async Rate-Limited API Batch Harvester

Fetch batches concurrently using `asyncio.Semaphore` and exponential backoff retries.

1. Write `retry_async` with exponential sleep backoff.
2. Bound batch execution with `asyncio.Semaphore` and `gather`.
3. Verify speedup & failure handling with `pytest`.
