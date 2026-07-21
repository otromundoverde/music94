from analysis.base_analyzer import BaseAnalyzer


class LoudnessAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        song.loudness = features.loudness

        return song