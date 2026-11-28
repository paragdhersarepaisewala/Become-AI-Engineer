"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_10_01_valid_and_invalid_article() -> None:
    from pydantic import ValidationError
    a = sol.Article(title='  Learn Pydantic ', views='12')
    assert a.title == 'Learn Pydantic' and a.views == 12 and a.tags == []
    for bad in [{'title': '  '}, {'title': 'hi'}, {'title': 'Valid', 'views': -1}]:
        try:
            sol.Article(**bad)
            assert False
        except ValidationError:
            pass


def test_wb_10_02_batch_filter() -> None:
    rows = [{'prompt': 'Explain AI', 'score': 5}, {'prompt': 'No', 'score': 5}, {'prompt': 'Good prompt', 'score': 9}]
    out = sol.filter_valid_prompts(rows)
    assert len(out) == 1 and out[0].prompt == 'Explain AI'
