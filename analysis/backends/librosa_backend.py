from pathlib import Path

from analysis.audio_data import AudioData
from analysis.backends.audio_backend import AudioBackend
from analysis.features.feature_set import FeatureSet


class LibrosaBackend(AudioBackend):

    def __init__(self):

        self.available = False

        self.librosa = None

        try:

            import librosa

            self.librosa = librosa

            self.available = True

            print("[Music94] Librosa backend loaded.")

        except Exception as error:

            print("[Music94] Librosa not available.")
            print(error)

    # ---------------------------------------------------------

    def load_audio(self, song):

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

        except Exception as error:

            print(error)

        return audio

    # ---------------------------------------------------------

    def extract_features(self, song):

        features = FeatureSet()

        audio = self.load_audio(song)

        #
        # Próximamente:
        #
        # BPM
        # Key
        # Loudness
        # etc.
        #

        return features