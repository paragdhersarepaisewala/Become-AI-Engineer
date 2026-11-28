# Workbook — Chapter 2: Working With Files & Everyday Built-In Libraries


---

## 2.1 Text File Basics: Count Non-Empty Lines (`Foundation` · Files & Stdlib)

Write `count_non_empty_lines(path: Path) -> int`: return `0` if missing, otherwise count lines with text after `.strip()`.

### Thinking Blueprint

- Guard `if not path.exists(): return 0`.
- Open with `with path.open('r', encoding='utf-8') as f:` and count `if line.strip():`.

### Progressive Hints

1. `'   \n'.strip()` is `''` (False), so blank lines are skipped cleanly.

### Dry-Run Trace
`'alpha\n\n   \nbeta\n'` -> `'alpha'` (+1), `''` (skip), `'   '` (skip), `'beta'` (+1) -> `2`.

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

**High-Level Blocks:** Path check prevents crashes; `with path.open(...)` streams lines and closes the file safely.


---

## 2.2 JSONL Filter & Nested Directory Writer (`Intermediate` · Files & Stdlib)

Write `filter_jsonl_file(src: Path, dst: Path, min_chars: int = 5) -> int` reading `src` line-by-line (skipping corrupt JSON), keeping records with `len(rec['text'].strip()) >= min_chars`, creating `dst.parent` if missing, writing JSONL to `dst`, and returning the count written.

### Thinking Blueprint

- Read `src` with `try: rec = json.loads(line)` / `except json.JSONDecodeError: continue`.
- Ensure `dst.parent.mkdir(parents=True, exist_ok=True)` before writing.

### Progressive Hints

1. Check `isinstance(rec, dict)` and `isinstance(rec.get('text'), str)`.

### Dry-Run Trace
Line `'{"text": "hello world"}'` -> kept; `'{broken'` -> skipped; `'{"text": "hi"}'` -> skipped.

### Answer & Explanation
```python
import json
from pathlib import Path

def filter_jsonl_file(src: Path, dst: Path, min_chars: int = 5) -> int:
    if not src.exists():
        raise FileNotFoundError(f'Missing file: {src}')
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

**High-Level Blocks:** Resilient line parser isolates JSONDecodeError; directory-safe writer creates nested folders cleanly.


---

## 2.3 CSV Summary With `csv.DictReader` & `Counter` (`Foundation` · Files & Stdlib)

Write `count_csv_labels(csv_path: Path, column: str = 'label') -> dict[str, int]` returning counts of stripped non-empty values in `column`.

### Thinking Blueprint

- Open with `encoding='utf-8', newline=''` and wrap with `csv.DictReader(f)`.
- Count non-empty stripped strings with `Counter` and return `dict(counts)`.

### Progressive Hints

1. `val = (row.get(column) or '').strip()`

### Dry-Run Trace
Rows `' pos '`, `''`, `'neg'`, `'pos'` -> `{'pos': 2, 'neg': 1}`.

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

**High-Level Blocks:** `DictReader` reads rows by header name; `Counter` aggregates counts in 1 line.
