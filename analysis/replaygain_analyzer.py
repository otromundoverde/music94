from analysis.base_analyzer import BaseAnalyzer


class ReplayGainAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        if features.replaygain is not None:

            song.replaygain = features.replaygain

        return song