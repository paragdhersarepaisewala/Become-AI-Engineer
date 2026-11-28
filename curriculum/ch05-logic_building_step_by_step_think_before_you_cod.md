# Chapter 5: Logic Building Step-by-Step (Think Before You Code)

*Paper dry-runs, accumulators (manual max/min/sum), filtering, grouping, nested loops, and gentle transition to faster patterns.*

**Why It Matters:** Jumping straight into LeetCode or DSA when you still hesitate on basic loop logic causes frustration. Here we build raw problem-solving logic slowly on everyday problems first—so DSA feels easy later.

**Skills Covered:** Paper Dry-Run, Manual Max/Min, Filter & Transform, Grouping Dicts, Nested Loops, Speeding Up Logic


---

## 5.1 How a Human Solves a Problem (Paper Dry-Run -> Variables)

> **Before You Start:** If you stare at a blank editor not knowing which line to type first, STOP typing and walk 4 items on paper first.

### 1. Definition
**Logic building** is simply noticing what small pieces of information your brain keeps track of while solving a 4-item example by hand—and turning each piece into a Python variable.

### 2. Exact Syntax — The 4-Step Human Thinking Checklist
```python
# Step 1: What goes IN and what comes OUT? (check empty list [] too!)
# Step 2: Walk a tiny example [4, 9, 2, 7] by hand.
# Step 3: Ask: 'What did my brain have to remember at each step?'
# Step 4: Turn that memory into variables + a loop!
```

- Example: *'Find the biggest number in `[4, 9, 2, 7]` without calling `max()`.'*
- Your eyes scan left-to-right. All your brain remembers is **1 number**: `'biggest I saw so far'`!
- Start `best = nums[0]` (`4`), compare each next item: if `n > best`, update `best = n`!

### 3. Tiny Example (Line-by-Line) — Finding Maximum Manually (Tracing Every Round)
```python
nums = [4, 9, 2, 7]
best = nums[0]
for n in nums:
    if n > best:
        best = n
print('Biggest:', best)
```

1. Start: `best = 4`.
2. Round 1 (`n=4`): `4 > 4` False -> `best` stays `4`.
3. Round 2 (`n=9`): `9 > 4` True -> `best` becomes `9`.
4. Round 3 (`n=2`): `2 > 9` False -> `best` stays `9`.
5. Round 4 (`n=7`): `7 > 9` False -> `best` stays `9` -> prints `9`!

### Why Not `best = 0`?
Always test negative numbers! If `nums = [-10, -3, -20]` and you started with `best = 0`, `best` would stay `0` (wrong—`0` isn't even in the list!). Starting at `best = nums[0]` (after guarding `if not nums:`) works for positive AND negative numbers!


### 4. Practical Example — Guarded Manual Min & Max Together

```python
def min_and_max(nums: list[int]):
    # Block 1 (Guard): empty list has no min or max
    if not nums:
        return None
    # Block 2: Remember smallest and largest seen so far
    low = nums[0]
    high = nums[0]
    for n in nums[1:]:
        if n < low:
            low = n
        if n > high:
            high = n
    return (low, high)

print(min_and_max([-10, -3, -20]))  # (-20, -3)
```

### Common Mistakes to Avoid

- Initializing `best = 0` instead of `nums[0]` (fails when all inputs are negative!).
- Forgetting to check `if not nums:` before accessing `nums[0]` (crashes with `IndexError` on `[]`).

**Key Takeaway:** Solve 4 items with your finger first; the things your brain remembers become your initial variables.


---

## 5.2 Everyday Loop Logic: Filtering, Building, Reversing & Checking

> **Before You Start:** Before touching algorithms, get super comfortable building new lists, checking flags (`all` / `any`), and tracking streaks.

### 1. Definition
Most everyday programming tasks fall into 4 simple patterns: **Filter** (keep some items), **Transform** (change every item), **All/Any Flag** (does every item pass?), and **Streak State** (what happened right before this item?).

### 2. Exact Syntax — Flag Logic (`all` vs `any`) & State Variable
```python
# Pattern A: Does ANY item fail? (start True, flip False on first failure)
all_positive = True
for n in nums:
    if n <= 0:
        all_positive = False
        break

# Pattern B: Streak state (remember previous item)
prev = text[0]
count = 1
```

- Never write `else: all_positive = True` inside the loop—one good item at the end would erase an earlier failure!
- `break` exits immediately once you already know the answer.

### 3. Tiny Example (Line-by-Line) — Reversing a List Manually (No `.reverse()` Shortcut)
```python
items = ['a', 'b', 'c']
reversed_items = []
for i in range(len(items) - 1, -1, -1):
    reversed_items.append(items[i])
print(reversed_items)
```

1. `range(2, -1, -1)` counts backwards: `2, 1, 0` (stops before `-1`).
2. Appends `items[2]` (`'c'`), `items[1]` (`'b'`), `items[0]` (`'a'`).
3. Prints `['c', 'b', 'a']`.

### Streak Logic: Run-Length Compression (`'aaabbc' -> 'a3b2c1'`)
Walk left-to-right holding two variables: `current` char and `count`. When the next char matches, `count += 1`. When it changes, save `f'{current}{count}'` and reset! Don't forget to save the final streak after the loop ends.


### 4. Practical Example — Run-Length String Compressor

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
    parts.append(f'{current}{count}')  # flush the final group!
    return ''.join(parts)

print(compress_runs('aaabbc'))  # 'a3b2c1'
```

### Common Mistakes to Avoid

- Adding `else: flag = True` inside an all-check loop (overwrites an earlier `False`!).
- Forgetting to flush the final group after a streak loop finishes.

**Key Takeaway:** Keep flag checks one-way (`True -> False` on failure + `break`), and always check what happens after the last loop item.


---

## 5.3 Grouping, Nested Loops (2D) & Breaking Problems Into Helpers

> **Before You Start:** If a problem feels big, don't write one 40-line tangled loop—split it into two tiny, obvious steps.

### 1. Definition
- **Nested loop:** A loop inside another loop—the inner loop runs completely for *each* round of the outer loop.
- **Decomposition:** Splitting a tricky task into 2 small helper functions where each helper is easy to trace.

### 2. Exact Syntax — Nested Loop Pairs & Grouping Pattern
```python
# Print all unique pairs (i < j avoids checking (a,b) AND (b,a)):
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        print(items[i], items[j])

# Grouping items into a dict of lists:
groups = {}
for word in words:
    first_letter = word[0]
    if first_letter not in groups:
        groups[first_letter] = []
    groups[first_letter].append(word)
```

- `j` starts at `i + 1` so an item never pairs with itself and pairs aren't repeated backwards.
- In grouping, we initialize `groups[key] = []` the first time we see `key`, then `.append()`.

### 3. Tiny Example (Line-by-Line) — Grouping Words by Length
```python
words = ['ai', 'cat', 'ml', 'code']
by_len = {}
for w in words:
    n = len(w)
    if n not in by_len:
        by_len[n] = []
    by_len[n].append(w)
print(by_len)
```

1. `'ai'` (len 2): creates `by_len[2] = ['ai']`.
2. `'cat'` (len 3): creates `by_len[3] = ['cat']`.
3. `'ml'` (len 2): `2` already exists -> appends `'ml'` -> `{2: ['ai', 'ml'], 3: ['cat'], 4: ['code']}`.

### Breaking a 2-Step Problem Into 2 Small Functions
Suppose you need: *'Find the word that appears most often in a paragraph, ignoring punctuation.'*
1. Helper 1: `clean_words(text)` -> lowercase & strip punctuation.
2. Helper 2: `count_words(words)` -> dict of counts, then loop over dict to find the highest count!


### 4. Practical Example — Two-Step Most Frequent Word (Zero Magic)

```python
def most_common_word(text: str) -> str:
    # Step 1: Count every word in a dict
    counts: dict[str, int] = {}
    for w in text.lower().split():
        counts[w] = counts.get(w, 0) + 1

    # Step 2: Manual max over (word, count) pairs
    best_word = ''
    best_count = 0
    for word, cnt in counts.items():
        if cnt > best_count:
            best_word = word
            best_count = cnt
    return best_word

print(most_common_word('AI helps build AI tools'))  # 'ai'
```

### Common Mistakes to Avoid

- Trying to do Step 1 and Step 2 inside one confusing loop when two simple loops back-to-back are crystal clear and still fast!

**Key Takeaway:** Two simple loops in sequence are way easier to write and debug than one tangled loop. Split big logic into small steps.


---

## 5.4 Leveling Up: Hash Map Lookups, Two Pointers, Sliding Window & Gentle Recursion

> **Before You Start:** Now that basic loops and dicts feel solid, let's see why certain patterns make slow nested loops 1,000x faster.

### 1. Definition
- **Hash Map Lookup (`seen`):** Remembering past items in a `dict`/`set` so you don't re-scan the whole list.
- **Two Pointers (`left`, `right`):** Two indexes walking inward on sorted data.
- **Sliding Window:** Updating a moving slice by `+new -old` instead of re-summing.
- **Recursion:** A function calling itself on a smaller piece until hitting a stopping **base case**.

### 2. Exact Syntax — Replacing a Slow Nested Loop With a `seen` Dictionary
```python
# Find two numbers adding to target:
seen = {}  # value -> index
for i, x in enumerate(nums):
    need = target - x
    if need in seen:
        return (seen[need], i)
    seen[x] = i
```

- `enumerate(nums)` gives `(index, value)` together so you don't need `range(len(nums))`.
- Instead of looping over all earlier elements to find `target - x`, `if need in seen:` checks the dictionary in **1 instant step**!

### 3. Tiny Example (Line-by-Line) — Gentle Recursion: Countdown & Sum
```python
def sum_list(nums: list[int]) -> int:
    if not nums:            # 1. Base case: empty list sums to 0
        return 0
    return nums[0] + sum_list(nums[1:])  # 2. First item + sum of rest

print(sum_list([3, 5, 2]))
```

1. `sum_list([3, 5, 2])` asks for `3 + sum_list([5, 2])`.
2. `sum_list([5, 2])` asks for `5 + sum_list([2])`.
3. `sum_list([2])` asks for `2 + sum_list([])`.
4. `sum_list([])` hits the Base Case and returns `0`, then everything unwinds: `2+0=2`, `5+2=7`, `3+7=10`!

### Two Quick Helpers You'll Use Often: Slicing & `''.join()`
- **Slicing:** `nums[1:]` means *'everything from index 1 to the end'* (skips `nums[0]`); `nums[:k]` means *'the first `k` items'*.
- **`''.join(parts)`:** Glues a list of strings like `['a3', 'b2']` into `'a3b2'` cleanly.
- **Variable Sliding Window:** For `'longest substring without repeats'`, jump `left = last_seen[ch] + 1` whenever `ch` was already seen inside `[left..right]` (`last_seen[ch] >= left`)!

**Step through the interactive Call Stack Visualizer below** to watch recursive frames stack up and return one by one!


### 4. Practical Example — Two Pointers & Sliding Window Side-by-Side

```python
# Block 1: Two Pointers (checks if sorted list has two numbers summing to target)
def has_pair_sorted(nums: list[int], target: int) -> bool:
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return True
        if s < target:
            left += 1
        else:
            right -= 1
    return False

# Block 2: Fixed Sliding Window (max sum of k consecutive numbers)
def max_window_sum(nums: list[int], k: int) -> int:
    win = sum(nums[:k])
    best = win
    for right in range(k, len(nums)):
        win += nums[right] - nums[right - k]
        best = max(best, win)
    return best
```

### Common Mistakes to Avoid

- Trying to use Two Pointers on an *unsorted* list when the logic assumes sorted order.
- Writing recursion without a reachable base case (`RecursionError`).

**Key Takeaway:** Reach for `seen` dicts, Two Pointers, and Sliding Windows whenever a nested loop feels repetitive.


---

## Hands-On Project: Pure-Python Text Tokenizer & Inverted Index Search Engine

Use your logic-building skills (splitting text, counting words, dict grouping) to build a pure-Python keyword search engine.

1. Write `tokenize(text)` normalizing lowercase words.
2. Build `InvertedIndex` mapping `word -> set of doc_ids`.
3. Implement ranked `AND` / `OR` queries + `pytest`.
