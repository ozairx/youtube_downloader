"""
YouTube downloader implementation.
"""

import logging
from typing import Any

from pytube import Playlist, YouTube
from tqdm import tqdm

from .config import Config
from .utils import is_youtube_playlist_url, is_youtube_url, normalize_youtube_url


class YouTubeDownloader:
    """YouTube video and playlist downloader."""

    def __init__(self, config: Config):
        """Initialize downloader with configuration."""
        self.config = config
        self.logger = logging.getLogger("yt-down.downloader")

    def download_video(self, url: str) -> str | None:
        """Download a single video and return the path to downloaded file."""
        # Validate URL
        if not is_youtube_url(url):
            self.logger.error(f"Invalid YouTube URL: {url}")
            return None

        # Normalize URL
        normalized_url = normalize_youtube_url(url)
        if not normalized_url:
            self.logger.error(f"Could not normalize URL: {url}")
            return None

        try:
            self.logger.info(f"Fetching video info for: {normalized_url}")

            # Create YouTube object
            yt = YouTube(
                normalized_url,
                on_progress_callback=self._progress_callback,
                on_complete_callback=self._complete_callback,
            )

            # Get video info
            title = yt.title
            author = yt.author
            length = yt.length

            self.logger.info(f"Title: {title}")
            self.logger.info(f"Author: {author}")
            self.logger.info(f"Duration: {length}s")

            # Get the highest quality audio stream
            audio_stream = yt.streams.filter(
                only_audio=True, file_extension="mp4"
            ).first()

            if not audio_stream:
                self.logger.error("No audio stream available")
                return None

            # Generate output filename
            output_path = self.config.get_output_path(title, author)
            temp_path = self.config.temp_dir / f"{output_path.stem}_temp.mp4"

            self.logger.info(f"Downloading to: {temp_path}")

            # Download the audio
            audio_stream.download(
                output_path=str(self.config.temp_dir),
                filename=temp_path.name,
            )

            self.logger.info(f"Download completed: {temp_path}")
            return str(temp_path)

        except Exception as e:
            self.logger.error(f"Error downloading video {url}: {e}")
            return None

    def download_playlist(self, url: str) -> list[str]:
        """Download all videos from a playlist and return list of downloaded files."""
        # Validate URL
        if not is_youtube_playlist_url(url):
            self.logger.error(f"Invalid YouTube playlist URL: {url}")
            return []

        try:
            self.logger.info(f"Fetching playlist info for: {url}")

            # Create Playlist object
            playlist = Playlist(url)

            # Get playlist info
            title = playlist.title
            owner = playlist.owner
            video_count = len(playlist.video_urls)

            self.logger.info(f"Playlist: {title}")
            self.logger.info(f"Owner: {owner}")
            self.logger.info(f"Videos: {video_count}")

            downloaded_files = []

            # Download each video with progress bar
            with tqdm(total=video_count, desc="Downloading playlist") as pbar:
                for i, video_url in enumerate(playlist.video_urls, 1):
                    self.logger.info(f"Downloading video {i}/{video_count}")

                    # Download individual video
                    downloaded_file = self.download_video(video_url)

                    if downloaded_file:
                        downloaded_files.append(downloaded_file)
                        self.logger.info(f"Successfully downloaded: {downloaded_file}")
                    else:
                        self.logger.warning(f"Failed to download video: {video_url}")

                    pbar.update(1)

            self.logger.info(
                f"Playlist download completed. {len(downloaded_files)}/{video_count} videos downloaded"
            )
            return downloaded_files

        except Exception as e:
            self.logger.error(f"Error downloading playlist {url}: {e}")
            return []

    def _progress_callback(
        self, stream: Any, chunk: bytes, bytes_remaining: int
    ) -> None:
        """Callback for download progress."""
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100

        # Log progress every 10%
        if int(percentage) % 10 == 0:
            self.logger.debug(f"Download progress: {percentage:.1f}%")
            self.logger.debug(f"Download progress: {percentage:.1f}%")

    def _complete_callback(self, stream: Any, file_path: str | None) -> None:
        """Callback for download completion."""
        if file_path is not None:
            self.logger.debug(f"Download completed: {file_path}")
        else:
            self.logger.debug("Download completed")
        self.logger.debug(f"Download completed: {file_path}")
