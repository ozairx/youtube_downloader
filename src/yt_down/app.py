"""
Main orchestrator for yt-down application.
"""

import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

from pytubefix import YouTube

from .config import Config
from .converter import AudioConverter
from .downloader import YouTubeDownloader
from .utils import is_youtube_playlist_url, is_youtube_url


class YTDownApp:
    """Main application class that orchestrates download and conversion."""

    def __init__(self, config: Config):
        """Initialize application with configuration."""
        self.config = config
        self.logger = logging.getLogger("yt-down.app")
        self.downloader = YouTubeDownloader(config)
        self.converter = AudioConverter(config)

    def process_single_video(self, url: str) -> bool:
        """Download and convert a single video."""
        try:
            # Validate URL
            if not is_youtube_url(url):
                self.logger.error(f"Invalid YouTube URL: {url}")
                return False

            # Get video metadata
            yt = YouTube(url)
            title = yt.title
            author = yt.author

            self.logger.info(f"Processing: {title} by {author}")

            # Download video
            downloaded_file = self.downloader.download_video(url)
            if not downloaded_file:
                self.logger.error(f"Failed to download video: {url}")
                return False

            # Convert to MP3
            converted_file = self.converter.convert_to_mp3(
                downloaded_file, title, author
            )
            if not converted_file:
                self.logger.error(f"Failed to convert video: {downloaded_file}")
                return False

            self.logger.info(f"Successfully processed: {converted_file}")
            return True

        except Exception as e:
            self.logger.error(f"Error processing video {url}: {e}")
            return False

    def process_playlist(self, url: str) -> tuple[int, int]:
        """Download and convert all videos from a playlist.

        Returns:
            Tuple of (successful_count, total_count)
        """
        try:
            # Validate URL
            if not is_youtube_playlist_url(url):
                self.logger.error(f"Invalid YouTube playlist URL: {url}")
                return 0, 0

            # Download all videos from playlist
            downloaded_files = self.downloader.download_playlist(url)

            if not downloaded_files:
                self.logger.error("No videos were downloaded from playlist")
                return 0, 0

            # Prepare conversion data with metadata extraction
            conversion_data = []
            for downloaded_file in downloaded_files:
                try:
                    # Extract metadata from filename or use a mapping
                    # For now, we'll use a basic approach based on temp filename
                    from pathlib import Path

                    temp_path = Path(downloaded_file)
                    # Extract from temp filename pattern: "Artist - Title_temp.mp4"
                    base_name = temp_path.stem.replace("_temp", "")

                    # Try to split by " - " to get artist and title
                    if " - " in base_name:
                        parts = base_name.split(" - ", 1)
                        if len(parts) == 2:
                            video_author = parts[0].strip()
                            video_title = parts[1].strip()
                        else:
                            video_author = "Unknown Artist"
                            video_title = base_name
                    else:
                        video_author = "Unknown Artist"
                        video_title = base_name

                    conversion_data.append((downloaded_file, video_title, video_author))
                except Exception as e:
                    self.logger.warning(
                        f"Could not get metadata for {downloaded_file}: {e}"
                    )
                    conversion_data.append(
                        (downloaded_file, "Unknown Title", "Unknown Artist")
                    )

            # Convert all files
            converted_files = self.converter.convert_batch(conversion_data)

            successful_count = len(converted_files)
            total_count = len(downloaded_files)

            self.logger.info(
                f"Playlist processing completed: {successful_count}/{total_count} videos converted"
            )
            return successful_count, total_count

        except Exception as e:
            self.logger.error(f"Error processing playlist {url}: {e}")
            return 0, 0

    def process_multiple_urls(self, urls: list[str]) -> tuple[int, int]:
        """Process multiple URLs concurrently.

        Returns:
            Tuple of (successful_count, total_count)
        """
        successful_count = 0
        total_count = len(urls)

        # Use ThreadPoolExecutor for concurrent processing
        with ThreadPoolExecutor(
            max_workers=self.config.max_concurrent_downloads
        ) as executor:
            # Submit all tasks
            future_to_url = {
                executor.submit(self.process_single_video, url): url for url in urls
            }

            # Process completed tasks
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    result = future.result()
                    if result:
                        successful_count += 1
                        self.logger.info(f"Successfully processed: {url}")
                    else:
                        self.logger.error(f"Failed to process: {url}")
                except Exception as e:
                    self.logger.error(f"Exception processing {url}: {e}")

        self.logger.info(
            f"Batch processing completed: {successful_count}/{total_count} URLs processed successfully"
        )
        return successful_count, total_count
