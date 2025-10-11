#!/bin/bash
# Installation script for yt-down via pipx

set -e

echo "🚀 Installing yt-down via pipx..."

# Check if pipx is installed
if ! command -v pipx &> /dev/null; then
    echo "❌ pipx is not installed. Installing pipx first..."
    
    if command -v uv &> /dev/null; then
        echo "📦 Installing pipx via uv..."
        uv tool install pipx
    elif command -v pip &> /dev/null; then
        echo "📦 Installing pipx via pip..."
        pip install --user pipx
        pipx ensurepath
    else
        echo "❌ Neither uv nor pip found. Please install one of them first."
        exit 1
    fi
fi

# Install yt-down
echo "📦 Installing yt-down..."
if [ -f "dist/yt_down-0.1.0-py3-none-any.whl" ]; then
    # Install from local wheel
    echo "🔧 Installing from local build..."
    pipx install dist/yt_down-0.1.0-py3-none-any.whl --force
else
    # Install from PyPI (when available)
    echo "🌐 Installing from PyPI..."
    pipx install yt-down
fi

# Verify installation
echo "✅ Verifying installation..."
if command -v yt-down &> /dev/null; then
    echo "✅ yt-down installed successfully!"
    echo "📍 Installation location: $(which yt-down)"
    echo "📋 Version info:"
    yt-down --version
    echo ""
    echo "🎯 Usage examples:"
    echo "  yt-down --url 'https://youtu.be/dQw4w9WgXcQ'"
    echo "  yt-down --playlist 'https://youtube.com/playlist?list=...' --quality 320"
    echo "  yt-down --help"
else
    echo "❌ Installation failed - yt-down command not found"
    exit 1
fi

echo ""
echo "🎉 Installation completed successfully!"
echo "💡 You can now use 'yt-down' from anywhere in your terminal"