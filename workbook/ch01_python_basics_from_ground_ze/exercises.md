# Workbook — Chapter 1: Python Basics From Ground Zero & Working With Files


---

## 1.1 Warm-Up: Loop + Condition + Dictionary Summary (`Foundation` · Python)

Write a function `grade_summary(scores: list[int]) -> dict[str, int]` that checks every score in `scores` and returns `{'passed': ..., 'failed': ...}`.
- A score **>= 60** counts as `'passed'`.
- A score **< 60** counts as `'failed'`.

**Example:** `grade_summary([40, 60, 85, 59])` returns `{'passed': 2, 'failed': 2}`.

### Thinking Blueprint

- Block 1 (Setup): Start with `counts = {'passed': 0, 'failed': 0}`.
- Block 2 (Loop & Decision): For each `s` in `scores`, if `s >= 60` add 1 to `counts['passed']`, else add 1 to `counts['failed']`.
- Block 3 (Return): Return `counts` (not print!).

### Progressive Hints

1. Start with `counts = {'passed': 0, 'failed': 0}` so empty lists also return `{'passed': 0, 'failed': 0}`.
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

**High-Level Blocks:** (1) Pre-initialize both dictionary keys to `0`; (2) Loop once over `scores` updating the right bucket; (3) `return` the dict.


---

## 1.2 Warm-Up: Safe Dictionary Lookup & Cleaning Strings (`Foundation` · Python)

Given a dictionary `user` (which might be missing `'name'` or `'role'`), write `format_badge(user: dict) -> str` returning:
`'<cleaned_name> (<cleaned_role>)'`
- If `'name'` is missing or empty after stripping, default to `'Guest'` (keep original title/case or strip spaces, e.g. `'  Sara '` -> `'Sara'`).
- If `'role'` is missing or empty after stripping, default to `'learner'`, and always lowercase the role.

### Thinking Blueprint

- Block 1 (Safe Read): Use `(user.get('name') or '').strip()` so missing or `None` never crashes.
- Block 2 (Fallback): If empty string after `.strip()`, fall back to `'Guest'` / `'learner'`.
- Block 3 (Format): Return `f'{name} ({role})'`.

### Progressive Hints

1. `raw_name = (user.get('name') or '').strip()`
2. `name = raw_name if raw_name else 'Guest'`

### Dry-Run Trace
`{'name': '  Sara ', 'role': ' ENGINEER '}` -> `name='Sara'`, `role='engineer'` -> `'Sara (engineer)'`.

### Answer & Explanation
```python
def format_badge(user: dict) -> str:
    raw_name = (user.get('name') or '').strip()
    raw_role = (user.get('role') or '').strip().lower()
    name = raw_name if raw_name else 'Guest'
    role = raw_role if raw_role else 'learner'
    return f'{name} ({role})'

if __name__ == '__main__':
    print(format_badge({'name': '  Sara ', 'role': ' ENGINEER '}))
```

**High-Level Blocks:** Using `.get()` + `or ''` protects against both missing keys and `None` values, and `.strip()` cleans accidental spaces.


---

## 1.3 File Basics: Count Non-Empty Lines in a `.txt` File (`Foundation` · Files & Stdlib)

Write `count_non_empty_lines(path: Path) -> int` that:
1. Returns `0` if `path` does not exist (do NOT crash!).
2. Otherwise opens `path` with `encoding='utf-8'` and counts how many lines are non-empty after `.strip()`.

### Thinking Blueprint

- Block 1 (Guard): `if not path.exists(): return 0` (or `try / except FileNotFoundError`).
- Block 2 (Read & Count): `with path.open('r', encoding='utf-8') as f:` loop line by line and count `if line.strip():`.

### Progressive Hints

1. Remember `'   \n'.strip()` becomes `''` (empty/False), so `if line.strip():` skips blank and whitespace-only lines!

### Dry-Run Trace
File with `'hello\n\n   \nworld\n'` -> `'hello'` (+1), `''` (skip), `'   '` (skip), `'world'` (+1) -> `2`.

### Answer & Explanation
```python
from pathlib import Path

def count_non_empty_lines(path: Path) -> int:
    if not path.exists():
        return 0
    count = 0
    with path.open('r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                count += 1
    return count
```

**High-Level Blocks:** (1) Safe missing-file check prevents crashes; (2) `with path.open(...)` streams the file line by line and closes it automatically.


---

## 1.4 Fix the Shared-Bucket Mutability Bug (`Foundation` · Python)

Write `add_tag(tag: str, tags: list[str] | None = None) -> list[str]` that:
1. Creates a fresh list when `tags` is `None`.
2. **Never mutates** the caller's input list when `tags` is passed — returns a new list with `tag` added if not already present.

### Thinking Blueprint

- Block 1 (Guard/Copy): If `tags is None` start with `[]`, else `list(tags)` creates an independent copy.
- Block 2 (Update): Append `tag` only if `tag not in result`, then return `result`.

### Progressive Hints

1. Use `tags: list[str] | None = None` instead of `= []`.
2. `result = [] if tags is None else list(tags)` isolates your new list from the caller's list.

### Dry-Run Trace
| Call | Input `tags` | `result` created | Output | Caller `base` |
|---|---|---|---|---|
| `add_tag('a')` | `None` | `[]` | `['a']` | N/A |
| `add_tag('b')` | `None` | `[]` (fresh!) | `['b']` | N/A |
| `add_tag('llm', base)` | `['ai']` | `['ai']` (copy) | `['ai', 'llm']` | `['ai']` |

### Answer & Explanation
```python
def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    result = [] if tags is None else list(tags)
    if tag not in result:
        result.append(tag)
    return result
```

**High-Level Blocks:** (1) *Defensive initialization* creates a fresh list object via `list(tags)` so caller state stays untouched; (2) *Deduplicated append* guarantees idempotency.

**Complexity:** O(N) time and space.


---

## 1.5 File I/O: Safe JSONL Loader & Filtered Writer (`pathlib` + `json`) (`Foundation` · Files & Stdlib)

Write `filter_jsonl_file(src: Path, dst: Path, min_chars: int = 5) -> int` that:
1. Reads `src` line-by-line with `encoding='utf-8'` (skip empty lines and malformed JSON lines cleanly).
2. Keeps records where `isinstance(rec.get('text'), str)` and `len(rec['text'].strip()) >= min_chars`.
3. Ensures `dst.parent` exists (`mkdir(parents=True, exist_ok=True)`), writes valid records as JSONL (`json.dumps` per line), and returns the count written.

### Thinking Blueprint

- Block 1 (Input Read & Parse): Open `src` via `with src.open('r', encoding='utf-8')`, iterate lines, `try: rec = json.loads(line)` / `except json.JSONDecodeError: continue`.
- Block 2 (Validation Filter): Check `text` is a `str` and stripped length >= `min_chars`.
- Block 3 (Safe Output Write): Create `dst.parent`, write one JSON line per kept record, return `len(kept)`.

### Progressive Hints

1. Check `if not src.exists(): raise FileNotFoundError(str(src))`.
2. Use `dst.parent.mkdir(parents=True, exist_ok=True)` before opening `dst`.

### Dry-Run Trace
| Line | JSON parse | `text` length >= 5? | Written? |
|---|---|---|---|
| `'{"text": "hello ai"}'` | ok | yes (8) | Yes |
| `'{bad json'` | JSONDecodeError | skipped | No |
| `'{"text": "hi"}'` | ok | no (2) | No |

### Answer & Explanation
```python
import json
from pathlib import Path

def filter_jsonl_file(src: Path, dst: Path, min_chars: int = 5) -> int:
    if not src.exists():
        raise FileNotFoundError(f'Source file not found: {src}')
    kept: list[dict] = []
    with src.open('r', encoding='utf-8') as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            text = rec.get('text') if isinstance(rec, dict) else None
            if isinstance(text, str) and len(text.strip()) >= min_chars:
                kept.append(rec)
    dst.parent.mkdir(parents=True, exist_ok=True)
    with dst.open('w', encoding='utf-8') as out:
        for rec in kept:
            out.write(json.dumps(rec) + '\n')
    return len(kept)
```

**High-Level Blocks:** (1) *Path guard* fails loudly if `src` is missing; (2) *Resilient streaming parser* isolates `JSONDecodeError` to a single line; (3) *Directory-safe writer* ensures nested output folders exist before writing UTF-8 lines.


---

## 1.6 CSV Summary with `csv.DictReader` & `collections.Counter` (`Foundation` · Files & Stdlib)

Write `count_csv_labels(csv_path: Path, column: str = 'label') -> dict[str, int]` that opens `csv_path` using `csv.DictReader`, skips rows where `column` is empty/whitespace, and returns a plain `dict[str, int]` mapping each stripped label to its occurrence count.

### Thinking Blueprint

- Block 1 (File Context): Open with `encoding='utf-8', newline=''` as required by Python's `csv` module.
- Block 2 (Counter Aggregation): Use `collections.Counter` over non-empty stripped `row.get(column, '').strip()` values.

### Progressive Hints

1. `newline=''` prevents blank-line bugs in Python's `csv` reader on Windows.
2. Return `dict(counts)` so callers get a normal `dict`.

### Dry-Run Trace
CSV rows `[{'label': ' pos '}, {'label': ''}, {'label': 'neg'}, {'label': 'pos'}]` -> `{'pos': 2, 'neg': 1}`.

### Answer & Explanation
```python
import csv
from collections import Counter
from pathlib import Path

def count_csv_labels(csv_path: Path, column: str = 'label') -> dict[str, int]:
    counts: Counter[str] = Counter()
    with csv_path.open('r', encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f):
            val = (row.get(column) or '').strip()
            if val:
                counts[val] += 1
    return dict(counts)
```

**High-Level Blocks:** (1) `csv.DictReader` parses quoted commas safely by header name; (2) `(row.get(column) or '').strip()` handles missing or `None` cells cleanly; (3) `Counter` aggregates frequencies without manual key checks.
