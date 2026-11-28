# Chapter 7: NumPy & Vectorized Linear Algebra

*Arrays, shapes, axes, broadcasting rules, dot products, cosine similarity, and stable softmax.*

**Why It Matters:** PyTorch tensors and Transformer attention layers work almost identically to NumPy arrays. Mastering `.shape`, `axis`, and broadcasting here makes deep learning code easy to read.

**Skills Covered:** np.array & .shape, axis=0 vs axis=1, Broadcasting, Dot Product (@), Softmax


---

## 7.1 NumPy Arrays, `.shape` & `axis` (Replacing Loops)

> **Before You Start:** If `axis=0` vs `axis=1` always confused you, remember: `axis` tells NumPy **which direction to collapse**.

### 1. Definition
A **NumPy array (`ndarray`)** stores numbers in one tightly packed block of C memory so math runs on entire rows/columns at once—often 50x faster than a Python `for` loop.

### 2. Exact Syntax — Creating Arrays, Checking Shape & Collapsing Axes
```python
import numpy as np

a = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
a.shape               # (2, 3) -> 2 rows, 3 columns
a.sum(axis=0)         # [5., 7., 9.]  (collapses rows -> 1 answer per column)
a.sum(axis=1)         # [6., 15.]     (collapses cols -> 1 answer per row)
a.sum(axis=1, keepdims=True)  # shape (2, 1) instead of (2,)
```

- `.shape` returns `(rows, cols)` for 2D matrices.
- `axis=0` collapses axis 0 (rows), leaving `(3,)`.
- `axis=1` collapses axis 1 (columns), leaving `(2,)`.
- `keepdims=True` keeps the collapsed axis as size `1` so you can divide rows by row-sums cleanly!

### 3. Tiny Example (Line-by-Line) — Doubling Numbers Without a `for` Loop
```python
import numpy as np
prices = np.array([10, 20, 30])
doubled = prices * 2
print(doubled)
```

1. `prices` is a 1D array of shape `(3,)`.
2. `prices * 2` multiplies every element in C memory at once -> `[20, 40, 60]`.

### Broadcasting & Dot Product (`@`)
- **Broadcasting:** NumPy compares two shapes **right-to-left**. Dimensions match if they are **equal** OR **one of them is `1`** (missing left axes are treated as `1`).
- **Dot Product / Matrix Multiply (`A @ B`):** Multiplies matching dimensions and sums them—used everywhere in embeddings and neural layers.

**Test shapes live** in the NumPy Broadcasting Explorer below!


### 4. Practical Example — Stable Softmax & Cosine Top-K Search

```python
import numpy as np

# Block 1: Subtract max first so np.exp(1000) never overflows to inf
def softmax(logits: np.ndarray) -> np.ndarray:
    shifted = logits - np.max(logits, axis=-1, keepdims=True)
    exps = np.exp(shifted)
    return exps / np.sum(exps, axis=-1, keepdims=True)

# Block 2: Unit-normalize rows, then dot-product with normalized query
def cosine_top_k(docs: np.ndarray, query: np.ndarray, k: int = 2) -> np.ndarray:
    docs_unit = docs / np.linalg.norm(docs, axis=1, keepdims=True)
    q_unit = query / np.linalg.norm(query)
    sims = docs_unit @ q_unit
    return np.argsort(sims)[::-1][:k]
```

### Common Mistakes to Avoid

- Forgetting `keepdims=True` before dividing `(N, D)` by `(N,)` (shape `(N,)` aligns on the right with `D`, not `N`!).
- Using `*` instead of `@` when you want matrix multiplication (`*` does element-by-element multiplication).

**Key Takeaway:** Print `.shape` whenever confused, pass `keepdims=True` when normalizing rows/columns, and read broadcasting right-to-left.


---

## Hands-On Project: Pure-NumPy Semantic Vector Search Engine

Implement L2 normalization, stable softmax, and top-K cosine similarity retrieval in pure NumPy.

1. Implement vectorized L2 row normalization.
2. Implement batched cosine similarity and top-K ranking.
3. Verify speed & accuracy with `pytest`.
