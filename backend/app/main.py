"""FastAPI backend for AI Engineer Academy: curriculum, workbook runner, and progress tracking."""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import Any, Literal

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.content_loader import (
    get_all_chapters,
    get_all_workbook_problems,
    get_chapter_by_id,
    get_problem_by_id,
)
from app.database import (
    get_all_chapter_progress,
    get_all_workbook_progress,
    get_streak_days,
    init_db,
    upsert_chapter_progress,
    upsert_workbook_progress,
)
from app.runner import run_python_code


@asynccontextmanager
async def lifespan(_app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="AI Engineer Academy API",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5175",
        "http://127.0.0.1:5175",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChapterProgressUpdate(BaseModel):
    status: Literal["not_started", "in_progress", "completed"] | None = None
    completed_sections: list[str] | None = None
    completed_milestones: list[str] | None = None
    quiz_answers: dict[str, int] | None = None
    notes: str | None = None


class WorkbookProgressUpdate(BaseModel):
    status: Literal["todo", "struggled", "solved_with_hints", "mastered"] | None = None
    last_code: str | None = None
    hints_used: int | None = Field(default=None, ge=0)


class RunCodeRequest(BaseModel):
    problem_id: str | None = None
    code: str
    mode: Literal["scratch", "test"] = "test"


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/dashboard")
def get_dashboard() -> dict[str, Any]:
    chapters = get_all_chapters()
    problems = get_all_workbook_problems()
    ch_prog = get_all_chapter_progress()
    wb_prog = get_all_workbook_progress()

    available_chapters = [c for c in chapters if c["status_type"] == "available"]
    completed_chapters = sum(
        1
        for c in available_chapters
        if ch_prog.get(c["id"], {}).get("status") == "completed"
    )

    total_sections = sum(len(c["sections"]) for c in available_chapters)
    completed_sections = sum(
        len(ch_prog.get(c["id"], {}).get("completed_sections", []))
        for c in available_chapters
    )

    total_milestones = sum(
        len(c["project"]["milestones"]) for c in available_chapters if c.get("project")
    )
    completed_milestones = sum(
        len(ch_prog.get(c["id"], {}).get("completed_milestones", []))
        for c in available_chapters
    )

    mastered_problems = sum(
        1
        for p in problems
        if wb_prog.get(p["id"], {}).get("status") == "mastered"
    )
    solved_with_hints = sum(
        1
        for p in problems
        if wb_prog.get(p["id"], {}).get("status") == "solved_with_hints"
    )
    struggled_problems = [
        {
            "id": p["id"],
            "title": p["title"],
            "chapter_id": p["chapter_id"],
            "topic": p["topic"],
            "status": wb_prog[p["id"]]["status"],
        }
        for p in problems
        if wb_prog.get(p["id"], {}).get("status") in ("struggled", "solved_with_hints")
    ]

    topic_stats: dict[str, dict[str, int]] = {}
    for p in problems:
        topic = p["topic"]
        bucket = topic_stats.setdefault(topic, {"total": 0, "mastered": 0, "struggled": 0})
        bucket["total"] += 1
        st = wb_prog.get(p["id"], {}).get("status", "todo")
        if st == "mastered":
            bucket["mastered"] += 1
        elif st == "struggled":
            bucket["struggled"] += 1

    next_chapter = None
    for c in available_chapters:
        if ch_prog.get(c["id"], {}).get("status", "not_started") != "completed":
            next_chapter = {"id": c["id"], "number": c["number"], "title": c["title"]}
            break

    next_problem = None
    for p in problems:
        st = wb_prog.get(p["id"], {}).get("status", "todo")
        if st in ("todo", "struggled"):
            next_problem = {
                "id": p["id"],
                "title": p["title"],
                "chapter_id": p["chapter_id"],
                "topic": p["topic"],
            }
            break

    return {
        "streak_days": get_streak_days(),
        "chapters": {
            "completed": completed_chapters,
            "available_total": len(available_chapters),
            "roadmap_total": len(chapters),
        },
        "sections": {
            "completed": completed_sections,
            "total": total_sections,
        },
        "projects": {
            "milestones_completed": completed_milestones,
            "milestones_total": total_milestones,
        },
        "workbook": {
            "mastered": mastered_problems,
            "solved_with_hints": solved_with_hints,
            "struggled_count": len([s for s in struggled_problems if s["status"] == "struggled"]),
            "total": len(problems),
        },
        "topic_stats": topic_stats,
        "needs_review": struggled_problems[:6],
        "next_chapter": next_chapter,
        "next_problem": next_problem,
    }


@app.get("/api/chapters")
def list_chapters() -> list[dict[str, Any]]:
    chapters = get_all_chapters()
    ch_prog = get_all_chapter_progress()
    result = []
    for c in chapters:
        prog = ch_prog.get(
            c["id"],
            {
                "status": "not_started",
                "completed_sections": [],
                "completed_milestones": [],
                "quiz_answers": {},
                "notes": "",
            },
        )
        result.append(
            {
                "id": c["id"],
                "number": c["number"],
                "phase": c["phase"],
                "phase_title": c["phase_title"],
                "title": c["title"],
                "subtitle": c["subtitle"],
                "status_type": c["status_type"],
                "estimated_hours": c["estimated_hours"],
                "why_it_matters": c["why_it_matters"],
                "just_in_time_tags": c["just_in_time_tags"],
                "sections_count": len(c.get("sections", [])),
                "project_title": c["project"]["title"] if c.get("project") else None,
                "milestones_count": len(c["project"]["milestones"]) if c.get("project") else 0,
                "progress": prog,
            }
        )
    return result


@app.get("/api/chapters/{chapter_id}")
def get_chapter(chapter_id: str) -> dict[str, Any]:
    chapter = get_chapter_by_id(chapter_id)
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    ch_prog = get_all_chapter_progress().get(
        chapter_id,
        {
            "chapter_id": chapter_id,
            "status": "not_started",
            "completed_sections": [],
            "completed_milestones": [],
            "quiz_answers": {},
            "notes": "",
        },
    )
    problems = [p for p in get_all_workbook_problems() if p["chapter_id"] == chapter_id]
    return {
        **chapter,
        "progress": ch_prog,
        "workbook_problem_ids": [p["id"] for p in problems],
    }


@app.post("/api/chapters/{chapter_id}/progress")
def update_chapter_progress(
    chapter_id: str, payload: ChapterProgressUpdate
) -> dict[str, Any]:
    chapter = get_chapter_by_id(chapter_id)
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return upsert_chapter_progress(
        chapter_id=chapter_id,
        status=payload.status,
        completed_sections=payload.completed_sections,
        completed_milestones=payload.completed_milestones,
        quiz_answers=payload.quiz_answers,
        notes=payload.notes,
    )


@app.get("/api/workbook")
def list_workbook(
    chapter_id: str | None = None,
    topic: str | None = None,
    difficulty: str | None = None,
) -> list[dict[str, Any]]:
    problems = get_all_workbook_problems()
    wb_prog = get_all_workbook_progress()
    filtered = []
    for p in problems:
        if chapter_id and p["chapter_id"] != chapter_id:
            continue
        if topic and p["topic"] != topic:
            continue
        if difficulty and p["difficulty"] != difficulty:
            continue
        prog = wb_prog.get(
            p["id"],
            {
                "status": "todo",
                "last_code": p["starter_code"],
                "attempts": 0,
                "hints_used": 0,
                "passed_tests": 0,
                "total_tests": len(p.get("test_cases", [])),
            },
        )
        filtered.append(
            {
                "id": p["id"],
                "chapter_id": p["chapter_id"],
                "number": p["number"],
                "title": p["title"],
                "topic": p["topic"],
                "question_type": p["question_type"],
                "difficulty": p["difficulty"],
                "summary": p["summary"],
                "progress": prog,
            }
        )
    return filtered


@app.get("/api/workbook/{problem_id}")
def get_workbook_problem(problem_id: str) -> dict[str, Any]:
    problem = get_problem_by_id(problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Workbook problem not found")
    prog = get_all_workbook_progress().get(
        problem_id,
        {
            "problem_id": problem_id,
            "status": "todo",
            "last_code": problem["starter_code"],
            "attempts": 0,
            "hints_used": 0,
            "passed_tests": 0,
            "total_tests": len(problem.get("test_cases", [])),
        },
    )
    if not prog.get("last_code"):
        prog["last_code"] = problem["starter_code"]
    return {**problem, "progress": prog}


@app.post("/api/workbook/{problem_id}/progress")
def update_workbook_progress(
    problem_id: str, payload: WorkbookProgressUpdate
) -> dict[str, Any]:
    problem = get_problem_by_id(problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Workbook problem not found")
    return upsert_workbook_progress(
        problem_id=problem_id,
        status=payload.status,
        last_code=payload.last_code,
        hints_used=payload.hints_used,
    )


@app.post("/api/workbook/run")
def run_workbook_code(payload: RunCodeRequest) -> dict[str, Any]:
    test_cases = None
    problem = None
    if payload.problem_id:
        problem = get_problem_by_id(payload.problem_id)
        if not problem:
            raise HTTPException(status_code=404, detail="Workbook problem not found")
        if payload.mode == "test":
            test_cases = problem.get("test_cases", [])

    result = run_python_code(payload.code, test_cases=test_cases)

    if problem and payload.mode == "test":
        existing = get_all_workbook_progress().get(problem["id"], {})
        hints_used = existing.get("hints_used", 0)
        current_status = existing.get("status", "todo")
        if result["ok"] and result["total_count"] > 0:
            new_status = "solved_with_hints" if hints_used > 0 else "mastered"
        elif current_status == "todo":
            new_status = "struggled"
        else:
            new_status = current_status

        progress = upsert_workbook_progress(
            problem_id=problem["id"],
            status=new_status,
            last_code=payload.code,
            increment_attempts=True,
            passed_tests=result["passed_count"],
            total_tests=result["total_count"],
        )
        result["progress"] = progress
    elif problem:
        progress = upsert_workbook_progress(
            problem_id=problem["id"],
            last_code=payload.code,
            increment_attempts=True,
        )
        result["progress"] = progress

    return result


@app.get("/api/projects")
def list_projects() -> list[dict[str, Any]]:
    chapters = get_all_chapters()
    ch_prog = get_all_chapter_progress()
    projects = []
    for c in chapters:
        if not c.get("project"):
            continue
        prog = ch_prog.get(c["id"], {})
        projects.append(
            {
                "chapter_id": c["id"],
                "chapter_number": c["number"],
                "chapter_title": c["title"],
                "phase": c["phase"],
                "status_type": c["status_type"],
                "project": c["project"],
                "completed_milestones": prog.get("completed_milestones", []),
            }
        )
    return projects
