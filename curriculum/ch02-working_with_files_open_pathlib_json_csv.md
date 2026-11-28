# Chapter 2: Working With Files (`open`, `pathlib`, `json`, `csv`)

*Reading & writing plain .txt files, pathlib.Path, try/except error handling, JSON/JSONL datasets, and CSV spreadsheets.*

**Why It Matters:** Real AI scripts don't hardcode text inside `.py` files—they read `.txt` notes, `.json` configs, `.jsonl` datasets, and `.csv` tables from disk safely.

**Skills Covered:** open() & with, pathlib.Path, try / except, json & jsonl, csv.DictReader


---

## 2.1 Reading & Writing Plain `.txt` Files (`open` & `with`)

> **Before You Start:** Start with plain `.txt` files first. Once 3 lines of `.txt` feel effortless, JSON and CSV are easy.

### 1. Definition
Opening a file connects your Python script to a file on your hard drive so you can read its contents or save new text into it.

### 2. Exact Syntax — The Safe `with open(...)` Pattern
```python
with open('notes.txt', 'w', encoding='utf-8') as f:
    f.write('Hello Python\n')

with open('notes.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
```

- `'w'` = **write** (creates or overwrites). `'a'` = **append** (adds to end). `'r'` = **read**.
- `with ... as f:` **automatically closes** the file when the indented block ends.
- `encoding='utf-8'` prevents Windows crashes on special characters or emojis.
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

1. Lines 1–2: Creates `demo.txt` with 3 lines (middle line is blank).
2. Line 6: Loops one line at a time.
3. Line 7: `'\n'.strip()` becomes `''` (empty/False), so blank lines are skipped!
4. Line 9: Prints `Non-empty lines: 2`.

### Reading All at Once vs Line by Line
- `f.read()` loads the **entire file** as one string (good for small files).
- `for line in f:` reads **one line at a time** (essential for huge 2 GB files!).


### 4. Practical Example — Appending a Log Entry Without Erasing Old Lines

```python
def append_log(filename: str, message: str) -> None:
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(message + '\n')

append_log('run.log', '[INFO] Started')
append_log('run.log', '[INFO] Finished')
print(open('run.log', encoding='utf-8').read())
```

### Common Mistakes to Avoid

- Opening with `'w'` when you meant `'a'` (accidentally erases old lines!).
- Forgetting `encoding='utf-8'` on Windows.

**Key Takeaway:** Always use `with open(..., encoding='utf-8') as f:`, loop `for line in f:` for large files, and call `.strip()`.


---

## 2.2 Clean Paths (`pathlib.Path`) & Handling Errors (`try / except`)

> **Before You Start:** On Windows, `'C:\new\test.txt'` breaks because `\n` means newline! `pathlib.Path` eliminates path headaches forever.

### 1. Definition
- **`pathlib.Path`:** A clean object representing a file or folder path across Windows, Mac, and Linux.
- **`try / except`:** Catches predictable errors (like a missing file) cleanly instead of crashing.

### 2. Exact Syntax — Path Operations & Specific Error Handling
```python
from pathlib import Path

p = Path('data') / 'raw' / 'notes.txt'
p.parent.mkdir(parents=True, exist_ok=True)

try:
    text = p.read_text(encoding='utf-8')
except FileNotFoundError:
    text = ''
```

- `/` joins folders cleanly regardless of OS.
- `p.exists()` checks if a file or folder exists.
- `p.parent.mkdir(parents=True, exist_ok=True)` safely creates missing parent folders.
- Always catch a **specific** error (`FileNotFoundError`, `ValueError`), never bare `except:`.

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
2. Line 5: Jumps straight to `except FileNotFoundError:` instead of crashing.
3. Lines 6–7: Prints a polite message and sets `content = ''`.

### Ensuring Output Folders Exist Before Writing
Always call `out_path.parent.mkdir(parents=True, exist_ok=True)` before saving into a subfolder like `output/2026/report.txt`.


### 4. Practical Example — Writing Safely into Nested Output Folders

```python
from pathlib import Path

out = Path('reports') / 'daily' / 'summary.txt'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text('All checks passed!\n', encoding='utf-8')
print(out.read_text(encoding='utf-8').strip())
```

### Common Mistakes to Avoid

- Trying to write into a subfolder before creating it -> `FileNotFoundError`.
- Writing bare `except:` which silently hides real typos.

**Key Takeaway:** Use `Path('a') / 'b.txt'`, create parent folders with `.mkdir(parents=True, exist_ok=True)`, and catch specific errors.


---

## 2.3 Loading & Saving JSON, JSONL & CSV Files

> **Before You Start:** Never split CSV lines with `line.split(',')` or parse JSON by hand—Python has `json` and `csv` built in!

### 1. Definition
- **JSON (`.json`):** Text format matching Python `dict`s and `list`s—used in configs and APIs.
- **JSONL (`.jsonl`):** 'JSON Lines'—one JSON object per line (standard for LLM datasets).
- **CSV (`.csv`):** Comma-separated spreadsheet table.

### 2. Exact Syntax — `json` and `csv.DictReader` Basics
```python
import csv, json
from pathlib import Path

data = json.loads('{"name": "AI"}')   # string -> dict
text = json.dumps({'name': 'AI'})       # dict -> string

with Path('data.csv').open('r', encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f))
```

- `json.load(f)` / `json.dump(obj, f)` work on open files.
- `json.loads(s)` / `json.dumps(obj)` ('s' = string) work on strings—ideal for `.jsonl` lines!
- `csv.DictReader(f)` reads each spreadsheet row as a `dict` keyed by header names.

### 3. Tiny Example (Line-by-Line) — Converting Python Dict -> JSON String -> Python Dict
```python
import json
record = {'user': 'Sam', 'score': 95}
as_text = json.dumps(record)
back_to_dict = json.loads(as_text)
print(type(as_text), as_text)
print(type(back_to_dict), back_to_dict['score'])
```

1. `json.dumps(record)` converts the dict into a text string.
2. `json.loads(as_text)` converts that string back into a Python `dict` so `back_to_dict['score']` works!

### Skipping Corrupt JSONL Lines Safely
Wrapping `json.loads(line)` inside `try / except json.JSONDecodeError:` skips a single broken line without crashing the whole pipeline.


### 4. Practical Example — Resilient JSONL Loader

```python
import json
from pathlib import Path

p = Path('sample.jsonl')
p.write_text('{"text": "ok"}\n{broken\n{"text": "good"}\n', encoding='utf-8')

records = []
with p.open('r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            continue
print(records)
```

### Common Mistakes to Avoid

- Mixing up `json.load(f)` (file) and `json.loads(s)` (string).
- Forgetting `newline=''` when opening CSV files for `csv` readers/writers.

**Key Takeaway:** Use `json.loads/dumps` for JSONL lines and `csv.DictReader` with `newline=''` for CSV tables.


---

## Hands-On Project: Dataset Inspector & File Converter CLI

Read a messy CSV file safely using `Path` and `csv.DictReader`, filter invalid rows, and export clean JSONL lines.

1. Check file existence with `Path`.
2. Read CSV rows using `csv.DictReader` and `encoding='utf-8'`.
3. Write clean JSONL lines and verify with `pytest`.
