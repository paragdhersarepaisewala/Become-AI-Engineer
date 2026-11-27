"""Reference solutions with explanations."""


# --- 4.1: DP Foundation: Climbing Stairs (`n = 60`) ---
def climb_ways(n: int) -> int:
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1


# --- 4.2: 1D DP Choice Pattern: Minimum Coin Change ---
def min_coins(coins: list[int], amount: int) -> int:
    inf = amount + 1
    dp = [inf] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return -1 if dp[amount] > amount else dp[amount]


# --- 4.3: 2D DP Table: Levenshtein Edit Distance ---
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


# --- 4.4: DAG Topological Sort (Pipeline Task Scheduler) ---
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
