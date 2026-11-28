"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_01_01_mixed_scores() -> None:
    assert sol.grade_summary([40, 60, 85, 59]) == {'passed': 2, 'failed': 2}


def test_wb_01_01_empty_list() -> None:
    assert sol.grade_summary([]) == {'passed': 0, 'failed': 0}


def test_wb_01_02_clean_and_skip() -> None:
    assert sol.clean_names(['  Sara ', '', ' ALEX ', '   ']) == ['sara', 'alex']


def test_wb_01_02_all_blank() -> None:
    assert sol.clean_names(['', '  ']) == []


def test_wb_01_03_fresh_defaults() -> None:
    assert sol.add_tag('a') == ['a']
    assert sol.add_tag('b') == ['b']


def test_wb_01_03_no_mutation() -> None:
    base = ['ai']
    assert sol.add_tag('ml', base) == ['ai', 'ml'] and base == ['ai']
