# 📦 Installation Guide - YT-Down# 📦 Installation Guide - YT-Down

This guide covers the recommended ways to install yt-down using modern Python package managers.This guide covers the recommended ways to install yt-down using modern Python package managers.

## 🚀 Quick Install (Recommended)## 🚀 Quick Install (Recommended)

### Using uvx (Fastest - UV Tool Runner)### Using uvx (Fastest - UV Tool Runner)

The fastest way to try yt-down without installing:```bash

# Install and run directly without installation

```bashuvx yt-down --help

# Run directly without installation

uvx yt-down --help# Or install permanently via UV

uv tool install yt-down

# Or install permanently via UV```

uv tool install yt-down

```### Using pipx (Isolated Installation)



### Using pipx (Isolated Installation)```bash

# Install pipx if you don't have it

Recommended for permanent installation with isolation:pip install pipx



```bash# Install yt-down

# Install pipx if you don't have itpipx install yt-down

pip install pipx

# Use from anywhere

# Install yt-downyt-down --help

pipx install yt-down```



# Use from anywhere### Using pip (Global Installation)

yt-down --help

```⚠️ **Not recommended** - Use pipx or uvx instead for better isolation



### Using pip (Global Installation)```bash

pip install yt-down

⚠️ **Not recommended** - Use pipx or uvx instead for better isolation```

makepkg -si

```bash```

pip install yt-down

```### Fedora/RHEL (RPM)



## 🔧 Development Installation```bash

# When available

### From Source (Local Development)# sudo dnf install yt-down

```

```bash

# Clone repository## 🔧 Development Installation

git clone https://github.com/ozairx/yt-down.git

cd yt-down### From Source



# Install with UV (recommended)```bash

uv sync# Clone repository

uv run python main.py --helpgit clone https://github.com/ozairx/yt-down.git

cd yt-down

# Or install with pip

pip install -e .# Install with UV (recommended)

```uv sync

uv run python main.py --help

### Build from Source

# Or install with pip

```bashpip install -e .

# Clone and build```

git clone https://github.com/ozairx/yt-down.git

cd yt-down### Build from Source



# Build wheel```bash

bash scripts/build.sh# Clone and build

git clone https://github.com/ozairx/yt-down.git

# Install built wheel with pipxcd yt-down

pipx install dist/yt_down-0.1.0-py3-none-any.whl

# Build wheel

# Or with uvxbash scripts/build.sh

uv tool install dist/yt_down-0.1.0-py3-none-any.whl

```# Install built wheel

pipx install dist/yt_down-0.1.0-py3-none-any.whl

## 🍎 macOS Installation```



### Using pipx (Recommended)## 🍎 macOS Installation



```bash### Using Homebrew

# Install Python if needed

brew install python```bash

# When available

# Install pipx# brew install yt-down

pip install pipx```



# Install yt-down### Using pipx (Recommended)

pipx install yt-down

``````bash

# Install Python if needed

### Using uvxbrew install python



```bash# Install pipx

# Install UV firstpip install pipx

curl -LsSf https://astral.sh/uv/install.sh | sh

# Install yt-down

# Run directlypipx install yt-down

uvx yt-down --help```



# Or install permanently## 🪟 Windows Installation

uv tool install yt-down

```### Using pip



## 🪟 Windows Installation```bash

# Install from PowerShell or Command Prompt

### Using pipxpip install yt-down



```powershell# Use from anywhere

# Install Python from python.org if neededyt-down --help

```

# Install pipx

pip install pipx### Using pipx

# Install yt-down```bash

pipx install yt-down# Install pipx first

```pip install pipx



### Using uvx# Install yt-down

pipx install yt-down

```powershell```

# Install UV first

powershell -c "irm https://astral.sh/uv/install.ps1 | iex"## 🐳 Container Installation



# Run directly### Docker

uvx yt-down --help

```bash

# Or install permanently# When available

uv tool install yt-down# docker run --rm -v $(pwd):/downloads yt-down --url "https://youtu.be/..."

``````

## 🐧 Linux Installation## ✅ Verify Installation

### Using pipxAfter installation, verify it works

```bash```bash

# Install Python and pip if needed (Ubuntu/Debian)# Check version

sudo apt install python3 python3-pipyt-down --version

# Install pipx# Show help

pip install pipxyt-down --help

# Add pipx bin to PATH# Test with a short video (optional)

pipx ensurepathyt-down --url "<https://youtu.be/dQw4w9WgXcQ>" --output-dir ./test

```

# Install yt-down

pipx install yt-down## 🔄 Updating

```

### pipx

### Using uvx

```bash

```bashpipx upgrade yt-down

# Install UV```

curl -LsSf https://astral.sh/uv/install.sh | sh

### pip

# Run directly

uvx yt-down --help```bash

pip install --upgrade yt-down

# Or install permanently```

uv tool install yt-down

```### Package Managers



## 📋 Prerequisites```bash

# Ubuntu/Debian

### System Requirementssudo apt update && sudo apt upgrade yt-down



- **Python**: 3.9 or higher# Arch Linux

- **Operating System**: Windows, macOS, or Linuxyay -Syu yt-down

- **Memory**: 512MB RAM minimum```

- **Disk Space**: 100MB for installation + space for downloads

## 🗑️ Uninstalling

### Required System Dependencies

### pipx

Some systems may need additional packages:

```bash

#### Ubuntu/Debianpipx uninstall yt-down

```

```bash

sudo apt install ffmpeg### pip

```

```bash

#### macOSpip uninstall yt-down

```

```bash

brew install ffmpeg### Package Managers

```

```bash

#### Windows# Ubuntu/Debian

sudo apt remove yt-down

Download FFmpeg from https://ffmpeg.org/download.html and add to PATH.

# Arch Linux

## 🔄 Updatingsudo pacman -R yt-down

```

### pipx

## 🛠️ Dependencies

```bash

pipx upgrade yt-downyt-down requires:

```

- **Python 3.9+** - Core runtime

### uvx/uv- **ffmpeg** - Audio/video processing (auto-installed on most systems)

```bash### Manual ffmpeg Installation

uv tool upgrade yt-down

```**Ubuntu/Debian:**



### pip (if used)```bash

sudo apt install ffmpeg

```bash```

pip install --upgrade yt-down

```**macOS:**



## 🗑️ Uninstalling```bash

brew install ffmpeg

### pipx```



```bash**Windows:**

pipx uninstall yt-down

```- Download from [ffmpeg.org](https://ffmpeg.org/download.html)

- Or use: `winget install ffmpeg`

### uvx/uv

## 🆘 Troubleshooting

```bash

uv tool uninstall yt-down### Common Issues

```

**Command not found after installation:**

### pip (if used)

```bash

```bash# For pipx, ensure PATH is updated

pip uninstall yt-downpipx ensurepath

```source ~/.bashrc  # or restart terminal

```

## ❓ Troubleshooting

**Permission errors on Linux/macOS:**

### Common Issues

```bash

1. **Command not found**: Make sure pipx/uv bin directory is in your PATH# Use pipx instead of pip for user installation

2. **Permission errors**: Use pipx/uvx instead of system pippipx install yt-down

3. **FFmpeg missing**: Install FFmpeg for your system (see Prerequisites)```



### Getting Help**Python version too old:**



```bash```bash

# Check installation# Check Python version

yt-down --versionpython --version



# Get help# Upgrade Python or use pyenv/conda

yt-down --help```



# Verbose output for debugging### Get Help

yt-down --verbose

```- 📖 [Documentation](https://github.com/ozairx/yt-down#readme)

- 🐛 [Report Issues](https://github.com/ozairx/yt-down/issues)

### Support- 💬 [Discussions](https://github.com/ozairx/yt-down/discussions)



- **GitHub Issues**: https://github.com/ozairx/yt-down/issues---

- **Documentation**: https://github.com/ozairx/yt-down#readme
**Installation successful?** Start using yt-down with our [Usage Guide](USAGE.md)!
