# Workbook — Chapter 10: Docker & Reproducible AI Environments


---

## 10.1 Dockerfile Layer-Cache & Security Linter (`Foundation` · Docker)

Write `audit_dockerfile(lines: list[str]) -> list[str]` returning `'PIN_BASE_IMAGE'`, `'CACHE_BUST_ORDER'`, and `'USE_NO_CACHE_PIP'` warnings.

### Thinking Blueprint

- Track index of first `COPY .` and first `pip install` while inspecting `FROM` and pip flags.

### Progressive Hints

1. Normalize spaces using `' '.join(raw.strip().split())`.

### Dry-Run Trace
`['FROM python:latest', 'COPY . .', 'RUN pip install -r req.txt']` -> all 3 warnings.

### Answer & Explanation
```python
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
```

**High-Level Blocks:** (1) Single-pass state tracker records key line indices; (2) Post-loop comparison checks layer order.


---

## 10.2 Compose Startup Order via Dependency Graph (`Intermediate` · Docker)

Given `services: dict[str, list[str]]` (`service -> depends_on list`), return a valid startup order with alphabetical tie-breaking.

### Thinking Blueprint

- Flip edges: if `gateway` depends on `redis`, `redis -> gateway`!
- Run Kahn's topological sort with `heapq`.

### Progressive Hints

1. `indeg[svc]` equals `len(deps)`.

### Dry-Run Trace
`redis` starts first -> unlocks `worker` -> unlocks `gateway`.

### Answer & Explanation
```python
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
```

**High-Level Blocks:** Reuses Chapter 4's exact Kahn's algorithm—showing how DSA directly powers container orchestration.
