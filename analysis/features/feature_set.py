from dataclasses import dataclass


@dataclass
class FeatureSet:

    bpm: float | None = None

    musical_key: str = ""

    camelot: str = ""

    energy: float | None = None

    danceability: float | None = None

    acousticness: float | None = None

    instrumentalness: float | None = None

    speechiness: float | None = None

    loudness: float | None = None

    dynamic_range: float | None = None

    replaygain: float | None = None

    mood: str = ""

    fingerprint: str = ""

    similarity_vector: list | None = None