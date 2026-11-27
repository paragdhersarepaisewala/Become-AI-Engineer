"""Starter exercises — implement each function and run pytest on test_problems.py."""


# --- 1.1: Warm-Up: Loop + Condition + Dictionary Summary ---
def grade_summary(scores: list[int]) -> dict[str, int]:
    # TODO: count how many scores are >= 60 vs < 60
    pass

if __name__ == '__main__':
    print(grade_summary([40, 60, 85, 59]))


# --- 1.2: Warm-Up: Safe Dictionary Lookup & Cleaning Strings ---
def format_badge(user: dict) -> str:
    # TODO: safely read 'name' and 'role' without KeyError
    pass

if __name__ == '__main__':
    print(format_badge({'name': '  Sara ', 'role': ' ENGINEER '}))


# --- 1.3: File Basics: Count Non-Empty Lines in a `.txt` File ---
from pathlib import Path

def count_non_empty_lines(path: Path) -> int:
    # TODO: return 0 if missing, else count non-blank lines
    pass


# --- 1.4: Fix the Shared-Bucket Mutability Bug ---
def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    # TODO: avoid mutable default trap and caller mutation
    pass


# --- 1.5: File I/O: Safe JSONL Loader & Filtered Writer (`pathlib` + `json`) ---
import json
from pathlib import Path

def filter_jsonl_file(src: Path, dst: Path, min_chars: int = 5) -> int:
    # TODO: read src safely, filter records, write clean JSONL to dst
    pass


# --- 1.6: CSV Summary with `csv.DictReader` & `collections.Counter` ---
import csv
from collections import Counter
from pathlib import Path

def count_csv_labels(csv_path: Path, column: str = 'label') -> dict[str, int]:
    # TODO: read CSV with DictReader and count non-empty labels
    pass
