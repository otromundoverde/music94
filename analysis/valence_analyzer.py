from analysis.base_analyzer import BaseAnalyzer


class ValenceAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        if features.valence is not None:

            song.valence = features.valence

        return song