# ⚡ FORGE - Terminal Swiss Army Knife ⚡

> *No internet? No problem. Powerful tools in your terminal.*

## 🚀 Installation (Android / Termux friendly)

```bash
git clone https://github.com/yourusername/forge.git
cd forge

# Install core lightweight libraries (Will not crash on Android)
pip install -r requirements.txt

# Run the app
python forge.py
```

## 🛠️ Features & Optional Dependencies

Forge is designed to be bulletproof. If you are missing a heavy dependency (like `psutil` or `imageio`), the script will still run perfectly! When you click on a feature you don't have the libraries for, it will gracefully tell you what to install.

1. **🌧️ Matrix Rain** - Classic digital waterfall *(Built-in)*
2. **🌀 Hypnotic Spirograph** - Parametric ASCII art *(Built-in)*
3. **⌨️ Hacker Typer** - Fast-paced offline typing test *(Built-in)*
4. **📱 ASCII QR Generator** - Terminal QR codes *(Requires: `qrcode`)*
5. **🖼️ Image to ASCII Preview** - Block art *(Requires: `pillow`)*
6. **🎬 Video Player (ASCII Cinema)** - Terminal MP4 player *(Requires: `imageio`, `imageio-ffmpeg`, `numpy`, `pillow`)*
7. **🔐 Iron Vault** - Robust offline password generator *(Built-in)*
8. **🗄️ File Locker** - AES File Encryption *(Requires: `cryptography`)*
9. **📊 System Scope** - Live hardware monitor *(Requires: `psutil`)*

## 🎬 Video Player Controls
- **Space**: Play / Pause
- **Right Arrow**: Seek Forward (10s)
- **Left Arrow**: Seek Backward (10s)
- **q**: Quit Player

## ⚠️ Legal / Disclaimer
This tool is provided for **educational and entertainment purposes only**. All tools run entirely offline using local files and resources. No data is transmitted.
