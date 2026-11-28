"""Phase 2 Practice Workbook (Chapters 8-14): NumPy, Pandas, Pydantic, Requests, FastAPI, FastMCP, Docker."""

from __future__ import annotations

from typing import Any

PHASE_2_WORKBOOK: list[dict[str, Any]] = [
    # ---------------- CHAPTER 8: NumPy ----------------
    {
        "id": "wb-08-01",
        "chapter_id": "ch08",
        "number": "8.1",
        "title": "Vectorized Standardization (Broadcasting + `axis`)",
        "topic": "NumPy",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Standardize feature columns to mean 0 and std 1 safely without loops.",
        "prompt_markdown": "Write `standardize_columns(x: np.ndarray) -> np.ndarray` for `(N, D)` replacing zero std with `1.0`.",
        "thinking_blueprint": ["Column stats with `axis=0, keepdims=True`.", "Guard zero std with `np.where`."],
        "hints": ["`keepdims=True` makes `(1, D)` broadcast across `(N, D)` cleanly."],
        "dry_run_trace": "`[[1, 5], [3, 5]]` -> `[[-1, 0], [1, 0]]`.",
        "starter_code": "import numpy as np\n\ndef standardize_columns(x: np.ndarray) -> np.ndarray:\n    pass\n",
        "solution_code": (
            "import numpy as np\n\n"
            "def standardize_columns(x: np.ndarray) -> np.ndarray:\n"
            "    x = np.asarray(x, dtype=float)\n"
            "    mean = x.mean(axis=0, keepdims=True)\n"
            "    std = x.std(axis=0, keepdims=True)\n"
            "    safe_std = np.where(std == 0, 1.0, std)\n"
            "    return (x - mean) / safe_std\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Column reduction (`keepdims=True`), zero-std guard, and broadcasted division.",
        "test_cases": [
            {"name": "std", "code": "import numpy as np\nx = np.array([[1.0, 5.0], [3.0, 5.0]])\nassert np.allclose(sol.standardize_columns(x), np.array([[-1.0, 0.0], [1.0, 0.0]]))"},
        ],
    },
    {
        "id": "wb-08-02",
        "chapter_id": "ch08",
        "number": "8.2",
        "title": "Numerically Stable Softmax",
        "topic": "NumPy",
        "question_type": "Logic & Coding",
        "difficulty": "Intermediate",
        "summary": "Implement row-wise softmax along `axis=-1` safe against overflow.",
        "prompt_markdown": "Write `stable_softmax(logits: np.ndarray) -> np.ndarray` for 1D or 2D inputs.",
        "thinking_blueprint": ["Subtract `np.max(..., axis=-1, keepdims=True)` before `np.exp`."],
        "hints": ["`axis=-1` always targets the last dimension."],
        "dry_run_trace": "`[1000.0, 1000.0]` -> `[0.5, 0.5]`.",
        "starter_code": "import numpy as np\n\ndef stable_softmax(logits: np.ndarray) -> np.ndarray:\n    pass\n",
        "solution_code": (
            "import numpy as np\n\n"
            "def stable_softmax(logits: np.ndarray) -> np.ndarray:\n"
            "    logits = np.asarray(logits, dtype=float)\n"
            "    shifted = logits - np.max(logits, axis=-1, keepdims=True)\n"
            "    exps = np.exp(shifted)\n"
            "    return exps / np.sum(exps, axis=-1, keepdims=True)\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Max-shift prevents `exp` overflow while leaving probabilities unchanged.",
        "test_cases": [
            {"name": "softmax", "code": "import numpy as np\nassert np.allclose(sol.stable_softmax(np.array([1000.0, 1000.0])), [0.5, 0.5])"},
        ],
    },
    {
        "id": "wb-08-03",
        "chapter_id": "ch08",
        "number": "8.3",
        "title": "Cosine Top-K Vector Retrieval",
        "topic": "NumPy",
        "question_type": "Logic & Coding",
        "difficulty": "Intermediate",
        "summary": "Rank document embeddings by cosine similarity in NumPy.",
        "prompt_markdown": "Write `cosine_top_k(docs: np.ndarray, query: np.ndarray, k: int) -> list[int]`.",
        "thinking_blueprint": ["Unit-normalize rows & query, then `docs_unit @ q_unit`."],
        "hints": ["`np.argsort(sims)[::-1][:k].tolist()`"],
        "dry_run_trace": "`[[1,0],[0,1],[1,1]]` with `[2,0]` -> `[0, 2]`.",
        "starter_code": "import numpy as np\n\ndef cosine_top_k(docs: np.ndarray, query: np.ndarray, k: int) -> list[int]:\n    pass\n",
        "solution_code": (
            "import numpy as np\n\n"
            "def cosine_top_k(docs: np.ndarray, query: np.ndarray, k: int) -> list[int]:\n"
            "    if k <= 0 or len(docs) == 0:\n"
            "        return []\n"
            "    docs = np.asarray(docs, dtype=float)\n"
            "    query = np.asarray(query, dtype=float)\n"
            "    doc_norms = np.maximum(np.linalg.norm(docs, axis=1, keepdims=True), 1e-12)\n"
            "    q_norm = max(float(np.linalg.norm(query)), 1e-12)\n"
            "    sims = (docs / doc_norms) @ (query / q_norm)\n"
            "    return np.argsort(sims)[::-1][:k].tolist()\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** L2 normalization + matrix-vector dot product + descending argsort.",
        "test_cases": [
            {"name": "topk", "code": "import numpy as np\ndocs = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])\nassert sol.cosine_top_k(docs, np.array([2.0, 0.0]), 2) == [0, 2]"},
        ],
    },

    # ---------------- CHAPTER 9: Pandas ----------------
    {
        "id": "wb-09-01",
        "chapter_id": "ch09",
        "number": "9.1",
        "title": "Pandas Text Cleaning & Deduplication",
        "topic": "Pandas",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Drop nulls, collapse whitespace, filter `min_len`, and deduplicate keeping highest `'score'`.",
        "prompt_markdown": "Write `clean_corpus(df: pd.DataFrame, min_len: int = 10) -> pd.DataFrame` sorted by `'id'`.",
        "thinking_blueprint": ["Drop nulls + `.copy()`, normalize spaces, sort by `'score'` desc before `drop_duplicates`."],
        "hints": ["Reset index cleanly with `.reset_index(drop=True)`."],
        "dry_run_trace": "Duplicate normalized texts retain the higher `'score'` row.",
        "starter_code": "import pandas as pd\n\ndef clean_corpus(df: pd.DataFrame, min_len: int = 10) -> pd.DataFrame:\n    pass\n",
        "solution_code": (
            "import pandas as pd\n\n"
            "def clean_corpus(df: pd.DataFrame, min_len: int = 10) -> pd.DataFrame:\n"
            "    out = df.dropna(subset=['text']).copy()\n"
            "    out['clean_text'] = out['text'].astype(str).str.split().str.join(' ')\n"
            "    out = out[out['clean_text'].str.len() >= min_len].copy()\n"
            "    out['_norm'] = out['clean_text'].str.lower()\n"
            "    out = out.sort_values('score', ascending=False).drop_duplicates(subset=['_norm'], keep='first')\n"
            "    return out.drop(columns=['_norm']).sort_values('id').reset_index(drop=True)\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Null filter, normalized dedup key, score-prioritized deduplication.",
        "test_cases": [
            {
                "name": "dedup",
                "code": (
                    "import pandas as pd\n"
                    "df = pd.DataFrame([{'id': 1, 'text': '  Hello   AI world  ', 'score': 0.5}, {'id': 2, 'text': None, 'score': 0.9}, {'id': 4, 'text': 'hello ai world', 'score': 0.95}])\n"
                    "res = sol.clean_corpus(df, min_len=10)\nassert list(res['id']) == [4]"
                ),
            },
        ],
    },
    {
        "id": "wb-09-02",
        "chapter_id": "ch09",
        "number": "9.2",
        "title": "GroupBy Quality Metrics per Dataset Source",
        "topic": "Pandas",
        "question_type": "Logic & Coding",
        "difficulty": "Intermediate",
        "summary": "Aggregate total rows, valid count, and average tokens per source.",
        "prompt_markdown": "Write `summarize_sources(df: pd.DataFrame) -> pd.DataFrame` returning `['source', 'total_rows', 'valid_rows', 'avg_tokens']`.",
        "thinking_blueprint": ["Use `.groupby('source', as_index=False).agg(...)`."],
        "hints": ["Cast `valid_rows` to `int`."],
        "dry_run_trace": "`wiki` `[100, 200]` -> `total_rows=2, avg_tokens=150.0`.",
        "starter_code": "import pandas as pd\n\ndef summarize_sources(df: pd.DataFrame) -> pd.DataFrame:\n    pass\n",
        "solution_code": (
            "import pandas as pd\n\n"
            "def summarize_sources(df: pd.DataFrame) -> pd.DataFrame:\n"
            "    summary = (\n"
            "        df.groupby('source', as_index=False)\n"
            "        .agg(total_rows=('tokens', 'count'), valid_rows=('is_valid', 'sum'), avg_tokens=('tokens', 'mean'))\n"
            "        .sort_values('source')\n"
            "        .reset_index(drop=True)\n"
            "    )\n"
            "    summary['valid_rows'] = summary['valid_rows'].astype(int)\n"
            "    return summary\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Named aggregations produce clean flat columns directly.",
        "test_cases": [
            {
                "name": "summary",
                "code": (
                    "import pandas as pd\n"
                    "df = pd.DataFrame([{'source': 'wiki', 'tokens': 100, 'is_valid': True}, {'source': 'wiki', 'tokens': 200, 'is_valid': False}, {'source': 'arxiv', 'tokens': 300, 'is_valid': True}])\n"
                    "res = sol.summarize_sources(df)\nassert list(res['source']) == ['arxiv', 'wiki'] and res.loc[1, 'valid_rows'] == 1"
                ),
            },
        ],
    },

    # ---------------- CHAPTER 10: Pydantic (Dedicated!) ----------------
    {
        "id": "wb-10-01",
        "chapter_id": "ch10",
        "number": "10.1",
        "title": "Pydantic `BaseModel` & `@field_validator`",
        "topic": "Pydantic",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Validate and clean user-submitted records with `BaseModel`, `Field`, and `@field_validator`.",
        "prompt_markdown": (
            "Create `class Article(BaseModel)` with:\n"
            "- `title: str` (stripped; raise `ValueError` if blank or length < 3 after stripping)\n"
            "- `views: int = Field(default=0, ge=0)`\n"
            "- `tags: list[str] = Field(default_factory=list)`"
        ),
        "thinking_blueprint": [
            "Use `@field_validator('title')` + `@classmethod` to strip whitespace and check `len(cleaned) < 3`.",
        ],
        "hints": [
            "Check length *after* stripping inside the validator so `'  a '` is rejected cleanly.",
        ],
        "dry_run_trace": "`Article(title='  Learn Pydantic ', views='12')` -> `title='Learn Pydantic'`, `views=12`.",
        "starter_code": (
            "from pydantic import BaseModel, Field, field_validator\n\n"
            "class Article(BaseModel):\n"
            "    # TODO: define title, views, tags and strip/validate title\n"
            "    pass\n\n"
            "if __name__ == '__main__':\n"
            "    print(Article(title='  Learn Pydantic ', views='12'))\n"
        ),
        "solution_code": (
            "from pydantic import BaseModel, Field, field_validator\n\n"
            "class Article(BaseModel):\n"
            "    title: str\n"
            "    views: int = Field(default=0, ge=0)\n"
            "    tags: list[str] = Field(default_factory=list)\n\n"
            "    @field_validator('title')\n"
            "    @classmethod\n"
            "    def validate_title(cls, v: str) -> str:\n"
            "        cleaned = v.strip()\n"
            "        if len(cleaned) < 3:\n"
            "            raise ValueError('title must have at least 3 characters')\n"
            "        return cleaned\n\n"
            "if __name__ == '__main__':\n"
            "    print(Article(title='  Learn Pydantic ', views='12'))\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Pydantic auto-coerces `'12' -> 12` while `@field_validator` cleans and guards string rules.",
        "test_cases": [
            {
                "name": "valid_and_invalid_article",
                "code": (
                    "from pydantic import ValidationError\n"
                    "a = sol.Article(title='  Learn Pydantic ', views='12')\n"
                    "assert a.title == 'Learn Pydantic' and a.views == 12 and a.tags == []\n"
                    "for bad in [{'title': '  '}, {'title': 'hi'}, {'title': 'Valid', 'views': -1}]:\n"
                    "    try:\n        sol.Article(**bad)\n        assert False\n    except ValidationError:\n        pass"
                ),
            },
        ],
    },
    {
        "id": "wb-10-02",
        "chapter_id": "ch10",
        "number": "10.2",
        "title": "Pydantic Batch Filter Over Messy JSON Records",
        "topic": "Pydantic",
        "question_type": "Logic & Coding",
        "difficulty": "Intermediate",
        "summary": "Use nested Pydantic models and `ValidationError` to separate valid records from corrupt rows.",
        "prompt_markdown": (
            "Define `PromptItem(BaseModel)` (`prompt: str` min_length=3, `score: int` `1..5`) and "
            "`filter_valid_prompts(rows: list[dict]) -> list[PromptItem]` returning only rows that pass validation."
        ),
        "thinking_blueprint": ["Loop over `rows`, call `PromptItem.model_validate(row)` inside `try / except ValidationError:`."],
        "hints": ["Import `ValidationError` from `pydantic`."],
        "dry_run_trace": "Invalid rows raise `ValidationError` and are skipped cleanly.",
        "starter_code": (
            "from pydantic import BaseModel, Field, ValidationError\n\n"
            "class PromptItem(BaseModel):\n"
            "    prompt: str = Field(min_length=3)\n"
            "    score: int = Field(ge=1, le=5)\n\n"
            "def filter_valid_prompts(rows: list[dict]) -> list[PromptItem]:\n"
            "    # TODO: validate each row and keep valid PromptItem objects\n"
            "    pass\n"
        ),
        "solution_code": (
            "from pydantic import BaseModel, Field, ValidationError\n\n"
            "class PromptItem(BaseModel):\n"
            "    prompt: str = Field(min_length=3)\n"
            "    score: int = Field(ge=1, le=5)\n\n"
            "def filter_valid_prompts(rows: list[dict]) -> list[PromptItem]:\n"
            "    valid: list[PromptItem] = []\n"
            "    for row in rows:\n"
            "        try:\n"
            "            valid.append(PromptItem.model_validate(row))\n"
            "        except ValidationError:\n"
            "            continue\n"
            "    return valid\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** `model_validate` + `ValidationError` cleanly separates good training data from bad rows.",
        "test_cases": [
            {
                "name": "batch_filter",
                "code": (
                    "rows = [{'prompt': 'Explain AI', 'score': 5}, {'prompt': 'No', 'score': 5}, {'prompt': 'Good prompt', 'score': 9}]\n"
                    "out = sol.filter_valid_prompts(rows)\nassert len(out) == 1 and out[0].prompt == 'Explain AI'"
                ),
            },
        ],
    },

    # ---------------- CHAPTER 11: Requests (Dedicated!) ----------------
    {
        "id": "wb-11-01",
        "chapter_id": "ch11",
        "number": "11.1",
        "title": "Safe HTTP Fetcher With `requests` & Timeout",
        "topic": "Requests",
        "question_type": "Systems",
        "difficulty": "Foundation",
        "summary": "Fetch JSON from an HTTP URL handling non-200 status codes and network errors gracefully.",
        "prompt_markdown": (
            "Write `fetch_json_safe(url: str, timeout: float = 3.0) -> dict | None` using `requests.get(url, timeout=timeout)`, "
            "calling `resp.raise_for_status()`, returning `resp.json()`, or returning `None` on `requests.RequestException`."
        ),
        "thinking_blueprint": ["Wrap `requests.get`, `raise_for_status()`, and `.json()` inside `try / except requests.RequestException:`."],
        "hints": ["Always pass `timeout=timeout`."],
        "dry_run_trace": "HTTP 200 -> parsed dict; HTTP 404 or connection failure -> `None`.",
        "starter_code": (
            "import requests\n\n"
            "def fetch_json_safe(url: str, timeout: float = 3.0):\n"
            "    # TODO: GET url with timeout, raise_for_status, return json or None on RequestException\n"
            "    pass\n"
        ),
        "solution_code": (
            "import requests\n\n"
            "def fetch_json_safe(url: str, timeout: float = 3.0):\n"
            "    try:\n"
            "        resp = requests.get(url, timeout=timeout)\n"
            "        resp.raise_for_status()\n"
            "        return resp.json()\n"
            "    except requests.RequestException:\n"
            "        return None\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** `timeout` avoids infinite hangs, `raise_for_status()` catches 4xx/5xx errors, and `RequestException` handles both HTTP and connection errors.",
        "test_cases": [
            {
                "name": "local_http_200_and_404",
                "code": (
                    "import json, threading\nfrom http.server import BaseHTTPRequestHandler, HTTPServer\n"
                    "class H(BaseHTTPRequestHandler):\n"
                    "    def do_GET(self):\n"
                    "        if self.path == '/ok':\n"
                    "            self.send_response(200); self.send_header('Content-Type', 'application/json'); self.end_headers()\n"
                    "            self.wfile.write(json.dumps({'status': 'ready'}).encode())\n"
                    "        else:\n"
                    "            self.send_response(404); self.end_headers()\n"
                    "    def log_message(self, *a): pass\n"
                    "srv = HTTPServer(('127.0.0.1', 0), H)\n"
                    "t = threading.Thread(target=lambda: [srv.handle_request(), srv.handle_request()], daemon=True); t.start()\n"
                    "assert sol.fetch_json_safe(f'http://127.0.0.1:{srv.server_port}/ok') == {'status': 'ready'}\n"
                    "assert sol.fetch_json_safe(f'http://127.0.0.1:{srv.server_port}/missing') is None\n"
                    "srv.server_close()"
                ),
            },
        ],
    },
    {
        "id": "wb-11-02",
        "chapter_id": "ch11",
        "number": "11.2",
        "title": "Automation: Fetch API + Validate With Pydantic + Save JSON",
        "topic": "Requests",
        "question_type": "Systems",
        "difficulty": "Intermediate",
        "summary": "Combine `requests` + `Pydantic` + `Path` file saving into a real data-fetching automation.",
        "prompt_markdown": (
            "Given `ApiNote(BaseModel)` (`id: int`, `text: str` min_length=1), write `sync_api_note(url: str, out_path: Path) -> bool` "
            "that fetches JSON via `requests.get(url, timeout=3.0)`, validates it as `ApiNote`, saves `.model_dump_json()` to `out_path` (creating parents), and returns `True` (or `False` on network/validation failure)."
        ),
        "thinking_blueprint": ["Fetch -> validate with `ApiNote.model_validate(...)` -> `out_path.parent.mkdir(...)` -> `write_text`."],
        "hints": ["Catch `(requests.RequestException, ValidationError)`."],
        "dry_run_trace": "Valid API reply -> saved to `out_path` -> `True`; bad JSON -> `False`.",
        "starter_code": (
            "from pathlib import Path\n"
            "import requests\n"
            "from pydantic import BaseModel, Field, ValidationError\n\n"
            "class ApiNote(BaseModel):\n"
            "    id: int\n"
            "    text: str = Field(min_length=1)\n\n"
            "def sync_api_note(url: str, out_path: Path) -> bool:\n"
            "    # TODO: fetch -> validate -> save JSON\n"
            "    pass\n"
        ),
        "solution_code": (
            "from pathlib import Path\n"
            "import requests\n"
            "from pydantic import BaseModel, Field, ValidationError\n\n"
            "class ApiNote(BaseModel):\n"
            "    id: int\n"
            "    text: str = Field(min_length=1)\n\n"
            "def sync_api_note(url: str, out_path: Path) -> bool:\n"
            "    try:\n"
            "        resp = requests.get(url, timeout=3.0)\n"
            "        resp.raise_for_status()\n"
            "        note = ApiNote.model_validate(resp.json())\n"
            "    except (requests.RequestException, ValidationError, ValueError):\n"
            "        return False\n"
            "    out_path.parent.mkdir(parents=True, exist_ok=True)\n"
            "    out_path.write_text(note.model_dump_json(indent=2), encoding='utf-8')\n"
            "    return True\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Fetch -> Validate -> Save is the core pattern of every reliable API ingestion automation.",
        "test_cases": [
            {
                "name": "fetch_validate_save",
                "code": (
                    "import json, tempfile, threading\nfrom pathlib import Path\nfrom http.server import BaseHTTPRequestHandler, HTTPServer\n"
                    "class H(BaseHTTPRequestHandler):\n"
                    "    def do_GET(self):\n"
                    "        self.send_response(200); self.send_header('Content-Type', 'application/json'); self.end_headers()\n"
                    "        payload = {'id': 7, 'text': 'Saved note'} if self.path == '/good' else {'id': 'x', 'text': ''}\n"
                    "        self.wfile.write(json.dumps(payload).encode())\n"
                    "    def log_message(self, *a): pass\n"
                    "srv = HTTPServer(('127.0.0.1', 0), H)\n"
                    "t = threading.Thread(target=lambda: [srv.handle_request(), srv.handle_request()], daemon=True); t.start()\n"
                    "with tempfile.TemporaryDirectory() as d:\n"
                    "    out = Path(d) / 'sub' / 'note.json'\n"
                    "    assert sol.sync_api_note(f'http://127.0.0.1:{srv.server_port}/good', out) is True\n"
                    "    assert json.loads(out.read_text(encoding='utf-8'))['id'] == 7\n"
                    "    assert sol.sync_api_note(f'http://127.0.0.1:{srv.server_port}/bad', out) is False\n"
                    "srv.server_close()"
                ),
            },
        ],
    },

    # ---------------- CHAPTER 12: FastAPI & Microservices ----------------
    {
        "id": "wb-12-01",
        "chapter_id": "ch12",
        "number": "12.1",
        "title": "Pydantic Contract & FastAPI `/tokenize` Endpoint",
        "topic": "FastAPI",
        "question_type": "Systems",
        "difficulty": "Foundation",
        "summary": "Build a validated FastAPI POST endpoint rejecting blank inputs with HTTP 422.",
        "prompt_markdown": "Build `app = FastAPI()` with `POST /tokenize` accepting `{'text': str, 'lowercase': bool = True}` and returning `{'tokens': list[str], 'count': int}`.",
        "thinking_blueprint": ["Pydantic `BaseModel` with `@field_validator` rejecting blank text.", "Route splits words and returns dict."],
        "hints": ["Raise `ValueError` inside `@field_validator` for automatic 422."],
        "dry_run_trace": "`{'text': 'Hello AI'}` -> `200 {'tokens': ['hello', 'ai'], 'count': 2}`.",
        "starter_code": "from fastapi import FastAPI\nfrom pydantic import BaseModel, Field, field_validator\n\napp = FastAPI()\n",
        "solution_code": (
            "from fastapi import FastAPI\n"
            "from pydantic import BaseModel, Field, field_validator\n\n"
            "app = FastAPI()\n\n"
            "class TokenizeRequest(BaseModel):\n"
            "    text: str = Field(min_length=1, max_length=500)\n"
            "    lowercase: bool = True\n\n"
            "    @field_validator('text')\n"
            "    @classmethod\n"
            "    def must_not_be_blank(cls, v: str) -> str:\n"
            "        if not v.strip():\n"
            "            raise ValueError('text cannot be blank')\n"
            "        return v\n\n"
            "@app.post('/tokenize')\n"
            "def tokenize_endpoint(req: TokenizeRequest) -> dict:\n"
            "    raw = req.text.lower() if req.lowercase else req.text\n"
            "    tokens = raw.split()\n"
            "    return {'tokens': tokens, 'count': len(tokens)}\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Input validation lives in Pydantic so route handlers stay clean.",
        "test_cases": [
            {
                "name": "valid_invalid",
                "code": (
                    "from fastapi.testclient import TestClient\nclient = TestClient(sol.app)\n"
                    "r1 = client.post('/tokenize', json={'text': 'Hello AI'})\n"
                    "assert r1.status_code == 200 and r1.json() == {'tokens': ['hello', 'ai'], 'count': 2}\n"
                    "assert client.post('/tokenize', json={'text': '   '}).status_code == 422"
                ),
            },
        ],
    },
    {
        "id": "wb-12-02",
        "chapter_id": "ch12",
        "number": "12.2",
        "title": "Microservice Pattern: Async Job Queue & Worker",
        "topic": "FastAPI",
        "question_type": "Systems",
        "difficulty": "Intermediate",
        "summary": "Decouple job submission from background execution with `asyncio.Queue`.",
        "prompt_markdown": "Implement `JobBroker` with `submit(payload: str) -> str` and `async def process_one() -> bool`.",
        "thinking_blueprint": ["`submit` enqueues non-blocking; `process_one` pops and marks `'done'`."],
        "hints": ["Use `self.queue.put_nowait((job_id, payload))` inside `submit()`."],
        "dry_run_trace": "`submit('train')` -> `'queued'` -> `process_one()` -> `'done'`.",
        "starter_code": (
            "import asyncio\n\nclass JobBroker:\n    def __init__(self) -> None:\n"
            "        self.queue: asyncio.Queue[tuple[str, str]] = asyncio.Queue()\n"
            "        self.jobs: dict[str, dict] = {}\n        self._counter = 0\n\n"
            "    def submit(self, payload: str) -> str:\n        pass\n\n"
            "    async def process_one(self) -> bool:\n        pass\n"
        ),
        "solution_code": (
            "import asyncio\n\nclass JobBroker:\n    def __init__(self) -> None:\n"
            "        self.queue: asyncio.Queue[tuple[str, str]] = asyncio.Queue()\n"
            "        self.jobs: dict[str, dict] = {}\n        self._counter = 0\n\n"
            "    def submit(self, payload: str) -> str:\n"
            "        self._counter += 1\n        job_id = f'job-{self._counter}'\n"
            "        self.jobs[job_id] = {'status': 'queued', 'result': None}\n"
            "        self.queue.put_nowait((job_id, payload))\n        return job_id\n\n"
            "    async def process_one(self) -> bool:\n"
            "        if self.queue.empty():\n            return False\n"
            "        job_id, payload = await self.queue.get()\n"
            "        self.jobs[job_id]['status'] = 'processing'\n        await asyncio.sleep(0)\n"
            "        self.jobs[job_id]['result'] = payload.upper()\n"
            "        self.jobs[job_id]['status'] = 'done'\n        self.queue.task_done()\n        return True\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Separates intake from heavy worker processing.",
        "test_cases": [
            {
                "name": "broker",
                "code": (
                    "import asyncio\nb = sol.JobBroker()\njid = b.submit('train')\n"
                    "assert b.jobs[jid]['status'] == 'queued' and asyncio.run(b.process_one()) is True\n"
                    "assert b.jobs[jid] == {'status': 'done', 'result': 'TRAIN'} and asyncio.run(b.process_one()) is False"
                ),
            },
        ],
    },

    # ---------------- CHAPTER 13: FastMCP (`mcp`) ----------------
    {
        "id": "wb-13-01",
        "chapter_id": "ch13",
        "number": "13.1",
        "title": "Build an MCP Tool Server (`MCPServer` & `@mcp.tool`)",
        "topic": "FastMCP",
        "question_type": "Systems",
        "difficulty": "Foundation",
        "summary": "Expose typed Python functions as MCP tools and verify them via `list_tools` / `call_tool`.",
        "prompt_markdown": (
            "Create `mcp = MCPServer('math-text-tools')` (`from mcp.server.mcpserver import MCPServer`) with two `@mcp.tool()` functions:\n"
            "1. `word_count(text: str) -> int`: returns number of whitespace-separated words.\n"
            "2. `multiply(a: int, b: int) -> int`: returns `a * b`."
        ),
        "thinking_blueprint": ["Instantiate `MCPServer`, decorate each typed function with `@mcp.tool()` and a clear docstring."],
        "hints": ["Remember to write type hints (`text: str -> int`) so MCP builds the tool schema automatically."],
        "dry_run_trace": "`call_tool('word_count', {'text': 'hello mcp world'})` -> `structured_content == {'result': 3}`.",
        "starter_code": (
            "from mcp.server.mcpserver import MCPServer\n\n"
            "mcp = MCPServer('math-text-tools')\n\n"
            "# TODO: register word_count and multiply with @mcp.tool()\n"
        ),
        "solution_code": (
            "from mcp.server.mcpserver import MCPServer\n\n"
            "mcp = MCPServer('math-text-tools')\n\n"
            "@mcp.tool()\n"
            "def word_count(text: str) -> int:\n"
            "    \"\"\"Count whitespace-separated words in text.\"\"\"\n"
            "    return len(text.split())\n\n"
            "@mcp.tool()\n"
            "def multiply(a: int, b: int) -> int:\n"
            "    \"\"\"Multiply two integers.\"\"\"\n"
            "    return a * b\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Decorated typed functions become standard MCP tools callable by any AI agent.",
        "test_cases": [
            {
                "name": "mcp_tools",
                "code": (
                    "import asyncio\n"
                    "names = [t.name for t in asyncio.run(sol.mcp.list_tools())]\n"
                    "assert 'word_count' in names and 'multiply' in names\n"
                    "r1 = asyncio.run(sol.mcp.call_tool('word_count', {'text': 'hello mcp world'}))\n"
                    "r2 = asyncio.run(sol.mcp.call_tool('multiply', {'a': 6, 'b': 7}))\n"
                    "assert r1.structured_content == {'result': 3}\n"
                    "assert r2.structured_content == {'result': 42}"
                ),
            },
        ],
    },
    {
        "id": "wb-13-02",
        "chapter_id": "ch13",
        "number": "13.2",
        "title": "MCP File-Note Tool & Resource With Path Safety",
        "topic": "FastMCP",
        "question_type": "Systems",
        "difficulty": "Intermediate",
        "summary": "Build an MCP tool + `@mcp.resource` reading/writing files safely without `../` traversal bugs.",
        "prompt_markdown": (
            "Write `build_notes_server(notes_dir: Path) -> MCPServer` returning an `MCPServer` with:\n"
            "- `@mcp.tool() def write_note(filename: str, content: str) -> str`: strips directory traversal using `Path(filename).name`, writes UTF-8 text into `notes_dir`, and returns `'Saved <safe_name>'`.\n"
            "- `@mcp.resource('notes://count') def note_count() -> str`: returns string count of `.txt` files in `notes_dir`."
        ),
        "thinking_blueprint": ["Sanitize with `safe = Path(filename).name`.", "Use `notes_dir.mkdir(parents=True, exist_ok=True)`."],
        "hints": ["`str(len(list(notes_dir.glob('*.txt'))))`"],
        "dry_run_trace": "`write_note('../../evil.txt', 'hi')` saves safely as `notes_dir/evil.txt`!",
        "starter_code": (
            "from pathlib import Path\n"
            "from mcp.server.mcpserver import MCPServer\n\n"
            "def build_notes_server(notes_dir: Path) -> MCPServer:\n"
            "    mcp = MCPServer('notes-server')\n"
            "    # TODO: add write_note tool and notes://count resource\n"
            "    return mcp\n"
        ),
        "solution_code": (
            "from pathlib import Path\n"
            "from mcp.server.mcpserver import MCPServer\n\n"
            "def build_notes_server(notes_dir: Path) -> MCPServer:\n"
            "    notes_dir.mkdir(parents=True, exist_ok=True)\n"
            "    mcp = MCPServer('notes-server')\n\n"
            "    @mcp.tool()\n"
            "    def write_note(filename: str, content: str) -> str:\n"
            "        \"\"\"Save a note safely inside notes_dir.\"\"\"\n"
            "        safe_name = Path(filename).name\n"
            "        (notes_dir / safe_name).write_text(content, encoding='utf-8')\n"
            "        return f'Saved {safe_name}'\n\n"
            "    @mcp.resource('notes://count')\n"
            "    def note_count() -> str:\n"
            "        return str(len(list(notes_dir.glob('*.txt'))))\n\n"
            "    return mcp\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** `Path(filename).name` blocks path-traversal attacks while exposing clean MCP tools & resources.",
        "test_cases": [
            {
                "name": "safe_notes_mcp",
                "code": (
                    "import asyncio, tempfile\nfrom pathlib import Path\n"
                    "with tempfile.TemporaryDirectory() as d:\n"
                    "    srv = sol.build_notes_server(Path(d))\n"
                    "    res = asyncio.run(srv.call_tool('write_note', {'filename': '../../a.txt', 'content': 'hello'}))\n"
                    "    assert res.structured_content == {'result': 'Saved a.txt'}\n"
                    "    assert (Path(d) / 'a.txt').read_text(encoding='utf-8') == 'hello'\n"
                    "    cnt = asyncio.run(srv.read_resource('notes://count'))\n"
                    "    assert cnt[0].content == '1'"
                ),
            },
        ],
    },

    # ---------------- CHAPTER 14: Docker ----------------
    {
        "id": "wb-14-01",
        "chapter_id": "ch14",
        "number": "14.1",
        "title": "Dockerfile Layer-Cache & Security Linter",
        "topic": "Docker",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Detect `:latest` tags, cache-busting `COPY . .` order, and missing `--no-cache-dir`.",
        "prompt_markdown": "Write `audit_dockerfile(lines: list[str]) -> list[str]` returning `'PIN_BASE_IMAGE'`, `'CACHE_BUST_ORDER'`, and `'USE_NO_CACHE_PIP'` warnings.",
        "thinking_blueprint": ["Track index of first `COPY .` and first `pip install`."],
        "hints": ["Normalize spaces with `' '.join(raw.strip().split())`."],
        "dry_run_trace": "`['FROM python:latest', 'COPY . .', 'RUN pip install -r req.txt']` -> all 3 warnings.",
        "starter_code": "def audit_dockerfile(lines: list[str]) -> list[str]:\n    pass\n",
        "solution_code": (
            "def audit_dockerfile(lines: list[str]) -> list[str]:\n"
            "    warnings: list[str] = []\n"
            "    copy_all_idx: int | None = None\n"
            "    pip_idx: int | None = None\n"
            "    for idx, raw in enumerate(lines):\n"
            "        line = ' '.join(raw.strip().split())\n"
            "        if line.startswith('FROM '):\n"
            "            image = line.split()[1]\n"
            "            if ':' not in image or image.endswith(':latest'):\n"
            "                warnings.append('PIN_BASE_IMAGE')\n"
            "        if line.startswith('COPY . ') or line.startswith('COPY ./ '):\n"
            "            if copy_all_idx is None:\n"
            "                copy_all_idx = idx\n"
            "        if 'pip install' in line:\n"
            "            if pip_idx is None:\n"
            "                pip_idx = idx\n"
            "            if '--no-cache-dir' not in line and 'USE_NO_CACHE_PIP' not in warnings:\n"
            "                warnings.append('USE_NO_CACHE_PIP')\n"
            "    if copy_all_idx is not None and pip_idx is not None and copy_all_idx < pip_idx:\n"
            "        warnings.append('CACHE_BUST_ORDER')\n"
            "    return warnings\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Single-pass index tracker + layer order check.",
        "test_cases": [
            {"name": "docker_lint", "code": "assert set(sol.audit_dockerfile(['FROM python:latest', 'COPY . .', 'RUN pip install -r requirements.txt'])) == {'PIN_BASE_IMAGE', 'CACHE_BUST_ORDER', 'USE_NO_CACHE_PIP'}\nassert sol.audit_dockerfile(['FROM python:3.12-slim', 'COPY requirements.txt .', 'RUN pip install --no-cache-dir -r requirements.txt', 'COPY . .']) == []"},
        ],
    },
    {
        "id": "wb-14-02",
        "chapter_id": "ch14",
        "number": "14.2",
        "title": "Compose Startup Order via Dependency Graph",
        "topic": "Docker",
        "question_type": "DSA & DP",
        "difficulty": "Intermediate",
        "summary": "Apply Chapter 6 topological sort to `docker-compose` `depends_on` ordering.",
        "prompt_markdown": "Given `services: dict[str, list[str]]`, return a valid startup order with alphabetical tie-breaking.",
        "thinking_blueprint": ["Flip edges: `dep -> svc`, then run Kahn's topological sort with `heapq`."],
        "hints": ["`indeg[svc] = len(deps)`"],
        "dry_run_trace": "`redis` -> `worker` -> `gateway`.",
        "starter_code": "import heapq\n\ndef compose_startup_order(services: dict[str, list[str]]) -> list[str]:\n    pass\n",
        "solution_code": (
            "import heapq\n\n"
            "def compose_startup_order(services: dict[str, list[str]]) -> list[str]:\n"
            "    dependents: dict[str, list[str]] = {s: [] for s in services}\n"
            "    indeg: dict[str, int] = {s: len(deps) for s, deps in services.items()}\n"
            "    for svc, deps in services.items():\n"
            "        for dep in deps:\n"
            "            dependents[dep].append(svc)\n"
            "    heap = [s for s, deg in indeg.items() if deg == 0]\n"
            "    heapq.heapify(heap)\n"
            "    order: list[str] = []\n"
            "    while heap:\n"
            "        cur = heapq.heappop(heap)\n"
            "        order.append(cur)\n"
            "        for nxt in dependents[cur]:\n"
            "            indeg[nxt] -= 1\n"
            "            if indeg[nxt] == 0:\n"
            "                heapq.heappush(heap, nxt)\n"
            "    if len(order) != len(services):\n"
            "        raise ValueError('Circular depends_on detected')\n"
            "    return order\n"
        ),
        "explanation_markdown": "**High-Level Blocks:** Reuses Kahn's topological sort for container startup ordering.",
        "test_cases": [
            {"name": "stack", "code": "assert sol.compose_startup_order({'gateway': ['worker', 'redis'], 'worker': ['redis'], 'redis': []}) == ['redis', 'worker', 'gateway']"},
        ],
    },
]
