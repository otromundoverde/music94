from abc import ABC
from abc import abstractmethod

from analysis.features.feature_set import FeatureSet


class AudioBackend(ABC):

    @abstractmethod
    def extract_features(self, song) -> FeatureSet:
        pass