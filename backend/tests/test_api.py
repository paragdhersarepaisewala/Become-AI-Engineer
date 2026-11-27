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
    assert dash.json()["chapters"]["available_total"] == 9
    assert dash.json()["chapters"]["roadmap_total"] == 15

    chapters = client.get("/api/chapters").json()
    assert len(chapters) == 15

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
                "def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:\n"
                "    result = [] if tags is None else list(tags)\n"
                "    if tag not in result:\n"
                "        result.append(tag)\n"
                "    return result\n"
            ),
        },
    )
    assert run_res.status_code == 200
    body = run_res.json()
    assert body["ok"] is True
    assert body["progress"]["status"] == "mastered"

    projects = client.get("/api/projects").json()
    assert len(projects) == 15
