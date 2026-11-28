# AI Engineer Academy — 15-Chapter Master Roadmap

Zero assumed knowledge. Logic, OOP, DSA, DP, Async, Docker, and Microservices taught just-in-time.



## Phase 1: Python From Zero — Basics, Files, `os`, OOP & Logic

- **Chapter 1: Python Core Building Blocks (From Scratch)** (Available, ~6h) — Variables, types, if/else decisions, for & while loops, lists/dicts/sets, one-line loops (comprehensions), and functions.
- **Chapter 2: Working With Files (`open`, `pathlib`, `json`, `csv`)** (Available, ~5h) — Reading & writing plain .txt files, pathlib.Path, try/except error handling, JSON/JSONL datasets, and CSV spreadsheets.
- **Chapter 3: The `os` Library & Simple File Automations** (Available, ~4h) — Inspecting folders (os.listdir, os.walk), joining paths (os.path), creating/renaming files & folders, and environment variables (os.getenv).
- **Chapter 4: Object-Oriented Programming (OOP) From Ground Zero** (Available, ~6h) — Why classes exist, __init__ & self, protecting state with methods, __repr__ & @dataclass, composition, and splitting files.
- **Chapter 5: Logic Building Step-by-Step (Think Before You Code)** (Available, ~7h) — Paper dry-runs, accumulators (manual max/min/sum), filtering, grouping, nested loops, and gentle transition to faster patterns.
- **Chapter 6: Essential DSA & Dynamic Programming Demystified** (Available, ~7h) — Big-O intuition, Queues (deque), Heaps (heapq), Graphs (BFS & DAGs), and Dynamic Programming from recursion to tables.
- **Chapter 7: Concurrency, Async Programming & Event Loops** (Available, ~5h) — Waiting vs computing, async def, await, asyncio.gather, Semaphores, and exponential backoff retries.

## Phase 2: AI Engineering Libraries (One Library Per Chapter)

- **Chapter 8: NumPy — Arrays, Shapes & Vectorized Math** (Available, ~5h) — Arrays vs Python lists, .shape, axis=0 vs axis=1, broadcasting rules, dot products (@), cosine similarity, and stable softmax.
- **Chapter 9: Pandas — DataFrames, Cleaning & Data Pipelines** (Available, ~5h) — Series & DataFrames, reading/writing CSV & JSON, loc vs iloc, filtering, .str cleaning, groupby, and deduplication.
- **Chapter 10: Pydantic — Data Validation, Models & Serialization** (Available, ~5h) — BaseModel, automatic type checking, Field constraints, @field_validator, nested models, ValidationError, and JSON serialization.
- **Chapter 11: Requests — Calling HTTP APIs & Web Automations** (Available, ~5h) — GET vs POST, status codes (200/404/429), query params, headers & API keys, timeouts, try/except, and saving API data with Pydantic.
- **Chapter 12: FastAPI — Building Typed Web APIs & Microservices** (Available, ~6h) — GET/POST routes, Pydantic request contracts, path/query params, TestClient, SSE streaming, and Gateway + Worker microservices.
- **Chapter 13: FastMCP (`mcp`) — Giving AI Agents Real Tools & Resources** (Available, ~5h) — What MCP is, creating an MCP server, @mcp.tool(), @mcp.resource(), Pydantic-typed tool inputs, and testing tool calls in Python.
- **Chapter 14: Docker — Reproducible Containers & Multi-Service Stacks** (Available, ~4h) — Images vs containers, Dockerfile syntax, layer caching, docker-compose networking, and GPU passthrough.

## Phase 3: Machine Learning & Deep Learning Under the Hood

- **Chapter 15: Classical ML & Rigorous Evaluation** (Roadmap (Phase 3–4), ~6h) — Train/val/test splits, data leakage prevention, gradient descent, logistic regression, trees, and metric tradeoffs.
- **Chapter 16: Neural Networks, Autograd & PyTorch Internals** (Roadmap (Phase 3–4), ~7h) — Computation graphs, building a tiny autograd engine from scratch, nn.Module, DataLoaders, and CUDA mixed precision.

## Phase 4: Transformers, Small LLMs, Fine-Tuning & LangChain

- **Chapter 17: Tokenization, Attention & Transformer Architecture** (Roadmap (Phase 3–4), ~8h) — BPE tokenization from scratch, RoPE positional encoding, Causal Multi-Head Attention, RMSNorm, SwiGLU, and KV-cache.
- **Chapter 18: Pre-Training a Small Language Model (SLM)** (Roadmap (Phase 3–4), ~8h) — Token packing, cosine LR schedules, gradient accumulation, VRAM math on your RTX 5070 Ti (16GB), and text decoding.
- **Chapter 19: Fine-Tuning LLMs (SFT, LoRA, QLoRA & DPO)** (Roadmap (Phase 3–4), ~8h) — Chat templates, prompt loss masking, LoRA rank/alpha math, 4-bit QLoRA on 16GB VRAM, and preference alignment.
- **Chapter 20: LangChain (LCEL), RAG, Agents, Evals & LLM Serving** (Roadmap (Phase 3–4), ~9h) — LangChain Runnables & LCEL composition, hybrid RAG, structured tool calling, LangGraph/agent loops, automated evals, and vLLM serving.
