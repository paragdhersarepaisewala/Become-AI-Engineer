# AI Engineer Academy — 15-Chapter Master Roadmap

Zero assumed knowledge. Logic, OOP, DSA, DP, Async, Docker, and Microservices taught just-in-time.



## Phase 1: Python Foundations, OOP & Logic Building

- **Chapter 1: Python Basics From Ground Zero & Working With Files** (Available, ~6h) — Variables, basic types, if/else, loops, lists, dicts, functions, opening/loading files (open, pathlib, json, csv), and clean script structure.
- **Chapter 2: Object-Oriented Programming (OOP) & Breaking the Monolith** (Available, ~5h) — Classes, self, __init__, dataclasses, composition vs inheritance, dunder methods (__call__, __len__), and modular files.
- **Chapter 3: Logic Building & Algorithmic Thinking** (Available, ~6h) — How to plan on paper, trace variables in tables, and master core patterns (hash maps, two pointers, sliding window, recursion).
- **Chapter 4: Essential DSA & Dynamic Programming Demystified** (Available, ~7h) — Big-O speed intuition, Queues, Heaps, Graphs (DAGs), and Dynamic Programming built step-by-step from recursion to tables.
- **Chapter 5: Concurrency, Async Programming & Event Loops** (Available, ~5h) — Waiting vs computing, the GIL, async def, await, asyncio.gather, Semaphores, and safe retries.

## Phase 2: The AI Engineer's Data, API & Container Stack

- **Chapter 6: NumPy & Vectorized Linear Algebra** (Available, ~5h) — Arrays, shapes, axes, broadcasting rules, dot products, cosine similarity, and stable softmax.
- **Chapter 7: Pandas & Production Data Curation** (Available, ~5h) — DataFrames, loc vs iloc, filtering, string cleaning, groupby summaries, and hash deduplication.
- **Chapter 8: FastAPI & Microservice Architecture** (Available, ~6h) — HTTP endpoints, Pydantic validation, async vs sync routes, SSE token streaming, and Gateway + Worker microservices.
- **Chapter 9: Docker & Reproducible AI Environments** (Available, ~4h) — Images vs containers, Dockerfile syntax, layer caching, docker-compose networking, and GPU passthrough.

## Phase 3: Machine Learning & Deep Learning Under the Hood

- **Chapter 10: Classical ML & Rigorous Evaluation** (Roadmap (Phase 3–4), ~6h) — Train/val/test splits, data leakage prevention, gradient descent, logistic regression, trees, and metric tradeoffs.
- **Chapter 11: Neural Networks, Autograd & PyTorch Internals** (Roadmap (Phase 3–4), ~7h) — Computation graphs, building a tiny autograd engine from scratch, nn.Module (OOP in action!), DataLoaders, and CUDA mixed precision.

## Phase 4: Transformers, Small LLMs, Fine-Tuning & LangChain

- **Chapter 12: Tokenization, Attention & Transformer Architecture** (Roadmap (Phase 3–4), ~8h) — BPE tokenization from scratch, RoPE positional encoding, Causal Multi-Head Attention, RMSNorm, SwiGLU, and KV-cache.
- **Chapter 13: Pre-Training a Small Language Model (SLM)** (Roadmap (Phase 3–4), ~8h) — Token packing, cosine LR schedules, gradient accumulation, VRAM math on your RTX 5070 Ti (16GB), and text decoding.
- **Chapter 14: Fine-Tuning LLMs (SFT, LoRA, QLoRA & DPO)** (Roadmap (Phase 3–4), ~8h) — Chat templates, prompt loss masking, LoRA rank/alpha math, 4-bit QLoRA on 16GB VRAM, and preference alignment.
- **Chapter 15: LangChain (LCEL), RAG, Agents, Evals & LLM Serving** (Roadmap (Phase 3–4), ~9h) — LangChain Runnables & LCEL composition, hybrid RAG, structured tool calling, LangGraph/agent loops, automated evals, and vLLM serving.
