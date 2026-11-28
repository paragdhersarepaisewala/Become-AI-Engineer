# Workbook — Chapter 1: Python Core Building Blocks (From Scratch)


---

## 1.1 Warm-Up: Loop + Decision + Dictionary Summary (`Foundation` · Python)

Write `grade_summary(scores: list[int]) -> dict[str, int]` returning `{'passed': ..., 'failed': ...}`.
- Score `>= 60` -> `'passed'`
- Score `< 60` -> `'failed'`

### Thinking Blueprint

- Block 1 (Setup): Start with `counts = {'passed': 0, 'failed': 0}`.
- Block 2 (Loop): For each score `s`, increment `'passed'` if `s >= 60` else `'failed'`.
- Block 3 (Return): Return `counts`.

### Progressive Hints

1. Initialize both keys to `0` before the loop.
2. Inside `for s in scores:`, use `if s >= 60:` and `else:`.

### Dry-Run Trace
| Round | `s` | `s >= 60?` | `counts` |
|---|---|---|---|
| 1 | 40 | No | `{'passed': 0, 'failed': 1}` |
| 2 | 60 | Yes | `{'passed': 1, 'failed': 1}` |

### Answer & Explanation
```python
def grade_summary(scores: list[int]) -> dict[str, int]:
    counts = {'passed': 0, 'failed': 0}
    for s in scores:
        if s >= 60:
            counts['passed'] += 1
        else:
            counts['failed'] += 1
    return counts

if __name__ == '__main__':
    print(grade_summary([40, 60, 85, 59]))
```

**High-Level Blocks:** Pre-seed counts, loop once updating the right key, then `return counts`.


---

## 1.2 One-Line Loop (Comprehension): Clean & Filter Names (`Foundation` · Python)

Write `clean_names(names: list[str]) -> list[str]` that strips spaces, lowercases each name, and skips blank/whitespace-only entries using a list comprehension.

### Thinking Blueprint

- Fold `[name.strip().lower() for name in names if name.strip()]`.

### Progressive Hints

1. Filter condition at the end: `if name.strip()` skips `''` and `'   '`.

### Dry-Run Trace
`'  Sara '` -> `'sara'`; `''` -> skipped.

### Answer & Explanation
```python
def clean_names(names: list[str]) -> list[str]:
    return [name.strip().lower() for name in names if name.strip()]

if __name__ == '__main__':
    print(clean_names(['  Sara ', '', ' ALEX ', '   ']))
```

**High-Level Blocks:** `[transform for item in collection if filter]` keeps only non-blank names and normalizes them.


---

## 1.3 Function Basics: Discount Price Calculator (`Foundation` · Python)

Write `apply_discount(price: float, discount_percent: float = 10.0) -> float` subtracting `discount_percent`% from `price` rounded to 2 decimals. Raise `ValueError('Invalid input')` if `price < 0` or `discount_percent < 0` or `discount_percent > 100`.

### Thinking Blueprint

- Validate bad inputs first -> `raise ValueError('Invalid input')`.
- Compute `saved = price * (discount_percent / 100)` and `return round(price - saved, 2)`.

### Progressive Hints

1. Use `return`, NOT `print()`.

### Dry-Run Trace
`apply_discount(100)` -> `90.0`; `apply_discount(80, 25)` -> `60.0`.

### Answer & Explanation
```python
def apply_discount(price: float, discount_percent: float = 10.0) -> float:
    if price < 0 or discount_percent < 0 or discount_percent > 100:
        raise ValueError('Invalid input')
    saved = price * (discount_percent / 100)
    return round(price - saved, 2)

if __name__ == '__main__':
    print(apply_discount(100))
```

**High-Level Blocks:** Validate bad inputs first, compute discount amount, and `return` the rounded float.
