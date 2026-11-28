"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_12_01_valid_invalid() -> None:
    from fastapi.testclient import TestClient
    client = TestClient(sol.app)
    r1 = client.post('/tokenize', json={'text': 'Hello AI'})
    assert r1.status_code == 200 and r1.json() == {'tokens': ['hello', 'ai'], 'count': 2}
    assert client.post('/tokenize', json={'text': '   '}).status_code == 422


def test_wb_12_02_broker() -> None:
    import asyncio
    b = sol.JobBroker()
    jid = b.submit('train')
    assert b.jobs[jid]['status'] == 'queued' and asyncio.run(b.process_one()) is True
    assert b.jobs[jid] == {'status': 'done', 'result': 'TRAIN'} and asyncio.run(b.process_one()) is False
