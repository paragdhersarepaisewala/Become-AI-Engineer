"""Starter exercises — implement each function and run pytest on test_problems.py."""


# --- 2.1: Text File Basics: Count Non-Empty Lines ---
from pathlib import Path

def count_non_empty_lines(path: Path) -> int:
    # TODO: return 0 if missing, else count non-blank lines
    pass


# --- 2.2: JSONL Filter & Nested Directory Writer ---
import json
from pathlib import Path

def filter_jsonl_file(src: Path, dst: Path, min_chars: int = 5) -> int:
    # TODO: read src, skip bad lines, filter by min_chars, write dst
    pass


# --- 2.3: CSV Summary With `csv.DictReader` ---
import csv
from pathlib import Path

def count_csv_labels(csv_path: Path, column: str = 'label') -> dict[str, int]:
    # TODO: read CSV and count labels
    pass
