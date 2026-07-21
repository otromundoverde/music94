from analysis.base_analyzer import BaseAnalyzer


class MoodAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        song.mood = features.mood

        return song