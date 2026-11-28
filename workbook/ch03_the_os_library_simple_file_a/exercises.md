# Workbook — Chapter 3: The `os` Library & Simple File Automations


---

## 3.1 `os` Scanner: Count Files by Extension (`Foundation` · os Library)

Write `count_extensions(folder: str) -> dict[str, int]` that inspects **files only** inside `folder` (ignoring subfolders!) and returns counts keyed by lowercase extension (e.g. `'.txt'`, `'.png'`, or `'none'` if no extension).

### Thinking Blueprint

- Loop `for name in os.listdir(folder):` and build `full = os.path.join(folder, name)`.
- Skip if `not os.path.isfile(full)`.
- Split `_, ext = os.path.splitext(name)` -> lowercase or `'none'`.

### Progressive Hints

1. Remember `os.listdir` returns filenames only—always `os.path.join(folder, name)` before checking `isfile`!

### Dry-Run Trace
`['a.TXT', 'b.txt', 'subdir/']` -> `subdir` skipped -> `{'.txt': 2}`.

### Answer & Explanation
```python
import os

def count_extensions(folder: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in os.listdir(folder):
        full = os.path.join(folder, name)
        if not os.path.isfile(full):
            continue
        _, ext = os.path.splitext(name)
        key = ext.lower() if ext else 'none'
        counts[key] = counts.get(key, 0) + 1
    return counts
```

**High-Level Blocks:** Join folder + filename first, guard with `os.path.isfile`, then split extension cleanly.


---

## 3.2 `os` Automation: Organize Messy Folder Into Buckets (`Intermediate` · os Library)

Write `organize_files(folder: str) -> dict[str, int]` that moves every file in `folder` into a subfolder:
- `.png` / `.jpg` -> `'images'`
- `.txt` / `.md` -> `'docs'`
- anything else -> `'other'`
Ignore existing subfolders and return counts of files moved per bucket.

### Thinking Blueprint

- Map extension -> bucket folder name.
- Call `os.makedirs(dest_dir, exist_ok=True)` then `os.rename(src, dest)`.

### Progressive Hints

1. Skip directories with `if not os.path.isfile(src): continue`.

### Dry-Run Trace
`['photo.png', 'notes.md', 'data.csv']` -> moves into `images/`, `docs/`, `other/` and returns `{'images': 1, 'docs': 1, 'other': 1}`.

### Answer & Explanation
```python
import os

def organize_files(folder: str) -> dict[str, int]:
    moved: dict[str, int] = {}
    for name in os.listdir(folder):
        src = os.path.join(folder, name)
        if not os.path.isfile(src):
            continue
        _, ext = os.path.splitext(name)
        ext = ext.lower()
        if ext in ('.png', '.jpg'):
            bucket = 'images'
        elif ext in ('.txt', '.md'):
            bucket = 'docs'
        else:
            bucket = 'other'
        dest_dir = os.path.join(folder, bucket)
        os.makedirs(dest_dir, exist_ok=True)
        os.rename(src, os.path.join(dest_dir, name))
        moved[bucket] = moved.get(bucket, 0) + 1
    return moved
```

**High-Level Blocks:** Classify by extension, create destination folder safely with `exist_ok=True`, and move via `os.rename`.
