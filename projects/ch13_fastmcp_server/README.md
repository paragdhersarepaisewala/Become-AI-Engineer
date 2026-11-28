# Project (Chapter 13): Local Workspace Notes & Search MCP Server

Build a real MCP server exposing `@mcp.tool()` note-saving/searching functions and `@mcp.resource()` file listings with path-traversal safety.

## Architecture Steps

1. Create `MCPServer('workspace-notes')`.
2. Implement `@mcp.tool()` functions to save and search `.txt` notes safely.
3. Implement `@mcp.resource()` listing available notes and verify with `pytest`.

## Milestones

- [ ] Create MCPServer with typed @mcp.tool() functions
- [ ] Add @mcp.resource() & path-traversal filename guard
- [ ] Verify tool calls & resources with pytest
