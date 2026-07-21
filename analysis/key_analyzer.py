from analysis.base_analyzer import BaseAnalyzer


class KeyAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        song.musical_key = features.musical_key
        song.camelot = features.camelot

        return song