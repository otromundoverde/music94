from analysis.base_analyzer import BaseAnalyzer


CAMELOT = {

    "Ab": "4B",
    "Eb": "5B",
    "Bb": "6B",
    "F": "7B",
    "C": "8B",
    "G": "9B",
    "D": "10B",
    "A": "11B",
    "E": "12B",
    "B": "1B",
    "F#": "2B",
    "C#": "3B",

    "Fm": "4A",
    "Cm": "5A",
    "Gm": "6A",
    "Dm": "7A",
    "Am": "8A",
    "Em": "9A",
    "Bm": "10A",
    "F#m": "11A",
    "C#m": "12A",
    "G#m": "1A",
    "D#m": "2A",
    "A#m": "3A",

}


class KeyAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        if features.musical_key is not None:

            song.musical_key = features.musical_key

        song.camelot = CAMELOT.get(

            song.musical_key,

            "",

        )

        return song