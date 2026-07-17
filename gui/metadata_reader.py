from mutagen import File
from mutagen.mp3 import MP3
from pathlib import Path


class MetadataReader:

    SUPPORTED_FORMATS = (
        ".mp3",
        ".flac",
        ".ogg",
        ".m4a",
        ".wav",
        ".aiff",
    )

    def __init__(self):
        pass

    def read(self, filepath):

        filepath = Path(filepath)

        if filepath.suffix.lower() not in self.SUPPORTED_FORMATS:
            return None

        try:

            audio = File(filepath, easy=True)

            if audio is None:
                return None

            info = File(filepath)

            metadata = {

                "title": self._tag(audio, "title", filepath.stem),

                "artist": self._tag(audio, "artist", "Desconocido"),

                "album": self._tag(audio, "album", "Desconocido"),

                "genre": self._tag(audio, "genre", "Sin género"),

                "year": self._year(audio),

                "track": self._track(audio),

                "duration": self._duration(info),

                "bitrate": self._bitrate(info),

                "samplerate": self._samplerate(info),

                "channels": self._channels(info),

                "extension": filepath.suffix.lower(),

                "filename": filepath.name,

                "folder": str(filepath.parent),

                "path": str(filepath),

                "size": filepath.stat().st_size,

            }

            return metadata

        except Exception:

            return None

    def _tag(self, audio, key, default):

        if key not in audio:
            return default

        value = audio[key]

        if isinstance(value, list):
            if len(value):
                return str(value[0])

        return str(value)

    def _year(self, audio):

        for tag in ("date", "year"):

            if tag in audio:

                value = str(audio[tag][0])

                if len(value) >= 4:
                    return value[:4]

        return ""

    def _track(self, audio):

        if "tracknumber" not in audio:
            return ""

        value = str(audio["tracknumber"][0])

        return value.split("/")[0]

    def _duration(self, info):

        try:

            seconds = int(info.info.length)

            minutes = seconds // 60

            seconds = seconds % 60

            return f"{minutes}:{seconds:02d}"

        except Exception:

            return ""

    def _bitrate(self, info):

        try:

            return int(info.info.bitrate / 1000)

        except Exception:

            return ""

    def _samplerate(self, info):

        try:

            return info.info.sample_rate

        except Exception:

            return ""

    def _channels(self, info):

        try:

            return info.info.channels

        except Exception:

            return ""