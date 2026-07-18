from pathlib import Path

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

    def extract_features(self, song):

        features = FeatureSet()

        if not self.available:

            return features

        try:

            audio_path = Path(song.path)

            if not audio_path.exists():

                return features

            y, sr = self.librosa.load(

                audio_path,

                sr=None,

                mono=True,

            )

            print(

                f"[Music94] Loaded: {audio_path.name}"

            )

            print(

                f"Samples: {len(y):,}"

            )

            print(

                f"Sample Rate: {sr}"

            )

        except Exception as error:

            print(error)

        return features