# Chapter 10: Docker & Reproducible AI Environments

*Images vs containers, Dockerfile syntax, layer caching, docker-compose networking, and GPU passthrough.*

**Why It Matters:** AI stacks break when Python versions, C++ libraries, or CUDA drivers differ between your PC and a server. Docker packages the exact OS, Python, and libraries into one portable container.

**Skills Covered:** Dockerfile, Images vs Containers, Layer Caching, docker-compose, .dockerignore


---

## 10.1 `Dockerfile` Syntax, Layer Caching & `docker-compose`

> **Before You Start:** Note: Docker isn't installed on this PC yet—install Docker Desktop for Windows (WSL 2) when ready to run containers locally.

### 1. Definition
- **Dockerfile:** A step-by-step recipe listing what OS, Python packages, and code to install.
- **Image:** The built, read-only snapshot produced from a Dockerfile.
- **Container:** A live running instance of an image (like running a program from an `.exe`).

### 2. Exact Syntax — Standard Python Dockerfile Instructions
```python
FROM python:3.12-slim                  # 1. Base OS + Python image (pin version!)
WORKDIR /app                           # 2. Folder inside the container
COPY requirements.txt .                # 3. Copy dependency list FIRST
RUN pip install --no-cache-dir -r requirements.txt  # 4. Install deps (cached!)
COPY app/ ./app/                       # 5. Copy your code LAST
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

- `FROM`: never use `:latest` (pin `3.12-slim` so builds don't break next year).
- `COPY requirements.txt` *before* `COPY app/`: Docker caches each step. If you only edit `.py` code, steps 1–4 stay cached and rebuild in 1 second!
- `0.0.0.0`: required inside containers so connections from outside the container can reach your API.

### 3. Tiny Example (Line-by-Line) — Connecting Two Services in `docker-compose.yml`
```python
services:
  redis:
    image: redis:7-alpine
  gateway:
    build: ./gateway
    ports:
      - '8000:8000'
    depends_on:
      - redis
```

1. `services:` lists every container to launch together via `docker compose up`.
2. `ports: ['8000:8000']` exposes container port 8000 to your Windows browser at `localhost:8000`.
3. Inside `gateway`, code connects to `redis://redis:6379` (using the service name `redis`, NOT `localhost`!).

### Always Include a `.dockerignore` File
Just like `.gitignore`, a `.dockerignore` listing `.venv`, `__pycache__`, and huge `.pt` model files keeps Docker from copying gigabytes of junk into your image.


### 4. Practical Example — Sample `.dockerignore` + Healthcheck

```python
# .dockerignore
.venv/
__pycache__/
*.db
.git/
```

### Common Mistakes to Avoid

- Putting `COPY . .` *above* `RUN pip install` (forces a slow full `pip install` on every single code edit!).
- Using `localhost` inside container A to reach container B (inside a container, `localhost` means *itself*, not the other service!).

**Key Takeaway:** Pin base tags, copy `requirements.txt` before source code, add `.dockerignore`, and talk between compose services by service name.


---

## Hands-On Project: Containerized Microservice Stack (API + Worker)

Package the Chapter 9 Gateway and Worker with `.dockerignore`, layer-cached Dockerfiles, and `docker-compose.yml`.

1. Install Docker Desktop for Windows (WSL 2).
2. Write `.dockerignore` and layer-cached `Dockerfile` files.
3. Create `docker-compose.yml` with healthchecks and service networking.
