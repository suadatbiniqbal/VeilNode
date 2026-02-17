import argparse
import sys
import os
from pathlib import Path
from .core import VeilNode


def main():
    parser = argparse.ArgumentParser(
        description="VeilNode - Tor Hidden Service Hosting Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  veilnode --sample              Start with built-in sample site
  veilnode /path/to/site         Host your own site
  veilnode --sample -p 9000      Use custom port
  veilnode . -p 8888             Host current directory

Created by suadatbiniqbal
        """
    )

    parser.add_argument(
        "directory",
        nargs='?',
        help="Path to the web directory to host (optional if using --sample)"
    )

    parser.add_argument(
        "-s", "--sample",
        action="store_true",
        help="Use built-in sample site for quick testing"
    )

    parser.add_argument(
        "-p", "--port",
        type=int,
        default=8080,
        help="Local port for the web server (default: 8080)"
    )

    parser.add_argument(
        "-t", "--tor-port",
        type=int,
        default=9051,
        help="Tor control port (default: 9051)"
    )

    args = parser.parse_args()

    # Determine directory
    if args.sample:
        # Use built-in sample site
        module_dir = Path(__file__).parent
        sample_dir = module_dir.parent / "examples" / "sample_site"
        if not sample_dir.exists():
            print("Error: Sample site not found.", file=sys.stderr)
            sys.exit(1)
        directory = sample_dir
    elif args.directory:
        directory = args.directory
    else:
        parser.print_help()
        print("\nError: Provide a directory or use --sample", file=sys.stderr)
        sys.exit(1)

    try:
        node = VeilNode(
            web_dir=directory,
            port=args.port,
            tor_port=args.tor_port
        )
        node.start()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()