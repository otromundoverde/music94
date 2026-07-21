from analysis.base_analyzer import BaseAnalyzer


class SpeechinessAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        if features.speechiness is not None:

            song.speechiness = features.speechiness

        return song