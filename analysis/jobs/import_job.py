from analysis.jobs.base_job import BaseJob


class ImportJob(BaseJob):

    def __init__(self, importer, folder):

        super().__init__()

        self.importer = importer
        self.folder = folder
        self.library = []

    # ---------------------------------------------------------

    def run(self):

        self.library = self.importer.import_folder(

            self.folder

        )