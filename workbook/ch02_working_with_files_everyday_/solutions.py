"""Reference solutions with explanations."""


# --- 2.1: Text File Basics: Count Non-Empty Lines ---
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


# --- 2.2: JSONL Filter & Nested Directory Writer ---
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


# --- 2.3: CSV Summary With `csv.DictReader` & `Counter` ---
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
