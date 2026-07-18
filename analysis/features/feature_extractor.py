from analysis.backends.librosa_backend import LibrosaBackend


class FeatureExtractor:

    def __init__(self):

        self.backend = LibrosaBackend()

    # ---------------------------------------------------------

    def extract(self, song):

        return self.backend.extract_features(song)