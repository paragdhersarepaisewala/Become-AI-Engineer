# Chapter 3: Logic Building & Algorithmic Thinking

*How to plan on paper, trace variables in tables, and master core patterns (hash maps, two pointers, sliding window, recursion).*

**Why It Matters:** Struggling with programming logic does NOT mean you are bad at coding—it means you are trying to type Python before figuring out the steps on paper. Here is a repeatable method to turn any problem into clean code.

**Skills Covered:** Paper Tracing, Hash Maps, Two Pointers, Sliding Window, Recursion Stack


---

## 3.1 The 4-Step Logic Blueprint (How to Think Before Coding)

> **Before You Start:** Never start typing code while the problem is still fuzzy in your head. Solve a 4-item example on paper first!

### 1. Definition
A **trace table** tracks what every variable holds after each loop step on a tiny sample input. Whatever your brain has to *remember* while solving the sample by hand becomes your Python variables.

### 2. Exact Syntax — The Sliding Window Pattern (Fixed Size `k`)
```python
window_sum = sum(nums[:k])   # 1. compute first window
best = window_sum
for right in range(k, len(nums)):
    window_sum += nums[right] - nums[right - k]  # 2. slide by +new -old
    best = max(best, window_sum)
```

- Instead of re-summing `k` numbers from scratch on every step, slide the window by adding the 1 entering item (`nums[right]`) and subtracting the 1 leaving item (`nums[right - k]`).
- Notice how `window_sum` and `best` are literally the two numbers your brain keeps track of when scanning left-to-right!

### 3. Tiny Example (Line-by-Line) — Max Sum of 2 Consecutive Numbers in `[2, 5, 1, 8]`
```python
nums = [2, 5, 1, 8]
win = nums[0] + nums[1]  # 7
best = win               # 7
for right in range(2, len(nums)):
    win = win + nums[right] - nums[right - 2]
    best = max(best, win)
print(best)  # 9 (from 1 + 8)
```

1. Start: `win = 2 + 5 = 7`, `best = 7`.
2. `right = 2` (`nums[2] = 1`, leaving `nums[0] = 2`): `win = 7 + 1 - 2 = 6`, `best = max(7, 6) = 7`.
3. `right = 3` (`nums[3] = 8`, leaving `nums[1] = 5`): `win = 6 + 8 - 5 = 9`, `best = max(7, 9) = 9`.

### Your 4-Step Checklist for Any New Problem
1. **Restate & Edge Cases:** What if the list is empty `[]`? What if `k` is bigger than `len(nums)`?
2. **Solve by Hand on 4 Items:** Write down a small table of each step.
3. **Pick the Pattern:** Counting/Lookup -> `dict`; Sorted pairs -> Two Pointers; Subarray/Substring -> Sliding Window.
4. **Write Block-by-Block:** Guard check -> initial state -> loop -> return.


### 4. Practical Example — Guarded Sliding Window Function

```python
def max_window_sum(nums: list[int], k: int) -> int:
    # Block 1 (Guard): fail clearly if window size is impossible
    if k <= 0 or k > len(nums):
        raise ValueError('Invalid window size')
    # Block 2 (Initial Window)
    win = sum(nums[:k])
    best = win
    # Block 3 (Slide across remaining elements)
    for right in range(k, len(nums)):
        win += nums[right] - nums[right - k]
        best = max(best, win)
    return best
```

### Common Mistakes to Avoid

- Off-by-one errors in `nums[right - k]` (always verify on `right = k` -> `k - k = 0`, the very first item!).
- Forgetting to check `k > len(nums)` before slicing.

**Key Takeaway:** Always solve a 4-item example on paper first—the numbers you keep track of become your variables.


---

## 3.2 Hash Maps, Two Pointers & Recursion

> **Before You Start:** If you ever catch yourself writing a loop inside another loop just to look something up, pause—there's almost always a faster 1-loop pattern.

### 1. Definition
- **Hash Map (`dict`):** Remembers what you already saw so checking 'have I seen X?' takes 1 step instead of scanning the whole list.
- **Two Pointers:** Two index variables (`left` and `right`) walking toward each other or in tandem.
- **Recursion:** A function that solves a big input by calling itself on a **smaller** input until hitting a **base case**.

### 2. Exact Syntax — Two Pointers vs Recursion Structure
```python
# Two Pointers on sorted list
left, right = 0, len(nums) - 1
while left < right:
    # move left += 1 or right -= 1

# Recursion structure (2 mandatory parts)
def solve(x):
    if is_smallest_case(x): return base_answer  # 1. Base Case
    return combine(solve(smaller(x)))           # 2. Recursive Step
```

- In `while left < right:`, at least one pointer MUST move every round so the loop finishes.
- In recursion, **Base Case** stops the calls; **Recursive Step** shrinks the problem strictly closer to the base case.

### 3. Tiny Example (Line-by-Line) — Checking if Two Sorted Numbers Add to Target
```python
nums = [1, 3, 4, 8]
target = 7
left, right = 0, len(nums) - 1
while left < right:
    s = nums[left] + nums[right]
    if s == target: print('Found!', nums[left], nums[right]); break
    elif s < target: left += 1
    else: right -= 1
```

1. Round 1: `1 + 8 = 9 > 7` (too big -> move `right` leftwards to `4`).
2. Round 2: `1 + 4 = 5 < 7` (too small -> move `left` rightwards to `3`).
3. Round 3: `3 + 4 = 7 == 7` -> Found!

**Step through the interactive Call Stack Visualizer below** to watch Python push and pop recursion frames live—no mental guesswork needed!


### 4. Practical Example — Recursive Nested List Sum (Base Case + Recursive Step)

```python
def sum_nested(node: int | list) -> int:
    # Block 1 (Base Case): single integer returns directly
    if isinstance(node, int):
        return node
    # Block 2 (Recursive Step): sum every child item
    total = 0
    for child in node:
        total += sum_nested(child)
    return total
```

### Common Mistakes to Avoid

- Forgetting the Base Case in recursion -> `RecursionError: maximum recursion depth exceeded`.
- Using Two Pointers on an *unsorted* list when the logic assumes sorted order.

**Key Takeaway:** Use `dict` for fast memory lookups, Two Pointers on sorted/symmetric arrays, and always verify your recursive Base Case first.


---

## Hands-On Project: Pure-Python Text Tokenizer & Inverted Index Search Engine

Build a keyword search engine mapping each word to matching document IDs using hash maps.

1. Write `tokenize(text)` normalizing lowercase words.
2. Build `InvertedIndex` class mapping `word -> set of doc_ids`.
3. Implement ranked `AND` / `OR` queries + `pytest`.
