from analysis.base_analyzer import BaseAnalyzer


class BPMAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        song.bpm = features.bpm

        return song