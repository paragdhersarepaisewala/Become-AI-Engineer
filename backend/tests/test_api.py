"""API integration tests for FastAPI tracker and code runner."""

from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

import app.database as db
from app.main import app


def test_api_end_to_end(tmp_path: Path, monkeypatch) -> None:
    test_db = tmp_path / "test_tracker.db"
    monkeypatch.setattr(db, "DB_PATH", test_db)
    db.init_db(test_db)

    client = TestClient(app)

    assert client.get("/api/health").status_code == 200

    dash = client.get("/api/dashboard")
    assert dash.status_code == 200
    assert dash.json()["chapters"]["available_total"] == 10
    assert dash.json()["chapters"]["roadmap_total"] == 16

    chapters = client.get("/api/chapters").json()
    assert len(chapters) == 16

    ch1 = client.get("/api/chapters/ch01").json()
    assert len(ch1["sections"]) == 6

    upd = client.post(
        "/api/chapters/ch01/progress",
        json={
            "status": "in_progress",
            "completed_sections": ["ch01-s1"],
            "notes": "Variables are labels!",
        },
    )
    assert upd.status_code == 200
    assert upd.json()["notes"] == "Variables are labels!"

    run_res = client.post(
        "/api/workbook/run",
        json={
            "problem_id": "wb-01-01",
            "mode": "test",
            "code": (
                "def grade_summary(scores: list[int]) -> dict[str, int]:\n"
                "    counts = {'passed': 0, 'failed': 0}\n"
                "    for s in scores:\n"
                "        if s >= 60:\n"
                "            counts['passed'] += 1\n"
                "        else:\n"
                "            counts['failed'] += 1\n"
                "    return counts\n"
            ),
        },
    )
    assert run_res.status_code == 200
    body = run_res.json()
    assert body["ok"] is True
    assert body["progress"]["status"] == "mastered"

    projects = client.get("/api/projects").json()
    assert len(projects) == 16
