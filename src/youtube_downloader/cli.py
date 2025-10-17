"""
Command line interface for yt-down.
"""

from pathlib import Path

import click

from .config import Config
from .logger import setup_logging


@click.command()
@click.option(
    "--url",
    "-u",
    help="YouTube video URL to download",
    type=str,
)
@click.option(
    "--playlist",
    "-p",
    help="YouTube playlist URL to download",
    type=str,
)
@click.option(
    "--output-dir",
    "-o",
    help="Output directory for downloaded files",
    type=click.Path(exists=False, file_okay=False, dir_okay=True, path_type=str),
)
@click.option(
    "--quality",
    "-q",
    help="Audio quality in kbps (default: 192)",
    type=int,
    default=192,
)
@click.option(
    "--format",
    "-f",
    help="Output format (default: mp3)",
    type=click.Choice(["mp3", "wav", "m4a"]),
    default="mp3",
)
@click.option(
    "--concurrent",
    "-c",
    help="Maximum concurrent downloads (default: 3)",
    type=int,
    default=3,
)
@click.option(
    "--verbose",
    "-v",
    help="Enable verbose logging",
    is_flag=True,
)
@click.version_option(version="0.1.0", prog_name="yt-down")
def main(
    url: str | None,
    playlist: str | None,
    output_dir: str | None,
    quality: int,
    format: str,
    concurrent: int,
    verbose: bool,
) -> None:
    """Download YouTube videos and convert them to MP3."""
    # Setup logging
    if verbose:
        log_level = "DEBUG"
        logger = setup_logging(log_level)
        logger.info("Starting yt-down v0.1.0")
        logger.info(
            f"Output directory: {Path(output_dir) if output_dir else Path.cwd() / 'downloads'}"
        )
        logger.info(f"Audio quality: {quality}kbps")
        logger.info(f"Output format: {format}")
    else:
        # In non-verbose mode, suppress INFO logs (only show WARNING and above)
        log_level = "WARNING"
        logger = setup_logging(log_level, quiet_mode=True)

    # Load configuration
    config = Config()

    # Override config with CLI arguments
    if output_dir:
        config.download_dir = Path(output_dir)
        config.download_dir.mkdir(parents=True, exist_ok=True)

    config.audio_quality = quality
    config.output_format = format
    config.max_concurrent_downloads = concurrent

    # Validate input
    if not url and not playlist:
        click.echo("Error: You must specify either --url or --playlist", err=True)
        raise click.Abort()

    if url and playlist:
        click.echo("Error: You cannot specify both --url and --playlist", err=True)
        raise click.Abort()

    try:
        from .app import YTDownApp

        # Create main application
        app = YTDownApp(config)

        if url:
            if verbose:
                logger.info(f"Downloading single video: {url}")

            success = app.process_single_video(url)
            if success:
                click.echo("✓ Video downloaded and converted successfully!")
            else:
                click.echo("✗ Failed to download video", err=True)
                raise click.Abort()

        elif playlist:
            if verbose:
                logger.info(f"Downloading playlist: {playlist}")

            successful, total = app.process_playlist(playlist)
            if successful > 0:
                click.echo(
                    f"✓ Playlist download completed: {successful}/{total} videos processed"
                )
            else:
                click.echo("✗ Failed to download any videos from playlist", err=True)
                raise click.Abort()

    except Exception as e:
        if verbose:
            logger.error(f"An error occurred: {e}")
        else:
            click.echo(f"✗ Error: {e}", err=True)
        raise click.Abort() from e


if __name__ == "__main__":
    main()
