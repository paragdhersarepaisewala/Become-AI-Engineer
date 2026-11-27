"""Starter exercises — implement each function and run pytest on test_problems.py."""


# --- 4.1: DP Foundation: Climbing Stairs (`n = 60`) ---
def climb_ways(n: int) -> int:
    # TODO: O(N) bottom-up DP
    pass


# --- 4.2: 1D DP Choice Pattern: Minimum Coin Change ---
def min_coins(coins: list[int], amount: int) -> int:
    # TODO: 1D DP table
    pass


# --- 4.3: 2D DP Table: Levenshtein Edit Distance ---
def edit_distance(a: str, b: str) -> int:
    # TODO: 2D DP grid
    pass


# --- 4.4: DAG Topological Sort (Pipeline Task Scheduler) ---
import heapq

def schedule_tasks(tasks: list[str], deps: list[tuple[str, str]]) -> list[str]:
    # TODO: Kahn's topological sort + cycle check
    pass
