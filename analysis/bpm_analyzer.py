from analysis.base_analyzer import BaseAnalyzer


class BPMAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        if features.bpm is not None:

            song.bpm = features.bpm

        return song