"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_06_01_small_60() -> None:
    assert [sol.climb_ways(i) for i in range(6)] == [1, 1, 2, 3, 5, 8]
    assert sol.climb_ways(60) == 2504730781961


def test_wb_06_02_coins() -> None:
    assert sol.min_coins([1, 3, 4], 6) == 2
    assert sol.min_coins([2], 3) == -1


def test_wb_06_03_edit() -> None:
    assert sol.edit_distance('kitten', 'sitting') == 3
    assert sol.edit_distance('cat', 'cut') == 1


def test_wb_06_04_dag() -> None:
    assert sol.schedule_tasks(['eval', 'clean', 'train'], [('clean', 'train'), ('train', 'eval')]) == ['clean', 'train', 'eval']
