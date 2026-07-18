class AnalysisPipeline:

    def __init__(self):

        self.modules = []

    # ---------------------------------------------------------

    def register(self, analyzer):

        self.modules.append(analyzer)

    # ---------------------------------------------------------

    def analyze(self, song):

        for analyzer in self.modules:

            analyzer.analyze(song)

        return song