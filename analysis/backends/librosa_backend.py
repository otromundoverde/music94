from pathlib import Path

import numpy as np

from analysis.audio_data import AudioData
from analysis.backends.audio_backend import AudioBackend
from analysis.cache.audio_cache import AudioCache
from analysis.features.feature_set import FeatureSet


class LibrosaBackend(AudioBackend):

    def __init__(self):

        self.available = False
        self.librosa = None

        self.cache = AudioCache()

        try:

            import librosa

            self.librosa = librosa
            self.available = True

            print("[Music94] Librosa backend loaded.")

        except Exception as error:

            print(error)

    # ---------------------------------------------------------

    def load_audio(self, song):

        if self.cache.has(song.path):

            return self.cache.get(song.path)

        audio = AudioData()

        if not self.available:

            return audio

        try:

            path = Path(song.path)

            if not path.exists():

                return audio

            samples, sample_rate = self.librosa.load(

                path,
                sr=None,
                mono=True,

            )

            audio.samples = samples
            audio.sample_rate = sample_rate
            audio.duration = len(samples) / sample_rate
            audio.channels = 1

            self.cache.put(song.path, audio)

        except Exception as error:

            print(error)

        return audio

    # ---------------------------------------------------------

    def extract_features(self, song):

        features = FeatureSet()

        audio = self.load_audio(song)

        if audio.samples is None:

            return features

        try:

            tempo, _ = self.librosa.beat.beat_track(

                y=audio.samples,
                sr=audio.sample_rate,

            )

            if isinstance(tempo, np.ndarray):

                if tempo.size:

                    tempo = float(tempo.flat[0])

                else:

                    return features

            else:

                tempo = float(tempo)

            features.bpm = round(tempo, 2)

            print(

                f"[Music94] {song.title} -> {features.bpm:.2f} BPM"

            )

        except Exception as error:

            print(error)

        return features