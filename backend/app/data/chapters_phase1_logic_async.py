"""Phase 1 Part B (Chapters 4-6): Step-by-Step Logic Building (Before DSA), DSA & DP, and Async Programming."""

from __future__ import annotations

from typing import Any

PHASE_1B_CHAPTERS: list[dict[str, Any]] = [
    # =========================================================================
    # CHAPTER 4: Logic Building Step-by-Step (Before Any DSA!)
    # =========================================================================
    {
        "id": "ch04",
        "number": 4,
        "phase": 1,
        "phase_title": "Phase 1: Python From Zero — Basics, Files, OOP & Logic",
        "title": "Logic Building Step-by-Step (Think Before You Code)",
        "subtitle": "Paper dry-runs, accumulators (manual max/min/sum), filtering, grouping, nested loops, and gentle transition to faster patterns.",
        "status_type": "available",
        "estimated_hours": 7,
        "why_it_matters": (
            "Jumping straight into LeetCode or DSA when you still hesitate on basic loop logic causes frustration. "
            "Here we build raw problem-solving logic slowly on everyday problems first—so DSA feels easy later."
        ),
        "just_in_time_tags": ["Paper Dry-Run", "Manual Max/Min", "Filter & Transform", "Grouping Dicts", "Nested Loops", "Speeding Up Logic"],
        "visualizer": "recursion_stack",
        "sections": [
            {
                "id": "ch04-s1",
                "title": "4.1 How a Human Solves a Problem (Paper Dry-Run -> Variables)",
                "zero_assumption_note": "If you stare at a blank editor not knowing which line to type first, STOP typing and walk 4 items on paper first.",
                "definition": (
                    "**Logic building** is simply noticing what small pieces of information your brain keeps track of while solving a 4-item example by hand—and turning each piece into a Python variable."
                ),
                "syntax_box": {
                    "title": "The 4-Step Human Thinking Checklist",
                    "syntax": (
                        "# Step 1: What goes IN and what comes OUT? (check empty list [] too!)\n"
                        "# Step 2: Walk a tiny example [4, 9, 2, 7] by hand.\n"
                        "# Step 3: Ask: 'What did my brain have to remember at each step?'\n"
                        "# Step 4: Turn that memory into variables + a loop!"
                    ),
                    "breakdown": [
                        "Example: *'Find the biggest number in `[4, 9, 2, 7]` without calling `max()`.'*",
                        "Your eyes scan left-to-right. All your brain remembers is **1 number**: `'biggest I saw so far'`!",
                        "Start `best = nums[0]` (`4`), compare each next item: if `n > best`, update `best = n`!",
                    ],
                },
                "tiny_example": {
                    "title": "Finding Maximum Manually (Tracing Every Round)",
                    "code": (
                        "nums = [4, 9, 2, 7]\n"
                        "best = nums[0]\n"
                        "for n in nums:\n"
                        "    if n > best:\n"
                        "        best = n\n"
                        "print('Biggest:', best)"
                    ),
                    "line_by_line": [
                        "Start: `best = 4`.",
                        "Round 1 (`n=4`): `4 > 4` False -> `best` stays `4`.",
                        "Round 2 (`n=9`): `9 > 4` True -> `best` becomes `9`.",
                        "Round 3 (`n=2`): `2 > 9` False -> `best` stays `9`.",
                        "Round 4 (`n=7`): `7 > 9` False -> `best` stays `9` -> prints `9`!",
                    ],
                },
                "body_markdown": (
                    "### Why Not `best = 0`?\n"
                    "Always test negative numbers! If `nums = [-10, -3, -20]` and you started with `best = 0`, `best` would stay `0` (wrong—`0` isn't even in the list!). "
                    "Starting at `best = nums[0]` (after guarding `if not nums:`) works for positive AND negative numbers!"
                ),
                "code_example": {
                    "title": "Guarded Manual Min & Max Together",
                    "code": (
                        "def min_and_max(nums: list[int]) -> tuple[int, int] | None:\n"
                        "    # Block 1 (Guard): empty list has no min or max\n"
                        "    if not nums:\n"
                        "        return None\n"
                        "    # Block 2: Remember smallest and largest seen so far\n"
                        "    low = nums[0]\n"
                        "    high = nums[0]\n"
                        "    for n in nums[1:]:\n"
                        "        if n < low:\n"
                        "            low = n\n"
                        "        if n > high:\n"
                        "            high = n\n"
                        "    return (low, high)\n\n"
                        "print(min_and_max([-10, -3, -20]))  # (-20, -3)\n"
                    ),
                },
                "common_mistakes": [
                    "Initializing `best = 0` instead of `nums[0]` (fails when all inputs are negative!).",
                    "Forgetting to check `if not nums:` before accessing `nums[0]` (crashes with `IndexError` on `[]`).",
                ],
                "key_takeaway": "Solve 4 items with your finger first; the things your brain remembers become your initial variables.",
            },
            {
                "id": "ch04-s2",
                "title": "4.2 Everyday Loop Logic: Filtering, Building, Reversing & Checking",
                "zero_assumption_note": "Before touching algorithms, get super comfortable building new lists, checking flags (`all` / `any`), and tracking streaks.",
                "definition": (
                    "Most everyday programming tasks fall into 4 simple patterns: **Filter** (keep some items), **Transform** (change every item), "
                    "**All/Any Flag** (does every item pass?), and **Streak State** (what happened right before this item?)."
                ),
                "syntax_box": {
                    "title": "Flag Logic (`all` vs `any`) & State Variable",
                    "syntax": (
                        "# Pattern A: Does ANY item fail? (start True, flip False on first failure)\n"
                        "all_positive = True\n"
                        "for n in nums:\n"
                        "    if n <= 0:\n"
                        "        all_positive = False\n"
                        "        break\n\n"
                        "# Pattern B: Streak state (remember previous item)\n"
                        "prev = text[0]\n"
                        "count = 1"
                    ),
                    "breakdown": [
                        "Never write `else: all_positive = True` inside the loop—one good item at the end would erase an earlier failure!",
                        "`break` exits immediately once you already know the answer.",
                    ],
                },
                "tiny_example": {
                    "title": "Reversing a List Manually (No `.reverse()` Shortcut)",
                    "code": (
                        "items = ['a', 'b', 'c']\n"
                        "reversed_items = []\n"
                        "for i in range(len(items) - 1, -1, -1):\n"
                        "    reversed_items.append(items[i])\n"
                        "print(reversed_items)"
                    ),
                    "line_by_line": [
                        "`range(2, -1, -1)` counts backwards: `2, 1, 0` (stops before `-1`).",
                        "Appends `items[2]` (`'c'`), `items[1]` (`'b'`), `items[0]` (`'a'`).",
                        "Prints `['c', 'b', 'a']`.",
                    ],
                },
                "body_markdown": (
                    "### Streak Logic: Run-Length Compression (`'aaabbc' -> 'a3b2c1'`)\n"
                    "Walk left-to-right holding two variables: `current` char and `count`. When the next char matches, `count += 1`. When it changes, save `f'{current}{count}'` and reset! Don't forget to save the final streak after the loop ends."
                ),
                "code_example": {
                    "title": "Run-Length String Compressor",
                    "code": (
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
                        "    parts.append(f'{current}{count}')  # flush the final group!\n"
                        "    return ''.join(parts)\n\n"
                        "print(compress_runs('aaabbc'))  # 'a3b2c1'\n"
                    ),
                },
                "common_mistakes": [
                    "Adding `else: flag = True` inside an all-check loop (overwrites an earlier `False`!).",
                    "Forgetting to flush the final group after a streak loop finishes.",
                ],
                "key_takeaway": "Keep flag checks one-way (`True -> False` on failure + `break`), and always check what happens after the last loop item.",
            },
            {
                "id": "ch04-s3",
                "title": "4.3 Grouping, Nested Loops (2D) & Breaking Problems Into Helpers",
                "zero_assumption_note": "If a problem feels big, don't write one 40-line tangled loop—split it into two tiny, obvious steps.",
                "definition": (
                    "- **Nested loop:** A loop inside another loop—the inner loop runs completely for *each* round of the outer loop.\n"
                    "- **Decomposition:** Splitting a tricky task into 2 small helper functions where each helper is easy to trace."
                ),
                "syntax_box": {
                    "title": "Nested Loop Pairs & Grouping Pattern",
                    "syntax": (
                        "# Print all unique pairs (i < j avoids checking (a,b) AND (b,a)):\n"
                        "for i in range(len(items)):\n"
                        "    for j in range(i + 1, len(items)):\n"
                        "        print(items[i], items[j])\n\n"
                        "# Grouping items into a dict of lists:\n"
                        "groups = {}\n"
                        "for word in words:\n"
                        "    first_letter = word[0]\n"
                        "    if first_letter not in groups:\n"
                        "        groups[first_letter] = []\n"
                        "    groups[first_letter].append(word)"
                    ),
                    "breakdown": [
                        "`j` starts at `i + 1` so an item never pairs with itself and pairs aren't repeated backwards.",
                        "In grouping, we initialize `groups[key] = []` the first time we see `key`, then `.append()`.",
                    ],
                },
                "tiny_example": {
                    "title": "Grouping Words by Length",
                    "code": (
                        "words = ['ai', 'cat', 'ml', 'code']\n"
                        "by_len = {}\n"
                        "for w in words:\n"
                        "    n = len(w)\n"
                        "    if n not in by_len:\n"
                        "        by_len[n] = []\n"
                        "    by_len[n].append(w)\n"
                        "print(by_len)"
                    ),
                    "line_by_line": [
                        "`'ai'` (len 2): creates `by_len[2] = ['ai']`.",
                        "`'cat'` (len 3): creates `by_len[3] = ['cat']`.",
                        "`'ml'` (len 2): `2` already exists -> appends `'ml'` -> `{2: ['ai', 'ml'], 3: ['cat'], 4: ['code']}`.",
                    ],
                },
                "body_markdown": (
                    "### Breaking a 2-Step Problem Into 2 Small Functions\n"
                    "Suppose you need: *'Find the word that appears most often in a paragraph, ignoring punctuation.'*\n"
                    "1. Helper 1: `clean_words(text)` -> lowercase & strip punctuation.\n"
                    "2. Helper 2: `count_words(words)` -> dict of counts, then loop over dict to find the highest count!"
                ),
                "code_example": {
                    "title": "Two-Step Most Frequent Word (Zero Magic)",
                    "code": (
                        "def most_common_word(text: str) -> str:\n"
                        "    # Step 1: Count every word in a dict\n"
                        "    counts: dict[str, int] = {}\n"
                        "    for w in text.lower().split():\n"
                        "        counts[w] = counts.get(w, 0) + 1\n\n"
                        "    # Step 2: Manual max over (word, count) pairs\n"
                        "    best_word = ''\n"
                        "    best_count = 0\n"
                        "    for word, cnt in counts.items():\n"
                        "        if cnt > best_count:\n"
                        "            best_word = word\n"
                        "            best_count = cnt\n"
                        "    return best_word\n\n"
                        "print(most_common_word('AI helps build AI tools'))  # 'ai'\n"
                    ),
                },
                "common_mistakes": [
                    "Trying to do Step 1 and Step 2 inside one confusing loop when two simple loops back-to-back are crystal clear and still fast!",
                ],
                "key_takeaway": "Two simple loops in sequence are way easier to write and debug than one tangled loop. Split big logic into small steps.",
            },
            {
                "id": "ch04-s4",
                "title": "4.4 Leveling Up: Hash Map Lookups, Two Pointers, Sliding Window & Gentle Recursion",
                "zero_assumption_note": "Now that basic loops and dicts feel solid, let's see why certain patterns make slow nested loops 1,000x faster.",
                "definition": (
                    "- **Hash Map Lookup (`seen`):** Remembering past items in a `dict`/`set` so you don't re-scan the whole list.\n"
                    "- **Two Pointers (`left`, `right`):** Two indexes walking inward on sorted data.\n"
                    "- **Sliding Window:** Updating a moving slice by `+new -old` instead of re-summing.\n"
                    "- **Recursion:** A function calling itself on a smaller piece until hitting a stopping **base case**."
                ),
                "syntax_box": {
                    "title": "Replacing a Slow Nested Loop With a `seen` Dictionary",
                    "syntax": (
                        "# Find two numbers adding to target:\n"
                        "seen = {}  # value -> index\n"
                        "for i, x in enumerate(nums):\n"
                        "    need = target - x\n"
                        "    if need in seen:\n"
                        "        return (seen[need], i)\n"
                        "    seen[x] = i"
                    ),
                    "breakdown": [
                        "`enumerate(nums)` gives `(index, value)` together so you don't need `range(len(nums))`.",
                        "Instead of looping over all earlier elements to find `target - x`, `if need in seen:` checks the dictionary in **1 instant step**!",
                    ],
                },
                "tiny_example": {
                    "title": "Gentle Recursion: Countdown & Sum",
                    "code": (
                        "def sum_list(nums: list[int]) -> int:\n"
                        "    if not nums:            # 1. Base case: empty list sums to 0\n"
                        "        return 0\n"
                        "    return nums[0] + sum_list(nums[1:])  # 2. First item + sum of rest\n\n"
                        "print(sum_list([3, 5, 2]))"
                    ),
                    "line_by_line": [
                        "`sum_list([3, 5, 2])` asks for `3 + sum_list([5, 2])`.",
                        "`sum_list([5, 2])` asks for `5 + sum_list([2])`.",
                        "`sum_list([2])` asks for `2 + sum_list([])`.",
                        "`sum_list([])` hits the Base Case and returns `0`, then everything unwinds: `2+0=2`, `5+2=7`, `3+7=10`!",
                    ],
                },
                "body_markdown": (
                    "**Step through the interactive Call Stack Visualizer below** to watch recursive frames stack up and return one by one!"
                ),
                "code_example": {
                    "title": "Two Pointers & Sliding Window Side-by-Side",
                    "code": (
                        "# Block 1: Two Pointers (checks if sorted list has two numbers summing to target)\n"
                        "def has_pair_sorted(nums: list[int], target: int) -> bool:\n"
                        "    left, right = 0, len(nums) - 1\n"
                        "    while left < right:\n"
                        "        s = nums[left] + nums[right]\n"
                        "        if s == target:\n"
                        "            return True\n"
                        "        if s < target:\n"
                        "            left += 1\n"
                        "        else:\n"
                        "            right -= 1\n"
                        "    return False\n\n"
                        "# Block 2: Fixed Sliding Window (max sum of k consecutive numbers)\n"
                        "def max_window_sum(nums: list[int], k: int) -> int:\n"
                        "    win = sum(nums[:k])\n"
                        "    best = win\n"
                        "    for right in range(k, len(nums)):\n"
                        "        win += nums[right] - nums[right - k]\n"
                        "        best = max(best, win)\n"
                        "    return best\n"
                    ),
                },
                "common_mistakes": [
                    "Trying to use Two Pointers on an *unsorted* list when the logic assumes sorted order.",
                    "Writing recursion without a reachable base case (`RecursionError`).",
                ],
                "key_takeaway": "Reach for `seen` dicts, Two Pointers, and Sliding Windows whenever a nested loop feels repetitive.",
            },
        ],
        "quizzes": [
            {
                "id": "ch04-q1",
                "question": "Why does initializing `best = 0` fail when finding the largest number in `[-5, -2, -9]`?",
                "options": [
                    "Python can't compare negative numbers",
                    "`0` is larger than all numbers in the list, so `best` stays `0` even though `0` isn't in the list",
                    "`for` loops skip negative numbers",
                    "`best` should start at `100`",
                ],
                "correct_index": 1,
                "explanation": "Starting `best = nums[0]` ensures your baseline is actually an element from the list.",
            },
            {
                "id": "ch04-q2",
                "question": "Why does `if need in seen:` with a `dict`/`set` beat an inner `for` loop?",
                "options": [
                    "Dictionary/set lookup checks membership in ~1 step instead of scanning every item again",
                    "Dictionaries sort numbers automatically",
                    "Sets use less syntax",
                    "Inner `for` loops aren't allowed in functions",
                ],
                "correct_index": 0,
                "explanation": "Hash-based lookup turns an O(N^2) double scan into a single O(N) pass.",
            },
        ],
        "project": {
            "title": "Pure-Python Text Tokenizer & Inverted Index Search Engine",
            "workspace_dir": "projects/ch04_mini_search_engine",
            "overview": "Use your logic-building skills (splitting text, counting words, dict grouping) to build a pure-Python keyword search engine.",
            "architecture_steps": [
                "Write `tokenize(text)` normalizing lowercase words.",
                "Build `InvertedIndex` mapping `word -> set of doc_ids`.",
                "Implement ranked `AND` / `OR` queries + `pytest`.",
            ],
            "milestones": [
                {"id": "ch04-m1", "label": "Implement text normalization & tokenizer"},
                {"id": "ch04-m2", "label": "Build InvertedIndex mapping words to doc IDs"},
                {"id": "ch04-m3", "label": "Implement ranked search queries + pytest"},
            ],
        },
    },

    # =========================================================================
    # CHAPTER 5: Essential DSA & Dynamic Programming Demystified
    # =========================================================================
    {
        "id": "ch05",
        "number": 5,
        "phase": 1,
        "phase_title": "Phase 1: Python From Zero — Basics, Files, OOP & Logic",
        "title": "Essential DSA & Dynamic Programming Demystified",
        "subtitle": "Big-O intuition, Queues (deque), Heaps (heapq), Graphs (BFS & DAGs), and Dynamic Programming from recursion to tables.",
        "status_type": "available",
        "estimated_hours": 7,
        "why_it_matters": (
            "Now that your loop & dict logic is strong, DSA gives you specialized tools: `deque` for queues/BFS, `heapq` for Top-K "
            "LLM token selection, DAGs for ML pipelines, and Dynamic Programming for sequence alignment & edit distance."
        ),
        "just_in_time_tags": ["Big-O", "Queue (deque)", "Heap (heapq)", "Graphs & DAGs", "Dynamic Programming"],
        "visualizer": "dp_table",
        "sections": [
            {
                "id": "ch05-s1",
                "title": "5.1 Queues (`deque`), Heaps (`heapq`) & Graphs (BFS & DAGs)",
                "zero_assumption_note": "Pick the data structure that matches the job you repeat most—never memorize unused structures.",
                "definition": (
                    "- **`deque`:** A fast two-ended queue (add to back, remove from front in 1 step).\n"
                    "- **`heapq`:** Quickly grabs the smallest or Top-K largest items without sorting the entire list.\n"
                    "- **Graph / DAG:** Nodes connected by arrows (e.g., task dependencies `clean -> train -> eval`)."
                ),
                "syntax_box": {
                    "title": "deque & heapq Essentials",
                    "syntax": (
                        "from collections import deque\n"
                        "import heapq\n\n"
                        "q = deque(['A'])\n"
                        "q.append('B')\n"
                        "front = q.popleft()              # 'A' in O(1) — unlike list.pop(0)!\n\n"
                        "top2 = heapq.nlargest(2, [5, 9, 2, 7])  # [9, 7]"
                    ),
                    "breakdown": [
                        "Never use `list.pop(0)` as a queue because Python shifts every remaining element in memory.",
                        "`seen = {'A'}` inside graph BFS prevents walking in circles forever if nodes point back to each other.",
                    ],
                },
                "tiny_example": {
                    "title": "Finding Shortest Hops in a Small Graph (BFS)",
                    "code": (
                        "from collections import deque\n"
                        "graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}\n"
                        "q = deque([('A', 0)])\n"
                        "seen = {'A'}\n"
                        "while q:\n"
                        "    node, dist = q.popleft()\n"
                        "    print(node, 'is', dist, 'hops from A')\n"
                        "    for nxt in graph[node]:\n"
                        "        if nxt not in seen:\n"
                        "            seen.add(nxt)\n"
                        "            q.append((nxt, dist + 1))"
                    ),
                    "line_by_line": [
                        "Starts at `'A'` with distance `0`.",
                        "Pops `'A'`, adds neighbors `'B'` (dist 1) and `'C'` (dist 1).",
                        "Pops `'B'` (dist 1), adds `'D'` (dist 2).",
                        "Because `deque` explores closer layers first, the first time BFS reaches any node is guaranteed to be the shortest path!",
                    ],
                },
                "body_markdown": (
                    "### Topological Sort on a DAG\n"
                    "When ML pipeline steps have prerequisites (`clean` before `train`, `train` before `eval`), Kahn's algorithm counts each step's remaining prerequisites (`in_degree`), runs `0`-prerequisite steps first, and unlocks downstream steps one by one."
                ),
                "code_example": {
                    "title": "Shortest Hops Function",
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
                    "Forgetting `seen` in BFS -> infinite loop on cyclic graphs.",
                    "Using `list.pop(0)` instead of `deque.popleft()`.",
                ],
                "key_takeaway": "Use `deque` for queues/BFS, `heapq` for Top-K, and Kahn's algorithm for dependent tasks.",
            },
            {
                "id": "ch05-s2",
                "title": "5.2 Dynamic Programming Demystified (Recursion -> Memo -> Table)",
                "zero_assumption_note": "Dynamic Programming is NOT a scary trick. It literally means: **save sub-answers so you never calculate the exact same thing twice**.",
                "definition": (
                    "**Dynamic Programming (DP)** takes a recursive problem where the same smaller calls repeat over and over, and caches each answer once in a `memo` dict or `dp` list."
                ),
                "syntax_box": {
                    "title": "From Slow Recursion -> Fast Memo -> Simple Loop Table",
                    "syntax": (
                        "# 1. Memoized Recursion (Top-Down):\n"
                        "memo = {}\n"
                        "def ways(n):\n"
                        "    if n <= 1: return 1\n"
                        "    if n in memo: return memo[n]\n"
                        "    memo[n] = ways(n - 1) + ways(n - 2)\n"
                        "    return memo[n]\n\n"
                        "# 2. Bottom-Up Table (Loop):\n"
                        "dp = [1] * (n + 1)\n"
                        "for i in range(2, n + 1):\n"
                        "    dp[i] = dp[i - 1] + dp[i - 2]"
                    ),
                    "breakdown": [
                        "Without `memo`, `ways(50)` repeats billions of calls and freezes for hours.",
                        "With `memo` or `dp`, each step `0..50` is computed **once** (50 additions -> finishes in 0.0001s!).",
                    ],
                },
                "tiny_example": {
                    "title": "Climbing 4 Stairs (1 or 2 Steps at a Time)",
                    "code": (
                        "dp = [1, 1, 0, 0, 0]\n"
                        "for i in range(2, 5):\n"
                        "    dp[i] = dp[i - 1] + dp[i - 2]\n"
                        "    print(f'Step {i}: {dp[i]} ways')\n"
                        "print('Full table:', dp)"
                    ),
                    "line_by_line": [
                        "Base cases: 1 way at step 0 (`dp[0]=1`), 1 way to reach step 1 (`dp[1]=1`).",
                        "To reach step 2, you came from step 1 or step 0: `1 + 1 = 2`.",
                        "Step 3: `2 + 1 = 3`. Step 4: `3 + 2 = 5`.",
                    ],
                },
                "body_markdown": (
                    "**Step through the interactive 2D DP Table below** to watch Edit Distance (`cat` -> `cut`) fill one cell at a time!"
                ),
                "code_example": {
                    "title": "1D DP: Minimum Coins (Where Greedy Fails)",
                    "code": (
                        "def min_coins(coins: list[int], amount: int) -> int:\n"
                        "    inf = amount + 1\n"
                        "    dp = [inf] * (amount + 1)\n"
                        "    dp[0] = 0\n"
                        "    for a in range(1, amount + 1):\n"
                        "        for c in coins:\n"
                        "            if c <= a:\n"
                        "                dp[a] = min(dp[a], 1 + dp[a - c])\n"
                        "    return -1 if dp[amount] > amount else dp[amount]\n\n"
                        "print('Min coins for 6 with [1,3,4]:', min_coins([1, 3, 4], 6))  # 2 (3+3)\n"
                    ),
                },
                "common_mistakes": [
                    "Trying to jump straight to a 2D loop without tracing a tiny `3x3` example on paper first.",
                    "Forgetting base cases (`dp[0]`).",
                ],
                "key_takeaway": "DP = recursion + cache (or a small loop filling a `dp` array from `0` upward).",
            },
        ],
        "quizzes": [
            {
                "id": "ch05-q1",
                "question": "What does adding `memo` or a `dp` table actually change?",
                "options": [
                    "It stores each subproblem answer once so repeated calls look it up in 1 step instead of recalculating",
                    "It runs loops backwards",
                    "It removes base cases",
                    "It requires NumPy",
                ],
                "correct_index": 0,
                "explanation": "Caching repeated subproblems eliminates exponential redundant work.",
            },
        ],
        "project": {
            "title": "Autocomplete, DP Spell-Checker & DAG Pipeline Scheduler",
            "workspace_dir": "projects/ch05_autocomplete_dp_scheduler",
            "overview": "Combine Trie autocomplete, 2D DP Levenshtein spell-checking, and Kahn's DAG topological sort.",
            "architecture_steps": [
                "Implement `Trie` prefix lookup.",
                "Implement 2D DP `edit_distance(a, b)`.",
                "Implement Kahn's topological sort (`schedule_tasks`).",
            ],
            "milestones": [
                {"id": "ch05-m1", "label": "Implement Trie prefix autocomplete"},
                {"id": "ch05-m2", "label": "Implement 2D DP edit distance"},
                {"id": "ch05-m3", "label": "Implement DAG topological sort & pytest"},
            ],
        },
    },

    # =========================================================================
    # CHAPTER 6: Async Programming & Concurrency
    # =========================================================================
    {
        "id": "ch06",
        "number": 6,
        "phase": 1,
        "phase_title": "Phase 1: Python From Zero — Basics, Files, OOP & Logic",
        "title": "Concurrency, Async Programming & Event Loops",
        "subtitle": "Waiting vs computing, async def, await, asyncio.gather, Semaphores, and exponential backoff retries.",
        "status_type": "available",
        "estimated_hours": 5,
        "why_it_matters": (
            "Calling LLM APIs, fetching documents, and serving web users spend most of their time *waiting* on network replies. "
            "`asyncio` overlaps all those waits so 100 API calls finish in ~1 second instead of 100 seconds."
        ),
        "just_in_time_tags": ["I/O vs CPU", "async def / await", "asyncio.gather", "Semaphore", "Retries"],
        "visualizer": "asyncio_loop",
        "sections": [
            {
                "id": "ch06-s1",
                "title": "6.1 `async def`, `await`, `gather` & `Semaphore` From Scratch",
                "zero_assumption_note": "When boiling water (3 min wait) and chopping onions, you don't stand frozen staring at the kettle—you start the kettle, then chop while waiting!",
                "definition": (
                    "- **Asynchronous (`asyncio`):** Lets one Python thread juggle many *waiting* I/O tasks by switching tasks whenever one hits `await`.\n"
                    "- **Event Loop:** The scheduler started by `asyncio.run(...)` that switches between paused tasks."
                ),
                "syntax_box": {
                    "title": "Core `asyncio` Syntax",
                    "syntax": (
                        "import asyncio\n\n"
                        "async def fetch(i: int) -> str:\n"
                        "    await asyncio.sleep(1.0)             # pauses & yields to other tasks!\n"
                        "    return f'ok-{i}'\n\n"
                        "async def main():\n"
                        "    res = await asyncio.gather(fetch(1), fetch(2))  # runs both together!\n"
                        "    print(res)\n\n"
                        "asyncio.run(main())"
                    ),
                    "breakdown": [
                        "`async def` creates a pauseable coroutine function.",
                        "`await` means: *\"Pause here until this wait finishes; let other tasks run in the meantime.\"*",
                        "`asyncio.gather(...)` launches multiple coroutines concurrently and returns results in original order.",
                        "`asyncio.Semaphore(N)` limits concurrency so at most `N` tasks run at once (prevents API rate-limit bans!).",
                    ],
                },
                "tiny_example": {
                    "title": "Two 1-Second Tasks Finishing in ~1 Second Total",
                    "code": (
                        "import asyncio, time\n\n"
                        "async def task(name):\n"
                        "    await asyncio.sleep(0.2)\n"
                        "    return name\n\n"
                        "async def main():\n"
                        "    t0 = time.perf_counter()\n"
                        "    out = await asyncio.gather(task('A'), task('B'), task('C'))\n"
                        "    print(out, f'in {time.perf_counter() - t0:.2f}s')\n\n"
                        "asyncio.run(main())"
                    ),
                    "line_by_line": [
                        "`gather` starts A, B, and C immediately—all three sleep for 0.2s *at the same time*.",
                        "Total time is `~0.20s` instead of `0.60s`!",
                    ],
                },
                "body_markdown": (
                    "**Try the interactive Asyncio Event Loop Simulator below** to compare Sequential `for await` vs `gather` vs `Semaphore(2)`!"
                ),
                "code_example": {
                    "title": "Capping Concurrency With `asyncio.Semaphore`",
                    "code": (
                        "import asyncio\n\n"
                        "async def bounded_worker(sem: asyncio.Semaphore, item_id: int) -> str:\n"
                        "    async with sem:\n"
                        "        await asyncio.sleep(0.05)\n"
                        "        return f'done-{item_id}'\n\n"
                        "async def run_batch() -> list[str]:\n"
                        "    sem = asyncio.Semaphore(3)\n"
                        "    return list(await asyncio.gather(*(bounded_worker(sem, i) for i in range(6))))\n\n"
                        "print(asyncio.run(run_batch()))\n"
                    ),
                },
                "common_mistakes": [
                    "Calling `time.sleep(1)` or `requests.get()` inside `async def` (freezes the whole event loop!). Use `await asyncio.sleep()` / `httpx.AsyncClient`.",
                    "Writing `for x in items: await task(x)` (runs sequentially instead of using `asyncio.gather`).",
                ],
                "key_takeaway": "Use `async def` + `await` for waiting I/O, `asyncio.gather` to overlap tasks, and `Semaphore` to limit concurrent requests.",
            },
        ],
        "quizzes": [
            {
                "id": "ch06-q1",
                "question": "Why does calling `time.sleep(5)` inside an `async def` function hurt performance?",
                "options": [
                    "It blocks the single event loop thread so NO other async tasks can run for 5 seconds",
                    "Python raises SyntaxError",
                    "It deletes pending tasks",
                    "It runs on another process",
                ],
                "correct_index": 0,
                "explanation": "Always use non-blocking `await asyncio.sleep(5)` so the event loop can run other tasks while waiting.",
            },
        ],
        "project": {
            "title": "Async Rate-Limited API Batch Harvester",
            "workspace_dir": "projects/ch06_async_harvester",
            "overview": "Fetch batches concurrently using `asyncio.Semaphore` and exponential backoff retries.",
            "architecture_steps": [
                "Write `retry_async` with exponential sleep backoff.",
                "Bound batch execution with `asyncio.Semaphore` and `gather`.",
                "Verify speedup & failure handling with `pytest`.",
            ],
            "milestones": [
                {"id": "ch06-m1", "label": "Implement exponential backoff retry coroutine"},
                {"id": "ch06-m2", "label": "Add Semaphore concurrency cap"},
                {"id": "ch06-m3", "label": "Pass pytest async speedup checks"},
            ],
        },
    },
]
