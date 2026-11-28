"""Phase 1 Part A (Chapters 1-4): Python Core, Files, Dedicated `os` Library + Automation, and OOP From Scratch."""

from __future__ import annotations

from typing import Any

PHASE_1A_CHAPTERS: list[dict[str, Any]] = [
    # =========================================================================
    # CHAPTER 1: Python Core Building Blocks
    # =========================================================================
    {
        "id": "ch01",
        "number": 1,
        "phase": 1,
        "phase_title": "Phase 1: Python From Zero — Basics, Files, `os`, OOP & Logic",
        "title": "Python Core Building Blocks (From Scratch)",
        "subtitle": "Variables, types, if/else decisions, for & while loops, lists/dicts/sets, one-line loops (comprehensions), and functions.",
        "status_type": "available",
        "estimated_hours": 6,
        "why_it_matters": (
            "Nothing in AI works without fluent Python basics. Every file automation, dataset cleaner, API server, and model training loop "
            "is built out of variables, decisions, loops, lists, dictionaries, and functions."
        ),
        "just_in_time_tags": ["Variables & Types", "if / elif / else", "for & while", "Lists & Dicts", "Comprehensions", "Functions"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch01-s1",
                "title": "1.1 Variables, Basic Types & Printing Output",
                "zero_assumption_note": "Python runs your script from Line 1 down to the bottom, one instruction at a time.",
                "definition": (
                    "A **variable** is a named label attached to a piece of data so you can reuse or update it later. "
                    "A **data type** tells Python what kind of data it is: whole number (`int`), decimal (`float`), text (`str`), or True/False (`bool`)."
                ),
                "syntax_box": {
                    "title": "Creating Variables, Converting Types & Printing",
                    "syntax": (
                        "name = 'Sara'            # str (text inside quotes)\n"
                        "age = 22                 # int (whole number)\n"
                        "gpa = 3.85               # float (decimal number)\n"
                        "is_enrolled = True       # bool (True or False — capital T/F)\n\n"
                        "num = int('15')          # converts text '15' -> number 15\n"
                        "print(f'{name} is {age}')  # f-string inserts variables inside {}"
                    ),
                    "breakdown": [
                        "`=` means **store the value on the right under the name on the left** (not math equality).",
                        "Anything inside quotes (`'...'` or `\"...\"`) is text (`str`), even `'15'`.",
                        "An **f-string** (`f'...'`) lets you drop variables straight into `{...}` when printing.",
                    ],
                },
                "tiny_example": {
                    "title": "Why `'5' + '5'` is `'55'` Instead of `10`",
                    "code": (
                        "a = '5'\n"
                        "b = '5'\n"
                        "print(a + b)             # glues text together -> '55'\n"
                        "print(int(a) + int(b))   # converts to numbers first -> 10"
                    ),
                    "line_by_line": [
                        "Lines 1–2: `'5'` has quotes, so Python treats `a` and `b` as text (`str`).",
                        "Line 3: `+` on two strings joins them into `'55'`.",
                        "Line 4: `int(a)` turns `'5'` into the integer `5`, so `5 + 5` prints `10`.",
                    ],
                },
                "body_markdown": (
                    "### Checking Any Type When Unsure\n"
                    "Whenever a bug surprises you, run `print(type(x), x)` to see both what Python thinks `x` is (`<class 'str'>` vs `<class 'int'>`) and what value it holds."
                ),
                "code_example": {
                    "title": "Simple Study Hours Calculator",
                    "code": (
                        "# Block 1: Store inputs\n"
                        "topic = 'Python'\n"
                        "hours_per_day = 2\n"
                        "days = 6\n\n"
                        "# Block 2: Compute total\n"
                        "total = hours_per_day * days\n\n"
                        "# Block 3: Display summary\n"
                        "print(f'Studied {topic} for {total} hours.')\n"
                    ),
                },
                "common_mistakes": [
                    "Trying to add text and a number directly (`'Age: ' + 20` crashes! Use `f'Age: {20}'`).",
                    "Putting spaces or starting a variable with a number (`my score = 10` is invalid; use `my_score = 10`).",
                ],
                "key_takeaway": "Use `int()`/`float()` to turn text into numbers before doing math, and `f'...'` strings for clean output.",
            },
            {
                "id": "ch01-s2",
                "title": "1.2 Making Decisions (`if / elif / else`)",
                "zero_assumption_note": "Python uses **4 spaces on the left (indentation)** to know which lines run inside an `if` block.",
                "definition": (
                    "An **`if / elif / else` statement** asks a True/False question and chooses which block of code to run."
                ),
                "syntax_box": {
                    "title": "Decision Tree Syntax",
                    "syntax": (
                        "if score >= 80:\n"
                        "    print('Grade A')\n"
                        "elif score >= 60:\n"
                        "    print('Pass')\n"
                        "else:\n"
                        "    print('Try again')"
                    ),
                    "breakdown": [
                        "Python checks from top to bottom and runs **only the first branch that is True**.",
                        "Comparisons: `==` (is equal?), `!=` (not equal?), `>`, `<`, `>=`, `<=`.",
                        "Combine checks: `and` (both True), `or` (at least one True), `not` (flips True <-> False).",
                    ],
                },
                "tiny_example": {
                    "title": "Checking Two Conditions with `and`",
                    "code": (
                        "has_ticket = True\n"
                        "age = 19\n"
                        "if has_ticket and age >= 18:\n"
                        "    print('Welcome in!')\n"
                        "else:\n"
                        "    print('Entry denied')"
                    ),
                    "line_by_line": [
                        "Line 3: Checks BOTH `has_ticket` (`True`) AND `age >= 18` (`19 >= 18` is `True`).",
                        "Line 4: Since both are `True`, prints `Welcome in!` and skips the `else` block.",
                    ],
                },
                "body_markdown": (
                    "### Why `elif` Matters Instead of Multiple `if`s\n"
                    "If you wrote two separate `if` statements (`if score >= 80:` and `if score >= 60:`), a score of `90` would trigger **both**! "
                    "Using `elif` guarantees at most one branch runs."
                ),
                "code_example": {
                    "title": "Safe Division Guard",
                    "code": (
                        "total_points = 450\n"
                        "num_tests = 0\n\n"
                        "if num_tests == 0:\n"
                        "    print('No tests taken yet.')\n"
                        "else:\n"
                        "    avg = total_points / num_tests\n"
                        "    print(f'Average: {avg}')\n"
                    ),
                },
                "common_mistakes": [
                    "Writing `if x = 5:` instead of `if x == 5:` (single `=` assigns; double `==` compares).",
                    "Forgetting the colon `:` at the end of `if`, `elif`, or `else:`.",
                ],
                "key_takeaway": "Use `==` to compare, `elif` for mutually exclusive branches, and always check edge cases like `0` before dividing.",
            },
            {
                "id": "ch01-s3",
                "title": "1.3 Repeating Work (`for` Loops, `range()` & `while` Loops)",
                "zero_assumption_note": "If you ever copy-paste the same line 5 times, a loop does it cleaner and works for 5 or 5,000,000 items.",
                "definition": (
                    "A **`for` loop** runs a block once for each item in a sequence. A **`while` loop** keeps repeating as long as a condition stays `True`."
                ),
                "syntax_box": {
                    "title": "for Loop, range(), and while Loop",
                    "syntax": (
                        "for item in ['a', 'b', 'c']:\n"
                        "    print(item)\n\n"
                        "for i in range(3):          # i takes values 0, 1, 2\n"
                        "    print(i)\n\n"
                        "count = 3\n"
                        "while count > 0:\n"
                        "    print(count)\n"
                        "    count -= 1              # MUST update count so loop ends!"
                    ),
                    "breakdown": [
                        "`range(3)` produces `0, 1, 2` (starts at `0`, stops *before* `3`). `range(1, 4)` produces `1, 2, 3`.",
                        "`break` immediately stops the loop early; `continue` skips the rest of the current round and moves to the next item.",
                    ],
                },
                "tiny_example": {
                    "title": "Tracing a Running Total Step-by-Step",
                    "code": (
                        "nums = [10, 20, 30]\n"
                        "total = 0\n"
                        "for n in nums:\n"
                        "    total = total + n\n"
                        "    print(f'Added {n}, total is now {total}')\n"
                        "print(f'Final: {total}')"
                    ),
                    "line_by_line": [
                        "Before loop: `total = 0`.",
                        "Round 1 (`n = 10`): `total` becomes `0 + 10 = 10`.",
                        "Round 2 (`n = 20`): `total` becomes `10 + 20 = 30`.",
                        "Round 3 (`n = 30`): `total` becomes `30 + 30 = 60`.",
                        "Line 6 (not indented): runs ONCE at the end -> `Final: 60`.",
                    ],
                },
                "body_markdown": (
                    "### Using `continue` to Skip Junk\n"
                    "Inside a loop over lines or numbers, `if val < 0: continue` skips invalid entries immediately so your main logic stays clean."
                ),
                "code_example": {
                    "title": "Skipping Negative Numbers While Summing",
                    "code": (
                        "readings = [12, -5, 8, -1, 10]\n"
                        "valid_sum = 0\n\n"
                        "for val in readings:\n"
                        "    if val < 0:\n"
                        "        continue\n"
                        "    valid_sum += val\n\n"
                        "print(f'Valid sum: {valid_sum}')  # 30\n"
                    ),
                },
                "common_mistakes": [
                    "Putting `total = 0` *inside* the loop (resets it back to 0 every round!).",
                    "Writing a `while` loop without changing the condition variable (infinite loop).",
                ],
                "key_takeaway": "Set initial totals *before* the loop, use `for` for collections/`range()`, and use `continue` to skip invalid items cleanly.",
            },
            {
                "id": "ch01-s4",
                "title": "1.4 Lists, Dictionaries, Sets & Tuples",
                "zero_assumption_note": "Think of a **list** like a numbered shelf (`0, 1, 2`), and a **dictionary** like labeled drawers (`'name'`, `'age'`).",
                "definition": (
                    "- **`list` (`[a, b]`):** Ordered collection indexed by position (`0, 1, 2...`).\n"
                    "- **`dict` (`{k: v}`):** Key -> Value lookup table.\n"
                    "- **`set` (`{a, b}`):** Unordered unique items only (auto-removes duplicates).\n"
                    "- **`tuple` (`(a, b)`):** Fixed, unchangeable list."
                ),
                "syntax_box": {
                    "title": "Essential List & Dictionary Syntax",
                    "syntax": (
                        "fruits = ['apple', 'banana']\n"
                        "fruits.append('mango')          # adds to end\n"
                        "print(fruits[0], fruits[-1])    # 'apple', 'mango'\n\n"
                        "person = {'name': 'Sam', 'age': 25}\n"
                        "person['city'] = 'Delhi'        # add or overwrite key\n"
                        "job = person.get('job', 'None') # safe lookup (no KeyError crash!)"
                    ),
                    "breakdown": [
                        "`fruits[0]` is item #1; `fruits[-1]` is the last item.",
                        "`person['job']` crashes if `'job'` doesn't exist; `person.get('job', 'None')` returns `'None'` safely.",
                        "Copying lists: `b = a` only makes a second label to the **same** list! Use `b = a.copy()` to make a real copy.",
                    ],
                },
                "tiny_example": {
                    "title": "Looping Over a Dictionary's Keys & Values",
                    "code": (
                        "scores = {'math': 90, 'python': 95}\n"
                        "for subject, pts in scores.items():\n"
                        "    print(f'{subject}: {pts}')"
                    ),
                    "line_by_line": [
                        "`scores.items()` yields each `(key, value)` pair one at a time.",
                        "Round 1: `subject='math'`, `pts=90`. Round 2: `subject='python'`, `pts=95`.",
                    ],
                },
                "body_markdown": (
                    "### Removing Duplicates Quickly with `set()`\n"
                    "`set(['ai', 'ml', 'ai'])` immediately gives `{'ai', 'ml'}`—handy whenever cleaning repeated tags or words."
                ),
                "code_example": {
                    "title": "Safe List Copy & Deduplicating Tags",
                    "code": (
                        "skills = ['python', 'sql']\n"
                        "resume_skills = skills.copy()\n"
                        "resume_skills.append('pytorch')\n"
                        "print('Base:', skills)\n"
                        "print('Resume:', resume_skills)\n\n"
                        "tags = ['ai', 'py', 'ai', 'ml']\n"
                        "print('Unique:', sorted(set(tags)))\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting Python list indexes start at `0` (`items[1]` is the second item).",
                    "Writing `copy = original` on a list instead of `copy = original.copy()`.",
                ],
                "key_takeaway": "Use `list` for ordered data, `dict` + `.get()` for named fields, `set` for uniqueness, and `.copy()` before mutating.",
            },
            {
                "id": "ch01-s5",
                "title": "1.5 One-Line `for` Loops Explained (List Comprehensions)",
                "zero_assumption_note": "One-line loops like `[x * 2 for x in nums if x > 0]` are NOT new magic—they are just a normal 4-line `for` loop folded onto one line!",
                "definition": (
                    "A **list comprehension** builds a new list by transforming and optionally filtering items from an existing collection on one line."
                ),
                "syntax_box": {
                    "title": "Normal `for` Loop vs One-Line Comprehension",
                    "syntax": (
                        "# 4-line normal loop:\n"
                        "result = []\n"
                        "for x in items:\n"
                        "    if condition(x):\n"
                        "        result.append(transform(x))\n\n"
                        "# Exact same thing on 1 line:\n"
                        "result = [transform(x) for x in items if condition(x)]"
                    ),
                    "breakdown": [
                        "**Read it in 3 parts:** `[ WHAT_TO_KEEP   for ITEM in COLLECTION   if FILTER_CONDITION ]`.",
                        "Part 1 (`transform(x)`): what goes into the new list.",
                        "Part 2 (`for x in items`): the loop header.",
                        "Part 3 (`if condition(x)`): optional filter—only items passing this `if` enter the new list!",
                    ],
                },
                "tiny_example": {
                    "title": "Doubling Only Even Numbers",
                    "code": (
                        "nums = [1, 2, 3, 4, 5]\n"
                        "evens_doubled = [n * 2 for n in nums if n % 2 == 0]\n"
                        "print(evens_doubled)"
                    ),
                    "line_by_line": [
                        "`n = 1`: `1 % 2 == 0` is False -> skipped.",
                        "`n = 2`: True -> adds `2 * 2 = 4`.",
                        "`n = 3`: False -> skipped.",
                        "`n = 4`: True -> adds `4 * 2 = 8` -> prints `[4, 8]`!",
                    ],
                },
                "body_markdown": (
                    "### Rule of Thumb\n"
                    "Only use a one-line comprehension when it is short and easy to read. For complex steps, a normal `for` loop is always better."
                ),
                "code_example": {
                    "title": "Cleaning Messy Usernames & Counting Passing Scores",
                    "code": (
                        "raw_names = ['  Sara ', '', '  ALEX', '   ']\n"
                        "clean_names = [name.strip().lower() for name in raw_names if name.strip()]\n"
                        "print(clean_names)\n\n"
                        "scores = [45, 80, 62, 50]\n"
                        "pass_count = sum(1 for s in scores if s >= 60)\n"
                        "print('Passed:', pass_count)\n"
                    ),
                },
                "common_mistakes": [
                    "Trying to cram complicated multi-branch logic into one unreadable comprehension.",
                ],
                "key_takeaway": "`[expr for x in items if cond]` is just shorthand for `out = []; for x in items: if cond: out.append(expr)`.",
            },
            {
                "id": "ch01-s6",
                "title": "1.6 Functions (`def`, `return` vs `print` & Safe Defaults)",
                "zero_assumption_note": "Think of a function like a blender: ingredients go in (parameters), work happens inside, and a smoothie comes back (`return`).",
                "definition": (
                    "A **function** gives a name to a reusable block of steps so you can call it anywhere with different inputs."
                ),
                "syntax_box": {
                    "title": "Function Definition & Calling",
                    "syntax": (
                        "def add_bonus(score: int, bonus: int = 5) -> int:\n"
                        "    new_score = score + bonus\n"
                        "    return new_score\n\n"
                        "final = add_bonus(80)       # uses default bonus=5 -> 85\n"
                        "final2 = add_bonus(80, 10)  # overrides bonus=10 -> 90"
                    ),
                    "breakdown": [
                        "`def` defines the function; it doesn't run until you call `add_bonus(...)`.",
                        "`: int` and `-> int` are **type hints** telling humans what types go in and come out.",
                        "`bonus: int = 5` is a **default argument** used if the caller doesn't pass a second value.",
                        "`return` hands the result back to the caller and exits the function.",
                    ],
                },
                "tiny_example": {
                    "title": "Why `print()` Cannot Replace `return`",
                    "code": (
                        "def broken_double(x):\n"
                        "    print(x * 2)\n\n"
                        "def working_double(x):\n"
                        "    return x * 2\n\n"
                        "a = broken_double(5)\n"
                        "b = working_double(5)\n"
                        "print('a is:', a, '| b is:', b)"
                    ),
                    "line_by_line": [
                        "`broken_double(5)` prints `10`, then ends with no `return`, so `a` becomes `None`.",
                        "`working_double(5)` returns `10`, so `b` becomes `10` (and you can do `b + 1`!).",
                    ],
                },
                "body_markdown": (
                    "### One Common Beginner Trap: Never Put `= []` as a Default\n"
                    "Suppose you write `def add_item(x, items=[]):`. Python creates that `[]` **only once** and reuses it across every call—so items from yesterday's call leak into today's call!\n"
                    "- **Fix:** Write `items=None` instead (`None` is Python's built-in word for *'nothing was passed'*), then check `if items is None:` inside the function with a normal `if / else`."
                ),
                "code_example": {
                    "title": "Simple Function With Default Value + Safe Optional List",
                    "code": (
                        "# Block 1: Simple function with a default parameter\n"
                        "def apply_discount(price: float, discount_percent: float = 10.0) -> float:\n"
                        "    saved = price * (discount_percent / 100)\n"
                        "    return round(price - saved, 2)\n\n"
                        "print(apply_discount(100))      # 90.0\n"
                        "print(apply_discount(100, 25))  # 75.0\n\n"
                        "# Block 2: Safe optional list using `None` and plain if/else\n"
                        "def add_tag(tag: str, existing=None):\n"
                        "    if existing is None:\n"
                        "        result = []\n"
                        "    else:\n"
                        "        result = existing.copy()\n"
                        "    if tag not in result:\n"
                        "        result.append(tag)\n"
                        "    return result\n\n"
                        "print(add_tag('python'))\n"
                        "print(add_tag('ai'))\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting `return` inside a function and wondering why the caller gets `None`.",
                    "Using `items=[]` as a default argument instead of `items=None`.",
                ],
                "key_takeaway": "Functions should `return` values (not just `print`), and optional lists should default to `None` followed by `if existing is None:`.",
            },
        ],
        "quizzes": [
            {
                "id": "ch01-q1",
                "question": "What does `[x * 10 for x in [1, 2, 3] if x > 1]` produce?",
                "options": ["[10, 20, 30]", "[20, 30]", "[2, 3]", "Error"],
                "correct_index": 1,
                "explanation": "`if x > 1` skips `1`, keeping `2` and `3`, then `x * 10` produces `[20, 30]`.",
            },
            {
                "id": "ch01-q2",
                "question": "What does `a` equal after `def f(x): print(x + 1)` then `a = f(4)`?",
                "options": ["5", "4", "None", "Error"],
                "correct_index": 2,
                "explanation": "Without a `return` statement, a Python function always returns `None`.",
            },
        ],
        "project": {
            "title": "Student Grade & Tag Analyzer Script",
            "workspace_dir": "projects/ch01_grade_analyzer",
            "overview": "Use variables, loops, comprehensions, dictionaries, and clean functions to summarize student scores and tags.",
            "architecture_steps": [
                "Write `clean_tags(raw_tags)` using a list comprehension + `set`.",
                "Write `summarize_scores(scores)` returning passed, failed, and average.",
                "Verify every function with `assert` checks.",
            ],
            "milestones": [
                {"id": "ch01-m1", "label": "Implement clean_tags using comprehension & set"},
                {"id": "ch01-m2", "label": "Implement summarize_scores handling empty lists"},
                {"id": "ch01-m3", "label": "Pass all pytest checks"},
            ],
        },
    },

    # =========================================================================
    # CHAPTER 2: Working With Files (txt, pathlib, try/except, json, csv)
    # =========================================================================
    {
        "id": "ch02",
        "number": 2,
        "phase": 1,
        "phase_title": "Phase 1: Python From Zero — Basics, Files, `os`, OOP & Logic",
        "title": "Working With Files (`open`, `pathlib`, `json`, `csv`)",
        "subtitle": "Reading & writing plain .txt files, pathlib.Path, try/except error handling, JSON/JSONL datasets, and CSV spreadsheets.",
        "status_type": "available",
        "estimated_hours": 5,
        "why_it_matters": (
            "Real AI scripts don't hardcode text inside `.py` files—they read `.txt` notes, `.json` configs, `.jsonl` datasets, and `.csv` tables from disk safely."
        ),
        "just_in_time_tags": ["open() & with", "pathlib.Path", "try / except", "json & jsonl", "csv.DictReader"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch02-s1",
                "title": "2.1 Reading & Writing Plain `.txt` Files (`open` & `with`)",
                "zero_assumption_note": "Start with plain `.txt` files first. Once 3 lines of `.txt` feel effortless, JSON and CSV are easy.",
                "definition": (
                    "Opening a file connects your Python script to a file on your hard drive so you can read its contents or save new text into it."
                ),
                "syntax_box": {
                    "title": "The Safe `with open(...)` Pattern",
                    "syntax": (
                        "with open('notes.txt', 'w', encoding='utf-8') as f:\n"
                        "    f.write('Hello Python\\n')\n\n"
                        "with open('notes.txt', 'r', encoding='utf-8') as f:\n"
                        "    for line in f:\n"
                        "        print(line.strip())"
                    ),
                    "breakdown": [
                        "`'w'` = **write** (creates or overwrites). `'a'` = **append** (adds to end). `'r'` = **read**.",
                        "`with ... as f:` **automatically closes** the file when the indented block ends.",
                        "`encoding='utf-8'` prevents Windows crashes on special characters or emojis.",
                        "`line.strip()` removes the invisible `'\\n'` newline at the end of each line.",
                    ],
                },
                "tiny_example": {
                    "title": "Writing 2 Lines and Counting Non-Empty Lines",
                    "code": (
                        "with open('demo.txt', 'w', encoding='utf-8') as f:\n"
                        "    f.write('First line\\n\\nSecond line\\n')\n\n"
                        "count = 0\n"
                        "with open('demo.txt', 'r', encoding='utf-8') as f:\n"
                        "    for line in f:\n"
                        "        if line.strip():\n"
                        "            count += 1\n"
                        "print('Non-empty lines:', count)"
                    ),
                    "line_by_line": [
                        "Lines 1–2: Creates `demo.txt` with 3 lines (middle line is blank).",
                        "Line 6: Loops one line at a time.",
                        "Line 7: `'\\n'.strip()` becomes `''` (empty/False), so blank lines are skipped!",
                        "Line 9: Prints `Non-empty lines: 2`.",
                    ],
                },
                "body_markdown": (
                    "### Reading All at Once vs Line by Line\n"
                    "- `f.read()` loads the **entire file** as one string (good for small files).\n"
                    "- `for line in f:` reads **one line at a time** (essential for huge 2 GB files!)."
                ),
                "code_example": {
                    "title": "Appending a Log Entry Without Erasing Old Lines",
                    "code": (
                        "def append_log(filename: str, message: str) -> None:\n"
                        "    with open(filename, 'a', encoding='utf-8') as f:\n"
                        "        f.write(message + '\\n')\n\n"
                        "append_log('run.log', '[INFO] Started')\n"
                        "append_log('run.log', '[INFO] Finished')\n"
                        "print(open('run.log', encoding='utf-8').read())\n"
                    ),
                },
                "common_mistakes": [
                    "Opening with `'w'` when you meant `'a'` (accidentally erases old lines!).",
                    "Forgetting `encoding='utf-8'` on Windows.",
                ],
                "key_takeaway": "Always use `with open(..., encoding='utf-8') as f:`, loop `for line in f:` for large files, and call `.strip()`.",
            },
            {
                "id": "ch02-s2",
                "title": "2.2 Clean Paths (`pathlib.Path`) & Handling Errors (`try / except`)",
                "zero_assumption_note": "On Windows, `'C:\\new\\test.txt'` breaks because `\\n` means newline! `pathlib.Path` eliminates path headaches forever.",
                "definition": (
                    "- **`pathlib.Path`:** A clean object representing a file or folder path across Windows, Mac, and Linux.\n"
                    "- **`try / except`:** Catches predictable errors (like a missing file) cleanly instead of crashing."
                ),
                "syntax_box": {
                    "title": "Path Operations & Specific Error Handling",
                    "syntax": (
                        "from pathlib import Path\n\n"
                        "p = Path('data') / 'raw' / 'notes.txt'\n"
                        "p.parent.mkdir(parents=True, exist_ok=True)\n\n"
                        "try:\n"
                        "    text = p.read_text(encoding='utf-8')\n"
                        "except FileNotFoundError:\n"
                        "    text = ''"
                    ),
                    "breakdown": [
                        "`/` joins folders cleanly regardless of OS.",
                        "`p.exists()` checks if a file or folder exists.",
                        "`p.parent.mkdir(parents=True, exist_ok=True)` safely creates missing parent folders.",
                        "Always catch a **specific** error (`FileNotFoundError`, `ValueError`), never bare `except:`.",
                    ],
                },
                "tiny_example": {
                    "title": "Safely Reading a Missing File",
                    "code": (
                        "from pathlib import Path\n\n"
                        "missing = Path('does_not_exist.txt')\n"
                        "try:\n"
                        "    content = missing.read_text(encoding='utf-8')\n"
                        "except FileNotFoundError:\n"
                        "    print('Could not find file—using empty default.')\n"
                        "    content = ''"
                    ),
                    "line_by_line": [
                        "Line 4: Tries to read `does_not_exist.txt`.",
                        "Line 5: Jumps straight to `except FileNotFoundError:` instead of crashing.",
                        "Lines 6–7: Prints a polite message and sets `content = ''`.",
                    ],
                },
                "body_markdown": (
                    "### Ensuring Output Folders Exist Before Writing\n"
                    "Always call `out_path.parent.mkdir(parents=True, exist_ok=True)` before saving into a subfolder like `output/2026/report.txt`."
                ),
                "code_example": {
                    "title": "Writing Safely into Nested Output Folders",
                    "code": (
                        "from pathlib import Path\n\n"
                        "out = Path('reports') / 'daily' / 'summary.txt'\n"
                        "out.parent.mkdir(parents=True, exist_ok=True)\n"
                        "out.write_text('All checks passed!\\n', encoding='utf-8')\n"
                        "print(out.read_text(encoding='utf-8').strip())\n"
                    ),
                },
                "common_mistakes": [
                    "Trying to write into a subfolder before creating it -> `FileNotFoundError`.",
                    "Writing bare `except:` which silently hides real typos.",
                ],
                "key_takeaway": "Use `Path('a') / 'b.txt'`, create parent folders with `.mkdir(parents=True, exist_ok=True)`, and catch specific errors.",
            },
            {
                "id": "ch02-s3",
                "title": "2.3 Loading & Saving JSON, JSONL & CSV Files",
                "zero_assumption_note": "Never split CSV lines with `line.split(',')` or parse JSON by hand—Python has `json` and `csv` built in!",
                "definition": (
                    "- **JSON (`.json`):** Text format matching Python `dict`s and `list`s—used in configs and APIs.\n"
                    "- **JSONL (`.jsonl`):** 'JSON Lines'—one JSON object per line (standard for LLM datasets).\n"
                    "- **CSV (`.csv`):** Comma-separated spreadsheet table."
                ),
                "syntax_box": {
                    "title": "`json` and `csv.DictReader` Basics",
                    "syntax": (
                        "import csv, json\n"
                        "from pathlib import Path\n\n"
                        "data = json.loads('{\"name\": \"AI\"}')   # string -> dict\n"
                        "text = json.dumps({'name': 'AI'})       # dict -> string\n\n"
                        "with Path('data.csv').open('r', encoding='utf-8', newline='') as f:\n"
                        "    rows = list(csv.DictReader(f))"
                    ),
                    "breakdown": [
                        "`json.load(f)` / `json.dump(obj, f)` work on open files.",
                        "`json.loads(s)` / `json.dumps(obj)` ('s' = string) work on strings—ideal for `.jsonl` lines!",
                        "`csv.DictReader(f)` reads each spreadsheet row as a `dict` keyed by header names.",
                    ],
                },
                "tiny_example": {
                    "title": "Converting Python Dict -> JSON String -> Python Dict",
                    "code": (
                        "import json\n"
                        "record = {'user': 'Sam', 'score': 95}\n"
                        "as_text = json.dumps(record)\n"
                        "back_to_dict = json.loads(as_text)\n"
                        "print(type(as_text), as_text)\n"
                        "print(type(back_to_dict), back_to_dict['score'])"
                    ),
                    "line_by_line": [
                        "`json.dumps(record)` converts the dict into a text string.",
                        "`json.loads(as_text)` converts that string back into a Python `dict` so `back_to_dict['score']` works!",
                    ],
                },
                "body_markdown": (
                    "### Skipping Corrupt JSONL Lines Safely\n"
                    "Wrapping `json.loads(line)` inside `try / except json.JSONDecodeError:` skips a single broken line without crashing the whole pipeline."
                ),
                "code_example": {
                    "title": "Resilient JSONL Loader",
                    "code": (
                        "import json\n"
                        "from pathlib import Path\n\n"
                        "p = Path('sample.jsonl')\n"
                        "p.write_text('{\"text\": \"ok\"}\\n{broken\\n{\"text\": \"good\"}\\n', encoding='utf-8')\n\n"
                        "records = []\n"
                        "with p.open('r', encoding='utf-8') as f:\n"
                        "    for line in f:\n"
                        "        if not line.strip():\n"
                        "            continue\n"
                        "        try:\n"
                        "            records.append(json.loads(line))\n"
                        "        except json.JSONDecodeError:\n"
                        "            continue\n"
                        "print(records)\n"
                    ),
                },
                "common_mistakes": [
                    "Mixing up `json.load(f)` (file) and `json.loads(s)` (string).",
                    "Forgetting `newline=''` when opening CSV files for `csv` readers/writers.",
                ],
                "key_takeaway": "Use `json.loads/dumps` for JSONL lines and `csv.DictReader` with `newline=''` for CSV tables.",
            },
        ],
        "quizzes": [
            {
                "id": "ch02-q1",
                "question": "Which mode opens a file to **add** new lines at the end without erasing existing lines?",
                "options": ["'r'", "'w'", "'a'", "'x'"],
                "correct_index": 2,
                "explanation": "`'w'` overwrites the file; `'a'` appends to the end.",
            },
            {
                "id": "ch02-q2",
                "question": "What is the difference between `json.load(f)` and `json.loads(line)`?",
                "options": [
                    "No difference",
                    "`json.load(f)` reads from an open file; `json.loads(line)` parses a string",
                    "`json.loads` only works on CSV",
                    "`json.load` writes to disk",
                ],
                "correct_index": 1,
                "explanation": "`load` takes a file object; `loads` takes a JSON string.",
            },
        ],
        "project": {
            "title": "Dataset Inspector & File Converter CLI",
            "workspace_dir": "projects/ch02_file_inspector",
            "overview": "Read a messy CSV file safely using `Path` and `csv.DictReader`, filter invalid rows, and export clean JSONL lines.",
            "architecture_steps": [
                "Check file existence with `Path`.",
                "Read CSV rows using `csv.DictReader` and `encoding='utf-8'`.",
                "Write clean JSONL lines and verify with `pytest`.",
            ],
            "milestones": [
                {"id": "ch02-m1", "label": "Read CSV safely with Path & encoding='utf-8'"},
                {"id": "ch02-m2", "label": "Filter invalid rows cleanly"},
                {"id": "ch02-m3", "label": "Write JSONL output and pass pytest"},
            ],
        },
    },

    # =========================================================================
    # CHAPTER 3: Dedicated Single-Library Chapter — The `os` Library & Automations
    # =========================================================================
    {
        "id": "ch03",
        "number": 3,
        "phase": 1,
        "phase_title": "Phase 1: Python From Zero — Basics, Files, `os`, OOP & Logic",
        "title": "The `os` Library & Simple File Automations",
        "subtitle": "Inspecting folders (os.listdir, os.walk), joining paths (os.path), creating/renaming files & folders, and environment variables (os.getenv).",
        "status_type": "available",
        "estimated_hours": 4,
        "why_it_matters": (
            "Python's built-in `os` module lets your scripts talk directly to your operating system—scanning folders of 1,000 files, "
            "organizing messy downloads automatically, checking file sizes, and reading API keys safely from environment variables."
        ),
        "just_in_time_tags": ["os.listdir", "os.path", "os.makedirs", "os.rename", "os.walk", "os.getenv"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch03-s1",
                "title": "3.1 Exploring Folders & Safe Paths (`os.getcwd`, `os.listdir`, `os.path`)",
                "zero_assumption_note": "Before automating folders, you must know how Python asks Windows/Linux: *'Where am I?'* and *'What files are inside this folder?'*",
                "definition": (
                    "The **`os` module** lets Python inspect folders, check whether a path is a file or directory, and split filenames from extensions."
                ),
                "syntax_box": {
                    "title": "Essential `os` & `os.path` Functions",
                    "syntax": (
                        "import os\n\n"
                        "here = os.getcwd()                          # current working folder\n"
                        "items = os.listdir(here)                    # list of file/folder names\n"
                        "full = os.path.join(here, 'notes.txt')      # safely join folder + file\n"
                        "print(os.path.isfile(full))                 # True if it's a file\n"
                        "name, ext = os.path.splitext('photo.jpg')   # ('photo', '.jpg')"
                    ),
                    "breakdown": [
                        "`os.listdir(folder)` returns **just the names** (`['a.txt', 'img.png']`), NOT full paths—always combine with `os.path.join(folder, name)`!",
                        "`os.path.isfile(full)` skips subfolders when you only want files.",
                        "`os.path.splitext('report.pdf')` splits into `('report', '.pdf')` cleanly.",
                    ],
                },
                "tiny_example": {
                    "title": "Listing Only `.txt` Files in the Current Folder",
                    "code": (
                        "import os\n\n"
                        "folder = os.getcwd()\n"
                        "for name in os.listdir(folder):\n"
                        "    full_path = os.path.join(folder, name)\n"
                        "    if os.path.isfile(full_path) and name.endswith('.txt'):\n"
                        "        print('Found text file:', name)"
                    ),
                    "line_by_line": [
                        "Line 3: Gets the current working directory.",
                        "Line 4: Loops through every entry name in that folder.",
                        "Line 5: Builds the full path so `isfile` works anywhere.",
                        "Line 6: Prints only real `.txt` files (ignoring directories).",
                    ],
                },
                "body_markdown": (
                    "### Walking Subfolders Automatically (`os.walk`)\n"
                    "`os.listdir()` looks **one level deep**. When you want every file inside nested subfolders too, `for root, dirs, files in os.walk(folder):` visits every subfolder automatically!"
                ),
                "code_example": {
                    "title": "Counting Files by Extension in a Folder",
                    "code": (
                        "import os\n\n"
                        "def count_by_extension(folder: str) -> dict[str, int]:\n"
                        "    counts: dict[str, int] = {}\n"
                        "    for name in os.listdir(folder):\n"
                        "        full = os.path.join(folder, name)\n"
                        "        if not os.path.isfile(full):\n"
                        "            continue\n"
                        "        _, ext = os.path.splitext(name)\n"
                        "        ext = ext.lower() or '(no ext)'\n"
                        "        counts[ext] = counts.get(ext, 0) + 1\n"
                        "    return counts\n\n"
                        "print(count_by_extension(os.getcwd()))\n"
                    ),
                },
                "common_mistakes": [
                    "Calling `os.path.isfile(name)` without `os.path.join(folder, name)` when scanning another folder (fails because Python checks the current folder instead!).",
                ],
                "key_takeaway": "Always combine `os.listdir(folder)` names with `os.path.join(folder, name)` before checking `isfile` or opening them.",
            },
            {
                "id": "ch03-s2",
                "title": "3.2 Simple File Automations (`os.makedirs`, `os.rename`, `os.getenv`)",
                "zero_assumption_note": "With just 3 `os` functions, you can build real desktop automations that sort messy folders in half a second.",
                "definition": (
                    "`os.makedirs` creates folders, `os.rename` moves or renames files, and `os.getenv` reads secret environment settings without hardcoding passwords."
                ),
                "syntax_box": {
                    "title": "Creating Folders, Moving Files & Reading Env Vars",
                    "syntax": (
                        "import os\n\n"
                        "os.makedirs('sorted/images', exist_ok=True)    # creates folder safely\n"
                        "os.rename('messy/pic.png', 'sorted/images/pic.png')  # moves or renames\n"
                        "api_key = os.getenv('OPENAI_API_KEY', 'missing')     # safe env lookup"
                    ),
                    "breakdown": [
                        "`exist_ok=True` prevents crashing if `'sorted/images'` already exists.",
                        "`os.rename(old_path, new_path)` moves a file to another folder on the same drive—or renames it!",
                        "`os.getenv('NAME', default)` reads an environment variable safely without raising `KeyError`.",
                    ],
                },
                "tiny_example": {
                    "title": "Safely Moving a File Into a New Folder",
                    "code": (
                        "import os, tempfile\n\n"
                        "with tempfile.TemporaryDirectory() as tmp:\n"
                        "    src = os.path.join(tmp, 'report.txt')\n"
                        "    open(src, 'w', encoding='utf-8').write('hello')\n\n"
                        "    dest_dir = os.path.join(tmp, 'archive')\n"
                        "    os.makedirs(dest_dir, exist_ok=True)\n"
                        "    dest = os.path.join(dest_dir, 'report.txt')\n"
                        "    os.rename(src, dest)\n"
                        "    print('Moved exists?', os.path.exists(dest))"
                    ),
                    "line_by_line": [
                        "Creates a safe temporary sandbox folder `tmp` (auto-deleted afterwards).",
                        "Creates `report.txt`, makes `archive/` folder, and moves the file inside with `os.rename`.",
                        "Prints `Moved exists? True`.",
                    ],
                },
                "body_markdown": (
                    "### Why `os.getenv()` Matters for AI Engineers\n"
                    "Never write `api_key = 'sk-proj-1234...'` directly in your Python file—if you `git push` it to GitHub, bots steal it in seconds! Store secrets in environment variables and read them with `os.getenv()`."
                ),
                "code_example": {
                    "title": "Mini Automation: Sort Files Into Extension Folders",
                    "code": (
                        "import os, tempfile\n\n"
                        "def organize_folder(folder: str) -> dict[str, int]:\n"
                        "    moved: dict[str, int] = {}\n"
                        "    for name in os.listdir(folder):\n"
                        "        src = os.path.join(folder, name)\n"
                        "        if not os.path.isfile(src):\n"
                        "            continue\n"
                        "        _, ext = os.path.splitext(name)\n"
                        "        bucket = ext.lstrip('.').lower() or 'other'\n"
                        "        target_dir = os.path.join(folder, bucket)\n"
                        "        os.makedirs(target_dir, exist_ok=True)\n"
                        "        os.rename(src, os.path.join(target_dir, name))\n"
                        "        moved[bucket] = moved.get(bucket, 0) + 1\n"
                        "    return moved\n\n"
                        "with tempfile.TemporaryDirectory() as d:\n"
                        "    for fn in ['a.txt', 'b.txt', 'pic.png']:\n"
                        "        open(os.path.join(d, fn), 'w').close()\n"
                        "    print('Organized:', organize_folder(d))\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting `exist_ok=True` in `os.makedirs(...)` -> crashes the second time you run your automation!",
                    "Calling `os.rename(src, dest)` when `dest`'s folder doesn't exist yet -> always call `os.makedirs` first.",
                ],
                "key_takeaway": "Combine `os.listdir`, `os.path.splitext`, `os.makedirs(..., exist_ok=True)`, and `os.rename` to automate file organization cleanly.",
            },
        ],
        "quizzes": [
            {
                "id": "ch03-q1",
                "question": "Why should you pass `exist_ok=True` to `os.makedirs('sorted/docs', exist_ok=True)`?",
                "options": [
                    "It deletes old files inside the folder",
                    "So your script doesn't crash with `FileExistsError` if the folder already exists",
                    "It converts paths to JSON",
                    "It makes files read-only",
                ],
                "correct_index": 1,
                "explanation": "Without `exist_ok=True`, running an automation script a second time crashes when the folder already exists.",
            },
        ],
        "project": {
            "title": "Automated Folder Organizer & Log Archiver (`os` Automation)",
            "workspace_dir": "projects/ch03_os_file_automator",
            "overview": "Use `os` (`listdir`, `path`, `makedirs`, `rename`, `walk`) to sort messy files into category folders and write a summary report.",
            "architecture_steps": [
                "Scan a target folder safely skipping subdirectories.",
                "Map extensions (`.png`/`.jpg` -> `images`, `.txt`/`.md` -> `docs`, else `other`).",
                "Create category folders with `os.makedirs(..., exist_ok=True)` and move files with `os.rename`.",
            ],
            "milestones": [
                {"id": "ch03-m1", "label": "Scan folder & count files by extension using os.path"},
                {"id": "ch03-m2", "label": "Create destination folders & move files cleanly"},
                {"id": "ch03-m3", "label": "Write automation report & pass pytest"},
            ],
        },
    },

    # =========================================================================
    # CHAPTER 4: Object-Oriented Programming (OOP) From Ground Zero
    # =========================================================================
    {
        "id": "ch04",
        "number": 4,
        "phase": 1,
        "phase_title": "Phase 1: Python From Zero — Basics, Files, `os`, OOP & Logic",
        "title": "Object-Oriented Programming (OOP) From Ground Zero",
        "subtitle": "Why classes exist, __init__ & self, protecting state with methods, __repr__ & @dataclass, composition, and splitting files.",
        "status_type": "available",
        "estimated_hours": 6,
        "why_it_matters": (
            "Pydantic models, PyTorch `nn.Module`, FastAPI dependencies, and LangChain Runnables are all built with OOP classes. "
            "Learning classes slowly from first principles makes every library in Phase 2–4 feel natural."
        ),
        "just_in_time_tags": ["Why Classes?", "__init__ & self", "Methods", "__repr__ & @dataclass", "Composition", "Modules & pytest"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch04-s1",
                "title": "4.1 Why Do Classes Exist? (Solving the Loose-Variables Mess)",
                "zero_assumption_note": "Forget textbook jargon like 'polymorphism' for now. Start with the exact everyday problem a `class` solves.",
                "definition": (
                    "A **class** is a blueprint that bundles an item's **data (attributes)** and its **actions (methods)** together into one neat **object**."
                ),
                "syntax_box": {
                    "title": "Before OOP (Messy) vs With a Class (Clean)",
                    "syntax": (
                        "# WITHOUT OOP (messy as soon as you have 5 accounts!):\n"
                        "acc1_owner = 'Sara'\n"
                        "acc1_balance = 100\n\n"
                        "# WITH OOP (1 blueprint -> create as many objects as you want):\n"
                        "class BankAccount:\n"
                        "    def __init__(self, owner: str, balance: int = 0) -> None:\n"
                        "        self.owner = owner\n"
                        "        self.balance = balance"
                    ),
                    "breakdown": [
                        "Think of `class` as a cookie cutter, and `BankAccount('Sara', 100)` as an actual cookie made from it.",
                        "Unlike plain dictionaries, a class locks in exact field names and attaches safe actions.",
                    ],
                },
                "tiny_example": {
                    "title": "Creating Two Independent Objects from One Class",
                    "code": (
                        "class Player:\n"
                        "    def __init__(self, name: str) -> None:\n"
                        "        self.name = name\n"
                        "        self.hp = 100\n\n"
                        "p1 = Player('Knight')\n"
                        "p2 = Player('Mage')\n"
                        "p1.hp = 80\n"
                        "print(p1.name, p1.hp, '|', p2.name, p2.hp)"
                    ),
                    "line_by_line": [
                        "`p1 = Player('Knight')` creates the first object (`p1.hp = 100`).",
                        "`p2 = Player('Mage')` creates a separate second object (`p2.hp` stays `100`!).",
                        "Changing `p1.hp = 80` leaves `p2.hp` untouched.",
                    ],
                },
                "body_markdown": (
                    "### Key Vocabulary\n"
                    "- **Class:** The blueprint (`Player`).\n"
                    "- **Object / Instance:** One item built from that blueprint (`p1`, `p2`).\n"
                    "- **Attribute:** A variable stored on an object (`p1.hp`)."
                ),
                "code_example": {
                    "title": "Modeling a Book Object",
                    "code": (
                        "class Book:\n"
                        "    def __init__(self, title: str, pages: int) -> None:\n"
                        "        self.title = title\n"
                        "        self.pages = pages\n\n"
                        "b1 = Book('Python Basics', 180)\n"
                        "print(f'{b1.title} has {b1.pages} pages')\n"
                    ),
                },
                "common_mistakes": [
                    "Thinking `class` runs immediately—just like `def`, `class` defines the blueprint until you call `Book(...)`.",
                ],
                "key_takeaway": "A class is a blueprint for creating independent objects that each hold their own attributes.",
            },
            {
                "id": "ch04-s2",
                "title": "4.2 Inside `__init__` & What `self` Actually Means",
                "zero_assumption_note": "`self` looks strange only because other languages hide it. In Python, it is completely transparent once you see how Python passes it.",
                "definition": (
                    "- **`__init__`:** The setup function that runs automatically when you create an object.\n"
                    "- **`self`:** Literally means **'this specific object calling the method right now'**."
                ),
                "syntax_box": {
                    "title": "How `self` Connects Attributes and Methods",
                    "syntax": (
                        "class Counter:\n"
                        "    def __init__(self) -> None:\n"
                        "        self.value = 0          # saved on THIS object\n\n"
                        "    def increment(self) -> None:\n"
                        "        self.value += 1         # updates THIS object's value\n\n"
                        "c = Counter()\n"
                        "c.increment()                   # Python runs Counter.increment(c)"
                    ),
                    "breakdown": [
                        "When you call `c.increment()`, Python automatically passes `c` as `self`!",
                        "Writing `self.value = 0` saves `value` on the object; writing `value = 0` (no `self.`) disappears when `__init__` ends.",
                    ],
                },
                "tiny_example": {
                    "title": "Watching `self` Keep Two Trackers Separate",
                    "code": (
                        "class StepTracker:\n"
                        "    def __init__(self, owner: str) -> None:\n"
                        "        self.owner = owner\n"
                        "        self.steps = 0\n\n"
                        "    def walk(self, n: int) -> None:\n"
                        "        self.steps += n\n\n"
                        "a = StepTracker('Sara')\n"
                        "b = StepTracker('Alex')\n"
                        "a.walk(500)\n"
                        "b.walk(1200)\n"
                        "print(a.owner, a.steps, '|', b.owner, b.steps)"
                    ),
                    "line_by_line": [
                        "`a.walk(500)` runs with `self = a` -> `a.steps` becomes `500`.",
                        "`b.walk(1200)` runs with `self = b` -> `b.steps` becomes `1200`.",
                    ],
                },
                "body_markdown": (
                    "### Protecting Object State With Validation\n"
                    "Putting updates inside methods like `deposit(amount)` lets you reject bad inputs (`if amount <= 0: raise ValueError(...)`) in one place."
                ),
                "code_example": {
                    "title": "BankAccount With Validation Methods",
                    "code": (
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
                        "acc = BankAccount('Sara', 100.0)\n"
                        "acc.deposit(50.0)\n"
                        "print('Balance:', acc.balance)\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting `self` in `def walk(n):` -> `TypeError`.",
                    "Forgetting `self.` when saving attributes in `__init__`.",
                ],
                "key_takeaway": "`self` is just the object calling the method, and methods let you validate and update state cleanly.",
            },
            {
                "id": "ch04-s3",
                "title": "4.3 `@dataclass`, `__len__`, `__call__`, Composition & Modules",
                "zero_assumption_note": "Double-underscore ('dunder') methods simply teach your custom class how to work with `print()`, `len()`, and `()`.",
                "definition": (
                    "- **`@dataclass`:** Auto-writes `__init__`, readable `print()` (`__repr__`), and `==` for data classes.\n"
                    "- **Composition:** Putting one object inside another (`Playlist` holding `Song` objects)."
                ),
                "syntax_box": {
                    "title": "@dataclass, __len__ & __call__",
                    "syntax": (
                        "from dataclasses import dataclass\n\n"
                        "@dataclass\n"
                        "class Song:\n"
                        "    title: str\n"
                        "    seconds: int\n\n"
                        "class TextCleaner:\n"
                        "    def __call__(self, text: str) -> str:\n"
                        "        return ' '.join(text.split()).lower()"
                    ),
                    "breakdown": [
                        "`@dataclass` eliminates `__init__` boilerplate for data objects.",
                        "`__len__(self)` enables `len(playlist)`.",
                        "`__call__(self, x)` lets a configured object be invoked like `cleaner('  Hi  ')`.",
                    ],
                },
                "tiny_example": {
                    "title": "Playlist Composing Song Objects",
                    "code": (
                        "from dataclasses import dataclass\n\n"
                        "@dataclass\n"
                        "class Song:\n"
                        "    title: str\n"
                        "    seconds: int\n\n"
                        "class Playlist:\n"
                        "    def __init__(self) -> None:\n"
                        "        self.songs: list[Song] = []\n"
                        "    def add(self, song: Song) -> None:\n"
                        "        self.songs.append(song)\n"
                        "    def total_seconds(self) -> int:\n"
                        "        return sum(s.seconds for s in self.songs)\n\n"
                        "pl = Playlist()\n"
                        "pl.add(Song('Intro', 90))\n"
                        "pl.add(Song('Main', 210))\n"
                        "print('Total:', pl.total_seconds())"
                    ),
                    "line_by_line": [
                        "`Song` holds data for one track cleanly.",
                        "`Playlist` holds a list of `Song` objects and sums `s.seconds` -> `300`.",
                    ],
                },
                "body_markdown": (
                    "### Splitting Files & Writing `pytest` Tests\n"
                    "Put `@dataclass` models in `models.py`, OOP logic in `analyzer.py` (no file I/O inside!), file reading in `cli.py`, and `def test_...(): assert ...` in `test_analyzer.py`."
                ),
                "code_example": {
                    "title": "Unit Testing an OOP Class",
                    "code": (
                        "def test_playlist_total() -> None:\n"
                        "    pl = Playlist()\n"
                        "    pl.add(Song('A', 60))\n"
                        "    assert pl.total_seconds() == 60\n"
                    ),
                },
                "common_mistakes": [
                    "Putting file reading inside OOP logic classes, making unit tests hard.",
                ],
                "key_takeaway": "Use `@dataclass` for data, composition for cooperating objects, and keep I/O out of core classes so `pytest` is effortless.",
            },
        ],
        "quizzes": [
            {
                "id": "ch04-q1",
                "question": "Inside `__init__`, why must you write `self.hp = 100` instead of `hp = 100`?",
                "options": [
                    "`hp = 100` vanishes when `__init__` ends; `self.hp = 100` stores it on that object",
                    "Python forbids variables without `self.`",
                    "`self.hp` makes it global",
                    "`hp = 100` makes it read-only",
                ],
                "correct_index": 0,
                "explanation": "Attaching attributes to `self` saves them on the object instance.",
            },
        ],
        "project": {
            "title": "Modular OOP Log Analyzer Package",
            "workspace_dir": "projects/ch04_log_analyzer",
            "overview": "Refactor `legacy_monolith.py` into clean `models.py`, `analyzer.py`, `cli.py`, and `pytest` tests.",
            "architecture_steps": [
                "Inspect `legacy_monolith.py` to separate file reading from counting.",
                "Create `LogEntry` and `LogReport` dataclasses in `models.py`.",
                "Build `LogAnalyzer` in `analyzer.py` and pass `pytest`.",
            ],
            "milestones": [
                {"id": "ch04-m1", "label": "Separate models.py dataclasses from file I/O"},
                {"id": "ch04-m2", "label": "Build LogAnalyzer class with clean state & methods"},
                {"id": "ch04-m3", "label": "Wire cli.py & pass pytest"},
            ],
        },
    },
]
