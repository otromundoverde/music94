from analysis.jobs.base_job import BaseJob


class AnalysisJob(BaseJob):

    def __init__(self, analyzer, songs):

        super().__init__()

        self.analyzer = analyzer
        self.songs = songs

    # ---------------------------------------------------------

    def run(self):

        self.total = len(self.songs)

        for index, song in enumerate(self.songs):

            if self.cancelled:

                break

            self.analyzer.analyze(song)

            self.progress = index + 1