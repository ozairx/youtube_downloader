#!/bin/bash
# Installation script for youtube-downloader via uv tool or pipx

set -e

echo "🚀 Installing youtube-downloader..."

# Check if uv is available and prefer it
if command -v uv &> /dev/null; then
    echo "✨ Installing via uv tool (recommended)..."
    
    if [ -f "dist/youtube_downloader-0.1.0-py3-none-any.whl" ]; then
        echo "🔧 Installing from local build..."
        uv tool install dist/youtube_downloader-0.1.0-py3-none-any.whl --force
    else
        echo "📦 Installing from PyPI..."
        uv tool install youtube-downloader
    fi
    
    echo "✅ Installation completed via uv!"
    echo "💡 You can also run directly without installation: uvx ytdwn --help"
    
# Fallback to pipx
elif command -v pipx &> /dev/null; then
    echo "📦 Installing via pipx..."
    
    if [ -f "dist/youtube_downloader-0.1.0-py3-none-any.whl" ]; then
        echo "🔧 Installing from local build..."
        pipx install dist/youtube_downloader-0.1.0-py3-none-any.whl --force
    else
        echo "📦 Installing from PyPI..."
        pipx install youtube-downloader
    fi
    
    echo "✅ Installation completed via pipx!"

# Neither uv nor pipx available
else
    echo "❌ Neither uv nor pipx found."
    echo "Please install one of them first:"
    echo ""
    echo "📦 Install UV (recommended):"
    echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo ""
    echo "📦 Install pipx:"
    echo "  pip install pipx"
    echo ""
    exit 1
fi

# Verify installation
echo "✅ Verifying installation..."
if command -v ytdwn &> /dev/null; then
    echo "✅ ytdwn installed successfully!"
    echo "📍 Installation location: $(which ytdwn)"
    echo "📋 Version info:"
    ytdwn --version 2>/dev/null || echo "Version check skipped (not yet published)"
    echo ""
    echo "🎯 Usage examples:"
    echo "  ytdwn --url 'https://youtu.be/dQw4w9WgXcQ'"
    echo "  ytdwn --playlist 'https://youtube.com/playlist?list=...' --quality 320"
    echo "  ytdwn --help"
else
    echo "❌ Installation failed - ytdwn command not found"
    echo "💡 Try restarting your terminal or running 'source ~/.bashrc'"
    exit 1
fi

echo ""
echo "🎉 Installation completed successfully!"
echo "💡 You can now use 'ytdwn' from anywhere in your terminal"
