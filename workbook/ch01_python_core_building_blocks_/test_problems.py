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


def test_wb_01_03_default_and_custom() -> None:
    assert sol.apply_discount(100) == 90.0
    assert sol.apply_discount(80, 25) == 60.0


def test_wb_01_03_invalid_inputs() -> None:
    try:
        sol.apply_discount(-10)
        assert False
    except ValueError:
        pass
