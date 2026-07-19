import numpy as np

from analysis.base_analyzer import BaseAnalyzer


NOTE_NAMES = (

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

)


class KeyAnalyzer(BaseAnalyzer):

    def analyze(self, song):

        audio = self.audio.load_audio(song)

        if audio.chroma is None:

            return song

        chroma = np.mean(audio.chroma, axis=1)

        note = int(np.argmax(chroma))

        song.musical_key = NOTE_NAMES[note]

        song.camelot = self.camelot(song.musical_key)

        print(

            f"[Music94] {song.title} -> {song.musical_key} ({song.camelot})"

        )

        return song

    # -----------------------------------------------------

    def camelot(self, key):

        table = {

            "C":"8B",
            "C#":"3B",
            "D":"10B",
            "Eb":"5B",
            "E":"12B",
            "F":"7B",
            "F#":"2B",
            "G":"9B",
            "Ab":"4B",
            "A":"11B",
            "Bb":"6B",
            "B":"1B",

        }

        return table.get(key, "")