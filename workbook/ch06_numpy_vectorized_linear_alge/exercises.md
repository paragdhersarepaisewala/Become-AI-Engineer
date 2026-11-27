# Workbook — Chapter 6: NumPy & Vectorized Linear Algebra


---

## 6.1 Vectorized Standardization (Broadcasting + `axis`) (`Foundation` · NumPy)

Write `standardize_columns(x: np.ndarray) -> np.ndarray` for shape `(N, D)` subtracting column means and dividing by column stds (replace zero std with `1.0`).

### Thinking Blueprint

- Compute column stats with `axis=0, keepdims=True` -> shape `(1, D)`.
- Guard constant columns with `np.where(std == 0, 1.0, std)`.

### Progressive Hints

1. `keepdims=True` makes `(1, D)` broadcast across `(N, D)` cleanly even when `N == D`.

### Dry-Run Trace
`[[1, 5], [3, 5]]` -> `mean=[[2, 5]], safe_std=[[1, 1]]` -> `[[-1, 0], [1, 0]]`.

### Answer & Explanation
```python
import numpy as np

def standardize_columns(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    mean = x.mean(axis=0, keepdims=True)
    std = x.std(axis=0, keepdims=True)
    safe_std = np.where(std == 0, 1.0, std)
    return (x - mean) / safe_std
```

**High-Level Blocks:** (1) Column reduction with `keepdims=True`; (2) Zero-division guard via `np.where`; (3) Broadcasted subtraction & division.


---

## 6.2 Numerically Stable Softmax (`Intermediate` · NumPy)

Write `stable_softmax(logits: np.ndarray) -> np.ndarray` working for both 1D `(C,)` and 2D `(B, C)` inputs.

### Thinking Blueprint

- Subtract `np.max(logits, axis=-1, keepdims=True)` first.
- Exponentiate and divide by `np.sum(..., axis=-1, keepdims=True)`.

### Progressive Hints

1. `axis=-1` always targets the last axis regardless of 1D/2D/3D shape.

### Dry-Run Trace
`[1000.0, 1000.0]` -> shift by `1000.0` -> `[0.0, 0.0]` -> `[0.5, 0.5]`.

### Answer & Explanation
```python
import numpy as np

def stable_softmax(logits: np.ndarray) -> np.ndarray:
    logits = np.asarray(logits, dtype=float)
    shifted = logits - np.max(logits, axis=-1, keepdims=True)
    exps = np.exp(shifted)
    return exps / np.sum(exps, axis=-1, keepdims=True)
```

**High-Level Blocks:** Shifting by max keeps all exponents `<= 0`, preventing `inf` while preserving exact mathematical probabilities.


---

## 6.3 Cosine Top-K Vector Retrieval (`Intermediate` · NumPy)

Write `cosine_top_k(docs: np.ndarray, query: np.ndarray, k: int) -> list[int]` returning top-`k` indices descending.

### Thinking Blueprint

- L2-normalize rows of `docs` and vector `query`.
- Dot product `docs_unit @ query_unit` computes all cosine scores at once.

### Progressive Hints

1. Guard zero vectors with `np.maximum(norms, 1e-12)`.

### Dry-Run Trace
`docs=[[1,0],[0,1],[1,1]]`, `query=[2,0]` -> sims `[1.0, 0.0, 0.707]` -> top 2 `[0, 2]`.

### Answer & Explanation
```python
import numpy as np

def cosine_top_k(docs: np.ndarray, query: np.ndarray, k: int) -> list[int]:
    if k <= 0 or len(docs) == 0:
        return []
    docs = np.asarray(docs, dtype=float)
    query = np.asarray(query, dtype=float)
    doc_norms = np.maximum(np.linalg.norm(docs, axis=1, keepdims=True), 1e-12)
    q_norm = max(float(np.linalg.norm(query)), 1e-12)
    sims = (docs / doc_norms) @ (query / q_norm)
    return np.argsort(sims)[::-1][:k].tolist()
```

**High-Level Blocks:** (1) Guard empty/`k<=0`; (2) Unit-normalize docs & query; (3) Matrix-vector dot product + descending argsort.
