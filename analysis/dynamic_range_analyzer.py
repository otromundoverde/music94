from analysis.base_analyzer import BaseAnalyzer

import numpy as np


class DynamicRangeAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        if features.dynamic_range is not None:

            song.dynamic_range = features.dynamic_range

        return song