from analysis.backends.librosa_backend import LibrosaBackend


class BaseAnalyzer:

    backend = LibrosaBackend()

    def __init__(self):

        self.audio = self.backend

    def analyze(self, song):

        raise NotImplementedError