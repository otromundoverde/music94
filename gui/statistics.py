from database.statistics_repository import StatisticsRepository


class Statistics:

    def __init__(self):

        self.repository = StatisticsRepository()

    # ---------------------------------------------------------

    def summary(self):

        seconds = self.repository.total_duration()

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60

        return {

            "songs": self.repository.total_songs(),

            "artists": self.repository.total_artists(),

            "albums": self.repository.total_albums(),

            "genres": self.repository.total_genres(),

            "duration": f"{hours}h {minutes}m",

        }