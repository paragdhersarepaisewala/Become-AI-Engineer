"""Phase 1 Part A (Chapters 1-3): Python Core & Comprehensions, Files & Stdlib, OOP From Scratch."""

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
        "phase_title": "Phase 1: Python From Zero — Basics, Files, OOP & Logic",
        "title": "Python Core Building Blocks (From Scratch)",
        "subtitle": "Variables, types, if/else decisions, for & while loops, lists/dicts/sets, one-line loops (comprehensions), and functions.",
        "status_type": "available",
        "estimated_hours": 6,
        "why_it_matters": (
            "Nothing in AI works without fluent Python basics. Every dataset loader, API server, and neural network training loop "
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
                        "# Guard against dividing by zero before computing average\n"
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
                    "Inside a loop over lines or numbers, `if not item: continue` skips empty entries immediately so your main logic stays clean and readable."
                ),
                "code_example": {
                    "title": "Skipping Negative Numbers While Summing",
                    "code": (
                        "readings = [12, -5, 8, -1, 10]\n"
                        "valid_sum = 0\n\n"
                        "for val in readings:\n"
                        "    if val < 0:\n"
                        "        continue  # skip sensor errors and jump to next val\n"
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
                    "title": "Safe List Copy & Dictionary Counting",
                    "code": (
                        "# Block 1: Independent copy so original list stays safe\n"
                        "skills = ['python', 'sql']\n"
                        "resume_skills = skills.copy()\n"
                        "resume_skills.append('pytorch')\n"
                        "print('Base:', skills)           # ['python', 'sql']\n"
                        "print('Resume:', resume_skills)  # ['python', 'sql', 'pytorch']\n\n"
                        "# Block 2: Deduplicate tags\n"
                        "tags = ['ai', 'py', 'ai', 'ml']\n"
                        "unique_tags = sorted(set(tags))\n"
                        "print('Unique:', unique_tags)    # ['ai', 'ml', 'py']\n"
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
                "zero_assumption_note": "You may have seen weird one-line Python like `[x * 2 for x in nums if x > 0]`. It is NOT new magic—it is just a normal 4-line `for` loop folded onto one line!",
                "definition": (
                    "A **list comprehension** builds a new list by transforming and optionally filtering items from an existing collection on one line."
                ),
                "syntax_box": {
                    "title": "Comparing Normal `for` Loop vs One-Line Comprehension",
                    "syntax": (
                        "# 4-line normal loop:\n"
                        "result = []\n"
                        "for x in items:\n"
                        "    if condition(x):\n"
                        "        result.append(transform(x))\n\n"
                        "# Exact same thing as a 1-line list comprehension:\n"
                        "result = [transform(x) for x in items if condition(x)]"
                    ),
                    "breakdown": [
                        "**Read it in 3 parts:** `[ WHAT_TO_KEEP   for ITEM in COLLECTION   if FILTER_CONDITION ]`.",
                        "Part 1 (`transform(x)`): what goes into the new list (same as what was inside `result.append(...)`).",
                        "Part 2 (`for x in items`): the loop header.",
                        "Part 3 (`if condition(x)`): optional filter—only items passing this `if` enter the new list!",
                    ],
                },
                "tiny_example": {
                    "title": "Step-by-Step: Doubling Only Even Numbers",
                    "code": (
                        "nums = [1, 2, 3, 4, 5]\n"
                        "evens_doubled = [n * 2 for n in nums if n % 2 == 0]\n"
                        "print(evens_doubled)"
                    ),
                    "line_by_line": [
                        "`n = 1`: `1 % 2 == 0` is False -> skipped.",
                        "`n = 2`: True -> adds `2 * 2 = 4`.",
                        "`n = 3`: False -> skipped.",
                        "`n = 4`: True -> adds `4 * 2 = 8`.",
                        "`n = 5`: False -> skipped -> prints `[4, 8]`!",
                    ],
                },
                "body_markdown": (
                    "### One Bonus Variation: `sum(...)` Without Brackets\n"
                    "You can also drop the `[]` inside `sum(...)` to count matching items cleanly:\n"
                    "- `passing = sum(1 for s in scores if s >= 60)` — adds `1` for every score `>= 60`!\n"
                    "- **Rule of thumb:** Only use a one-line comprehension when it is short and easy to read. If you need 2+ conditions or complex steps, write a normal `for` loop!"
                ),
                "code_example": {
                    "title": "Cleaning Messy Usernames & Counting Passing Scores",
                    "code": (
                        "# Block 1: Strip spaces, lowercase, and skip empty strings\n"
                        "raw_names = ['  Sara ', '', '  ALEX', '   ']\n"
                        "clean_names = [name.strip().lower() for name in raw_names if name.strip()]\n"
                        "print(clean_names)  # ['sara', 'alex']\n\n"
                        "# Block 2: Count scores >= 60 using a generator inside sum()\n"
                        "scores = [45, 80, 62, 50]\n"
                        "pass_count = sum(1 for s in scores if s >= 60)\n"
                        "print('Passed:', pass_count)  # 2\n"
                    ),
                },
                "common_mistakes": [
                    "Trying to cram complicated `if/elif/else` or nested loops into one unreadable line (use a normal `for` loop instead!).",
                    "Forgetting where `if` goes when filtering (`[x for x in nums if x > 0]`: filter `if` goes at the END; an `if/else` value choice like `['yes' if x > 0 else 'no' for x in nums]` goes at the FRONT).",
                ],
                "key_takeaway": "A list comprehension `[expr for x in items if cond]` is just shorthand for `out = []; for x in items: if cond: out.append(expr)`.",
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
                        "    print(x * 2)      # only prints on screen; returns None!\n\n"
                        "def working_double(x):\n"
                        "    return x * 2      # hands 10 back to the variable\n\n"
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
                    "### One Hidden Trap: Default `= []`\n"
                    "Never put `items=[]` in a `def` line—Python creates that default list once and shares it across every future call! "
                    "Always default to `items=None` and write `if items is None: items = []` inside."
                ),
                "code_example": {
                    "title": "Safe Optional List Parameter (`None` Sentinel)",
                    "code": (
                        "def add_tag(tag: str, existing: list[str] | None = None) -> list[str]:\n"
                        "    # Block 1: Always make a fresh list or copy caller's list\n"
                        "    result = [] if existing is None else existing.copy()\n"
                        "    # Block 2: Add tag only if not already present\n"
                        "    if tag not in result:\n"
                        "        result.append(tag)\n"
                        "    return result\n\n"
                        "print(add_tag('python'))  # ['python']\n"
                        "print(add_tag('ai'))      # ['ai'] (independent list!)\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting `return` inside a function and wondering why the caller gets `None`.",
                    "Using `items=[]` as a default argument instead of `items=None`.",
                ],
                "key_takeaway": "Functions should `return` values (not just `print`), and optional lists/dicts should always default to `None`.",
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
            {
                "id": "ch01-q3",
                "question": "Why should you write `tags: list[str] | None = None` instead of `tags: list[str] = []`?",
                "options": [
                    "Python forbids `[]` in function signatures",
                    "A default `[]` is created once and reused across every call, leaking items between calls",
                    "`None` runs faster on GPU",
                    "It converts the list into a tuple",
                ],
                "correct_index": 1,
                "explanation": "Mutable defaults (`[]`, `{}`) persist across calls; `None` lets you create a brand-new list inside the function each time.",
            },
        ],
        "project": {
            "title": "Student Grade & Tag Analyzer Script",
            "workspace_dir": "projects/ch01_grade_analyzer",
            "overview": "Use variables, loops, comprehensions, dictionaries, and clean functions (with `return`, no files yet!) to summarize student scores and tags.",
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
    # CHAPTER 2: Working With Files & Small Standard Libraries
    # =========================================================================
    {
        "id": "ch02",
        "number": 2,
        "phase": 1,
        "phase_title": "Phase 1: Python From Zero — Basics, Files, OOP & Logic",
        "title": "Working With Files & Everyday Built-In Libraries",
        "subtitle": "Reading & writing .txt files, pathlib.Path, try/except error handling, JSON/JSONL, CSV spreadsheets, and small stdlib helpers.",
        "status_type": "available",
        "estimated_hours": 5,
        "why_it_matters": (
            "Real programs don't hardcode data inside `.py` files—they load text documents, JSON configs, and CSV spreadsheets from disk "
            "without crashing when a file is missing or malformed."
        ),
        "just_in_time_tags": ["open() & with", "pathlib.Path", "try / except", "json & jsonl", "csv.DictReader", "Counter & os"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch02-s1",
                "title": "2.1 Reading & Writing Plain `.txt` Files (`open` & `with`)",
                "zero_assumption_note": "Start with plain `.txt` files first. Once 3 lines of `.txt` feel effortless, JSON and CSV are easy.",
                "definition": (
                    "Opening a file connects your Python script to a file on your hard drive so you can read its contents or write new text into it."
                ),
                "syntax_box": {
                    "title": "The Safe `with open(...)` Pattern",
                    "syntax": (
                        "# Writing text to a file ('w' creates or overwrites):\n"
                        "with open('notes.txt', 'w', encoding='utf-8') as f:\n"
                        "    f.write('Hello Python\\n')\n\n"
                        "# Reading text back ('r' reads):\n"
                        "with open('notes.txt', 'r', encoding='utf-8') as f:\n"
                        "    for line in f:\n"
                        "        print(line.strip())"
                    ),
                    "breakdown": [
                        "`'w'` = **write** (creates file or erases old content!). `'a'` = **append** (adds to end). `'r'` = **read**.",
                        "`with ... as f:` **automatically closes** the file when the indented block finishes—even if an error occurs.",
                        "`encoding='utf-8'` tells Python how to read/write emojis, accents, and quotes properly on Windows.",
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
                        "Lines 1–2: Creates `demo.txt` with 3 lines (middle line is blank `'\\n'`).",
                        "Line 6: Loops one line at a time.",
                        "Line 7: `'\\n'.strip()` becomes `''` (empty/False), so blank lines are skipped!",
                        "Line 9: Prints `Non-empty lines: 2`.",
                    ],
                },
                "body_markdown": (
                    "### Reading All at Once vs Line by Line\n"
                    "- `f.read()` loads the **entire file** as one big string (great for tiny config files).\n"
                    "- `for line in f:` reads **one line at a time** (essential for huge 2 GB AI training files so your RAM doesn't explode!)."
                ),
                "code_example": {
                    "title": "Appending a Log Entry Without Erasing Old Lines",
                    "code": (
                        "def append_log(filename: str, message: str) -> None:\n"
                        "    # 'a' appends to the end instead of overwriting like 'w'\n"
                        "    with open(filename, 'a', encoding='utf-8') as f:\n"
                        "        f.write(message + '\\n')\n"
                    ),
                },
                "common_mistakes": [
                    "Opening a file with `'w'` when you meant `'a'` (accidentally wipes the existing file!).",
                    "Forgetting `encoding='utf-8'` on Windows (crashes with `UnicodeDecodeError` on curly quotes or emojis).",
                ],
                "key_takeaway": "Always use `with open(..., encoding='utf-8') as f:`, loop `for line in f:` for large files, and call `.strip()` on lines.",
            },
            {
                "id": "ch02-s2",
                "title": "2.2 Clean File Paths (`pathlib.Path`) & Handling Errors (`try / except`)",
                "zero_assumption_note": "On Windows, `'C:\\new\\test.txt'` breaks because `\\n` means newline and `\\t` means tab! `pathlib.Path` eliminates path headaches forever.",
                "definition": (
                    "- **`pathlib.Path`:** A clean Python object representing a file or folder path that works identically on Windows, Mac, and Linux.\n"
                    "- **`try / except`:** Lets your code catch predictable errors (like a missing file) and respond cleanly instead of crashing."
                ),
                "syntax_box": {
                    "title": "Path Operations & Specific Error Handling",
                    "syntax": (
                        "from pathlib import Path\n\n"
                        "p = Path('data') / 'raw' / 'notes.txt'     # builds folder/raw/notes.txt\n"
                        "p.parent.mkdir(parents=True, exist_ok=True) # creates data/raw/ if missing\n\n"
                        "try:\n"
                        "    text = p.read_text(encoding='utf-8')\n"
                        "except FileNotFoundError:\n"
                        "    text = ''                              # fallback if file doesn't exist"
                    ),
                    "breakdown": [
                        "Use `/` between `Path` objects—Python automatically converts it to `\\` on Windows or `/` on Linux/Mac.",
                        "`p.exists()` returns `True` or `False`.",
                        "`p.parent.mkdir(parents=True, exist_ok=True)` safely creates missing folders without failing if they already exist.",
                        "Always catch a **specific** error (`except FileNotFoundError:` or `except ValueError:`), never bare `except:` (bare `except:` hides typos and real bugs!).",
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
                        "Line 5: Python jumps straight to `except FileNotFoundError:` instead of crashing.",
                        "Line 6–7: Prints a polite message and sets `content = ''` so the rest of the script keeps running.",
                    ],
                },
                "body_markdown": (
                    "### Finding All `.txt` Files in a Folder\n"
                    "`list(Path('docs').glob('*.txt'))` finds every text file inside `docs/` in one clean line!"
                ),
                "code_example": {
                    "title": "Writing Safely into Nested Output Folders",
                    "code": (
                        "from pathlib import Path\n\n"
                        "def save_report(out_path: Path, body: str) -> None:\n"
                        "    # Ensure parent folders exist before opening the file\n"
                        "    out_path.parent.mkdir(parents=True, exist_ok=True)\n"
                        "    out_path.write_text(body, encoding='utf-8')\n"
                    ),
                },
                "common_mistakes": [
                    "Trying to write `Path('new_folder/out.txt').write_text(...)` before creating `new_folder` -> `FileNotFoundError`.",
                    "Writing bare `except:` which silently swallows syntax/variable bugs.",
                ],
                "key_takeaway": "Use `Path('a') / 'b.txt'`, call `.parent.mkdir(parents=True, exist_ok=True)` before writing, and catch specific exceptions with `try/except`.",
            },
            {
                "id": "ch02-s3",
                "title": "2.3 Loading & Saving JSON, JSONL & CSV Files",
                "zero_assumption_note": "Never split CSV lines with `line.split(',')` or parse JSON by hand—Python already has `json` and `csv` built in!",
                "definition": (
                    "- **JSON (`.json`):** A text format that looks almost identical to Python `dict`s and `list`s—used everywhere in configs and web APIs.\n"
                    "- **JSONL (`.jsonl`):** 'JSON Lines'—one standalone JSON object per line (standard for LLM fine-tuning datasets!).\n"
                    "- **CSV (`.csv`):** Comma-separated spreadsheet table."
                ),
                "syntax_box": {
                    "title": "`json` and `csv.DictReader` Basics",
                    "syntax": (
                        "import csv, json\n"
                        "from pathlib import Path\n\n"
                        "# JSON: file <-> Python dict/list\n"
                        "data = json.loads('{\"name\": \"AI\"}')   # string -> dict\n"
                        "text = json.dumps({'name': 'AI'})       # dict -> string\n\n"
                        "# CSV: read each row as a dictionary by column header\n"
                        "with Path('data.csv').open('r', encoding='utf-8', newline='') as f:\n"
                        "    rows = list(csv.DictReader(f))"
                    ),
                    "breakdown": [
                        "`json.load(f)` / `json.dump(obj, f)` work directly on an open file `f`.",
                        "`json.loads(s)` / `json.dumps(obj)` ('s' = string) convert between a single string and Python data—perfect for reading `.jsonl` line by line!",
                        "`csv.DictReader(f)` uses row 1 as column keys, returning each data row as a `dict` like `{'id': '1', 'label': 'pos'}`.",
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
                        "`json.dumps(record)` turns the Python dict into a plain text string `'{\"user\": \"Sam\", \"score\": 95}'`.",
                        "`json.loads(as_text)` parses that string back into a real Python `dict` so `back_to_dict['score']` works!",
                    ],
                },
                "body_markdown": (
                    "### Handling Broken Lines in `.jsonl` Datasets\n"
                    "Real datasets sometimes have 1 corrupted line out of 10,000. Wrapping `json.loads(line)` inside `try / except json.JSONDecodeError:` skips only that broken line instead of crashing the whole job."
                ),
                "code_example": {
                    "title": "Resilient JSONL Loader",
                    "code": (
                        "import json\n"
                        "from pathlib import Path\n\n"
                        "def read_jsonl(path: Path) -> list[dict]:\n"
                        "    items: list[dict] = []\n"
                        "    with path.open('r', encoding='utf-8') as f:\n"
                        "        for raw in f:\n"
                        "            line = raw.strip()\n"
                        "            if not line:\n"
                        "                continue\n"
                        "            try:\n"
                        "                items.append(json.loads(line))\n"
                        "            except json.JSONDecodeError:\n"
                        "                continue  # skip malformed line safely\n"
                        "    return items\n"
                    ),
                },
                "common_mistakes": [
                    "Mixing up `json.load(f)` (takes a file object) with `json.loads(s)` (takes a string).",
                    "Forgetting `newline=''` when opening CSV files for `csv.DictReader` / `csv.writer`.",
                ],
                "key_takeaway": "Use `json.loads/dumps` for JSONL lines and `csv.DictReader` with `newline=''` for CSV tables.",
            },
            {
                "id": "ch02-s4",
                "title": "2.4 Small Built-In Tools (`Counter`, `defaultdict`, `os`, `__main__`)",
                "zero_assumption_note": "These tiny built-in modules save dozens of lines of repetitive code once you already know loops and dicts.",
                "definition": (
                    "Python ships with pre-installed helper modules (`collections`, `os`) so you don't have to reinvent counting, grouping, or reading environment settings."
                ),
                "syntax_box": {
                    "title": "Counter, defaultdict, os.getenv & `__main__`",
                    "syntax": (
                        "from collections import Counter, defaultdict\n"
                        "import os\n\n"
                        "counts = Counter(['ai', 'py', 'ai'])  # Counter({'ai': 2, 'py': 1})\n"
                        "groups = defaultdict(list)            # new keys auto-start as []\n"
                        "key = os.getenv('API_KEY', 'none')    # safe env var lookup\n\n"
                        "if __name__ == '__main__':\n"
                        "    # only runs when you run THIS file directly"
                    ),
                    "breakdown": [
                        "`Counter(items).most_common(2)` returns the top 2 `(item, count)` pairs immediately.",
                        "`defaultdict(list)` lets you write `groups[tag].append(val)` without `if tag not in groups: groups[tag] = []`.",
                        "`if __name__ == '__main__':` keeps helper files quiet if another script imports functions from them.",
                    ],
                },
                "tiny_example": {
                    "title": "Counting Words in 2 Lines with `Counter`",
                    "code": (
                        "from collections import Counter\n"
                        "words = 'learn python learn ai learn'.split()\n"
                        "c = Counter(words)\n"
                        "print(dict(c), '| Top 1:', c.most_common(1))"
                    ),
                    "line_by_line": [
                        "`.split()` breaks the sentence into `['learn', 'python', 'learn', 'ai', 'learn']`.",
                        "`Counter(words)` counts each word automatically.",
                        "`c.most_common(1)` returns `[('learn', 3)]`.",
                    ],
                },
                "body_markdown": (
                    "### Putting It All Together\n"
                    "Combining `Path` + `csv.DictReader` + `Counter` lets you inspect an entire dataset in under 15 readable lines!"
                ),
                "code_example": {
                    "title": "3-Block Script Reading & Summarizing Data",
                    "code": (
                        "from collections import Counter\n\n"
                        "def summarize_labels(rows: list[dict[str, str]]) -> dict[str, int]:\n"
                        "    labels = [r['label'].strip() for r in rows if r.get('label', '').strip()]\n"
                        "    return dict(Counter(labels))\n\n"
                        "if __name__ == '__main__':\n"
                        "    sample = [{'label': 'pos'}, {'label': 'neg'}, {'label': 'pos'}]\n"
                        "    print(summarize_labels(sample))  # {'pos': 2, 'neg': 1}\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting `dict(counts)` when an API or test expects a plain `dict` instead of a `Counter`.",
                ],
                "key_takeaway": "Use `Counter` for counting, `defaultdict(list)` for grouping, and `if __name__ == '__main__':` at the bottom of runnable scripts.",
            },
        ],
        "quizzes": [
            {
                "id": "ch02-q1",
                "question": "Which mode opens a file to **add** new lines at the end without deleting what's already inside?",
                "options": ["'r'", "'w'", "'a'", "'x'"],
                "correct_index": 2,
                "explanation": "`'w'` overwrites the entire file; `'a'` appends to the end.",
            },
            {
                "id": "ch02-q2",
                "question": "What is the difference between `json.load(f)` and `json.loads(line)`?",
                "options": [
                    "No difference",
                    "`json.load(f)` reads from an open file; `json.loads(line)` parses a string (`s` = string)",
                    "`json.loads` only works on CSV",
                    "`json.load` writes to disk",
                ],
                "correct_index": 1,
                "explanation": "`load` takes a file handle `f`; `loads` takes a JSON string (very useful when reading `.jsonl` line by line).",
            },
        ],
        "project": {
            "title": "Dataset Inspector & File Converter CLI",
            "workspace_dir": "projects/ch02_file_inspector",
            "overview": "Read a CSV file safely using `Path` and `csv.DictReader`, count labels with `Counter`, and export clean JSONL lines.",
            "architecture_steps": [
                "Check file existence with `Path`.",
                "Read CSV rows using `csv.DictReader` and `encoding='utf-8'`.",
                "Count categories with `Counter` and write clean JSONL output.",
            ],
            "milestones": [
                {"id": "ch02-m1", "label": "Read CSV safely with Path & encoding='utf-8'"},
                {"id": "ch02-m2", "label": "Count categories using Counter & skip empty rows"},
                {"id": "ch02-m3", "label": "Write JSONL output and pass pytest"},
            ],
        },
    },

    # =========================================================================
    # CHAPTER 3: Object-Oriented Programming (OOP) From Ground Zero
    # =========================================================================
    {
        "id": "ch03",
        "number": 3,
        "phase": 1,
        "phase_title": "Phase 1: Python From Zero — Basics, Files, OOP & Logic",
        "title": "Object-Oriented Programming (OOP) From Ground Zero",
        "subtitle": "Why classes exist, __init__ & self, protecting state with methods, __repr__ & @dataclass, objects working together (composition), and splitting files.",
        "status_type": "available",
        "estimated_hours": 6,
        "why_it_matters": (
            "If you skip OOP fundamentals, PyTorch (`nn.Module`), custom Datasets, and LangChain feel like magic. Once built slowly from "
            "first principles, classes feel completely natural."
        ),
        "just_in_time_tags": ["Why Classes?", "__init__ & self", "Methods & Validation", "__repr__ & @dataclass", "Composition", "Modules & pytest"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch03-s1",
                "title": "3.1 Why Do Classes Exist? (Solving the Loose-Variables Mess)",
                "zero_assumption_note": "Forget fancy textbook words like 'polymorphism' for now. Let's start with the real problem a `class` solves.",
                "definition": (
                    "A **class** is a custom blueprint (like a form template) that bundles an item's **data** and the **functions that use that data** together into one neat **object**."
                ),
                "syntax_box": {
                    "title": "Before OOP (Messy) vs With a Class (Clean)",
                    "syntax": (
                        "# WITHOUT OOP (messy as soon as you have 5 accounts!):\n"
                        "acc1_owner = 'Sara'\n"
                        "acc1_balance = 100\n"
                        "acc2_owner = 'Alex'\n"
                        "acc2_balance = 50\n\n"
                        "# WITH OOP (1 blueprint, create as many accounts as you want):\n"
                        "class BankAccount:\n"
                        "    def __init__(self, owner: str, balance: int = 0) -> None:\n"
                        "        self.owner = owner\n"
                        "        self.balance = balance"
                    ),
                    "breakdown": [
                        "Think of `class BankAccount:` as a cookie cutter, and `acc1 = BankAccount('Sara', 100)` as an actual cookie made from it.",
                        "Even dictionaries (`{'owner': 'Sara', 'balacne': 100}`) let typos slip through silently—a class locks in exact attribute names and attaches safe actions!",
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
                        "`class Player:` defines the blueprint (`name` and starting `hp = 100`).",
                        "`p1 = Player('Knight')` creates the first object (`p1.name='Knight'`, `p1.hp=100`).",
                        "`p2 = Player('Mage')` creates a completely separate second object (`p2.hp` is still `100`!).",
                        "Changing `p1.hp = 80` leaves `p2.hp` untouched!",
                    ],
                },
                "body_markdown": (
                    "### Key Vocabulary (In Plain English)\n"
                    "- **Class:** The blueprint (`Player`).\n"
                    "- **Instance / Object:** One real item built from that blueprint (`p1`, `p2`).\n"
                    "- **Attribute:** A variable living inside an object (`p1.hp`)."
                ),
                "code_example": {
                    "title": "Modeling a Book Object",
                    "code": (
                        "class Book:\n"
                        "    def __init__(self, title: str, pages: int) -> None:\n"
                        "        self.title = title\n"
                        "        self.pages = pages\n\n"
                        "b1 = Book('Python Basics', 180)\n"
                        "b2 = Book('AI Systems', 320)\n"
                        "print(f'{b1.title} has {b1.pages} pages')\n"
                    ),
                },
                "common_mistakes": [
                    "Thinking `class` runs immediately—just like `def`, `class` only defines the blueprint until you create an object like `Book(...)`.",
                ],
                "key_takeaway": "A class is a blueprint for creating independent objects that each hold their own attributes.",
            },
            {
                "id": "ch03-s2",
                "title": "3.2 Inside `__init__` & What `self` Actually Means",
                "zero_assumption_note": "`self` looks strange only because other languages hide it. In Python, it is completely transparent once you see how Python passes it.",
                "definition": (
                    "- **`__init__`:** The setup function that runs automatically the instant you create an object (`Player('Knight')`).\n"
                    "- **`self`:** Simply means **'this specific object calling the method right now'**."
                ),
                "syntax_box": {
                    "title": "How `self` Connects Attributes and Methods",
                    "syntax": (
                        "class Counter:\n"
                        "    def __init__(self) -> None:\n"
                        "        self.value = 0          # attach `value` to THIS object\n\n"
                        "    def increment(self) -> None:\n"
                        "        self.value += 1         # update THIS object's `value`\n\n"
                        "c = Counter()\n"
                        "c.increment()                   # Python runs Counter.increment(c)!"
                    ),
                    "breakdown": [
                        "When you call `c.increment()`, Python secretly translates it to `Counter.increment(c)`—passing `c` as `self`!",
                        "That's why **every normal method inside a class takes `self` as its first parameter**.",
                        "Inside `__init__`, writing `self.value = 0` saves `0` on the object forever. Writing `value = 0` (without `self.`) creates a temporary variable that disappears as soon as `__init__` finishes!",
                    ],
                },
                "tiny_example": {
                    "title": "Watching `self` Keep Two Counters Separate",
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
                        "`a.walk(500)` runs `walk` with `self = a` -> `a.steps` becomes `500`.",
                        "`b.walk(1200)` runs `walk` with `self = b` -> `b.steps` becomes `1200`.",
                        "Prints `Sara 500 | Alex 1200`.",
                    ],
                },
                "body_markdown": (
                    "### Protecting Object State With Validation\n"
                    "Because updates go through a method (like `deposit(amount)` or `walk(n)`), you can guard against bad data in **one place** (`if amount <= 0: raise ValueError(...)`) instead of scattering checks across 10 files."
                ),
                "code_example": {
                    "title": "Safe BankAccount Methods With Guard Checks",
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
                        "print('Withdraw 200 ok?', acc.withdraw(200.0), '| Balance:', acc.balance)\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting `self` in `def walk(n):` -> crashes with `TypeError: walk() takes 1 positional argument but 2 were given`.",
                    "Forgetting `self.` when setting attributes inside `__init__` (`steps = 0` instead of `self.steps = 0`).",
                ],
                "key_takeaway": "`self` is just the object calling the method, and methods let you validate and update an object's state safely.",
            },
            {
                "id": "ch03-s3",
                "title": "3.3 Making Classes Clean: `__repr__`, `@dataclass`, `__len__` & `__call__`",
                "zero_assumption_note": "If you ever tried `print(my_object)` and saw `<Book object at 0x000001A2F>`, this fixes that!",
                "definition": (
                    "**Dunder ('double-underscore') methods** teach your custom class how to work with standard Python built-ins like `print()`, `len()`, `in`, and `()`."
                ),
                "syntax_box": {
                    "title": "The 4 Most Useful Shortcuts & Dunders",
                    "syntax": (
                        "from dataclasses import dataclass\n\n"
                        "@dataclass\n"
                        "class Song:\n"
                        "    title: str\n"
                        "    seconds: int\n\n"
                        "# @dataclass auto-creates __init__, readable print() (__repr__), and == !"
                    ),
                    "breakdown": [
                        "`__repr__(self) -> str`: controls what `print(obj)` displays.",
                        "`@dataclass`: decorator that writes `__init__`, `__repr__`, and `==` automatically for data-holding classes!",
                        "`__len__(self) -> int`: lets callers write `len(my_playlist)`.",
                        "`__call__(self, x)`: lets an object holding settings in `self` be called like a function: `cleaner('  hi  ')`.",
                    ],
                },
                "tiny_example": {
                    "title": "Using `@dataclass` vs Plain Class",
                    "code": (
                        "from dataclasses import dataclass\n\n"
                        "@dataclass\n"
                        "class Song:\n"
                        "    title: str\n"
                        "    seconds: int\n\n"
                        "s1 = Song('Focus Beat', 180)\n"
                        "s2 = Song('Focus Beat', 180)\n"
                        "print(s1)          # Song(title='Focus Beat', seconds=180)\n"
                        "print(s1 == s2)    # True!"
                    ),
                    "line_by_line": [
                        "Without `@dataclass`, `print(s1)` prints an ugly memory address and `s1 == s2` is `False`!",
                        "With `@dataclass`, Python prints all fields cleanly and compares values with `==`.",
                    ],
                },
                "body_markdown": (
                    "### Why `__call__` Matters Later in AI\n"
                    "When you build neural layers in PyTorch (`layer(x)`) or text steps in LangChain (`chain(prompt)`), they store configuration/weights in `self` and run via `__call__`."
                ),
                "code_example": {
                    "title": "A Small Callable Normalizer (`__call__`)",
                    "code": (
                        "class TextCleaner:\n"
                        "    def __init__(self, lowercase: bool = True) -> None:\n"
                        "        self.lowercase = lowercase\n\n"
                        "    def __call__(self, text: str) -> str:\n"
                        "        cleaned = ' '.join(text.split())\n"
                        "        return cleaned.lower() if self.lowercase else cleaned\n\n"
                        "clean = TextCleaner(lowercase=True)\n"
                        "print(clean('  Hello   AI  '))  # 'hello ai'\n"
                    ),
                },
                "common_mistakes": [
                    "Expecting `==` to compare fields on a normal class without `@dataclass` or `__eq__` (Python compares memory addresses by default!).",
                ],
                "key_takeaway": "Use `@dataclass` for clean data objects, `__len__` for collections, and `__call__` when an object acts like a configured function.",
            },
            {
                "id": "ch03-s4",
                "title": "3.4 Objects Working Together (Composition) & Splitting Files",
                "zero_assumption_note": "Real apps aren't 1 class—they are 2 or 3 small classes cooperating, organized across clean `.py` files.",
                "definition": (
                    "- **Composition ('has-a'):** Putting one object inside another object (for example, a `Playlist` *has* a list of `Song` objects).\n"
                    "- **Modular Files:** Putting data models in `models.py`, logic classes in `player.py`, and tests in `test_player.py`."
                ),
                "syntax_box": {
                    "title": "Composition + Importing Across Files",
                    "syntax": (
                        "class Playlist:\n"
                        "    def __init__(self, name: str) -> None:\n"
                        "        self.name = name\n"
                        "        self.songs: list[Song] = []  # Playlist HAS Song objects\n\n"
                        "    def add(self, song: Song) -> None:\n"
                        "        self.songs.append(song)\n\n"
                        "    def __len__(self) -> int:\n"
                        "        return len(self.songs)"
                    ),
                    "breakdown": [
                        "`Song` knows about one song (`title`, `seconds`). `Playlist` knows how to hold and summarize many `Song`s.",
                        "When splitting files, `from models import Song` lets `playlist.py` reuse `Song` without cramming everything into 1 huge script!",
                    ],
                },
                "tiny_example": {
                    "title": "Playlist Holding Song Objects",
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
                        "print('Total seconds:', pl.total_seconds())"
                    ),
                    "line_by_line": [
                        "Creates two `Song` objects and adds them to `pl`.",
                        "`sum(s.seconds for s in self.songs)` loops through every `Song` object inside `pl` and sums `.seconds` -> `300`.",
                    ],
                },
                "body_markdown": (
                    "### Verifying Classes Automatically With `pytest`\n"
                    "Put `def test_playlist_total():` in `test_playlist.py` using `assert pl.total_seconds() == 300`, then run `python -m pytest` to verify every method in milliseconds."
                ),
                "code_example": {
                    "title": "Testing Your Class With `assert` / `pytest`",
                    "code": (
                        "def test_playlist_counts() -> None:\n"
                        "    pl = Playlist()\n"
                        "    pl.add(Song('A', 60))\n"
                        "    pl.add(Song('B', 120))\n"
                        "    assert pl.total_seconds() == 180\n"
                    ),
                },
                "common_mistakes": [
                    "Giving one giant class 15 unrelated jobs (reading files, parsing text, and printing reports) instead of splitting small cooperating classes.",
                ],
                "key_takeaway": "Build small single-job classes that hold each other (composition), split them into clean `.py` modules, and test with `pytest`.",
            },
        ],
        "quizzes": [
            {
                "id": "ch03-q1",
                "question": "Inside `__init__`, why must you write `self.hp = 100` instead of `hp = 100`?",
                "options": [
                    "`hp = 100` creates a temporary local variable that disappears when `__init__` finishes; `self.hp` saves it on the object",
                    "Python forbids variable names without `self.`",
                    "`self.hp` makes it a global variable shared by all objects",
                    "`hp = 100` makes it read-only",
                ],
                "correct_index": 0,
                "explanation": "Attaching attributes to `self` stores them on that specific object instance.",
            },
            {
                "id": "ch03-q2",
                "question": "What does `@dataclass` give you automatically?",
                "options": [
                    "File saving to CSV",
                    "`__init__`, clean `print()` output (`__repr__`), and field-by-field `==` equality",
                    "Multithreading",
                    "Automatic database tables",
                ],
                "correct_index": 1,
                "explanation": "`@dataclass` removes boilerplate for classes whose main job is holding structured fields.",
            },
        ],
        "project": {
            "title": "Modular OOP Log Analyzer Package",
            "workspace_dir": "projects/ch03_log_analyzer",
            "overview": "Refactor `legacy_monolith.py` into clean `models.py` (`@dataclass`), `analyzer.py` (`class LogAnalyzer`), `cli.py`, and `pytest` tests.",
            "architecture_steps": [
                "Inspect `legacy_monolith.py` and separate file reading from counting.",
                "Create `LogEntry` and `LogReport` dataclasses in `models.py`.",
                "Build `LogAnalyzer` in `analyzer.py` and test with `pytest`.",
            ],
            "milestones": [
                {"id": "ch03-m1", "label": "Separate models.py dataclasses from file I/O"},
                {"id": "ch03-m2", "label": "Build LogAnalyzer class with clean state & methods"},
                {"id": "ch03-m3", "label": "Wire cli.py with Path & pass pytest"},
            ],
        },
    },
]
