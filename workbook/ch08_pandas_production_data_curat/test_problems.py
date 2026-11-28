"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_08_01_dedup_filter() -> None:
    import pandas as pd
    df = pd.DataFrame([{'id': 1, 'text': '  Hello   AI world  ', 'score': 0.5}, {'id': 2, 'text': None, 'score': 0.9}, {'id': 3, 'text': 'short', 'score': 0.9}, {'id': 4, 'text': 'hello ai world', 'score': 0.95}])
    res = sol.clean_corpus(df, min_len=10)
    assert list(res['id']) == [4] and res.loc[0, 'clean_text'] == 'hello ai world'


def test_wb_08_02_source_summary() -> None:
    import pandas as pd
    df = pd.DataFrame([{'source': 'wiki', 'tokens': 100, 'is_valid': True}, {'source': 'wiki', 'tokens': 200, 'is_valid': False}, {'source': 'arxiv', 'tokens': 300, 'is_valid': True}])
    res = sol.summarize_sources(df)
    assert list(res['source']) == ['arxiv', 'wiki'] and res.loc[1, 'valid_rows'] == 1 and res.loc[1, 'avg_tokens'] == 150.0
