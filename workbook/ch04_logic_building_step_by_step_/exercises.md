# Workbook — Chapter 4: Logic Building Step-by-Step (Think Before You Code)


---

## 4.1 Basic Logic: Find Largest Number Manually (No `max()`) (`Foundation` · Logic)

Write `find_max(nums: list[int]) -> int | None` **without calling `max()` or `sorted()`**.
Return `None` if `nums` is empty. Must work for negative numbers like `[-10, -3, -20]` -> `-3`.

### Thinking Blueprint

- Guard `if not nums: return None`.
- Start `best = nums[0]` (NOT `0`!), loop `for n in nums[1:]:`, update if `n > best`.

### Progressive Hints

1. Starting at `0` fails on `[-10, -3, -20]` because `0` is bigger than every item!

### Dry-Run Trace
`[-10, -3, -20]`: `best=-10` -> `-3 > -10` (`best=-3`) -> `-20 > -3` False -> `-3`.

### Answer & Explanation
```python
def find_max(nums: list[int]) -> int | None:
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

**High-Level Blocks:** Guard empty list, anchor `best` at `nums[0]`, and scan left-to-right once.


---

## 4.2 Grouping Logic: Group Words by First Letter (`Foundation` · Logic)

Write `group_by_first_letter(words: list[str]) -> dict[str, list[str]]` that skips empty strings and groups each stripped word under its lowercase first character.

### Thinking Blueprint

- Start `groups: dict[str, list[str]] = {}`.
- For each word: strip it; if empty `continue`; `key = w[0].lower()`; if `key not in groups`: `groups[key] = []`; `groups[key].append(w)`.

### Progressive Hints

1. Initialize `groups[key] = []` the first time you see `key`.

### Dry-Run Trace
`['Apple', 'ant', 'Ball']` -> `{'a': ['Apple', 'ant'], 'b': ['Ball']}`.

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

**High-Level Blocks:** Clean & skip blanks first, then create bucket if missing before appending.


---

## 4.3 State Machine Logic: Run-Length Encoder (`Foundation` · Logic)

Write `compress_runs(text: str) -> str` turning `'aaabbc'` -> `'a3b2c1'`, `'x'` -> `'x1'`, `''` -> `''`.

### Thinking Blueprint

- Track `current` and `count`; flush when char changes and once more after the loop.

### Progressive Hints

1. Guard `if not text: return ''` first.

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

**High-Level Blocks:** Track streak state and remember the final flush after the loop.


---

## 4.4 Sliding Window: Longest Unique Substring (`Intermediate` · Logic)

Write `longest_unique_len(s: str) -> int` returning the longest substring length with all distinct characters.

### Thinking Blueprint

- Jump `left = last_seen[ch] + 1` whenever `ch` repeats inside `[left..right]`.

### Progressive Hints

1. Check `if ch in last_seen and last_seen[ch] >= left:` so `left` never moves backwards.

### Dry-Run Trace
`'pwwkew'` -> `'wke'` length `3`.

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

**High-Level Blocks:** Maintain duplicate-free invariant in one O(N) pass.
