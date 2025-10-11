#!/bin/bash
# Build script for yt-down distribution packages

set -e

echo "🏗️  Building yt-down distribution packages..."

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info/
find . -name __pycache__ -type d -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true

# Install build dependencies
echo "📦 Installing build dependencies..."
if command -v uv &> /dev/null; then
    uv sync --extra dev
else
    pip install -e ".[dev]"
fi

# Build wheel and source distribution
echo "🔨 Building wheel and source distribution..."
python -m build

# Verify build
echo "✅ Verifying build..."
if [ -f "dist/yt_down-0.1.0-py3-none-any.whl" ] && [ -f "dist/yt_down-0.1.0.tar.gz" ]; then
    echo "✅ Build successful!"
    echo "📦 Generated files:"
    ls -la dist/
else
    echo "❌ Build failed - missing expected files"
    echo "📦 Generated files:"
    ls -la dist/ 2>/dev/null || echo "No dist directory found"
    exit 1
fi

# Test installation in virtual environment
echo "🧪 Testing installation..."
TEMP_VENV=$(mktemp -d)
python -m venv "$TEMP_VENV"
source "$TEMP_VENV/bin/activate"

pip install dist/yt_down-0.1.0-py3-none-any.whl
yt-down --help > /dev/null && echo "✅ CLI test passed" || echo "❌ CLI test failed"

deactivate
rm -rf "$TEMP_VENV"

echo "🎉 Build and test completed successfully!"
echo ""
echo "📋 Next steps:"
echo "  • Upload to PyPI: twine upload dist/*"
echo "  • Install via pipx: pipx install dist/yt_down-0.1.0-py3-none-any.whl"
echo "  • Test from PyPI: pipx install yt-down"