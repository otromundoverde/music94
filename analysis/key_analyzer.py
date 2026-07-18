from analysis.base_analyzer import BaseAnalyzer


class KeyAnalyzer(BaseAnalyzer):

    def analyze(self, song):

        audio = self.audio.load_audio(song)

        if audio.chroma is None:

            return song

        return song