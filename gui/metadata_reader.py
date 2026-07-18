from mutagen import File
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

                "album_artist": self._tag(audio, "albumartist", ""),

                "genre": self._tag(audio, "genre", "Sin género"),

                "year": self._year(audio),

                "track": self._track(audio),

                "disc": self._disc(audio),

                "composer": self._tag(audio, "composer", ""),

                "label": self._tag(audio, "label", ""),

                "country": "",

                "duration": self._duration_seconds(info),

                "bitrate": self._bitrate(info),

                "sample_rate": self._samplerate(info),

                "channels": self._channels(info),

                "filename": filepath.name,

                "extension": filepath.suffix.lower(),

                "folder": str(filepath.parent),

                "path": str(filepath),

                "filesize": filepath.stat().st_size,

            }

            return metadata

        except Exception:

            return None

    def _tag(self, audio, key, default):

        if key not in audio:
            return default

        value = audio[key]

        if isinstance(value, list):

            return str(value[0]) if value else default

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

        return str(audio["tracknumber"][0]).split("/")[0]

    def _disc(self, audio):

        if "discnumber" not in audio:

            return ""

        return str(audio["discnumber"][0]).split("/")[0]

    def _duration_seconds(self, info):

        try:

            return int(info.info.length)

        except Exception:

            return 0

    def _bitrate(self, info):

        try:

            return int(info.info.bitrate / 1000)

        except Exception:

            return 0

    def _samplerate(self, info):

        try:

            return int(info.info.sample_rate)

        except Exception:

            return 0

    def _channels(self, info):

        try:

            return int(info.info.channels)

        except Exception:

            return 0