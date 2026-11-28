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
| 3 | 85 | Yes | `{'passed': 2, 'failed': 1}` |
| 4 | 59 | No | `{'passed': 2, 'failed': 2}` |

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

**Example:** `['  Sara ', '', ' ALEX ', '   ']` -> `['sara', 'alex']`.

### Thinking Blueprint

- Start with a 4-line loop mentally: `if name.strip(): out.append(name.strip().lower())`.
- Fold onto 1 line: `[name.strip().lower() for name in names if name.strip()]`.

### Progressive Hints

1. Filter condition at the end: `if name.strip()` skips `''` and `'   '`.
2. Output expression at the front: `name.strip().lower()`.

### Dry-Run Trace
`'  Sara '` -> `'Sara'` (truthy -> keep `'sara'`); `''` -> `''` (falsy -> skip).

### Answer & Explanation
```python
def clean_names(names: list[str]) -> list[str]:
    return [name.strip().lower() for name in names if name.strip()]

if __name__ == '__main__':
    print(clean_names(['  Sara ', '', ' ALEX ', '   ']))
```

**High-Level Blocks:** `[transform for item in collection if filter]` keeps only non-blank names and normalizes them.


---

## 1.3 Safe Functions: Fix the Shared Default List Bug (`Foundation` · Python)

Write `add_tag(tag: str, tags: list[str] | None = None) -> list[str]` returning a new list with `tag` added if not already present, without mutating `tags`.

### Thinking Blueprint

- If `tags is None`, start with `[]`, else `tags.copy()`.
- Append `tag` only if `tag not in result`.

### Progressive Hints

1. `result = [] if tags is None else list(tags)`

### Dry-Run Trace
`add_tag('a')` -> `['a']`; `add_tag('b')` -> `['b']`; `add_tag('ml', base)` leaves `base` untouched.

### Answer & Explanation
```python
def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    result = [] if tags is None else list(tags)
    if tag not in result:
        result.append(tag)
    return result

if __name__ == '__main__':
    print(add_tag('python'))
```

**High-Level Blocks:** `None` sentinel ensures fresh lists on omitted args; `list(tags)` protects caller lists.
