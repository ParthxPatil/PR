import http.server
import socketserver

PORT = 8080


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        try:
            super().do_GET()
        except FileNotFoundError:
            self.send_error(404, "File Not Found")


def run_server():
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Serving HTTP on port {PORT}...")
        print(f"Open http://localhost:{PORT}/ in a browser.")
        httpd.serve_forever()


if __name__ == "__main__":
    run_server()
