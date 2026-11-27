"""Verifies that every reference solution in the workbook passes all automated test cases."""

from __future__ import annotations

import pytest

from app.content_loader import get_all_workbook_problems
from app.runner import run_python_code

PROBLEMS = get_all_workbook_problems()


@pytest.mark.parametrize("problem", PROBLEMS, ids=[p["id"] for p in PROBLEMS])
def test_reference_solution_passes_all_tests(problem: dict) -> None:
    result = run_python_code(
        code=problem["solution_code"],
        test_cases=problem["test_cases"],
        timeout_seconds=5.0,
    )
    assert result["ok"], f"{problem['id']} failed: {result['stderr']} | {result['test_results']}"
    assert result["passed_count"] == result["total_count"]
    assert result["total_count"] > 0
