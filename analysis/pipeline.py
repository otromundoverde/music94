from analysis.bpm_analyzer import BPMAnalyzer
from analysis.danceability_analyzer import DanceabilityAnalyzer
from analysis.dynamic_range_analyzer import DynamicRangeAnalyzer
from analysis.energy_analyzer import EnergyAnalyzer
from analysis.features.feature_extractor import FeatureExtractor
from analysis.key_analyzer import KeyAnalyzer
from analysis.loudness_analyzer import LoudnessAnalyzer
from analysis.mood_analyzer import MoodAnalyzer
from analysis.replaygain_analyzer import ReplayGainAnalyzer
from analysis.similarity_analyzer import SimilarityAnalyzer
from analysis.acousticness_analyzer import AcousticnessAnalyzer
from analysis.instrumentalness_analyzer import InstrumentalnessAnalyzer
from analysis.speechiness_analyzer import SpeechinessAnalyzer

class AnalysisPipeline:

    def __init__(self):

        self.extractor = FeatureExtractor()

        self.modules = [

            BPMAnalyzer(),

            KeyAnalyzer(),

            EnergyAnalyzer(),

            AcousticnessAnalyzer(),

            DanceabilityAnalyzer(),

            InstrumentalnessAnalyzer(),

            LoudnessAnalyzer(),

            ReplayGainAnalyzer(),

            DynamicRangeAnalyzer(),

            MoodAnalyzer(),

            SimilarityAnalyzer(),

        ]

    # ---------------------------------------------------------

    def analyze(self, song):

        features = self.extractor.extract(song)

        for analyzer in self.modules:

            analyzer.analyze(song, features)

        return song