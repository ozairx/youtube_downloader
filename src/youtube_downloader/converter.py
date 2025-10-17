"""
Audio conversion utilities using moviepy.
"""

import logging
from pathlib import Path

from moviepy.editor import AudioFileClip
from mutagen.easyid3 import EasyID3
from mutagen.id3._util import ID3NoHeaderError
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
)

from .config import Config


class AudioConverter:
    """Audio file converter and metadata handler."""

    def __init__(self, config: Config):
        """Initialize converter with configuration."""
        self.config = config
        self.logger = logging.getLogger("ytdwn.converter")

    def convert_to_mp3(
        self, input_file: str, title: str, artist: str = ""
    ) -> str | None:
        """Convert audio file to MP3 with metadata."""
        input_path = Path(input_file)

        if not input_path.exists():
            self.logger.error(f"Input file not found: {input_file}")
            return None

        # Generate output path
        output_path = self.config.get_output_path(title, artist)

        try:
            self.logger.debug(f"Converting {input_path.name} to MP3")

            # Load audio clip
            audio_clip = AudioFileClip(str(input_path))

            # Convert to MP3 with specified bitrate
            audio_clip.write_audiofile(
                str(output_path),
                bitrate=f"{self.config.audio_quality}k",
                verbose=False,
                logger=None,  # Disable moviepy logging
            )

            # Close clip to free resources
            audio_clip.close()

            self.logger.debug(f"Conversion completed: {output_path}")

            # Add metadata
            self._add_metadata(output_path, title, artist)

            # Clean up temp file
            try:
                input_path.unlink()
                self.logger.debug(f"Cleaned up temp file: {input_path}")
            except Exception as e:
                self.logger.warning(f"Could not clean up temp file: {e}")

            return str(output_path)

        except Exception as e:
            self.logger.error(f"Error converting {input_file}: {e}")
            return None

    def _add_metadata(self, file_path: Path, title: str, artist: str = "") -> None:
        """Add ID3 metadata to MP3 file."""
        try:
            self.logger.debug(f"Adding metadata to: {file_path}")

            # Initialize ID3 tags
            try:
                audio_file = EasyID3(str(file_path))
            except ID3NoHeaderError:
                audio_file = EasyID3()

            # Set metadata
            audio_file["title"] = title
            if artist:
                audio_file["artist"] = artist
                audio_file["albumartist"] = artist

            # Save metadata
            audio_file.save(str(file_path))
            self.logger.debug("Metadata added successfully")

        except Exception as e:
            self.logger.warning(f"Could not add metadata: {e}")

    def convert_batch(
        self, files_and_metadata: list[tuple[str, str, str]]
    ) -> list[str]:
        """Convert multiple files to MP3.

        Args:
            files_and_metadata: List of tuples (file_path, title, artist)

        Returns:
            List of successfully converted file paths
        """
        converted_files = []

        # Criar barra de progresso moderna para conversão
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold cyan]{task.description}"),
            BarColumn(complete_style="cyan", finished_style="bright_cyan"),
            TextColumn("[progress.percentage]{task.percentage:>3.1f}%"),
            TextColumn("({task.completed}/{task.total})"),
            TimeElapsedColumn(),
            expand=True,
        ) as progress:
            task = progress.add_task(
                "🎧 Convertendo para MP3", total=len(files_and_metadata)
            )

            for file_path, title, artist in files_and_metadata:
                self.logger.debug(f"Converting: {title}")

                converted_file = self.convert_to_mp3(file_path, title, artist)

                if converted_file:
                    converted_files.append(converted_file)
                    self.logger.debug(f"Successfully converted: {converted_file}")
                else:
                    self.logger.error(f"Failed to convert: {file_path}")

                progress.update(task, advance=1)

        self.logger.debug(
            f"Batch conversion completed. {len(converted_files)}/{len(files_and_metadata)} files converted"
        )
        return converted_files
