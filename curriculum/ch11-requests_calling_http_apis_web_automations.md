# Chapter 11: Requests — Calling HTTP APIs & Web Automations

*GET vs POST, status codes (200/404/429), query params, headers & API keys, timeouts, try/except, and saving API data with Pydantic.*

**Why It Matters:** Before you *build* your own web APIs with FastAPI, you should master *calling* web APIs with `requests`—fetching weather, news, GitHub data, or LLM endpoints, validating responses with Pydantic, and saving them to disk.

**Skills Covered:** requests, GET & POST, Status Codes, Params & Headers, Timeouts, API + Pydantic


---

## 11.1 How HTTP Works + `requests.get()` & `requests.post()`

> **Before You Start:** Every time your browser opens a webpage or an app talks to ChatGPT, it sends an HTTP request and gets back a status code + body.

### 1. Definition
**`requests`** is Python's classic, human-friendly library for sending HTTP requests (`GET` to fetch data, `POST` to send data) and reading JSON replies.

### 2. Exact Syntax — Core `requests` Syntax (With Mandatory `timeout`!)
```python
import requests

# GET with query parameters (?q=python&limit=5):
resp = requests.get(
    'https://api.example.com/search',
    params={'q': 'python', 'limit': 5},
    headers={'Authorization': 'Bearer YOUR_TOKEN'},
    timeout=10,
)
resp.raise_for_status()   # raises error if status is 4xx or 5xx!
data = resp.json()        # parses JSON reply into Python dict/list
```

- `resp.status_code`: `200` = OK, `404` = Not Found, `401/403` = Bad API key, `429` = Rate Limited, `500` = Server Error.
- `params={...}` safely builds URL query strings (`?q=python&limit=5`) for you.
- `timeout=10`: **NEVER omit `timeout`**—otherwise a frozen server can hang your Python script forever!
- `resp.raise_for_status()`: immediately turns 404/500 responses into a catchable Python error.

### 3. Tiny Example (Line-by-Line) — Sending JSON With `requests.post(..., json=...)` (Local Test Server)
```python
import json, threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

# Tiny local fake server so this runs offline right here!
class EchoHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        body = json.loads(self.rfile.read(length))
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'echo': body['msg'].upper()}).encode())
    def log_message(self, *args): pass

srv = HTTPServer(('127.0.0.1', 0), EchoHandler)
threading.Thread(target=srv.handle_request, daemon=True).start()

url = f'http://127.0.0.1:{srv.server_port}/'
r = requests.post(url, json={'msg': 'hello api'}, timeout=5)
print(r.status_code, r.json())
srv.server_close()
```

1. Starts a tiny local HTTP server on an automatic free port (`port=0`).
2. `requests.post(url, json={'msg': 'hello api'}, timeout=5)` sends JSON automatically with the right headers.
3. Prints `200 {'echo': 'HELLO API'}`!

### Combining `requests` + `Pydantic` + Files (Real Automation!)
1. Fetch JSON from an endpoint with `requests.get(..., timeout=10)` inside `try / except requests.RequestException:`.
2. Validate the returned JSON with your **Chapter 10 Pydantic `BaseModel`**.
3. Save the clean data to disk with `Path.write_text(...)`!


### 4. Practical Example — Safe API Fetcher With Error Handling

```python
import requests

def fetch_json_safe(url: str, timeout: float = 5.0) -> dict | None:
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as err:
        print('API request failed:', err)
        return None
```

### Common Mistakes to Avoid

- Calling `requests.get(url)` without `timeout=...` (can hang indefinitely).
- Passing `data={'a': 1}` when an API expects JSON—always use `json={'a': 1}` for JSON APIs!
- Hardcoding API keys instead of reading them via `os.getenv('API_KEY')`.

**Key Takeaway:** Always pass `timeout=`, check `resp.raise_for_status()`, catch `requests.RequestException`, and validate `.json()` with Pydantic.


---

## Hands-On Project: API Data Fetcher, Pydantic Validator & JSON Archiver

Fetch JSON records from an HTTP endpoint using `requests`, validate them with Pydantic, and save cleaned results to disk.

1. Write `fetch_json(url, timeout)` handling `RequestException` and non-200 statuses.
2. Validate payloads with a Pydantic `BaseModel`.
3. Save validated records to a JSON file and test against a local mock HTTP server.
