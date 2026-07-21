from analysis.base_analyzer import BaseAnalyzer


class MoodAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        energy = song.energy or 0.0

        dance = song.danceability or 0.0

        acoustic = song.acousticness or 0.0

        speech = song.speechiness or 0.0

        valence = features.valence or 0.0

        if acoustic > 0.70:

            song.mood = "Acoustic"

        elif speech > 0.45:

            song.mood = "Spoken"

        elif energy > 0.70 and valence > 0.60:

            song.mood = "Happy"

        elif energy > 0.70:

            song.mood = "Energetic"

        elif dance > 0.65:

            song.mood = "Dance"

        elif valence < 0.35:

            song.mood = "Dark"

        elif energy < 0.30:

            song.mood = "Calm"

        else:

            song.mood = "Balanced"

        return song