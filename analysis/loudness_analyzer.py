from analysis.base_analyzer import BaseAnalyzer


class LoudnessAnalyzer(BaseAnalyzer):

    def analyze(self, song):

        audio = self.audio.load_audio(song)

        if audio.rms is None:

            return song

        return song