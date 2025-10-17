#!/bin/bash
# Installation script for yt-down via uv tool or pipx

set -e

echo "🚀 Installing yt-down..."

# Check if uv is available and prefer it
if command -v uv &> /dev/null; then
    echo "✨ Installing via uv tool (recommended)..."
    
    if [ -f "dist/yt_down-0.1.0-py3-none-any.whl" ]; then
        echo "🔧 Installing from local build..."
        uv tool install dist/yt_down-0.1.0-py3-none-any.whl --force
    else
        echo "📦 Installing from PyPI..."
        uv tool install yt-down
    fi
    
    echo "✅ Installation completed via uv!"
    echo "�� You can also run directly without installation: uvx yt-down --help"
    
# Fallback to pipx
elif command -v pipx &> /dev/null; then
    echo "📦 Installing via pipx..."
    
    if [ -f "dist/yt_down-0.1.0-py3-none-any.whl" ]; then
        echo "🔧 Installing from local build..."
        pipx install dist/yt_down-0.1.0-py3-none-any.whl --force
    else
        echo "📦 Installing from PyPI..."
        pipx install yt-down
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
if command -v yt-down &> /dev/null; then
    echo "✅ yt-down installed successfully!"
    echo "📍 Installation location: $(which yt-down)"
    echo "📋 Version info:"
    yt-down --version 2>/dev/null || echo "Version check skipped (not yet published)"
    echo ""
    echo "🎯 Usage examples:"
    echo "  yt-down --url 'https://youtu.be/dQw4w9WgXcQ'"
    echo "  yt-down --playlist 'https://youtube.com/playlist?list=...' --quality 320"
    echo "  yt-down --help"
else
    echo "❌ Installation failed - yt-down command not found"
    echo "💡 Try restarting your terminal or running 'source ~/.bashrc'"
    exit 1
fi

echo ""
echo "🎉 Installation completed successfully!"
echo "💡 You can now use 'yt-down' from anywhere in your terminal"
