from abc import ABC, abstractmethod


class BaseJob(ABC):

    def __init__(self):

        self.running = False
        self.finished = False
        self.progress = 0
        self.total = 0
        self.cancelled = False

    # ---------------------------------------------------------

    def start(self):

        self.running = True
        self.finished = False
        self.cancelled = False

        self.run()

        self.running = False
        self.finished = True

    # ---------------------------------------------------------

    def cancel(self):

        self.cancelled = True

    # ---------------------------------------------------------

    @abstractmethod
    def run(self):

        pass