from analysis.base_analyzer import BaseAnalyzer


class EnergyAnalyzer(BaseAnalyzer):

    def analyze(self, song, features):

        if features.energy is not None:

            song.energy = features.energy

        return song