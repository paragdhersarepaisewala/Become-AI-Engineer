# Chapter 2: Working With Files & Everyday Built-In Libraries

*Reading & writing .txt files, pathlib.Path, try/except error handling, JSON/JSONL, CSV spreadsheets, and small stdlib helpers.*

**Why It Matters:** Real programs don't hardcode data inside `.py` files—they load text documents, JSON configs, and CSV spreadsheets from disk without crashing when a file is missing or malformed.

**Skills Covered:** open() & with, pathlib.Path, try / except, json & jsonl, csv.DictReader, Counter & os


---

## 2.1 Reading & Writing Plain `.txt` Files (`open` & `with`)

> **Before You Start:** Start with plain `.txt` files first. Once 3 lines of `.txt` feel effortless, JSON and CSV are easy.

### 1. Definition
Opening a file connects your Python script to a file on your hard drive so you can read its contents or write new text into it.

### 2. Exact Syntax — The Safe `with open(...)` Pattern
```python
# Writing text to a file ('w' creates or overwrites):
with open('notes.txt', 'w', encoding='utf-8') as f:
    f.write('Hello Python\n')

# Reading text back ('r' reads):
with open('notes.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
```

- `'w'` = **write** (creates file or erases old content!). `'a'` = **append** (adds to end). `'r'` = **read**.
- `with ... as f:` **automatically closes** the file when the indented block finishes—even if an error occurs.
- `encoding='utf-8'` tells Python how to read/write emojis, accents, and quotes properly on Windows.
- `line.strip()` removes the invisible `'\n'` newline at the end of each line.

### 3. Tiny Example (Line-by-Line) — Writing 2 Lines and Counting Non-Empty Lines
```python
with open('demo.txt', 'w', encoding='utf-8') as f:
    f.write('First line\n\nSecond line\n')

count = 0
with open('demo.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip():
            count += 1
print('Non-empty lines:', count)
```

1. Lines 1–2: Creates `demo.txt` with 3 lines (middle line is blank `'\n'`).
2. Line 6: Loops one line at a time.
3. Line 7: `'\n'.strip()` becomes `''` (empty/False), so blank lines are skipped!
4. Line 9: Prints `Non-empty lines: 2`.

### Reading All at Once vs Line by Line
- `f.read()` loads the **entire file** as one big string (great for tiny config files).
- `for line in f:` reads **one line at a time** (essential for huge 2 GB AI training files so your RAM doesn't explode!).


### 4. Practical Example — Appending a Log Entry Without Erasing Old Lines

```python
def append_log(filename: str, message: str) -> None:
    # 'a' appends to the end instead of overwriting like 'w'
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(message + '\n')
```

### Common Mistakes to Avoid

- Opening a file with `'w'` when you meant `'a'` (accidentally wipes the existing file!).
- Forgetting `encoding='utf-8'` on Windows (crashes with `UnicodeDecodeError` on curly quotes or emojis).

**Key Takeaway:** Always use `with open(..., encoding='utf-8') as f:`, loop `for line in f:` for large files, and call `.strip()` on lines.


---

## 2.2 Clean File Paths (`pathlib.Path`) & Handling Errors (`try / except`)

> **Before You Start:** On Windows, `'C:\new\test.txt'` breaks because `\n` means newline and `\t` means tab! `pathlib.Path` eliminates path headaches forever.

### 1. Definition
- **`pathlib.Path`:** A clean Python object representing a file or folder path that works identically on Windows, Mac, and Linux.
- **`try / except`:** Lets your code catch predictable errors (like a missing file) and respond cleanly instead of crashing.

### 2. Exact Syntax — Path Operations & Specific Error Handling
```python
from pathlib import Path

p = Path('data') / 'raw' / 'notes.txt'     # builds folder/raw/notes.txt
p.parent.mkdir(parents=True, exist_ok=True) # creates data/raw/ if missing

try:
    text = p.read_text(encoding='utf-8')
except FileNotFoundError:
    text = ''                              # fallback if file doesn't exist
```

- Use `/` between `Path` objects—Python automatically converts it to `\` on Windows or `/` on Linux/Mac.
- `p.exists()` returns `True` or `False`.
- `p.parent.mkdir(parents=True, exist_ok=True)` safely creates missing folders without failing if they already exist.
- Always catch a **specific** error (`except FileNotFoundError:` or `except ValueError:`), never bare `except:` (bare `except:` hides typos and real bugs!).

### 3. Tiny Example (Line-by-Line) — Safely Reading a Missing File
```python
from pathlib import Path

missing = Path('does_not_exist.txt')
try:
    content = missing.read_text(encoding='utf-8')
except FileNotFoundError:
    print('Could not find file—using empty default.')
    content = ''
```

1. Line 4: Tries to read `does_not_exist.txt`.
2. Line 5: Python jumps straight to `except FileNotFoundError:` instead of crashing.
3. Line 6–7: Prints a polite message and sets `content = ''` so the rest of the script keeps running.

### Finding All `.txt` Files in a Folder
`list(Path('docs').glob('*.txt'))` finds every text file inside `docs/` in one clean line!


### 4. Practical Example — Writing Safely into Nested Output Folders

```python
from pathlib import Path

def save_report(out_path: Path, body: str) -> None:
    # Ensure parent folders exist before opening the file
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(body, encoding='utf-8')
```

### Common Mistakes to Avoid

- Trying to write `Path('new_folder/out.txt').write_text(...)` before creating `new_folder` -> `FileNotFoundError`.
- Writing bare `except:` which silently swallows syntax/variable bugs.

**Key Takeaway:** Use `Path('a') / 'b.txt'`, call `.parent.mkdir(parents=True, exist_ok=True)` before writing, and catch specific exceptions with `try/except`.


---

## 2.3 Loading & Saving JSON, JSONL & CSV Files

> **Before You Start:** Never split CSV lines with `line.split(',')` or parse JSON by hand—Python already has `json` and `csv` built in!

### 1. Definition
- **JSON (`.json`):** A text format that looks almost identical to Python `dict`s and `list`s—used everywhere in configs and web APIs.
- **JSONL (`.jsonl`):** 'JSON Lines'—one standalone JSON object per line (standard for LLM fine-tuning datasets!).
- **CSV (`.csv`):** Comma-separated spreadsheet table.

### 2. Exact Syntax — `json` and `csv.DictReader` Basics
```python
import csv, json
from pathlib import Path

# JSON: file <-> Python dict/list
data = json.loads('{"name": "AI"}')   # string -> dict
text = json.dumps({'name': 'AI'})       # dict -> string

# CSV: read each row as a dictionary by column header
with Path('data.csv').open('r', encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f))
```

- `json.load(f)` / `json.dump(obj, f)` work directly on an open file `f`.
- `json.loads(s)` / `json.dumps(obj)` ('s' = string) convert between a single string and Python data—perfect for reading `.jsonl` line by line!
- `csv.DictReader(f)` uses row 1 as column keys, returning each data row as a `dict` like `{'id': '1', 'label': 'pos'}`.

### 3. Tiny Example (Line-by-Line) — Converting Python Dict -> JSON String -> Python Dict
```python
import json
record = {'user': 'Sam', 'score': 95}
as_text = json.dumps(record)
back_to_dict = json.loads(as_text)
print(type(as_text), as_text)
print(type(back_to_dict), back_to_dict['score'])
```

1. `json.dumps(record)` turns the Python dict into a plain text string `'{"user": "Sam", "score": 95}'`.
2. `json.loads(as_text)` parses that string back into a real Python `dict` so `back_to_dict['score']` works!

### Handling Broken Lines in `.jsonl` Datasets
Real datasets sometimes have 1 corrupted line out of 10,000. Wrapping `json.loads(line)` inside `try / except json.JSONDecodeError:` skips only that broken line instead of crashing the whole job.


### 4. Practical Example — Resilient JSONL Loader

```python
import json
from pathlib import Path

def read_jsonl(path: Path) -> list[dict]:
    items: list[dict] = []
    with path.open('r', encoding='utf-8') as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            try:
                items.append(json.loads(line))
            except json.JSONDecodeError:
                continue  # skip malformed line safely
    return items
```

### Common Mistakes to Avoid

- Mixing up `json.load(f)` (takes a file object) with `json.loads(s)` (takes a string).
- Forgetting `newline=''` when opening CSV files for `csv.DictReader` / `csv.writer`.

**Key Takeaway:** Use `json.loads/dumps` for JSONL lines and `csv.DictReader` with `newline=''` for CSV tables.


---

## 2.4 Small Built-In Tools (`Counter`, `defaultdict`, `os`, `__main__`)

> **Before You Start:** These tiny built-in modules save dozens of lines of repetitive code once you already know loops and dicts.

### 1. Definition
Python ships with pre-installed helper modules (`collections`, `os`) so you don't have to reinvent counting, grouping, or reading environment settings.

### 2. Exact Syntax — Counter, defaultdict, os.getenv & `__main__`
```python
from collections import Counter, defaultdict
import os

counts = Counter(['ai', 'py', 'ai'])  # Counter({'ai': 2, 'py': 1})
groups = defaultdict(list)            # new keys auto-start as []
key = os.getenv('API_KEY', 'none')    # safe env var lookup

if __name__ == '__main__':
    # only runs when you run THIS file directly
```

- `Counter(items).most_common(2)` returns the top 2 `(item, count)` pairs immediately.
- `defaultdict(list)` lets you write `groups[tag].append(val)` without `if tag not in groups: groups[tag] = []`.
- `if __name__ == '__main__':` keeps helper files quiet if another script imports functions from them.

### 3. Tiny Example (Line-by-Line) — Counting Words in 2 Lines with `Counter`
```python
from collections import Counter
words = 'learn python learn ai learn'.split()
c = Counter(words)
print(dict(c), '| Top 1:', c.most_common(1))
```

1. `.split()` breaks the sentence into `['learn', 'python', 'learn', 'ai', 'learn']`.
2. `Counter(words)` counts each word automatically.
3. `c.most_common(1)` returns `[('learn', 3)]`.

### Putting It All Together
Combining `Path` + `csv.DictReader` + `Counter` lets you inspect an entire dataset in under 15 readable lines!


### 4. Practical Example — 3-Block Script Reading & Summarizing Data

```python
from collections import Counter

def summarize_labels(rows: list[dict[str, str]]) -> dict[str, int]:
    labels = [r['label'].strip() for r in rows if r.get('label', '').strip()]
    return dict(Counter(labels))

if __name__ == '__main__':
    sample = [{'label': 'pos'}, {'label': 'neg'}, {'label': 'pos'}]
    print(summarize_labels(sample))  # {'pos': 2, 'neg': 1}
```

### Common Mistakes to Avoid

- Forgetting `dict(counts)` when an API or test expects a plain `dict` instead of a `Counter`.

**Key Takeaway:** Use `Counter` for counting, `defaultdict(list)` for grouping, and `if __name__ == '__main__':` at the bottom of runnable scripts.


---

## Hands-On Project: Dataset Inspector & File Converter CLI

Read a CSV file safely using `Path` and `csv.DictReader`, count labels with `Counter`, and export clean JSONL lines.

1. Check file existence with `Path`.
2. Read CSV rows using `csv.DictReader` and `encoding='utf-8'`.
3. Count categories with `Counter` and write clean JSONL output.
