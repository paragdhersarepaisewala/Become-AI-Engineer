"""Local Python sandbox runner for executing workbook code and running test cases."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any


def run_python_code(
    code: str,
    test_cases: list[dict[str, str]] | None = None,
    timeout_seconds: float = 5.0,
) -> dict[str, Any]:
    """Execute user Python code in an isolated temp directory with optional test assertions."""
    start = time.perf_counter()
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"

    with tempfile.TemporaryDirectory(prefix="aie_runner_") as tmp_dir:
        tmp_path = Path(tmp_dir)
        user_file = tmp_path / "user_solution.py"
        user_file.write_text(code, encoding="utf-8")

        if not test_cases:
            try:
                proc = subprocess.run(
                    [sys.executable, str(user_file)],
                    cwd=tmp_dir,
                    capture_output=True,
                    text=True,
                    timeout=timeout_seconds,
                    env=env,
                )
                elapsed_ms = round((time.perf_counter() - start) * 1000, 1)
                return {
                    "ok": proc.returncode == 0,
                    "stdout": proc.stdout,
                    "stderr": proc.stderr,
                    "elapsed_ms": elapsed_ms,
                    "test_results": [],
                    "passed_count": 0,
                    "total_count": 0,
                }
            except subprocess.TimeoutExpired:
                return {
                    "ok": False,
                    "stdout": "",
                    "stderr": f"Execution timed out after {timeout_seconds}s (check for infinite loops!).",
                    "elapsed_ms": timeout_seconds * 1000,
                    "test_results": [],
                    "passed_count": 0,
                    "total_count": 0,
                }

        harness_code = _build_test_harness(test_cases)
        harness_file = tmp_path / "run_tests.py"
        harness_file.write_text(harness_code, encoding="utf-8")

        try:
            proc = subprocess.run(
                [sys.executable, str(harness_file)],
                cwd=tmp_dir,
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
                env=env,
            )
            elapsed_ms = round((time.perf_counter() - start) * 1000, 1)
            raw_out = proc.stdout
            marker = "__AIE_TEST_RESULTS__:"
            user_stdout = raw_out
            test_results: list[dict[str, Any]] = []

            if marker in raw_out:
                before, after = raw_out.split(marker, 1)
                user_stdout = before
                try:
                    test_results = json.loads(after.strip())
                except json.JSONDecodeError:
                    test_results = []

            passed_count = sum(1 for r in test_results if r.get("passed"))
            total_count = len(test_cases)
            return {
                "ok": proc.returncode == 0 and passed_count == total_count,
                "stdout": user_stdout.strip(),
                "stderr": proc.stderr.strip(),
                "elapsed_ms": elapsed_ms,
                "test_results": test_results,
                "passed_count": passed_count,
                "total_count": total_count,
            }
        except subprocess.TimeoutExpired:
            return {
                "ok": False,
                "stdout": "",
                "stderr": f"Test execution timed out after {timeout_seconds}s (possible infinite loop).",
                "elapsed_ms": timeout_seconds * 1000,
                "test_results": [
                    {"name": tc["name"], "passed": False, "error": "Timed out"}
                    for tc in test_cases
                ],
                "passed_count": 0,
                "total_count": len(test_cases),
            }


def _build_test_harness(test_cases: list[dict[str, str]]) -> str:
    tests_json = json.dumps(test_cases)
    return f"""import json
import traceback

try:
    import user_solution as sol
except Exception:
    results = [{{"name": tc["name"], "passed": False, "error": traceback.format_exc(limit=3)}} for tc in {tests_json}]
    print("__AIE_TEST_RESULTS__:" + json.dumps(results))
    raise SystemExit(1)

results = []
for tc in {tests_json}:
    ns = {{"sol": sol}}
    try:
        exec(tc["code"], ns, ns)
        results.append({{"name": tc["name"], "passed": True, "error": ""}})
    except AssertionError as exc:
        msg = str(exc) or "Assertion failed"
        results.append({{"name": tc["name"], "passed": False, "error": msg}})
    except Exception:
        results.append({{"name": tc["name"], "passed": False, "error": traceback.format_exc(limit=3)}})

print("__AIE_TEST_RESULTS__:" + json.dumps(results))
"""
