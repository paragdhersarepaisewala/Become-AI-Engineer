# Chapter 6: Essential DSA & Dynamic Programming Demystified

*Big-O intuition, Queues (deque), Heaps (heapq), Graphs (BFS & DAGs), and Dynamic Programming from recursion to tables.*

**Why It Matters:** Now that your loop & dict logic is strong, DSA gives you specialized tools: `deque` for queues/BFS, `heapq` for Top-K LLM token selection, DAGs for ML pipelines, and Dynamic Programming for sequence alignment & edit distance.

**Skills Covered:** Big-O, Queue (deque), Heap (heapq), Graphs & DAGs, Dynamic Programming


---

## 6.1 Queues (`deque`), Heaps (`heapq`) & Graphs (BFS & DAGs)

> **Before You Start:** Pick the data structure that matches the job you repeat most—never memorize unused structures.

### 1. Definition
- **`deque`:** A fast two-ended queue (add to back, remove from front in 1 step).
- **`heapq`:** Quickly grabs the smallest or Top-K largest items without sorting the entire list.
- **Graph / DAG:** Nodes connected by arrows (e.g., task dependencies `clean -> train -> eval`).

### 2. Exact Syntax — deque & heapq Essentials
```python
from collections import deque
import heapq

q = deque(['A'])
q.append('B')
front = q.popleft()              # 'A' in O(1) — unlike list.pop(0)!

top2 = heapq.nlargest(2, [5, 9, 2, 7])  # [9, 7]
```

- Never use `list.pop(0)` as a queue because Python shifts every remaining element in memory.
- `seen = {'A'}` inside graph BFS prevents walking in circles forever if nodes point back to each other.

### 3. Tiny Example (Line-by-Line) — Finding Shortest Hops in a Small Graph (BFS)
```python
from collections import deque
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
q = deque([('A', 0)])
seen = {'A'}
while q:
    node, dist = q.popleft()
    print(node, 'is', dist, 'hops from A')
    for nxt in graph[node]:
        if nxt not in seen:
            seen.add(nxt)
            q.append((nxt, dist + 1))
```

1. Starts at `'A'` with distance `0`.
2. Pops `'A'`, adds neighbors `'B'` (dist 1) and `'C'` (dist 1).
3. Pops `'B'` (dist 1), adds `'D'` (dist 2).
4. Because `deque` explores closer layers first, the first time BFS reaches any node is guaranteed to be the shortest path!

### Topological Sort on a DAG
When ML pipeline steps have prerequisites (`clean` before `train`, `train` before `eval`), Kahn's algorithm counts each step's remaining prerequisites (`in_degree`), runs `0`-prerequisite steps first, and unlocks downstream steps one by one.


### 4. Practical Example — Shortest Hops Function

```python
from collections import deque

def shortest_hops(graph: dict[str, list[str]], start: str, goal: str) -> int:
    q = deque([(start, 0)])
    seen = {start}
    while q:
        node, dist = q.popleft()
        if node == goal:
            return dist
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, dist + 1))
    return -1
```

### Common Mistakes to Avoid

- Forgetting `seen` in BFS -> infinite loop on cyclic graphs.
- Using `list.pop(0)` instead of `deque.popleft()`.

**Key Takeaway:** Use `deque` for queues/BFS, `heapq` for Top-K, and `seen` sets to avoid revisiting nodes.


---

## 6.2 DAG Topological Sort (Ordering Dependent Tasks)

> **Before You Start:** If Task B needs Task A to finish first, you cannot just sort alphabetically—you need a **dependency order**.

### 1. Definition
**Topological Sort (Kahn's Algorithm)** orders tasks in a Directed Acyclic Graph (DAG) so every prerequisite finishes before tasks that depend on it—and detects circular deadlocks (`A -> B -> A`).

### 2. Exact Syntax — Kahn's Algorithm (3 Steps)
```python
# 1. Count prerequisites (in-degree) and build outgoing `adj` list:
adj = {t: [] for t in tasks}
indeg = {t: 0 for t in tasks}
for src, dst in deps:
    adj[src].append(dst)
    indeg[dst] += 1

# 2. Start with tasks having 0 prerequisites (min-heap for alphabetical tie-break):
heap = [t for t in tasks if indeg[t] == 0]
heapq.heapify(heap)
```

- `indeg[t]` = how many unfinished prerequisites task `t` is waiting on.
- Pop a ready task from `heap`, append to `order`, and subtract `1` from each dependent task's `indeg`. When any dependent hits `0`, push it onto `heap`!
- At the end, if `len(order) != len(tasks)`, there was a **cycle** (deadlock)!

### 3. Tiny Example (Line-by-Line) — Scheduling `clean -> train -> eval`
```python
import heapq

def schedule(tasks, deps):
    adj = {t: [] for t in tasks}
    indeg = {t: 0 for t in tasks}
    for a, b in deps:
        adj[a].append(b)
        indeg[b] += 1
    heap = [t for t in tasks if indeg[t] == 0]
    heapq.heapify(heap)
    order = []
    while heap:
        cur = heapq.heappop(heap)
        order.append(cur)
        for nxt in adj[cur]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                heapq.heappush(heap, nxt)
    return order

print(schedule(['eval', 'clean', 'train'], [('clean', 'train'), ('train', 'eval')]))
```

1. `clean` has `indeg=0`, so it pops first.
2. Finishing `clean` drops `train`'s `indeg` from `1` to `0` -> pushes `train`.
3. Finishing `train` unlocks `eval` -> returns `['clean', 'train', 'eval']`!

### Detecting Circular Dependencies
If `A` waits for `B` and `B` waits for `A`, neither ever reaches `indeg == 0`—so `len(order) < len(tasks)` catches the cycle immediately (`raise ValueError('Cycle detected')`).


### 4. Practical Example — Cycle Detection Guard

```python
# After the while heap loop finishes:
# if len(order) != len(tasks):
#     raise ValueError('Cycle detected')
print('If len(order) == len(tasks), the DAG is valid!')
```

### Common Mistakes to Avoid

- Forgetting `heapq.heapify(heap)` before `heappop(heap)` (leaves list unsorted!).

**Key Takeaway:** Kahn's algorithm tracks `in_degree`, runs `0`-prerequisite tasks via `heapq`, and catches cycles via `len(order) != len(tasks)`.


---

## 6.3 Dynamic Programming Demystified (1D Lists & 2D Grids)

> **Before You Start:** Dynamic Programming is NOT a scary trick. It literally means: **save sub-answers so you never calculate the exact same thing twice**.

### 1. Definition
**Dynamic Programming (DP)** takes a recursive problem where the same smaller calls repeat over and over, and caches each answer once in a `memo` dict or `dp` list.

### 2. Exact Syntax — From Slow Recursion -> Fast Memo -> Simple Loop Table
```python
# 1. Memoized Recursion (Top-Down):
memo = {}
def ways(n):
    if n <= 1: return 1
    if n in memo: return memo[n]
    memo[n] = ways(n - 1) + ways(n - 2)
    return memo[n]

# 2. Bottom-Up Table (Loop):
dp = [1] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
```

- Without `memo`, `ways(50)` repeats billions of calls and freezes for hours.
- With `memo` or `dp`, each step `0..50` is computed **once** (50 additions -> finishes in 0.0001s!).

### 3. Tiny Example (Line-by-Line) — Climbing 4 Stairs (1 or 2 Steps at a Time)
```python
dp = [1, 1, 0, 0, 0]
for i in range(2, 5):
    dp[i] = dp[i - 1] + dp[i - 2]
    print(f'Step {i}: {dp[i]} ways')
print('Full table:', dp)
```

1. Base cases: 1 way at step 0 (`dp[0]=1`), 1 way to reach step 1 (`dp[1]=1`).
2. To reach step 2, you came from step 1 or step 0: `1 + 1 = 2`.
3. Step 3: `2 + 1 = 3`. Step 4: `3 + 2 = 5`.

### Building a 2D DP Grid (Edit Distance)
To compare two strings `a` (length `m`) and `b` (length `n`), create a 2D table of size `(m + 1) x (n + 1)` with:
`dp = [[0] * (n + 1) for _ in range(m + 1)]`
*(Never write `[[0] * (n + 1)] * (m + 1)`—that copies the SAME row reference `m + 1` times!)*

**Step through the interactive 2D DP Table below** to watch Edit Distance (`cat` -> `cut`) fill one cell at a time!


### 4. Practical Example — 1D DP: Minimum Coins (Where Greedy Fails)

```python
def min_coins(coins: list[int], amount: int) -> int:
    inf = amount + 1
    dp = [inf] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], 1 + dp[a - c])
    if dp[amount] > amount:
        return -1
    return dp[amount]

print('Min coins for 6 with [1,3,4]:', min_coins([1, 3, 4], 6))  # 2 (3+3)
```

### Common Mistakes to Avoid

- Trying to jump straight to a 2D loop without tracing a tiny `3x3` example on paper first.
- Forgetting base cases (`dp[0]`).

**Key Takeaway:** DP = recursion + cache (or a small loop filling a `dp` array from `0` upward).


---

## Hands-On Project: Autocomplete, DP Spell-Checker & DAG Pipeline Scheduler

Combine Trie autocomplete, 2D DP Levenshtein spell-checking, and Kahn's DAG topological sort.

1. Implement `Trie` prefix lookup.
2. Implement 2D DP `edit_distance(a, b)`.
3. Implement Kahn's topological sort (`schedule_tasks`).
