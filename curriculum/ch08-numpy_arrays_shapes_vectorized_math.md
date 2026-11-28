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

### Helpful Column Stats & Conditional Replacement (`mean`, `std`, `np.where`)
- `x.mean(axis=0, keepdims=True)` and `x.std(axis=0, keepdims=True)` compute column averages & spreads.
- `np.where(std == 0, 1.0, std)` works like an element-by-element `if / else`: wherever `std == 0`, pick `1.0`, otherwise keep `std` (prevents dividing by zero!).
- `np.asarray(x, dtype=float)` cleanly turns a Python list or int array into a float array.


### 4. Practical Example — Column Standardization With `np.where`

```python
import numpy as np

x = np.array([[1.0, 5.0], [3.0, 5.0]])
mean = x.mean(axis=0, keepdims=True)
std = x.std(axis=0, keepdims=True)
safe_std = np.where(std == 0, 1.0, std)  # avoid 0/0 = NaN!
print((x - mean) / safe_std)
```

### Common Mistakes to Avoid

- Forgetting `keepdims=True` before dividing `(N, D)` by `(N,)`.
- Dividing by `std` without `np.where(std == 0, 1.0, std)` on constant columns -> produces `NaN`!

**Key Takeaway:** Print `.shape`, use `keepdims=True`, and guard zero division with `np.where`.


---

## 8.2 Broadcasting, Dot Product (`@`) & Stable Softmax

> **Before You Start:** Broadcasting lets NumPy combine arrays of different shapes without copying data.

### 1. Definition
- **Broadcasting:** Compares two shapes **right-to-left**. Two axes match if they are **equal** OR **one of them is `1`**.
- **Matrix Multiply (`A @ B`):** Multiplies matching dimensions and sums them—used everywhere in embeddings and neural layers.

### 2. Exact Syntax — Dot Product & Numerically Stable Softmax
```python
scores = docs @ query   # dot product along last axis
shifted = logits - np.max(logits, axis=-1, keepdims=True)
probs = np.exp(shifted) / np.sum(np.exp(shifted), axis=-1, keepdims=True)
```

- `axis=-1` always targets the last axis regardless of whether the array is 1D or 2D.
- Subtracting `max(logits)` keeps exponents `<= 0` so `np.exp(1000)` never overflows to `inf`!

### 3. Tiny Example (Line-by-Line) — Row-Wise Softmax
```python
import numpy as np
logits = np.array([2.0, 1.0, 0.1])
shifted = logits - np.max(logits)
probs = np.exp(shifted) / np.sum(np.exp(shifted))
print(probs, '| Sum:', probs.sum())
```

1. Shifts logits so largest becomes `0.0`.
2. Exponentiates and divides by sum -> probabilities summing to `1.0`.

**Test shapes live** in the NumPy Broadcasting Explorer below!


### 4. Practical Example — Pure-NumPy Cosine Similarity Top-K

```python
import numpy as np

docs = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
q = np.array([2.0, 0.0])
docs_unit = docs / np.linalg.norm(docs, axis=1, keepdims=True)
q_unit = q / np.linalg.norm(q)
sims = docs_unit @ q_unit
print('Top-2 indices:', np.argsort(sims)[::-1][:2].tolist())
```

### Common Mistakes to Avoid

- Using `*` instead of `@` when you want matrix multiplication.

**Key Takeaway:** Read broadcasting right-to-left and always subtract max logits before `np.exp()`.


---

## Hands-On Project: Pure-NumPy Semantic Vector Search Engine

Implement L2 normalization, stable softmax, and top-K cosine similarity retrieval in pure NumPy.

1. Implement vectorized L2 row normalization.
2. Implement batched cosine similarity and top-K ranking.
3. Verify speed & accuracy with `pytest`.
