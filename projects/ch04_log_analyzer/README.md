# Project (Chapter 4): Modular OOP Log Analyzer Package

Refactor `legacy_monolith.py` into clean `models.py`, `analyzer.py`, `cli.py`, and `pytest` tests.

## Architecture Steps

1. Inspect `legacy_monolith.py` to separate file reading from counting.
2. Create `LogEntry` and `LogReport` dataclasses in `models.py`.
3. Build `LogAnalyzer` in `analyzer.py` and pass `pytest`.

## Milestones

- [ ] Separate models.py dataclasses from file I/O
- [ ] Build LogAnalyzer class with clean state & methods
- [ ] Wire cli.py & pass pytest
