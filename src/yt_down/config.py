"""
Configuration management for yt-down.
"""

import os
from pathlib import Path

from dotenv import load_dotenv


class Config:
    """Configuration class for yt-down application."""

    def __init__(self, env_file: str | None = None):
        """Initialize configuration."""
        # Load environment variables
        if env_file:
            load_dotenv(env_file)
        else:
            load_dotenv()

        # Download settings
        self.download_dir = Path(os.getenv("DOWNLOAD_DIR", "./downloads"))
        self.temp_dir = Path(os.getenv("TEMP_DIR", "./temp"))
        self.output_format = os.getenv("OUTPUT_FORMAT", "mp3")
        self.audio_quality = int(os.getenv("AUDIO_QUALITY", "192"))

        # Concurrency settings
        self.max_concurrent_downloads = int(os.getenv("MAX_CONCURRENT_DOWNLOADS", "3"))

        # Logging settings
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.log_file = os.getenv("LOG_FILE", "yt-down.log")

        # Create directories if they don't exist
        self.download_dir.mkdir(parents=True, exist_ok=True)
        self.temp_dir.mkdir(parents=True, exist_ok=True)

    def get_output_path(self, title: str, artist: str = "") -> Path:
        """Generate output path for a given title and artist."""
        # Sanitize filename
        safe_title = self._sanitize_filename(title)

        if artist:
            safe_artist = self._sanitize_filename(artist)
            filename = f"{safe_artist} - {safe_title}.{self.output_format}"
        else:
            filename = f"{safe_title}.{self.output_format}"

        return self.download_dir / filename

    def _sanitize_filename(self, filename: str) -> str:
        """Sanitize filename to be safe for filesystem."""
        # Remove or replace invalid characters
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, "_")

        # Remove leading/trailing whitespace and dots
        filename = filename.strip(" .")

        # Limit length
        if len(filename) > 200:
            filename = filename[:200]

        return filename
