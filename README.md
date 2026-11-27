# Become AI Engineer — Interactive Course, Practice Workbook & Learning Tracker

A project-based, zero-assumptions learning platform designed to take an intermediate Python scripter to a strong AI Engineer—covering Python fundamentals, file handling, OOP, logic building, DSA & Dynamic Programming, `asyncio`, NumPy, Pandas, FastAPI microservices, Docker, and a full Phase 3–4 roadmap into PyTorch, Transformers, Small LLM pre-training, QLoRA fine-tuning, and LangChain.

## What Is Included

1. **Structured Course (`curriculum/` & Web Course Reader)**
   - **Phase 1–2 (Chapters 1–9, Complete):** Every section follows a consistent **Definition → Exact Syntax → Tiny Line-by-Line Example → Practical Example → Common Mistakes** format, with interactive visualizers (Call Stack Stepper, 2D DP Table Stepper, Asyncio Event Loop Timeline, NumPy Broadcasting Explorer), quizzes, personal notes, and live **Run Code** buttons.
   - **Phase 3–4 (Chapters 10–15, Roadmap):** Classical ML & evaluation, Tiny Autograd & PyTorch internals, Transformers from scratch, pre-training Small LLMs, fine-tuning (SFT/LoRA/QLoRA/DPO), and LangChain (LCEL), RAG & serving.
2. **Separate Practice Workbook (`workbook/` & Web Workbook Tab)**
   - 28 hands-on coding & logic drills across Chapters 1–9 (`exercises.md`, `problems.py`, `solutions.py`, `test_problems.py`), each with a **Logic Thinking Blueprint**, progressive hints, **Dry-Run Trace Table**, reference answer & explanation, and automated Python test verification.
3. **Project-Based Learning Hub (`projects/` & Web Projects Tab)**
   - Practical per-chapter projects with architecture steps, starter code, and milestone tracking stored in SQLite.

---

## Prerequisites

- **Python** `3.11+` (tested on Python `3.13.11`)
- **Node.js** `18+` and **npm** (tested on Node `v25.6.1`)
- **Git**
- *(Optional for Chapter 9)* **Docker Desktop**

---

## Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/paragdhersarepaisewala/Become-AI-Engineer.git
cd Become-AI-Engineer
```

### 2. Install Backend Dependencies (Python)
Create a virtual environment (recommended) and install backend packages:

**Windows (PowerShell):**
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd ..
```

**macOS / Linux:**
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd ..
```

### 3. Install Frontend Dependencies (Node.js)
```bash
cd frontend
npm install
cd ..
```

---

## Running the Application

### Option A: One-Command Launch on Windows PowerShell
```powershell
.\start.ps1
```
Then open **http://localhost:5175** in your browser.

### Option B: Manual Launch (Any OS)
**Terminal 1 — Start FastAPI Backend (`http://127.0.0.1:8050`):**
```bash
cd backend
python -m uvicorn app.main:app --reload --port 8050
```

**Terminal 2 — Start React Frontend (`http://localhost:5175`):**
```bash
cd frontend
npm run dev
```
Open **http://localhost:5175** in your browser. Your learning progress, quiz answers, workbook code drafts, and streaks are saved locally in `backend/learning_tracker.db` (ignored by Git).

---

## Running Tests & Syncing Workspace Files

- **Verify backend API + all 28 workbook reference solutions:**
  ```bash
  cd backend
  python -m pytest -v
  ```
- **Practice workbook exercises in VS Code / terminal:**
  Edit `problems.py` inside any `workbook/chXX_.../` folder and run:
  ```bash
  python -m pytest workbook/ch01_python_basics_from_ground_zero_/test_problems.py
  ```
- **Regenerate mirrored `curriculum/`, `workbook/`, and `projects/` files after editing `backend/app/data/`:**
  ```bash
  cd backend
  python -m app.sync_workspace
  ```

---

## Repository Structure

```text
├── backend/
│   ├── app/
│   │   ├── data/              # Structured chapters (Ch 1–15) & workbook drills
│   │   ├── database.py        # SQLite progress, workbook attempts & streak tracking
│   │   ├── main.py            # FastAPI REST endpoints
│   │   ├── runner.py          # Isolated subprocess Python & test runner
│   │   └── sync_workspace.py  # Exports curriculum/, workbook/, and projects/
│   ├── tests/                 # API & workbook reference solution pytest suites
│   └── requirements.txt
├── frontend/                  # Vite + React + TypeScript UI & visualizers
├── curriculum/                # Readable Markdown roadmap & chapter lessons
├── workbook/                  # Standalone Markdown sheets, starter .py & pytest files
├── projects/                  # Hands-on project specs & starter code
└── start.ps1                  # Windows one-command dev launcher
```
