from abc import ABC
from abc import abstractmethod


class BaseAnalyzer(ABC):

    @abstractmethod
    def analyze(self, song):

        pass