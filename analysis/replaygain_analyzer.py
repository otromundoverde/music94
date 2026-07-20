from analysis.base_analyzer import BaseAnalyzer


class ReplayGainAnalyzer(BaseAnalyzer):

    def analyze(self, song):

        audio = self.backend.load_audio(song)

        if audio.samples is None:

            return song

        # Implementación real en una etapa posterior

        return song