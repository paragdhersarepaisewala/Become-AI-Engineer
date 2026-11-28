"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_07_01_bounded() -> None:
    import asyncio
    state = {'active': 0, 'peak': 0}
    async def w(x):
        state['active'] += 1
        state['peak'] = max(state['peak'], state['active'])
        await asyncio.sleep(0.02)
        state['active'] -= 1
        return x.upper()
    res = asyncio.run(sol.run_bounded(['a', 'b', 'c', 'd'], w, 2))
    assert res == ['A', 'B', 'C', 'D'] and state['peak'] <= 2


def test_wb_07_02_retry() -> None:
    import asyncio
    state = {'calls': 0}
    async def flaky():
        state['calls'] += 1
        if state['calls'] < 3: raise RuntimeError('429')
        return 'ok'
    assert asyncio.run(sol.retry_async(flaky, max_retries=3, base_delay=0.005)) == 'ok' and state['calls'] == 3
