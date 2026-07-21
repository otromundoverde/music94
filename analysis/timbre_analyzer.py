from analysis.base_analyzer import BaseAnalyzer


class TimbreAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        if features.timbre is not None:

            song.timbre = features.timbre

        return song