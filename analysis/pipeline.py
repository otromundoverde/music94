from analysis.bpm_analyzer import BPMAnalyzer
from analysis.dynamic_range_analyzer import DynamicRangeAnalyzer
from analysis.key_analyzer import KeyAnalyzer
from analysis.loudness_analyzer import LoudnessAnalyzer
from analysis.mood_analyzer import MoodAnalyzer
from analysis.replaygain_analyzer import ReplayGainAnalyzer
from analysis.similarity_analyzer import SimilarityAnalyzer

from analysis.features.feature_extractor import FeatureExtractor


class AnalysisPipeline:

    def __init__(self):

        self.extractor = FeatureExtractor()

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

        features = self.extractor.extract(song)

        song.bpm = features.bpm

        song.musical_key = features.musical_key

        song.camelot = features.camelot

        song.energy = features.energy

        song.danceability = features.danceability

        song.acousticness = features.acousticness

        song.instrumentalness = features.instrumentalness

        song.speechiness = features.speechiness

        song.loudness = features.loudness

        song.dynamic_range = features.dynamic_range

        song.replaygain = features.replaygain

        song.mood = features.mood

        for analyzer in self.modules:

            analyzer.analyze(song)

        return song