"""Starter exercises — implement each function and run pytest on test_problems.py."""


# --- 13.1: Build an MCP Tool Server (`MCPServer` & `@mcp.tool`) ---
from mcp.server.mcpserver import MCPServer

mcp = MCPServer('math-text-tools')

# TODO: register word_count and multiply with @mcp.tool()


# --- 13.2: MCP File-Note Tool & Resource With Path Safety ---
from pathlib import Path
from mcp.server.mcpserver import MCPServer

def build_notes_server(notes_dir: Path) -> MCPServer:
    mcp = MCPServer('notes-server')
    # TODO: add write_note tool and notes://count resource
    return mcp
