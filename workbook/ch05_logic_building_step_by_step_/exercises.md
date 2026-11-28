# Workbook — Chapter 5: Logic Building Step-by-Step (Think Before You Code)


---

## 5.1 Basic Logic: Find Largest Number Manually (No `max()`) (`Foundation` · Logic)

Write `find_max(nums: list[int])` returning `None` if empty, else the largest int (must handle `[-10, -3, -20] -> -3`).

### Thinking Blueprint

- Start `best = nums[0]` (not `0`!) after guarding `if not nums:`.

### Progressive Hints

1. Loop `for n in nums[1:]:` and update `if n > best: best = n`.

### Dry-Run Trace
`[-10, -3, -20]` -> `-3`.

### Answer & Explanation
```python
def find_max(nums: list[int]):
    if not nums:
        return None
    best = nums[0]
    for n in nums[1:]:
        if n > best:
            best = n
    return best

if __name__ == '__main__':
    print(find_max([-10, -3, -20]))
```

**High-Level Blocks:** Guard empty list, anchor `best` at `nums[0]`, scan once.


---

## 5.2 Grouping Logic: Group Words by First Letter (`Foundation` · Logic)

Write `group_by_first_letter(words: list[str]) -> dict[str, list[str]]` skipping blanks.

### Thinking Blueprint

- Strip word; if empty `continue`; initialize `groups[key] = []` if missing; append.

### Progressive Hints

1. `key = w[0].lower()`

### Dry-Run Trace
`['Apple', '  ', 'ant', 'Ball']` -> `{'a': ['Apple', 'ant'], 'b': ['Ball']}`.

### Answer & Explanation
```python
def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for raw in words:
        w = raw.strip()
        if not w:
            continue
        key = w[0].lower()
        if key not in groups:
            groups[key] = []
        groups[key].append(w)
    return groups
```

**High-Level Blocks:** Clean & skip blanks first, create missing buckets, then append.


---

## 5.3 State Machine Logic: Run-Length Encoder (`Foundation` · Logic)

Write `compress_runs(text: str) -> str` turning `'aaabbc'` -> `'a3b2c1'`.

### Thinking Blueprint

- Track `current` and `count`, flush on change, and flush once after the loop.

### Progressive Hints

1. Guard `if not text: return ''`.

### Dry-Run Trace
`'aab'` -> `'a2b1'`.

### Answer & Explanation
```python
def compress_runs(text: str) -> str:
    if not text:
        return ''
    parts: list[str] = []
    current = text[0]
    count = 1
    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            parts.append(f'{current}{count}')
            current = ch
            count = 1
    parts.append(f'{current}{count}')
    return ''.join(parts)
```

**High-Level Blocks:** Track streak state and flush the final group after the loop.


---

## 5.4 Sliding Window: Longest Unique Substring (`Intermediate` · Logic)

Write `longest_unique_len(s: str) -> int` returning longest substring length with all distinct chars.

### Thinking Blueprint

- Jump `left = last_seen[ch] + 1` when `last_seen[ch] >= left`.

### Progressive Hints

1. Never move `left` backwards.

### Dry-Run Trace
`'pwwkew'` -> `3` (`'wke'`).

### Answer & Explanation
```python
def longest_unique_len(s: str) -> int:
    last_seen: dict[str, int] = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best
```

**High-Level Blocks:** Duplicate-free invariant in O(N).
