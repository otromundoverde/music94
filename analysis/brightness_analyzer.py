from analysis.base_analyzer import BaseAnalyzer


class BrightnessAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        if features.brightness is not None:

            song.brightness = features.brightness

        return song