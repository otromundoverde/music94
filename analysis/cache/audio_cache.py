from analysis.audio_data import AudioData


class AudioCache:

    def __init__(self):

        self._cache = {}

    # ---------------------------------------------------------

    def clear(self):

        self._cache.clear()

    # ---------------------------------------------------------

    def has(self, path):

        return path in self._cache

    # ---------------------------------------------------------

    def get(self, path):

        return self._cache.get(path)

    # ---------------------------------------------------------

    def put(self, path, audio: AudioData):

        self._cache[path] = audio

    # ---------------------------------------------------------

    def remove(self, path):

        if path in self._cache:

            del self._cache[path]

    # ---------------------------------------------------------

    def size(self):

        return len(self._cache)

    # ---------------------------------------------------------

    def statistics(self):

        return {

            "cached_files": len(self._cache)

        }