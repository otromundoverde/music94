from database.analytics_repository import AnalyticsRepository


class AnalyticsEngine:

    def __init__(self):

        self.repository = AnalyticsRepository()

    # ---------------------------------------------------------

    def library_summary(self):

        return {

            "top_artists": self.repository.top_artists(),

            "top_albums": self.repository.top_albums(),

            "top_genres": self.repository.top_genres(),

            "top_labels": self.repository.top_labels(),

            "top_countries": self.repository.top_countries(),

        }

    # ---------------------------------------------------------

    def dashboard(self):

        return {

            "years": self.repository.songs_by_year(),

            "decades": self.repository.songs_by_decade(),

            "extensions": self.repository.songs_by_extension(),

            "bitrates": self.repository.songs_by_bitrate(),

            "samplerates": self.repository.songs_by_samplerate(),

        }