"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_13_01_mcp_tools() -> None:
    import asyncio
    names = [t.name for t in asyncio.run(sol.mcp.list_tools())]
    assert 'word_count' in names and 'multiply' in names
    r1 = asyncio.run(sol.mcp.call_tool('word_count', {'text': 'hello mcp world'}))
    r2 = asyncio.run(sol.mcp.call_tool('multiply', {'a': 6, 'b': 7}))
    assert r1.structured_content == {'result': 3}
    assert r2.structured_content == {'result': 42}


def test_wb_13_02_safe_notes_mcp() -> None:
    import asyncio, tempfile
    from pathlib import Path
    with tempfile.TemporaryDirectory() as d:
        srv = sol.build_notes_server(Path(d))
        res = asyncio.run(srv.call_tool('write_note', {'filename': '../../a.txt', 'content': 'hello'}))
        assert res.structured_content == {'result': 'Saved a.txt'}
        assert (Path(d) / 'a.txt').read_text(encoding='utf-8') == 'hello'
        cnt = asyncio.run(srv.read_resource('notes://count'))
        assert cnt[0].content == '1'
