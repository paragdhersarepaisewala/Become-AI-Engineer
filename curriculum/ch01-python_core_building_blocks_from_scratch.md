# Chapter 1: Python Core Building Blocks (From Scratch)

*Variables, types, if/else decisions, for & while loops, lists/dicts/sets, one-line loops (comprehensions), and functions.*

**Why It Matters:** Nothing in AI works without fluent Python basics. Every file automation, dataset cleaner, API server, and model training loop is built out of variables, decisions, loops, lists, dictionaries, and functions.

**Skills Covered:** Variables & Types, if / elif / else, for & while, Lists & Dicts, Comprehensions, Functions


---

## 1.1 Variables, Basic Types & Printing Output

> **Before You Start:** Python runs your script from Line 1 down to the bottom, one instruction at a time.

### 1. Definition
A **variable** is a named label attached to a piece of data so you can reuse or update it later. A **data type** tells Python what kind of data it is: whole number (`int`), decimal (`float`), text (`str`), or True/False (`bool`).

### 2. Exact Syntax — Creating Variables, Converting Types & Printing
```python
name = 'Sara'            # str (text inside quotes)
age = 22                 # int (whole number)
gpa = 3.85               # float (decimal number)
is_enrolled = True       # bool (True or False — capital T/F)

num = int('15')          # converts text '15' -> number 15
print(f'{name} is {age}')  # f-string inserts variables inside {}
```

- `=` means **store the value on the right under the name on the left** (not math equality).
- Anything inside quotes (`'...'` or `"..."`) is text (`str`), even `'15'`.
- An **f-string** (`f'...'`) lets you drop variables straight into `{...}` when printing.

### 3. Tiny Example (Line-by-Line) — Why `'5' + '5'` is `'55'` Instead of `10`
```python
a = '5'
b = '5'
print(a + b)             # glues text together -> '55'
print(int(a) + int(b))   # converts to numbers first -> 10
```

1. Lines 1–2: `'5'` has quotes, so Python treats `a` and `b` as text (`str`).
2. Line 3: `+` on two strings joins them into `'55'`.
3. Line 4: `int(a)` turns `'5'` into the integer `5`, so `5 + 5` prints `10`.

### Checking Any Type When Unsure
Whenever a bug surprises you, run `print(type(x), x)` to see both what Python thinks `x` is (`<class 'str'>` vs `<class 'int'>`) and what value it holds.


### 4. Practical Example — Simple Study Hours Calculator

```python
# Block 1: Store inputs
topic = 'Python'
hours_per_day = 2
days = 6

# Block 2: Compute total
total = hours_per_day * days

# Block 3: Display summary
print(f'Studied {topic} for {total} hours.')
```

### Common Mistakes to Avoid

- Trying to add text and a number directly (`'Age: ' + 20` crashes! Use `f'Age: {20}'`).
- Putting spaces or starting a variable with a number (`my score = 10` is invalid; use `my_score = 10`).

**Key Takeaway:** Use `int()`/`float()` to turn text into numbers before doing math, and `f'...'` strings for clean output.


---

## 1.2 Making Decisions (`if / elif / else`)

> **Before You Start:** Python uses **4 spaces on the left (indentation)** to know which lines run inside an `if` block.

### 1. Definition
An **`if / elif / else` statement** asks a True/False question and chooses which block of code to run.

### 2. Exact Syntax — Decision Tree Syntax
```python
if score >= 80:
    print('Grade A')
elif score >= 60:
    print('Pass')
else:
    print('Try again')
```

- Python checks from top to bottom and runs **only the first branch that is True**.
- Comparisons: `==` (is equal?), `!=` (not equal?), `>`, `<`, `>=`, `<=`.
- Combine checks: `and` (both True), `or` (at least one True), `not` (flips True <-> False).

### 3. Tiny Example (Line-by-Line) — Checking Two Conditions with `and`
```python
has_ticket = True
age = 19
if has_ticket and age >= 18:
    print('Welcome in!')
else:
    print('Entry denied')
```

1. Line 3: Checks BOTH `has_ticket` (`True`) AND `age >= 18` (`19 >= 18` is `True`).
2. Line 4: Since both are `True`, prints `Welcome in!` and skips the `else` block.

### Why `elif` Matters Instead of Multiple `if`s
If you wrote two separate `if` statements (`if score >= 80:` and `if score >= 60:`), a score of `90` would trigger **both**! Using `elif` guarantees at most one branch runs.


### 4. Practical Example — Safe Division Guard

```python
total_points = 450
num_tests = 0

if num_tests == 0:
    print('No tests taken yet.')
else:
    avg = total_points / num_tests
    print(f'Average: {avg}')
```

### Common Mistakes to Avoid

- Writing `if x = 5:` instead of `if x == 5:` (single `=` assigns; double `==` compares).
- Forgetting the colon `:` at the end of `if`, `elif`, or `else:`.

**Key Takeaway:** Use `==` to compare, `elif` for mutually exclusive branches, and always check edge cases like `0` before dividing.


---

## 1.3 Repeating Work (`for` Loops, `range()` & `while` Loops)

> **Before You Start:** If you ever copy-paste the same line 5 times, a loop does it cleaner and works for 5 or 5,000,000 items.

### 1. Definition
A **`for` loop** runs a block once for each item in a sequence. A **`while` loop** keeps repeating as long as a condition stays `True`.

### 2. Exact Syntax — for Loop, range(), and while Loop
```python
for item in ['a', 'b', 'c']:
    print(item)

for i in range(3):          # i takes values 0, 1, 2
    print(i)

count = 3
while count > 0:
    print(count)
    count -= 1              # MUST update count so loop ends!
```

- `range(3)` produces `0, 1, 2` (starts at `0`, stops *before* `3`). `range(1, 4)` produces `1, 2, 3`.
- `break` immediately stops the loop early; `continue` skips the rest of the current round and moves to the next item.

### 3. Tiny Example (Line-by-Line) — Tracing a Running Total Step-by-Step
```python
nums = [10, 20, 30]
total = 0
for n in nums:
    total = total + n
    print(f'Added {n}, total is now {total}')
print(f'Final: {total}')
```

1. Before loop: `total = 0`.
2. Round 1 (`n = 10`): `total` becomes `0 + 10 = 10`.
3. Round 2 (`n = 20`): `total` becomes `10 + 20 = 30`.
4. Round 3 (`n = 30`): `total` becomes `30 + 30 = 60`.
5. Line 6 (not indented): runs ONCE at the end -> `Final: 60`.

### Using `continue` to Skip Junk
Inside a loop over lines or numbers, `if val < 0: continue` skips invalid entries immediately so your main logic stays clean.


### 4. Practical Example — Skipping Negative Numbers While Summing

```python
readings = [12, -5, 8, -1, 10]
valid_sum = 0

for val in readings:
    if val < 0:
        continue
    valid_sum += val

print(f'Valid sum: {valid_sum}')  # 30
```

### Common Mistakes to Avoid

- Putting `total = 0` *inside* the loop (resets it back to 0 every round!).
- Writing a `while` loop without changing the condition variable (infinite loop).

**Key Takeaway:** Set initial totals *before* the loop, use `for` for collections/`range()`, and use `continue` to skip invalid items cleanly.


---

## 1.4 Lists, Dictionaries, Sets & Tuples

> **Before You Start:** Think of a **list** like a numbered shelf (`0, 1, 2`), and a **dictionary** like labeled drawers (`'name'`, `'age'`).

### 1. Definition
- **`list` (`[a, b]`):** Ordered collection indexed by position (`0, 1, 2...`).
- **`dict` (`{k: v}`):** Key -> Value lookup table.
- **`set` (`{a, b}`):** Unordered unique items only (auto-removes duplicates).
- **`tuple` (`(a, b)`):** Fixed, unchangeable list.

### 2. Exact Syntax — Essential List & Dictionary Syntax
```python
fruits = ['apple', 'banana']
fruits.append('mango')          # adds to end
print(fruits[0], fruits[-1])    # 'apple', 'mango'

person = {'name': 'Sam', 'age': 25}
person['city'] = 'Delhi'        # add or overwrite key
job = person.get('job', 'None') # safe lookup (no KeyError crash!)
```

- `fruits[0]` is item #1; `fruits[-1]` is the last item.
- `person['job']` crashes if `'job'` doesn't exist; `person.get('job', 'None')` returns `'None'` safely.
- Copying lists: `b = a` only makes a second label to the **same** list! Use `b = a.copy()` to make a real copy.

### 3. Tiny Example (Line-by-Line) — Looping Over a Dictionary's Keys & Values
```python
scores = {'math': 90, 'python': 95}
for subject, pts in scores.items():
    print(f'{subject}: {pts}')
```

1. `scores.items()` yields each `(key, value)` pair one at a time.
2. Round 1: `subject='math'`, `pts=90`. Round 2: `subject='python'`, `pts=95`.

### Removing Duplicates Quickly with `set()`
`set(['ai', 'ml', 'ai'])` immediately gives `{'ai', 'ml'}`—handy whenever cleaning repeated tags or words.


### 4. Practical Example — Safe List Copy & Deduplicating Tags

```python
skills = ['python', 'sql']
resume_skills = skills.copy()
resume_skills.append('pytorch')
print('Base:', skills)
print('Resume:', resume_skills)

tags = ['ai', 'py', 'ai', 'ml']
print('Unique:', sorted(set(tags)))
```

### Common Mistakes to Avoid

- Forgetting Python list indexes start at `0` (`items[1]` is the second item).
- Writing `copy = original` on a list instead of `copy = original.copy()`.

**Key Takeaway:** Use `list` for ordered data, `dict` + `.get()` for named fields, `set` for uniqueness, and `.copy()` before mutating.


---

## 1.5 One-Line `for` Loops Explained (List Comprehensions)

> **Before You Start:** One-line loops like `[x * 2 for x in nums if x > 0]` are NOT new magic—they are just a normal 4-line `for` loop folded onto one line!

### 1. Definition
A **list comprehension** builds a new list by transforming and optionally filtering items from an existing collection on one line.

### 2. Exact Syntax — Normal `for` Loop vs One-Line Comprehension
```python
# 4-line normal loop:
result = []
for x in items:
    if condition(x):
        result.append(transform(x))

# Exact same thing on 1 line:
result = [transform(x) for x in items if condition(x)]
```

- **Read it in 3 parts:** `[ WHAT_TO_KEEP   for ITEM in COLLECTION   if FILTER_CONDITION ]`.
- Part 1 (`transform(x)`): what goes into the new list.
- Part 2 (`for x in items`): the loop header.
- Part 3 (`if condition(x)`): optional filter—only items passing this `if` enter the new list!

### 3. Tiny Example (Line-by-Line) — Doubling Only Even Numbers
```python
nums = [1, 2, 3, 4, 5]
evens_doubled = [n * 2 for n in nums if n % 2 == 0]
print(evens_doubled)
```

1. `n = 1`: `1 % 2 == 0` is False -> skipped.
2. `n = 2`: True -> adds `2 * 2 = 4`.
3. `n = 3`: False -> skipped.
4. `n = 4`: True -> adds `4 * 2 = 8` -> prints `[4, 8]`!

### Rule of Thumb
Only use a one-line comprehension when it is short and easy to read. For complex steps, a normal `for` loop is always better.


### 4. Practical Example — Cleaning Messy Usernames & Counting Passing Scores

```python
raw_names = ['  Sara ', '', '  ALEX', '   ']
clean_names = [name.strip().lower() for name in raw_names if name.strip()]
print(clean_names)

scores = [45, 80, 62, 50]
pass_count = sum(1 for s in scores if s >= 60)
print('Passed:', pass_count)
```

### Common Mistakes to Avoid

- Trying to cram complicated multi-branch logic into one unreadable comprehension.

**Key Takeaway:** `[expr for x in items if cond]` is just shorthand for `out = []; for x in items: if cond: out.append(expr)`.


---

## 1.6 Functions (`def`, `return` vs `print` & Safe Defaults)

> **Before You Start:** Think of a function like a blender: ingredients go in (parameters), work happens inside, and a smoothie comes back (`return`).

### 1. Definition
A **function** gives a name to a reusable block of steps so you can call it anywhere with different inputs.

### 2. Exact Syntax — Function Definition & Calling
```python
def add_bonus(score: int, bonus: int = 5) -> int:
    new_score = score + bonus
    return new_score

final = add_bonus(80)       # uses default bonus=5 -> 85
final2 = add_bonus(80, 10)  # overrides bonus=10 -> 90
```

- `def` defines the function; it doesn't run until you call `add_bonus(...)`.
- `: int` and `-> int` are **type hints** telling humans what types go in and come out.
- `bonus: int = 5` is a **default argument** used if the caller doesn't pass a second value.
- `return` hands the result back to the caller and exits the function.

### 3. Tiny Example (Line-by-Line) — Why `print()` Cannot Replace `return`
```python
def broken_double(x):
    print(x * 2)

def working_double(x):
    return x * 2

a = broken_double(5)
b = working_double(5)
print('a is:', a, '| b is:', b)
```

1. `broken_double(5)` prints `10`, then ends with no `return`, so `a` becomes `None`.
2. `working_double(5)` returns `10`, so `b` becomes `10` (and you can do `b + 1`!).

### One Common Beginner Trap: Never Put `= []` as a Default
Suppose you write `def add_item(x, items=[]):`. Python creates that `[]` **only once** and reuses it across every call—so items from yesterday's call leak into today's call!
- **Fix:** Write `items=None` instead (`None` is Python's built-in word for *'nothing was passed'*), then check `if items is None:` inside the function with a normal `if / else`.


### 4. Practical Example — Simple Function With Default Value + Safe Optional List

```python
# Block 1: Simple function with a default parameter
def apply_discount(price: float, discount_percent: float = 10.0) -> float:
    saved = price * (discount_percent / 100)
    return round(price - saved, 2)

print(apply_discount(100))      # 90.0
print(apply_discount(100, 25))  # 75.0

# Block 2: Safe optional list using `None` and plain if/else
def add_tag(tag: str, existing=None):
    if existing is None:
        result = []
    else:
        result = existing.copy()
    if tag not in result:
        result.append(tag)
    return result

print(add_tag('python'))
print(add_tag('ai'))
```

### Common Mistakes to Avoid

- Forgetting `return` inside a function and wondering why the caller gets `None`.
- Using `items=[]` as a default argument instead of `items=None`.

**Key Takeaway:** Functions should `return` values (not just `print`), and optional lists should default to `None` followed by `if existing is None:`.


---

## 1.7 Error Handling (`try / except` & `raise ValueError`)

> **Before You Start:** If you ever tried `int('abc')` or `10 / 0`, Python stopped with red text (an Exception). Here is how to catch errors politely AND trigger clear errors on bad inputs.

### 1. Definition
- **`try / except`:** Runs risky code inside `try:`; if an expected error happens, jumps to `except` instead of crashing the whole program.
- **`raise ValueError('...')`:** Intentionally stops your own function with a clear message when a caller passes impossible input (like a negative price).

### 2. Exact Syntax — Catching Errors (`try / except`) & Raising Errors (`raise`)
```python
# 1. Catching an error cleanly:
try:
    num = int(user_text)
except ValueError:
    num = 0                    # fallback value instead of crashing!

# 2. Guarding your own function with `raise`:
def set_age(age: int) -> int:
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age
```

- Common built-in errors: `ValueError` (right type, bad value like `int('abc')`), `ZeroDivisionError` (`10 / 0`), `KeyError` (missing dict key), `TypeError` (`'5' + 5`).
- Always name the **specific** error (`except ValueError:`), never bare `except:` (bare `except:` hides your own typos!).
- When testing functions that `raise ValueError`, callers wrap them in `try / except ValueError:` to confirm bad inputs are caught!

### 3. Tiny Example (Line-by-Line) — Converting Messy Strings Safely
```python
def to_int_safe(text: str, default: int = 0) -> int:
    try:
        return int(text)
    except ValueError:
        return default

print(to_int_safe('42'))     # 42
print(to_int_safe('hello'))  # 0 (no crash!)
```

1. `to_int_safe('42')`: `int('42')` succeeds -> returns `42`.
2. `to_int_safe('hello')`: `int('hello')` fails with `ValueError`, jumps to `except ValueError:`, and returns `0`!

### Why Validation (`raise ValueError`) Helps Beginners
Suppose you write `apply_discount(price, discount_percent)`. If someone passes `price = -50`, silently returning `-45` hides a bug! Checking `if price < 0: raise ValueError('Invalid input')` catches bad data immediately at the door.


### 4. Practical Example — Validating Inputs With `raise` + Catching Errors Safely

```python
def apply_discount(price: float, discount_percent: float = 10.0) -> float:
    if price < 0 or discount_percent < 0 or discount_percent > 100:
        raise ValueError('Invalid input')
    return round(price - price * (discount_percent / 100), 2)

# Block 2: Caller handles bad input politely with try/except
for p in [100, -20]:
    try:
        print('Final price:', apply_discount(p))
    except ValueError as err:
        print('Skipped bad price:', err)
```

### Common Mistakes to Avoid

- Writing bare `except:` with no error name (silently hides real bugs like misspelled variables!).
- Returning `None` or printing `'Error'` instead of `raise ValueError(...)` when a function's contract requires valid numbers.

**Key Takeaway:** Use `try / except SpecificError:` to handle expected failures politely, and `raise ValueError(...)` to reject invalid inputs early.


---

## Hands-On Project: Student Grade & Tag Analyzer Script

Use variables, loops, comprehensions, dictionaries, and clean functions to summarize student scores and tags.

1. Write `clean_tags(raw_tags)` using a list comprehension + `set`.
2. Write `summarize_scores(scores)` returning passed, failed, and average.
3. Verify every function with `assert` checks.
