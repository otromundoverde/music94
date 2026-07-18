from analysis.bpm_analyzer import BPMAnalyzer
from analysis.dynamic_range_analyzer import DynamicRangeAnalyzer
from analysis.key_analyzer import KeyAnalyzer
from analysis.loudness_analyzer import LoudnessAnalyzer
from analysis.mood_analyzer import MoodAnalyzer
from analysis.replaygain_analyzer import ReplayGainAnalyzer
from analysis.similarity_analyzer import SimilarityAnalyzer


class AnalysisPipeline:

    def __init__(self):

        self.modules = [

            BPMAnalyzer(),

            KeyAnalyzer(),

            LoudnessAnalyzer(),

            ReplayGainAnalyzer(),

            DynamicRangeAnalyzer(),

            MoodAnalyzer(),

            SimilarityAnalyzer(),

        ]

    # ---------------------------------------------------------

    def analyze(self, song):

        for analyzer in self.modules:

            analyzer.analyze(song)

        return song