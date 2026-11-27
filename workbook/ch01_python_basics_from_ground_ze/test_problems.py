"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_01_00a_mixed_scores() -> None:
    assert sol.grade_summary([40, 60, 85, 59]) == {'passed': 2, 'failed': 2}


def test_wb_01_00a_empty_list() -> None:
    assert sol.grade_summary([]) == {'passed': 0, 'failed': 0}


def test_wb_01_00b_clean_values() -> None:
    assert sol.format_badge({'name': '  Sara ', 'role': ' ENGINEER '}) == 'Sara (engineer)'


def test_wb_01_00b_missing_keys() -> None:
    assert sol.format_badge({}) == 'Guest (learner)'
    assert sol.format_badge({'name': '   ', 'role': None}) == 'Guest (learner)'


def test_wb_01_00c_counts_and_missing() -> None:
    import tempfile
    from pathlib import Path
    with tempfile.TemporaryDirectory() as d:
        missing = Path(d) / 'nope.txt'
        assert sol.count_non_empty_lines(missing) == 0
        p = Path(d) / 'notes.txt'
        p.write_text('alpha\n\n   \nbeta\n', encoding='utf-8')
        assert sol.count_non_empty_lines(p) == 2


def test_wb_01_01_fresh_default_calls() -> None:
    assert sol.add_tag('a') == ['a']
    assert sol.add_tag('b') == ['b']


def test_wb_01_01_no_caller_mutation() -> None:
    base = ['ai']
    out = sol.add_tag('ml', base)
    assert out == ['ai', 'ml']
    assert base == ['ai']


def test_wb_01_01_dedup_existing_tag() -> None:
    assert sol.add_tag('ai', ['ai', 'py']) == ['ai', 'py']


def test_wb_01_02_filters_corrupt_and_short_lines() -> None:
    import json, tempfile
    from pathlib import Path
    with tempfile.TemporaryDirectory() as d:
        src = Path(d) / 'in.jsonl'
        dst = Path(d) / 'nested' / 'out.jsonl'
        src.write_text('{"text": "hello world"}\n{broken\n{"text": "hi"}\n\n', encoding='utf-8')
        n = sol.filter_jsonl_file(src, dst, min_chars=5)
        assert n == 1
        lines = dst.read_text(encoding='utf-8').strip().splitlines()
        assert json.loads(lines[0]) == {'text': 'hello world'}


def test_wb_01_03_counts_csv_safely() -> None:
    import tempfile
    from pathlib import Path
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / 'data.csv'
        p.write_text('id,label\n1, pos \n2,\n3,neg\n4,pos\n', encoding='utf-8')
        assert sol.count_csv_labels(p) == {'pos': 2, 'neg': 1}
