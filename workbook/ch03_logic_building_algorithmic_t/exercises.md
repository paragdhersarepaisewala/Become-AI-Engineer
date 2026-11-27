# Workbook — Chapter 3: Logic Building & Algorithmic Thinking


---

## 3.1 State Machine Logic: Run-Length Encoder (`Foundation` · Logic)

Write `compress_runs(text: str) -> str` turning `'aaabbc'` -> `'a3b2c1'`, `'x'` -> `'x1'`, `''` -> `''`.

### Thinking Blueprint

- Track `current` char and streak `count`.
- Flush when character changes, AND flush the final streak after the loop ends.

### Progressive Hints

1. Guard `if not text: return ''` first.

### Dry-Run Trace
`'aab'` -> `current='a', count=2` -> see `'b'` -> flush `'a2'`, reset `current='b', count=1` -> end loop -> flush `'b1'` -> `'a2b1'`.

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

**High-Level Blocks:** (1) Guard empty input; (2) Track current streak state; (3) Final flush outside the loop handles the last character group.


---

## 3.2 Hash Map Logic: First Unique Character Index (`Foundation` · Logic)

Return the index of the first character in `s` appearing **exactly once**, or `-1` if none.

### Thinking Blueprint

- Pass 1: Count every character with `dict`.
- Pass 2: Find first `(i, ch)` with `counts[ch] == 1`.

### Progressive Hints

1. Use `counts.get(ch, 0) + 1` in pass 1.

### Dry-Run Trace
`'aabc'` -> `counts={'a':2, 'b':1, 'c':1}` -> `i=2 ('b')` has count 1 -> returns `2`.

### Answer & Explanation
```python
def first_unique_index(s: str) -> int:
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
```

**High-Level Blocks:** Pass 1 gathers global knowledge (frequencies); Pass 2 uses that O(1) lookup table in original index order.


---

## 3.3 Dynamic Sliding Window: Longest Unique Substring (`Intermediate` · Logic)

Write `longest_unique_len(s: str) -> int` returning the length of the longest substring with all distinct characters.

### Thinking Blueprint

- Maintain valid window `[left..right]`.
- If `ch` was seen inside the current window (`last_seen[ch] >= left`), jump `left = last_seen[ch] + 1`.

### Progressive Hints

1. Never let `left` move backwards—always check `last_seen[ch] >= left`.

### Dry-Run Trace
`'pwwkew'`: at `right=2 ('w')`, `last_seen['w']=1 >= 0`, so `left` jumps to `2`; window `'wke'` reaches length `3`.

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

**High-Level Blocks:** (1) Window invariant check jumps `left` past duplicates; (2) Record latest index; (3) Update `best` window length.


---

## 3.4 Recursion & Call Stack: Flatten Nested Lists (`Intermediate` · Logic)

Write `flatten(nested: list) -> list[int]` turning `[1, [2, [3, 4]], [], 5]` into `[1, 2, 3, 4, 5]`.

### Thinking Blueprint

- If element is a `list`, recurse and `.extend()`.
- Else (base case), `.append()`.

### Progressive Hints

1. Use `isinstance(item, list)`.

### Dry-Run Trace
`flatten([2, [3, 4]])` calls `flatten([3, 4])` -> `[3, 4]` -> returns `[2, 3, 4]`.

### Answer & Explanation
```python
def flatten(nested: list) -> list[int]:
    out: list[int] = []
    for item in nested:
        if isinstance(item, list):
            out.extend(flatten(item))
        else:
            out.append(item)
    return out
```

**High-Level Blocks:** Each stack frame handles one nesting depth and merges child results cleanly via `.extend()`.
