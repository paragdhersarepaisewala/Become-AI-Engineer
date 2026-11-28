# Workbook — Chapter 13: FastMCP (`mcp`) — Giving AI Agents Real Tools & Resources


---

## 13.1 Build an MCP Tool Server (`MCPServer` & `@mcp.tool`) (`Foundation` · FastMCP)

Create `mcp = MCPServer('math-text-tools')` (`from mcp.server.mcpserver import MCPServer`) with two `@mcp.tool()` functions:
1. `word_count(text: str) -> int`: returns number of whitespace-separated words.
2. `multiply(a: int, b: int) -> int`: returns `a * b`.

### Thinking Blueprint

- Instantiate `MCPServer`, decorate each typed function with `@mcp.tool()` and a clear docstring.

### Progressive Hints

1. Remember to write type hints (`text: str -> int`) so MCP builds the tool schema automatically.

### Dry-Run Trace
`call_tool('word_count', {'text': 'hello mcp world'})` -> `structured_content == {'result': 3}`.

### Answer & Explanation
```python
from mcp.server.mcpserver import MCPServer

mcp = MCPServer('math-text-tools')

@mcp.tool()
def word_count(text: str) -> int:
    """Count whitespace-separated words in text."""
    return len(text.split())

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b
```

**High-Level Blocks:** Decorated typed functions become standard MCP tools callable by any AI agent.


---

## 13.2 MCP File-Note Tool & Resource With Path Safety (`Intermediate` · FastMCP)

Write `build_notes_server(notes_dir: Path) -> MCPServer` returning an `MCPServer` with:
- `@mcp.tool() def write_note(filename: str, content: str) -> str`: strips directory traversal using `Path(filename).name`, writes UTF-8 text into `notes_dir`, and returns `'Saved <safe_name>'`.
- `@mcp.resource('notes://count') def note_count() -> str`: returns string count of `.txt` files in `notes_dir`.

### Thinking Blueprint

- Sanitize with `safe = Path(filename).name`.
- Use `notes_dir.mkdir(parents=True, exist_ok=True)`.

### Progressive Hints

1. `str(len(list(notes_dir.glob('*.txt'))))`

### Dry-Run Trace
`write_note('../../evil.txt', 'hi')` saves safely as `notes_dir/evil.txt`!

### Answer & Explanation
```python
from pathlib import Path
from mcp.server.mcpserver import MCPServer

def build_notes_server(notes_dir: Path) -> MCPServer:
    notes_dir.mkdir(parents=True, exist_ok=True)
    mcp = MCPServer('notes-server')

    @mcp.tool()
    def write_note(filename: str, content: str) -> str:
        """Save a note safely inside notes_dir."""
        safe_name = Path(filename).name
        (notes_dir / safe_name).write_text(content, encoding='utf-8')
        return f'Saved {safe_name}'

    @mcp.resource('notes://count')
    def note_count() -> str:
        return str(len(list(notes_dir.glob('*.txt'))))

    return mcp
```

**High-Level Blocks:** `Path(filename).name` blocks path-traversal attacks while exposing clean MCP tools & resources.
