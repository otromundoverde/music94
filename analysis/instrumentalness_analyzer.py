from analysis.base_analyzer import BaseAnalyzer


class InstrumentalnessAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        if features.instrumentalness is not None:

            song.instrumentalness = features.instrumentalness

        return song