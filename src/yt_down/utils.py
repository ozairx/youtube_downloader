"""
URL validation utilities for YouTube.
"""

import re
from urllib.parse import parse_qs, urlparse


def is_youtube_url(url: str) -> bool:
    """Check if URL is a valid YouTube URL."""
    youtube_patterns = [
        r"(?:https?://)?(?:www\.)?youtube\.com/watch\?v=[\w-]+",
        r"(?:https?://)?(?:www\.)?youtu\.be/[\w-]+",
        r"(?:https?://)?(?:www\.)?youtube\.com/embed/[\w-]+",
        r"(?:https?://)?(?:www\.)?youtube\.com/v/[\w-]+",
    ]

    return any(re.match(pattern, url, re.IGNORECASE) for pattern in youtube_patterns)


def is_youtube_playlist_url(url: str) -> bool:
    """Check if URL is a valid YouTube playlist URL."""
    playlist_patterns = [
        r"(?:https?://)?(?:www\.)?youtube\.com/playlist\?list=[\w-]+",
        r"(?:https?://)?(?:www\.)?youtube\.com/watch\?.*list=[\w-]+",
    ]

    return any(re.match(pattern, url, re.IGNORECASE) for pattern in playlist_patterns)


def extract_video_id(url: str) -> str | None:
    """Extract video ID from YouTube URL."""
    if not is_youtube_url(url):
        return None

    # Parse URL
    parsed = urlparse(url)

    # Standard youtube.com/watch?v=VIDEO_ID
    if "youtube.com" in parsed.netloc and "watch" in parsed.path:
        query_params = parse_qs(parsed.query)
        return query_params.get("v", [None])[0]

    # Short youtu.be/VIDEO_ID
    if "youtu.be" in parsed.netloc:
        return parsed.path.lstrip("/")

    # Embed youtube.com/embed/VIDEO_ID
    if "youtube.com" in parsed.netloc and "embed" in parsed.path:
        return parsed.path.split("/")[-1]

    # Direct youtube.com/v/VIDEO_ID
    if "youtube.com" in parsed.netloc and "/v/" in parsed.path:
        return parsed.path.split("/")[-1]

    return None


def extract_playlist_id(url: str) -> str | None:
    """Extract playlist ID from YouTube URL."""
    if not is_youtube_playlist_url(url):
        return None

    # Parse URL
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)

    return query_params.get("list", [None])[0]


def normalize_youtube_url(url: str) -> str | None:
    """Normalize YouTube URL to standard format."""
    video_id = extract_video_id(url)
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id}"

    playlist_id = extract_playlist_id(url)
    if playlist_id:
        return f"https://www.youtube.com/playlist?list={playlist_id}"

    return None
