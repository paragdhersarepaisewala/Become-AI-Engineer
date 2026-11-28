# Workbook — Chapter 8: NumPy — Arrays, Shapes & Vectorized Math


---

## 8.1 Vectorized Standardization (Broadcasting + `axis`) (`Foundation` · NumPy)

Write `standardize_columns(x: np.ndarray) -> np.ndarray` for `(N, D)` replacing zero std with `1.0`.

### Thinking Blueprint

- Column stats with `axis=0, keepdims=True`.
- Guard zero std with `np.where`.

### Progressive Hints

1. `keepdims=True` makes `(1, D)` broadcast across `(N, D)` cleanly.

### Dry-Run Trace
`[[1, 5], [3, 5]]` -> `[[-1, 0], [1, 0]]`.

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

**High-Level Blocks:** Column reduction (`keepdims=True`), zero-std guard, and broadcasted division.


---

## 8.2 Numerically Stable Softmax (`Intermediate` · NumPy)

Write `stable_softmax(logits: np.ndarray) -> np.ndarray` for 1D or 2D inputs.

### Thinking Blueprint

- Subtract `np.max(..., axis=-1, keepdims=True)` before `np.exp`.

### Progressive Hints

1. `axis=-1` always targets the last dimension.

### Dry-Run Trace
`[1000.0, 1000.0]` -> `[0.5, 0.5]`.

### Answer & Explanation
```python
import numpy as np

def stable_softmax(logits: np.ndarray) -> np.ndarray:
    logits = np.asarray(logits, dtype=float)
    shifted = logits - np.max(logits, axis=-1, keepdims=True)
    exps = np.exp(shifted)
    return exps / np.sum(exps, axis=-1, keepdims=True)
```

**High-Level Blocks:** Max-shift prevents `exp` overflow while leaving probabilities unchanged.


---

## 8.3 Cosine Top-K Vector Retrieval (`Intermediate` · NumPy)

Write `cosine_top_k(docs: np.ndarray, query: np.ndarray, k: int) -> list[int]`.

### Thinking Blueprint

- Unit-normalize rows & query, then `docs_unit @ q_unit`.

### Progressive Hints

1. `np.argsort(sims)[::-1][:k].tolist()`

### Dry-Run Trace
`[[1,0],[0,1],[1,1]]` with `[2,0]` -> `[0, 2]`.

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

**High-Level Blocks:** L2 normalization + matrix-vector dot product + descending argsort.
