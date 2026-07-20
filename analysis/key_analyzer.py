from collections import Counter

import numpy as np

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

    def analyze(self, song):

        audio = self.backend.load_audio(song)

        if audio.chroma is None:

            return song

        try:

            chroma = np.sum(audio.chroma, axis=1)

            index = int(np.argmax(chroma))

            song.musical_key = self.NOTES[index]

        except Exception:

            song.musical_key = ""

        return song