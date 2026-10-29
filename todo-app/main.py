import os
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = int(os.environ.get("PORT", "3000"))

class TodoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Todo application running")

server = HTTPServer(("0.0.0.0", PORT), TodoHandler)

print(f"Server started in port {PORT}", flush=True)

server.serve_forever()
