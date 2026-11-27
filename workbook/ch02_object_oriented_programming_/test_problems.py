"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_02_01_store_crud_and_dunders() -> None:
    s = sol.DocumentStore()
    s.add(sol.Document('d1', 'Learn PyTorch'))
    s.add(sol.Document('d2', 'Learn FastAPI'))
    assert len(s) == 2 and 'd1' in s and 'd9' not in s
    assert [d.doc_id for d in s.search('pytorch')] == ['d1']
    try:
        s.add(sol.Document('d3', '   '))
        assert False
    except ValueError:
        pass


def test_wb_02_02_composed_pipeline() -> None:
    p = sol.Pipeline([sol.StripWhitespace(), sol.ReplaceWord('ml', 'AI')])
    assert p('  learn   ml   fast ') == 'learn AI fast'


def test_wb_02_03_mixed_logs() -> None:
    assert sol.parse_logs(['[INFO] a', 'bad', '[ERROR] b', '[WARN] c']) == {'INFO': 1, 'WARN': 1, 'ERROR': 1}


def test_wb_02_03_empty_unknown() -> None:
    assert sol.parse_logs(['', '[DEBUG] x']) == {'INFO': 0, 'WARN': 0, 'ERROR': 0}
