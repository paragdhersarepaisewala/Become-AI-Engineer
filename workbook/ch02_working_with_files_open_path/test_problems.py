"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_02_01_counts_and_missing() -> None:
    import tempfile
    from pathlib import Path
    with tempfile.TemporaryDirectory() as d:
        assert sol.count_non_empty_lines(Path(d) / 'nope.txt') == 0
        p = Path(d) / 'notes.txt'
        p.write_text('alpha\n\n   \nbeta\n', encoding='utf-8')
        assert sol.count_non_empty_lines(p) == 2


def test_wb_02_02_filters_corrupt_and_short() -> None:
    import json, tempfile
    from pathlib import Path
    with tempfile.TemporaryDirectory() as d:
        src = Path(d) / 'in.jsonl'
        dst = Path(d) / 'nested' / 'out.jsonl'
        src.write_text('{"text": "hello world"}\n{broken\n{"text": "hi"}\n', encoding='utf-8')
        assert sol.filter_jsonl_file(src, dst, min_chars=5) == 1
        assert json.loads(dst.read_text(encoding='utf-8').strip()) == {'text': 'hello world'}


def test_wb_02_03_counts_csv() -> None:
    import tempfile
    from pathlib import Path
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / 'data.csv'
        p.write_text('id,label\n1, pos \n2,\n3,neg\n4,pos\n', encoding='utf-8')
        assert sol.count_csv_labels(p) == {'pos': 2, 'neg': 1}
