"""Starter exercises — implement each function and run pytest on test_problems.py."""


# --- 10.1: Dockerfile Layer-Cache & Security Linter ---
def audit_dockerfile(lines: list[str]) -> list[str]:
    # TODO: audit FROM tag, COPY order, and pip --no-cache-dir
    pass


# --- 10.2: Compose Startup Order via Dependency Graph ---
import heapq

def compose_startup_order(services: dict[str, list[str]]) -> list[str]:
    # TODO: topological sort over depends_on
    pass
