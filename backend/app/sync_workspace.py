"""Generates mirrored Markdown curriculum, separate workbook files, and project starter kits in the workspace."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from app.content_loader import get_all_chapters, get_all_workbook_problems

ROOT = Path(__file__).resolve().parent.parent.parent


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def sync_all() -> None:
    chapters = get_all_chapters()
    problems = get_all_workbook_problems()

    _write_curriculum(chapters)
    _write_workbook(chapters, problems)
    _write_projects(chapters)


def _write_curriculum(chapters: list[dict[str, Any]]) -> None:
    cur_dir = ROOT / "curriculum"
    cur_dir.mkdir(parents=True, exist_ok=True)

    roadmap_lines = [
        "# AI Engineer Academy — 15-Chapter Master Roadmap\n",
        "Zero assumed knowledge. Logic, OOP, DSA, DP, Async, Docker, and Microservices taught just-in-time.\n",
        "",
    ]
    current_phase = None
    for ch in chapters:
        if ch["phase"] != current_phase:
            current_phase = ch["phase"]
            roadmap_lines.append(f"\n## {ch['phase_title']}\n")
        badge = "Available" if ch["status_type"] == "available" else "Roadmap (Phase 3–4)"
        roadmap_lines.append(
            f"- **Chapter {ch['number']}: {ch['title']}** ({badge}, ~{ch['estimated_hours']}h) — {ch['subtitle']}"
        )
    (cur_dir / "00-roadmap.md").write_text("\n".join(roadmap_lines) + "\n", encoding="utf-8")

    for ch in chapters:
        if ch["status_type"] != "available":
            continue
        lines = [
            f"# Chapter {ch['number']}: {ch['title']}\n",
            f"*{ch['subtitle']}*\n",
            f"**Why It Matters:** {ch['why_it_matters']}\n",
            f"**Skills Covered:** {', '.join(ch['just_in_time_tags'])}\n",
        ]
        for sec in ch["sections"]:
            lines.append(f"\n---\n\n## {sec['title']}\n")
            if sec.get("zero_assumption_note"):
                lines.append(f"> **Before You Start:** {sec['zero_assumption_note']}\n")
            if sec.get("definition"):
                lines.append(f"### 1. Definition\n{sec['definition']}\n")
            if sec.get("syntax_box"):
                sb = sec["syntax_box"]
                lines.append(f"### 2. Exact Syntax — {sb['title']}\n```python\n{sb['syntax'].rstrip()}\n```\n")
                for b in sb["breakdown"]:
                    lines.append(f"- {b}")
                lines.append("")
            if sec.get("tiny_example"):
                te = sec["tiny_example"]
                lines.append(f"### 3. Tiny Example (Line-by-Line) — {te['title']}\n```python\n{te['code'].rstrip()}\n```\n")
                for idx, step in enumerate(te["line_by_line"], start=1):
                    lines.append(f"{idx}. {step}")
                lines.append("")
            lines.append(sec["body_markdown"] + "\n")
            if sec.get("code_example"):
                lines.append(f"\n### 4. Practical Example — {sec['code_example']['title']}\n")
                lines.append(f"```python\n{sec['code_example']['code'].rstrip()}\n```\n")
            if sec.get("common_mistakes"):
                lines.append("### Common Mistakes to Avoid\n")
                for m in sec["common_mistakes"]:
                    lines.append(f"- {m}")
                lines.append("")
            lines.append(f"**Key Takeaway:** {sec['key_takeaway']}\n")

        if ch.get("project"):
            proj = ch["project"]
            lines.append(f"\n---\n\n## Hands-On Project: {proj['title']}\n")
            lines.append(f"{proj['overview']}\n")
            for idx, step in enumerate(proj["architecture_steps"], start=1):
                lines.append(f"{idx}. {step}")
            lines.append("")

        filename = f"{ch['id']}-{_slug(ch['title'])[:48]}.md"
        (cur_dir / filename).write_text("\n".join(lines), encoding="utf-8")


def _write_workbook(chapters: list[dict[str, Any]], problems: list[dict[str, Any]]) -> None:
    wb_dir = ROOT / "workbook"
    wb_dir.mkdir(parents=True, exist_ok=True)
    (wb_dir / "README.md").write_text(
        "# Separate Practice Workbook\n\n"
        "Each chapter folder contains:\n"
        "- `exercises.md`: Questions, Thinking Blueprints, Dry-Run Traces, Answers & Explanations\n"
        "- `problems.py`: Starter stubs for you to solve in VS Code\n"
        "- `solutions.py`: Reference solutions\n"
        "- `test_problems.py`: `pytest` assertions to verify your `problems.py` code\n\n"
        "Run tests for a chapter: `python -m pytest workbook/ch01_.../test_problems.py`\n",
        encoding="utf-8",
    )

    by_ch: dict[str, list[dict[str, Any]]] = {}
    for p in problems:
        by_ch.setdefault(p["chapter_id"], []).append(p)

    ch_map = {c["id"]: c for c in chapters}
    for ch_id, probs in by_ch.items():
        ch = ch_map[ch_id]
        folder = wb_dir / f"{ch_id}_{_slug(ch['title'])[:28]}"
        folder.mkdir(parents=True, exist_ok=True)

        md_lines = [f"# Workbook — Chapter {ch['number']}: {ch['title']}\n"]
        starter_blocks = ['"""Starter exercises — implement each function and run pytest on test_problems.py."""\n']
        solution_blocks = ['"""Reference solutions with explanations."""\n']
        test_blocks = [
            '"""Automated pytest checks for your solutions in problems.py."""\n\n'
            "import problems as sol\n"
        ]

        for p in probs:
            md_lines.append(f"\n---\n\n## {p['number']} {p['title']} (`{p['difficulty']}` · {p['topic']})\n")
            md_lines.append(p["prompt_markdown"] + "\n")
            md_lines.append("### Thinking Blueprint\n")
            for step in p["thinking_blueprint"]:
                md_lines.append(f"- {step}")
            md_lines.append("\n### Progressive Hints\n")
            for idx, h in enumerate(p["hints"], start=1):
                md_lines.append(f"{idx}. {h}")
            md_lines.append("\n### Dry-Run Trace\n" + p["dry_run_trace"] + "\n")
            md_lines.append(f"### Answer & Explanation\n```python\n{p['solution_code'].rstrip()}\n```\n")
            md_lines.append(p["explanation_markdown"] + "\n")

            starter_blocks.append(f"\n# --- {p['number']}: {p['title']} ---\n{p['starter_code'].rstrip()}\n")
            solution_blocks.append(f"\n# --- {p['number']}: {p['title']} ---\n{p['solution_code'].rstrip()}\n")

            for tc in p["test_cases"]:
                indented = "\n".join("    " + line for line in tc["code"].splitlines())
                fn_name = f"test_{_slug(p['id'])}_{_slug(tc['name'])}"
                test_blocks.append(f"\ndef {fn_name}() -> None:\n{indented}\n")

        (folder / "exercises.md").write_text("\n".join(md_lines), encoding="utf-8")
        (folder / "problems.py").write_text("\n".join(starter_blocks), encoding="utf-8")
        (folder / "solutions.py").write_text("\n".join(solution_blocks), encoding="utf-8")
        (folder / "test_problems.py").write_text("\n".join(test_blocks), encoding="utf-8")


def _write_projects(chapters: list[dict[str, Any]]) -> None:
    for ch in chapters:
        if ch["status_type"] != "available" or not ch.get("project"):
            continue
        proj = ch["project"]
        proj_dir = ROOT / proj["workspace_dir"]
        proj_dir.mkdir(parents=True, exist_ok=True)
        readme = [
            f"# Project (Chapter {ch['number']}): {proj['title']}\n",
            proj["overview"] + "\n",
            "## Architecture Steps\n",
        ]
        for idx, step in enumerate(proj["architecture_steps"], start=1):
            readme.append(f"{idx}. {step}")
        readme.append("\n## Milestones\n")
        for m in proj["milestones"]:
            readme.append(f"- [ ] {m['label']}")
        (proj_dir / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")

    # Add legacy_monolith.py starter for Ch 2 refactoring project
    ch2_dir = ROOT / "projects" / "ch02_log_analyzer"
    if ch2_dir.exists():
        (ch2_dir / "legacy_monolith.py").write_text(
            '"""Messy monolithic log analyzer — refactor this into models.py, analyzer.py, and cli.py!"""\n\n'
            "SAMPLE_LOGS = [\n"
            '    "[INFO] 2026-11-01 Server started on port 8000",\n'
            '    "[WARN] 2026-11-01 High memory usage 84%",\n'
            '    "corrupt log entry missing level",\n'
            '    "[ERROR] 2026-11-01 Failed to connect to vector store",\n'
            "]\n\n"
            "def run_monolith():\n"
            "    info = 0\n"
            "    warn = 0\n"
            "    err = 0\n"
            "    for line in SAMPLE_LOGS:\n"
            '        if "[INFO]" in line:\n'
            "            info += 1\n"
            '        elif "[WARN]" in line:\n'
            "            warn += 1\n"
            '        elif "[ERROR]" in line:\n'
            "            err += 1\n"
            '    print(f"INFO={info} WARN={warn} ERROR={err}")\n\n'
            'if __name__ == "__main__":\n'
            "    run_monolith()\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    sync_all()
    print("Workspace curriculum, workbook, and projects synced cleanly.")
