import os
import time
import socket
from pathlib import Path
from stem.control import Controller
from stem import Signal
from .ui import UI
from .config import Config


class VeilNode:
    def __init__(self, web_dir, port=8080, tor_port=9051):
        self.web_dir = Path(web_dir).resolve()
        self.port = port
        self.tor_port = tor_port
        self.hidden_service_dir = None
        self.onion_address = None
        self.ui = UI()
        self.config = Config()
        self.controller = None

        if not self.web_dir.exists():
            raise FileNotFoundError(f"Web directory not found: {self.web_dir}")

    def setup_hidden_service(self):
        """Configure and initialize the Tor hidden service"""
        try:
            self.ui.print_status("Connecting to Tor control port...")

            # Try multiple authentication methods automatically
            auth_methods = [
                lambda c: c.authenticate(),
                lambda c: c.authenticate(""),
                lambda c: c.authenticate(password=""),
            ]

            self.controller = Controller.from_port(port=self.tor_port)

            for auth_func in auth_methods:
                try:
                    auth_func(self.controller)
                    break
                except:
                    continue

            self.ui.print_status("Establishing hidden service...")

            response = self.controller.create_ephemeral_hidden_service(
                {80: self.port},
                await_publication=True
            )

            self.onion_address = f"{response.service_id}.onion"
            self.ui.print_success(f"Hidden service created: {self.onion_address}")

            return response.service_id

        except Exception as e:
            self.ui.print_error(f"Failed to setup hidden service: {str(e)}")
            self.ui.print_info("Tip: Make sure Tor is running")
            raise

    def verify_tor_running(self):
        """Check if Tor service is running"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('127.0.0.1', self.tor_port))
            sock.close()
            return result == 0
        except:
            return False

    def start(self):
        """Start the VeilNode service"""
        self.ui.print_banner()

        if not self.verify_tor_running():
            self.ui.print_error("Tor service is not running on port {}".format(self.tor_port))
            self.ui.print_info("")
            self.ui.print_info("Quick Start Commands:")
            self.ui.print_info("  Termux:  pkg install tor && tor &")
            self.ui.print_info("  Linux:   sudo systemctl start tor")
            self.ui.print_info("  macOS:   brew services start tor")
            self.ui.print_info("")
            return

        self.ui.print_info(f"Web directory: {self.web_dir}")
        self.ui.print_info(f"Local port: {self.port}")

        try:
            from .server import WebServer

            service_id = self.setup_hidden_service()

            server = WebServer(str(self.web_dir), self.port)

            self.ui.print_success("VeilNode is running")
            self.ui.print_onion_address(self.onion_address)
            self.ui.print_info("Press Ctrl+C to stop the service")

            server.start()

            while True:
                time.sleep(1)

        except KeyboardInterrupt:
            self.ui.print_status("Shutting down VeilNode...")
            if 'server' in locals():
                server.stop()
            if self.controller:
                self.controller.close()
            self.ui.print_success("Service stopped successfully")
        except Exception as e:
            self.ui.print_error(f"Error: {str(e)}")
            if self.controller:
                self.controller.close()
            raise