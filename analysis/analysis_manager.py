from analysis.bpm_analyzer import BPMAnalyzer
from analysis.key_analyzer import KeyAnalyzer
from analysis.loudness_analyzer import LoudnessAnalyzer
from analysis.dynamic_range_analyzer import DynamicRangeAnalyzer
from analysis.replaygain_analyzer import ReplayGainAnalyzer
from analysis.mood_analyzer import MoodAnalyzer
from analysis.similarity_analyzer import SimilarityAnalyzer


class AnalysisManager:

    def __init__(self):

        self.bpm = BPMAnalyzer()

        self.key = KeyAnalyzer()

        self.loudness = LoudnessAnalyzer()

        self.dynamic = DynamicRangeAnalyzer()

        self.replaygain = ReplayGainAnalyzer()

        self.mood = MoodAnalyzer()

        self.similarity = SimilarityAnalyzer()

    # ---------------------------------------------------------

    def analyze(self, song):

        self.bpm.analyze(song)

        self.key.analyze(song)

        self.loudness.analyze(song)

        self.dynamic.analyze(song)

        self.replaygain.analyze(song)

        self.mood.analyze(song)

        self.similarity.analyze(song)

        return song