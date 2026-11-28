# Chapter 14: Docker — Reproducible Containers & Multi-Service Stacks

*Images vs containers, Dockerfile syntax, layer caching, docker-compose networking, and GPU passthrough.*

**Why It Matters:** AI stacks break when Python versions, C++ libraries, or CUDA drivers differ between your PC and a server. Docker packages the exact OS, Python, and libraries into one portable container.

**Skills Covered:** Docker, Dockerfile, Layer Caching, docker-compose, .dockerignore


---

## 14.1 `Dockerfile` Syntax, Layer Caching & `docker-compose`

> **Before You Start:** Note: Docker isn't installed on this PC yet—install Docker Desktop for Windows (WSL 2) when ready to run containers locally.

### 1. Definition
- **Dockerfile:** A recipe listing what OS, Python packages, and code to install.
- **Image:** The read-only snapshot built from a Dockerfile.
- **Container:** A live running instance of an image.

### 2. Exact Syntax — Standard Python Dockerfile Instructions
```python
FROM python:3.12-slim                  # 1. Pin base version!
WORKDIR /app                           # 2. Folder inside container
COPY requirements.txt .                # 3. Copy dependencies FIRST
RUN pip install --no-cache-dir -r requirements.txt  # 4. Cached!
COPY app/ ./app/                       # 5. Copy your code LAST
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

- `FROM`: never use `:latest` (pin `3.12-slim` so builds stay predictable).
- `COPY requirements.txt` *before* `COPY app/`: keeps `pip install` cached when you only edit `.py` code.
- `0.0.0.0`: required inside containers so connections from outside reach your API.

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

1. `services:` launches every container together via `docker compose up`.
2. Inside `gateway`, code connects to `redis://redis:6379` (using the service name `redis`, NOT `localhost`!).

### Always Include a `.dockerignore` File
Listing `.venv`, `__pycache__`, and large `.pt` model files in `.dockerignore` keeps Docker images fast and lean.


### 4. Practical Example — Sample `.dockerignore`

```python
.venv/
__pycache__/
*.db
.git/
```

### Common Mistakes to Avoid

- Putting `COPY . .` *above* `RUN pip install` (breaks caching on every code edit!).
- Using `localhost` inside container A to reach container B.

**Key Takeaway:** Pin base tags, copy `requirements.txt` before source code, add `.dockerignore`, and talk between compose services by service name.


---

## Hands-On Project: Containerized Microservice Stack (API + Worker)

Package the Chapter 12 Gateway and Worker with `.dockerignore`, layer-cached Dockerfiles, and `docker-compose.yml`.

1. Install Docker Desktop for Windows (WSL 2).
2. Write `.dockerignore` and layer-cached `Dockerfile` files.
3. Create `docker-compose.yml` with healthchecks and service networking.
