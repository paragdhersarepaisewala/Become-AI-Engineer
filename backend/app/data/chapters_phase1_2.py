"""Combines Phase 1 (Ch 1-6) and Phase 2 (Ch 7-10) chapters."""

from __future__ import annotations

from app.data.chapters_phase1 import PHASE_1A_CHAPTERS
from app.data.chapters_phase1_logic_async import PHASE_1B_CHAPTERS
from app.data.chapters_phase2 import PHASE_2_CHAPTERS

PHASE_1_2_CHAPTERS = [*PHASE_1A_CHAPTERS, *PHASE_1B_CHAPTERS, *PHASE_2_CHAPTERS]
