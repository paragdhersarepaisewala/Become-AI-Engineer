"""Phase 1 Curriculum (Chapters 1-5): Structured ground-zero lessons with Definitions, Exact Syntax, Line-by-Line Examples, and Common Mistakes."""

from __future__ import annotations

from typing import Any

PHASE_1_CHAPTERS: list[dict[str, Any]] = [
    {
        "id": "ch01",
        "number": 1,
        "phase": 1,
        "phase_title": "Phase 1: Python Foundations, OOP & Logic Building",
        "title": "Python Basics From Ground Zero & Working With Files",
        "subtitle": "Variables, basic types, if/else, loops, lists, dicts, functions, opening/loading files (open, pathlib, json, csv), and clean script structure.",
        "status_type": "available",
        "estimated_hours": 6,
        "why_it_matters": (
            "Every AI tool—whether loading a dataset, cleaning chat logs, or calling an API—starts with the exact same building blocks: "
            "variables, decisions, loops, collections, functions, and reading/writing files safely."
        ),
        "just_in_time_tags": ["Variables & Types", "if / Loops", "Lists & Dicts", "Functions", "Files (open/json/csv)", "Stdlib Helpers"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch01-s1",
                "title": "1.1 Variables, Data Types & Printing Output",
                "zero_assumption_note": "Python runs your script from Line 1 down to the last line, one instruction at a time.",
                "definition": (
                    "A **variable** is a nickname you attach to a value so you can reuse or update it later. "
                    "A **data type** tells Python what kind of value it is (a whole number, a decimal number, text, or a True/False flag)."
                ),
                "syntax_box": {
                    "title": "Creating Variables & Printing with f-strings",
                    "syntax": (
                        "variable_name = value\n"
                        "print(f'Some text {variable_name}')\n"
                        "number = int('42')     # converts text '42' -> integer 42\n"
                        "decimal = float('3.5') # converts text '3.5' -> float 3.5"
                    ),
                    "breakdown": [
                        "`=` means **assign** (store the value on the right under the name on the left), NOT math equality.",
                        "`int` = whole number (`25`), `float` = decimal (`19.99`), `str` = text in quotes (`'Alex'`), `bool` = `True` or `False`.",
                        "`f'...'` (f-string) inserts any variable inside `{...}` cleanly into text.",
                    ],
                },
                "tiny_example": {
                    "title": "Numbers vs Text (Strings)",
                    "code": (
                        "name = 'Sara'\n"
                        "age = 22\n"
                        "next_year = age + 1\n"
                        "print(f'{name} will be {next_year}')"
                    ),
                    "line_by_line": [
                        "Line 1: Stores the text `'Sara'` (`str`) in `name`.",
                        "Line 2: Stores the whole number `22` (`int`) in `age`.",
                        "Line 3: Reads `age` (`22`), adds `1`, and stores `23` in `next_year`.",
                        "Line 4: Prints `Sara will be 23`.",
                    ],
                },
                "body_markdown": (
                    "### Why Types Matter in Real Programs\n"
                    "When you read input from a user or a text file, Python always gives you **text (`str`)**—even if it looks like `'10'`. "
                    "`'10' + '5'` gives `'105'` (glued text), whereas `int('10') + int('5')` gives `15` (math)."
                ),
                "code_example": {
                    "title": "Calculating Study Hours from String Input",
                    "code": (
                        "# Block 1: Raw settings (pretend '3' came from a config file as text)\n"
                        "hours_text = '3'\n"
                        "days = 4\n\n"
                        "# Block 2: Convert text to int before multiplying\n"
                        "hours_num = int(hours_text)\n"
                        "total_hours = hours_num * days\n\n"
                        "# Block 3: Display result\n"
                        "print(f'Total study time: {total_hours} hours')\n"
                    ),
                },
                "common_mistakes": [
                    "Trying to do math on `'5'` without calling `int('5')` or `float('5')`.",
                    "Writing `2name = 'x'` (variable names cannot start with a digit or contain spaces—use `user_name`).",
                ],
                "key_takeaway": "Know whether a variable is a number (`int`/`float`) or text (`str`), convert explicitly with `int()`/`float()`, and use `f'...'` to display values.",
            },
            {
                "id": "ch01-s2",
                "title": "1.2 Making Decisions (`if / elif / else`) & Loops (`for` & `while`)",
                "zero_assumption_note": "Python uses **4 spaces of indentation** on the left to know which lines belong inside an `if` or loop.",
                "definition": (
                    "An **`if` statement** lets your program choose between actions based on a True/False question. "
                    "A **loop** (`for` or `while`) repeats a block of code automatically without you copy-pasting lines."
                ),
                "syntax_box": {
                    "title": "if / elif / else and for / while",
                    "syntax": (
                        "if condition:\n"
                        "    # runs when condition is True\n"
                        "elif other_condition:\n"
                        "    # runs if first was False and this is True\n"
                        "else:\n"
                        "    # runs when all above were False\n\n"
                        "for item in collection:\n"
                        "    # repeats once per item\n\n"
                        "while keep_going:\n"
                        "    # repeats as long as keep_going is True"
                    ),
                    "breakdown": [
                        "Comparison operators: `==` (equal to), `!=` (not equal), `>`, `<`, `>=`, `<=`.",
                        "Logical connectors: `and` (both True), `or` (at least one True), `not` (flips True/False).",
                        "`range(5)` generates numbers `0, 1, 2, 3, 4` (stops *before* 5).",
                    ],
                },
                "tiny_example": {
                    "title": "Adding Up 3 Scores with a `for` Loop",
                    "code": (
                        "scores = [10, 20, 30]\n"
                        "total = 0\n"
                        "for s in scores:\n"
                        "    total = total + s\n"
                        "print(total)"
                    ),
                    "line_by_line": [
                        "Line 1: Creates a list of 3 numbers.",
                        "Line 2: Starts a running counter `total` at `0` *before* the loop.",
                        "Line 3: Round 1 sets `s = 10` -> `total` becomes `10`. Round 2 sets `s = 20` -> `30`. Round 3 sets `s = 30` -> `60`.",
                        "Line 5 (not indented, so outside the loop!): Prints `60` once after the loop ends.",
                    ],
                },
                "body_markdown": (
                    "### Choosing Between `for` and `while`\n"
                    "- Use **`for`** 90% of the time: when walking through items in a list, lines in a file, or `range(n)`.\n"
                    "- Use **`while`** when you don't know how many rounds it will take (e.g., retrying a network request until it succeeds)."
                ),
                "code_example": {
                    "title": "Counting Passing Scores with `for` + `if/else`",
                    "code": (
                        "scores = [45, 82, 91, 58]\n"
                        "passed = 0\n\n"
                        "# Block 1: Inspect each score one at a time\n"
                        "for score in scores:\n"
                        "    if score >= 60:\n"
                        "        passed += 1  # shorthand for passed = passed + 1\n"
                        "        print(f'{score}: Pass')\n"
                        "    else:\n"
                        "        print(f'{score}: Review')\n\n"
                        "# Block 2: Final count after loop finishes\n"
                        "print(f'Total passed: {passed}')\n"
                    ),
                },
                "common_mistakes": [
                    "Using `=` instead of `==` inside an `if` check (`if x == 5:` checks equality; `x = 5` assigns).",
                    "Putting `total = 0` *inside* the `for` loop (which resets `total` back to `0` on every round!).",
                    "Writing a `while` loop without updating the condition variable (causes an infinite loop).",
                ],
                "key_takeaway": "Initialize counters *before* the loop, keep indentation consistent (4 spaces), and use `==` for comparisons.",
            },
            {
                "id": "ch01-s3",
                "title": "1.3 Lists, Dictionaries, Sets & Tuples",
                "zero_assumption_note": "Instead of making 20 separate variables (`score1`, `score2`, ...), Python gives you 4 containers.",
                "definition": (
                    "- **List (`[]`):** Ordered sequence accessed by index (`0, 1, 2...`).\n"
                    "- **Dictionary (`{k: v}`):** Key-value lookup table (like a real dictionary: look up a word to get its meaning).\n"
                    "- **Set (`{a, b}`):** Unordered bag that automatically keeps **unique** items only.\n"
                    "- **Tuple (`(a, b)`):** Locked list that cannot be modified after creation."
                ),
                "syntax_box": {
                    "title": "Core Container Operations",
                    "syntax": (
                        "items = ['a', 'b']          # list\n"
                        "items.append('c')           # add to end -> ['a', 'b', 'c']\n"
                        "first = items[0]            # 'a' (index starts at 0!)\n\n"
                        "user = {'name': 'Sam'}      # dict\n"
                        "city = user.get('city', 'Unknown')  # safe lookup! never crashes\n"
                        "user['age'] = 24            # add or update key"
                    ),
                    "breakdown": [
                        "`items[0]` is the **first** item; `items[-1]` is the **last** item.",
                        "`user['city']` **crashes** with `KeyError` if `'city'` is missing; `user.get('city', default)` returns `default` safely.",
                        "Copying a list: `b = a` only makes a second label to the **same** list. Use `b = a.copy()` to make a real separate copy!",
                    ],
                },
                "tiny_example": {
                    "title": "Safe Dictionary Lookup & Removing Duplicates with `set`",
                    "code": (
                        "tags = ['ai', 'python', 'ai']\n"
                        "unique = set(tags)\n"
                        "print(unique)\n"
                        "user = {'name': 'Sara'}\n"
                        "print(user.get('role', 'student'))"
                    ),
                    "line_by_line": [
                        "Line 1: List with duplicate `'ai'`.",
                        "Line 2: `set(tags)` removes duplicates -> `{'ai', 'python'}`.",
                        "Line 4: Dictionary with only `'name'`.",
                        "Line 5: `.get('role', 'student')` sees `'role'` is missing and safely returns `'student'` instead of crashing.",
                    ],
                },
                "body_markdown": (
                    "### Which Container Should I Pick?\n"
                    "- Need items in order and might add/remove later? -> **`list`**\n"
                    "- Need to attach fields/counts to named labels (like JSON)? -> **`dict`**\n"
                    "- Need to eliminate duplicates or check `if word in seen` quickly? -> **`set`**\n"
                    "- Returning fixed pairs like `(width, height)` that shouldn't change? -> **`tuple`**"
                ),
                "code_example": {
                    "title": "Counting & Safe List Copying",
                    "code": (
                        "# Block 1: List copy vs alias\n"
                        "original = ['python', 'sql']\n"
                        "safe_copy = original.copy()\n"
                        "safe_copy.append('docker')\n"
                        "print('original:', original)   # ['python', 'sql'] (untouched!)\n"
                        "print('copy:', safe_copy)      # ['python', 'sql', 'docker']\n\n"
                        "# Block 2: Updating a dictionary counter manually\n"
                        "counts = {}\n"
                        "for word in ['ai', 'ml', 'ai']:\n"
                        "    counts[word] = counts.get(word, 0) + 1\n"
                        "print(counts)  # {'ai': 2, 'ml': 1}\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting Python indexes start at `0`, not `1` (`items[1]` is the *second* item).",
                    "Writing `user['missing_key']` instead of `user.get('missing_key')` when a key might not exist.",
                    "Writing `b = a` expecting a separate copy of a list, then accidentally modifying `a`.",
                ],
                "key_takeaway": "Use `list` for order, `dict` + `.get()` for named fields, `set` for uniqueness, and `.copy()` before mutating a borrowed list.",
            },
            {
                "id": "ch01-s4",
                "title": "1.4 Functions (`def`, Parameters & `return` vs `print`)",
                "zero_assumption_note": "If you ever got `None` back from a function and didn't know why, this section fixes that forever.",
                "definition": (
                    "A **function** is a named, reusable mini-machine: you pass inputs in (**parameters**), it runs its code, "
                    "and it hands a result back with **`return`**."
                ),
                "syntax_box": {
                    "title": "Defining & Calling a Function",
                    "syntax": (
                        "def function_name(param1: str, param2: int = 1) -> str:\n"
                        "    result = f'{param1} x {param2}'\n"
                        "    return result\n\n"
                        "answer = function_name('hello', 3)  # saves 'hello x 3' in answer"
                    ),
                    "breakdown": [
                        "`def` creates the function (it does NOT run it until you call `function_name(...)`!).",
                        "`: str` and `-> str` are **type hints**—optional labels for humans saying what types go in and come out.",
                        "`param2: int = 1` is a **default value** used if the caller skips `param2`.",
                        "`return` sends the value back to the caller and immediately exits the function.",
                    ],
                },
                "tiny_example": {
                    "title": "`print` vs `return` Side-by-Side",
                    "code": (
                        "def bad_double(x):\n"
                        "    print(x * 2)\n\n"
                        "def good_double(x):\n"
                        "    return x * 2\n\n"
                        "a = bad_double(5)   # prints 10, but a is None!\n"
                        "b = good_double(5)  # b holds 10, so b + 1 == 11!"
                    ),
                    "line_by_line": [
                        "`bad_double(5)` prints `10` on screen, then hits the end without `return`, so Python gives back `None`.",
                        "Trying `a + 1` would crash (`None + 1` is invalid!).",
                        "`good_double(5)` returns `10` into `b`, so your program can keep using `b`.",
                    ],
                },
                "body_markdown": (
                    "### One Crucial Function Trap: Default `= []`\n"
                    "Python creates default argument values **only once** when `def` is read. If you write `def add(x, items=[]):`, "
                    "every call shares that same list! Always write `items=None` and create a fresh `[]` inside the function."
                ),
                "code_example": {
                    "title": "Clean Reusable Function with Safe Optional List",
                    "code": (
                        "# Block 1: Helper with safe default None\n"
                        "def add_tag(tag: str, existing: list[str] | None = None) -> list[str]:\n"
                        "    result = [] if existing is None else existing.copy()\n"
                        "    if tag not in result:\n"
                        "        result.append(tag)\n"
                        "    return result\n\n"
                        "# Block 2: Each call without existing gets its own fresh list\n"
                        "print(add_tag('python'))  # ['python']\n"
                        "print(add_tag('ai'))      # ['ai'] (not ['python', 'ai']!)\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting `return` inside a function and getting `None`.",
                    "Using `=[]` or `={}` as a default parameter instead of `=None`.",
                ],
                "key_takeaway": "Functions should `return` values (not just `print` them), and optional mutable defaults should always be `None`.",
            },
            {
                "id": "ch01-s5",
                "title": "1.5 Opening, Reading & Writing Files (`open`, `pathlib`, `json`, `csv`)",
                "zero_assumption_note": "Let's start with a 3-line `.txt` file first before touching JSON or CSV.",
                "definition": (
                    "File handling lets Python save data permanently to your hard drive and load real datasets (`txt`, `json`, `csv`) into memory."
                ),
                "syntax_box": {
                    "title": "Opening Files Safely with `with` & `pathlib.Path`",
                    "syntax": (
                        "from pathlib import Path\n\n"
                        "p = Path('folder') / 'notes.txt'        # works on Windows, Mac, Linux\n"
                        "with p.open('w', encoding='utf-8') as f:\n"
                        "    f.write('Hello\\n')\n\n"
                        "with p.open('r', encoding='utf-8') as f:\n"
                        "    text = f.read()"
                    ),
                    "breakdown": [
                        "`Path('folder') / 'notes.txt'` joins folder and filename cleanly with `/`.",
                        "`'w'` = write (overwrites), `'a'` = append (adds to end), `'r'` = read.",
                        "`with ... as f:` **automatically closes** the file when the block ends, even if an error occurs.",
                        "`encoding='utf-8'` prevents Windows crashes on special characters or emojis.",
                    ],
                },
                "tiny_example": {
                    "title": "Reading a Text File Line by Line",
                    "code": (
                        "from pathlib import Path\n"
                        "p = Path('notes.txt')\n"
                        "if p.exists():\n"
                        "    with p.open('r', encoding='utf-8') as f:\n"
                        "        for line in f:\n"
                        "            print(line.strip())"
                    ),
                    "line_by_line": [
                        "`p.exists()` checks whether the file is actually on disk before opening.",
                        "`for line in f:` reads one line at a time (great for huge files!).",
                        "`line.strip()` removes the hidden newline `'\\n'` at the end of each line.",
                    ],
                },
                "body_markdown": (
                    "### Loading Structured Files (`json` & `csv`) + `try / except`\n"
                    "- **`json.load(f)`** reads a `.json` file directly into a Python `dict` or `list`. **`json.loads(line)`** parses a single JSON string (`.jsonl` datasets have 1 JSON object per line).\n"
                    "- **`csv.DictReader(f)`** reads a `.csv` spreadsheet row by row, giving each row as a `dict` keyed by the header row.\n"
                    "- **`try / except`:** Lets you catch predictable errors like `FileNotFoundError` or `json.JSONDecodeError` instead of crashing."
                ),
                "code_example": {
                    "title": "Safe JSON & CSV Loaders Explained Block-by-Block",
                    "code": (
                        "import csv\n"
                        "import json\n"
                        "from pathlib import Path\n\n"
                        "# Block 1: Load a JSON file safely with try/except\n"
                        "def load_json_safe(path: Path) -> dict:\n"
                        "    try:\n"
                        "        with path.open('r', encoding='utf-8') as f:\n"
                        "            return json.load(f)\n"
                        "    except FileNotFoundError:\n"
                        "        return {}\n\n"
                        "# Block 2: Load CSV rows as a list of dictionaries\n"
                        "def load_csv(path: Path) -> list[dict[str, str]]:\n"
                        "    with path.open('r', encoding='utf-8', newline='') as f:\n"
                        "        return list(csv.DictReader(f))\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting `encoding='utf-8'` on Windows.",
                    "Forgetting `newline=''` when opening CSV files for `csv.DictReader` / `csv.writer`.",
                    "Trying to parse CSV with `line.split(',')` (breaks whenever a text column contains a comma!).",
                ],
                "key_takeaway": "Always use `Path`, `with path.open(..., encoding='utf-8')`, `json`/`csv`, and specific `try/except` blocks.",
            },
            {
                "id": "ch01-s6",
                "title": "1.6 Small Standard Libraries & Clean Script Structure",
                "zero_assumption_note": "Now that you know loops, dicts, functions, and files, these 3 small built-in tools save huge amounts of boilerplate.",
                "definition": (
                    "Python's **standard library** is a toolbox of built-in modules (`collections`, `os`, `json`, `csv`, `pathlib`) "
                    "that come pre-installed with Python—no `pip install` required."
                ),
                "syntax_box": {
                    "title": "Counter, defaultdict, os.getenv & `__main__` Guard",
                    "syntax": (
                        "from collections import Counter, defaultdict\n"
                        "import os\n\n"
                        "counts = Counter(['ai', 'py', 'ai'])   # {'ai': 2, 'py': 1}\n"
                        "groups = defaultdict(list)             # missing key auto-starts as []\n"
                        "api_key = os.getenv('API_KEY', '')     # reads env var safely\n\n"
                        "if __name__ == '__main__':\n"
                        "    # code here ONLY runs when you run THIS file directly"
                    ),
                    "breakdown": [
                        "`Counter(items)` replaces manual `counts[x] = counts.get(x, 0) + 1` loops.",
                        "`defaultdict(list)` lets you write `groups[tag].append(item)` without `if tag not in groups:`.",
                        "`if __name__ == '__main__':` prevents your script from auto-running when another file imports a helper from it.",
                    ],
                },
                "tiny_example": {
                    "title": "Grouping Items with `defaultdict(list)`",
                    "code": (
                        "from collections import defaultdict\n"
                        "groups = defaultdict(list)\n"
                        "groups['fruit'].append('apple')\n"
                        "groups['fruit'].append('pear')\n"
                        "print(dict(groups))"
                    ),
                    "line_by_line": [
                        "Line 2: Creates a special dict where any brand-new key automatically starts with `[]`.",
                        "Line 3: `'fruit'` wasn't in `groups` yet—Python auto-created `[]` and appended `'apple'`.",
                        "Line 5: Converts back to a normal dict and prints `{'fruit': ['apple', 'pear']}`.",
                    ],
                },
                "body_markdown": (
                    "### Clean 3-Block Layout for Any Python File\n"
                    "1. **Top:** `import` statements.\n"
                    "2. **Middle:** Helper functions (take arguments, `return` values, zero hardcoded paths).\n"
                    "3. **Bottom:** `if __name__ == '__main__':` block that reads files/inputs and calls your functions."
                ),
                "code_example": {
                    "title": "Clean 3-Block Script Skeleton",
                    "code": (
                        "# Block 1: Imports\n"
                        "from collections import Counter\n\n"
                        "# Block 2: Pure helper function\n"
                        "def top_words(text: str, n: int = 2) -> list[tuple[str, int]]:\n"
                        "    words = text.lower().split()\n"
                        "    return Counter(words).most_common(n)\n\n"
                        "# Block 3: Main runner (only runs when executed directly)\n"
                        "if __name__ == '__main__':\n"
                        "    print(top_words('ai python ai ml ai'))  # [('ai', 3), ('python', 1)]\n"
                    ),
                },
                "common_mistakes": [
                    "Putting file-reading or `print()` loops at top level without `if __name__ == '__main__':` (causes surprises when importing).",
                ],
                "key_takeaway": "Organize files as Imports -> Functions -> `if __name__ == '__main__':`, and use `Counter` / `defaultdict` to keep code short and clear.",
            },
        ],
        "quizzes": [
            {
                "id": "ch01-q1",
                "question": "What does `'5' + '5'` produce in Python?",
                "options": ["10", "'55' (text concatenation)", "Error", "5.5"],
                "correct_index": 1,
                "explanation": "Quotes make `'5'` a `str` (text). Use `int('5') + int('5')` for `10`.",
            },
            {
                "id": "ch01-q2",
                "question": "What happens if a function only calls `print(x)` without `return x`?",
                "options": [
                    "It returns `x` anyway",
                    "It shows text on screen, and the caller receives `None`",
                    "It saves `x` to disk",
                    "Python raises an error",
                ],
                "correct_index": 1,
                "explanation": "`print` only writes to the console; `return` hands a value back to your Python code.",
            },
            {
                "id": "ch01-q3",
                "question": "Why use `with path.open('r', encoding='utf-8') as f:`?",
                "options": [
                    "It guarantees the file closes automatically and handles Unicode safely on Windows",
                    "It converts files to JSON automatically",
                    "It deletes the file afterward",
                    "It makes loops run on GPU",
                ],
                "correct_index": 0,
                "explanation": "`with` closes the handle safely even on errors, and `utf-8` prevents Windows `cp1252` decoding crashes.",
            },
        ],
        "project": {
            "title": "Dataset Inspector & File Converter CLI",
            "workspace_dir": "projects/ch01_file_inspector",
            "overview": "Read a CSV file safely with `Path` and `csv.DictReader`, count categories with `Counter`, and save a clean JSONL file.",
            "architecture_steps": [
                "Check file existence with `pathlib.Path`.",
                "Load CSV rows safely via `csv.DictReader` and `encoding='utf-8'`.",
                "Count categories with `Counter` and export clean JSONL lines.",
            ],
            "milestones": [
                {"id": "ch01-m1", "label": "Read CSV safely with Path and encoding='utf-8'"},
                {"id": "ch01-m2", "label": "Count categories with Counter & skip blank rows"},
                {"id": "ch01-m3", "label": "Write JSONL output and pass pytest"},
            ],
        },
    },
    {
        "id": "ch02",
        "number": 2,
        "phase": 1,
        "phase_title": "Phase 1: Python Foundations, OOP & Logic Building",
        "title": "Object-Oriented Programming (OOP) & Breaking the Monolith",
        "subtitle": "Classes, self, __init__, dataclasses, composition vs inheritance, dunder methods (__call__, __len__), and modular files.",
        "status_type": "available",
        "estimated_hours": 5,
        "why_it_matters": (
            "Loose scripts with global variables turn messy fast. Plus, PyTorch (`nn.Module`), custom Datasets (`__len__`, `__getitem__`), "
            "and LangChain Runnables are all built using OOP classes."
        ),
        "just_in_time_tags": ["class & self", "__init__", "@dataclass", "Composition", "Dunder Methods", "Modularity"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch02-s1",
                "title": "2.1 Classes, `__init__` & `self` (Bundling Data + Functions)",
                "zero_assumption_note": "If you have ever wondered what `self` means inside `def method(self):`, this explains it cleanly.",
                "definition": (
                    "A **class** is a blueprint for creating objects that bundle **data (attributes)** and **actions (methods)** together in one place, "
                    "instead of passing 5 separate variables into every function."
                ),
                "syntax_box": {
                    "title": "Defining a Class & Creating Instances",
                    "syntax": (
                        "class BankAccount:\n"
                        "    def __init__(self, owner: str, balance: float = 0.0) -> None:\n"
                        "        self.owner = owner\n"
                        "        self.balance = balance\n\n"
                        "    def deposit(self, amount: float) -> None:\n"
                        "        self.balance += amount\n\n"
                        "acc = BankAccount('Sara', 100.0)  # calls __init__ automatically\n"
                        "acc.deposit(50.0)                 # acc becomes `self` inside deposit!"
                    ),
                    "breakdown": [
                        "`__init__` (constructor) runs once automatically when you create `BankAccount(...)`.",
                        "`self` means **this specific object**. If you create `acc1` and `acc2`, `self` keeps their balances separate.",
                        "`self.balance` is an **attribute** (data attached to the object). `deposit` is a **method** (a function inside a class).",
                    ],
                },
                "tiny_example": {
                    "title": "Two Independent Counter Objects",
                    "code": (
                        "class CounterBox:\n"
                        "    def __init__(self) -> None:\n"
                        "        self.count = 0\n\n"
                        "    def add_one(self) -> None:\n"
                        "        self.count += 1\n\n"
                        "a = CounterBox()\n"
                        "b = CounterBox()\n"
                        "a.add_one()\n"
                        "print(a.count, b.count)"
                    ),
                    "line_by_line": [
                        "`a = CounterBox()` creates box `a` with `a.count = 0`.",
                        "`b = CounterBox()` creates a separate box `b` with `b.count = 0`.",
                        "`a.add_one()` runs with `self = a`, so `a.count` becomes `1` while `b.count` stays `0`!",
                    ],
                },
                "body_markdown": (
                    "### Shortcut for Pure Data Classes: `@dataclass`\n"
                    "When a class's only job is holding fields (like `Document(doc_id, text)`), writing `self.x = x` ten times gets tedious. "
                    "Putting `@dataclass` above a class makes Python write `__init__`, nice `print()` output (`__repr__`), and `==` comparisons automatically!"
                ),
                "code_example": {
                    "title": "@dataclass + Stateful DocumentStore",
                    "code": (
                        "from dataclasses import dataclass\n\n"
                        "# Block 1: Passive data record — @dataclass auto-writes __init__ and __repr__\n"
                        "@dataclass\n"
                        "class Document:\n"
                        "    doc_id: str\n"
                        "    text: str\n\n"
                        "# Block 2: Stateful service class owning its dictionary of documents\n"
                        "class DocumentStore:\n"
                        "    def __init__(self) -> None:\n"
                        "        self._docs: dict[str, Document] = {}\n\n"
                        "    def add(self, doc: Document) -> None:\n"
                        "        self._docs[doc.doc_id] = doc\n\n"
                        "    def get(self, doc_id: str) -> Document | None:\n"
                        "        return self._docs.get(doc_id)\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting `self` as the first parameter of a method (`def add(doc):` crashes with `TypeError` when called as `store.add(doc)`!).",
                    "Forgetting `self.` when saving attributes inside `__init__` (`count = 0` creates a temporary local variable that vanishes after `__init__`!).",
                ],
                "key_takeaway": "A class groups data (`self.x`) and actions (`def method(self)`). Use `@dataclass` for simple data records.",
            },
            {
                "id": "ch02-s2",
                "title": "2.2 Dunder Methods (`__len__`, `__call__`) & Composition",
                "zero_assumption_note": "Double-underscore ('dunder') methods look weird at first, but they just connect your class to built-in Python syntax like `len(x)` and `x()`.",
                "definition": (
                    "- **Dunder methods (`__name__`):** Special hooks Python calls behind the scenes (`len(obj)` calls `obj.__len__()`; `obj(x)` calls `obj.__call__(x)`).\n"
                    "- **Composition:** Building a bigger object by storing smaller helper objects inside `self` (plugging LEGO bricks together) instead of deep inheritance."
                ),
                "syntax_box": {
                    "title": "__len__, __contains__, __call__ & Composition",
                    "syntax": (
                        "class WordCleaner:\n"
                        "    def __init__(self, lowercase: bool = True) -> None:\n"
                        "        self.lowercase = lowercase\n\n"
                        "    def __call__(self, text: str) -> str:\n"
                        "        out = ' '.join(text.split())\n"
                        "        return out.lower() if self.lowercase else out\n\n"
                        "cleaner = WordCleaner(lowercase=True)\n"
                        "cleaner('  Hello   AI  ')  # invokes __call__ -> 'hello ai'"
                    ),
                    "breakdown": [
                        "`__len__(self)` -> lets callers run `len(my_object)`.",
                        "`__contains__(self, item)` -> lets callers run `if 'id1' in my_store:`.",
                        "`__call__(self, x)` -> lets an object holding config/weights in `self` be called like a function `model(x)`!",
                    ],
                },
                "tiny_example": {
                    "title": "Making `len(bag)` Work on a Custom Class",
                    "code": (
                        "class Bag:\n"
                        "    def __init__(self) -> None:\n"
                        "        self.items = []\n"
                        "    def add(self, x) -> None:\n"
                        "        self.items.append(x)\n"
                        "    def __len__(self) -> int:\n"
                        "        return len(self.items)\n\n"
                        "b = Bag()\n"
                        "b.add('apple')\n"
                        "print(len(b))"
                    ),
                    "line_by_line": [
                        "`Bag` stores a private list `self.items`.",
                        "Defining `__len__` teaches Python what `len(b)` should return.",
                        "`print(len(b))` prints `1`.",
                    ],
                },
                "body_markdown": (
                    "### Why AI Frameworks Love Composition + `__call__`\n"
                    "Both **PyTorch (`nn.Module`)** and **LangChain (`Runnable`)** work by composing small objects (`step1`, `step2`) inside a pipeline and calling them like functions!"
                ),
                "code_example": {
                    "title": "Composable Pipeline Using Small `__call__` Steps",
                    "code": (
                        "class StripStep:\n"
                        "    def __call__(self, text: str) -> str:\n"
                        "        return ' '.join(text.split())\n\n"
                        "class LowerStep:\n"
                        "    def __call__(self, text: str) -> str:\n"
                        "        return text.lower()\n\n"
                        "# Block 1: Composition — Pipeline HAS a list of steps (no inheritance needed)\n"
                        "class Pipeline:\n"
                        "    def __init__(self, steps: list) -> None:\n"
                        "        self.steps = steps\n\n"
                        "    def __call__(self, text: str) -> str:\n"
                        "        for step in self.steps:\n"
                        "            text = step(text)\n"
                        "        return text\n\n"
                        "pipe = Pipeline([StripStep(), LowerStep()])\n"
                        "print(pipe('  Hello   WORLD  '))  # 'hello world'\n"
                    ),
                },
                "common_mistakes": [
                    "Creating 4-level inheritance trees (`class SmartCleaner(BaseCleaner(Helper))`) when passing a helper object into `__init__` is cleaner and easier to test.",
                ],
                "key_takeaway": "Use `__call__` to make configured objects act like functions, and compose small independent classes together.",
            },
            {
                "id": "ch02-s3",
                "title": "2.3 Breaking Monoliths into Modular Files & `pytest`",
                "zero_assumption_note": "A 'monolith' is one giant `.py` file where file loading, logic, and `print()` are tangled together so you can't test anything cleanly.",
                "definition": (
                    "**Modular architecture** splits your code by job: data definitions (`models.py`), pure logic/classes (`analyzer.py`), "
                    "file/CLI wiring (`cli.py`), and automated checks (`test_*.py`)."
                ),
                "syntax_box": {
                    "title": "Writing a `pytest` Unit Test",
                    "syntax": (
                        "def test_something() -> None:\n"
                        "    actual = my_function('input')\n"
                        "    assert actual == 'expected'"
                    ),
                    "breakdown": [
                        "Any file starting with `test_` and function starting with `test_` is discovered automatically when you run `python -m pytest`.",
                        "`assert condition` passes silently if True, and prints a clear diff if False.",
                    ],
                },
                "tiny_example": {
                    "title": "Separating Pure Logic from File I/O",
                    "code": (
                        "# Pure function: takes a list of strings, returns a dict (no open() inside!)\n"
                        "def count_errors(lines: list[str]) -> int:\n"
                        "    return sum(1 for line in lines if '[ERROR]' in line)\n\n"
                        "def test_count_errors() -> None:\n"
                        "    assert count_errors(['[INFO] ok', '[ERROR] fail']) == 1"
                    ),
                    "line_by_line": [
                        "`count_errors` does NOT open any file—it accepts `list[str]` directly.",
                        "Because it has zero file I/O, `test_count_errors` can test it in 1 millisecond with a tiny fake list!",
                    ],
                },
                "body_markdown": (
                    "When you separate **pure logic** from **file/terminal I/O**, bugs become trivial to isolate and every change is verified automatically by `pytest`."
                ),
                "code_example": {
                    "title": "3-File Package Layout",
                    "code": (
                        "# models.py   -> @dataclass LogEntry, LogReport\n"
                        "# analyzer.py -> class LogAnalyzer (pure logic, zero open/print)\n"
                        "# cli.py      -> uses Path.open() to read file, calls LogAnalyzer, prints summary\n"
                        "# test_analyzer.py -> pytest functions passing fake lists directly to LogAnalyzer\n"
                    ),
                },
                "common_mistakes": [
                    "Hardcoding `open('server.log')` inside parsing functions, making unit tests impossible without creating real files.",
                ],
                "key_takeaway": "Keep file/network I/O at the edges (`cli.py`) and pure OOP/logic in testable modules.",
            },
        ],
        "quizzes": [
            {
                "id": "ch02-q1",
                "question": "What does `self` refer to inside a Python class method?",
                "options": [
                    "The Python interpreter itself",
                    "The specific object instance the method was called on",
                    "A global variable shared by all classes",
                    "The return type",
                ],
                "correct_index": 1,
                "explanation": "Calling `store_a.add(doc)` passes `store_a` automatically as `self`, keeping its data separate from `store_b`.",
            },
            {
                "id": "ch02-q2",
                "question": "What does implementing `__call__` on a class let you do?",
                "options": [
                    "Run `len(obj)`",
                    "Call the object like a function: `obj(x)`",
                    "Save the object to JSON",
                    "Loop over the object",
                ],
                "correct_index": 1,
                "explanation": "`__call__` is used in PyTorch `nn.Module` and LangChain so configured objects can be invoked as `model(x)`.",
            },
        ],
        "project": {
            "title": "Modular OOP Log Analyzer Package",
            "workspace_dir": "projects/ch02_log_analyzer",
            "overview": "Refactor `legacy_monolith.py` into `models.py`, `analyzer.py`, and `cli.py` with a passing `pytest` suite.",
            "architecture_steps": [
                "Inspect `legacy_monolith.py` to separate parsing from printing.",
                "Create `LogEntry` and `LogReport` dataclasses in `models.py`.",
                "Implement `LogAnalyzer` in `analyzer.py` and verify with `pytest`.",
            ],
            "milestones": [
                {"id": "ch02-m1", "label": "Separate models.py dataclasses from file I/O"},
                {"id": "ch02-m2", "label": "Build LogAnalyzer class with clean methods"},
                {"id": "ch02-m3", "label": "Wire cli.py with Path & pass pytest"},
            ],
        },
    },
    {
        "id": "ch03",
        "number": 3,
        "phase": 1,
        "phase_title": "Phase 1: Python Foundations, OOP & Logic Building",
        "title": "Logic Building & Algorithmic Thinking",
        "subtitle": "How to plan on paper, trace variables in tables, and master core patterns (hash maps, two pointers, sliding window, recursion).",
        "status_type": "available",
        "estimated_hours": 6,
        "why_it_matters": (
            "Struggling with programming logic does NOT mean you are bad at coding—it means you are trying to type Python "
            "before figuring out the steps on paper. Here is a repeatable method to turn any problem into clean code."
        ),
        "just_in_time_tags": ["Paper Tracing", "Hash Maps", "Two Pointers", "Sliding Window", "Recursion Stack"],
        "visualizer": "recursion_stack",
        "sections": [
            {
                "id": "ch03-s1",
                "title": "3.1 The 4-Step Logic Blueprint (How to Think Before Coding)",
                "zero_assumption_note": "Never start typing code while the problem is still fuzzy in your head. Solve a 4-item example on paper first!",
                "definition": (
                    "A **trace table** tracks what every variable holds after each loop step on a tiny sample input. "
                    "Whatever your brain has to *remember* while solving the sample by hand becomes your Python variables."
                ),
                "syntax_box": {
                    "title": "The Sliding Window Pattern (Fixed Size `k`)",
                    "syntax": (
                        "window_sum = sum(nums[:k])   # 1. compute first window\n"
                        "best = window_sum\n"
                        "for right in range(k, len(nums)):\n"
                        "    window_sum += nums[right] - nums[right - k]  # 2. slide by +new -old\n"
                        "    best = max(best, window_sum)"
                    ),
                    "breakdown": [
                        "Instead of re-summing `k` numbers from scratch on every step, slide the window by adding the 1 entering item (`nums[right]`) and subtracting the 1 leaving item (`nums[right - k]`).",
                        "Notice how `window_sum` and `best` are literally the two numbers your brain keeps track of when scanning left-to-right!",
                    ],
                },
                "tiny_example": {
                    "title": "Max Sum of 2 Consecutive Numbers in `[2, 5, 1, 8]`",
                    "code": (
                        "nums = [2, 5, 1, 8]\n"
                        "win = nums[0] + nums[1]  # 7\n"
                        "best = win               # 7\n"
                        "for right in range(2, len(nums)):\n"
                        "    win = win + nums[right] - nums[right - 2]\n"
                        "    best = max(best, win)\n"
                        "print(best)  # 9 (from 1 + 8)"
                    ),
                    "line_by_line": [
                        "Start: `win = 2 + 5 = 7`, `best = 7`.",
                        "`right = 2` (`nums[2] = 1`, leaving `nums[0] = 2`): `win = 7 + 1 - 2 = 6`, `best = max(7, 6) = 7`.",
                        "`right = 3` (`nums[3] = 8`, leaving `nums[1] = 5`): `win = 6 + 8 - 5 = 9`, `best = max(7, 9) = 9`.",
                    ],
                },
                "body_markdown": (
                    "### Your 4-Step Checklist for Any New Problem\n"
                    "1. **Restate & Edge Cases:** What if the list is empty `[]`? What if `k` is bigger than `len(nums)`?\n"
                    "2. **Solve by Hand on 4 Items:** Write down a small table of each step.\n"
                    "3. **Pick the Pattern:** Counting/Lookup -> `dict`; Sorted pairs -> Two Pointers; Subarray/Substring -> Sliding Window.\n"
                    "4. **Write Block-by-Block:** Guard check -> initial state -> loop -> return."
                ),
                "code_example": {
                    "title": "Guarded Sliding Window Function",
                    "code": (
                        "def max_window_sum(nums: list[int], k: int) -> int:\n"
                        "    # Block 1 (Guard): fail clearly if window size is impossible\n"
                        "    if k <= 0 or k > len(nums):\n"
                        "        raise ValueError('Invalid window size')\n"
                        "    # Block 2 (Initial Window)\n"
                        "    win = sum(nums[:k])\n"
                        "    best = win\n"
                        "    # Block 3 (Slide across remaining elements)\n"
                        "    for right in range(k, len(nums)):\n"
                        "        win += nums[right] - nums[right - k]\n"
                        "        best = max(best, win)\n"
                        "    return best\n"
                    ),
                },
                "common_mistakes": [
                    "Off-by-one errors in `nums[right - k]` (always verify on `right = k` -> `k - k = 0`, the very first item!).",
                    "Forgetting to check `k > len(nums)` before slicing.",
                ],
                "key_takeaway": "Always solve a 4-item example on paper first—the numbers you keep track of become your variables.",
            },
            {
                "id": "ch03-s2",
                "title": "3.2 Hash Maps, Two Pointers & Recursion",
                "zero_assumption_note": "If you ever catch yourself writing a loop inside another loop just to look something up, pause—there's almost always a faster 1-loop pattern.",
                "definition": (
                    "- **Hash Map (`dict`):** Remembers what you already saw so checking 'have I seen X?' takes 1 step instead of scanning the whole list.\n"
                    "- **Two Pointers:** Two index variables (`left` and `right`) walking toward each other or in tandem.\n"
                    "- **Recursion:** A function that solves a big input by calling itself on a **smaller** input until hitting a **base case**."
                ),
                "syntax_box": {
                    "title": "Two Pointers vs Recursion Structure",
                    "syntax": (
                        "# Two Pointers on sorted list\n"
                        "left, right = 0, len(nums) - 1\n"
                        "while left < right:\n"
                        "    # move left += 1 or right -= 1\n\n"
                        "# Recursion structure (2 mandatory parts)\n"
                        "def solve(x):\n"
                        "    if is_smallest_case(x): return base_answer  # 1. Base Case\n"
                        "    return combine(solve(smaller(x)))           # 2. Recursive Step"
                    ),
                    "breakdown": [
                        "In `while left < right:`, at least one pointer MUST move every round so the loop finishes.",
                        "In recursion, **Base Case** stops the calls; **Recursive Step** shrinks the problem strictly closer to the base case.",
                    ],
                },
                "tiny_example": {
                    "title": "Checking if Two Sorted Numbers Add to Target",
                    "code": (
                        "nums = [1, 3, 4, 8]\n"
                        "target = 7\n"
                        "left, right = 0, len(nums) - 1\n"
                        "while left < right:\n"
                        "    s = nums[left] + nums[right]\n"
                        "    if s == target: print('Found!', nums[left], nums[right]); break\n"
                        "    elif s < target: left += 1\n"
                        "    else: right -= 1"
                    ),
                    "line_by_line": [
                        "Round 1: `1 + 8 = 9 > 7` (too big -> move `right` leftwards to `4`).",
                        "Round 2: `1 + 4 = 5 < 7` (too small -> move `left` rightwards to `3`).",
                        "Round 3: `3 + 4 = 7 == 7` -> Found!",
                    ],
                },
                "body_markdown": (
                    "**Step through the interactive Call Stack Visualizer below** to watch Python push and pop recursion frames live—no mental guesswork needed!"
                ),
                "code_example": {
                    "title": "Recursive Nested List Sum (Base Case + Recursive Step)",
                    "code": (
                        "def sum_nested(node: int | list) -> int:\n"
                        "    # Block 1 (Base Case): single integer returns directly\n"
                        "    if isinstance(node, int):\n"
                        "        return node\n"
                        "    # Block 2 (Recursive Step): sum every child item\n"
                        "    total = 0\n"
                        "    for child in node:\n"
                        "        total += sum_nested(child)\n"
                        "    return total\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting the Base Case in recursion -> `RecursionError: maximum recursion depth exceeded`.",
                    "Using Two Pointers on an *unsorted* list when the logic assumes sorted order.",
                ],
                "key_takeaway": "Use `dict` for fast memory lookups, Two Pointers on sorted/symmetric arrays, and always verify your recursive Base Case first.",
            },
        ],
        "quizzes": [
            {
                "id": "ch03-q1",
                "question": "Why does Two Pointers (`left = 0, right = n - 1`) work for finding a target sum in a **sorted** list?",
                "options": [
                    "Because moving `left` right increases the sum, and moving `right` left decreases the sum predictably",
                    "Because Python sorts lists automatically inside `while` loops",
                    "It only works on strings",
                    "It checks every pair in O(N^2)",
                ],
                "correct_index": 0,
                "explanation": "Sorted order lets you safely eliminate impossible pairs in one step instead of checking all pairs.",
            },
        ],
        "project": {
            "title": "Pure-Python Text Tokenizer & Inverted Index Search Engine",
            "workspace_dir": "projects/ch03_mini_search_engine",
            "overview": "Build a keyword search engine mapping each word to matching document IDs using hash maps.",
            "architecture_steps": [
                "Write `tokenize(text)` normalizing lowercase words.",
                "Build `InvertedIndex` class mapping `word -> set of doc_ids`.",
                "Implement ranked `AND` / `OR` queries + `pytest`.",
            ],
            "milestones": [
                {"id": "ch03-m1", "label": "Implement text normalization & tokenizer"},
                {"id": "ch03-m2", "label": "Build InvertedIndex class with O(1) lookup"},
                {"id": "ch03-m3", "label": "Implement ranked search queries + pytest"},
            ],
        },
    },
    {
        "id": "ch04",
        "number": 4,
        "phase": 1,
        "phase_title": "Phase 1: Python Foundations, OOP & Logic Building",
        "title": "Essential DSA & Dynamic Programming Demystified",
        "subtitle": "Big-O speed intuition, Queues, Heaps, Graphs (DAGs), and Dynamic Programming built step-by-step from recursion to tables.",
        "status_type": "available",
        "estimated_hours": 7,
        "why_it_matters": (
            "Graphs power ML pipelines and neural computation graphs, heaps power Top-K LLM token sampling, and Dynamic Programming "
            "powers spell-checking, sequence alignment, and optimal tokenization."
        ),
        "just_in_time_tags": ["Big-O", "Queue (deque)", "Heap (heapq)", "DAG Topo Sort", "Dynamic Programming"],
        "visualizer": "dp_table",
        "sections": [
            {
                "id": "ch04-s1",
                "title": "4.1 Big-O Speed Intuition, `deque`, `heapq` & Graphs (DAGs)",
                "zero_assumption_note": "You don't need 40 academic structures. Master these 3 tools and you know what 95% of real systems use.",
                "definition": (
                    "- **Big-O:** A rough measure of how steps grow as input size `N` grows (`O(1)` instant, `O(N)` single pass, `O(N^2)` nested loop—slow for large `N`).\n"
                    "- **Queue (`collections.deque`):** First-In, First-Out line (like a checkout line).\n"
                    "- **Min-Heap (`heapq`):** Automatically keeps the smallest (or Top-K) items ready without re-sorting everything.\n"
                    "- **DAG:** Tasks connected by arrows (`A -> B` means A must finish before B) with no loops/cycles."
                ),
                "syntax_box": {
                    "title": "deque (Queue) & heapq (Top-K)",
                    "syntax": (
                        "from collections import deque\n"
                        "import heapq\n\n"
                        "q = deque(['start'])        # O(1) fast queue\n"
                        "q.append('next')            # add to back\n"
                        "first = q.popleft()         # remove from front in O(1)!\n\n"
                        "top2 = heapq.nlargest(2, [10, 50, 30, 40])  # [50, 40]"
                    ),
                    "breakdown": [
                        "Never use `my_list.pop(0)` for a queue—Python shifts every remaining item in memory (`O(N)`). Always use `deque.popleft()` (`O(1)`).",
                        "`heapq.nlargest(k, items)` grabs the top `k` items without sorting millions of elements.",
                    ],
                },
                "tiny_example": {
                    "title": "Walking a Friendship/Link Graph Layer by Layer (BFS)",
                    "code": (
                        "from collections import deque\n"
                        "graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}\n"
                        "q = deque(['A'])\n"
                        "seen = {'A'}\n"
                        "while q:\n"
                        "    node = q.popleft()\n"
                        "    print(node)\n"
                        "    for nxt in graph[node]:\n"
                        "        if nxt not in seen:\n"
                        "            seen.add(nxt)\n"
                        "            q.append(nxt)"
                    ),
                    "line_by_line": [
                        "Starts queue with `'A'` and marks `'A'` as `seen` so we never revisit it.",
                        "Pops `'A'`, prints `'A'`, and queues neighbors `'B'` and `'C'`.",
                        "Next pops `'B'`, queues `'D'`, then pops `'C'`, then `'D'` -> visits `A, B, C, D` in breadth-first order!",
                    ],
                },
                "body_markdown": (
                    "### Connecting Graphs to AI Pipelines\n"
                    "Whenever Step B depends on Step A (`clean -> train -> eval`), **Kahn's Topological Sort** uses a queue/heap of tasks with `0` remaining prerequisites to run everything in safe order—and detects circular deadlocks!"
                ),
                "code_example": {
                    "title": "Top-K & Shortest Hops Helper",
                    "code": (
                        "from collections import deque\n\n"
                        "def shortest_hops(graph: dict[str, list[str]], start: str, goal: str) -> int:\n"
                        "    q = deque([(start, 0)])\n"
                        "    seen = {start}\n"
                        "    while q:\n"
                        "        node, dist = q.popleft()\n"
                        "        if node == goal:\n"
                        "            return dist\n"
                        "        for nxt in graph.get(node, []):\n"
                        "            if nxt not in seen:\n"
                        "                seen.add(nxt)\n"
                        "                q.append((nxt, dist + 1))\n"
                        "    return -1\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting a `seen` set in BFS -> infinite loop on cycles like `A <-> B`.",
                    "Using `list.pop(0)` instead of `deque.popleft()`.",
                ],
                "key_takeaway": "FIFO queue -> `deque`, Top-K -> `heapq`, shortest unweighted path -> BFS with `seen` set.",
            },
            {
                "id": "ch04-s2",
                "title": "4.2 Dynamic Programming (DP) Demystified: Never Solve Twice",
                "zero_assumption_note": "Ignore the scary name 'Dynamic Programming'. It literally means **remembering answers to smaller subproblems so you don't recompute them**.",
                "definition": (
                    "**Dynamic Programming (DP)** solves big problems by breaking them into smaller overlapping subproblems, "
                    "storing each sub-answer once (in a `memo` dict or `dp` list/grid), and reusing it."
                ),
                "syntax_box": {
                    "title": "The 2 Ways to Write DP (Memoization vs Bottom-Up Table)",
                    "syntax": (
                        "# Way 1: Top-Down Memoization (Recursion + Cache Dict)\n"
                        "memo = {}\n"
                        "def ways(n):\n"
                        "    if n <= 1: return 1\n"
                        "    if n in memo: return memo[n]        # already solved? reuse!\n"
                        "    memo[n] = ways(n - 1) + ways(n - 2)\n"
                        "    return memo[n]\n\n"
                        "# Way 2: Bottom-Up Table (Simple Loop)\n"
                        "dp = [1] * (n + 1)\n"
                        "for i in range(2, n + 1):\n"
                        "    dp[i] = dp[i - 1] + dp[i - 2]"
                    ),
                    "breakdown": [
                        "**Why naive recursion fails:** Without `memo`, `ways(5)` calculates `ways(3)` twice and `ways(2)` three times. For `n=60`, that's over 1,000,000,000,000,000 calls!",
                        "**With DP:** Each number `0..n` is calculated **once** (`60` steps total -> instant!).",
                    ],
                },
                "tiny_example": {
                    "title": "Climbing Stairs (1 or 2 steps at a time)",
                    "code": (
                        "n = 4\n"
                        "dp = [0] * (n + 1)\n"
                        "dp[0] = 1\n"
                        "dp[1] = 1\n"
                        "for i in range(2, n + 1):\n"
                        "    dp[i] = dp[i - 1] + dp[i - 2]\n"
                        "print(dp[4])"
                    ),
                    "line_by_line": [
                        "`dp = [1, 1, 0, 0, 0]` (1 way to stand at step 0, 1 way to reach step 1).",
                        "`i = 2`: `dp[2] = dp[1] + dp[0] = 1 + 1 = 2`.",
                        "`i = 3`: `dp[3] = dp[2] + dp[1] = 2 + 1 = 3`.",
                        "`i = 4`: `dp[4] = dp[3] + dp[2] = 3 + 2 = 5` -> prints `5`!",
                    ],
                },
                "body_markdown": (
                    "**Explore the interactive 2D DP Table Stepper below!** Click `Step Cell` to watch Edit Distance (`cat` -> `cut`) fill one square at a time."
                ),
                "code_example": {
                    "title": "1D DP Optimization: Minimum Coins for Target Amount",
                    "code": (
                        "def min_coins(coins: list[int], amount: int) -> int:\n"
                        "    # Block 1: Start every amount as 'impossible' (amount + 1), except 0 -> 0 coins\n"
                        "    inf = amount + 1\n"
                        "    dp = [inf] * (amount + 1)\n"
                        "    dp[0] = 0\n\n"
                        "    # Block 2: For each sub-amount, test every valid coin and keep the minimum\n"
                        "    for a in range(1, amount + 1):\n"
                        "        for c in coins:\n"
                        "            if c <= a:\n"
                        "                dp[a] = min(dp[a], 1 + dp[a - c])\n\n"
                        "    return -1 if dp[amount] > amount else dp[amount]\n"
                    ),
                },
                "common_mistakes": [
                    "Trying to memorize a 2D formula without first writing out a tiny `3x3` grid on paper.",
                    "Forgetting the base case (`dp[0] = 0` or `dp[0] = 1`).",
                ],
                "key_takeaway": "DP = recursion + cache (or a small loop filling a `dp` array from `0` upward). Never recompute the same subproblem twice.",
            },
        ],
        "quizzes": [
            {
                "id": "ch04-q1",
                "question": "In plain English, what does adding `memo` (or a `dp` table) change in a recursive solution?",
                "options": [
                    "It runs the code on a GPU",
                    "It saves each subproblem result the first time so future calls look it up in 1 step instead of recalculating",
                    "It deletes base cases",
                    "It sorts the input list",
                ],
                "correct_index": 1,
                "explanation": "Caching sub-answers turns exponential repeated work into a single linear pass.",
            },
        ],
        "project": {
            "title": "Autocomplete, DP Spell-Checker & DAG Pipeline Scheduler",
            "workspace_dir": "projects/ch04_autocomplete_dp_scheduler",
            "overview": "Build a Trie autocomplete, 2D DP Levenshtein spell-checker, and DAG topological pipeline scheduler.",
            "architecture_steps": [
                "Implement `Trie` prefix lookup.",
                "Implement 2D DP `edit_distance(a, b)`.",
                "Implement Kahn's topological sort (`schedule_tasks`).",
            ],
            "milestones": [
                {"id": "ch04-m1", "label": "Implement Trie insert & autocomplete"},
                {"id": "ch04-m2", "label": "Implement 2D DP edit distance"},
                {"id": "ch04-m3", "label": "Implement DAG topological sort & pytest"},
            ],
        },
    },
    {
        "id": "ch05",
        "number": 5,
        "phase": 1,
        "phase_title": "Phase 1: Python Foundations, OOP & Logic Building",
        "title": "Concurrency, Async Programming & Event Loops",
        "subtitle": "Waiting vs computing, the GIL, async def, await, asyncio.gather, Semaphores, and safe retries.",
        "status_type": "available",
        "estimated_hours": 5,
        "why_it_matters": (
            "Calling LLM APIs, fetching web pages, and handling FastAPI users spend 95% of their time *waiting* on the network. "
            "`asyncio` lets one Python process handle hundreds of waiting tasks at once instead of stalling one-by-one."
        ),
        "just_in_time_tags": ["I/O vs CPU", "async def / await", "asyncio.gather", "Semaphore", "Retries"],
        "visualizer": "asyncio_loop",
        "sections": [
            {
                "id": "ch05-s1",
                "title": "5.1 `async def`, `await` & `asyncio.gather` From Scratch",
                "zero_assumption_note": "Imagine cooking pasta and boiling tea: you don't stare frozen at the kettle for 3 minutes before starting the pasta—you start the kettle, then chop vegetables while it heats!",
                "definition": (
                    "- **Synchronous (normal) code:** Waits idly for Task 1 to finish completely before starting Task 2.\n"
                    "- **Asynchronous (`asyncio`):** When Task 1 hits a network/timer wait (`await`), Python pauses Task 1 and works on Task 2 immediately.\n"
                    "- **Event Loop:** The traffic controller inside `asyncio.run(...)` that switches between paused tasks whenever one is ready."
                ),
                "syntax_box": {
                    "title": "Core `asyncio` Keywords",
                    "syntax": (
                        "import asyncio\n\n"
                        "async def fetch_data(idx: int) -> str:      # 1. `async def` defines a coroutine\n"
                        "    await asyncio.sleep(1.0)                # 2. `await` pauses & yields to other tasks\n"
                        "    return f'done-{idx}'\n\n"
                        "async def main():\n"
                        "    results = await asyncio.gather(         # 3. `gather` runs all concurrently!\n"
                        "        fetch_data(1), fetch_data(2)\n"
                        "    )\n\n"
                        "asyncio.run(main())                         # 4. starts the event loop"
                    ),
                    "breakdown": [
                        "`async def`: marks a function as pauseable (calling it creates a coroutine object; it doesn't run until `await`ed).",
                        "`await`: *\"Pause THIS task while waiting, and let the Event Loop run other tasks until this finishes.\"*",
                        "`asyncio.gather(t1, t2, ...)`: starts all given coroutines together and returns their results in the same order.",
                    ],
                },
                "tiny_example": {
                    "title": "2 Tasks Taking 1s Total Instead of 2s",
                    "code": (
                        "import asyncio\n\n"
                        "async def greet(name):\n"
                        "    await asyncio.sleep(1)\n"
                        "    return f'hi {name}'\n\n"
                        "async def main():\n"
                        "    res = await asyncio.gather(greet('A'), greet('B'))\n"
                        "    print(res)\n\n"
                        "asyncio.run(main())"
                    ),
                    "line_by_line": [
                        "`asyncio.run(main())` boots the Event Loop.",
                        "`gather(greet('A'), greet('B'))` starts `'A'`—it hits `await asyncio.sleep(1)` and pauses.",
                        "Immediately (0ms later!), the loop starts `'B'`—it also pauses for 1s.",
                        "After 1 second total, both wake up and `print(res)` outputs `['hi A', 'hi B']`!",
                    ],
                },
                "body_markdown": (
                    "### Limiting Concurrency with `asyncio.Semaphore`\n"
                    "Firing 1,000 API calls at once gets you blocked (`429 Too Many Requests`). Wrap calls in `sem = asyncio.Semaphore(5)` and `async with sem:` so **at most 5** run at any moment.\n\n"
                    "**Test the Asyncio Event Loop Simulator below** to see Sequential vs `gather` vs `Semaphore(2)` timelines!"
                ),
                "code_example": {
                    "title": "Bounded Async Worker with Semaphore",
                    "code": (
                        "import asyncio\n\n"
                        "async def safe_fetch(sem: asyncio.Semaphore, item_id: int) -> str:\n"
                        "    # Block 1: Wait here if 3 workers are already active\n"
                        "    async with sem:\n"
                        "        await asyncio.sleep(0.1)\n"
                        "        return f'ok-{item_id}'\n\n"
                        "async def run_batch() -> list[str]:\n"
                        "    # Block 2: Cap concurrent tasks to 3\n"
                        "    sem = asyncio.Semaphore(3)\n"
                        "    tasks = [safe_fetch(sem, i) for i in range(10)]\n"
                        "    return list(await asyncio.gather(*tasks))\n"
                    ),
                },
                "common_mistakes": [
                    "Calling `time.sleep(2)` or `requests.get()` inside `async def`—that freezes the ENTIRE event loop! Use `await asyncio.sleep(2)` or `httpx.AsyncClient`.",
                    "Writing `for x in items: await fetch(x)`—that runs one-by-one sequentially! Use `asyncio.gather(...)`.",
                ],
                "key_takeaway": "Use `async def` + `await` for waiting/network I/O, `asyncio.gather` to overlap tasks, and `Semaphore` to avoid rate limits.",
            },
        ],
        "quizzes": [
            {
                "id": "ch05-q1",
                "question": "Why does `for x in items: await fetch(x)` fail to run concurrently?",
                "options": [
                    "Python forbids `await` inside loops",
                    "Each `await` waits until `fetch(x)` finishes before starting the next item",
                    "Loops disable the event loop",
                    "`fetch` runs on another CPU",
                ],
                "correct_index": 1,
                "explanation": "Use `asyncio.gather(*(fetch(x) for x in items))` so all coroutines start waiting together.",
            },
        ],
        "project": {
            "title": "Async Rate-Limited API Batch Harvester",
            "workspace_dir": "projects/ch05_async_harvester",
            "overview": "Fetch batches concurrently with `asyncio.Semaphore` caps and exponential backoff retries.",
            "architecture_steps": [
                "Write `retry_async` with exponential sleep backoff.",
                "Bound batch execution with `asyncio.Semaphore` and `gather`.",
                "Verify speedup & failure handling with `pytest`.",
            ],
            "milestones": [
                {"id": "ch05-m1", "label": "Implement exponential backoff retry coroutine"},
                {"id": "ch05-m2", "label": "Add Semaphore concurrency cap"},
                {"id": "ch05-m3", "label": "Pass pytest async speedup checks"},
            ],
        },
    },
]
