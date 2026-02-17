# VeilNode

VeilNode is a lightweight Python tool that allows you to host static
websites as Tor hidden services with minimal configuration. It works on
Linux, macOS, Windows, and Termux (Android).

Created by suadatbiniqbal.

------------------------------------------------------------------------

## Overview

VeilNode simplifies the process of hosting static content on the Tor
network. It automatically handles Tor control communication and hidden
service creation, allowing you to serve a local directory as a .onion
site with a single command.

It is designed for developers, privacy enthusiasts, and researchers who
want a simple way to publish static content over Tor.

------------------------------------------------------------------------

## Quick Install and Run

### Termux (Android)

``` bash
pkg update && pkg install -y tor python git && git clone https://github.com/suadatbiniqbal/VeilNode.git && cd VeilNode && pip install stem && mkdir -p $PREFIX/etc/tor && echo -e "ControlPort 9051
CookieAuthentication 0" > $PREFIX/etc/tor/torrc && tor & sleep 15 && pip install -e . && veilnode --sample
```

------------------------------------------------------------------------

### Linux (Ubuntu/Debian)

``` bash
sudo apt update
sudo apt install -y tor git python3-pip
sudo systemctl start tor

git clone https://github.com/suadatbiniqbal/VeilNode.git
cd VeilNode

sudo bash -c 'echo -e "ControlPort 9051
CookieAuthentication 0" >> /etc/tor/torrc'
sudo systemctl restart tor

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .

veilnode --sample
```

------------------------------------------------------------------------

### macOS

``` bash
brew install tor git
brew services start tor

git clone https://github.com/suadatbiniqbal/VeilNode.git
cd VeilNode

echo -e "ControlPort 9051
CookieAuthentication 0" >> /usr/local/etc/tor/torrc
brew services restart tor

pip3 install -r requirements.txt
pip3 install -e .

veilnode --sample
```

------------------------------------------------------------------------

### Windows

1.  Install Python 3.
2.  Install Tor Browser from the official Tor Project website.
3.  Keep Tor Browser running.
4.  Clone the repository and install dependencies:

``` bash
git clone https://github.com/suadatbiniqbal/VeilNode.git
cd VeilNode
pip install -r requirements.txt
pip install -e .
veilnode --sample
```

------------------------------------------------------------------------

## Usage

``` bash
veilnode --sample              # Launch demo site
veilnode .                     # Host current directory
veilnode /path/to/site         # Host custom directory
veilnode --sample -p 9000      # Custom local port
veilnode --sample -t 9151      # Custom Tor control port
veilnode ~/my-site -p 8888     # Custom site with custom port
veilnode --help                # Show help menu
```

------------------------------------------------------------------------

## Project Structure

    VeilNode/
    ├── veilnode/
    │   ├── __init__.py
    │   ├── core.py
    │   ├── server.py
    │   ├── config.py
    │   ├── ui.py
    │   └── cli.py
    ├── examples/
    │   └── sample_site/
    │       └── index.html
    ├── requirements.txt
    ├── setup.py
    └── README.md

------------------------------------------------------------------------

## Features

-   Minimal configuration required
-   Automatic Tor control authentication
-   Built-in sample site
-   Custom port support
-   Cross-platform compatibility
-   Clean terminal interface
-   Static site hosting support

------------------------------------------------------------------------

## License

MIT License

------------------------------------------------------------------------

## Disclaimer

This project is intended for educational and legitimate purposes only.
Users are responsible for complying with all applicable laws and
regulations.
