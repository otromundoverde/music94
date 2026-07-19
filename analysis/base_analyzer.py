from analysis.backends.librosa_backend import LibrosaBackend


class BaseAnalyzer:

    backend = LibrosaBackend()

    def analyze(self, song):

        raise NotImplementedError