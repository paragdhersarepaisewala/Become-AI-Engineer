"""Reference solutions with explanations."""


# --- 3.1: `os` Scanner: Count Files by Extension ---
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


# --- 3.2: `os` Automation: Organize Messy Folder Into Buckets ---
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
