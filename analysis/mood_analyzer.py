from analysis.base_analyzer import BaseAnalyzer


class MoodAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        song.energy = features.energy
        song.danceability = features.danceability
        song.acousticness = features.acousticness
        song.instrumentalness = features.instrumentalness
        song.speechiness = features.speechiness
        song.mood = features.mood

        return song