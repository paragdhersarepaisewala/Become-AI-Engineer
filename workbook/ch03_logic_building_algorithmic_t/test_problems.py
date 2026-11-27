"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_03_01_basic() -> None:
    assert sol.compress_runs('aaabbc') == 'a3b2c1'


def test_wb_03_01_single_empty() -> None:
    assert sol.compress_runs('z') == 'z1'
    assert sol.compress_runs('') == ''


def test_wb_03_02_found() -> None:
    assert sol.first_unique_index('loveai') == 0
    assert sol.first_unique_index('aabc') == 2


def test_wb_03_02_none() -> None:
    assert sol.first_unique_index('aabb') == -1
    assert sol.first_unique_index('') == -1


def test_wb_03_03_examples() -> None:
    assert sol.longest_unique_len('abcabcbb') == 3
    assert sol.longest_unique_len('pwwkew') == 3


def test_wb_03_03_edge_cases() -> None:
    assert sol.longest_unique_len('') == 0
    assert sol.longest_unique_len('bbbb') == 1


def test_wb_03_04_nested() -> None:
    assert sol.flatten([1, [2, [3, 4]], [], 5]) == [1, 2, 3, 4, 5]


def test_wb_03_04_empty() -> None:
    assert sol.flatten([[], [[]]]) == []
