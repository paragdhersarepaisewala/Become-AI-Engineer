# Chapter 1: Python Basics From Ground Zero & Working With Files

*Variables, basic types, if/else, loops, lists, dicts, functions, opening/loading files (open, pathlib, json, csv), and clean script structure.*

**Why It Matters:** Every AI tool—whether loading a dataset, cleaning chat logs, or calling an API—starts with the exact same building blocks: variables, decisions, loops, collections, functions, and reading/writing files safely.

**Skills Covered:** Variables & Types, if / Loops, Lists & Dicts, Functions, Files (open/json/csv), Stdlib Helpers


---

## 1.1 Variables, Data Types & Printing Output

> **Before You Start:** Python runs your script from Line 1 down to the last line, one instruction at a time.

### 1. Definition
A **variable** is a nickname you attach to a value so you can reuse or update it later. A **data type** tells Python what kind of value it is (a whole number, a decimal number, text, or a True/False flag).

### 2. Exact Syntax — Creating Variables & Printing with f-strings
```python
variable_name = value
print(f'Some text {variable_name}')
number = int('42')     # converts text '42' -> integer 42
decimal = float('3.5') # converts text '3.5' -> float 3.5
```

- `=` means **assign** (store the value on the right under the name on the left), NOT math equality.
- `int` = whole number (`25`), `float` = decimal (`19.99`), `str` = text in quotes (`'Alex'`), `bool` = `True` or `False`.
- `f'...'` (f-string) inserts any variable inside `{...}` cleanly into text.

### 3. Tiny Example (Line-by-Line) — Numbers vs Text (Strings)
```python
name = 'Sara'
age = 22
next_year = age + 1
print(f'{name} will be {next_year}')
```

1. Line 1: Stores the text `'Sara'` (`str`) in `name`.
2. Line 2: Stores the whole number `22` (`int`) in `age`.
3. Line 3: Reads `age` (`22`), adds `1`, and stores `23` in `next_year`.
4. Line 4: Prints `Sara will be 23`.

### Why Types Matter in Real Programs
When you read input from a user or a text file, Python always gives you **text (`str`)**—even if it looks like `'10'`. `'10' + '5'` gives `'105'` (glued text), whereas `int('10') + int('5')` gives `15` (math).


### 4. Practical Example — Calculating Study Hours from String Input

```python
# Block 1: Raw settings (pretend '3' came from a config file as text)
hours_text = '3'
days = 4

# Block 2: Convert text to int before multiplying
hours_num = int(hours_text)
total_hours = hours_num * days

# Block 3: Display result
print(f'Total study time: {total_hours} hours')
```

### Common Mistakes to Avoid

- Trying to do math on `'5'` without calling `int('5')` or `float('5')`.
- Writing `2name = 'x'` (variable names cannot start with a digit or contain spaces—use `user_name`).

**Key Takeaway:** Know whether a variable is a number (`int`/`float`) or text (`str`), convert explicitly with `int()`/`float()`, and use `f'...'` to display values.


---

## 1.2 Making Decisions (`if / elif / else`) & Loops (`for` & `while`)

> **Before You Start:** Python uses **4 spaces of indentation** on the left to know which lines belong inside an `if` or loop.

### 1. Definition
An **`if` statement** lets your program choose between actions based on a True/False question. A **loop** (`for` or `while`) repeats a block of code automatically without you copy-pasting lines.

### 2. Exact Syntax — if / elif / else and for / while
```python
if condition:
    # runs when condition is True
elif other_condition:
    # runs if first was False and this is True
else:
    # runs when all above were False

for item in collection:
    # repeats once per item

while keep_going:
    # repeats as long as keep_going is True
```

- Comparison operators: `==` (equal to), `!=` (not equal), `>`, `<`, `>=`, `<=`.
- Logical connectors: `and` (both True), `or` (at least one True), `not` (flips True/False).
- `range(5)` generates numbers `0, 1, 2, 3, 4` (stops *before* 5).

### 3. Tiny Example (Line-by-Line) — Adding Up 3 Scores with a `for` Loop
```python
scores = [10, 20, 30]
total = 0
for s in scores:
    total = total + s
print(total)
```

1. Line 1: Creates a list of 3 numbers.
2. Line 2: Starts a running counter `total` at `0` *before* the loop.
3. Line 3: Round 1 sets `s = 10` -> `total` becomes `10`. Round 2 sets `s = 20` -> `30`. Round 3 sets `s = 30` -> `60`.
4. Line 5 (not indented, so outside the loop!): Prints `60` once after the loop ends.

### Choosing Between `for` and `while`
- Use **`for`** 90% of the time: when walking through items in a list, lines in a file, or `range(n)`.
- Use **`while`** when you don't know how many rounds it will take (e.g., retrying a network request until it succeeds).


### 4. Practical Example — Counting Passing Scores with `for` + `if/else`

```python
scores = [45, 82, 91, 58]
passed = 0

# Block 1: Inspect each score one at a time
for score in scores:
    if score >= 60:
        passed += 1  # shorthand for passed = passed + 1
        print(f'{score}: Pass')
    else:
        print(f'{score}: Review')

# Block 2: Final count after loop finishes
print(f'Total passed: {passed}')
```

### Common Mistakes to Avoid

- Using `=` instead of `==` inside an `if` check (`if x == 5:` checks equality; `x = 5` assigns).
- Putting `total = 0` *inside* the `for` loop (which resets `total` back to `0` on every round!).
- Writing a `while` loop without updating the condition variable (causes an infinite loop).

**Key Takeaway:** Initialize counters *before* the loop, keep indentation consistent (4 spaces), and use `==` for comparisons.


---

## 1.3 Lists, Dictionaries, Sets & Tuples

> **Before You Start:** Instead of making 20 separate variables (`score1`, `score2`, ...), Python gives you 4 containers.

### 1. Definition
- **List (`[]`):** Ordered sequence accessed by index (`0, 1, 2...`).
- **Dictionary (`{k: v}`):** Key-value lookup table (like a real dictionary: look up a word to get its meaning).
- **Set (`{a, b}`):** Unordered bag that automatically keeps **unique** items only.
- **Tuple (`(a, b)`):** Locked list that cannot be modified after creation.

### 2. Exact Syntax — Core Container Operations
```python
items = ['a', 'b']          # list
items.append('c')           # add to end -> ['a', 'b', 'c']
first = items[0]            # 'a' (index starts at 0!)

user = {'name': 'Sam'}      # dict
city = user.get('city', 'Unknown')  # safe lookup! never crashes
user['age'] = 24            # add or update key
```

- `items[0]` is the **first** item; `items[-1]` is the **last** item.
- `user['city']` **crashes** with `KeyError` if `'city'` is missing; `user.get('city', default)` returns `default` safely.
- Copying a list: `b = a` only makes a second label to the **same** list. Use `b = a.copy()` to make a real separate copy!

### 3. Tiny Example (Line-by-Line) — Safe Dictionary Lookup & Removing Duplicates with `set`
```python
tags = ['ai', 'python', 'ai']
unique = set(tags)
print(unique)
user = {'name': 'Sara'}
print(user.get('role', 'student'))
```

1. Line 1: List with duplicate `'ai'`.
2. Line 2: `set(tags)` removes duplicates -> `{'ai', 'python'}`.
3. Line 4: Dictionary with only `'name'`.
4. Line 5: `.get('role', 'student')` sees `'role'` is missing and safely returns `'student'` instead of crashing.

### Which Container Should I Pick?
- Need items in order and might add/remove later? -> **`list`**
- Need to attach fields/counts to named labels (like JSON)? -> **`dict`**
- Need to eliminate duplicates or check `if word in seen` quickly? -> **`set`**
- Returning fixed pairs like `(width, height)` that shouldn't change? -> **`tuple`**


### 4. Practical Example — Counting & Safe List Copying

```python
# Block 1: List copy vs alias
original = ['python', 'sql']
safe_copy = original.copy()
safe_copy.append('docker')
print('original:', original)   # ['python', 'sql'] (untouched!)
print('copy:', safe_copy)      # ['python', 'sql', 'docker']

# Block 2: Updating a dictionary counter manually
counts = {}
for word in ['ai', 'ml', 'ai']:
    counts[word] = counts.get(word, 0) + 1
print(counts)  # {'ai': 2, 'ml': 1}
```

### Common Mistakes to Avoid

- Forgetting Python indexes start at `0`, not `1` (`items[1]` is the *second* item).
- Writing `user['missing_key']` instead of `user.get('missing_key')` when a key might not exist.
- Writing `b = a` expecting a separate copy of a list, then accidentally modifying `a`.

**Key Takeaway:** Use `list` for order, `dict` + `.get()` for named fields, `set` for uniqueness, and `.copy()` before mutating a borrowed list.


---

## 1.4 Functions (`def`, Parameters & `return` vs `print`)

> **Before You Start:** If you ever got `None` back from a function and didn't know why, this section fixes that forever.

### 1. Definition
A **function** is a named, reusable mini-machine: you pass inputs in (**parameters**), it runs its code, and it hands a result back with **`return`**.

### 2. Exact Syntax — Defining & Calling a Function
```python
def function_name(param1: str, param2: int = 1) -> str:
    result = f'{param1} x {param2}'
    return result

answer = function_name('hello', 3)  # saves 'hello x 3' in answer
```

- `def` creates the function (it does NOT run it until you call `function_name(...)`!).
- `: str` and `-> str` are **type hints**—optional labels for humans saying what types go in and come out.
- `param2: int = 1` is a **default value** used if the caller skips `param2`.
- `return` sends the value back to the caller and immediately exits the function.

### 3. Tiny Example (Line-by-Line) — `print` vs `return` Side-by-Side
```python
def bad_double(x):
    print(x * 2)

def good_double(x):
    return x * 2

a = bad_double(5)   # prints 10, but a is None!
b = good_double(5)  # b holds 10, so b + 1 == 11!
```

1. `bad_double(5)` prints `10` on screen, then hits the end without `return`, so Python gives back `None`.
2. Trying `a + 1` would crash (`None + 1` is invalid!).
3. `good_double(5)` returns `10` into `b`, so your program can keep using `b`.

### One Crucial Function Trap: Default `= []`
Python creates default argument values **only once** when `def` is read. If you write `def add(x, items=[]):`, every call shares that same list! Always write `items=None` and create a fresh `[]` inside the function.


### 4. Practical Example — Clean Reusable Function with Safe Optional List

```python
# Block 1: Helper with safe default None
def add_tag(tag: str, existing: list[str] | None = None) -> list[str]:
    result = [] if existing is None else existing.copy()
    if tag not in result:
        result.append(tag)
    return result

# Block 2: Each call without existing gets its own fresh list
print(add_tag('python'))  # ['python']
print(add_tag('ai'))      # ['ai'] (not ['python', 'ai']!)
```

### Common Mistakes to Avoid

- Forgetting `return` inside a function and getting `None`.
- Using `=[]` or `={}` as a default parameter instead of `=None`.

**Key Takeaway:** Functions should `return` values (not just `print` them), and optional mutable defaults should always be `None`.


---

## 1.5 Opening, Reading & Writing Files (`open`, `pathlib`, `json`, `csv`)

> **Before You Start:** Let's start with a 3-line `.txt` file first before touching JSON or CSV.

### 1. Definition
File handling lets Python save data permanently to your hard drive and load real datasets (`txt`, `json`, `csv`) into memory.

### 2. Exact Syntax — Opening Files Safely with `with` & `pathlib.Path`
```python
from pathlib import Path

p = Path('folder') / 'notes.txt'        # works on Windows, Mac, Linux
with p.open('w', encoding='utf-8') as f:
    f.write('Hello\n')

with p.open('r', encoding='utf-8') as f:
    text = f.read()
```

- `Path('folder') / 'notes.txt'` joins folder and filename cleanly with `/`.
- `'w'` = write (overwrites), `'a'` = append (adds to end), `'r'` = read.
- `with ... as f:` **automatically closes** the file when the block ends, even if an error occurs.
- `encoding='utf-8'` prevents Windows crashes on special characters or emojis.

### 3. Tiny Example (Line-by-Line) — Reading a Text File Line by Line
```python
from pathlib import Path
p = Path('notes.txt')
if p.exists():
    with p.open('r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())
```

1. `p.exists()` checks whether the file is actually on disk before opening.
2. `for line in f:` reads one line at a time (great for huge files!).
3. `line.strip()` removes the hidden newline `'\n'` at the end of each line.

### Loading Structured Files (`json` & `csv`) + `try / except`
- **`json.load(f)`** reads a `.json` file directly into a Python `dict` or `list`. **`json.loads(line)`** parses a single JSON string (`.jsonl` datasets have 1 JSON object per line).
- **`csv.DictReader(f)`** reads a `.csv` spreadsheet row by row, giving each row as a `dict` keyed by the header row.
- **`try / except`:** Lets you catch predictable errors like `FileNotFoundError` or `json.JSONDecodeError` instead of crashing.


### 4. Practical Example — Safe JSON & CSV Loaders Explained Block-by-Block

```python
import csv
import json
from pathlib import Path

# Block 1: Load a JSON file safely with try/except
def load_json_safe(path: Path) -> dict:
    try:
        with path.open('r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Block 2: Load CSV rows as a list of dictionaries
def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open('r', encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))
```

### Common Mistakes to Avoid

- Forgetting `encoding='utf-8'` on Windows.
- Forgetting `newline=''` when opening CSV files for `csv.DictReader` / `csv.writer`.
- Trying to parse CSV with `line.split(',')` (breaks whenever a text column contains a comma!).

**Key Takeaway:** Always use `Path`, `with path.open(..., encoding='utf-8')`, `json`/`csv`, and specific `try/except` blocks.


---

## 1.6 Small Standard Libraries & Clean Script Structure

> **Before You Start:** Now that you know loops, dicts, functions, and files, these 3 small built-in tools save huge amounts of boilerplate.

### 1. Definition
Python's **standard library** is a toolbox of built-in modules (`collections`, `os`, `json`, `csv`, `pathlib`) that come pre-installed with Python—no `pip install` required.

### 2. Exact Syntax — Counter, defaultdict, os.getenv & `__main__` Guard
```python
from collections import Counter, defaultdict
import os

counts = Counter(['ai', 'py', 'ai'])   # {'ai': 2, 'py': 1}
groups = defaultdict(list)             # missing key auto-starts as []
api_key = os.getenv('API_KEY', '')     # reads env var safely

if __name__ == '__main__':
    # code here ONLY runs when you run THIS file directly
```

- `Counter(items)` replaces manual `counts[x] = counts.get(x, 0) + 1` loops.
- `defaultdict(list)` lets you write `groups[tag].append(item)` without `if tag not in groups:`.
- `if __name__ == '__main__':` prevents your script from auto-running when another file imports a helper from it.

### 3. Tiny Example (Line-by-Line) — Grouping Items with `defaultdict(list)`
```python
from collections import defaultdict
groups = defaultdict(list)
groups['fruit'].append('apple')
groups['fruit'].append('pear')
print(dict(groups))
```

1. Line 2: Creates a special dict where any brand-new key automatically starts with `[]`.
2. Line 3: `'fruit'` wasn't in `groups` yet—Python auto-created `[]` and appended `'apple'`.
3. Line 5: Converts back to a normal dict and prints `{'fruit': ['apple', 'pear']}`.

### Clean 3-Block Layout for Any Python File
1. **Top:** `import` statements.
2. **Middle:** Helper functions (take arguments, `return` values, zero hardcoded paths).
3. **Bottom:** `if __name__ == '__main__':` block that reads files/inputs and calls your functions.


### 4. Practical Example — Clean 3-Block Script Skeleton

```python
# Block 1: Imports
from collections import Counter

# Block 2: Pure helper function
def top_words(text: str, n: int = 2) -> list[tuple[str, int]]:
    words = text.lower().split()
    return Counter(words).most_common(n)

# Block 3: Main runner (only runs when executed directly)
if __name__ == '__main__':
    print(top_words('ai python ai ml ai'))  # [('ai', 3), ('python', 1)]
```

### Common Mistakes to Avoid

- Putting file-reading or `print()` loops at top level without `if __name__ == '__main__':` (causes surprises when importing).

**Key Takeaway:** Organize files as Imports -> Functions -> `if __name__ == '__main__':`, and use `Counter` / `defaultdict` to keep code short and clear.


---

## Hands-On Project: Dataset Inspector & File Converter CLI

Read a CSV file safely with `Path` and `csv.DictReader`, count categories with `Counter`, and save a clean JSONL file.

1. Check file existence with `pathlib.Path`.
2. Load CSV rows safely via `csv.DictReader` and `encoding='utf-8'`.
3. Count categories with `Counter` and export clean JSONL lines.
