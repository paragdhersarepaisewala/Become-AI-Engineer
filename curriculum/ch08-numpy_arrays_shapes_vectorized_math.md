# Chapter 8: NumPy — Arrays, Shapes & Vectorized Math

*Arrays vs Python lists, .shape, axis=0 vs axis=1, broadcasting rules, dot products (@), cosine similarity, and stable softmax.*

**Why It Matters:** PyTorch tensors and Transformer attention layers work almost identically to NumPy arrays. Mastering `.shape`, `axis`, and broadcasting here makes deep learning code easy to read.

**Skills Covered:** NumPy, np.array & .shape, axis=0 vs axis=1, Broadcasting, Dot Product (@), Softmax


---

## 8.1 NumPy Arrays, `.shape` & `axis` (Replacing Slow Loops)

> **Before You Start:** If `axis=0` vs `axis=1` always confused you, remember: `axis` tells NumPy **which direction to collapse**.

### 1. Definition
A **NumPy array (`ndarray`)** stores numbers in one packed block of C memory so math runs across whole rows/columns at once—often 50x faster than a Python `for` loop.

### 2. Exact Syntax — Creating Arrays, Checking Shape & Collapsing Axes
```python
import numpy as np

a = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
a.shape               # (2, 3) -> 2 rows, 3 columns
a.sum(axis=0)         # [5., 7., 9.]  (collapses rows -> 1 per column)
a.sum(axis=1)         # [6., 15.]     (collapses cols -> 1 per row)
a.sum(axis=1, keepdims=True)  # shape (2, 1)
```

- `.shape` returns `(rows, cols)` for 2D arrays.
- `axis=0` collapses axis 0 (rows); `axis=1` collapses axis 1 (columns).
- `keepdims=True` keeps the collapsed axis as size `1` so division aligns cleanly!

### 3. Tiny Example (Line-by-Line) — Doubling Numbers Without a `for` Loop
```python
import numpy as np
prices = np.array([10, 20, 30])
print(prices * 2)
```

1. `prices` is a 1D array of shape `(3,)`.
2. `prices * 2` multiplies every number in C memory at once -> `[20 40 60]`.

### Broadcasting & Dot Product (`@`)
- **Broadcasting:** Compares two shapes **right-to-left**. Dimensions match if they are **equal** OR **one of them is `1`**.
- **Matrix Multiply (`A @ B`):** Multiplies matching dimensions and sums them—used everywhere in embeddings and neural layers.

**Test shapes live** in the NumPy Broadcasting Explorer below!


### 4. Practical Example — Stable Softmax & Cosine Top-K Search

```python
import numpy as np

def softmax(logits: np.ndarray) -> np.ndarray:
    shifted = logits - np.max(logits, axis=-1, keepdims=True)
    exps = np.exp(shifted)
    return exps / np.sum(exps, axis=-1, keepdims=True)

print(softmax(np.array([2.0, 1.0, 0.1])))
```

### Common Mistakes to Avoid

- Forgetting `keepdims=True` before dividing `(N, D)` by `(N,)`.
- Using `*` instead of `@` when you want matrix multiplication.

**Key Takeaway:** Print `.shape` whenever confused, pass `keepdims=True` when normalizing rows/columns, and read broadcasting right-to-left.


---

## Hands-On Project: Pure-NumPy Semantic Vector Search Engine

Implement L2 normalization, stable softmax, and top-K cosine similarity retrieval in pure NumPy.

1. Implement vectorized L2 row normalization.
2. Implement batched cosine similarity and top-K ranking.
3. Verify speed & accuracy with `pytest`.
