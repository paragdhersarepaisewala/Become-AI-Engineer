"""Reference solutions with explanations."""


# --- 10.1: Dockerfile Layer-Cache & Security Linter ---
def audit_dockerfile(lines: list[str]) -> list[str]:
    warnings: list[str] = []
    copy_all_idx: int | None = None
    pip_idx: int | None = None
    for idx, raw in enumerate(lines):
        line = ' '.join(raw.strip().split())
        if line.startswith('FROM '):
            image = line.split()[1]
            if ':' not in image or image.endswith(':latest'):
                warnings.append('PIN_BASE_IMAGE')
        if line.startswith('COPY . ') or line.startswith('COPY ./ '):
            if copy_all_idx is None:
                copy_all_idx = idx
        if 'pip install' in line:
            if pip_idx is None:
                pip_idx = idx
            if '--no-cache-dir' not in line and 'USE_NO_CACHE_PIP' not in warnings:
                warnings.append('USE_NO_CACHE_PIP')
    if copy_all_idx is not None and pip_idx is not None and copy_all_idx < pip_idx:
        warnings.append('CACHE_BUST_ORDER')
    return warnings


# --- 10.2: Compose Startup Order via Dependency Graph ---
import heapq

def compose_startup_order(services: dict[str, list[str]]) -> list[str]:
    dependents: dict[str, list[str]] = {s: [] for s in services}
    indeg: dict[str, int] = {s: len(deps) for s, deps in services.items()}
    for svc, deps in services.items():
        for dep in deps:
            dependents[dep].append(svc)
    heap = [s for s, deg in indeg.items() if deg == 0]
    heapq.heapify(heap)
    order: list[str] = []
    while heap:
        cur = heapq.heappop(heap)
        order.append(cur)
        for nxt in dependents[cur]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                heapq.heappush(heap, nxt)
    if len(order) != len(services):
        raise ValueError('Circular depends_on detected')
    return order
