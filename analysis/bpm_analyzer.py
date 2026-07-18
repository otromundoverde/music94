from analysis.base_analyzer import BaseAnalyzer


class BPMAnalyzer(BaseAnalyzer):

    def analyze(self, song):

        features = self.audio.extract_features(song)

        if features.bpm is not None:

            song.bpm = features.bpm

        return song