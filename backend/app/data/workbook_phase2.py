"""Phase 2 Practice Workbook (Chapters 6-9): NumPy, Pandas, FastAPI Microservices, Docker."""

from __future__ import annotations

from typing import Any

PHASE_2_WORKBOOK: list[dict[str, Any]] = [
    # ---------------- CHAPTER 6: NumPy ----------------
    {
        "id": "wb-06-01",
        "chapter_id": "ch06",
        "number": "6.1",
        "title": "Vectorized Standardization (Broadcasting + `axis`)",
        "topic": "NumPy",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Standardize feature columns to mean 0 and std 1 safely without Python loops.",
        "prompt_markdown": (
            "Write `standardize_columns(x: np.ndarray) -> np.ndarray` for shape `(N, D)` subtracting column means and dividing "
            "by column stds (replace zero std with `1.0`)."
        ),
        "thinking_blueprint": [
            "Compute column stats with `axis=0, keepdims=True` -> shape `(1, D)`.",
            "Guard constant columns with `np.where(std == 0, 1.0, std)`.",
        ],
        "hints": [
            "`keepdims=True` makes `(1, D)` broadcast across `(N, D)` cleanly even when `N == D`.",
        ],
        "dry_run_trace": (
            "`[[1, 5], [3, 5]]` -> `mean=[[2, 5]], safe_std=[[1, 1]]` -> `[[-1, 0], [1, 0]]`."
        ),
        "starter_code": (
            "import numpy as np\n\n"
            "def standardize_columns(x: np.ndarray) -> np.ndarray:\n"
            "    # TODO: normalize columns safely\n"
            "    pass\n"
        ),
        "solution_code": (
            "import numpy as np\n\n"
            "def standardize_columns(x: np.ndarray) -> np.ndarray:\n"
            "    x = np.asarray(x, dtype=float)\n"
            "    mean = x.mean(axis=0, keepdims=True)\n"
            "    std = x.std(axis=0, keepdims=True)\n"
            "    safe_std = np.where(std == 0, 1.0, std)\n"
            "    return (x - mean) / safe_std\n"
        ),
        "explanation_markdown": (
            "**High-Level Blocks:** (1) Column reduction with `keepdims=True`; (2) Zero-division guard via `np.where`; (3) Broadcasted subtraction & division."
        ),
        "test_cases": [
            {"name": "standardize_constant_col", "code": "import numpy as np\nx = np.array([[1.0, 5.0], [3.0, 5.0]])\nassert np.allclose(sol.standardize_columns(x), np.array([[-1.0, 0.0], [1.0, 0.0]]))"},
        ],
    },
    {
        "id": "wb-06-02",
        "chapter_id": "ch06",
        "number": "6.2",
        "title": "Numerically Stable Softmax",
        "topic": "NumPy",
        "question_type": "Logic & Coding",
        "difficulty": "Intermediate",
        "summary": "Implement row-wise softmax along `axis=-1` safe against `exp(1000)` overflow.",
        "prompt_markdown": (
            "Write `stable_softmax(logits: np.ndarray) -> np.ndarray` working for both 1D `(C,)` and 2D `(B, C)` inputs."
        ),
        "thinking_blueprint": [
            "Subtract `np.max(logits, axis=-1, keepdims=True)` first.",
            "Exponentiate and divide by `np.sum(..., axis=-1, keepdims=True)`.",
        ],
        "hints": [
            "`axis=-1` always targets the last axis regardless of 1D/2D/3D shape.",
        ],
        "dry_run_trace": (
            "`[1000.0, 1000.0]` -> shift by `1000.0` -> `[0.0, 0.0]` -> `[0.5, 0.5]`."
        ),
        "starter_code": (
            "import numpy as np\n\n"
            "def stable_softmax(logits: np.ndarray) -> np.ndarray:\n"
            "    # TODO: stable softmax along axis=-1\n"
            "    pass\n"
        ),
        "solution_code": (
            "import numpy as np\n\n"
            "def stable_softmax(logits: np.ndarray) -> np.ndarray:\n"
            "    logits = np.asarray(logits, dtype=float)\n"
            "    shifted = logits - np.max(logits, axis=-1, keepdims=True)\n"
            "    exps = np.exp(shifted)\n"
            "    return exps / np.sum(exps, axis=-1, keepdims=True)\n"
        ),
        "explanation_markdown": (
            "**High-Level Blocks:** Shifting by max keeps all exponents `<= 0`, preventing `inf` while preserving exact mathematical probabilities."
        ),
        "test_cases": [
            {"name": "overflow_safe_2d", "code": "import numpy as np\nassert np.allclose(sol.stable_softmax(np.array([1000.0, 1000.0])), [0.5, 0.5])\np2 = sol.stable_softmax(np.array([[1.0, 2.0, 3.0], [0.0, 0.0, 0.0]]))\nassert np.allclose(p2.sum(axis=-1), [1.0, 1.0])"},
        ],
    },
    {
        "id": "wb-06-03",
        "chapter_id": "ch06",
        "number": "6.3",
        "title": "Cosine Top-K Vector Retrieval",
        "topic": "NumPy",
        "question_type": "Logic & Coding",
        "difficulty": "Intermediate",
        "summary": "Rank document embeddings by cosine similarity using pure NumPy matrix multiplication.",
        "prompt_markdown": (
            "Write `cosine_top_k(docs: np.ndarray, query: np.ndarray, k: int) -> list[int]` returning top-`k` indices descending."
        ),
        "thinking_blueprint": [
            "L2-normalize rows of `docs` and vector `query`.",
            "Dot product `docs_unit @ query_unit` computes all cosine scores at once.",
        ],
        "hints": [
            "Guard zero vectors with `np.maximum(norms, 1e-12)`.",
        ],
        "dry_run_trace": (
            "`docs=[[1,0],[0,1],[1,1]]`, `query=[2,0]` -> sims `[1.0, 0.0, 0.707]` -> top 2 `[0, 2]`."
        ),
        "starter_code": (
            "import numpy as np\n\n"
            "def cosine_top_k(docs: np.ndarray, query: np.ndarray, k: int) -> list[int]:\n"
            "    # TODO: return indices of top-k cosine-similar rows\n"
            "    pass\n"
        ),
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
        "explanation_markdown": (
            "**High-Level Blocks:** (1) Guard empty/`k<=0`; (2) Unit-normalize docs & query; (3) Matrix-vector dot product + descending argsort."
        ),
        "test_cases": [
            {"name": "top_k", "code": "import numpy as np\ndocs = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])\nassert sol.cosine_top_k(docs, np.array([2.0, 0.0]), 2) == [0, 2]"},
        ],
    },
    # ---------------- CHAPTER 7: Pandas ----------------
    {
        "id": "wb-07-01",
        "chapter_id": "ch07",
        "number": "7.1",
        "title": "Pandas Text Cleaning & Hash Deduplication",
        "topic": "Pandas",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Clean missing/short rows, normalize whitespace, and deduplicate keeping highest score.",
        "prompt_markdown": (
            "Write `clean_corpus(df: pd.DataFrame, min_len: int = 10) -> pd.DataFrame`: drop null `'text'`, collapse whitespace into "
            "`'clean_text'`, keep `len >= min_len`, deduplicate case-insensitively keeping highest `'score'`, and sort by `'id'`."
        ),
        "thinking_blueprint": [
            "Drop nulls + `.copy()`.",
            "Vectorized `.str.split().str.join(' ')` normalizes whitespace.",
            "Sort by `'score'` descending before `drop_duplicates`, then sort by `'id'`.",
        ],
        "hints": [
            "Remember `.reset_index(drop=True)` after sorting.",
        ],
        "dry_run_trace": (
            "`'  Hello   AI world  '` (score 0.5) & `'hello ai world'` (score 0.95) -> keeps row with score 0.95."
        ),
        "starter_code": (
            "import pandas as pd\n\n"
            "def clean_corpus(df: pd.DataFrame, min_len: int = 10) -> pd.DataFrame:\n"
            "    # TODO: clean and deduplicate text corpus\n"
            "    pass\n"
        ),
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
        "explanation_markdown": (
            "**High-Level Blocks:** (1) Null & length filtering; (2) Normalized dedup key; (3) Score-prioritized deduplication."
        ),
        "test_cases": [
            {
                "name": "dedup_filter",
                "code": (
                    "import pandas as pd\n"
                    "df = pd.DataFrame([{'id': 1, 'text': '  Hello   AI world  ', 'score': 0.5}, {'id': 2, 'text': None, 'score': 0.9}, {'id': 3, 'text': 'short', 'score': 0.9}, {'id': 4, 'text': 'hello ai world', 'score': 0.95}])\n"
                    "res = sol.clean_corpus(df, min_len=10)\n"
                    "assert list(res['id']) == [4] and res.loc[0, 'clean_text'] == 'hello ai world'"
                ),
            },
        ],
    },
    {
        "id": "wb-07-02",
        "chapter_id": "ch07",
        "number": "7.2",
        "title": "GroupBy Quality Metrics per Dataset Source",
        "topic": "Pandas",
        "question_type": "Logic & Coding",
        "difficulty": "Intermediate",
        "summary": "Aggregate total rows, valid count, and average tokens per dataset source.",
        "prompt_markdown": (
            "Write `summarize_sources(df: pd.DataFrame) -> pd.DataFrame` returning `['source', 'total_rows', 'valid_rows', 'avg_tokens']` sorted by `'source'`."
        ),
        "thinking_blueprint": [
            "Use `.groupby('source', as_index=False).agg(...)` with named aggregations.",
        ],
        "hints": [
            "Cast `valid_rows` to `int`.",
        ],
        "dry_run_trace": (
            "Source `'wiki'` `[100, 200]`, `[True, False]` -> `total_rows=2, valid_rows=1, avg_tokens=150.0`."
        ),
        "starter_code": (
            "import pandas as pd\n\n"
            "def summarize_sources(df: pd.DataFrame) -> pd.DataFrame:\n"
            "    # TODO: summarize source quality metrics\n"
            "    pass\n"
        ),
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
        "explanation_markdown": (
            "**High-Level Blocks:** Named aggregation produces flat column names directly without MultiIndex cleanup."
        ),
        "test_cases": [
            {
                "name": "source_summary",
                "code": (
                    "import pandas as pd\n"
                    "df = pd.DataFrame([{'source': 'wiki', 'tokens': 100, 'is_valid': True}, {'source': 'wiki', 'tokens': 200, 'is_valid': False}, {'source': 'arxiv', 'tokens': 300, 'is_valid': True}])\n"
                    "res = sol.summarize_sources(df)\n"
                    "assert list(res['source']) == ['arxiv', 'wiki'] and res.loc[1, 'valid_rows'] == 1 and res.loc[1, 'avg_tokens'] == 150.0"
                ),
            },
        ],
    },
    # ---------------- CHAPTER 8: FastAPI & Microservices ----------------
    {
        "id": "wb-08-01",
        "chapter_id": "ch08",
        "number": "8.1",
        "title": "Pydantic Contract & FastAPI `/tokenize` Endpoint",
        "topic": "FastAPI",
        "question_type": "Systems",
        "difficulty": "Foundation",
        "summary": "Build a validated FastAPI POST endpoint rejecting blank inputs with HTTP 422.",
        "prompt_markdown": (
            "Build `app = FastAPI()` with `POST /tokenize` accepting `{'text': str, 'lowercase': bool = True}` (reject blank strings via HTTP 422) "
            "and returning `{'tokens': list[str], 'count': int}`."
        ),
        "thinking_blueprint": [
            "Block 1: Pydantic `BaseModel` with `@field_validator('text')` rejecting whitespace-only text.",
            "Block 2: Route handler transforms and returns structured dict.",
        ],
        "hints": [
            "Raise `ValueError` inside `@field_validator` to trigger FastAPI's automatic 422 response.",
        ],
        "dry_run_trace": (
            "`{'text': 'Hello AI'}` -> `200 {'tokens': ['hello', 'ai'], 'count': 2}`. `{'text': '   '}` -> `422`."
        ),
        "starter_code": (
            "from fastapi import FastAPI\n"
            "from pydantic import BaseModel, Field, field_validator\n\n"
            "app = FastAPI()\n\n"
            "# TODO: define TokenizeRequest and POST /tokenize\n"
        ),
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
        "explanation_markdown": (
            "**High-Level Blocks:** Input validation sits cleanly inside the Pydantic contract so endpoint code stays focused on business logic."
        ),
        "test_cases": [
            {
                "name": "valid_and_invalid",
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
        "id": "wb-08-02",
        "chapter_id": "ch08",
        "number": "8.2",
        "title": "Microservice Pattern: Async Job Queue & Worker",
        "topic": "FastAPI",
        "question_type": "Systems",
        "difficulty": "Intermediate",
        "summary": "Decouple job submission from background execution with `asyncio.Queue`.",
        "prompt_markdown": (
            "Implement `JobBroker` with `submit(payload: str) -> str` and `async def process_one() -> bool`."
        ),
        "thinking_blueprint": [
            "`submit` generates `job-1`, sets status `'queued'`, and enqueues without blocking.",
            "`process_one` returns `False` if empty, else processes one job to `'done'` and returns `True`.",
        ],
        "hints": [
            "Use `self.queue.put_nowait((job_id, payload))` inside synchronous `submit()`.",
        ],
        "dry_run_trace": (
            "`submit('train')` -> `'queued'` -> `await process_one()` -> `{'status': 'done', 'result': 'TRAIN'}`."
        ),
        "starter_code": (
            "import asyncio\n\n"
            "class JobBroker:\n"
            "    def __init__(self) -> None:\n"
            "        self.queue: asyncio.Queue[tuple[str, str]] = asyncio.Queue()\n"
            "        self.jobs: dict[str, dict] = {}\n"
            "        self._counter = 0\n\n"
            "    def submit(self, payload: str) -> str:\n"
            "        pass\n\n"
            "    async def process_one(self) -> bool:\n"
            "        pass\n"
        ),
        "solution_code": (
            "import asyncio\n\n"
            "class JobBroker:\n"
            "    def __init__(self) -> None:\n"
            "        self.queue: asyncio.Queue[tuple[str, str]] = asyncio.Queue()\n"
            "        self.jobs: dict[str, dict] = {}\n"
            "        self._counter = 0\n\n"
            "    def submit(self, payload: str) -> str:\n"
            "        self._counter += 1\n"
            "        job_id = f'job-{self._counter}'\n"
            "        self.jobs[job_id] = {'status': 'queued', 'result': None}\n"
            "        self.queue.put_nowait((job_id, payload))\n"
            "        return job_id\n\n"
            "    async def process_one(self) -> bool:\n"
            "        if self.queue.empty():\n"
            "            return False\n"
            "        job_id, payload = await self.queue.get()\n"
            "        self.jobs[job_id]['status'] = 'processing'\n"
            "        await asyncio.sleep(0)\n"
            "        self.jobs[job_id]['result'] = payload.upper()\n"
            "        self.jobs[job_id]['status'] = 'done'\n"
            "        self.queue.task_done()\n"
            "        return True\n"
        ),
        "explanation_markdown": (
            "**High-Level Blocks:** Separating job intake (`submit`) from execution (`process_one`) models the exact Redis + Worker microservice pattern."
        ),
        "test_cases": [
            {
                "name": "broker_lifecycle",
                "code": (
                    "import asyncio\nb = sol.JobBroker()\njid = b.submit('train')\n"
                    "assert b.jobs[jid]['status'] == 'queued'\n"
                    "assert asyncio.run(b.process_one()) is True\n"
                    "assert b.jobs[jid] == {'status': 'done', 'result': 'TRAIN'}\n"
                    "assert asyncio.run(b.process_one()) is False"
                ),
            },
        ],
    },
    # ---------------- CHAPTER 9: Docker ----------------
    {
        "id": "wb-09-01",
        "chapter_id": "ch09",
        "number": "9.1",
        "title": "Dockerfile Layer-Cache & Security Linter",
        "topic": "Docker",
        "question_type": "Logic & Coding",
        "difficulty": "Foundation",
        "summary": "Detect `:latest` tags, cache-busting `COPY . .` ordering, and missing `--no-cache-dir`.",
        "prompt_markdown": (
            "Write `audit_dockerfile(lines: list[str]) -> list[str]` returning `'PIN_BASE_IMAGE'`, `'CACHE_BUST_ORDER'`, and `'USE_NO_CACHE_PIP'` warnings."
        ),
        "thinking_blueprint": [
            "Track index of first `COPY .` and first `pip install` while inspecting `FROM` and pip flags.",
        ],
        "hints": [
            "Normalize spaces using `' '.join(raw.strip().split())`.",
        ],
        "dry_run_trace": (
            "`['FROM python:latest', 'COPY . .', 'RUN pip install -r req.txt']` -> all 3 warnings."
        ),
        "starter_code": (
            "def audit_dockerfile(lines: list[str]) -> list[str]:\n"
            "    # TODO: audit FROM tag, COPY order, and pip --no-cache-dir\n"
            "    pass\n"
        ),
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
        "explanation_markdown": (
            "**High-Level Blocks:** (1) Single-pass state tracker records key line indices; (2) Post-loop comparison checks layer order."
        ),
        "test_cases": [
            {"name": "bad_good", "code": "assert set(sol.audit_dockerfile(['FROM python:latest', 'COPY . .', 'RUN pip install -r requirements.txt'])) == {'PIN_BASE_IMAGE', 'CACHE_BUST_ORDER', 'USE_NO_CACHE_PIP'}\nassert sol.audit_dockerfile(['FROM python:3.12-slim', 'COPY requirements.txt .', 'RUN pip install --no-cache-dir -r requirements.txt', 'COPY . .']) == []"},
        ],
    },
    {
        "id": "wb-09-02",
        "chapter_id": "ch09",
        "number": "9.2",
        "title": "Compose Startup Order via Dependency Graph",
        "topic": "Docker",
        "question_type": "DSA & DP",
        "difficulty": "Intermediate",
        "summary": "Apply Chapter 4 DAG topological sort to `docker-compose` `depends_on` ordering.",
        "prompt_markdown": (
            "Given `services: dict[str, list[str]]` (`service -> depends_on list`), return a valid startup order with alphabetical tie-breaking."
        ),
        "thinking_blueprint": [
            "Flip edges: if `gateway` depends on `redis`, `redis -> gateway`!",
            "Run Kahn's topological sort with `heapq`.",
        ],
        "hints": [
            "`indeg[svc]` equals `len(deps)`.",
        ],
        "dry_run_trace": (
            "`redis` starts first -> unlocks `worker` -> unlocks `gateway`."
        ),
        "starter_code": (
            "import heapq\n\n"
            "def compose_startup_order(services: dict[str, list[str]]) -> list[str]:\n"
            "    # TODO: topological sort over depends_on\n"
            "    pass\n"
        ),
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
        "explanation_markdown": (
            "**High-Level Blocks:** Reuses Chapter 4's exact Kahn's algorithm—showing how DSA directly powers container orchestration."
        ),
        "test_cases": [
            {"name": "stack_order", "code": "assert sol.compose_startup_order({'gateway': ['worker', 'redis'], 'worker': ['redis'], 'redis': []}) == ['redis', 'worker', 'gateway']"},
        ],
    },
]
