"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_03_01_counts_files_only() -> None:
    import os, tempfile
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, 'subfolder'))
        open(os.path.join(d, 'A.TXT'), 'w').close()
        open(os.path.join(d, 'b.txt'), 'w').close()
        open(os.path.join(d, 'README'), 'w').close()
        assert sol.count_extensions(d) == {'.txt': 2, 'none': 1}


def test_wb_03_02_organizes_cleanly() -> None:
    import os, tempfile
    with tempfile.TemporaryDirectory() as d:
        for fn in ['pic.jpg', 'todo.md', 'raw.csv']:
            open(os.path.join(d, fn), 'w').close()
        res = sol.organize_files(d)
        assert res == {'images': 1, 'docs': 1, 'other': 1}
        assert os.path.isfile(os.path.join(d, 'images', 'pic.jpg'))
        assert os.path.isfile(os.path.join(d, 'docs', 'todo.md'))
