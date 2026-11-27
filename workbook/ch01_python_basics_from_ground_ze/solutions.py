"""Reference solutions with explanations."""


# --- 1.1: Warm-Up: Loop + Condition + Dictionary Summary ---
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


# --- 1.2: Warm-Up: Safe Dictionary Lookup & Cleaning Strings ---
def format_badge(user: dict) -> str:
    raw_name = (user.get('name') or '').strip()
    raw_role = (user.get('role') or '').strip().lower()
    name = raw_name if raw_name else 'Guest'
    role = raw_role if raw_role else 'learner'
    return f'{name} ({role})'

if __name__ == '__main__':
    print(format_badge({'name': '  Sara ', 'role': ' ENGINEER '}))


# --- 1.3: File Basics: Count Non-Empty Lines in a `.txt` File ---
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


# --- 1.4: Fix the Shared-Bucket Mutability Bug ---
def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    result = [] if tags is None else list(tags)
    if tag not in result:
        result.append(tag)
    return result


# --- 1.5: File I/O: Safe JSONL Loader & Filtered Writer (`pathlib` + `json`) ---
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


# --- 1.6: CSV Summary with `csv.DictReader` & `collections.Counter` ---
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
