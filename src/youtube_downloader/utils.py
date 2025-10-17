"""
URL validation utilities for YouTube.
"""

import re
from urllib.parse import parse_qs, urlencode, urlparse


def is_youtube_url(url: str) -> bool:
    """Check if URL is a valid YouTube URL."""
    youtube_patterns = [
        r"(?:https?://)?(?:www\.)?youtube\.com/watch\?.*v=[\w-]+",
        r"(?:https?://)?(?:www\.)?youtu\.be/[\w-]+",
        r"(?:https?://)?(?:www\.)?youtube\.com/embed/[\w-]+",
        r"(?:https?://)?(?:www\.)?youtube\.com/v/[\w-]+",
    ]

    return any(re.match(pattern, url, re.IGNORECASE) for pattern in youtube_patterns)


def is_youtube_playlist_url(url: str) -> bool:
    """Check if URL is a valid YouTube playlist URL."""
    # Simplifiquei para usar apenas parse_qs ao invés de regex complexo
    parsed = urlparse(url)

    # Verificar se é domínio do YouTube
    if not any(
        domain in parsed.netloc.lower() for domain in ["youtube.com", "youtu.be"]
    ):
        return False

    # Verificar se tem parâmetro list na query string
    query_params = parse_qs(parsed.query)
    return "list" in query_params and len(query_params["list"]) > 0


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
    # Parse URL
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)

    # Buscar parâmetro 'list' independente de outros parâmetros
    playlist_list = query_params.get("list", [])
    if playlist_list and len(playlist_list) > 0:
        return playlist_list[0]

    return None


def normalize_youtube_url(url: str) -> str | None:
    """Normalize YouTube URL to standard format."""
    # Tentar extrair video ID primeiro
    video_id = extract_video_id(url)
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id}"

    # Tentar extrair playlist ID
    playlist_id = extract_playlist_id(url)
    if playlist_id:
        return f"https://www.youtube.com/playlist?list={playlist_id}"

    return None


def clean_youtube_url(url: str) -> str:
    """Remove unnecessary parameters from YouTube URLs like 'si', 'feature', etc."""
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)

    # Manter apenas parâmetros essenciais
    essential_params = {}

    if "v" in query_params:
        essential_params["v"] = query_params["v"][0]
    if "list" in query_params:
        essential_params["list"] = query_params["list"][0]
    if "t" in query_params:  # timestamp
        essential_params["t"] = query_params["t"][0]

    # Reconstruir URL limpa
    if essential_params:
        query_string = urlencode(essential_params)
        return f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{query_string}"
    else:
        return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
