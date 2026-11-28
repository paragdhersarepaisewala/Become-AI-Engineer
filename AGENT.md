# AGENT.md — Repository Maintenance & Curriculum Guidelines

Follow these instructions on every update to **Become AI Engineer**.

## 1. Mandatory Verification & Git Push Workflow
After **every** course update, workbook addition, or web software upgrade:
1. Sync the mirrored workspace files (`curriculum/`, `workbook/`, `projects/`):
   ```powershell
   cd backend
   python -m app.sync_workspace
   ```
2. Run the full backend & workbook test suite (all tests must pass):
   ```powershell
   python -m pytest -v
   ```
3. Verify the TypeScript & Vite frontend build:
   ```powershell
   cd ..\frontend
   npm run build
   ```
4. Commit all updated files with a clear message and **push to `origin main`** (`https://github.com/paragdhersarepaisewala/Become-AI-Engineer.git`):
   ```powershell
   cd ..
   git add -A
   git commit -m "<concise summary of course/software upgrade>"
   git push origin main
   ```

## 2. Curriculum Authoring Rules (Beginner-First)
- **One Library Per Chapter:** Keep major libraries in dedicated chapters (`os`, `numpy`, `pandas`, `pydantic`, `requests`, `fastapi`, `fastmcp`, `docker`). Never cram unrelated libraries together.
- **Strict 5-Part Section Format:** Every lesson section must follow:
  1. **Before You Start** (plain-English context)
  2. **1. Definition (What Is It?)**
  3. **2. Exact Syntax** + symbol/keyword breakdown
  4. **3. Tiny Example (Line-by-Line)**
  5. **4. Practical Example** + **Common Mistakes to Avoid** + **Key Takeaway**
- **Zero Unintroduced Jargon or Syntax:** Never use syntax (e.g., inline ternaries `a if cond else b`, union types `| None`, `lambda`, or decorators) before explicitly teaching it.
- **Files & Simple Automations:** Include practical file reading/writing and small real-world automation projects (`os` file organizer, `requests` API saver, `FastMCP` tool server).
- **Live Runnable Examples:** Ensure **Run Code** always shows clear `stdout`/`stderr` output in both Course lessons and Practice Workbook exercises.
