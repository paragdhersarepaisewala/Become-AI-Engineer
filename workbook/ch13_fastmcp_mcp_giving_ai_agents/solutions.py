"""Reference solutions with explanations."""


# --- 13.1: Build an MCP Tool Server (`MCPServer` & `@mcp.tool`) ---
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


# --- 13.2: MCP File-Note Tool & Resource With Path Safety ---
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
