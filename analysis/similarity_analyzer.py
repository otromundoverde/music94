from analysis.base_analyzer import BaseAnalyzer


class SimilarityAnalyzer(BaseAnalyzer):

    def analyze(self, song):

        audio = self.audio.load_audio(song)

        if audio.mfcc is None:

            return song

        return song