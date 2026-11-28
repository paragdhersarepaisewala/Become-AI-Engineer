# Workbook — Chapter 5: Essential DSA & Dynamic Programming Demystified


---

## 5.1 DP Foundation: Climbing Stairs (`n = 60`) (`Foundation` · Dynamic Programming)

Climb `1` or `2` steps at a time. Write `climb_ways(n: int) -> int` (`climb_ways(0) == 1`).

### Thinking Blueprint

- `dp[i] = dp[i-1] + dp[i-2]` starting from `1, 1`.

### Progressive Hints

1. Use two variables `prev2, prev1 = 1, 1`.

### Dry-Run Trace
`0->1, 1->1, 2->2, 3->3, 4->5`.

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

**High-Level Blocks:** Bottom-up rolling variables compute each step once.


---

## 5.2 1D DP Choice Pattern: Minimum Coin Change (`Intermediate` · Dynamic Programming)

Return fewest coins summing to `amount`, or `-1` if impossible.

### Thinking Blueprint

- `dp[a] = min(dp[a], 1 + dp[a - c])` for each coin `c <= a`.

### Progressive Hints

1. Start `dp = [amount + 1] * (amount + 1)` with `dp[0] = 0`.

### Dry-Run Trace
`dp[3]=1`, so `dp[6]` finds `1+dp[3]=2`.

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

**High-Level Blocks:** Tests every valid coin choice at each sub-amount and keeps the global minimum.


---

## 5.3 2D DP Table: Levenshtein Edit Distance (`Challenge` · Dynamic Programming)

Write `edit_distance(a: str, b: str) -> int` (`'kitten'` -> `'sitting'` == `3`).

### Thinking Blueprint

- Equal -> `dp[i-1][j-1]`; else `1 + min(top, left, diag)`.

### Progressive Hints

1. Initialize base row `0..n` and base col `0..m`.

### Dry-Run Trace
`'cat' -> 'cut'` == `1`.

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

**High-Level Blocks:** Compares delete (`top`), insert (`left`), and match/replace (`diagonal`).


---

## 5.4 DAG Topological Sort (Pipeline Task Scheduler) (`Challenge` · DSA)

Given `tasks` and `deps` `(a, b)`, return alphabetical topological order or raise `ValueError('Cycle detected')`.

### Thinking Blueprint

- Track `indeg` and `adj`, pop 0-indegree from `heapq`.

### Progressive Hints

1. If `len(order) != len(tasks)`, raise `ValueError`.

### Dry-Run Trace
`clean -> train -> eval`.

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

**High-Level Blocks:** Graph + in-degree setup, min-heap execution, and length check for cycles.
