from analysis.base_analyzer import BaseAnalyzer


class ReplayGainAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        song.replaygain = features.replaygain

        return song