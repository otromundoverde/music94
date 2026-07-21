from analysis.base_analyzer import BaseAnalyzer


class DanceabilityAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        if features.danceability is not None:

            song.danceability = features.danceability

        return song