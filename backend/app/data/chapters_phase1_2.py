"""Combines Phase 1 and Phase 2 chapters."""

from __future__ import annotations

from app.data.chapters_phase1 import PHASE_1_CHAPTERS
from app.data.chapters_phase2 import PHASE_2_CHAPTERS

PHASE_1_2_CHAPTERS = [*PHASE_1_CHAPTERS, *PHASE_2_CHAPTERS]
