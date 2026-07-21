from analysis.base_analyzer import BaseAnalyzer


class DynamicRangeAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        song.dynamic_range = features.dynamic_range

        return song