from analysis.backends.audio_backend import AudioBackend
from analysis.features.feature_set import FeatureSet


class LibrosaBackend(AudioBackend):

    def __init__(self):

        pass

    # ---------------------------------------------------------

    def extract_features(self, song):

        features = FeatureSet()

        #
        # Próximamente:
        #
        # BPM
        # Key
        # Chroma
        # MFCC
        # Loudness
        # Spectral Features
        #

        return features