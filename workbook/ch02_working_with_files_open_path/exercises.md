# Workbook — Chapter 2: Working With Files (`open`, `pathlib`, `json`, `csv`)


---

## 2.1 Text File Basics: Count Non-Empty Lines (`Foundation` · Files)

Write `count_non_empty_lines(path: Path) -> int`: return `0` if missing, otherwise count lines with text after `.strip()`.

### Thinking Blueprint

- Guard `if not path.exists(): return 0`.
- Stream lines via `with path.open('r', encoding='utf-8') as f:`.

### Progressive Hints

1. `if line.strip():` skips blank and whitespace-only lines.

### Dry-Run Trace
`'alpha\n\n   \nbeta\n'` -> `2`.

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

**High-Level Blocks:** Path check prevents crashes; `with path.open(...)` streams lines and closes safely.


---

## 2.2 JSONL Filter & Nested Directory Writer (`Intermediate` · Files)

Write `filter_jsonl_file(src: Path, dst: Path, min_chars: int = 5) -> int` skipping broken JSON lines, keeping dicts with `len(rec['text'].strip()) >= min_chars`, creating `dst.parent`, writing JSONL, and returning the count.

### Thinking Blueprint

- Isolate `json.JSONDecodeError` per line.
- Create `dst.parent.mkdir(parents=True, exist_ok=True)` before writing.

### Progressive Hints

1. Check `isinstance(rec, dict)` and `isinstance(rec.get('text'), str)`.

### Dry-Run Trace
`'{"text": "hello world"}'` -> kept; `'{broken'` -> skipped.

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

**High-Level Blocks:** Resilient line parser + directory-safe writer.


---

## 2.3 CSV Summary With `csv.DictReader` (`Foundation` · Files)

Write `count_csv_labels(csv_path: Path, column: str = 'label') -> dict[str, int]`.

### Thinking Blueprint

- Open with `encoding='utf-8', newline=''` and wrap with `csv.DictReader(f)`.

### Progressive Hints

1. `val = (row.get(column) or '').strip()`

### Dry-Run Trace
Rows `' pos '`, `''`, `'neg'`, `'pos'` -> `{'pos': 2, 'neg': 1}`.

### Answer & Explanation
```python
import csv
from pathlib import Path

def count_csv_labels(csv_path: Path, column: str = 'label') -> dict[str, int]:
    counts: dict[str, int] = {}
    with csv_path.open('r', encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f):
            val = (row.get(column) or '').strip()
            if val:
                counts[val] = counts.get(val, 0) + 1
    return counts
```

**High-Level Blocks:** `DictReader` reads rows by header name and counts non-blank labels.
