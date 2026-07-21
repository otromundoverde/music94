from analysis.base_analyzer import BaseAnalyzer


class KeyAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        if features.musical_key:

            song.musical_key = features.musical_key

        if features.camelot:

            song.camelot = features.camelot

        return song