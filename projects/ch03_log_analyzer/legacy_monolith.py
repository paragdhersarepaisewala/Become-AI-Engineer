"""Messy monolithic log analyzer — refactor this into models.py, analyzer.py, and cli.py!"""

SAMPLE_LOGS = [
    "[INFO] 2026-11-01 Server started on port 8000",
    "[WARN] 2026-11-01 High memory usage 84%",
    "corrupt log entry missing level",
    "[ERROR] 2026-11-01 Failed to connect to vector store",
]

def run_monolith():
    info = 0
    warn = 0
    err = 0
    for line in SAMPLE_LOGS:
        if "[INFO]" in line:
            info += 1
        elif "[WARN]" in line:
            warn += 1
        elif "[ERROR]" in line:
            err += 1
    print(f"INFO={info} WARN={warn} ERROR={err}")

if __name__ == "__main__":
    run_monolith()
