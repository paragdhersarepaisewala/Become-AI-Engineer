# Workbook — Chapter 4: Essential DSA & Dynamic Programming Demystified


---

## 4.1 DP Foundation: Climbing Stairs (`n = 60`) (`Foundation` · Dynamic Programming)

Climb `1` or `2` steps at a time. Write `climb_ways(n: int) -> int` (`climb_ways(0) == 1`) fast enough for `n = 60`.

### Thinking Blueprint

- `dp[i] = dp[i-1] + dp[i-2]` with `dp[0]=1, dp[1]=1`.
- Keep only `prev2, prev1` in O(1) memory.

### Progressive Hints

1. `prev2, prev1 = prev1, prev2 + prev1`.

### Dry-Run Trace
`n=0->1, 1->1, 2->2, 3->3, 4->5, 5->8`.

### Answer & Explanation
```python
def climb_ways(n: int) -> int:
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1
```

**High-Level Blocks:** Bottom-up rolling variables compute each step exactly once instead of ~2^60 redundant recursive calls.


---

## 4.2 1D DP Choice Pattern: Minimum Coin Change (`Intermediate` · Dynamic Programming)

Return fewest coins from `coins` to sum to `amount`, or `-1` if impossible.

### Thinking Blueprint

- `dp[a]` = min coins for amount `a`; `dp[0] = 0`.
- Try all `c <= a`: `dp[a] = min(dp[a], 1 + dp[a - c])`.

### Progressive Hints

1. Initialize `dp = [amount + 1] * (amount + 1)` with `dp[0] = 0`.

### Dry-Run Trace
For `coins=[1,3,4], amount=6`: `dp[3]=1`, so `dp[6]` checks `1+dp[3]=2` -> returns `2`.

### Answer & Explanation
```python
def min_coins(coins: list[int], amount: int) -> int:
    inf = amount + 1
    dp = [inf] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return -1 if dp[amount] > amount else dp[amount]
```

**High-Level Blocks:** (1) Sentinel `amount+1` represents unreachable states; (2) Inner coin loop tests every valid last coin and picks the minimum.


---

## 4.3 2D DP Table: Levenshtein Edit Distance (`Challenge` · Dynamic Programming)

Write `edit_distance(a: str, b: str) -> int` returning minimum edits (`'kitten'` -> `'sitting'` == `3`).

### Thinking Blueprint

- `dp[i][j]` = edit distance between `a[:i]` and `b[:j]`.
- Equal chars -> `dp[i-1][j-1]`; else `1 + min(delete, insert, replace)`.

### Progressive Hints

1. Initialize row 0 to `0..n` and col 0 to `0..m`.

### Dry-Run Trace
`'cat'` -> `'cut'`: `dp[3][3] == 1` (single replace `'a'->'u'`).

### Answer & Explanation
```python
def edit_distance(a: str, b: str) -> int:
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]
```

**High-Level Blocks:** (1) Base edges represent converting to/from empty prefixes; (2) Interior transitions compare top (delete), left (insert), and diagonal (match/replace).


---

## 4.4 DAG Topological Sort (Pipeline Task Scheduler) (`Challenge` · DSA)

Given `tasks` and `deps` (`(a, b)` means `a` runs before `b`), return deterministic topological order (alphabetical min-heap tie-break), or raise `ValueError('Cycle detected')` on cycles.

### Thinking Blueprint

- Compute `indeg` and `adj` list.
- Pop 0-indegree tasks from a min-heap, decrement dependents, verify `len(order) == len(tasks)`.

### Progressive Hints

1. Use `heapq` so ready tasks always pop in alphabetical order.

### Dry-Run Trace
`clean -> train -> eval` unlocks one task at a time in O((V+E) log V).

### Answer & Explanation
```python
import heapq

def schedule_tasks(tasks: list[str], deps: list[tuple[str, str]]) -> list[str]:
    adj: dict[str, list[str]] = {t: [] for t in tasks}
    indeg: dict[str, int] = {t: 0 for t in tasks}
    for src, dst in deps:
        adj[src].append(dst)
        indeg[dst] += 1
    heap = [t for t in tasks if indeg[t] == 0]
    heapq.heapify(heap)
    order: list[str] = []
    while heap:
        cur = heapq.heappop(heap)
        order.append(cur)
        for nxt in adj[cur]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                heapq.heappush(heap, nxt)
    if len(order) != len(tasks):
        raise ValueError('Cycle detected')
    return order
```

**High-Level Blocks:** (1) Graph + in-degree construction; (2) Min-heap processes ready nodes; (3) Length mismatch detects cycles cleanly.
