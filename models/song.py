from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class Song:

    id: Optional[int] = None

    # ============================
    # METADATA ORIGINAL
    # ============================

    title: str = ""
    artist: str = ""
    album: str = ""
    album_artist: str = ""
    genre: str = ""
    year: str = ""
    track: str = ""
    disc: str = ""
    composer: str = ""
    label: str = ""
    country: str = ""

    duration: int = 0

    bitrate: int = 0
    sample_rate: int = 0
    channels: int = 0

    filename: str = ""
    extension: str = ""
    folder: str = ""
    path: str = ""
    filesize: int = 0

    # ============================
    # MUSIC94 ANALYSIS
    # ============================

    bpm: Optional[float] = None
    musical_key: str = ""
    camelot: str = ""

    energy: Optional[float] = None
    danceability: Optional[float] = None
    acousticness: Optional[float] = None
    instrumentalness: Optional[float] = None
    speechiness: Optional[float] = None

    loudness: Optional[float] = None
    dynamic_range: Optional[float] = None
    replaygain: Optional[float] = None

    mood: str = ""

    valence: Optional[float] = None

    brightness: Optional[float] = None

    timbre: Optional[float] = None

    # ============================
    # MUSIC94
    # ============================

    cover_path: str = ""

    date_added: str = ""

    last_modified: str = ""