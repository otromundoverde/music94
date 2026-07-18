from analysis.base_analyzer import BaseAnalyzer


class MoodAnalyzer(BaseAnalyzer):

    def analyze(self, song):

        audio = self.audio.load_audio(song)

        if audio.samples is None:

            return song

        return song