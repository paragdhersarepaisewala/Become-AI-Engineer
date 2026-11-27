"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_06_01_standardize_constant_col() -> None:
    import numpy as np
    x = np.array([[1.0, 5.0], [3.0, 5.0]])
    assert np.allclose(sol.standardize_columns(x), np.array([[-1.0, 0.0], [1.0, 0.0]]))


def test_wb_06_02_overflow_safe_2d() -> None:
    import numpy as np
    assert np.allclose(sol.stable_softmax(np.array([1000.0, 1000.0])), [0.5, 0.5])
    p2 = sol.stable_softmax(np.array([[1.0, 2.0, 3.0], [0.0, 0.0, 0.0]]))
    assert np.allclose(p2.sum(axis=-1), [1.0, 1.0])


def test_wb_06_03_top_k() -> None:
    import numpy as np
    docs = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    assert sol.cosine_top_k(docs, np.array([2.0, 0.0]), 2) == [0, 2]
