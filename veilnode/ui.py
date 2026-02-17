class UI:
    COLORS = {
        'RESET': '\033[0m',
        'BOLD': '\033[1m',
        'DIM': '\033[2m',
        'CYAN': '\033[96m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'RED': '\033[91m',
        'MAGENTA': '\033[95m',
        'BLUE': '\033[94m',
    }

    def colorize(self, text, color):
        """Apply color to text"""
        return f"{self.COLORS.get(color, '')}{text}{self.COLORS['RESET']}"

    def print_banner(self):
        """Display the VeilNode banner"""
        banner = """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║  ██╗   ██╗███████╗██╗██╗     ███╗   ██╗ ██████╗ ██████╗ ║
║  ██║   ██║██╔════╝██║██║     ████╗  ██║██╔═══██╗██╔══██╗║
║  ██║   ██║█████╗  ██║██║     ██╔██╗ ██║██║   ██║██║  ██║║
║  ╚██╗ ██╔╝██╔══╝  ██║██║     ██║╚██╗██║██║   ██║██║  ██║║
║   ╚████╔╝ ███████╗██║███████╗██║ ╚████║╚██████╔╝██████╔╝║
║    ╚═══╝  ╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ║
║                                                           ║
║              Tor Hidden Service Hosting Tool             ║
║                  Created by suadatbiniqbal                ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
        """
        print(self.colorize(banner, 'CYAN'))

    def print_status(self, message):
        """Print status message"""
        print(f"{self.colorize('[*]', 'BLUE')} {message}")

    def print_success(self, message):
        """Print success message"""
        print(f"{self.colorize('[+]', 'GREEN')} {message}")

    def print_error(self, message):
        """Print error message"""
        print(f"{self.colorize('[!]', 'RED')} {message}")

    def print_info(self, message):
        """Print info message"""
        print(f"{self.colorize('[i]', 'YELLOW')} {message}")

    def print_onion_address(self, address):
        """Print the onion address in a highlighted box"""
        border = "═" * (len(address) + 4)
        print(f"\n{self.colorize(f'╔{border}╗', 'MAGENTA')}")
        print(f"{self.colorize(f'║  {address}  ║', 'MAGENTA')}")
        print(f"{self.colorize(f'╚{border}╝', 'MAGENTA')}\n")