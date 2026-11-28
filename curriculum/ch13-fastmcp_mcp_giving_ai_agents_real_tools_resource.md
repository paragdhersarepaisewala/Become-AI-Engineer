# Chapter 13: FastMCP (`mcp`) — Giving AI Agents Real Tools & Resources

*What MCP is, creating an MCP server, @mcp.tool(), @mcp.resource(), Pydantic-typed tool inputs, and testing tool calls in Python.*

**Why It Matters:** Modern AI assistants (Claude, Cursor, Antigravity, custom agents) use **MCP (Model Context Protocol)** to safely read your files, query databases, and run automations. FastMCP lets you expose any Python function to an AI agent in 10 lines!

**Skills Covered:** FastMCP / MCPServer, @mcp.tool(), @mcp.resource(), Agent Tools, Structured Output


---

## 13.1 What Is MCP? + Building Your First Tool With `@mcp.tool()`

> **Before You Start:** Note on imports: in `mcp` v1.x or the standalone `fastmcp` package, you import `from fastmcp import FastMCP`. In the official `mcp` v2.0 SDK installed on this computer, it is named `MCPServer` (`from mcp.server.mcpserver import MCPServer`)—with the exact same decorators!

### 1. Definition
**MCP (Model Context Protocol)** is a standard USB-C port for AI models: instead of writing custom glue code for every AI app, you build **one MCP server** exposing `@mcp.tool()` actions and `@mcp.resource()` read-only data, and any MCP-compatible AI can use it.

### 2. Exact Syntax — Creating an MCP Server With Tools & Resources
```python
from mcp.server.mcpserver import MCPServer  # (or `FastMCP` in fastmcp pkg)

mcp = MCPServer('my-assistant-tools')

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two integers together."""
    return a + b

@mcp.resource('info://version')
def get_version() -> str:
    return '1.0.0'
```

- `@mcp.tool()` turns a typed Python function into an action an AI agent can call! **Always write a clear docstring**—the AI reads that docstring to know *when* to call your tool.
- `@mcp.resource('uri://...')` exposes read-only data (like config files or logs) by URI.
- `mcp.run()` starts the server over stdio so AI hosts (Cursor, Claude Desktop, Antigravity) can talk to it.

### 3. Tiny Example (Line-by-Line) — Registering & Calling an MCP Tool in Python
```python
import asyncio
from mcp.server.mcpserver import MCPServer

mcp = MCPServer('word-tools')

@mcp.tool()
def count_words(text: str) -> int:
    """Count whitespace-separated words in text."""
    return len(text.split())

tools = asyncio.run(mcp.list_tools())
result = asyncio.run(mcp.call_tool('count_words', {'text': 'hello mcp world'}))
print('Registered:', [t.name for t in tools])
print('Result:', result.structured_content)
```

1. Creates an `MCPServer` named `'word-tools'`.
2. `@mcp.tool()` automatically inspects `text: str -> int` and builds a JSON schema for the AI.
3. `mcp.list_tools()` shows `['count_words']`, and `mcp.call_tool(...)` runs it and returns `{'result': 3}`!

### Connecting Files & Automations Into MCP Tools
Think about everything you built in Chapters 2, 3, 10, and 11 (`open`/`Path` file reading, `os` folder inspection, `Pydantic` validation, `requests` API calls): wrapping those functions with `@mcp.tool()` immediately turns them into safe tools an AI assistant can call!


### 4. Practical Example — File-Reading & Note-Saving MCP Tool Server

```python
import asyncio, tempfile
from pathlib import Path
from mcp.server.mcpserver import MCPServer

mcp = MCPServer('notes-server')

with tempfile.TemporaryDirectory() as tmp:
    notes_dir = Path(tmp)

    @mcp.tool()
    def save_note(filename: str, body: str) -> str:
        """Save a plain text note safely inside notes_dir."""
        safe_name = Path(filename).name  # prevents ../ path traversal!
        target = notes_dir / safe_name
        target.write_text(body, encoding='utf-8')
        return f'Saved {safe_name}'

    @mcp.resource('notes://list')
    def list_notes() -> str:
        return ', '.join(p.name for p in notes_dir.glob('*.txt'))

    res = asyncio.run(mcp.call_tool('save_note', {'filename': 'todo.txt', 'body': 'Learn MCP'}))
    listing = asyncio.run(mcp.read_resource('notes://list'))
    print(res.structured_content, '| Notes:', listing[0].content)
```

### Common Mistakes to Avoid

- Forgetting type hints or docstrings on `@mcp.tool()` functions (the AI won't know what arguments to pass or when to use the tool!).
- Using raw user-supplied `filename` without `Path(filename).name` (lets a caller pass `../../secret.txt`!).

**Key Takeaway:** Type hints + clear docstrings + `@mcp.tool()` turn any safe Python file/API automation into a standard AI-agent tool.


---

## Hands-On Project: Local Workspace Notes & Search MCP Server

Build a real MCP server exposing `@mcp.tool()` note-saving/searching functions and `@mcp.resource()` file listings with path-traversal safety.

1. Create `MCPServer('workspace-notes')`.
2. Implement `@mcp.tool()` functions to save and search `.txt` notes safely.
3. Implement `@mcp.resource()` listing available notes and verify with `pytest`.
