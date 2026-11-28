# Chapter 5: Essential DSA & Dynamic Programming Demystified

*Big-O intuition, Queues (deque), Heaps (heapq), Graphs (BFS & DAGs), and Dynamic Programming from recursion to tables.*

**Why It Matters:** Now that your loop & dict logic is strong, DSA gives you specialized tools: `deque` for queues/BFS, `heapq` for Top-K LLM token selection, DAGs for ML pipelines, and Dynamic Programming for sequence alignment & edit distance.

**Skills Covered:** Big-O, Queue (deque), Heap (heapq), Graphs & DAGs, Dynamic Programming


---

## 5.1 Queues (`deque`), Heaps (`heapq`) & Graphs (BFS & DAGs)

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

**Key Takeaway:** Use `deque` for queues/BFS, `heapq` for Top-K, and Kahn's algorithm for dependent tasks.


---

## 5.2 Dynamic Programming Demystified (Recursion -> Memo -> Table)

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
    return -1 if dp[amount] > amount else dp[amount]

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
