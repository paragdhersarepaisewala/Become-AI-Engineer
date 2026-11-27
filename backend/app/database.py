"""SQLite persistence layer for tracking chapter mastery, workbook drills, and study streaks."""

from __future__ import annotations

import json
import sqlite3
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

DB_PATH = Path(__file__).resolve().parent.parent / "learning_tracker.db"


def get_connection(db_path: Path | None = None) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path or DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: Path | None = None) -> None:
    with get_connection(db_path) as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS chapter_progress (
                chapter_id TEXT PRIMARY KEY,
                status TEXT NOT NULL DEFAULT 'not_started',
                completed_sections_json TEXT NOT NULL DEFAULT '[]',
                completed_milestones_json TEXT NOT NULL DEFAULT '[]',
                quiz_answers_json TEXT NOT NULL DEFAULT '{}',
                notes TEXT NOT NULL DEFAULT '',
                updated_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS workbook_progress (
                problem_id TEXT PRIMARY KEY,
                status TEXT NOT NULL DEFAULT 'todo',
                last_code TEXT NOT NULL DEFAULT '',
                attempts INTEGER NOT NULL DEFAULT 0,
                hints_used INTEGER NOT NULL DEFAULT 0,
                passed_tests INTEGER NOT NULL DEFAULT 0,
                total_tests INTEGER NOT NULL DEFAULT 0,
                updated_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS study_activity (
                activity_date TEXT PRIMARY KEY,
                actions_count INTEGER NOT NULL DEFAULT 0
            );
            """
        )


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def record_activity(db_path: Path | None = None) -> None:
    today = date.today().isoformat()
    with get_connection(db_path) as conn:
        conn.execute(
            """
            INSERT INTO study_activity (activity_date, actions_count)
            VALUES (?, 1)
            ON CONFLICT(activity_date)
            DO UPDATE SET actions_count = actions_count + 1
            """,
            (today,),
        )


def get_streak_days(db_path: Path | None = None) -> int:
    with get_connection(db_path) as conn:
        rows = conn.execute(
            "SELECT activity_date FROM study_activity ORDER BY activity_date DESC"
        ).fetchall()
    active_dates = {row["activity_date"] for row in rows}
    if not active_dates:
        return 0

    today = date.today()
    cursor = today if today.isoformat() in active_dates else today - timedelta(days=1)
    streak = 0
    while cursor.isoformat() in active_dates:
        streak += 1
        cursor -= timedelta(days=1)
    return streak


def get_all_chapter_progress(db_path: Path | None = None) -> dict[str, dict[str, Any]]:
    with get_connection(db_path) as conn:
        rows = conn.execute("SELECT * FROM chapter_progress").fetchall()
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        result[row["chapter_id"]] = {
            "chapter_id": row["chapter_id"],
            "status": row["status"],
            "completed_sections": json.loads(row["completed_sections_json"]),
            "completed_milestones": json.loads(row["completed_milestones_json"]),
            "quiz_answers": json.loads(row["quiz_answers_json"]),
            "notes": row["notes"],
            "updated_at": row["updated_at"],
        }
    return result


def upsert_chapter_progress(
    chapter_id: str,
    status: str | None = None,
    completed_sections: list[str] | None = None,
    completed_milestones: list[str] | None = None,
    quiz_answers: dict[str, int] | None = None,
    notes: str | None = None,
    db_path: Path | None = None,
) -> dict[str, Any]:
    existing = get_all_chapter_progress(db_path).get(
        chapter_id,
        {
            "status": "not_started",
            "completed_sections": [],
            "completed_milestones": [],
            "quiz_answers": {},
            "notes": "",
        },
    )
    new_status = status if status is not None else existing["status"]
    new_sections = (
        completed_sections
        if completed_sections is not None
        else existing["completed_sections"]
    )
    new_milestones = (
        completed_milestones
        if completed_milestones is not None
        else existing["completed_milestones"]
    )
    new_quiz = (
        quiz_answers if quiz_answers is not None else existing["quiz_answers"]
    )
    new_notes = notes if notes is not None else existing["notes"]
    now = _now_iso()

    with get_connection(db_path) as conn:
        conn.execute(
            """
            INSERT INTO chapter_progress (
                chapter_id, status, completed_sections_json,
                completed_milestones_json, quiz_answers_json, notes, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(chapter_id) DO UPDATE SET
                status = excluded.status,
                completed_sections_json = excluded.completed_sections_json,
                completed_milestones_json = excluded.completed_milestones_json,
                quiz_answers_json = excluded.quiz_answers_json,
                notes = excluded.notes,
                updated_at = excluded.updated_at
            """,
            (
                chapter_id,
                new_status,
                json.dumps(new_sections),
                json.dumps(new_milestones),
                json.dumps(new_quiz),
                new_notes,
                now,
            ),
        )
    record_activity(db_path)
    return {
        "chapter_id": chapter_id,
        "status": new_status,
        "completed_sections": new_sections,
        "completed_milestones": new_milestones,
        "quiz_answers": new_quiz,
        "notes": new_notes,
        "updated_at": now,
    }


def get_all_workbook_progress(db_path: Path | None = None) -> dict[str, dict[str, Any]]:
    with get_connection(db_path) as conn:
        rows = conn.execute("SELECT * FROM workbook_progress").fetchall()
    return {row["problem_id"]: dict(row) for row in rows}


def upsert_workbook_progress(
    problem_id: str,
    status: str | None = None,
    last_code: str | None = None,
    increment_attempts: bool = False,
    hints_used: int | None = None,
    passed_tests: int | None = None,
    total_tests: int | None = None,
    db_path: Path | None = None,
) -> dict[str, Any]:
    existing = get_all_workbook_progress(db_path).get(
        problem_id,
        {
            "status": "todo",
            "last_code": "",
            "attempts": 0,
            "hints_used": 0,
            "passed_tests": 0,
            "total_tests": 0,
        },
    )
    new_status = status if status is not None else existing["status"]
    new_code = last_code if last_code is not None else existing["last_code"]
    new_attempts = existing["attempts"] + (1 if increment_attempts else 0)
    new_hints = (
        max(existing["hints_used"], hints_used)
        if hints_used is not None
        else existing["hints_used"]
    )
    new_passed = (
        passed_tests if passed_tests is not None else existing["passed_tests"]
    )
    new_total = total_tests if total_tests is not None else existing["total_tests"]
    now = _now_iso()

    with get_connection(db_path) as conn:
        conn.execute(
            """
            INSERT INTO workbook_progress (
                problem_id, status, last_code, attempts,
                hints_used, passed_tests, total_tests, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(problem_id) DO UPDATE SET
                status = excluded.status,
                last_code = excluded.last_code,
                attempts = excluded.attempts,
                hints_used = excluded.hints_used,
                passed_tests = excluded.passed_tests,
                total_tests = excluded.total_tests,
                updated_at = excluded.updated_at
            """,
            (
                problem_id,
                new_status,
                new_code,
                new_attempts,
                new_hints,
                new_passed,
                new_total,
                now,
            ),
        )
    record_activity(db_path)
    return {
        "problem_id": problem_id,
        "status": new_status,
        "last_code": new_code,
        "attempts": new_attempts,
        "hints_used": new_hints,
        "passed_tests": new_passed,
        "total_tests": new_total,
        "updated_at": now,
    }
