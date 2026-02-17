# VeilNode

A simple Python tool for hosting websites on Tor hidden services. Works on Linux, macOS, Termux, and Windows.

Created by suadatbiniqbal

---

## 🚀 One-Line Install & Run

### Termux (Android)
```bash
pkg update && pkg install -y tor python git && git clone https://github.com/suadatbiniqbal/VeilNode.git && cd VeilNode && pip install stem && mkdir -p $PREFIX/etc/tor && echo -e "ControlPort 9051\nCookieAuthentication 0" > $PREFIX/etc/tor/torrc && tor & sleep 15 && pip install -e . && veilnode --sample
```


## Method 2 
# Download
curl -O https://raw.githubusercontent.com/suadatbiniqbal/VeilNode/main/install_termux.sh

# Make executable
chmod +x install_termux.sh

# Run
./install_termux.sh


### Linux (Ubuntu/Debian)
```bash
sudo apt update && sudo apt install -y tor git python3-pip && sudo systemctl start tor && git clone https://github.com/suadatbiniqbal/VeilNode.git && cd VeilNode && sudo bash -c 'echo -e "ControlPort 9051\nCookieAuthentication 0" >> /etc/tor/torrc' && sudo systemctl restart tor && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && pip install -e . && veilnode --sample
```

### macOS
```bash
brew install tor git && brew services start tor && git clone https://github.com/suadatbiniqbal/VeilNode.git && cd VeilNode && echo -e "ControlPort 9051\nCookieAuthentication 0" >> /usr/local/etc/tor/torrc && brew services restart tor && pip3 install -r requirements.txt && pip3 install -e . && veilnode --sample
```

---

## 📦 Step-by-Step Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/suadatbiniqbal/VeilNode.git
cd VeilNode
```

Or download ZIP:
```bash
wget https://github.com/suadatbiniqbal/VeilNode/archive/main.zip
unzip main.zip
cd VeilNode-main
```

### Step 2: Install Tor

**Termux:**
```bash
pkg update
pkg install tor python git
```

**Linux:**
```bash
sudo apt update
sudo apt install tor python3-pip
```

**macOS:**
```bash
brew install tor
```

**Windows:**
- Download Tor Browser from torproject.org
- Keep it running

### Step 3: Configure Tor

**Termux:**
```bash
mkdir -p $PREFIX/etc/tor
echo "ControlPort 9051" > $PREFIX/etc/tor/torrc
echo "CookieAuthentication 0" >> $PREFIX/etc/tor/torrc
```

**Linux:**
```bash
sudo nano /etc/tor/torrc
```
Add these lines:
```
ControlPort 9051
CookieAuthentication 0
```
Save: `Ctrl+X`, `Y`, `Enter`

**macOS:**
```bash
nano /usr/local/etc/tor/torrc
```
Add:
```
ControlPort 9051
CookieAuthentication 0
```

### Step 4: Start Tor

**Termux:**
```bash
tor &
sleep 15
```

**Linux:**
```bash
sudo systemctl start tor
sudo systemctl enable tor
```

**macOS:**
```bash
brew services start tor
```

### Step 5: Install VeilNode

**All platforms:**
```bash
pip install -r requirements.txt
pip install -e .
```

**Linux (with venv):**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

### Step 6: Run VeilNode

```bash
veilnode --sample
```

---

## 💻 Usage Commands

### Basic Usage

```bash
# Demo site
veilnode --sample

# Your own site
veilnode /path/to/your/site

# Current directory
veilnode .

# Custom port
veilnode --sample -p 9000

# Custom Tor port
veilnode --sample -t 9151

# Combined
veilnode ~/my-site -p 8888
```

### Advanced Usage

```bash
# React/Vue build
veilnode build/

# Multiple sites (separate terminals)
veilnode ~/site1 -p 8080  # Terminal 1
veilnode ~/site2 -p 8081  # Terminal 2

# Help
veilnode --help
```

---

## 🎨 How to Host Your Custom Website

### Option 1: Simple Single Page

```bash
mkdir ~/my-onion-site
cd ~/my-onion-site

cat > index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>My Onion Site</title>
    <style>
        body {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 20vh;
        }
        h1 { font-size: 4em; }
    </style>
</head>
<body>
    <h1>🎭 Hello Dark Web!</h1>
    <p>My first hidden service</p>
</body>
</html>
EOF

veilnode .
```

### Option 2: Multi-Page Website

```bash
mkdir -p ~/my-website/{css,js,images}
cd ~/my-website

# Create index.html
cat > index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <nav>
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
    </nav>
    <h1>Welcome!</h1>
</body>
</html>
EOF

# Create CSS
cat > css/style.css << 'EOF'
body {
    background: #0a0e27;
    color: #00ff41;
    font-family: monospace;
}
nav { padding: 20px; }
nav a { color: #00ff41; margin: 0 20px; }
EOF

veilnode .
```

### Option 3: Host Existing Project

```bash
cd ~/my-react-app
npm run build
veilnode build/
```

---

## 📖 Quick Reference

```bash
# Clone
git clone https://github.com/suadatbiniqbal/VeilNode.git
cd VeilNode

# Install
pip install -r requirements.txt
pip install -e .

# Start Tor
tor &                          # Termux
sudo systemctl start tor       # Linux
brew services start tor        # macOS

# Run
veilnode --sample              # Demo
veilnode .                     # Current dir
veilnode /path/to/site         # Custom path
veilnode --sample -p 9000      # Custom port

# Stop
Ctrl+C
```

---

## 🔧 Troubleshooting

### Tor not running

**Termux:**
```bash
tor &
sleep 15
veilnode --sample
```

**Linux:**
```bash
sudo systemctl start tor
```

**macOS:**
```bash
brew services start tor
```

### Authentication required

```bash
# Edit torrc and set:
CookieAuthentication 0

# Then restart Tor
sudo systemctl restart tor  # Linux
brew services restart tor   # macOS
pkill tor && tor &         # Termux
```

### Port in use

```bash
veilnode --sample -p 9999
```

### Module not found

```bash
pip install stem
```

---

## 🌐 What You Can Host

- HTML/CSS/JavaScript websites
- React/Vue/Angular builds
- Static blogs
- Images, videos, fonts
- Documentation sites
- Portfolios
- Any static content

---

## 🛡️ Security Tips

- Never include personal info
- Keep VeilNode running (stopping changes .onion address)
- Use Tor Browser to access
- Test before sharing

---

## 📁 Project Structure

```
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
```

---

## 📝 License

MIT License

## 👨‍💻 Author

Created by suadatbiniqbal

GitHub: https://github.com/suadatbiniqbal

## ⚠️ Disclaimer

For educational and legitimate purposes only. Users are responsible for complying with all laws.

---

## 🎯 Features

✅ No config editing required  
✅ Works with default Tor  
✅ Built-in sample site  
✅ Custom port support  
✅ Cross-platform  
✅ Auto authentication  
✅ Beautiful terminal UI  

---

**Made with ❤️ by suadatbiniqbal**