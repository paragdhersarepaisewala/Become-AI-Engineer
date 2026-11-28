"""Phase 2 Curriculum (Chapters 8-14, One Library Per Chapter): NumPy, Pandas, Pydantic, Requests, FastAPI, FastMCP, Docker."""

from __future__ import annotations

from typing import Any

PHASE_2_CHAPTERS: list[dict[str, Any]] = [
    # =========================================================================
    # CHAPTER 8: NumPy (Single Library Focus)
    # =========================================================================
    {
        "id": "ch08",
        "number": 8,
        "phase": 2,
        "phase_title": "Phase 2: AI Engineering Libraries (One Library Per Chapter)",
        "title": "NumPy — Arrays, Shapes & Vectorized Math",
        "subtitle": "Arrays vs Python lists, .shape, axis=0 vs axis=1, broadcasting rules, dot products (@), cosine similarity, and stable softmax.",
        "status_type": "available",
        "estimated_hours": 5,
        "why_it_matters": (
            "PyTorch tensors and Transformer attention layers work almost identically to NumPy arrays. Mastering `.shape`, `axis`, "
            "and broadcasting here makes deep learning code easy to read."
        ),
        "just_in_time_tags": ["NumPy", "np.array & .shape", "axis=0 vs axis=1", "Broadcasting", "Dot Product (@)", "Softmax"],
        "visualizer": "numpy_broadcast",
        "sections": [
            {
                "id": "ch08-s1",
                "title": "8.1 NumPy Arrays, `.shape` & `axis` (Replacing Slow Loops)",
                "zero_assumption_note": "If `axis=0` vs `axis=1` always confused you, remember: `axis` tells NumPy **which direction to collapse**.",
                "definition": (
                    "A **NumPy array (`ndarray`)** stores numbers in one packed block of C memory so math runs across whole rows/columns "
                    "at once—often 50x faster than a Python `for` loop."
                ),
                "syntax_box": {
                    "title": "Creating Arrays, Checking Shape & Collapsing Axes",
                    "syntax": (
                        "import numpy as np\n\n"
                        "a = np.array([[1.0, 2.0, 3.0],\n"
                        "              [4.0, 5.0, 6.0]])\n"
                        "a.shape               # (2, 3) -> 2 rows, 3 columns\n"
                        "a.sum(axis=0)         # [5., 7., 9.]  (collapses rows -> 1 per column)\n"
                        "a.sum(axis=1)         # [6., 15.]     (collapses cols -> 1 per row)\n"
                        "a.sum(axis=1, keepdims=True)  # shape (2, 1)"
                    ),
                    "breakdown": [
                        "`.shape` returns `(rows, cols)` for 2D arrays.",
                        "`axis=0` collapses axis 0 (rows); `axis=1` collapses axis 1 (columns).",
                        "`keepdims=True` keeps the collapsed axis as size `1` so division aligns cleanly!",
                    ],
                },
                "tiny_example": {
                    "title": "Doubling Numbers Without a `for` Loop",
                    "code": (
                        "import numpy as np\n"
                        "prices = np.array([10, 20, 30])\n"
                        "print(prices * 2)"
                    ),
                    "line_by_line": [
                        "`prices` is a 1D array of shape `(3,)`.",
                        "`prices * 2` multiplies every number in C memory at once -> `[20 40 60]`.",
                    ],
                },
                "body_markdown": (
                    "### Broadcasting & Dot Product (`@`)\n"
                    "- **Broadcasting:** Compares two shapes **right-to-left**. Dimensions match if they are **equal** OR **one of them is `1`**.\n"
                    "- **Matrix Multiply (`A @ B`):** Multiplies matching dimensions and sums them—used everywhere in embeddings and neural layers.\n\n"
                    "**Test shapes live** in the NumPy Broadcasting Explorer below!"
                ),
                "code_example": {
                    "title": "Stable Softmax & Cosine Top-K Search",
                    "code": (
                        "import numpy as np\n\n"
                        "def softmax(logits: np.ndarray) -> np.ndarray:\n"
                        "    shifted = logits - np.max(logits, axis=-1, keepdims=True)\n"
                        "    exps = np.exp(shifted)\n"
                        "    return exps / np.sum(exps, axis=-1, keepdims=True)\n\n"
                        "print(softmax(np.array([2.0, 1.0, 0.1])))\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting `keepdims=True` before dividing `(N, D)` by `(N,)`.",
                    "Using `*` instead of `@` when you want matrix multiplication.",
                ],
                "key_takeaway": "Print `.shape` whenever confused, pass `keepdims=True` when normalizing rows/columns, and read broadcasting right-to-left.",
            },
        ],
        "quizzes": [
            {
                "id": "ch08-q1",
                "question": "If `X` has shape `(4, 3)`, what shape does `X.sum(axis=1, keepdims=True)` return?",
                "options": ["(3,)", "(4, 1)", "(1, 3)", "(4,)"],
                "correct_index": 1,
                "explanation": "`axis=1` collapses the 3 columns into 1 while `keepdims=True` preserves the 2D shape `(4, 1)`.",
            },
        ],
        "project": {
            "title": "Pure-NumPy Semantic Vector Search Engine",
            "workspace_dir": "projects/ch08_numpy_semantic_search",
            "overview": "Implement L2 normalization, stable softmax, and top-K cosine similarity retrieval in pure NumPy.",
            "architecture_steps": [
                "Implement vectorized L2 row normalization.",
                "Implement batched cosine similarity and top-K ranking.",
                "Verify speed & accuracy with `pytest`.",
            ],
            "milestones": [
                {"id": "ch08-m1", "label": "Implement L2 normalization & stable softmax"},
                {"id": "ch08-m2", "label": "Implement top-K cosine search"},
                {"id": "ch08-m3", "label": "Verify with pytest"},
            ],
        },
    },

    # =========================================================================
    # CHAPTER 9: Pandas (Single Library Focus)
    # =========================================================================
    {
        "id": "ch09",
        "number": 9,
        "phase": 2,
        "phase_title": "Phase 2: AI Engineering Libraries (One Library Per Chapter)",
        "title": "Pandas — DataFrames, Cleaning & Data Pipelines",
        "subtitle": "Series & DataFrames, reading/writing CSV & JSON, loc vs iloc, filtering, .str cleaning, groupby, and deduplication.",
        "status_type": "available",
        "estimated_hours": 5,
        "why_it_matters": (
            "Training ML models or fine-tuning LLMs on duplicate, null, or noisy text wastes compute and causes train/test leakage."
        ),
        "just_in_time_tags": ["Pandas", "DataFrame", "loc vs iloc", "read_csv / to_json", "GroupBy", "Deduplication"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch09-s1",
                "title": "9.1 DataFrames, `loc`/`iloc`, File I/O & Cleaning Datasets",
                "zero_assumption_note": "Think of a Pandas `DataFrame` as an in-memory Excel table where each column is a fast Series.",
                "definition": (
                    "A **DataFrame** holds rows and named columns (`df['text']`, `df['score']`). Instead of looping row-by-row, "
                    "you filter and transform entire columns at once using boolean masks and `.str` methods."
                ),
                "syntax_box": {
                    "title": "Essential DataFrame Syntax",
                    "syntax": (
                        "import pandas as pd\n\n"
                        "df = pd.DataFrame([{'text': ' Hi ', 'score': 0.9}, {'text': None, 'score': 0.2}])\n"
                        "clean = df.dropna(subset=['text']).copy()\n"
                        "clean['text'] = clean['text'].str.strip()\n"
                        "high = clean[clean['score'] >= 0.8]\n"
                        "df.loc[0, 'text']   # select by label\n"
                        "df.iloc[0, 0]       # select by integer position"
                    ),
                    "breakdown": [
                        "`.dropna(subset=['text'])`: removes rows where `'text'` is `None`/`NaN`.",
                        "`.copy()` after filtering prevents Pandas `SettingWithCopyWarning` when editing columns later.",
                        "`loc` uses **labels** (`df.loc[0:2]` includes `2`); `iloc` uses integer **positions** (`df.iloc[0:2]` stops before `2`).",
                    ],
                },
                "tiny_example": {
                    "title": "Filtering & Summarizing by Source",
                    "code": (
                        "import pandas as pd\n"
                        "df = pd.DataFrame([\n"
                        "    {'src': 'wiki', 'tokens': 100},\n"
                        "    {'src': 'wiki', 'tokens': 200},\n"
                        "    {'src': 'docs', 'tokens': 300},\n"
                        "])\n"
                        "print(df.groupby('src', as_index=False)['tokens'].mean())"
                    ),
                    "line_by_line": [
                        "Builds a 3-row table with `'src'` and `'tokens'`.",
                        "`groupby('src', as_index=False)` groups `'wiki'` rows together and `'docs'` rows together.",
                        "`.mean()` computes average tokens per source.",
                    ],
                },
                "body_markdown": (
                    "### Reading & Exporting Cleaned Files\n"
                    "Use `pd.read_csv('raw.csv')` / `pd.read_json('raw.jsonl', lines=True)` to load datasets, and `clean.to_csv('clean.csv', index=False)` to save without extra index columns."
                ),
                "code_example": {
                    "title": "Hash Deduplication Pipeline",
                    "code": (
                        "import hashlib\nimport pandas as pd\n\n"
                        "def text_hash(s: str) -> str:\n"
                        "    return hashlib.sha256(' '.join(s.lower().split()).encode('utf-8')).hexdigest()\n\n"
                        "df = pd.DataFrame([\n"
                        "    {'id': 1, 'text': 'Hello   AI'},\n"
                        "    {'id': 2, 'text': 'hello ai'},\n"
                        "])\n"
                        "df['hash'] = df['text'].map(text_hash)\n"
                        "print(df.drop_duplicates(subset=['hash']).reset_index(drop=True))\n"
                    ),
                },
                "common_mistakes": [
                    "Using `.iterrows()` to edit rows instead of vectorized `.str` / `.map()`.",
                    "Forgetting `.copy()` after filtering before adding new columns.",
                ],
                "key_takeaway": "Drop nulls, `.copy()`, clean columns with `.str`, deduplicate with hashes, and summarize with `.groupby().agg()`.",
            },
        ],
        "quizzes": [
            {
                "id": "ch09-q1",
                "question": "Why call `.copy()` right after filtering a DataFrame like `sub = df[df['score'] > 0.5].copy()`?",
                "options": [
                    "It sorts rows",
                    "It ensures `sub` is independent so adding columns won't trigger `SettingWithCopyWarning`",
                    "It saves to CSV",
                    "It drops NaN values",
                ],
                "correct_index": 1,
                "explanation": "Filtering often returns a view; `.copy()` makes future column edits safe.",
            },
        ],
        "project": {
            "title": "End-to-End LLM Corpus Curation Pipeline",
            "workspace_dir": "projects/ch09_corpus_curation_pipeline",
            "overview": "Clean messy JSONL/CSV text data, deduplicate via SHA-256, and export clean splits with source quality metrics.",
            "architecture_steps": [
                "Load raw records into Pandas and remove null/short noise.",
                "Deduplicate by normalized text hash.",
                "Produce `groupby` quality stats and save clean outputs.",
            ],
            "milestones": [
                {"id": "ch09-m1", "label": "Ingest & normalize raw text records"},
                {"id": "ch09-m2", "label": "Implement normalized hash deduplication"},
                {"id": "ch09-m3", "label": "Generate quality summary & export clean CSV/JSONL"},
            ],
        },
    },

    # =========================================================================
    # CHAPTER 10: Pydantic (Dedicated Chapter BEFORE Requests & FastAPI!)
    # =========================================================================
    {
        "id": "ch10",
        "number": 10,
        "phase": 2,
        "phase_title": "Phase 2: AI Engineering Libraries (One Library Per Chapter)",
        "title": "Pydantic — Data Validation, Models & Serialization",
        "subtitle": "BaseModel, automatic type checking, Field constraints, @field_validator, nested models, ValidationError, and JSON serialization.",
        "status_type": "available",
        "estimated_hours": 5,
        "why_it_matters": (
            "Before you call external APIs with `requests` or build servers with `FastAPI` or tools with `FastMCP`, "
            "you need **Pydantic**—the #1 library in Python AI engineering for validating messy JSON, enforcing schemas, and preventing silent data bugs."
        ),
        "just_in_time_tags": ["Pydantic", "BaseModel", "Field", "@field_validator", "Nested Models", "ValidationError"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch10-s1",
                "title": "10.1 `BaseModel` & Automatic Validation (Why Dicts Aren't Enough)",
                "zero_assumption_note": "Remember `@dataclass` from Chapter 4? `@dataclass` does NOT check if someone passes `'twenty'` for `age: int`. **Pydantic `BaseModel` DOES check and enforces rules automatically!**",
                "definition": (
                    "**Pydantic** lets you define Python classes inheriting from `BaseModel` that automatically convert valid inputs (like `'25'` -> `25`), "
                    "reject invalid inputs with a clear `ValidationError`, and convert cleanly to/from JSON."
                ),
                "syntax_box": {
                    "title": "Defining a `BaseModel` & Catching `ValidationError`",
                    "syntax": (
                        "from pydantic import BaseModel, Field, ValidationError\n\n"
                        "class UserProfile(BaseModel):\n"
                        "    username: str = Field(min_length=3, max_length=20)\n"
                        "    age: int = Field(ge=13)       # ge = greater than or equal to 13\n"
                        "    is_active: bool = True        # default value\n\n"
                        "user = UserProfile(username='sara', age='22')  # converts '22' -> 22!\n"
                        "print(user.model_dump())          # converts back to plain dict"
                    ),
                    "breakdown": [
                        "`BaseModel`: parent class giving your model validation + JSON superpowers.",
                        "`Field(min_length=3, ge=13)`: adds strict rules (`gt`, `ge`, `lt`, `le`, `min_length`, `max_length`).",
                        "`user.model_dump()` -> Python `dict`; `user.model_dump_json()` -> JSON string; `UserProfile.model_validate_json(raw_str)` -> parses & validates JSON in 1 call!",
                    ],
                },
                "tiny_example": {
                    "title": "Watching Pydantic Reject Bad Data Automatically",
                    "code": (
                        "from pydantic import BaseModel, Field, ValidationError\n\n"
                        "class Item(BaseModel):\n"
                        "    name: str = Field(min_length=1)\n"
                        "    price: float = Field(gt=0)\n\n"
                        "print(Item(name='Book', price='19.5'))\n"
                        "try:\n"
                        "    Item(name='Book', price=-5)\n"
                        "except ValidationError as err:\n"
                        "    print('Rejected!', err.errors()[0]['msg'])"
                    ),
                    "line_by_line": [
                        "`Item(name='Book', price='19.5')` succeeds and converts `'19.5'` to float `19.5`.",
                        "`Item(name='Book', price=-5)` fails `gt=0` and raises `ValidationError` cleanly!",
                    ],
                },
                "body_markdown": (
                    "### Why Pydantic Comes *Before* `requests`, `FastAPI` & `FastMCP`\n"
                    "- With **`requests`**, external APIs return messy JSON—Pydantic validates it immediately.\n"
                    "- With **`FastAPI`**, your endpoints use Pydantic models to reject invalid user JSON automatically.\n"
                    "- With **`FastMCP`**, AI agent tool inputs and outputs are typed with Pydantic schemas!"
                ),
                "code_example": {
                    "title": "Validating a JSON File of Records Safely",
                    "code": (
                        "from pydantic import BaseModel, Field, ValidationError\n\n"
                        "class PromptSample(BaseModel):\n"
                        "    prompt: str = Field(min_length=3)\n"
                        "    rating: int = Field(ge=1, le=5)\n\n"
                        "raw_rows = [\n"
                        "    {'prompt': 'Explain loops', 'rating': 5},\n"
                        "    {'prompt': 'Hi', 'rating': 5},        # too short!\n"
                        "    {'prompt': 'Explain OOP', 'rating': 9}, # rating > 5!\n"
                        "]\n\n"
                        "valid = []\n"
                        "for row in raw_rows:\n"
                        "    try:\n"
                        "        valid.append(PromptSample.model_validate(row))\n"
                        "    except ValidationError:\n"
                        "        continue\n"
                        "print('Valid samples:', valid)\n"
                    ),
                },
                "common_mistakes": [
                    "Trying to modify a Pydantic model like a dict (`user['age']` instead of `user.age`).",
                    "Using old Pydantic v1 `.dict()` / `.parse_raw()` instead of v2 `.model_dump()` / `.model_validate_json()`.",
                ],
                "key_takeaway": "Use Pydantic `BaseModel` + `Field` to turn untrusted dicts/JSON into guaranteed, typed Python objects.",
            },
            {
                "id": "ch10-s2",
                "title": "10.2 Custom `@field_validator` & Nested Models",
                "zero_assumption_note": "Built-in `Field` rules handle lengths and numbers—but what if you want to strip whitespace or reject blank `'   '` strings?",
                "definition": (
                    "- **`@field_validator`:** A custom Python check you attach to any field (for cleaning strings or checking custom business rules).\n"
                    "- **Nested Models:** Putting one `BaseModel` inside another (e.g., an `Order` containing a list of `OrderItem` models)."
                ),
                "syntax_box": {
                    "title": "Custom Field Validator + Nested Model",
                    "syntax": (
                        "from pydantic import BaseModel, field_validator\n\n"
                        "class Tag(BaseModel):\n"
                        "    name: str\n\n"
                        "    @field_validator('name')\n"
                        "    @classmethod\n"
                        "    def clean_name(cls, v: str) -> str:\n"
                        "        cleaned = v.strip().lower()\n"
                        "        if not cleaned:\n"
                        "            raise ValueError('name cannot be blank')\n"
                        "        return cleaned"
                    ),
                    "breakdown": [
                        "`@field_validator('name')` runs automatically whenever `Tag(name=...)` is created.",
                        "`@classmethod` is required by Pydantic v2 (`cls` is the `Tag` class, `v` is the incoming value).",
                        "Return the cleaned value (like `cleaned`), or `raise ValueError(...)` to fail validation.",
                    ],
                },
                "tiny_example": {
                    "title": "Nested Model Validating a Full Config",
                    "code": (
                        "from pydantic import BaseModel, Field\n\n"
                        "class ModelConfig(BaseModel):\n"
                        "    name: str\n"
                        "    temperature: float = Field(ge=0.0, le=2.0)\n\n"
                        "class AppSettings(BaseModel):\n"
                        "    app_name: str\n"
                        "    llm: ModelConfig\n\n"
                        "cfg = AppSettings(app_name='Tutor', llm={'name': 'qwen', 'temperature': 0.3})\n"
                        "print(cfg.llm.name, cfg.llm.temperature)"
                    ),
                    "line_by_line": [
                        "`AppSettings` accepts a nested dict for `llm` and automatically validates it into a `ModelConfig` object!",
                        "`cfg.llm.name` accesses nested fields with dot-notation and full type safety.",
                    ],
                },
                "body_markdown": (
                    "### Saving Validated Models Directly to JSON Files\n"
                    "`Path('config.json').write_text(cfg.model_dump_json(indent=2), encoding='utf-8')` saves nicely formatted JSON in 1 line, and `AppSettings.model_validate_json(...)` loads & re-validates it!"
                ),
                "code_example": {
                    "title": "Round-Trip Config Validation + File Save",
                    "code": (
                        "from pathlib import Path\n"
                        "import tempfile\n"
                        "from pydantic import BaseModel, Field, field_validator\n\n"
                        "class Note(BaseModel):\n"
                        "    title: str = Field(min_length=1)\n"
                        "    tags: list[str] = []\n\n"
                        "    @field_validator('title')\n"
                        "    @classmethod\n"
                        "    def strip_title(cls, v: str) -> str:\n"
                        "        s = v.strip()\n"
                        "        if not s:\n"
                        "            raise ValueError('Title cannot be blank')\n"
                        "        return s\n\n"
                        "with tempfile.TemporaryDirectory() as d:\n"
                        "    p = Path(d) / 'note.json'\n"
                        "    n = Note(title='  Learn Pydantic  ', tags=['ai'])\n"
                        "    p.write_text(n.model_dump_json(indent=2), encoding='utf-8')\n"
                        "    loaded = Note.model_validate_json(p.read_text(encoding='utf-8'))\n"
                        "    print(loaded)\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting `@classmethod` below `@field_validator(...)`.",
                    "Using mutable `tags: list[str] = []` in normal Python `def` vs Pydantic (in Pydantic `BaseModel`, `tags: list[str] = []` IS actually copied per instance safely, though `Field(default_factory=list)` is even cleaner!).",
                ],
                "key_takeaway": "Use `@field_validator` to normalize/reject custom values, and nest `BaseModel` classes for complex configs & API payloads.",
            },
        ],
        "quizzes": [
            {
                "id": "ch10-q1",
                "question": "How do you validate and parse a raw JSON string `raw` into a Pydantic `User` model in Pydantic v2?",
                "options": [
                    "User.model_validate_json(raw)",
                    "json.dump(User, raw)",
                    "User.to_json(raw)",
                    "open(raw)",
                ],
                "correct_index": 0,
                "explanation": "`Model.model_validate_json(raw)` parses JSON and enforces all Pydantic field rules in one step.",
            },
        ],
        "project": {
            "title": "Typed Dataset & Config Validator (`Pydantic`)",
            "workspace_dir": "projects/ch10_pydantic_validator",
            "overview": "Build nested Pydantic models with `@field_validator` to validate raw JSONL files, log bad rows, and save clean validated JSON.",
            "architecture_steps": [
                "Define nested Pydantic schemas with `Field` and `@field_validator`.",
                "Read raw JSONL records and separate valid objects from `ValidationError` rows.",
                "Write clean validated JSON output and verify with `pytest`.",
            ],
            "milestones": [
                {"id": "ch10-m1", "label": "Define Pydantic schemas with Field & @field_validator"},
                {"id": "ch10-m2", "label": "Validate file records catching ValidationError cleanly"},
                {"id": "ch10-m3", "label": "Save clean JSON & pass pytest"},
            ],
        },
    },

    # =========================================================================
    # CHAPTER 11: Requests (Dedicated Chapter BEFORE FastAPI!)
    # =========================================================================
    {
        "id": "ch11",
        "number": 11,
        "phase": 2,
        "phase_title": "Phase 2: AI Engineering Libraries (One Library Per Chapter)",
        "title": "Requests — Calling HTTP APIs & Web Automations",
        "subtitle": "GET vs POST, status codes (200/404/429), query params, headers & API keys, timeouts, try/except, and saving API data with Pydantic.",
        "status_type": "available",
        "estimated_hours": 5,
        "why_it_matters": (
            "Before you *build* your own web APIs with FastAPI, you should master *calling* web APIs with `requests`—fetching weather, "
            "news, GitHub data, or LLM endpoints, validating responses with Pydantic, and saving them to disk."
        ),
        "just_in_time_tags": ["requests", "GET & POST", "Status Codes", "Params & Headers", "Timeouts", "API + Pydantic"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch11-s1",
                "title": "11.1 How HTTP Works + `requests.get()` & `requests.post()`",
                "zero_assumption_note": "Every time your browser opens a webpage or an app talks to ChatGPT, it sends an HTTP request and gets back a status code + body.",
                "definition": (
                    "**`requests`** is Python's classic, human-friendly library for sending HTTP requests (`GET` to fetch data, `POST` to send data) and reading JSON replies."
                ),
                "syntax_box": {
                    "title": "Core `requests` Syntax (With Mandatory `timeout`!)",
                    "syntax": (
                        "import requests\n\n"
                        "# GET with query parameters (?q=python&limit=5):\n"
                        "resp = requests.get(\n"
                        "    'https://api.example.com/search',\n"
                        "    params={'q': 'python', 'limit': 5},\n"
                        "    headers={'Authorization': 'Bearer YOUR_TOKEN'},\n"
                        "    timeout=10,\n"
                        ")\n"
                        "resp.raise_for_status()   # raises error if status is 4xx or 5xx!\n"
                        "data = resp.json()        # parses JSON reply into Python dict/list"
                    ),
                    "breakdown": [
                        "`resp.status_code`: `200` = OK, `404` = Not Found, `401/403` = Bad API key, `429` = Rate Limited, `500` = Server Error.",
                        "`params={...}` safely builds URL query strings (`?q=python&limit=5`) for you.",
                        "`timeout=10`: **NEVER omit `timeout`**—otherwise a frozen server can hang your Python script forever!",
                        "`resp.raise_for_status()`: immediately turns 404/500 responses into a catchable Python error.",
                    ],
                },
                "tiny_example": {
                    "title": "Sending JSON With `requests.post(..., json=...)` (Local Test Server)",
                    "code": (
                        "import json, threading\n"
                        "from http.server import BaseHTTPRequestHandler, HTTPServer\n"
                        "import requests\n\n"
                        "# Tiny local fake server so this runs offline right here!\n"
                        "class EchoHandler(BaseHTTPRequestHandler):\n"
                        "    def do_POST(self):\n"
                        "        length = int(self.headers['Content-Length'])\n"
                        "        body = json.loads(self.rfile.read(length))\n"
                        "        self.send_response(200)\n"
                        "        self.send_header('Content-Type', 'application/json')\n"
                        "        self.end_headers()\n"
                        "        self.wfile.write(json.dumps({'echo': body['msg'].upper()}).encode())\n"
                        "    def log_message(self, *args): pass\n\n"
                        "srv = HTTPServer(('127.0.0.1', 0), EchoHandler)\n"
                        "threading.Thread(target=srv.handle_request, daemon=True).start()\n\n"
                        "url = f'http://127.0.0.1:{srv.server_port}/'\n"
                        "r = requests.post(url, json={'msg': 'hello api'}, timeout=5)\n"
                        "print(r.status_code, r.json())\n"
                        "srv.server_close()"
                    ),
                    "line_by_line": [
                        "Starts a tiny local HTTP server on an automatic free port (`port=0`).",
                        "`requests.post(url, json={'msg': 'hello api'}, timeout=5)` sends JSON automatically with the right headers.",
                        "Prints `200 {'echo': 'HELLO API'}`!",
                    ],
                },
                "body_markdown": (
                    "### Combining `requests` + `Pydantic` + Files (Real Automation!)\n"
                    "1. Fetch JSON from an endpoint with `requests.get(..., timeout=10)` inside `try / except requests.RequestException:`.\n"
                    "2. Validate the returned JSON with your **Chapter 10 Pydantic `BaseModel`**.\n"
                    "3. Save the clean data to disk with `Path.write_text(...)`!"
                ),
                "code_example": {
                    "title": "Safe API Fetcher With Error Handling",
                    "code": (
                        "import requests\n\n"
                        "def fetch_json_safe(url: str, timeout: float = 5.0) -> dict | None:\n"
                        "    try:\n"
                        "        resp = requests.get(url, timeout=timeout)\n"
                        "        resp.raise_for_status()\n"
                        "        return resp.json()\n"
                        "    except requests.RequestException as err:\n"
                        "        print('API request failed:', err)\n"
                        "        return None\n"
                    ),
                },
                "common_mistakes": [
                    "Calling `requests.get(url)` without `timeout=...` (can hang indefinitely).",
                    "Passing `data={'a': 1}` when an API expects JSON—always use `json={'a': 1}` for JSON APIs!",
                    "Hardcoding API keys instead of reading them via `os.getenv('API_KEY')`.",
                ],
                "key_takeaway": "Always pass `timeout=`, check `resp.raise_for_status()`, catch `requests.RequestException`, and validate `.json()` with Pydantic.",
            },
        ],
        "quizzes": [
            {
                "id": "ch11-q1",
                "question": "Why should you ALWAYS pass `timeout=10` (or similar) to `requests.get()` and `requests.post()`?",
                "options": [
                    "It makes responses return faster",
                    "Without a timeout, a slow or unreachable server can freeze your Python script forever",
                    "It automatically parses JSON",
                    "It enables HTTPS",
                ],
                "correct_index": 1,
                "explanation": "By default `requests` waits indefinitely for a response unless `timeout` is explicitly specified.",
            },
        ],
        "project": {
            "title": "API Data Fetcher, Pydantic Validator & JSON Archiver",
            "workspace_dir": "projects/ch11_requests_automator",
            "overview": "Fetch JSON records from an HTTP endpoint using `requests`, validate them with Pydantic, and save cleaned results to disk.",
            "architecture_steps": [
                "Write `fetch_json(url, timeout)` handling `RequestException` and non-200 statuses.",
                "Validate payloads with a Pydantic `BaseModel`.",
                "Save validated records to a JSON file and test against a local mock HTTP server.",
            ],
            "milestones": [
                {"id": "ch11-m1", "label": "Implement timeout-safe requests fetcher"},
                {"id": "ch11-m2", "label": "Validate API JSON responses with Pydantic"},
                {"id": "ch11-m3", "label": "Save results to JSON file & pass pytest"},
            ],
        },
    },

    # =========================================================================
    # CHAPTER 12: FastAPI (Single Framework Focus)
    # =========================================================================
    {
        "id": "ch12",
        "number": 12,
        "phase": 2,
        "phase_title": "Phase 2: AI Engineering Libraries (One Library Per Chapter)",
        "title": "FastAPI — Building Typed Web APIs & Microservices",
        "subtitle": "GET/POST routes, Pydantic request contracts, path/query params, TestClient, SSE streaming, and Gateway + Worker microservices.",
        "status_type": "available",
        "estimated_hours": 6,
        "why_it_matters": (
            "Now that you know **Pydantic** (Ch 10) and how clients call APIs with **`requests`** (Ch 11), `FastAPI` connects both: "
            "you build the server side that receives JSON, validates it with Pydantic, and streams answers back."
        ),
        "just_in_time_tags": ["FastAPI", "@app.get / @app.post", "Pydantic Contracts", "TestClient", "SSE Streaming", "Microservices"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch12-s1",
                "title": "12.1 FastAPI Routes, Pydantic Contracts & Microservices",
                "zero_assumption_note": "An API endpoint is just a Python function attached to a URL (`@app.post('/analyze')`) using your Chapter 10 Pydantic models.",
                "definition": (
                    "- **FastAPI:** Turns typed Python functions into fast HTTP APIs with automatic `/docs` swagger UI.\n"
                    "- **Microservice Split:** Keeping a lightweight **API Gateway** separate from heavy **Worker** processes connected by a queue."
                ),
                "syntax_box": {
                    "title": "FastAPI + Pydantic Schema Template",
                    "syntax": (
                        "from fastapi import FastAPI\n"
                        "from pydantic import BaseModel, Field\n\n"
                        "app = FastAPI()\n\n"
                        "class InputData(BaseModel):\n"
                        "    text: str = Field(min_length=1)\n\n"
                        "@app.post('/analyze')\n"
                        "def analyze(payload: InputData) -> dict:\n"
                        "    return {'length': len(payload.text)}"
                    ),
                    "breakdown": [
                        "`@app.post('/analyze')` links HTTP POST `/analyze` to `analyze`.",
                        "FastAPI automatically parses incoming JSON into `InputData` and returns `422` if invalid!",
                        "Use `def` for CPU/blocking work (runs in a threadpool); use `async def` when `await`-ing non-blocking I/O.",
                    ],
                },
                "tiny_example": {
                    "title": "Testing FastAPI Endpoints With `TestClient`",
                    "code": (
                        "from fastapi import FastAPI\n"
                        "from fastapi.testclient import TestClient\n\n"
                        "app = FastAPI()\n"
                        "@app.get('/ping')\n"
                        "def ping() -> dict:\n"
                        "    return {'ok': True}\n\n"
                        "client = TestClient(app)\n"
                        "resp = client.get('/ping')\n"
                        "print(resp.status_code, resp.json())"
                    ),
                    "line_by_line": [
                        "`TestClient(app)` tests your API in memory without starting uvicorn.",
                        "Prints `200 {'ok': True}`.",
                    ],
                },
                "body_markdown": (
                    "### Streaming Tokens (`SSE`) & Gateway-Worker Queues\n"
                    "`StreamingResponse` yields LLM tokens word-by-word as they generate, while slow batch jobs go onto a queue (`asyncio.Queue` / Redis) for background workers."
                ),
                "code_example": {
                    "title": "Streaming Words via Server-Sent Events (SSE)",
                    "code": (
                        "import asyncio\n"
                        "from fastapi import FastAPI\n"
                        "from fastapi.responses import StreamingResponse\n\n"
                        "app = FastAPI()\n\n"
                        "@app.get('/stream')\n"
                        "async def stream_words() -> StreamingResponse:\n"
                        "    async def token_generator():\n"
                        "        for word in ['AI', 'engineers', 'ship', 'systems.']:\n"
                        "            yield f'data: {word}\\n\\n'\n"
                        "            await asyncio.sleep(0.02)\n"
                        "    return StreamingResponse(token_generator(), media_type='text/event-stream')\n"
                    ),
                },
                "common_mistakes": [
                    "Running slow blocking CPU/PyTorch calls directly inside `async def` without `await` (freezes the server!).",
                ],
                "key_takeaway": "Validate payloads with Pydantic, test with `TestClient`, stream tokens via SSE, and offload heavy work to workers.",
            },
        ],
        "quizzes": [
            {
                "id": "ch12-q1",
                "question": "What HTTP status code does FastAPI automatically return when incoming JSON violates a Pydantic `Field` rule?",
                "options": ["200 OK", "404 Not Found", "422 Unprocessable Entity", "500 Internal Server Error"],
                "correct_index": 2,
                "explanation": "FastAPI validates incoming payloads against your Pydantic `BaseModel` and returns `422` with error details.",
            },
        ],
        "project": {
            "title": "Async Inference Gateway & Background Worker Microservice",
            "workspace_dir": "projects/ch12_inference_microservice",
            "overview": "Build a decoupled FastAPI Gateway + async background worker queue with `TestClient` tests.",
            "architecture_steps": [
                "Define shared Pydantic schemas.",
                "Build Gateway endpoints + SSE stream.",
                "Build async worker loop and test with `TestClient`.",
            ],
            "milestones": [
                {"id": "ch12-m1", "label": "Create Pydantic contracts"},
                {"id": "ch12-m2", "label": "Build FastAPI gateway + SSE endpoint"},
                {"id": "ch12-m3", "label": "Build async worker & pass TestClient pytest"},
            ],
        },
    },

    # =========================================================================
    # CHAPTER 13: FastMCP (`mcp`) — Dedicated Chapter for MCP Tools & Servers
    # =========================================================================
    {
        "id": "ch13",
        "number": 13,
        "phase": 2,
        "phase_title": "Phase 2: AI Engineering Libraries (One Library Per Chapter)",
        "title": "FastMCP (`mcp`) — Giving AI Agents Real Tools & Resources",
        "subtitle": "What MCP is, creating an MCP server, @mcp.tool(), @mcp.resource(), Pydantic-typed tool inputs, and testing tool calls in Python.",
        "status_type": "available",
        "estimated_hours": 5,
        "why_it_matters": (
            "Modern AI assistants (Claude, Cursor, Antigravity, custom agents) use **MCP (Model Context Protocol)** to safely read your files, "
            "query databases, and run automations. FastMCP lets you expose any Python function to an AI agent in 10 lines!"
        ),
        "just_in_time_tags": ["FastMCP / MCPServer", "@mcp.tool()", "@mcp.resource()", "Agent Tools", "Structured Output"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch13-s1",
                "title": "13.1 What Is MCP? + Building Your First Tool With `@mcp.tool()`",
                "zero_assumption_note": (
                    "Note on imports: in `mcp` v1.x or the standalone `fastmcp` package, you import `from fastmcp import FastMCP`. "
                    "In the official `mcp` v2.0 SDK installed on this computer, it is named `MCPServer` (`from mcp.server.mcpserver import MCPServer`)—with the exact same decorators!"
                ),
                "definition": (
                    "**MCP (Model Context Protocol)** is a standard USB-C port for AI models: instead of writing custom glue code for every AI app, "
                    "you build **one MCP server** exposing `@mcp.tool()` actions and `@mcp.resource()` read-only data, and any MCP-compatible AI can use it."
                ),
                "syntax_box": {
                    "title": "Creating an MCP Server With Tools & Resources",
                    "syntax": (
                        "from mcp.server.mcpserver import MCPServer  # (or `FastMCP` in fastmcp pkg)\n\n"
                        "mcp = MCPServer('my-assistant-tools')\n\n"
                        "@mcp.tool()\n"
                        "def add_numbers(a: int, b: int) -> int:\n"
                        "    \"\"\"Add two integers together.\"\"\"\n"
                        "    return a + b\n\n"
                        "@mcp.resource('info://version')\n"
                        "def get_version() -> str:\n"
                        "    return '1.0.0'"
                    ),
                    "breakdown": [
                        "`@mcp.tool()` turns a typed Python function into an action an AI agent can call! **Always write a clear docstring**—the AI reads that docstring to know *when* to call your tool.",
                        "`@mcp.resource('uri://...')` exposes read-only data (like config files or logs) by URI.",
                        "`mcp.run()` starts the server over stdio so AI hosts (Cursor, Claude Desktop, Antigravity) can talk to it.",
                    ],
                },
                "tiny_example": {
                    "title": "Registering & Calling an MCP Tool in Python",
                    "code": (
                        "import asyncio\n"
                        "from mcp.server.mcpserver import MCPServer\n\n"
                        "mcp = MCPServer('word-tools')\n\n"
                        "@mcp.tool()\n"
                        "def count_words(text: str) -> int:\n"
                        "    \"\"\"Count whitespace-separated words in text.\"\"\"\n"
                        "    return len(text.split())\n\n"
                        "tools = asyncio.run(mcp.list_tools())\n"
                        "result = asyncio.run(mcp.call_tool('count_words', {'text': 'hello mcp world'}))\n"
                        "print('Registered:', [t.name for t in tools])\n"
                        "print('Result:', result.structured_content)"
                    ),
                    "line_by_line": [
                        "Creates an `MCPServer` named `'word-tools'`.",
                        "`@mcp.tool()` automatically inspects `text: str -> int` and builds a JSON schema for the AI.",
                        "`mcp.list_tools()` shows `['count_words']`, and `mcp.call_tool(...)` runs it and returns `{'result': 3}`!",
                    ],
                },
                "body_markdown": (
                    "### Connecting Files & Automations Into MCP Tools\n"
                    "Think about everything you built in Chapters 2, 3, 10, and 11 (`open`/`Path` file reading, `os` folder inspection, `Pydantic` validation, `requests` API calls): "
                    "wrapping those functions with `@mcp.tool()` immediately turns them into safe tools an AI assistant can call!"
                ),
                "code_example": {
                    "title": "File-Reading & Note-Saving MCP Tool Server",
                    "code": (
                        "import asyncio, tempfile\n"
                        "from pathlib import Path\n"
                        "from mcp.server.mcpserver import MCPServer\n\n"
                        "mcp = MCPServer('notes-server')\n\n"
                        "with tempfile.TemporaryDirectory() as tmp:\n"
                        "    notes_dir = Path(tmp)\n\n"
                        "    @mcp.tool()\n"
                        "    def save_note(filename: str, body: str) -> str:\n"
                        "        \"\"\"Save a plain text note safely inside notes_dir.\"\"\"\n"
                        "        safe_name = Path(filename).name  # prevents ../ path traversal!\n"
                        "        target = notes_dir / safe_name\n"
                        "        target.write_text(body, encoding='utf-8')\n"
                        "        return f'Saved {safe_name}'\n\n"
                        "    @mcp.resource('notes://list')\n"
                        "    def list_notes() -> str:\n"
                        "        return ', '.join(p.name for p in notes_dir.glob('*.txt'))\n\n"
                        "    res = asyncio.run(mcp.call_tool('save_note', {'filename': 'todo.txt', 'body': 'Learn MCP'}))\n"
                        "    listing = asyncio.run(mcp.read_resource('notes://list'))\n"
                        "    print(res.structured_content, '| Notes:', listing[0].content)\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting type hints or docstrings on `@mcp.tool()` functions (the AI won't know what arguments to pass or when to use the tool!).",
                    "Using raw user-supplied `filename` without `Path(filename).name` (lets a caller pass `../../secret.txt`!).",
                ],
                "key_takeaway": "Type hints + clear docstrings + `@mcp.tool()` turn any safe Python file/API automation into a standard AI-agent tool.",
            },
        ],
        "quizzes": [
            {
                "id": "ch13-q1",
                "question": "Why are Python type hints (`a: int`) and docstrings especially important on `@mcp.tool()` functions?",
                "options": [
                    "Python won't compile without docstrings",
                    "MCP uses type hints to generate the JSON input schema, and the AI reads the docstring to understand when and how to call the tool",
                    "They make the tool run on GPU",
                    "They encrypt network traffic",
                ],
                "correct_index": 1,
                "explanation": "AI models rely on the tool schema (from type hints) and description (from the docstring) to choose and call tools accurately.",
            },
        ],
        "project": {
            "title": "Local Workspace Notes & Search MCP Server",
            "workspace_dir": "projects/ch13_fastmcp_server",
            "overview": "Build a real MCP server exposing `@mcp.tool()` note-saving/searching functions and `@mcp.resource()` file listings with path-traversal safety.",
            "architecture_steps": [
                "Create `MCPServer('workspace-notes')`.",
                "Implement `@mcp.tool()` functions to save and search `.txt` notes safely.",
                "Implement `@mcp.resource()` listing available notes and verify with `pytest`.",
            ],
            "milestones": [
                {"id": "ch13-m1", "label": "Create MCPServer with typed @mcp.tool() functions"},
                {"id": "ch13-m2", "label": "Add @mcp.resource() & path-traversal filename guard"},
                {"id": "ch13-m3", "label": "Verify tool calls & resources with pytest"},
            ],
        },
    },

    # =========================================================================
    # CHAPTER 14: Docker (Single Tool Focus)
    # =========================================================================
    {
        "id": "ch14",
        "number": 14,
        "phase": 2,
        "phase_title": "Phase 2: AI Engineering Libraries (One Library Per Chapter)",
        "title": "Docker — Reproducible Containers & Multi-Service Stacks",
        "subtitle": "Images vs containers, Dockerfile syntax, layer caching, docker-compose networking, and GPU passthrough.",
        "status_type": "available",
        "estimated_hours": 4,
        "why_it_matters": (
            "AI stacks break when Python versions, C++ libraries, or CUDA drivers differ between your PC and a server. "
            "Docker packages the exact OS, Python, and libraries into one portable container."
        ),
        "just_in_time_tags": ["Docker", "Dockerfile", "Layer Caching", "docker-compose", ".dockerignore"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch14-s1",
                "title": "14.1 `Dockerfile` Syntax, Layer Caching & `docker-compose`",
                "zero_assumption_note": "Note: Docker isn't installed on this PC yet—install Docker Desktop for Windows (WSL 2) when ready to run containers locally.",
                "definition": (
                    "- **Dockerfile:** A recipe listing what OS, Python packages, and code to install.\n"
                    "- **Image:** The read-only snapshot built from a Dockerfile.\n"
                    "- **Container:** A live running instance of an image."
                ),
                "syntax_box": {
                    "title": "Standard Python Dockerfile Instructions",
                    "syntax": (
                        "FROM python:3.12-slim                  # 1. Pin base version!\n"
                        "WORKDIR /app                           # 2. Folder inside container\n"
                        "COPY requirements.txt .                # 3. Copy dependencies FIRST\n"
                        "RUN pip install --no-cache-dir -r requirements.txt  # 4. Cached!\n"
                        "COPY app/ ./app/                       # 5. Copy your code LAST\n"
                        "CMD [\"uvicorn\", \"app.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]"
                    ),
                    "breakdown": [
                        "`FROM`: never use `:latest` (pin `3.12-slim` so builds stay predictable).",
                        "`COPY requirements.txt` *before* `COPY app/`: keeps `pip install` cached when you only edit `.py` code.",
                        "`0.0.0.0`: required inside containers so connections from outside reach your API.",
                    ],
                },
                "tiny_example": {
                    "title": "Connecting Two Services in `docker-compose.yml`",
                    "code": (
                        "services:\n"
                        "  redis:\n"
                        "    image: redis:7-alpine\n"
                        "  gateway:\n"
                        "    build: ./gateway\n"
                        "    ports:\n"
                        "      - '8000:8000'\n"
                        "    depends_on:\n"
                        "      - redis"
                    ),
                    "line_by_line": [
                        "`services:` launches every container together via `docker compose up`.",
                        "Inside `gateway`, code connects to `redis://redis:6379` (using the service name `redis`, NOT `localhost`!).",
                    ],
                },
                "body_markdown": (
                    "### Always Include a `.dockerignore` File\n"
                    "Listing `.venv`, `__pycache__`, and large `.pt` model files in `.dockerignore` keeps Docker images fast and lean."
                ),
                "code_example": {
                    "title": "Sample `.dockerignore`",
                    "code": (
                        ".venv/\n"
                        "__pycache__/\n"
                        "*.db\n"
                        ".git/\n"
                    ),
                },
                "common_mistakes": [
                    "Putting `COPY . .` *above* `RUN pip install` (breaks caching on every code edit!).",
                    "Using `localhost` inside container A to reach container B.",
                ],
                "key_takeaway": "Pin base tags, copy `requirements.txt` before source code, add `.dockerignore`, and talk between compose services by service name.",
            },
        ],
        "quizzes": [
            {
                "id": "ch14-q1",
                "question": "Inside a `docker-compose` network, how should the `gateway` container call the `worker` container?",
                "options": [
                    "http://localhost:8001",
                    "http://worker:8001 (using the Compose service name)",
                    "http://127.0.0.1:8001",
                    "Containers cannot talk to each other",
                ],
                "correct_index": 1,
                "explanation": "Each container has its own `localhost`; Docker Compose resolves containers by service name (`worker`).",
            },
        ],
        "project": {
            "title": "Containerized Microservice Stack (API + Worker)",
            "workspace_dir": "projects/ch14_dockerized_stack",
            "overview": "Package the Chapter 12 Gateway and Worker with `.dockerignore`, layer-cached Dockerfiles, and `docker-compose.yml`.",
            "architecture_steps": [
                "Install Docker Desktop for Windows (WSL 2).",
                "Write `.dockerignore` and layer-cached `Dockerfile` files.",
                "Create `docker-compose.yml` with healthchecks and service networking.",
            ],
            "milestones": [
                {"id": "ch14-m1", "label": "Create .dockerignore & layer-cached Dockerfiles"},
                {"id": "ch14-m2", "label": "Write docker-compose.yml with healthchecks"},
                {"id": "ch14-m3", "label": "Validate stack build in Docker Desktop"},
            ],
        },
    },
]
