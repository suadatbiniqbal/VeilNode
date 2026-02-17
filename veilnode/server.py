import http.server
import socketserver
import threading
from pathlib import Path


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=None, **kwargs):
        self.directory = directory
        super().__init__(*args, directory=directory, **kwargs)

    def log_message(self, format, *args):
        """Suppress default logging for cleaner output"""
        pass

    def end_headers(self):
        self.send_header('Server', 'VeilNode/1.0')
        super().end_headers()


class WebServer:
    def __init__(self, directory, port):
        self.directory = Path(directory).resolve()
        self.port = port
        self.httpd = None
        self.thread = None

    def start(self):
        """Start the web server in a separate thread"""
        handler = lambda *args, **kwargs: CustomHTTPRequestHandler(
            *args, directory=str(self.directory), **kwargs
        )

        self.httpd = socketserver.TCPServer(
            ("127.0.0.1", self.port),
            handler
        )

        self.thread = threading.Thread(target=self.httpd.serve_forever)
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        """Stop the web server"""
        if self.httpd:
            self.httpd.shutdown()
            self.httpd.server_close()