"""Phase 2 Curriculum (Chapters 6-9): Structured beginner-friendly lessons for NumPy, Pandas, FastAPI & Docker."""

from __future__ import annotations

from typing import Any

PHASE_2_CHAPTERS: list[dict[str, Any]] = [
    {
        "id": "ch06",
        "number": 6,
        "phase": 2,
        "phase_title": "Phase 2: The AI Engineer's Data, API & Container Stack",
        "title": "NumPy & Vectorized Linear Algebra",
        "subtitle": "Arrays, shapes, axes, broadcasting rules, dot products, cosine similarity, and stable softmax.",
        "status_type": "available",
        "estimated_hours": 5,
        "why_it_matters": (
            "PyTorch tensors and Transformer attention layers work almost identically to NumPy arrays. Mastering `.shape`, `axis`, "
            "and broadcasting here makes deep learning code easy to read."
        ),
        "just_in_time_tags": ["np.array & .shape", "axis=0 vs axis=1", "Broadcasting", "Dot Product (@)", "Softmax"],
        "visualizer": "numpy_broadcast",
        "sections": [
            {
                "id": "ch06-s1",
                "title": "6.1 NumPy Arrays, `.shape` & `axis` (Replacing Loops)",
                "zero_assumption_note": "If `axis=0` vs `axis=1` always confused you, remember: `axis` tells NumPy **which direction to collapse**.",
                "definition": (
                    "A **NumPy array (`ndarray`)** stores numbers in one tightly packed block of C memory so math runs on entire rows/columns "
                    "at once—often 50x faster than a Python `for` loop."
                ),
                "syntax_box": {
                    "title": "Creating Arrays, Checking Shape & Collapsing Axes",
                    "syntax": (
                        "import numpy as np\n\n"
                        "a = np.array([[1.0, 2.0, 3.0],\n"
                        "              [4.0, 5.0, 6.0]])\n"
                        "a.shape               # (2, 3) -> 2 rows, 3 columns\n"
                        "a.sum(axis=0)         # [5., 7., 9.]  (collapses rows -> 1 answer per column)\n"
                        "a.sum(axis=1)         # [6., 15.]     (collapses cols -> 1 answer per row)\n"
                        "a.sum(axis=1, keepdims=True)  # shape (2, 1) instead of (2,)"
                    ),
                    "breakdown": [
                        "`.shape` returns `(rows, cols)` for 2D matrices.",
                        "`axis=0` collapses axis 0 (rows), leaving `(3,)`.",
                        "`axis=1` collapses axis 1 (columns), leaving `(2,)`.",
                        "`keepdims=True` keeps the collapsed axis as size `1` so you can divide rows by row-sums cleanly!",
                    ],
                },
                "tiny_example": {
                    "title": "Doubling Numbers Without a `for` Loop",
                    "code": (
                        "import numpy as np\n"
                        "prices = np.array([10, 20, 30])\n"
                        "doubled = prices * 2\n"
                        "print(doubled)"
                    ),
                    "line_by_line": [
                        "`prices` is a 1D array of shape `(3,)`.",
                        "`prices * 2` multiplies every element in C memory at once -> `[20, 40, 60]`.",
                    ],
                },
                "body_markdown": (
                    "### Broadcasting & Dot Product (`@`)\n"
                    "- **Broadcasting:** NumPy compares two shapes **right-to-left**. Dimensions match if they are **equal** OR **one of them is `1`** (missing left axes are treated as `1`).\n"
                    "- **Dot Product / Matrix Multiply (`A @ B`):** Multiplies matching dimensions and sums them—used everywhere in embeddings and neural layers.\n\n"
                    "**Test shapes live** in the NumPy Broadcasting Explorer below!"
                ),
                "code_example": {
                    "title": "Stable Softmax & Cosine Top-K Search",
                    "code": (
                        "import numpy as np\n\n"
                        "# Block 1: Subtract max first so np.exp(1000) never overflows to inf\n"
                        "def softmax(logits: np.ndarray) -> np.ndarray:\n"
                        "    shifted = logits - np.max(logits, axis=-1, keepdims=True)\n"
                        "    exps = np.exp(shifted)\n"
                        "    return exps / np.sum(exps, axis=-1, keepdims=True)\n\n"
                        "# Block 2: Unit-normalize rows, then dot-product with normalized query\n"
                        "def cosine_top_k(docs: np.ndarray, query: np.ndarray, k: int = 2) -> np.ndarray:\n"
                        "    docs_unit = docs / np.linalg.norm(docs, axis=1, keepdims=True)\n"
                        "    q_unit = query / np.linalg.norm(query)\n"
                        "    sims = docs_unit @ q_unit\n"
                        "    return np.argsort(sims)[::-1][:k]\n"
                    ),
                },
                "common_mistakes": [
                    "Forgetting `keepdims=True` before dividing `(N, D)` by `(N,)` (shape `(N,)` aligns on the right with `D`, not `N`!).",
                    "Using `*` instead of `@` when you want matrix multiplication (`*` does element-by-element multiplication).",
                ],
                "key_takeaway": "Print `.shape` whenever confused, pass `keepdims=True` when normalizing rows/columns, and read broadcasting right-to-left.",
            },
        ],
        "quizzes": [
            {
                "id": "ch06-q1",
                "question": "If `X` has shape `(4, 3)`, what shape does `X.sum(axis=1, keepdims=True)` return?",
                "options": ["(3,)", "(4, 1)", "(1, 3)", "(4,)"],
                "correct_index": 1,
                "explanation": "`axis=1` collapses the 3 columns into 1 while `keepdims=True` preserves the 2D shape `(4, 1)`.",
            },
        ],
        "project": {
            "title": "Pure-NumPy Semantic Vector Search Engine",
            "workspace_dir": "projects/ch06_numpy_semantic_search",
            "overview": "Implement L2 normalization, stable softmax, and top-K cosine similarity retrieval in pure NumPy.",
            "architecture_steps": [
                "Implement vectorized L2 row normalization.",
                "Implement batched cosine similarity and top-K ranking.",
                "Verify speed & accuracy with `pytest`.",
            ],
            "milestones": [
                {"id": "ch06-m1", "label": "Implement L2 normalization & stable softmax"},
                {"id": "ch06-m2", "label": "Implement top-K cosine search"},
                {"id": "ch06-m3", "label": "Verify with pytest"},
            ],
        },
    },
    {
        "id": "ch07",
        "number": 7,
        "phase": 2,
        "phase_title": "Phase 2: The AI Engineer's Data, API & Container Stack",
        "title": "Pandas & Production Data Curation",
        "subtitle": "DataFrames, loc vs iloc, filtering, string cleaning, groupby summaries, and hash deduplication.",
        "status_type": "available",
        "estimated_hours": 5,
        "why_it_matters": (
            "Training ML models or fine-tuning LLMs on duplicate, null, or noisy text wastes compute and causes train/test leakage."
        ),
        "just_in_time_tags": ["DataFrame", "loc vs iloc", "Boolean Masks", ".str Cleaning", "GroupBy", "Deduplication"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch07-s1",
                "title": "7.1 DataFrames, `loc`/`iloc` & Cleaning Datasets Without Loops",
                "zero_assumption_note": "Think of a Pandas `DataFrame` as an in-memory Excel table where each column is a fast NumPy-backed `Series`.",
                "definition": (
                    "A **DataFrame** holds rows and named columns (`df['text']`, `df['score']`). Instead of looping row-by-row, "
                    "you filter and transform entire columns at once using boolean masks and `.str` methods."
                ),
                "syntax_box": {
                    "title": "Essential DataFrame Syntax",
                    "syntax": (
                        "import pandas as pd\n\n"
                        "df = pd.DataFrame([{'text': ' Hi ', 'score': 0.9}, {'text': None, 'score': 0.2}])\n"
                        "clean = df.dropna(subset=['text']).copy()         # drop missing text\n"
                        "clean['text'] = clean['text'].str.strip()         # clean whole column\n"
                        "high = clean[clean['score'] >= 0.8]               # boolean filter\n"
                        "df.loc[0, 'text']     # select by label\n"
                        "df.iloc[0, 0]         # select by integer row/col position"
                    ),
                    "breakdown": [
                        "`.dropna(subset=['text'])`: removes rows where `'text'` is `None`/`NaN`.",
                        "`.copy()` after filtering prevents Pandas `SettingWithCopyWarning` when you edit columns later.",
                        "`loc` uses row/column **labels** (`df.loc[0:2]` includes `2`); `iloc` uses integer **positions** (`df.iloc[0:2]` stops before `2`).",
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
                        "`.mean()` computes average tokens per source: `docs -> 300.0`, `wiki -> 150.0`.",
                    ],
                },
                "body_markdown": (
                    "### Deduplicating Text Datasets Before Training\n"
                    "Sorting by quality score descending and calling `.drop_duplicates(subset=['_norm'], keep='first')` ensures only the best version of duplicate records stays in your training corpus."
                ),
                "code_example": {
                    "title": "Hash Deduplication Pipeline",
                    "code": (
                        "import hashlib\nimport pandas as pd\n\n"
                        "def text_hash(s: str) -> str:\n"
                        "    norm = ' '.join(s.lower().split())\n"
                        "    return hashlib.sha256(norm.encode('utf-8')).hexdigest()\n\n"
                        "def curate(df: pd.DataFrame) -> pd.DataFrame:\n"
                        "    out = df.dropna(subset=['text']).copy()\n"
                        "    out['hash'] = out['text'].map(text_hash)\n"
                        "    return out.drop_duplicates(subset=['hash']).reset_index(drop=True)\n"
                    ),
                },
                "common_mistakes": [
                    "Using `.iterrows()` to modify rows (very slow!). Use `.str`, `.map()`, or vectorized math.",
                    "Forgetting `.copy()` after slicing a DataFrame before adding new columns.",
                ],
                "key_takeaway": "Drop nulls, `.copy()`, clean columns with `.str`, deduplicate with hashes, and summarize with `.groupby().agg()`.",
            },
        ],
        "quizzes": [
            {
                "id": "ch07-q1",
                "question": "Why call `.copy()` right after filtering a DataFrame like `sub = df[df['score'] > 0.5].copy()`?",
                "options": [
                    "It sorts the rows",
                    "It ensures `sub` is an independent DataFrame so adding columns won't trigger `SettingWithCopyWarning`",
                    "It saves the DataFrame to CSV",
                    "It drops NaN values",
                ],
                "correct_index": 1,
                "explanation": "Filtering often creates a view; `.copy()` makes modifications safe and explicit.",
            },
        ],
        "project": {
            "title": "End-to-End LLM Corpus Curation Pipeline",
            "workspace_dir": "projects/ch07_corpus_curation_pipeline",
            "overview": "Clean messy JSONL text data, deduplicate via SHA-256, and generate per-source quality metrics.",
            "architecture_steps": [
                "Load raw records into Pandas and remove null/short noise.",
                "Deduplicate by normalized text hash.",
                "Produce `groupby` quality stats and clean splits.",
            ],
            "milestones": [
                {"id": "ch07-m1", "label": "Ingest & normalize raw text records"},
                {"id": "ch07-m2", "label": "Implement normalized hash deduplication"},
                {"id": "ch07-m3", "label": "Generate quality summary & splits"},
            ],
        },
    },
    {
        "id": "ch08",
        "number": 8,
        "phase": 2,
        "phase_title": "Phase 2: The AI Engineer's Data, API & Container Stack",
        "title": "FastAPI & Microservice Architecture",
        "subtitle": "HTTP endpoints, Pydantic validation, async vs sync routes, SSE token streaming, and Gateway + Worker microservices.",
        "status_type": "available",
        "estimated_hours": 6,
        "why_it_matters": (
            "FastAPI turns Python functions into web APIs with automatic data validation and interactive docs. Splitting heavy GPU inference "
            "into a background worker prevents slow model calls from freezing the API."
        ),
        "just_in_time_tags": ["FastAPI", "Pydantic BaseModel", "@app.post", "SSE Streaming", "Microservices"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch08-s1",
                "title": "8.1 FastAPI Endpoints, Pydantic Contracts & Microservices",
                "zero_assumption_note": "An API endpoint is just a Python function attached to a URL (like `POST /tokenize`) that receives JSON and returns JSON.",
                "definition": (
                    "- **FastAPI:** A Python web framework that turns typed functions into fast HTTP APIs.\n"
                    "- **Pydantic (`BaseModel`):** Automatically checks incoming JSON types/constraints and rejects bad inputs with HTTP `422` before your code runs.\n"
                    "- **Microservice Split:** Keeping a fast lightweight **API Gateway** separate from heavy **Worker** processes connected by a queue."
                ),
                "syntax_box": {
                    "title": "FastAPI + Pydantic Schema Template",
                    "syntax": (
                        "from fastapi import FastAPI\n"
                        "from pydantic import BaseModel, Field\n\n"
                        "app = FastAPI()\n\n"
                        "class InputData(BaseModel):\n"
                        "    text: str = Field(min_length=1)   # rejects empty string automatically!\n\n"
                        "@app.post('/analyze')\n"
                        "def analyze(payload: InputData) -> dict:\n"
                        "    return {'length': len(payload.text)}"
                    ),
                    "breakdown": [
                        "`@app.post('/analyze')` is a decorator linking HTTP POST `/analyze` to the `analyze` function.",
                        "Passing `payload: InputData` makes FastAPI parse and validate the request JSON automatically.",
                        "Use `def` for CPU/blocking work (FastAPI runs it in a threadpool); use `async def` only when `await`-ing non-blocking I/O!",
                    ],
                },
                "tiny_example": {
                    "title": "Testing an Endpoint Without Starting a Server (`TestClient`)",
                    "code": (
                        "from fastapi.testclient import TestClient\n"
                        "# assuming `app` from above:\n"
                        "client = TestClient(app)\n"
                        "resp = client.post('/analyze', json={'text': 'hello'})\n"
                        "print(resp.status_code, resp.json())"
                    ),
                    "line_by_line": [
                        "`TestClient(app)` lets you send fake HTTP requests directly in `pytest`.",
                        "`resp.status_code` is `200`, and `resp.json()` is `{'length': 5}`.",
                        "Sending `{'text': ''}` automatically returns `422` because `min_length=1` failed!",
                    ],
                },
                "body_markdown": (
                    "### Streaming Tokens (`SSE`) & Gateway-Worker Queues\n"
                    "When an LLM generates 200 words, waiting until the end feels slow. `StreamingResponse` yields tokens one-by-one as they generate, while heavy batch jobs go onto a queue (`asyncio.Queue` / Redis) for background workers."
                ),
                "code_example": {
                    "title": "Streaming Tokens via Server-Sent Events (SSE)",
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
                        "            await asyncio.sleep(0.05)\n"
                        "    return StreamingResponse(token_generator(), media_type='text/event-stream')\n"
                    ),
                },
                "common_mistakes": [
                    "Running slow synchronous PyTorch/CPU code directly inside `async def` without `await` (blocks the entire server!).",
                ],
                "key_takeaway": "Let Pydantic validate inputs at the boundary, use `TestClient` for instant tests, and offload heavy work to workers.",
            },
        ],
        "quizzes": [
            {
                "id": "ch08-q1",
                "question": "What HTTP status code does FastAPI automatically return when incoming JSON violates a Pydantic `Field` rule?",
                "options": ["200 OK", "404 Not Found", "422 Unprocessable Entity", "500 Internal Server Error"],
                "correct_index": 2,
                "explanation": "FastAPI validates incoming payloads against your Pydantic `BaseModel` and returns `422` with clear field error details.",
            },
        ],
        "project": {
            "title": "Async Inference Gateway & Background Worker Microservice",
            "workspace_dir": "projects/ch08_inference_microservice",
            "overview": "Build a decoupled FastAPI Gateway + async background worker queue with `TestClient` tests.",
            "architecture_steps": [
                "Define shared Pydantic schemas.",
                "Build Gateway endpoints + SSE stream.",
                "Build async worker loop and test with `TestClient`.",
            ],
            "milestones": [
                {"id": "ch08-m1", "label": "Create Pydantic contracts"},
                {"id": "ch08-m2", "label": "Build FastAPI gateway + SSE endpoint"},
                {"id": "ch08-m3", "label": "Build async worker & pass TestClient pytest"},
            ],
        },
    },
    {
        "id": "ch09",
        "number": 9,
        "phase": 2,
        "phase_title": "Phase 2: The AI Engineer's Data, API & Container Stack",
        "title": "Docker & Reproducible AI Environments",
        "subtitle": "Images vs containers, Dockerfile syntax, layer caching, docker-compose networking, and GPU passthrough.",
        "status_type": "available",
        "estimated_hours": 4,
        "why_it_matters": (
            "AI stacks break when Python versions, C++ libraries, or CUDA drivers differ between your PC and a server. "
            "Docker packages the exact OS, Python, and libraries into one portable container."
        ),
        "just_in_time_tags": ["Dockerfile", "Images vs Containers", "Layer Caching", "docker-compose", ".dockerignore"],
        "visualizer": None,
        "sections": [
            {
                "id": "ch09-s1",
                "title": "9.1 `Dockerfile` Syntax, Layer Caching & `docker-compose`",
                "zero_assumption_note": "Note: Docker isn't installed on this PC yet—install Docker Desktop for Windows (WSL 2) when ready to run containers locally.",
                "definition": (
                    "- **Dockerfile:** A step-by-step recipe listing what OS, Python packages, and code to install.\n"
                    "- **Image:** The built, read-only snapshot produced from a Dockerfile.\n"
                    "- **Container:** A live running instance of an image (like running a program from an `.exe`)."
                ),
                "syntax_box": {
                    "title": "Standard Python Dockerfile Instructions",
                    "syntax": (
                        "FROM python:3.12-slim                  # 1. Base OS + Python image (pin version!)\n"
                        "WORKDIR /app                           # 2. Folder inside the container\n"
                        "COPY requirements.txt .                # 3. Copy dependency list FIRST\n"
                        "RUN pip install --no-cache-dir -r requirements.txt  # 4. Install deps (cached!)\n"
                        "COPY app/ ./app/                       # 5. Copy your code LAST\n"
                        "CMD [\"uvicorn\", \"app.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]"
                    ),
                    "breakdown": [
                        "`FROM`: never use `:latest` (pin `3.12-slim` so builds don't break next year).",
                        "`COPY requirements.txt` *before* `COPY app/`: Docker caches each step. If you only edit `.py` code, steps 1–4 stay cached and rebuild in 1 second!",
                        "`0.0.0.0`: required inside containers so connections from outside the container can reach your API.",
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
                        "`services:` lists every container to launch together via `docker compose up`.",
                        "`ports: ['8000:8000']` exposes container port 8000 to your Windows browser at `localhost:8000`.",
                        "Inside `gateway`, code connects to `redis://redis:6379` (using the service name `redis`, NOT `localhost`!).",
                    ],
                },
                "body_markdown": (
                    "### Always Include a `.dockerignore` File\n"
                    "Just like `.gitignore`, a `.dockerignore` listing `.venv`, `__pycache__`, and huge `.pt` model files keeps Docker from copying gigabytes of junk into your image."
                ),
                "code_example": {
                    "title": "Sample `.dockerignore` + Healthcheck",
                    "code": (
                        "# .dockerignore\n"
                        ".venv/\n"
                        "__pycache__/\n"
                        "*.db\n"
                        ".git/\n"
                    ),
                },
                "common_mistakes": [
                    "Putting `COPY . .` *above* `RUN pip install` (forces a slow full `pip install` on every single code edit!).",
                    "Using `localhost` inside container A to reach container B (inside a container, `localhost` means *itself*, not the other service!).",
                ],
                "key_takeaway": "Pin base tags, copy `requirements.txt` before source code, add `.dockerignore`, and talk between compose services by service name.",
            },
        ],
        "quizzes": [
            {
                "id": "ch09-q1",
                "question": "Inside a `docker-compose` network, how should the `gateway` container call the `worker` container?",
                "options": [
                    "http://localhost:8001",
                    "http://worker:8001 (using the Compose service name)",
                    "http://127.0.0.1:8001",
                    "Containers cannot talk to each other",
                ],
                "correct_index": 1,
                "explanation": "Each container has its own `localhost`; Docker Compose provides internal DNS by service name (`worker`).",
            },
        ],
        "project": {
            "title": "Containerized Microservice Stack (API + Worker)",
            "workspace_dir": "projects/ch09_dockerized_stack",
            "overview": "Package the Chapter 8 Gateway and Worker with `.dockerignore`, layer-cached Dockerfiles, and `docker-compose.yml`.",
            "architecture_steps": [
                "Install Docker Desktop for Windows (WSL 2).",
                "Write `.dockerignore` and layer-cached `Dockerfile` files.",
                "Create `docker-compose.yml` with healthchecks and service networking.",
            ],
            "milestones": [
                {"id": "ch09-m1", "label": "Create .dockerignore & layer-cached Dockerfiles"},
                {"id": "ch09-m2", "label": "Write docker-compose.yml with healthchecks"},
                {"id": "ch09-m3", "label": "Validate stack build in Docker Desktop"},
            ],
        },
    },
]
