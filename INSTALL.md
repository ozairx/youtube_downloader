# 📦 Installation Guide - YT-Down

This guide covers multiple ways to install yt-down on different systems.

## 🚀 Quick Install (Recommended)

### Using pipx (Isolated Installation)

```bash
# Install pipx if you don't have it
pip install pipx

# Install yt-down
pipx install yt-down

# Use from anywhere
yt-down --help
```

### Using pip (Global Installation)

```bash
pip install yt-down
```

## 🐧 Linux Package Managers

### Ubuntu/Debian (APT)

```bash
# Add repository (when available)
# sudo add-apt-repository ppa:username/yt-down
# sudo apt update

# Install
# sudo apt install yt-down
```

### Arch Linux (AUR)

```bash
# Using yay
yay -S yt-down

# Using paru
paru -S yt-down

# Manual build
git clone https://aur.archlinux.org/yt-down.git
cd yt-down
makepkg -si
```

### Fedora/RHEL (RPM)

```bash
# When available
# sudo dnf install yt-down
```

## 🔧 Development Installation

### From Source

```bash
# Clone repository
git clone https://github.com/ozairx/yt-down.git
cd yt-down

# Install with UV (recommended)
uv sync
uv run python main.py --help

# Or install with pip
pip install -e .
```

### Build from Source

```bash
# Clone and build
git clone https://github.com/ozairx/yt-down.git
cd yt-down

# Build wheel
bash scripts/build.sh

# Install built wheel
pipx install dist/yt_down-0.1.0-py3-none-any.whl
```

## 🍎 macOS Installation

### Using Homebrew

```bash
# When available
# brew install yt-down
```

### Using pipx (Recommended)

```bash
# Install Python if needed
brew install python

# Install pipx
pip install pipx

# Install yt-down
pipx install yt-down
```

## 🪟 Windows Installation

### Using pip

```bash
# Install from PowerShell or Command Prompt
pip install yt-down

# Use from anywhere
yt-down --help
```

### Using pipx

```bash
# Install pipx first
pip install pipx

# Install yt-down
pipx install yt-down
```

## 🐳 Container Installation

### Docker

```bash
# When available
# docker run --rm -v $(pwd):/downloads yt-down --url "https://youtu.be/..."
```

## ✅ Verify Installation

After installation, verify it works:

```bash
# Check version
yt-down --version

# Show help
yt-down --help

# Test with a short video (optional)
yt-down --url "https://youtu.be/dQw4w9WgXcQ" --output-dir ./test
```

## 🔄 Updating

### pipx

```bash
pipx upgrade yt-down
```

### pip

```bash
pip install --upgrade yt-down
```

### Package Managers

```bash
# Ubuntu/Debian
sudo apt update && sudo apt upgrade yt-down

# Arch Linux
yay -Syu yt-down
```

## 🗑️ Uninstalling

### pipx

```bash
pipx uninstall yt-down
```

### pip

```bash
pip uninstall yt-down
```

### Package Managers

```bash
# Ubuntu/Debian
sudo apt remove yt-down

# Arch Linux
sudo pacman -R yt-down
```

## 🛠️ Dependencies

yt-down requires:

- **Python 3.9+** - Core runtime
- **ffmpeg** - Audio/video processing (auto-installed on most systems)

### Manual ffmpeg Installation

**Ubuntu/Debian:**

```bash
sudo apt install ffmpeg
```

**macOS:**

```bash
brew install ffmpeg
```

**Windows:**

- Download from [ffmpeg.org](https://ffmpeg.org/download.html)
- Or use: `winget install ffmpeg`

## 🆘 Troubleshooting

### Common Issues

**Command not found after installation:**

```bash
# For pipx, ensure PATH is updated
pipx ensurepath
source ~/.bashrc  # or restart terminal
```

**Permission errors on Linux/macOS:**

```bash
# Use pipx instead of pip for user installation
pipx install yt-down
```

**Python version too old:**

```bash
# Check Python version
python --version

# Upgrade Python or use pyenv/conda
```

### Get Help

- 📖 [Documentation](https://github.com/ozairx/yt-down#readme)
- 🐛 [Report Issues](https://github.com/ozairx/yt-down/issues)
- 💬 [Discussions](https://github.com/ozairx/yt-down/discussions)

---

**Installation successful?** Start using yt-down with our [Usage Guide](USAGE.md)!
