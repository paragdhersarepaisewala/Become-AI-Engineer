"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_04_01_account_ops() -> None:
    a = sol.BankAccount('Sara', 100)
    b = sol.BankAccount('Alex', 20)
    a.deposit(50)
    assert a.balance == 150 and b.balance == 20
    assert a.withdraw(200) is False and a.withdraw(40) is True and a.balance == 110


def test_wb_04_02_playlist() -> None:
    pl = sol.Playlist()
    pl.add(sol.Song('Intro', 90))
    pl.add(sol.Song('Main', 210))
    assert len(pl) == 2 and pl.total_seconds() == 300


def test_wb_04_03_pipeline() -> None:
    p = sol.Pipeline([sol.StripWhitespace(), sol.ReplaceWord('ml', 'AI')])
    assert p('  learn   ml   fast ') == 'learn AI fast'
