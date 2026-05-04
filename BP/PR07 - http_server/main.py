import http.server
import socketserver

PORT = 8080


class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        # If the user visits the root URL "/", serve index.html
        if self.path == "/":
            self.path = "/index.html"

        # Try to serve the requested file
        try:
            super().do_GET()
        except FileNotFoundError:
            # If the file doesn't exist, send a 404 error
            self.send_error(404, "File Not Found")


# Start the server
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server is running on port {PORT}")
    print(f"Open your browser and go to: http://localhost:{PORT}/")
    print("Press CTRL + C to stop the server.")

    # Keep the server running until manually stopped
    httpd.serve_forever()
