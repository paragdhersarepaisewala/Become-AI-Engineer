"""Phase 1 Practice Workbook (Chapters 1-7): Python Core, Files, `os` Automations, OOP, Logic, DSA/DP, Async."""

from __future__ import annotations

from typing import Any

PHASE_1_WORKBOOK: list[dict[str, Any]] = [
    # ---------------- CHAPTER 1: Python Core & Comprehensions ----------------
    {
        "id": "wb-01-01",
        "chapter_id": "ch01",
        "number": "1.1",
        "title": "Warm-Up: Loop + Decision + Dictionary Summary",
        "topic": "Python",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Practice basic loops, if/else checks, and building a summary dictionary.",
        "prompt_markdown": (
            "Write `grade_summary(scores: list[int]) -> dict[str, int]` returning `{'passed': ..., 'failed': ...}`.\n"
            "- Score `>= 60` -> `'passed'`\n"
            "- Score `< 60` -> `'failed'`"
        ),
        "thinking_blueprint": [
            "Block 1 (Setup): Start with `counts = {'passed': 0, 'failed': 0}`.",
            "Block 2 (Loop): For each score `s`, increment `'passed'` if `s >= 60` else `'failed'`.",
            "Block 3 (Return): Return `counts`.",
        ],
        "hints": [
            "Initialize both keys to `0` before the loop.",
            "Inside `for s in scores:`, use `if s >= 60:` and `else:`.",
        ],
        "dry_run_trace": "| Round | `s` | `s >= 60?` | `counts` |\n|---|---|---|---|\n| 1 | 40 | No | `{'passed': 0, 'failed': 1}` |\n| 2 | 60 | Yes | `{'passed': 1, 'failed': 1}` |",
        "starter_code": (
            "def grade_summary(scores: list[int]) -> dict[str, int]:\n"
            "    # TODO: count how many scores are >= 60 vs < 60\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    print(grade_summary([40, 60, 85, 59]))\n"
        ),
        "solution_code": (
            "def grade_summary(scores: list[int]) -> dict[str, int]:\n"
            "    counts = {'passed': 0, 'failed': 0}\n"
            "    for s in scores:\n"
            "        if s >= 60:\n"
            "            counts['passed'] += 1\n"
            "        else:\n"
            "            counts['failed'] += 1\n"
            "    return counts\n\n"
            "if __name__ == '__main__':\n"
            "    print(grade_summary([40, 60, 85, 59]))\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Pre-seed counts, loop once updating the right key, then `return counts`.",
        "test_cases": [
            {"name": "mixed_scores", "code": "assert sol.grade_summary([40, 60, 85, 59]) == {'passed': 2, 'failed': 2}"},
            {"name": "empty_list", "code": "assert sol.grade_summary([]) == {'passed': 0, 'failed': 0}"},
        ],
    },
    {
        "id": "wb-01-02",
        "chapter_id": "ch01",
        "number": "1.2",
        "title": "One-Line Loop (Comprehension): Clean & Filter Names",
        "topic": "Python",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Write a one-line list comprehension `[expr for x in items if cond]`.",
        "prompt_markdown": (
            "Write `clean_names(names: list[str]) -> list[str]` that strips spaces, lowercases each name, "
            "and skips blank/whitespace-only entries using a list comprehension."
        ),
        "thinking_blueprint": [
            "Fold `[name.strip().lower() for name in names if name.strip()]`.",
        ],
        "hints": [
            "Filter condition at the end: `if name.strip()` skips `''` and `'   '`.",
        ],
        "dry_run_trace": "`'  Sara '` -> `'sara'`; `''` -> skipped.",
        "starter_code": (
            "def clean_names(names: list[str]) -> list[str]:\n"
            "    # TODO: strip & lowercase non-empty names\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    print(clean_names(['  Sara ', '', ' ALEX ', '   ']))\n"
        ),
        "solution_code": (
            "def clean_names(names: list[str]) -> list[str]:\n"
            "    return [name.strip().lower() for name in names if name.strip()]\n\n"
            "if __name__ == '__main__':\n"
            "    print(clean_names(['  Sara ', '', ' ALEX ', '   ']))\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** `[transform for item in collection if filter]` keeps only non-blank names and normalizes them.",
        "test_cases": [
            {"name": "clean_and_skip", "code": "assert sol.clean_names(['  Sara ', '', ' ALEX ', '   ']) == ['sara', 'alex']"},
            {"name": "all_blank", "code": "assert sol.clean_names(['', '  ']) == []"},
        ],
    },
    {
        "id": "wb-01-03",
        "chapter_id": "ch01",
        "number": "1.3",
        "title": "Function Basics: Discount Price Calculator",
        "topic": "Python",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Practice parameters, default values, input validation, and `return`.",
        "prompt_markdown": (
            "Write `apply_discount(price: float, discount_percent: float = 10.0) -> float` subtracting `discount_percent`% from `price` rounded to 2 decimals. "
            "Raise `ValueError('Invalid input')` if `price < 0` or `discount_percent < 0` or `discount_percent > 100`."
        ),
        "thinking_blueprint": [
            "Validate bad inputs first -> `raise ValueError('Invalid input')`.",
            "Compute `saved = price * (discount_percent / 100)` and `return round(price - saved, 2)`.",
        ],
        "hints": [
            "Use `return`, NOT `print()`.",
        ],
        "dry_run_trace": "`apply_discount(100)` -> `90.0`; `apply_discount(80, 25)` -> `60.0`.",
        "starter_code": (
            "def apply_discount(price: float, discount_percent: float = 10.0) -> float:\n"
            "    # TODO: validate inputs, subtract discount%, and return rounded price\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    print(apply_discount(100))\n"
        ),
        "solution_code": (
            "def apply_discount(price: float, discount_percent: float = 10.0) -> float:\n"
            "    if price < 0 or discount_percent < 0 or discount_percent > 100:\n"
            "        raise ValueError('Invalid input')\n"
            "    saved = price * (discount_percent / 100)\n"
            "    return round(price - saved, 2)\n\n"
            "if __name__ == '__main__':\n"
            "    print(apply_discount(100))\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Validate bad inputs first, compute discount amount, and `return` the rounded float.",
        "test_cases": [
            {"name": "default_and_custom", "code": "assert sol.apply_discount(100) == 90.0\nassert sol.apply_discount(80, 25) == 60.0"},
            {"name": "invalid_inputs", "code": "try:\n    sol.apply_discount(-10)\n    assert False\nexcept ValueError:\n    pass"},
        ],
    },
    {
        "id": "wb-01-04",
        "chapter_id": "ch01",
        "number": "1.4",
        "title": "Error Handling: Safe Integer List Parser",
        "topic": "Python",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Use `try / except ValueError` to convert valid strings into integers and skip bad entries safely.",
        "prompt_markdown": (
            "Write `parse_ints(items: list[str]) -> list[int]` that tries `int(x.strip())` on each string, "
            "keeps valid integers, and skips entries like `'abc'` or `''` using `try / except ValueError` (do NOT crash!)."
        ),
        "thinking_blueprint": [
            "Start `out: list[int] = []`.",
            "Loop over `items`: inside `try:`, append `int(x.strip())`; inside `except ValueError:`, `continue`.",
        ],
        "hints": [
            "Only catch `ValueError`, never bare `except:`.",
        ],
        "dry_run_trace": (
            "`[' 10 ', 'abc', '-5', '']` -> `10` (ok), `'abc'` (ValueError -> skip), `-5` (ok), `''` (ValueError -> skip) -> `[10, -5]`."
        ),
        "starter_code": (
            "def parse_ints(items: list[str]) -> list[int]:\n"
            "    # TODO: convert valid strings to int and skip invalid ones using try/except ValueError\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    print(parse_ints([' 10 ', 'abc', '-5', '']))\n"
        ),
        "solution_code": (
            "def parse_ints(items: list[str]) -> list[int]:\n"
            "    out: list[int] = []\n"
            "    for raw in items:\n"
            "        try:\n"
            "            out.append(int(raw.strip()))\n"
            "        except ValueError:\n"
            "            continue\n"
            "    return out\n\n"
            "if __name__ == '__main__':\n"
            "    print(parse_ints([' 10 ', 'abc', '-5', '']))\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** `try / except ValueError` isolates bad strings like `'abc'` so valid numbers still get collected cleanly.",
        "test_cases": [
            {"name": "parses_safely", "code": "assert sol.parse_ints([' 10 ', 'abc', '-5', '']) == [10, -5]"},
            {"name": "all_bad", "code": "assert sol.parse_ints(['x', '3.5']) == []"},
        ],
    },

    # ---------------- CHAPTER 2: Working With Files ----------------
    {
        "id": "wb-02-01",
        "chapter_id": "ch02",
        "number": "2.1",
        "title": "Text File Basics: Count Non-Empty Lines",
        "topic": "Files",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Open a `.txt` file safely with `Path` + `encoding='utf-8'` and handle missing files.",
        "prompt_markdown": "Write `count_non_empty_lines(path: Path) -> int`: return `0` if missing, otherwise count lines with text after `.strip()`.",
        "thinking_blueprint": ["Guard `if not path.exists(): return 0`.", "Stream lines via `with path.open('r', encoding='utf-8') as f:`."],
        "hints": ["`if line.strip():` skips blank and whitespace-only lines."],
        "dry_run_trace": "`'alpha\\n\\n   \\nbeta\\n'` -> `2`.",
        "starter_code": (
            "from pathlib import Path\n\n"
            "def count_non_empty_lines(path: Path) -> int:\n"
            "    # TODO: return 0 if missing, else count non-blank lines\n"
            "    pass\n"
        ),
        "solution_code": (
            "from pathlib import Path\n\n"
            "def count_non_empty_lines(path: Path) -> int:\n"
            "    if not path.exists():\n"
            "        return 0\n"
            "    count = 0\n"
            "    with path.open('r', encoding='utf-8') as f:\n"
            "        for line in f:\n"
            "            if line.strip():\n"
            "                count += 1\n"
            "    return count\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Path check prevents crashes; `with path.open(...)` streams lines and closes safely.",
        "test_cases": [
            {
                "name": "counts_and_missing",
                "code": (
                    "import tempfile\nfrom pathlib import Path\n"
                    "with tempfile.TemporaryDirectory() as d:\n"
                    "    assert sol.count_non_empty_lines(Path(d) / 'nope.txt') == 0\n"
                    "    p = Path(d) / 'notes.txt'\n"
                    "    p.write_text('alpha\\n\\n   \\nbeta\\n', encoding='utf-8')\n"
                    "    assert sol.count_non_empty_lines(p) == 2"
                ),
            },
        ],
    },
    {
        "id": "wb-02-02",
        "chapter_id": "ch02",
        "number": "2.2",
        "title": "JSONL Filter & Nested Directory Writer",
        "topic": "Files",
        "question_type": "Logic & Coding",
        "difficulty": "Intermediate",
        "summary": "Read JSONL skipping corrupt JSON via `try/except`, filter short text, and write clean JSONL.",
        "prompt_markdown": (
            "Write `filter_jsonl_file(src: Path, dst: Path, min_chars: int = 5) -> int` skipping broken JSON lines, "
            "keeping dicts with `len(rec['text'].strip()) >= min_chars`, creating `dst.parent`, writing JSONL, and returning the count."
        ),
        "thinking_blueprint": ["Isolate `json.JSONDecodeError` per line.", "Create `dst.parent.mkdir(parents=True, exist_ok=True)` before writing."],
        "hints": ["Check `isinstance(rec, dict)` and `isinstance(rec.get('text'), str)`."],
        "dry_run_trace": "`'{\"text\": \"hello world\"}'` -> kept; `'{broken'` -> skipped.",
        "starter_code": (
            "import json\nfrom pathlib import Path\n\n"
            "def filter_jsonl_file(src: Path, dst: Path, min_chars: int = 5) -> int:\n"
            "    # TODO: read src, skip bad lines, filter by min_chars, write dst\n"
            "    pass\n"
        ),
        "solution_code": (
            "import json\nfrom pathlib import Path\n\n"
            "def filter_jsonl_file(src: Path, dst: Path, min_chars: int = 5) -> int:\n"
            "    if not src.exists():\n"
            "        raise FileNotFoundError(f'Missing file: {src}')\n"
            "    kept: list[dict] = []\n"
            "    with src.open('r', encoding='utf-8') as f:\n"
            "        for raw in f:\n"
            "            line = raw.strip()\n"
            "            if not line:\n"
            "                continue\n"
            "            try:\n"
            "                rec = json.loads(line)\n"
            "            except json.JSONDecodeError:\n"
            "                continue\n"
            "            text = rec.get('text') if isinstance(rec, dict) else None\n"
            "            if isinstance(text, str) and len(text.strip()) >= min_chars:\n"
            "                kept.append(rec)\n"
            "    dst.parent.mkdir(parents=True, exist_ok=True)\n"
            "    with dst.open('w', encoding='utf-8') as out:\n"
            "        for rec in kept:\n"
            "            out.write(json.dumps(rec) + '\\n')\n"
            "    return len(kept)\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Resilient line parser + directory-safe writer.",
        "test_cases": [
            {
                "name": "filters_corrupt_and_short",
                "code": (
                    "import json, tempfile\nfrom pathlib import Path\n"
                    "with tempfile.TemporaryDirectory() as d:\n"
                    "    src = Path(d) / 'in.jsonl'\n"
                    "    dst = Path(d) / 'nested' / 'out.jsonl'\n"
                    "    src.write_text('{\"text\": \"hello world\"}\\n{broken\\n{\"text\": \"hi\"}\\n', encoding='utf-8')\n"
                    "    assert sol.filter_jsonl_file(src, dst, min_chars=5) == 1\n"
                    "    assert json.loads(dst.read_text(encoding='utf-8').strip()) == {'text': 'hello world'}"
                ),
            },
        ],
    },
    {
        "id": "wb-02-03",
        "chapter_id": "ch02",
        "number": "2.3",
        "title": "CSV Summary With `csv.DictReader`",
        "topic": "Files",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Read CSV rows by column header and count non-empty labels.",
        "prompt_markdown": "Write `count_csv_labels(csv_path: Path, column: str = 'label') -> dict[str, int]`.",
        "thinking_blueprint": ["Open with `encoding='utf-8', newline=''` and wrap with `csv.DictReader(f)`."],
        "hints": ["`val = (row.get(column) or '').strip()`"],
        "dry_run_trace": "Rows `' pos '`, `''`, `'neg'`, `'pos'` -> `{'pos': 2, 'neg': 1}`.",
        "starter_code": (
            "import csv\nfrom pathlib import Path\n\n"
            "def count_csv_labels(csv_path: Path, column: str = 'label') -> dict[str, int]:\n"
            "    # TODO: read CSV and count labels\n"
            "    pass\n"
        ),
        "solution_code": (
            "import csv\nfrom pathlib import Path\n\n"
            "def count_csv_labels(csv_path: Path, column: str = 'label') -> dict[str, int]:\n"
            "    counts: dict[str, int] = {}\n"
            "    with csv_path.open('r', encoding='utf-8', newline='') as f:\n"
            "        for row in csv.DictReader(f):\n"
            "            val = (row.get(column) or '').strip()\n"
            "            if val:\n"
            "                counts[val] = counts.get(val, 0) + 1\n"
            "    return counts\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** `DictReader` reads rows by header name and counts non-blank labels.",
        "test_cases": [
            {
                "name": "counts_csv",
                "code": (
                    "import tempfile\nfrom pathlib import Path\n"
                    "with tempfile.TemporaryDirectory() as d:\n"
                    "    p = Path(d) / 'data.csv'\n"
                    "    p.write_text('id,label\\n1, pos \\n2,\\n3,neg\\n4,pos\\n', encoding='utf-8')\n"
                    "    assert sol.count_csv_labels(p) == {'pos': 2, 'neg': 1}"
                ),
            },
        ],
    },

    # ---------------- CHAPTER 3: Dedicated `os` Library & Automations ----------------
    {
        "id": "wb-03-01",
        "chapter_id": "ch03",
        "number": "3.1",
        "title": "`os` Scanner: Count Files by Extension",
        "topic": "os Library",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Use `os.listdir`, `os.path.join`, `os.path.isfile`, and `os.path.splitext` safely.",
        "prompt_markdown": (
            "Write `count_extensions(folder: str) -> dict[str, int]` that inspects **files only** inside `folder` "
            "(ignoring subfolders!) and returns counts keyed by lowercase extension (e.g. `'.txt'`, `'.png'`, or `'none'` if no extension)."
        ),
        "thinking_blueprint": [
            "Loop `for name in os.listdir(folder):` and build `full = os.path.join(folder, name)`.",
            "Skip if `not os.path.isfile(full)`.",
            "Split `_, ext = os.path.splitext(name)` -> lowercase or `'none'`.",
        ],
        "hints": [
            "Remember `os.listdir` returns filenames only—always `os.path.join(folder, name)` before checking `isfile`!",
        ],
        "dry_run_trace": "`['a.TXT', 'b.txt', 'subdir/']` -> `subdir` skipped -> `{'.txt': 2}`.",
        "starter_code": (
            "import os\n\n"
            "def count_extensions(folder: str) -> dict[str, int]:\n"
            "    # TODO: count files (not folders!) by lowercase extension\n"
            "    pass\n"
        ),
        "solution_code": (
            "import os\n\n"
            "def count_extensions(folder: str) -> dict[str, int]:\n"
            "    counts: dict[str, int] = {}\n"
            "    for name in os.listdir(folder):\n"
            "        full = os.path.join(folder, name)\n"
            "        if not os.path.isfile(full):\n"
            "            continue\n"
            "        _, ext = os.path.splitext(name)\n"
            "        key = ext.lower() if ext else 'none'\n"
            "        counts[key] = counts.get(key, 0) + 1\n"
            "    return counts\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Join folder + filename first, guard with `os.path.isfile`, then split extension cleanly.",
        "test_cases": [
            {
                "name": "counts_files_only",
                "code": (
                    "import os, tempfile\n"
                    "with tempfile.TemporaryDirectory() as d:\n"
                    "    os.makedirs(os.path.join(d, 'subfolder'))\n"
                    "    open(os.path.join(d, 'A.TXT'), 'w').close()\n"
                    "    open(os.path.join(d, 'b.txt'), 'w').close()\n"
                    "    open(os.path.join(d, 'README'), 'w').close()\n"
                    "    assert sol.count_extensions(d) == {'.txt': 2, 'none': 1}"
                ),
            },
        ],
    },
    {
        "id": "wb-03-02",
        "chapter_id": "ch03",
        "number": "3.2",
        "title": "`os` Automation: Organize Messy Folder Into Buckets",
        "topic": "os Library",
        "question_type": "Systems",
        "difficulty": "Intermediate",
        "summary": "Build a real folder-cleaning automation with `os.makedirs` and `os.rename`.",
        "prompt_markdown": (
            "Write `organize_files(folder: str) -> dict[str, int]` that moves every file in `folder` into a subfolder:\n"
            "- `.png` / `.jpg` -> `'images'`\n"
            "- `.txt` / `.md` -> `'docs'`\n"
            "- anything else -> `'other'`\n"
            "Ignore existing subfolders and return counts of files moved per bucket."
        ),
        "thinking_blueprint": [
            "Map extension -> bucket folder name.",
            "Call `os.makedirs(dest_dir, exist_ok=True)` then `os.rename(src, dest)`.",
        ],
        "hints": [
            "Skip directories with `if not os.path.isfile(src): continue`.",
        ],
        "dry_run_trace": "`['photo.png', 'notes.md', 'data.csv']` -> moves into `images/`, `docs/`, `other/` and returns `{'images': 1, 'docs': 1, 'other': 1}`.",
        "starter_code": (
            "import os\n\n"
            "def organize_files(folder: str) -> dict[str, int]:\n"
            "    # TODO: move files into images/, docs/, or other/ using os\n"
            "    pass\n"
        ),
        "solution_code": (
            "import os\n\n"
            "def organize_files(folder: str) -> dict[str, int]:\n"
            "    moved: dict[str, int] = {}\n"
            "    for name in os.listdir(folder):\n"
            "        src = os.path.join(folder, name)\n"
            "        if not os.path.isfile(src):\n"
            "            continue\n"
            "        _, ext = os.path.splitext(name)\n"
            "        ext = ext.lower()\n"
            "        if ext in ('.png', '.jpg'):\n"
            "            bucket = 'images'\n"
            "        elif ext in ('.txt', '.md'):\n"
            "            bucket = 'docs'\n"
            "        else:\n"
            "            bucket = 'other'\n"
            "        dest_dir = os.path.join(folder, bucket)\n"
            "        os.makedirs(dest_dir, exist_ok=True)\n"
            "        os.rename(src, os.path.join(dest_dir, name))\n"
            "        moved[bucket] = moved.get(bucket, 0) + 1\n"
            "    return moved\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Classify by extension, create destination folder safely with `exist_ok=True`, and move via `os.rename`.",
        "test_cases": [
            {
                "name": "organizes_cleanly",
                "code": (
                    "import os, tempfile\n"
                    "with tempfile.TemporaryDirectory() as d:\n"
                    "    for fn in ['pic.jpg', 'todo.md', 'raw.csv']:\n"
                    "        open(os.path.join(d, fn), 'w').close()\n"
                    "    res = sol.organize_files(d)\n"
                    "    assert res == {'images': 1, 'docs': 1, 'other': 1}\n"
                    "    assert os.path.isfile(os.path.join(d, 'images', 'pic.jpg'))\n"
                    "    assert os.path.isfile(os.path.join(d, 'docs', 'todo.md'))"
                ),
            },
        ],
    },

    # ---------------- CHAPTER 4: Beginner-Friendly OOP ----------------
    {
        "id": "wb-04-01",
        "chapter_id": "ch04",
        "number": "4.1",
        "title": "First Class & Methods: Build a `BankAccount`",
        "topic": "OOP",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Practice `__init__`, `self`, and methods that validate and update object state.",
        "prompt_markdown": "Build `BankAccount(owner, balance=0.0)` with `deposit(amount)` (`ValueError` if `<=0`) and `withdraw(amount) -> bool`.",
        "thinking_blueprint": ["Save `self.owner` and `self.balance` in `__init__`.", "Guard `<= 0` amounts."],
        "hints": ["Always put `self` as the first parameter of every method."],
        "dry_run_trace": "`a = BankAccount('Sara', 100); a.deposit(50)` -> `150`.",
        "starter_code": (
            "class BankAccount:\n"
            "    def __init__(self, owner: str, balance: float = 0.0) -> None:\n"
            "        pass\n\n"
            "    def deposit(self, amount: float) -> None:\n"
            "        pass\n\n"
            "    def withdraw(self, amount: float) -> bool:\n"
            "        pass\n\n"
            "if __name__ == '__main__':\n"
            "    acc = BankAccount('Sara', 100.0)\n"
            "    acc.deposit(50.0)\n"
            "    print(acc.owner, acc.balance)\n"
        ),
        "solution_code": (
            "class BankAccount:\n"
            "    def __init__(self, owner: str, balance: float = 0.0) -> None:\n"
            "        self.owner = owner\n"
            "        self.balance = balance\n\n"
            "    def deposit(self, amount: float) -> None:\n"
            "        if amount <= 0:\n"
            "            raise ValueError('Deposit must be positive')\n"
            "        self.balance += amount\n\n"
            "    def withdraw(self, amount: float) -> bool:\n"
            "        if amount <= 0 or amount > self.balance:\n"
            "            return False\n"
            "        self.balance -= amount\n"
            "        return True\n\n"
            "if __name__ == '__main__':\n"
            "    acc = BankAccount('Sara', 100.0)\n"
            "    acc.deposit(50.0)\n"
            "    print(acc.owner, acc.balance)\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** `self` isolates each account's balance, and methods validate state changes.",
        "test_cases": [
            {
                "name": "account_ops",
                "code": (
                    "a = sol.BankAccount('Sara', 100)\nb = sol.BankAccount('Alex', 20)\na.deposit(50)\n"
                    "assert a.balance == 150 and b.balance == 20\n"
                    "assert a.withdraw(200) is False and a.withdraw(40) is True and a.balance == 110"
                ),
            },
        ],
    },
    {
        "id": "wb-04-02",
        "chapter_id": "ch04",
        "number": "4.2",
        "title": "Composition & `@dataclass`: `Song` + `Playlist`",
        "topic": "OOP",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Build two cooperating classes using `@dataclass` and `__len__`.",
        "prompt_markdown": "Implement `@dataclass class Song(title: str, seconds: int)` and `class Playlist` with `add(song)`, `total_seconds() -> int`, and `__len__() -> int`.",
        "thinking_blueprint": ["`Playlist.__init__` sets `self.songs = []`."],
        "hints": ["`return sum(s.seconds for s in self.songs)`"],
        "dry_run_trace": "`Intro (90s) + Main (210s)` -> `len == 2`, `total_seconds == 300`.",
        "starter_code": (
            "from dataclasses import dataclass\n\n"
            "@dataclass\n"
            "class Song:\n"
            "    title: str\n"
            "    seconds: int\n\n"
            "class Playlist:\n"
            "    def __init__(self) -> None:\n"
            "        pass\n\n"
            "    def add(self, song: Song) -> None:\n"
            "        pass\n\n"
            "    def total_seconds(self) -> int:\n"
            "        pass\n\n"
            "    def __len__(self) -> int:\n"
            "        pass\n"
        ),
        "solution_code": (
            "from dataclasses import dataclass\n\n"
            "@dataclass\n"
            "class Song:\n"
            "    title: str\n"
            "    seconds: int\n\n"
            "class Playlist:\n"
            "    def __init__(self) -> None:\n"
            "        self.songs: list[Song] = []\n\n"
            "    def add(self, song: Song) -> None:\n"
            "        self.songs.append(song)\n\n"
            "    def total_seconds(self) -> int:\n"
            "        return sum(s.seconds for s in self.songs)\n\n"
            "    def __len__(self) -> int:\n"
            "        return len(self.songs)\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Composition (`Playlist` holding `Song` objects) keeps each class small.",
        "test_cases": [
            {"name": "playlist", "code": "pl = sol.Playlist()\npl.add(sol.Song('Intro', 90))\npl.add(sol.Song('Main', 210))\nassert len(pl) == 2 and pl.total_seconds() == 300"},
        ],
    },
    {
        "id": "wb-04-03",
        "chapter_id": "ch04",
        "number": "4.3",
        "title": "Callable Objects (`__call__`): Composable Text Pipeline",
        "topic": "OOP",
        "question_type": "Logic & Coding",
        "difficulty": "Intermediate",
        "summary": "Implement small `__call__` step classes and compose them inside `Pipeline`.",
        "prompt_markdown": "Implement `StripWhitespace`, `ReplaceWord(old, new)`, and `Pipeline(steps)` where each has `__call__(self, text: str) -> str`.",
        "thinking_blueprint": ["Each step holds config in `__init__` and runs in `__call__`."],
        "hints": ["`' '.join(text.split())` collapses extra whitespace cleanly."],
        "dry_run_trace": "`Pipeline([StripWhitespace(), ReplaceWord('ml', 'AI')])('  learn   ml ')` -> `'learn AI'`.",
        "starter_code": (
            "class StripWhitespace:\n"
            "    def __call__(self, text: str) -> str:\n"
            "        pass\n\n"
            "class ReplaceWord:\n"
            "    def __init__(self, old: str, new: str) -> None:\n"
            "        pass\n\n"
            "    def __call__(self, text: str) -> str:\n"
            "        pass\n\n"
            "class Pipeline:\n"
            "    def __init__(self, steps: list) -> None:\n"
            "        pass\n\n"
            "    def __call__(self, text: str) -> str:\n"
            "        pass\n"
        ),
        "solution_code": (
            "class StripWhitespace:\n"
            "    def __call__(self, text: str) -> str:\n"
            "        return ' '.join(text.split())\n\n"
            "class ReplaceWord:\n"
            "    def __init__(self, old: str, new: str) -> None:\n"
            "        self.old = old\n"
            "        self.new = new\n\n"
            "    def __call__(self, text: str) -> str:\n"
            "        words = []\n"
            "        for w in text.split():\n"
            "            if w == self.old:\n"
            "                words.append(self.new)\n"
            "            else:\n"
            "                words.append(w)\n"
            "        return ' '.join(words)\n\n"
            "class Pipeline:\n"
            "    def __init__(self, steps: list) -> None:\n"
            "        self.steps = list(steps)\n\n"
            "    def __call__(self, text: str) -> str:\n"
            "        out = text\n"
            "        for step in self.steps:\n"
            "            out = step(out)\n"
            "        return out\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Uniform `__call__` interfaces plug together just like PyTorch `nn.Sequential` and LangChain LCEL.",
        "test_cases": [
            {"name": "pipeline", "code": "p = sol.Pipeline([sol.StripWhitespace(), sol.ReplaceWord('ml', 'AI')])\nassert p('  learn   ml   fast ') == 'learn AI fast'"},
        ],
    },

    # ---------------- CHAPTER 5: Step-by-Step Logic Building ----------------
    {
        "id": "wb-05-01",
        "chapter_id": "ch05",
        "number": "5.1",
        "title": "Basic Logic: Find Largest Number Manually (No `max()`)",
        "topic": "Logic",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Track `best` across positive and negative numbers without calling `max()`.",
        "prompt_markdown": "Write `find_max(nums: list[int])` returning `None` if empty, else the largest int (must handle `[-10, -3, -20] -> -3`).",
        "thinking_blueprint": ["Start `best = nums[0]` (not `0`!) after guarding `if not nums:`."],
        "hints": ["Loop `for n in nums[1:]:` and update `if n > best: best = n`."],
        "dry_run_trace": "`[-10, -3, -20]` -> `-3`.",
        "starter_code": (
            "def find_max(nums: list[int]):\n"
            "    # TODO: find largest without max() or sorted()\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    print(find_max([-10, -3, -20]))\n"
        ),
        "solution_code": (
            "def find_max(nums: list[int]):\n"
            "    if not nums:\n"
            "        return None\n"
            "    best = nums[0]\n"
            "    for n in nums[1:]:\n"
            "        if n > best:\n"
            "            best = n\n"
            "    return best\n\n"
            "if __name__ == '__main__':\n"
            "    print(find_max([-10, -3, -20]))\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Guard empty list, anchor `best` at `nums[0]`, scan once.",
        "test_cases": [
            {"name": "max_cases", "code": "assert sol.find_max([-10, -3, -20]) == -3\nassert sol.find_max([]) is None\nassert sol.find_max([4, 9, 2]) == 9"},
        ],
    },
    {
        "id": "wb-05-02",
        "chapter_id": "ch05",
        "number": "5.2",
        "title": "Grouping Logic: Group Words by First Letter",
        "topic": "Logic",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Group stripped words into a dict of lists keyed by lowercase first letter.",
        "prompt_markdown": "Write `group_by_first_letter(words: list[str]) -> dict[str, list[str]]` skipping blanks.",
        "thinking_blueprint": ["Strip word; if empty `continue`; initialize `groups[key] = []` if missing; append."],
        "hints": ["`key = w[0].lower()`"],
        "dry_run_trace": "`['Apple', '  ', 'ant', 'Ball']` -> `{'a': ['Apple', 'ant'], 'b': ['Ball']}`.",
        "starter_code": (
            "def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:\n"
            "    # TODO: group non-empty stripped words\n"
            "    pass\n"
        ),
        "solution_code": (
            "def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:\n"
            "    groups: dict[str, list[str]] = {}\n"
            "    for raw in words:\n"
            "        w = raw.strip()\n"
            "        if not w:\n"
            "            continue\n"
            "        key = w[0].lower()\n"
            "        if key not in groups:\n"
            "            groups[key] = []\n"
            "        groups[key].append(w)\n"
            "    return groups\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Clean & skip blanks first, create missing buckets, then append.",
        "test_cases": [
            {"name": "group", "code": "assert sol.group_by_first_letter(['Apple', '  ', 'ant', 'Ball']) == {'a': ['Apple', 'ant'], 'b': ['Ball']}"},
        ],
    },
    {
        "id": "wb-05-03",
        "chapter_id": "ch05",
        "number": "5.3",
        "title": "State Machine Logic: Run-Length Encoder",
        "topic": "Logic",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Track `current` character and streak `count`.",
        "prompt_markdown": "Write `compress_runs(text: str) -> str` turning `'aaabbc'` -> `'a3b2c1'`.",
        "thinking_blueprint": ["Track `current` and `count`, flush on change, and flush once after the loop."],
        "hints": ["Guard `if not text: return ''`."],
        "dry_run_trace": "`'aab'` -> `'a2b1'`.",
        "starter_code": "def compress_runs(text: str) -> str:\n    pass\n",
        "solution_code": (
            "def compress_runs(text: str) -> str:\n"
            "    if not text:\n"
            "        return ''\n"
            "    parts: list[str] = []\n"
            "    current = text[0]\n"
            "    count = 1\n"
            "    for ch in text[1:]:\n"
            "        if ch == current:\n"
            "            count += 1\n"
            "        else:\n"
            "            parts.append(f'{current}{count}')\n"
            "            current = ch\n"
            "            count = 1\n"
            "    parts.append(f'{current}{count}')\n"
            "    return ''.join(parts)\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Track streak state and flush the final group after the loop.",
        "test_cases": [
            {"name": "basic", "code": "assert sol.compress_runs('aaabbc') == 'a3b2c1'\nassert sol.compress_runs('') == ''"},
        ],
    },
    {
        "id": "wb-05-04",
        "chapter_id": "ch05",
        "number": "5.4",
        "title": "Sliding Window: Longest Unique Substring",
        "topic": "Logic",
        "question_type": "Logic & Coding",
        "difficulty": "Intermediate",
        "summary": "Maintain a duplicate-free window with `left` and `last_seen`.",
        "prompt_markdown": "Write `longest_unique_len(s: str) -> int` returning longest substring length with all distinct chars.",
        "thinking_blueprint": ["Jump `left = last_seen[ch] + 1` when `last_seen[ch] >= left`."],
        "hints": ["Never move `left` backwards."],
        "dry_run_trace": "`'pwwkew'` -> `3` (`'wke'`).",
        "starter_code": "def longest_unique_len(s: str) -> int:\n    pass\n",
        "solution_code": (
            "def longest_unique_len(s: str) -> int:\n"
            "    last_seen: dict[str, int] = {}\n"
            "    left = 0\n"
            "    best = 0\n"
            "    for right, ch in enumerate(s):\n"
            "        if ch in last_seen and last_seen[ch] >= left:\n"
            "            left = last_seen[ch] + 1\n"
            "        last_seen[ch] = right\n"
            "        best = max(best, right - left + 1)\n"
            "    return best\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Duplicate-free invariant in O(N).",
        "test_cases": [
            {"name": "examples", "code": "assert sol.longest_unique_len('abcabcbb') == 3\nassert sol.longest_unique_len('pwwkew') == 3"},
        ],
    },

    # ---------------- CHAPTER 6: DSA & Dynamic Programming ----------------
    {
        "id": "wb-06-01",
        "chapter_id": "ch06",
        "number": "6.1",
        "title": "DP Foundation: Climbing Stairs (`n = 60`)",
        "topic": "Dynamic Programming",
        "question_type": "DSA & DP",
        "difficulty": "Foundation",
        "summary": "Eliminate exponential recursion using bottom-up DP.",
        "prompt_markdown": "Climb `1` or `2` steps at a time. Write `climb_ways(n: int) -> int` (`climb_ways(0) == 1`).",
        "thinking_blueprint": ["`dp[i] = dp[i-1] + dp[i-2]`."],
        "hints": ["Use `prev2, prev1 = 1, 1`."],
        "dry_run_trace": "`0->1, 1->1, 2->2, 3->3, 4->5`.",
        "starter_code": "def climb_ways(n: int) -> int:\n    pass\n",
        "solution_code": (
            "def climb_ways(n: int) -> int:\n"
            "    if n <= 1:\n"
            "        return 1\n"
            "    prev2, prev1 = 1, 1\n"
            "    for _ in range(2, n + 1):\n"
            "        prev2, prev1 = prev1, prev2 + prev1\n"
            "    return prev1\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Bottom-up rolling variables compute each step once.",
        "test_cases": [
            {"name": "small_60", "code": "assert [sol.climb_ways(i) for i in range(6)] == [1, 1, 2, 3, 5, 8]\nassert sol.climb_ways(60) == 2504730781961"},
        ],
    },
    {
        "id": "wb-06-02",
        "chapter_id": "ch06",
        "number": "6.2",
        "title": "1D DP Choice Pattern: Minimum Coin Change",
        "topic": "Dynamic Programming",
        "question_type": "DSA & DP",
        "difficulty": "Intermediate",
        "summary": "Solve coin change where greedy fails (`[1,3,4], 6 -> 2`).",
        "prompt_markdown": "Return fewest coins summing to `amount`, or `-1` if impossible.",
        "thinking_blueprint": ["`dp[a] = min(dp[a], 1 + dp[a - c])`."],
        "hints": ["`dp = [amount + 1] * (amount + 1)` with `dp[0] = 0`."],
        "dry_run_trace": "`dp[6]` finds `1 + dp[3] = 2`.",
        "starter_code": "def min_coins(coins: list[int], amount: int) -> int:\n    pass\n",
        "solution_code": (
            "def min_coins(coins: list[int], amount: int) -> int:\n"
            "    inf = amount + 1\n"
            "    dp = [inf] * (amount + 1)\n"
            "    dp[0] = 0\n"
            "    for a in range(1, amount + 1):\n"
            "        for c in coins:\n"
            "            if c <= a:\n"
            "                dp[a] = min(dp[a], 1 + dp[a - c])\n"
            "    if dp[amount] > amount:\n"
            "        return -1\n"
            "    return dp[amount]\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Evaluates every coin choice for each sub-amount.",
        "test_cases": [
            {"name": "coins", "code": "assert sol.min_coins([1, 3, 4], 6) == 2\nassert sol.min_coins([2], 3) == -1"},
        ],
    },
    {
        "id": "wb-06-03",
        "chapter_id": "ch06",
        "number": "6.3",
        "title": "2D DP Table: Levenshtein Edit Distance",
        "topic": "Dynamic Programming",
        "question_type": "DSA & DP",
        "difficulty": "Challenge",
        "summary": "Compute minimum insert/delete/replace edits between two strings.",
        "prompt_markdown": "Write `edit_distance(a: str, b: str) -> int` (`'kitten'` -> `'sitting'` == `3`).",
        "thinking_blueprint": ["Equal -> `dp[i-1][j-1]`; else `1 + min(top, left, diag)`."],
        "hints": ["Initialize base row `0..n` and col `0..m`."],
        "dry_run_trace": "`'cat' -> 'cut'` == `1`.",
        "starter_code": "def edit_distance(a: str, b: str) -> int:\n    pass\n",
        "solution_code": (
            "def edit_distance(a: str, b: str) -> int:\n"
            "    m, n = len(a), len(b)\n"
            "    dp = [[0] * (n + 1) for _ in range(m + 1)]\n"
            "    for i in range(m + 1):\n"
            "        dp[i][0] = i\n"
            "    for j in range(n + 1):\n"
            "        dp[0][j] = j\n"
            "    for i in range(1, m + 1):\n"
            "        for j in range(1, n + 1):\n"
            "            if a[i - 1] == b[j - 1]:\n"
            "                dp[i][j] = dp[i - 1][j - 1]\n"
            "            else:\n"
            "                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])\n"
            "    return dp[m][n]\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Compares delete (`top`), insert (`left`), and match/replace (`diagonal`).",
        "test_cases": [
            {"name": "edit", "code": "assert sol.edit_distance('kitten', 'sitting') == 3\nassert sol.edit_distance('cat', 'cut') == 1"},
        ],
    },
    {
        "id": "wb-06-04",
        "chapter_id": "ch06",
        "number": "6.4",
        "title": "DAG Topological Sort (Pipeline Task Scheduler)",
        "topic": "DSA",
        "question_type": "DSA & DP",
        "difficulty": "Challenge",
        "summary": "Order dependent tasks with Kahn's algorithm + cycle detection.",
        "prompt_markdown": "Given `tasks` and `deps` `(a, b)`, return alphabetical topological order or raise `ValueError('Cycle detected')`.",
        "thinking_blueprint": ["Track `indeg` and `adj`, pop 0-indegree from `heapq`."],
        "hints": ["Check `len(order) != len(tasks)` for cycles."],
        "dry_run_trace": "`clean -> train -> eval`.",
        "starter_code": "import heapq\n\ndef schedule_tasks(tasks: list[str], deps: list[tuple[str, str]]) -> list[str]:\n    pass\n",
        "solution_code": (
            "import heapq\n\n"
            "def schedule_tasks(tasks: list[str], deps: list[tuple[str, str]]) -> list[str]:\n"
            "    adj: dict[str, list[str]] = {t: [] for t in tasks}\n"
            "    indeg: dict[str, int] = {t: 0 for t in tasks}\n"
            "    for src, dst in deps:\n"
            "        adj[src].append(dst)\n"
            "        indeg[dst] += 1\n"
            "    heap = [t for t in tasks if indeg[t] == 0]\n"
            "    heapq.heapify(heap)\n"
            "    order: list[str] = []\n"
            "    while heap:\n"
            "        cur = heapq.heappop(heap)\n"
            "        order.append(cur)\n"
            "        for nxt in adj[cur]:\n"
            "            indeg[nxt] -= 1\n"
            "            if indeg[nxt] == 0:\n"
            "                heapq.heappush(heap, nxt)\n"
            "    if len(order) != len(tasks):\n"
            "        raise ValueError('Cycle detected')\n"
            "    return order\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Graph + in-degree setup, min-heap execution, and cycle check.",
        "test_cases": [
            {"name": "dag", "code": "assert sol.schedule_tasks(['eval', 'clean', 'train'], [('clean', 'train'), ('train', 'eval')]) == ['clean', 'train', 'eval']"},
        ],
    },

    # ---------------- CHAPTER 7: Async Programming ----------------
    {
        "id": "wb-07-01",
        "chapter_id": "ch07",
        "number": "7.1",
        "title": "Async Concurrency: Bounded Batch Runner with Semaphore",
        "topic": "Async",
        "question_type": "Systems",
        "difficulty": "Foundation",
        "summary": "Run async tasks concurrently while enforcing max in-flight concurrency.",
        "prompt_markdown": "Write `async def run_bounded(items: list[str], worker, max_concurrent: int) -> list[str]`.",
        "thinking_blueprint": ["Wrap `worker(item)` in `async with sem:` and `asyncio.gather`."],
        "hints": ["`asyncio.gather` preserves original order."],
        "dry_run_trace": "At most `max_concurrent` workers run at the same instant.",
        "starter_code": "import asyncio\n\nasync def run_bounded(items: list[str], worker, max_concurrent: int) -> list[str]:\n    pass\n",
        "solution_code": (
            "import asyncio\n\n"
            "async def run_bounded(items: list[str], worker, max_concurrent: int) -> list[str]:\n"
            "    if max_concurrent < 1:\n"
            "        raise ValueError('max_concurrent must be >= 1')\n"
            "    sem = asyncio.Semaphore(max_concurrent)\n"
            "    async def guarded(item: str) -> str:\n"
            "        async with sem:\n"
            "            return await worker(item)\n"
            "    return list(await asyncio.gather(*(guarded(x) for x in items)))\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** `Semaphore` caps concurrency while `gather` overlaps waits.",
        "test_cases": [
            {
                "name": "bounded",
                "code": (
                    "import asyncio\nstate = {'active': 0, 'peak': 0}\n"
                    "async def w(x):\n    state['active'] += 1\n    state['peak'] = max(state['peak'], state['active'])\n"
                    "    await asyncio.sleep(0.02)\n    state['active'] -= 1\n    return x.upper()\n"
                    "res = asyncio.run(sol.run_bounded(['a', 'b', 'c', 'd'], w, 2))\n"
                    "assert res == ['A', 'B', 'C', 'D'] and state['peak'] <= 2"
                ),
            },
        ],
    },
    {
        "id": "wb-07-02",
        "chapter_id": "ch07",
        "number": "7.2",
        "title": "Async Retries with Exponential Backoff",
        "topic": "Async",
        "question_type": "Systems",
        "difficulty": "Intermediate",
        "summary": "Retry transient failures using non-blocking `asyncio.sleep`.",
        "prompt_markdown": "Write `async def retry_async(fn, max_retries: int = 3, base_delay: float = 0.01)`.",
        "thinking_blueprint": ["Loop `0..max_retries`, `await fn()`, on last failure re-raise else sleep exponentially."],
        "hints": ["Never use `time.sleep` inside `async def`!"],
        "dry_run_trace": "0.01s -> 0.02s -> succeeds.",
        "starter_code": "import asyncio\n\nasync def retry_async(fn, max_retries: int = 3, base_delay: float = 0.01):\n    pass\n",
        "solution_code": (
            "import asyncio\n\n"
            "async def retry_async(fn, max_retries: int = 3, base_delay: float = 0.01):\n"
            "    for attempt in range(max_retries + 1):\n"
            "        try:\n"
            "            return await fn()\n"
            "        except Exception:\n"
            "            if attempt == max_retries:\n"
            "                raise\n"
            "            await asyncio.sleep(base_delay * (2 ** attempt))\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Non-blocking exponential backoff protects rate-limited APIs.",
        "test_cases": [
            {
                "name": "retry",
                "code": (
                    "import asyncio\nstate = {'calls': 0}\n"
                    "async def flaky():\n    state['calls'] += 1\n    if state['calls'] < 3: raise RuntimeError('429')\n    return 'ok'\n"
                    "assert asyncio.run(sol.retry_async(flaky, max_retries=3, base_delay=0.005)) == 'ok' and state['calls'] == 3"
                ),
            },
        ],
    },
]
