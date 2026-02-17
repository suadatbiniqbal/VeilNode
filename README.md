# VeilNode

VeilNode is a lightweight Python tool for hosting static websites as Tor
hidden services with minimal configuration. It works on Linux, macOS,
Windows, and Termux (Android).

Created by suadatbiniqbal.

------------------------------------------------------------------------

## Overview

VeilNode simplifies the process of publishing static content on the Tor
network. It automatically communicates with Tor's control port, creates
a hidden service, and serves a local directory as a .onion website.

It is designed for developers, privacy researchers, and users who want a
simple, clean way to deploy static sites over Tor without complex
configuration.

------------------------------------------------------------------------

## One-Line Install and Run

### Termux (Android)

``` bash
pkg update && pkg install -y tor python git && git clone https://github.com/suadatbiniqbal/VeilNode.git && cd VeilNode && pip install stem && mkdir -p $PREFIX/etc/tor && echo -e "ControlPort 9051
CookieAuthentication 0" > $PREFIX/etc/tor/torrc && tor & sleep 15 && pip install -e . && veilnode --sample
```

------------------------------------------------------------------------

## Alternative Termux Installation (.sh Script Method)

Download the installer:

``` bash
curl -O https://raw.githubusercontent.com/suadatbiniqbal/VeilNode/main/install_termux.sh
```

Make it executable:

``` bash
chmod +x install_termux.sh
```

Run the installer:

``` bash
./install_termux.sh
```

------------------------------------------------------------------------

## Linux (Ubuntu/Debian)

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

## macOS

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

## Windows

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

## Step-by-Step Installation

### 1. Clone Repository

``` bash
git clone https://github.com/suadatbiniqbal/VeilNode.git
cd VeilNode
```

Or download the ZIP archive and extract it.

------------------------------------------------------------------------

### 2. Install Tor

Termux:

``` bash
pkg update
pkg install tor python git
```

Linux:

``` bash
sudo apt update
sudo apt install tor python3-pip
```

macOS:

``` bash
brew install tor
```

Windows: Install Tor Browser and keep it running.

------------------------------------------------------------------------

### 3. Configure Tor

Add the following lines to your torrc file:

    ControlPort 9051
    CookieAuthentication 0

Restart Tor after saving the configuration.

------------------------------------------------------------------------

### 4. Install VeilNode

``` bash
pip install -r requirements.txt
pip install -e .
```

Recommended (Linux/macOS):

``` bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

------------------------------------------------------------------------

### 5. Run VeilNode

``` bash
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
veilnode build/                # Host React/Vue build directory
veilnode --help                # Display help information
```

To host multiple sites, run separate instances in different terminals
using different ports.

------------------------------------------------------------------------

## Hosting Your Own Website

### Single Page Example

``` bash
mkdir ~/my-onion-site
cd ~/my-onion-site
veilnode .
```

------------------------------------------------------------------------

### Multi-Page Website

Create a structured directory with HTML, CSS, and assets, then run:

``` bash
veilnode .
```

------------------------------------------------------------------------

### Hosting an Existing Project

For frameworks such as React:

``` bash
npm run build
veilnode build/
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

## Security Notes

-   Avoid publishing personal information.
-   Keep VeilNode running to maintain your .onion address.
-   Use Tor Browser to access hidden services.
-   Test locally before sharing links.

------------------------------------------------------------------------

## License

This project is licensed under the MIT License.

------------------------------------------------------------------------

## Disclaimer

VeilNode is provided for educational and legitimate use only. Users are
solely responsible for ensuring compliance with applicable laws and
regulations in their jurisdiction.
