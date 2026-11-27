# Project (Chapter 2): Modular OOP Log Analyzer Package

Refactor `legacy_monolith.py` into `models.py`, `analyzer.py`, and `cli.py` with a passing `pytest` suite.

## Architecture Steps

1. Inspect `legacy_monolith.py` to separate parsing from printing.
2. Create `LogEntry` and `LogReport` dataclasses in `models.py`.
3. Implement `LogAnalyzer` in `analyzer.py` and verify with `pytest`.

## Milestones

- [ ] Separate models.py dataclasses from file I/O
- [ ] Build LogAnalyzer class with clean methods
- [ ] Wire cli.py with Path & pass pytest
