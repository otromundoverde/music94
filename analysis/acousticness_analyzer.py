from analysis.base_analyzer import BaseAnalyzer


class AcousticnessAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        if features.acousticness is not None:

            song.acousticness = features.acousticness

        return song