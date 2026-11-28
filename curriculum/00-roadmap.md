# AI Engineer Academy — 15-Chapter Master Roadmap

Zero assumed knowledge. Logic, OOP, DSA, DP, Async, Docker, and Microservices taught just-in-time.



## Phase 1: Python From Zero — Basics, Files, OOP & Logic

- **Chapter 1: Python Core Building Blocks (From Scratch)** (Available, ~6h) — Variables, types, if/else decisions, for & while loops, lists/dicts/sets, one-line loops (comprehensions), and functions.
- **Chapter 2: Working With Files & Everyday Built-In Libraries** (Available, ~5h) — Reading & writing .txt files, pathlib.Path, try/except error handling, JSON/JSONL, CSV spreadsheets, and small stdlib helpers.
- **Chapter 3: Object-Oriented Programming (OOP) From Ground Zero** (Available, ~6h) — Why classes exist, __init__ & self, protecting state with methods, __repr__ & @dataclass, objects working together (composition), and splitting files.
- **Chapter 4: Logic Building Step-by-Step (Think Before You Code)** (Available, ~7h) — Paper dry-runs, accumulators (manual max/min/sum), filtering, grouping, nested loops, and gentle transition to faster patterns.
- **Chapter 5: Essential DSA & Dynamic Programming Demystified** (Available, ~7h) — Big-O intuition, Queues (deque), Heaps (heapq), Graphs (BFS & DAGs), and Dynamic Programming from recursion to tables.
- **Chapter 6: Concurrency, Async Programming & Event Loops** (Available, ~5h) — Waiting vs computing, async def, await, asyncio.gather, Semaphores, and exponential backoff retries.

## Phase 2: The AI Engineer's Data, API & Container Stack

- **Chapter 7: NumPy & Vectorized Linear Algebra** (Available, ~5h) — Arrays, shapes, axes, broadcasting rules, dot products, cosine similarity, and stable softmax.
- **Chapter 8: Pandas & Production Data Curation** (Available, ~5h) — DataFrames, loc vs iloc, filtering, string cleaning, groupby summaries, and hash deduplication.
- **Chapter 9: FastAPI & Microservice Architecture** (Available, ~6h) — HTTP endpoints, Pydantic validation, async vs sync routes, SSE token streaming, and Gateway + Worker microservices.
- **Chapter 10: Docker & Reproducible AI Environments** (Available, ~4h) — Images vs containers, Dockerfile syntax, layer caching, docker-compose networking, and GPU passthrough.

## Phase 3: Machine Learning & Deep Learning Under the Hood

- **Chapter 11: Classical ML & Rigorous Evaluation** (Roadmap (Phase 3–4), ~6h) — Train/val/test splits, data leakage prevention, gradient descent, logistic regression, trees, and metric tradeoffs.
- **Chapter 12: Neural Networks, Autograd & PyTorch Internals** (Roadmap (Phase 3–4), ~7h) — Computation graphs, building a tiny autograd engine from scratch, nn.Module (OOP in action!), DataLoaders, and CUDA mixed precision.

## Phase 4: Transformers, Small LLMs, Fine-Tuning & LangChain

- **Chapter 13: Tokenization, Attention & Transformer Architecture** (Roadmap (Phase 3–4), ~8h) — BPE tokenization from scratch, RoPE positional encoding, Causal Multi-Head Attention, RMSNorm, SwiGLU, and KV-cache.
- **Chapter 14: Pre-Training a Small Language Model (SLM)** (Roadmap (Phase 3–4), ~8h) — Token packing, cosine LR schedules, gradient accumulation, VRAM math on your RTX 5070 Ti (16GB), and text decoding.
- **Chapter 15: Fine-Tuning LLMs (SFT, LoRA, QLoRA & DPO)** (Roadmap (Phase 3–4), ~8h) — Chat templates, prompt loss masking, LoRA rank/alpha math, 4-bit QLoRA on 16GB VRAM, and preference alignment.
- **Chapter 16: LangChain (LCEL), RAG, Agents, Evals & LLM Serving** (Roadmap (Phase 3–4), ~9h) — LangChain Runnables & LCEL composition, hybrid RAG, structured tool calling, LangGraph/agent loops, automated evals, and vLLM serving.
