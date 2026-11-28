# Project (Chapter 3): Automated Folder Organizer & Log Archiver (`os` Automation)

Use `os` (`listdir`, `path`, `makedirs`, `rename`, `walk`) to sort messy files into category folders and write a summary report.

## Architecture Steps

1. Scan a target folder safely skipping subdirectories.
2. Map extensions (`.png`/`.jpg` -> `images`, `.txt`/`.md` -> `docs`, else `other`).
3. Create category folders with `os.makedirs(..., exist_ok=True)` and move files with `os.rename`.

## Milestones

- [ ] Scan folder & count files by extension using os.path
- [ ] Create destination folders & move files cleanly
- [ ] Write automation report & pass pytest
