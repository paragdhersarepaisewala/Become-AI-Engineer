"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_10_01_bad_good() -> None:
    assert set(sol.audit_dockerfile(['FROM python:latest', 'COPY . .', 'RUN pip install -r requirements.txt'])) == {'PIN_BASE_IMAGE', 'CACHE_BUST_ORDER', 'USE_NO_CACHE_PIP'}
    assert sol.audit_dockerfile(['FROM python:3.12-slim', 'COPY requirements.txt .', 'RUN pip install --no-cache-dir -r requirements.txt', 'COPY . .']) == []


def test_wb_10_02_stack_order() -> None:
    assert sol.compose_startup_order({'gateway': ['worker', 'redis'], 'worker': ['redis'], 'redis': []}) == ['redis', 'worker', 'gateway']
