"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_05_01_max_cases() -> None:
    assert sol.find_max([-10, -3, -20]) == -3
    assert sol.find_max([]) is None
    assert sol.find_max([4, 9, 2]) == 9


def test_wb_05_02_group() -> None:
    assert sol.group_by_first_letter(['Apple', '  ', 'ant', 'Ball']) == {'a': ['Apple', 'ant'], 'b': ['Ball']}


def test_wb_05_03_basic() -> None:
    assert sol.compress_runs('aaabbc') == 'a3b2c1'
    assert sol.compress_runs('') == ''


def test_wb_05_04_examples() -> None:
    assert sol.longest_unique_len('abcabcbb') == 3
    assert sol.longest_unique_len('pwwkew') == 3
