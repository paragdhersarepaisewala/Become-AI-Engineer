# Chapter 3: The `os` Library & Simple File Automations

*Inspecting folders (os.listdir, os.walk), joining paths (os.path), creating/renaming files & folders, and environment variables (os.getenv).*

**Why It Matters:** Python's built-in `os` module lets your scripts talk directly to your operating system—scanning folders of 1,000 files, organizing messy downloads automatically, checking file sizes, and reading API keys safely from environment variables.

**Skills Covered:** os.listdir, os.path, os.makedirs, os.rename, os.walk, os.getenv


---

## 3.1 Exploring Folders & Safe Paths (`os.getcwd`, `os.listdir`, `os.path`)

> **Before You Start:** Before automating folders, you must know how Python asks Windows/Linux: *'Where am I?'* and *'What files are inside this folder?'*

### 1. Definition
The **`os` module** lets Python inspect folders, check whether a path is a file or directory, and split filenames from extensions.

### 2. Exact Syntax — Essential `os` & `os.path` Functions
```python
import os

here = os.getcwd()                          # current working folder
items = os.listdir(here)                    # list of file/folder names
full = os.path.join(here, 'notes.txt')      # safely join folder + file
print(os.path.isfile(full))                 # True if it's a file
name, ext = os.path.splitext('photo.jpg')   # ('photo', '.jpg')
```

- `os.listdir(folder)` returns **just the names** (`['a.txt', 'img.png']`), NOT full paths—always combine with `os.path.join(folder, name)`!
- `os.path.isfile(full)` skips subfolders when you only want files.
- `os.path.splitext('report.pdf')` splits into `('report', '.pdf')` cleanly.

### 3. Tiny Example (Line-by-Line) — Listing Only `.txt` Files in the Current Folder
```python
import os

folder = os.getcwd()
for name in os.listdir(folder):
    full_path = os.path.join(folder, name)
    if os.path.isfile(full_path) and name.endswith('.txt'):
        print('Found text file:', name)
```

1. Line 3: Gets the current working directory.
2. Line 4: Loops through every entry name in that folder.
3. Line 5: Builds the full path so `isfile` works anywhere.
4. Line 6: Prints only real `.txt` files (ignoring directories).

### Walking Subfolders Automatically (`os.walk`)
`os.listdir()` looks **one level deep**. When you want every file inside nested subfolders too, `for root, dirs, files in os.walk(folder):` visits every subfolder automatically!


### 4. Practical Example — Counting Files by Extension in a Folder

```python
import os

def count_by_extension(folder: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in os.listdir(folder):
        full = os.path.join(folder, name)
        if not os.path.isfile(full):
            continue
        _, ext = os.path.splitext(name)
        ext = ext.lower() or '(no ext)'
        counts[ext] = counts.get(ext, 0) + 1
    return counts

print(count_by_extension(os.getcwd()))
```

### Common Mistakes to Avoid

- Calling `os.path.isfile(name)` without `os.path.join(folder, name)` when scanning another folder (fails because Python checks the current folder instead!).

**Key Takeaway:** Always combine `os.listdir(folder)` names with `os.path.join(folder, name)` before checking `isfile` or opening them.


---

## 3.2 Simple File Automations (`os.makedirs`, `os.rename`, `os.getenv`)

> **Before You Start:** With just 3 `os` functions, you can build real desktop automations that sort messy folders in half a second.

### 1. Definition
`os.makedirs` creates folders, `os.rename` moves or renames files, and `os.getenv` reads secret environment settings without hardcoding passwords.

### 2. Exact Syntax — Creating Folders, Moving Files & Reading Env Vars
```python
import os

os.makedirs('sorted/images', exist_ok=True)    # creates folder safely
os.rename('messy/pic.png', 'sorted/images/pic.png')  # moves or renames
api_key = os.getenv('OPENAI_API_KEY', 'missing')     # safe env lookup
```

- `exist_ok=True` prevents crashing if `'sorted/images'` already exists.
- `os.rename(old_path, new_path)` moves a file to another folder on the same drive—or renames it!
- `os.getenv('NAME', default)` reads an environment variable safely without raising `KeyError`.

### 3. Tiny Example (Line-by-Line) — Safely Moving a File Into a New Folder
```python
import os, tempfile

with tempfile.TemporaryDirectory() as tmp:
    src = os.path.join(tmp, 'report.txt')
    open(src, 'w', encoding='utf-8').write('hello')

    dest_dir = os.path.join(tmp, 'archive')
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, 'report.txt')
    os.rename(src, dest)
    print('Moved exists?', os.path.exists(dest))
```

1. Creates a safe temporary sandbox folder `tmp` (auto-deleted afterwards).
2. Creates `report.txt`, makes `archive/` folder, and moves the file inside with `os.rename`.
3. Prints `Moved exists? True`.

### Why `os.getenv()` Matters for AI Engineers
Never write `api_key = 'sk-proj-1234...'` directly in your Python file—if you `git push` it to GitHub, bots steal it in seconds! Store secrets in environment variables and read them with `os.getenv()`.


### 4. Practical Example — Mini Automation: Sort Files Into Extension Folders

```python
import os, tempfile

def organize_folder(folder: str) -> dict[str, int]:
    moved: dict[str, int] = {}
    for name in os.listdir(folder):
        src = os.path.join(folder, name)
        if not os.path.isfile(src):
            continue
        _, ext = os.path.splitext(name)
        bucket = ext.lstrip('.').lower() or 'other'
        target_dir = os.path.join(folder, bucket)
        os.makedirs(target_dir, exist_ok=True)
        os.rename(src, os.path.join(target_dir, name))
        moved[bucket] = moved.get(bucket, 0) + 1
    return moved

with tempfile.TemporaryDirectory() as d:
    for fn in ['a.txt', 'b.txt', 'pic.png']:
        open(os.path.join(d, fn), 'w').close()
    print('Organized:', organize_folder(d))
```

### Common Mistakes to Avoid

- Forgetting `exist_ok=True` in `os.makedirs(...)` -> crashes the second time you run your automation!
- Calling `os.rename(src, dest)` when `dest`'s folder doesn't exist yet -> always call `os.makedirs` first.

**Key Takeaway:** Combine `os.listdir`, `os.path.splitext`, `os.makedirs(..., exist_ok=True)`, and `os.rename` to automate file organization cleanly.


---

## Hands-On Project: Automated Folder Organizer & Log Archiver (`os` Automation)

Use `os` (`listdir`, `path`, `makedirs`, `rename`, `walk`) to sort messy files into category folders and write a summary report.

1. Scan a target folder safely skipping subdirectories.
2. Map extensions (`.png`/`.jpg` -> `images`, `.txt`/`.md` -> `docs`, else `other`).
3. Create category folders with `os.makedirs(..., exist_ok=True)` and move files with `os.rename`.
