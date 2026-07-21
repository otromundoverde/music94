from analysis.base_analyzer import BaseAnalyzer


class KeyAnalyzer(BaseAnalyzer):

    NOTES = [

        "C",
        "C#",
        "D",
        "Eb",
        "E",
        "F",
        "F#",
        "G",
        "Ab",
        "A",
        "Bb",
        "B",

    ]

    def analyze(self, song, features):

        if features.key_strength is None:

            return song

        audio = features.audio

        if audio is None:

            return song

        if audio.chroma is None:

            return song

        import numpy as np

        chroma = np.mean(audio.chroma, axis=1)

        note = int(np.argmax(chroma))

        song.musical_key = self.NOTES[note]

        return song