class JobManager:

    def __init__(self):

        self.jobs = []

    # ---------------------------------------------------------

    def add(self, job):

        self.jobs.append(job)

    # ---------------------------------------------------------

    def start_all(self):

        for job in self.jobs:

            job.start()

    # ---------------------------------------------------------

    def clear(self):

        self.jobs.clear()

    # ---------------------------------------------------------

    def running_jobs(self):

        return [

            job

            for job in self.jobs

            if job.running

        ]

    # ---------------------------------------------------------

    def finished_jobs(self):

        return [

            job

            for job in self.jobs

            if job.finished

        ]