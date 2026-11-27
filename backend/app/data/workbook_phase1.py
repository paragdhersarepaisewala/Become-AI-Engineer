"""Phase 1 Practice Workbook (Chapters 1-5): Python Revision & Files, OOP, Logic, DSA & DP, Asyncio."""

from __future__ import annotations

from typing import Any

PHASE_1_WORKBOOK: list[dict[str, Any]] = [
    # ---------------- CHAPTER 1: Python Revision & Files ----------------
    {
        "id": "wb-01-00a",
        "chapter_id": "ch01",
        "number": "1.1",
        "title": "Warm-Up: Loop + Condition + Dictionary Summary",
        "topic": "Python",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Practice basic loops, if/else checks, and building a summary dictionary from a list of scores.",
        "prompt_markdown": (
            "Write a function `grade_summary(scores: list[int]) -> dict[str, int]` that checks every score in `scores` and returns "
            "`{'passed': ..., 'failed': ...}`.\n"
            "- A score **>= 60** counts as `'passed'`.\n"
            "- A score **< 60** counts as `'failed'`.\n\n"
            "**Example:** `grade_summary([40, 60, 85, 59])` returns `{'passed': 2, 'failed': 2}`."
        ),
        "thinking_blueprint": [
            "Block 1 (Setup): Start with `counts = {'passed': 0, 'failed': 0}`.",
            "Block 2 (Loop & Decision): For each `s` in `scores`, if `s >= 60` add 1 to `counts['passed']`, else add 1 to `counts['failed']`.",
            "Block 3 (Return): Return `counts` (not print!).",
        ],
        "hints": [
            "Start with `counts = {'passed': 0, 'failed': 0}` so empty lists also return `{'passed': 0, 'failed': 0}`.",
            "Inside `for s in scores:`, use `if s >= 60:` and `else:`.",
        ],
        "dry_run_trace": (
            "| Round | `s` | `s >= 60?` | `counts` |\n"
            "|---|---|---|---|\n"
            "| 1 | 40 | No | `{'passed': 0, 'failed': 1}` |\n"
            "| 2 | 60 | Yes | `{'passed': 1, 'failed': 1}` |\n"
            "| 3 | 85 | Yes | `{'passed': 2, 'failed': 1}` |\n"
            "| 4 | 59 | No | `{'passed': 2, 'failed': 2}` |"
        ),
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
        "explanation_markdown": (
            "**High-Level Blocks:** (1) Pre-initialize both dictionary keys to `0`; (2) Loop once over `scores` updating the right bucket; (3) `return` the dict."
        ),
        "test_cases": [
            {"name": "mixed_scores", "code": "assert sol.grade_summary([40, 60, 85, 59]) == {'passed': 2, 'failed': 2}"},
            {"name": "empty_list", "code": "assert sol.grade_summary([]) == {'passed': 0, 'failed': 0}"},
        ],
    },
    {
        "id": "wb-01-00b",
        "chapter_id": "ch01",
        "number": "1.2",
        "title": "Warm-Up: Safe Dictionary Lookup & Cleaning Strings",
        "topic": "Python",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Practice `.get()`, string `.strip()` / `.lower()`, and avoiding KeyError crashes.",
        "prompt_markdown": (
            "Given a dictionary `user` (which might be missing `'name'` or `'role'`), write `format_badge(user: dict) -> str` returning:\n"
            "`'<cleaned_name> (<cleaned_role>)'`\n"
            "- If `'name'` is missing or empty after stripping, default to `'Guest'` (keep original title/case or strip spaces, e.g. `'  Sara '` -> `'Sara'`).\n"
            "- If `'role'` is missing or empty after stripping, default to `'learner'`, and always lowercase the role."
        ),
        "thinking_blueprint": [
            "Block 1 (Safe Read): Use `(user.get('name') or '').strip()` so missing or `None` never crashes.",
            "Block 2 (Fallback): If empty string after `.strip()`, fall back to `'Guest'` / `'learner'`.",
            "Block 3 (Format): Return `f'{name} ({role})'`.",
        ],
        "hints": [
            "`raw_name = (user.get('name') or '').strip()`",
            "`name = raw_name if raw_name else 'Guest'`",
        ],
        "dry_run_trace": (
            "`{'name': '  Sara ', 'role': ' ENGINEER '}` -> `name='Sara'`, `role='engineer'` -> `'Sara (engineer)'`."
        ),
        "starter_code": (
            "def format_badge(user: dict) -> str:\n"
            "    # TODO: safely read 'name' and 'role' without KeyError\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    print(format_badge({'name': '  Sara ', 'role': ' ENGINEER '}))\n"
        ),
        "solution_code": (
            "def format_badge(user: dict) -> str:\n"
            "    raw_name = (user.get('name') or '').strip()\n"
            "    raw_role = (user.get('role') or '').strip().lower()\n"
            "    name = raw_name if raw_name else 'Guest'\n"
            "    role = raw_role if raw_role else 'learner'\n"
            "    return f'{name} ({role})'\n\n"
            "if __name__ == '__main__':\n"
            "    print(format_badge({'name': '  Sara ', 'role': ' ENGINEER '}))\n"
        ),
        "explanation_markdown": (
            "**High-Level Blocks:** Using `.get()` + `or ''` protects against both missing keys and `None` values, and `.strip()` cleans accidental spaces."
        ),
        "test_cases": [
            {"name": "clean_values", "code": "assert sol.format_badge({'name': '  Sara ', 'role': ' ENGINEER '}) == 'Sara (engineer)'"},
            {"name": "missing_keys", "code": "assert sol.format_badge({}) == 'Guest (learner)'\nassert sol.format_badge({'name': '   ', 'role': None}) == 'Guest (learner)'"},
        ],
    },
    {
        "id": "wb-01-00c",
        "chapter_id": "ch01",
        "number": "1.3",
        "title": "File Basics: Count Non-Empty Lines in a `.txt` File",
        "topic": "Files & Stdlib",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Open a plain text file safely with `Path`, `encoding='utf-8'`, and handle missing files cleanly.",
        "prompt_markdown": (
            "Write `count_non_empty_lines(path: Path) -> int` that:\n"
            "1. Returns `0` if `path` does not exist (do NOT crash!).\n"
            "2. Otherwise opens `path` with `encoding='utf-8'` and counts how many lines are non-empty after `.strip()`."
        ),
        "thinking_blueprint": [
            "Block 1 (Guard): `if not path.exists(): return 0` (or `try / except FileNotFoundError`).",
            "Block 2 (Read & Count): `with path.open('r', encoding='utf-8') as f:` loop line by line and count `if line.strip():`.",
        ],
        "hints": [
            "Remember `'   \\n'.strip()` becomes `''` (empty/False), so `if line.strip():` skips blank and whitespace-only lines!",
        ],
        "dry_run_trace": (
            "File with `'hello\\n\\n   \\nworld\\n'` -> `'hello'` (+1), `''` (skip), `'   '` (skip), `'world'` (+1) -> `2`."
        ),
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
        "explanation_markdown": (
            "**High-Level Blocks:** (1) Safe missing-file check prevents crashes; (2) `with path.open(...)` streams the file line by line and closes it automatically."
        ),
        "test_cases": [
            {
                "name": "counts_and_missing",
                "code": (
                    "import tempfile\nfrom pathlib import Path\n"
                    "with tempfile.TemporaryDirectory() as d:\n"
                    "    missing = Path(d) / 'nope.txt'\n"
                    "    assert sol.count_non_empty_lines(missing) == 0\n"
                    "    p = Path(d) / 'notes.txt'\n"
                    "    p.write_text('alpha\\n\\n   \\nbeta\\n', encoding='utf-8')\n"
                    "    assert sol.count_non_empty_lines(p) == 2"
                ),
            },
        ],
    },
    {
        "id": "wb-01-01",
        "chapter_id": "ch01",
        "number": "1.4",
        "title": "Fix the Shared-Bucket Mutability Bug",
        "topic": "Python",
        "question_type": "Trace & Bug Hunt",
        "difficulty": "Foundation",
        "summary": "Eliminate Python's mutable default argument and caller-list aliasing traps.",
        "prompt_markdown": (
            "Write `add_tag(tag: str, tags: list[str] | None = None) -> list[str]` that:\n"
            "1. Creates a fresh list when `tags` is `None`.\n"
            "2. **Never mutates** the caller's input list when `tags` is passed — returns a new list with `tag` added if not already present."
        ),
        "thinking_blueprint": [
            "Block 1 (Guard/Copy): If `tags is None` start with `[]`, else `list(tags)` creates an independent copy.",
            "Block 2 (Update): Append `tag` only if `tag not in result`, then return `result`.",
        ],
        "hints": [
            "Use `tags: list[str] | None = None` instead of `= []`.",
            "`result = [] if tags is None else list(tags)` isolates your new list from the caller's list.",
        ],
        "dry_run_trace": (
            "| Call | Input `tags` | `result` created | Output | Caller `base` |\n"
            "|---|---|---|---|---|\n"
            "| `add_tag('a')` | `None` | `[]` | `['a']` | N/A |\n"
            "| `add_tag('b')` | `None` | `[]` (fresh!) | `['b']` | N/A |\n"
            "| `add_tag('llm', base)` | `['ai']` | `['ai']` (copy) | `['ai', 'llm']` | `['ai']` |"
        ),
        "starter_code": (
            "def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:\n"
            "    # TODO: avoid mutable default trap and caller mutation\n"
            "    pass\n"
        ),
        "solution_code": (
            "def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:\n"
            "    result = [] if tags is None else list(tags)\n"
            "    if tag not in result:\n"
            "        result.append(tag)\n"
            "    return result\n"
        ),
        "explanation_markdown": (
            "**High-Level Blocks:** (1) *Defensive initialization* creates a fresh list object via `list(tags)` so caller state stays untouched; "
            "(2) *Deduplicated append* guarantees idempotency.\n\n**Complexity:** O(N) time and space."
        ),
        "test_cases": [
            {"name": "fresh_default_calls", "code": "assert sol.add_tag('a') == ['a']\nassert sol.add_tag('b') == ['b']"},
            {"name": "no_caller_mutation", "code": "base = ['ai']\nout = sol.add_tag('ml', base)\nassert out == ['ai', 'ml']\nassert base == ['ai']"},
            {"name": "dedup_existing_tag", "code": "assert sol.add_tag('ai', ['ai', 'py']) == ['ai', 'py']"},
        ],
    },
    {
        "id": "wb-01-02",
        "chapter_id": "ch01",
        "number": "1.5",
        "title": "File I/O: Safe JSONL Loader & Filtered Writer (`pathlib` + `json`)",
        "topic": "Files & Stdlib",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Open a JSONL file safely with UTF-8, skip corrupt lines with `try/except`, and write clean JSONL output.",
        "prompt_markdown": (
            "Write `filter_jsonl_file(src: Path, dst: Path, min_chars: int = 5) -> int` that:\n"
            "1. Reads `src` line-by-line with `encoding='utf-8'` (skip empty lines and malformed JSON lines cleanly).\n"
            "2. Keeps records where `isinstance(rec.get('text'), str)` and `len(rec['text'].strip()) >= min_chars`.\n"
            "3. Ensures `dst.parent` exists (`mkdir(parents=True, exist_ok=True)`), writes valid records as JSONL (`json.dumps` per line), and returns the count written."
        ),
        "thinking_blueprint": [
            "Block 1 (Input Read & Parse): Open `src` via `with src.open('r', encoding='utf-8')`, iterate lines, `try: rec = json.loads(line)` / `except json.JSONDecodeError: continue`.",
            "Block 2 (Validation Filter): Check `text` is a `str` and stripped length >= `min_chars`.",
            "Block 3 (Safe Output Write): Create `dst.parent`, write one JSON line per kept record, return `len(kept)`.",
        ],
        "hints": [
            "Check `if not src.exists(): raise FileNotFoundError(str(src))`.",
            "Use `dst.parent.mkdir(parents=True, exist_ok=True)` before opening `dst`.",
        ],
        "dry_run_trace": (
            "| Line | JSON parse | `text` length >= 5? | Written? |\n"
            "|---|---|---|---|\n"
            "| `'{\"text\": \"hello ai\"}'` | ok | yes (8) | Yes |\n"
            "| `'{bad json'` | JSONDecodeError | skipped | No |\n"
            "| `'{\"text\": \"hi\"}'` | ok | no (2) | No |"
        ),
        "starter_code": (
            "import json\n"
            "from pathlib import Path\n\n"
            "def filter_jsonl_file(src: Path, dst: Path, min_chars: int = 5) -> int:\n"
            "    # TODO: read src safely, filter records, write clean JSONL to dst\n"
            "    pass\n"
        ),
        "solution_code": (
            "import json\n"
            "from pathlib import Path\n\n"
            "def filter_jsonl_file(src: Path, dst: Path, min_chars: int = 5) -> int:\n"
            "    if not src.exists():\n"
            "        raise FileNotFoundError(f'Source file not found: {src}')\n"
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
        "explanation_markdown": (
            "**High-Level Blocks:** (1) *Path guard* fails loudly if `src` is missing; (2) *Resilient streaming parser* isolates `JSONDecodeError` to a single line; "
            "(3) *Directory-safe writer* ensures nested output folders exist before writing UTF-8 lines."
        ),
        "test_cases": [
            {
                "name": "filters_corrupt_and_short_lines",
                "code": (
                    "import json, tempfile\nfrom pathlib import Path\n"
                    "with tempfile.TemporaryDirectory() as d:\n"
                    "    src = Path(d) / 'in.jsonl'\n"
                    "    dst = Path(d) / 'nested' / 'out.jsonl'\n"
                    "    src.write_text('{\"text\": \"hello world\"}\\n{broken\\n{\"text\": \"hi\"}\\n\\n', encoding='utf-8')\n"
                    "    n = sol.filter_jsonl_file(src, dst, min_chars=5)\n"
                    "    assert n == 1\n"
                    "    lines = dst.read_text(encoding='utf-8').strip().splitlines()\n"
                    "    assert json.loads(lines[0]) == {'text': 'hello world'}"
                ),
            },
        ],
    },
    {
        "id": "wb-01-03",
        "chapter_id": "ch01",
        "number": "1.6",
        "title": "CSV Summary with `csv.DictReader` & `collections.Counter`",
        "topic": "Files & Stdlib",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Load a CSV file cleanly using standard libraries and aggregate counts per label.",
        "prompt_markdown": (
            "Write `count_csv_labels(csv_path: Path, column: str = 'label') -> dict[str, int]` that opens `csv_path` "
            "using `csv.DictReader`, skips rows where `column` is empty/whitespace, and returns a plain `dict[str, int]` "
            "mapping each stripped label to its occurrence count."
        ),
        "thinking_blueprint": [
            "Block 1 (File Context): Open with `encoding='utf-8', newline=''` as required by Python's `csv` module.",
            "Block 2 (Counter Aggregation): Use `collections.Counter` over non-empty stripped `row.get(column, '').strip()` values.",
        ],
        "hints": [
            "`newline=''` prevents blank-line bugs in Python's `csv` reader on Windows.",
            "Return `dict(counts)` so callers get a normal `dict`.",
        ],
        "dry_run_trace": (
            "CSV rows `[{'label': ' pos '}, {'label': ''}, {'label': 'neg'}, {'label': 'pos'}]` -> `{'pos': 2, 'neg': 1}`."
        ),
        "starter_code": (
            "import csv\n"
            "from collections import Counter\n"
            "from pathlib import Path\n\n"
            "def count_csv_labels(csv_path: Path, column: str = 'label') -> dict[str, int]:\n"
            "    # TODO: read CSV with DictReader and count non-empty labels\n"
            "    pass\n"
        ),
        "solution_code": (
            "import csv\n"
            "from collections import Counter\n"
            "from pathlib import Path\n\n"
            "def count_csv_labels(csv_path: Path, column: str = 'label') -> dict[str, int]:\n"
            "    counts: Counter[str] = Counter()\n"
            "    with csv_path.open('r', encoding='utf-8', newline='') as f:\n"
            "        for row in csv.DictReader(f):\n"
            "            val = (row.get(column) or '').strip()\n"
            "            if val:\n"
            "                counts[val] += 1\n"
            "    return dict(counts)\n"
        ),
        "explanation_markdown": (
            "**High-Level Blocks:** (1) `csv.DictReader` parses quoted commas safely by header name; (2) `(row.get(column) or '').strip()` handles missing or `None` cells cleanly; (3) `Counter` aggregates frequencies without manual key checks."
        ),
        "test_cases": [
            {
                "name": "counts_csv_safely",
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
    # ---------------- CHAPTER 2: OOP & Modularity ----------------
    {
        "id": "wb-02-01",
        "chapter_id": "ch02",
        "number": "2.1",
        "title": "OOP State & Dunders: Build a `DocumentStore` Class",
        "topic": "OOP",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Bundle state and operations inside a clean class supporting `len(store)` and `doc_id in store`.",
        "prompt_markdown": (
            "Implement `@dataclass class Document(doc_id: str, text: str)` and `class DocumentStore` with:\n"
            "- `add(doc: Document) -> None` (reject empty `doc.text.strip()` with `ValueError`)\n"
            "- `get(doc_id: str) -> Document | None`\n"
            "- `search(keyword: str) -> list[Document]` (case-insensitive substring match in `text`, preserving insertion order)\n"
            "- `__len__(self) -> int` and `__contains__(self, doc_id: str) -> bool`"
        ),
        "thinking_blueprint": [
            "Block 1 (`Document` dataclass): Holds `doc_id` and `text`.",
            "Block 2 (`DocumentStore.__init__`): Initializes `self._docs: dict[str, Document] = {}` (Python 3.7+ dicts preserve insertion order!).",
            "Block 3 (Methods & Dunders): Implement `add`, `get`, `search`, `__len__`, and `__contains__`.",
        ],
        "hints": [
            "Validate `if not doc.text.strip(): raise ValueError('Empty document')` inside `add()`.",
            "In `__contains__`, return `doc_id in self._docs`.",
        ],
        "dry_run_trace": (
            "`store.add(Document('1', 'Hello AI'))` -> `len(store) == 1`, `'1' in store is True`, `store.search('ai')` returns `[Document('1', 'Hello AI')]`."
        ),
        "starter_code": (
            "from dataclasses import dataclass\n\n"
            "@dataclass\n"
            "class Document:\n"
            "    doc_id: str\n"
            "    text: str\n\n"
            "class DocumentStore:\n"
            "    def __init__(self) -> None:\n"
            "        # TODO: initialize internal storage\n"
            "        pass\n\n"
            "    def add(self, doc: Document) -> None:\n"
            "        pass\n\n"
            "    def get(self, doc_id: str) -> Document | None:\n"
            "        pass\n\n"
            "    def search(self, keyword: str) -> list[Document]:\n"
            "        pass\n\n"
            "    def __len__(self) -> int:\n"
            "        pass\n\n"
            "    def __contains__(self, doc_id: str) -> bool:\n"
            "        pass\n"
        ),
        "solution_code": (
            "from dataclasses import dataclass\n\n"
            "@dataclass\n"
            "class Document:\n"
            "    doc_id: str\n"
            "    text: str\n\n"
            "class DocumentStore:\n"
            "    def __init__(self) -> None:\n"
            "        self._docs: dict[str, Document] = {}\n\n"
            "    def add(self, doc: Document) -> None:\n"
            "        if not doc.text.strip():\n"
            "            raise ValueError('Document text cannot be empty')\n"
            "        self._docs[doc.doc_id] = doc\n\n"
            "    def get(self, doc_id: str) -> Document | None:\n"
            "        return self._docs.get(doc_id)\n\n"
            "    def search(self, keyword: str) -> list[Document]:\n"
            "        q = keyword.lower()\n"
            "        return [d for d in self._docs.values() if q in d.text.lower()]\n\n"
            "    def __len__(self) -> int:\n"
            "        return len(self._docs)\n\n"
            "    def __contains__(self, doc_id: str) -> bool:\n"
            "        return doc_id in self._docs\n"
        ),
        "explanation_markdown": (
            "**High-Level Blocks:** (1) `@dataclass` models passive record data; (2) `DocumentStore` encapsulates `_docs` behind validated methods (`add` guards empty text); "
            "(3) Dunder methods (`__len__`, `__contains__`) integrate naturally with Python syntax (`len(store)`, `'id' in store`)."
        ),
        "test_cases": [
            {
                "name": "store_crud_and_dunders",
                "code": (
                    "s = sol.DocumentStore()\n"
                    "s.add(sol.Document('d1', 'Learn PyTorch'))\n"
                    "s.add(sol.Document('d2', 'Learn FastAPI'))\n"
                    "assert len(s) == 2 and 'd1' in s and 'd9' not in s\n"
                    "assert [d.doc_id for d in s.search('pytorch')] == ['d1']\n"
                    "try:\n    s.add(sol.Document('d3', '   '))\n    assert False\nexcept ValueError:\n    pass"
                ),
            },
        ],
    },
    {
        "id": "wb-02-02",
        "chapter_id": "ch02",
        "number": "2.2",
        "title": "OOP Composition & `__call__`: Composable Text Pipeline",
        "topic": "OOP",
        "question_type": "Logic & Coding",
        "difficulty": "Intermediate",
        "summary": "Implement small callable step classes and compose them cleanly (just like PyTorch Transforms & LangChain Runnables).",
        "prompt_markdown": (
            "Implement three classes:\n"
            "1. `StripWhitespace`: `__call__(self, text: str) -> str` collapses internal whitespace and strips ends.\n"
            "2. `ReplaceWord(old: str, new: str)`: `__call__(self, text: str) -> str` replaces exact whitespace-separated words matching `old` with `new`.\n"
            "3. `Pipeline(steps: list)`: `__call__(self, text: str) -> str` passes `text` sequentially through each step."
        ),
        "thinking_blueprint": [
            "Each transform class holds its config in `__init__` and runs its action in `__call__`.",
            "`Pipeline` uses **composition** (`self.steps`)—it doesn't inherit from any transform, it simply calls each step in order.",
        ],
        "hints": [
            "In `ReplaceWord`, split on whitespace (`text.split()`), swap `new if w == self.old else w`, and `' '.join(...)`.",
        ],
        "dry_run_trace": (
            "`Pipeline([StripWhitespace(), ReplaceWord('ml', 'AI')])('  hello   ml  ')` -> `'hello ml'` -> `'hello AI'`."
        ),
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
            "        return ' '.join(self.new if w == self.old else w for w in text.split())\n\n"
            "class Pipeline:\n"
            "    def __init__(self, steps: list) -> None:\n"
            "        self.steps = list(steps)\n\n"
            "    def __call__(self, text: str) -> str:\n"
            "        out = text\n"
            "        for step in self.steps:\n"
            "            out = step(out)\n"
            "        return out\n"
        ),
        "explanation_markdown": (
            "**High-Level Blocks:** This is the exact *Composable Runnable* design pattern behind PyTorch `nn.Sequential` and LangChain LCEL (`step1 | step2`). Every stage implements the same `__call__(x) -> y` contract."
        ),
        "test_cases": [
            {
                "name": "composed_pipeline",
                "code": (
                    "p = sol.Pipeline([sol.StripWhitespace(), sol.ReplaceWord('ml', 'AI')])\n"
                    "assert p('  learn   ml   fast ') == 'learn AI fast'"
                ),
            },
        ],
    },
    {
        "id": "wb-02-03",
        "chapter_id": "ch02",
        "number": "2.3",
        "title": "Pure Modular Log Line Parser",
        "topic": "OOP",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Separate pure parsing logic from file I/O while handling blank and corrupt lines safely.",
        "prompt_markdown": (
            "Write `parse_logs(lines: list[str]) -> dict[str, int]` counting `'INFO'`, `'WARN'`, `'ERROR'` from lines like "
            "`'[ERROR] Disk full'`, ignoring blank lines, missing brackets, or unknown levels."
        ),
        "thinking_blueprint": [
            "Block 1: Pre-seed `counts = {'INFO': 0, 'WARN': 0, 'ERROR': 0}`.",
            "Block 2: Guard-clause loop extracts `[LEVEL]` cleanly.",
        ],
        "hints": [
            "Check `if not s.startswith('[') or ']' not in s: continue`.",
        ],
        "dry_run_trace": (
            "`['[INFO] ok', 'junk', '[ERROR] x']` -> `{'INFO': 1, 'WARN': 0, 'ERROR': 1}`."
        ),
        "starter_code": (
            "def parse_logs(lines: list[str]) -> dict[str, int]:\n"
            "    # TODO: count INFO, WARN, ERROR ignoring invalid lines\n"
            "    pass\n"
        ),
        "solution_code": (
            "def parse_logs(lines: list[str]) -> dict[str, int]:\n"
            "    counts = {'INFO': 0, 'WARN': 0, 'ERROR': 0}\n"
            "    for line in lines:\n"
            "        s = line.strip()\n"
            "        if not s.startswith('[') or ']' not in s:\n"
            "            continue\n"
            "        level = s[1:s.index(']')].upper()\n"
            "        if level in counts:\n"
            "            counts[level] += 1\n"
            "    return counts\n"
        ),
        "explanation_markdown": (
            "**High-Level Blocks:** Pure function takes `list[str]` instead of a file path so it can be unit-tested in memory without touching disk."
        ),
        "test_cases": [
            {"name": "mixed_logs", "code": "assert sol.parse_logs(['[INFO] a', 'bad', '[ERROR] b', '[WARN] c']) == {'INFO': 1, 'WARN': 1, 'ERROR': 1}"},
            {"name": "empty_unknown", "code": "assert sol.parse_logs(['', '[DEBUG] x']) == {'INFO': 0, 'WARN': 0, 'ERROR': 0}"},
        ],
    },
    # ---------------- CHAPTER 3: Logic Building ----------------
    {
        "id": "wb-03-01",
        "chapter_id": "ch03",
        "number": "3.1",
        "title": "State Machine Logic: Run-Length Encoder",
        "topic": "Logic",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Build loop-state logic by compressing consecutive repeated characters.",
        "prompt_markdown": (
            "Write `compress_runs(text: str) -> str` turning `'aaabbc'` -> `'a3b2c1'`, `'x'` -> `'x1'`, `''` -> `''`."
        ),
        "thinking_blueprint": [
            "Track `current` char and streak `count`.",
            "Flush when character changes, AND flush the final streak after the loop ends.",
        ],
        "hints": [
            "Guard `if not text: return ''` first.",
        ],
        "dry_run_trace": (
            "`'aab'` -> `current='a', count=2` -> see `'b'` -> flush `'a2'`, reset `current='b', count=1` -> end loop -> flush `'b1'` -> `'a2b1'`."
        ),
        "starter_code": (
            "def compress_runs(text: str) -> str:\n"
            "    # TODO: track current character and streak count\n"
            "    pass\n"
        ),
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
        "explanation_markdown": (
            "**High-Level Blocks:** (1) Guard empty input; (2) Track current streak state; (3) Final flush outside the loop handles the last character group."
        ),
        "test_cases": [
            {"name": "basic", "code": "assert sol.compress_runs('aaabbc') == 'a3b2c1'"},
            {"name": "single_empty", "code": "assert sol.compress_runs('z') == 'z1'\nassert sol.compress_runs('') == ''"},
        ],
    },
    {
        "id": "wb-03-02",
        "chapter_id": "ch03",
        "number": "3.2",
        "title": "Hash Map Logic: First Unique Character Index",
        "topic": "Logic",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Use a two-pass frequency map to avoid O(N^2) scanning.",
        "prompt_markdown": (
            "Return the index of the first character in `s` appearing **exactly once**, or `-1` if none."
        ),
        "thinking_blueprint": [
            "Pass 1: Count every character with `dict`.",
            "Pass 2: Find first `(i, ch)` with `counts[ch] == 1`.",
        ],
        "hints": [
            "Use `counts.get(ch, 0) + 1` in pass 1.",
        ],
        "dry_run_trace": (
            "`'aabc'` -> `counts={'a':2, 'b':1, 'c':1}` -> `i=2 ('b')` has count 1 -> returns `2`."
        ),
        "starter_code": (
            "def first_unique_index(s: str) -> int:\n"
            "    # TODO: two-pass frequency map\n"
            "    pass\n"
        ),
        "solution_code": (
            "def first_unique_index(s: str) -> int:\n"
            "    counts: dict[str, int] = {}\n"
            "    for ch in s:\n"
            "        counts[ch] = counts.get(ch, 0) + 1\n"
            "    for i, ch in enumerate(s):\n"
            "        if counts[ch] == 1:\n"
            "            return i\n"
            "    return -1\n"
        ),
        "explanation_markdown": (
            "**High-Level Blocks:** Pass 1 gathers global knowledge (frequencies); Pass 2 uses that O(1) lookup table in original index order."
        ),
        "test_cases": [
            {"name": "found", "code": "assert sol.first_unique_index('loveai') == 0\nassert sol.first_unique_index('aabc') == 2"},
            {"name": "none", "code": "assert sol.first_unique_index('aabb') == -1\nassert sol.first_unique_index('') == -1"},
        ],
    },
    {
        "id": "wb-03-03",
        "chapter_id": "ch03",
        "number": "3.3",
        "title": "Dynamic Sliding Window: Longest Unique Substring",
        "topic": "Logic",
        "question_type": "Logic & Coding",
        "difficulty": "Intermediate",
        "summary": "Expand/shrink a window with `left`/`right` pointers and a `last_seen` map.",
        "prompt_markdown": (
            "Write `longest_unique_len(s: str) -> int` returning the length of the longest substring with all distinct characters."
        ),
        "thinking_blueprint": [
            "Maintain valid window `[left..right]`.",
            "If `ch` was seen inside the current window (`last_seen[ch] >= left`), jump `left = last_seen[ch] + 1`.",
        ],
        "hints": [
            "Never let `left` move backwards—always check `last_seen[ch] >= left`.",
        ],
        "dry_run_trace": (
            "`'pwwkew'`: at `right=2 ('w')`, `last_seen['w']=1 >= 0`, so `left` jumps to `2`; window `'wke'` reaches length `3`."
        ),
        "starter_code": (
            "def longest_unique_len(s: str) -> int:\n"
            "    # TODO: sliding window with left pointer and last_seen map\n"
            "    pass\n"
        ),
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
        "explanation_markdown": (
            "**High-Level Blocks:** (1) Window invariant check jumps `left` past duplicates; (2) Record latest index; (3) Update `best` window length."
        ),
        "test_cases": [
            {"name": "examples", "code": "assert sol.longest_unique_len('abcabcbb') == 3\nassert sol.longest_unique_len('pwwkew') == 3"},
            {"name": "edge_cases", "code": "assert sol.longest_unique_len('') == 0\nassert sol.longest_unique_len('bbbb') == 1"},
        ],
    },
    {
        "id": "wb-03-04",
        "chapter_id": "ch03",
        "number": "3.4",
        "title": "Recursion & Call Stack: Flatten Nested Lists",
        "topic": "Logic",
        "question_type": "Logic & Coding",
        "difficulty": "Intermediate",
        "summary": "Write base and recursive cases cleanly to flatten arbitrary-depth lists.",
        "prompt_markdown": (
            "Write `flatten(nested: list) -> list[int]` turning `[1, [2, [3, 4]], [], 5]` into `[1, 2, 3, 4, 5]`."
        ),
        "thinking_blueprint": [
            "If element is a `list`, recurse and `.extend()`.",
            "Else (base case), `.append()`.",
        ],
        "hints": [
            "Use `isinstance(item, list)`.",
        ],
        "dry_run_trace": (
            "`flatten([2, [3, 4]])` calls `flatten([3, 4])` -> `[3, 4]` -> returns `[2, 3, 4]`."
        ),
        "starter_code": (
            "def flatten(nested: list) -> list[int]:\n"
            "    # TODO: recursively flatten nested lists\n"
            "    pass\n"
        ),
        "solution_code": (
            "def flatten(nested: list) -> list[int]:\n"
            "    out: list[int] = []\n"
            "    for item in nested:\n"
            "        if isinstance(item, list):\n"
            "            out.extend(flatten(item))\n"
            "        else:\n"
            "            out.append(item)\n"
            "    return out\n"
        ),
        "explanation_markdown": (
            "**High-Level Blocks:** Each stack frame handles one nesting depth and merges child results cleanly via `.extend()`."
        ),
        "test_cases": [
            {"name": "nested", "code": "assert sol.flatten([1, [2, [3, 4]], [], 5]) == [1, 2, 3, 4, 5]"},
            {"name": "empty", "code": "assert sol.flatten([[], [[]]]) == []"},
        ],
    },
    # ---------------- CHAPTER 4: DSA & Dynamic Programming ----------------
    {
        "id": "wb-04-01",
        "chapter_id": "ch04",
        "number": "4.1",
        "title": "DP Foundation: Climbing Stairs (`n = 60`)",
        "topic": "Dynamic Programming",
        "question_type": "DSA & DP",
        "difficulty": "Foundation",
        "summary": "Eliminate exponential recursion using bottom-up DP state transitions.",
        "prompt_markdown": (
            "Climb `1` or `2` steps at a time. Write `climb_ways(n: int) -> int` (`climb_ways(0) == 1`) fast enough for `n = 60`."
        ),
        "thinking_blueprint": [
            "`dp[i] = dp[i-1] + dp[i-2]` with `dp[0]=1, dp[1]=1`.",
            "Keep only `prev2, prev1` in O(1) memory.",
        ],
        "hints": [
            "`prev2, prev1 = prev1, prev2 + prev1`.",
        ],
        "dry_run_trace": (
            "`n=0->1, 1->1, 2->2, 3->3, 4->5, 5->8`."
        ),
        "starter_code": (
            "def climb_ways(n: int) -> int:\n"
            "    # TODO: O(N) bottom-up DP\n"
            "    pass\n"
        ),
        "solution_code": (
            "def climb_ways(n: int) -> int:\n"
            "    if n <= 1:\n"
            "        return 1\n"
            "    prev2, prev1 = 1, 1\n"
            "    for _ in range(2, n + 1):\n"
            "        prev2, prev1 = prev1, prev2 + prev1\n"
            "    return prev1\n"
        ),
        "explanation_markdown": (
            "**High-Level Blocks:** Bottom-up rolling variables compute each step exactly once instead of ~2^60 redundant recursive calls."
        ),
        "test_cases": [
            {"name": "small", "code": "assert [sol.climb_ways(i) for i in range(6)] == [1, 1, 2, 3, 5, 8]"},
            {"name": "large_n60", "code": "assert sol.climb_ways(60) == 2504730781961"},
        ],
    },
    {
        "id": "wb-04-02",
        "chapter_id": "ch04",
        "number": "4.2",
        "title": "1D DP Choice Pattern: Minimum Coin Change",
        "topic": "Dynamic Programming",
        "question_type": "DSA & DP",
        "difficulty": "Intermediate",
        "summary": "Use a 1D DP table where greedy fails (`coins=[1,3,4], amount=6`).",
        "prompt_markdown": (
            "Return fewest coins from `coins` to sum to `amount`, or `-1` if impossible."
        ),
        "thinking_blueprint": [
            "`dp[a]` = min coins for amount `a`; `dp[0] = 0`.",
            "Try all `c <= a`: `dp[a] = min(dp[a], 1 + dp[a - c])`.",
        ],
        "hints": [
            "Initialize `dp = [amount + 1] * (amount + 1)` with `dp[0] = 0`.",
        ],
        "dry_run_trace": (
            "For `coins=[1,3,4], amount=6`: `dp[3]=1`, so `dp[6]` checks `1+dp[3]=2` -> returns `2`."
        ),
        "starter_code": (
            "def min_coins(coins: list[int], amount: int) -> int:\n"
            "    # TODO: 1D DP table\n"
            "    pass\n"
        ),
        "solution_code": (
            "def min_coins(coins: list[int], amount: int) -> int:\n"
            "    inf = amount + 1\n"
            "    dp = [inf] * (amount + 1)\n"
            "    dp[0] = 0\n"
            "    for a in range(1, amount + 1):\n"
            "        for c in coins:\n"
            "            if c <= a:\n"
            "                dp[a] = min(dp[a], 1 + dp[a - c])\n"
            "    return -1 if dp[amount] > amount else dp[amount]\n"
        ),
        "explanation_markdown": (
            "**High-Level Blocks:** (1) Sentinel `amount+1` represents unreachable states; (2) Inner coin loop tests every valid last coin and picks the minimum."
        ),
        "test_cases": [
            {"name": "non_greedy", "code": "assert sol.min_coins([1, 3, 4], 6) == 2"},
            {"name": "impossible_zero", "code": "assert sol.min_coins([2], 3) == -1\nassert sol.min_coins([1, 5], 0) == 0"},
        ],
    },
    {
        "id": "wb-04-03",
        "chapter_id": "ch04",
        "number": "4.3",
        "title": "2D DP Table: Levenshtein Edit Distance",
        "topic": "Dynamic Programming",
        "question_type": "DSA & DP",
        "difficulty": "Challenge",
        "summary": "Compute minimum insert/delete/replace edits between two strings.",
        "prompt_markdown": (
            "Write `edit_distance(a: str, b: str) -> int` returning minimum edits (`'kitten'` -> `'sitting'` == `3`)."
        ),
        "thinking_blueprint": [
            "`dp[i][j]` = edit distance between `a[:i]` and `b[:j]`.",
            "Equal chars -> `dp[i-1][j-1]`; else `1 + min(delete, insert, replace)`.",
        ],
        "hints": [
            "Initialize row 0 to `0..n` and col 0 to `0..m`.",
        ],
        "dry_run_trace": (
            "`'cat'` -> `'cut'`: `dp[3][3] == 1` (single replace `'a'->'u'`)."
        ),
        "starter_code": (
            "def edit_distance(a: str, b: str) -> int:\n"
            "    # TODO: 2D DP grid\n"
            "    pass\n"
        ),
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
        "explanation_markdown": (
            "**High-Level Blocks:** (1) Base edges represent converting to/from empty prefixes; (2) Interior transitions compare top (delete), left (insert), and diagonal (match/replace)."
        ),
        "test_cases": [
            {"name": "classic", "code": "assert sol.edit_distance('kitten', 'sitting') == 3\nassert sol.edit_distance('cat', 'cut') == 1"},
            {"name": "empty", "code": "assert sol.edit_distance('', 'abc') == 3\nassert sol.edit_distance('ai', 'ai') == 0"},
        ],
    },
    {
        "id": "wb-04-04",
        "chapter_id": "ch04",
        "number": "4.4",
        "title": "DAG Topological Sort (Pipeline Task Scheduler)",
        "topic": "DSA",
        "question_type": "DSA & DP",
        "difficulty": "Challenge",
        "summary": "Order dependent tasks with Kahn's BFS topological sort and detect cycles.",
        "prompt_markdown": (
            "Given `tasks` and `deps` (`(a, b)` means `a` runs before `b`), return deterministic topological order (alphabetical min-heap tie-break), "
            "or raise `ValueError('Cycle detected')` on cycles."
        ),
        "thinking_blueprint": [
            "Compute `indeg` and `adj` list.",
            "Pop 0-indegree tasks from a min-heap, decrement dependents, verify `len(order) == len(tasks)`.",
        ],
        "hints": [
            "Use `heapq` so ready tasks always pop in alphabetical order.",
        ],
        "dry_run_trace": (
            "`clean -> train -> eval` unlocks one task at a time in O((V+E) log V)."
        ),
        "starter_code": (
            "import heapq\n\n"
            "def schedule_tasks(tasks: list[str], deps: list[tuple[str, str]]) -> list[str]:\n"
            "    # TODO: Kahn's topological sort + cycle check\n"
            "    pass\n"
        ),
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
        "explanation_markdown": (
            "**High-Level Blocks:** (1) Graph + in-degree construction; (2) Min-heap processes ready nodes; (3) Length mismatch detects cycles cleanly."
        ),
        "test_cases": [
            {"name": "valid_dag", "code": "assert sol.schedule_tasks(['eval', 'clean', 'train'], [('clean', 'train'), ('train', 'eval')]) == ['clean', 'train', 'eval']"},
            {"name": "cycle", "code": "try:\n    sol.schedule_tasks(['a', 'b'], [('a', 'b'), ('b', 'a')])\n    assert False\nexcept ValueError:\n    pass"},
        ],
    },
    # ---------------- CHAPTER 5: Async Programming ----------------
    {
        "id": "wb-05-01",
        "chapter_id": "ch05",
        "number": "5.1",
        "title": "Async Concurrency: Bounded Batch Runner with Semaphore",
        "topic": "Async",
        "question_type": "Systems",
        "difficulty": "Foundation",
        "summary": "Run async tasks concurrently while strictly enforcing max in-flight concurrency.",
        "prompt_markdown": (
            "Write `async def run_bounded(items: list[str], worker, max_concurrent: int) -> list[str]` preserving input order "
            "and allowing at most `max_concurrent` workers simultaneously."
        ),
        "thinking_blueprint": [
            "Create `sem = asyncio.Semaphore(max_concurrent)`.",
            "Wrap each item in `async with sem: return await worker(item)` and gather all tasks.",
        ],
        "hints": [
            "`asyncio.gather` preserves input order even if later tasks finish first.",
        ],
        "dry_run_trace": (
            "With `max_concurrent=2`, tasks 0 & 1 enter together; task 2 waits until one releases the semaphore."
        ),
        "starter_code": (
            "import asyncio\n\n"
            "async def run_bounded(items: list[str], worker, max_concurrent: int) -> list[str]:\n"
            "    # TODO: bound concurrent worker calls with Semaphore\n"
            "    pass\n"
        ),
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
        "explanation_markdown": (
            "**High-Level Blocks:** `async with sem:` acts as an automatic concurrency gate, releasing even on exceptions, while `gather` overlaps all awaits."
        ),
        "test_cases": [
            {
                "name": "respects_limit_and_order",
                "code": (
                    "import asyncio\nstate = {'active': 0, 'peak': 0}\n"
                    "async def fake_worker(x):\n"
                    "    state['active'] += 1\n    state['peak'] = max(state['peak'], state['active'])\n"
                    "    await asyncio.sleep(0.02)\n    state['active'] -= 1\n    return x.upper()\n"
                    "res = asyncio.run(sol.run_bounded(['a', 'b', 'c', 'd', 'e'], fake_worker, 2))\n"
                    "assert res == ['A', 'B', 'C', 'D', 'E'] and state['peak'] <= 2"
                ),
            },
        ],
    },
    {
        "id": "wb-05-02",
        "chapter_id": "ch05",
        "number": "5.2",
        "title": "Async Retries with Exponential Backoff",
        "topic": "Async",
        "question_type": "Systems",
        "difficulty": "Intermediate",
        "summary": "Retry transient async failures with `base_delay * (2 ** attempt)` non-blocking sleeps.",
        "prompt_markdown": (
            "Write `async def retry_async(fn, max_retries: int = 3, base_delay: float = 0.01)` trying up to `1 + max_retries` times."
        ),
        "thinking_blueprint": [
            "Loop `attempt` from `0..max_retries`.",
            "Try `return await fn()`; on error re-raise on last attempt, else `await asyncio.sleep(base_delay * (2 ** attempt))`.",
        ],
        "hints": [
            "Always use `await asyncio.sleep(...)`, never `time.sleep(...)`.",
        ],
        "dry_run_trace": (
            "Attempt 0 fails -> sleep 0.01s; Attempt 1 fails -> sleep 0.02s; Attempt 2 succeeds -> return value."
        ),
        "starter_code": (
            "import asyncio\n\n"
            "async def retry_async(fn, max_retries: int = 3, base_delay: float = 0.01):\n"
            "    # TODO: retry with exponential backoff\n"
            "    pass\n"
        ),
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
        "explanation_markdown": (
            "**High-Level Blocks:** Non-blocking exponential backoff lets other coroutines keep working on the event loop while waiting to retry."
        ),
        "test_cases": [
            {
                "name": "succeeds_after_transient_failures",
                "code": (
                    "import asyncio\nstate = {'calls': 0}\n"
                    "async def flaky():\n    state['calls'] += 1\n    if state['calls'] < 3: raise RuntimeError('429')\n    return 'ok'\n"
                    "assert asyncio.run(sol.retry_async(flaky, max_retries=3, base_delay=0.005)) == 'ok' and state['calls'] == 3"
                ),
            },
        ],
    },
]
