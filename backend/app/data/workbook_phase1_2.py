"""Combines Phase 1 and Phase 2 workbook problems."""

from __future__ import annotations

from app.data.workbook_phase1 import PHASE_1_WORKBOOK
from app.data.workbook_phase2 import PHASE_2_WORKBOOK

WORKBOOK_PROBLEMS = [*PHASE_1_WORKBOOK, *PHASE_2_WORKBOOK]
