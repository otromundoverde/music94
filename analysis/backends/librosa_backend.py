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

        #
        # El análisis real comenzará en v0.5.3
        #

        return features