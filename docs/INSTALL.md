# 📦 Installation Guide - YouTube Downloader# 📦 Installation Guide - YT-Down# 📦 Installation Guide - YT-Down

This guide covers the recommended ways to install youtube-downloader using modern Python package managers.This guide covers the recommended ways to install yt-down using modern Python package managers.This guide covers the recommended ways to install yt-down using modern Python package managers.

## 🚀 Quick Install (Recommended)## 🚀 Quick Install (Recommended)## 🚀 Quick Install (Recommended)

### Using uvx (Fastest - UV Tool Runner)### Using uvx (Fastest - UV Tool Runner)### Using uvx (Fastest - UV Tool Runner)

The fastest way to try youtube-downloader without installing:The fastest way to try yt-down without installing:```bash

```bash# Install and run directly without installation

# Run directly without installation

uvx ytdwn --help```bashuvx yt-down --help



# Or install permanently via UV# Run directly without installation

uv tool install youtube-downloader

```uvx yt-down --help# Or install permanently via UV



### Using pipx (Isolated Installation)uv tool install yt-down



Recommended for permanent installation with isolation:# Or install permanently via UV```



```bashuv tool install yt-down

# Install pipx if you don't have it

pip install pipx```### Using pipx (Isolated Installation)



# Install youtube-downloader

pipx install youtube-downloader

### Using pipx (Isolated Installation)```bash

# Use from anywhere

ytdwn --help# Install pipx if you don't have it

```

Recommended for permanent installation with isolation:pip install pipx

### Using pip (Global Installation)

⚠️ **Not recommended** - Use pipx or uvx instead for better isolation

```bash# Install yt-down

```bash

pip install youtube-downloader# Install pipx if you don't have itpipx install yt-down

```

pip install pipx

## 🔧 Development Installation

# Use from anywhere

### From Source (Local Development)

# Install yt-downyt-down --help

```bash

# Clone repositorypipx install yt-down```

git clone https://github.com/ozairx/youtube_downloader.git

cd youtube_downloader



# Install with UV (recommended)# Use from anywhere### Using pip (Global Installation)

uv sync

uv run python main.py --helpyt-down --help



# Or install with pip```⚠️ **Not recommended** - Use pipx or uvx instead for better isolation

pip install -e .

```

### Build from Source### Using pip (Global Installation)```bash

```bashpip install yt-down

# Clone and build

git clone https://github.com/ozairx/youtube_downloader.git⚠️ **Not recommended** - Use pipx or uvx instead for better isolation```

cd youtube_downloader

makepkg -si

# Build wheel

bash scripts/build.sh```bash```



# Install built wheel with pipxpip install yt-down

pipx install dist/youtube_downloader-0.1.0-py3-none-any.whl

```### Fedora/RHEL (RPM)

# Or with uvx

uv tool install dist/youtube_downloader-0.1.0-py3-none-any.whl

```

## 🔧 Development Installation```bash

## 🍎 macOS Installation

# When available

### Using pipx (Recommended)

### From Source (Local Development)# sudo dnf install yt-down

```bash

# Install Python if needed```

brew install python

```bash

# Install pipx

pip install pipx# Clone repository## 🔧 Development Installation



# Install youtube-downloadergit clone https://github.com/ozairx/yt-down.git

pipx install youtube-downloader

```cd yt-down### From Source



### Using uvx



```bash# Install with UV (recommended)```bash

# Install UV first

curl -LsSf https://astral.sh/uv/install.sh | shuv sync# Clone repository



# Run directlyuv run python main.py --helpgit clone https://github.com/ozairx/yt-down.git

uvx ytdwn --help

cd yt-down

# Or install permanently

uv tool install youtube-downloader# Or install with pip

```

pip install -e .# Install with UV (recommended)

## 🪟 Windows Installation

```uv sync

### Using pipx

uv run python main.py --help

```powershell

# Install Python from python.org if needed### Build from Source



# Install pipx# Or install with pip

pip install pipx

```bashpip install -e .

# Install youtube-downloader

pipx install youtube-downloader# Clone and build```

```

git clone <https://github.com/ozairx/yt-down.git>

### Using uvx

cd yt-down### Build from Source

```powershell

# Install UV first

powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Build wheel```bash

# Run directly

uvx ytdwn --helpbash scripts/build.sh# Clone and build



# Or install permanentlygit clone https://github.com/ozairx/yt-down.git

uv tool install youtube-downloader

```# Install built wheel with pipxcd yt-down



## 🐧 Linux Installationpipx install dist/yt_down-0.1.0-py3-none-any.whl



### Using pipx# Build wheel



```bash# Or with uvxbash scripts/build.sh

# Install Python and pip if needed (Ubuntu/Debian)

sudo apt install python3 python3-pipuv tool install dist/yt_down-0.1.0-py3-none-any.whl



# Install pipx```# Install built wheel

pip install pipx

pipx install dist/yt_down-0.1.0-py3-none-any.whl

# Add pipx bin to PATH

pipx ensurepath## 🍎 macOS Installation```



# Install youtube-downloader

pipx install youtube-downloader

```### Using pipx (Recommended)## 🍎 macOS Installation



### Using uvx



```bash```bash### Using Homebrew

# Install UV

curl -LsSf https://astral.sh/uv/install.sh | sh# Install Python if needed



# Run directlybrew install python```bash

uvx ytdwn --help

# When available

# Or install permanently

uv tool install youtube-downloader# Install pipx# brew install yt-down

```

pip install pipx```

## 📋 Prerequisites

### System Requirements

# Install yt-down### Using pipx (Recommended)

- **Python**: 3.9 or higher

- **Operating System**: Windows, macOS, or Linuxpipx install yt-down

- **Memory**: 512MB RAM minimum

- **Disk Space**: 100MB for installation + space for downloads``````bash

### Required System Dependencies# Install Python if needed

Some systems may need additional packages:### Using uvxbrew install python

#### Ubuntu/Debian

```bash```bash# Install pipx

sudo apt install ffmpeg

```# Install UV firstpip install pipx



#### macOScurl -LsSf https://astral.sh/uv/install.sh | sh



```bash# Install yt-down

brew install ffmpeg

```# Run directlypipx install yt-down



#### Windowsuvx yt-down --help```



Download FFmpeg from https://ffmpeg.org/download.html and add to PATH.



## 🔄 Updating# Or install permanently## 🪟 Windows Installation



### pipxuv tool install yt-down



```bash```### Using pip

pipx upgrade youtube-downloader

```

### uvx/uv## 🪟 Windows Installation```bash

```bash# Install from PowerShell or Command Prompt

uv tool upgrade youtube-downloader

```### Using pipxpip install yt-down



### pip (if used)



```bash```powershell# Use from anywhere

pip install --upgrade youtube-downloader

```# Install Python from python.org if neededyt-down --help



## 🗑️ Uninstalling```



### pipx# Install pipx



```bashpip install pipx### Using pipx

pipx uninstall youtube-downloader

```# Install yt-down```bash



### uvx/uvpipx install yt-down# Install pipx first



```bash```pip install pipx

uv tool uninstall youtube-downloader

```

### pip (if used)### Using uvx# Install yt-down

```bashpipx install yt-down

pip uninstall youtube-downloader

``````powershell```



## ❓ Troubleshooting# Install UV first



### Common Issuespowershell -c "irm https://astral.sh/uv/install.ps1 | iex"## 🐳 Container Installation



1. **Command not found**: Make sure pipx/uv bin directory is in your PATH

2. **Permission errors**: Use pipx/uvx instead of system pip

3. **FFmpeg missing**: Install FFmpeg for your system (see Prerequisites)# Run directly### Docker



### Getting Helpuvx yt-down --help



```bash```bash

# Check installation

ytdwn --version# Or install permanently# When available



# Get helpuv tool install yt-down# docker run --rm -v $(pwd):/downloads yt-down --url "https://youtu.be/..."

ytdwn --help

``````

# Verbose output for debugging

ytdwn --verbose## 🐧 Linux Installation## ✅ Verify Installation

```

### Using pipxAfter installation, verify it works

### Support

```bash```bash

- **GitHub Issues**: https://github.com/ozairx/youtube_downloader/issues

- **Documentation**: https://github.com/ozairx/youtube_downloader#readme# Install Python and pip if needed (Ubuntu/Debian)# Check version

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
