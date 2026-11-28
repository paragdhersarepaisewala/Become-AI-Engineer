"""Automated pytest checks for your solutions in problems.py."""

import problems as sol


def test_wb_11_01_local_http_200_and_404() -> None:
    import json, threading
    from http.server import BaseHTTPRequestHandler, HTTPServer
    class H(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/ok':
                self.send_response(200); self.send_header('Content-Type', 'application/json'); self.end_headers()
                self.wfile.write(json.dumps({'status': 'ready'}).encode())
            else:
                self.send_response(404); self.end_headers()
        def log_message(self, *a): pass
    srv = HTTPServer(('127.0.0.1', 0), H)
    t = threading.Thread(target=lambda: [srv.handle_request(), srv.handle_request()], daemon=True); t.start()
    assert sol.fetch_json_safe(f'http://127.0.0.1:{srv.server_port}/ok') == {'status': 'ready'}
    assert sol.fetch_json_safe(f'http://127.0.0.1:{srv.server_port}/missing') is None
    srv.server_close()


def test_wb_11_02_fetch_validate_save() -> None:
    import json, tempfile, threading
    from pathlib import Path
    from http.server import BaseHTTPRequestHandler, HTTPServer
    class H(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200); self.send_header('Content-Type', 'application/json'); self.end_headers()
            payload = {'id': 7, 'text': 'Saved note'} if self.path == '/good' else {'id': 'x', 'text': ''}
            self.wfile.write(json.dumps(payload).encode())
        def log_message(self, *a): pass
    srv = HTTPServer(('127.0.0.1', 0), H)
    t = threading.Thread(target=lambda: [srv.handle_request(), srv.handle_request()], daemon=True); t.start()
    with tempfile.TemporaryDirectory() as d:
        out = Path(d) / 'sub' / 'note.json'
        assert sol.sync_api_note(f'http://127.0.0.1:{srv.server_port}/good', out) is True
        assert json.loads(out.read_text(encoding='utf-8'))['id'] == 7
        assert sol.sync_api_note(f'http://127.0.0.1:{srv.server_port}/bad', out) is False
    srv.server_close()
