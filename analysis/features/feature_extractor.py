from analysis.backends.librosa_backend import LibrosaBackend


class FeatureExtractor:

    def __init__(self):

        self.backend = LibrosaBackend()

    # ---------------------------------------------------------

    def extract(self, song):

        features = self.backend.extract_features(song)

        features.audio = self.backend.load_audio(song)

        return features