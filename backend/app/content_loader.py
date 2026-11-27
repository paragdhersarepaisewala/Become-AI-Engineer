"""Loads structured curriculum chapters and practice workbook problems."""

from __future__ import annotations

from typing import Any

from app.data.chapters_phase1_2 import PHASE_1_2_CHAPTERS
from app.data.chapters_phase3_4_roadmap import PHASE_3_4_ROADMAP_CHAPTERS
from app.data.workbook_phase1_2 import WORKBOOK_PROBLEMS


def get_all_chapters() -> list[dict[str, Any]]:
    return [*PHASE_1_2_CHAPTERS, *PHASE_3_4_ROADMAP_CHAPTERS]


def get_chapter_by_id(chapter_id: str) -> dict[str, Any] | None:
    for chapter in get_all_chapters():
        if chapter["id"] == chapter_id:
            return chapter
    return None


def get_all_workbook_problems() -> list[dict[str, Any]]:
    return list(WORKBOOK_PROBLEMS)


def get_problem_by_id(problem_id: str) -> dict[str, Any] | None:
    for problem in WORKBOOK_PROBLEMS:
        if problem["id"] == problem_id:
            return problem
    return None
