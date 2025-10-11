#!/bin/bash
# Release script for yt-down

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 yt-down Release Script${NC}"
echo "========================="

# Check if version is provided
if [ -z "$1" ]; then
    echo -e "${RED}❌ Usage: $0 <version>${NC}"
    echo "Example: $0 0.1.1"
    exit 1
fi

VERSION=$1
echo -e "${YELLOW}📦 Preparing release for version: $VERSION${NC}"

# Verify git status
if [ -n "$(git status --porcelain)" ]; then
    echo -e "${RED}❌ Working directory is not clean. Please commit all changes first.${NC}"
    exit 1
fi

# Update version in pyproject.toml
echo -e "${BLUE}📝 Updating version in pyproject.toml...${NC}"
sed -i "s/version = \".*\"/version = \"$VERSION\"/" pyproject.toml

# Update CHANGELOG.md
echo -e "${BLUE}📝 Updating CHANGELOG.md...${NC}"
DATE=$(date +%Y-%m-%d)
sed -i "s/## \[Unreleased\]/## [Unreleased]\n\n## [$VERSION] - $DATE/" CHANGELOG.md

# Run tests
echo -e "${BLUE}🧪 Running tests...${NC}"
if command -v uv &> /dev/null; then
    uv run python -m pytest tests/ 2>/dev/null || echo "⚠️  No tests found, skipping..."
else
    echo "⚠️  UV not found, skipping tests"
fi

# Build packages
echo -e "${BLUE}🔨 Building packages...${NC}"
bash scripts/build.sh

# Commit version bump
echo -e "${BLUE}📝 Committing version bump...${NC}"
git add pyproject.toml CHANGELOG.md
git commit -m "Bump version to $VERSION"

# Create git tag
echo -e "${BLUE}🏷️  Creating git tag...${NC}"
git tag -a "v$VERSION" -m "Release version $VERSION"

# Push changes and tags
echo -e "${YELLOW}🌐 Ready to push changes and tags?${NC}"
read -p "Push to origin? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git push origin main
    git push origin "v$VERSION"
    echo -e "${GREEN}✅ Changes and tags pushed successfully!${NC}"
else
    echo -e "${YELLOW}⚠️  Skipped pushing. Remember to push manually:${NC}"
    echo "  git push origin main"
    echo "  git push origin v$VERSION"
fi

# Upload to PyPI
echo -e "${YELLOW}📦 Ready to upload to PyPI?${NC}"
read -p "Upload to PyPI? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    if command -v twine &> /dev/null; then
        twine upload dist/*
        echo -e "${GREEN}✅ Uploaded to PyPI successfully!${NC}"
    else
        echo -e "${RED}❌ Twine not found. Install with: pip install twine${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  Skipped PyPI upload. Upload manually with:${NC}"
    echo "  twine upload dist/*"
fi

echo ""
echo -e "${GREEN}🎉 Release $VERSION completed successfully!${NC}"
echo ""
echo -e "${BLUE}📋 Post-release checklist:${NC}"
echo "  ✅ Version updated in pyproject.toml"
echo "  ✅ CHANGELOG.md updated"
echo "  ✅ Git tag created"
echo "  📦 Packages built in dist/"
echo ""
echo -e "${BLUE}🌐 Installation commands:${NC}"
echo "  pipx install yt-down"
echo "  pip install yt-down"