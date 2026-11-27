"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_04_01_small() -> None:
    assert [sol.climb_ways(i) for i in range(6)] == [1, 1, 2, 3, 5, 8]


def test_wb_04_01_large_n60() -> None:
    assert sol.climb_ways(60) == 2504730781961


def test_wb_04_02_non_greedy() -> None:
    assert sol.min_coins([1, 3, 4], 6) == 2


def test_wb_04_02_impossible_zero() -> None:
    assert sol.min_coins([2], 3) == -1
    assert sol.min_coins([1, 5], 0) == 0


def test_wb_04_03_classic() -> None:
    assert sol.edit_distance('kitten', 'sitting') == 3
    assert sol.edit_distance('cat', 'cut') == 1


def test_wb_04_03_empty() -> None:
    assert sol.edit_distance('', 'abc') == 3
    assert sol.edit_distance('ai', 'ai') == 0


def test_wb_04_04_valid_dag() -> None:
    assert sol.schedule_tasks(['eval', 'clean', 'train'], [('clean', 'train'), ('train', 'eval')]) == ['clean', 'train', 'eval']


def test_wb_04_04_cycle() -> None:
    try:
        sol.schedule_tasks(['a', 'b'], [('a', 'b'), ('b', 'a')])
        assert False
    except ValueError:
        pass
