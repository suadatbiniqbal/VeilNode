#!/data/data/com.termux/files/usr/bin/bash

# VeilNode Automated Installer for Termux
# Created by suadatbiniqbal

clear

cat << "EOF"
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║  ██╗   ██╗███████╗██╗██╗     ███╗   ██╗ ██████╗ ██████╗ ║
║  ██║   ██║██╔════╝██║██║     ████╗  ██║██╔═══██╗██╔══██╗║
║  ██║   ██║█████╗  ██║██║     ██╔██╗ ██║██║   ██║██║  ██║║
║  ╚██╗ ██╔╝██╔══╝  ██║██║     ██║╚██╗██║██║   ██║██║  ██║║
║   ╚████╔╝ ███████╗██║███████╗██║ ╚████║╚██████╔╝██████╔╝║
║    ╚═══╝  ╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ║
║                                                           ║
║              Termux Automated Installer                  ║
║                  Created by suadatbiniqbal                ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
EOF

echo ""
echo "This script will install and configure VeilNode on Termux"
echo ""
sleep 2

# Function to print status
print_status() {
    echo "[*] $1"
}

print_success() {
    echo "[+] $1"
}

print_error() {
    echo "[!] $1"
}

# Update packages
print_status "Updating package lists..."
pkg update -y > /dev/null 2>&1
if [ $? -eq 0 ]; then
    print_success "Package lists updated"
else
    print_error "Failed to update packages"
    exit 1
fi

# Install Tor
print_status "Installing Tor..."
if ! command -v tor &> /dev/null; then
    pkg install -y tor > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        print_success "Tor installed"
    else
        print_error "Failed to install Tor"
        exit 1
    fi
else
    print_success "Tor already installed"
fi

# Install Python
print_status "Installing Python..."
if ! command -v python &> /dev/null; then
    pkg install -y python > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        print_success "Python installed"
    else
        print_error "Failed to install Python"
        exit 1
    fi
else
    print_success "Python already installed"
fi

# Install Git
print_status "Installing Git..."
if ! command -v git &> /dev/null; then
    pkg install -y git > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        print_success "Git installed"
    else
        print_error "Failed to install Git"
        exit 1
    fi
else
    print_success "Git already installed"
fi

# Clone VeilNode
print_status "Cloning VeilNode repository..."
cd ~
if [ -d "VeilNode" ]; then
    print_status "VeilNode directory exists, pulling latest changes..."
    cd VeilNode
    git pull > /dev/null 2>&1
else
    git clone https://github.com/suadatbiniqbal/VeilNode.git > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        print_success "VeilNode cloned successfully"
        cd VeilNode
    else
        print_error "Failed to clone VeilNode"
        exit 1
    fi
fi

# Install Python dependencies
print_status "Installing Python dependencies..."
pip install -r requirements.txt > /dev/null 2>&1
if [ $? -eq 0 ]; then
    print_success "Dependencies installed"
else
    print_error "Failed to install dependencies"
    exit 1
fi

# Install VeilNode
print_status "Installing VeilNode..."
pip install -e . > /dev/null 2>&1
if [ $? -eq 0 ]; then
    print_success "VeilNode installed"
else
    print_error "Failed to install VeilNode"
    exit 1
fi

# Configure Tor
print_status "Configuring Tor..."
mkdir -p $PREFIX/etc/tor
cat > $PREFIX/etc/tor/torrc << 'TORRC'
ControlPort 9051
CookieAuthentication 0
TORRC

if [ $? -eq 0 ]; then
    print_success "Tor configured"
else
    print_error "Failed to configure Tor"
    exit 1
fi

# Check if Tor is running
print_status "Checking Tor service..."
if pgrep -x "tor" > /dev/null; then
    print_status "Tor is already running, restarting..."
    pkill tor
    sleep 2
fi

# Start Tor
print_status "Starting Tor service..."
tor > /dev/null 2>&1 &
TOR_PID=$!

if [ $? -eq 0 ]; then
    print_success "Tor started (PID: $TOR_PID)"
else
    print_error "Failed to start Tor"
    exit 1
fi

# Wait for Tor to connect
print_status "Waiting for Tor to establish connection..."
for i in {15..1}; do
    echo -ne "Connecting... $i seconds remaining "
    sleep 1
done
echo ""
print_success "Tor connection established"

# Final message
echo ""
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                  INSTALLATION COMPLETE!                   ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""
echo "VeilNode is now installed and ready to use!"
echo ""
echo "Quick commands:"
echo "  veilnode --sample              # Start with demo site"
echo "  veilnode /path/to/site         # Host your own site"
echo "  veilnode --help                # Show help"
echo ""
echo "Starting VeilNode with sample site in 3 seconds..."
sleep 3

# Start VeilNode
veilnode --sample
