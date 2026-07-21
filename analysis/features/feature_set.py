from dataclasses import dataclass


@dataclass
class FeatureSet:

    bpm: float | None = None

    musical_key: str = ""

    camelot: str = ""

    key_strength: float | None = None

    loudness: float | None = None

    dynamic_range: float | None = None

    replaygain: float | None = None

    energy: float | None = None

    danceability: float | None = None

    acousticness: float | None = None

    instrumentalness: float | None = None

    speechiness: float | None = None

    mood: str = ""

    valence: float | None = None

    brightness: float | None = None