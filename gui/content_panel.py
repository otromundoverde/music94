from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)

from gui.header import Header
from gui.search_bar import SearchBar
from gui.filter_bar import FilterBar
from gui.library_table import LibraryTable
from gui.details_panel import DetailsPanel
from gui.library_manager import LibraryManager


class ContentPanel(QWidget):

    def __init__(self):
        super().__init__()

        self.manager = LibraryManager()

        layout = QVBoxLayout()

        self.header = Header()

        self.search = SearchBar()

        self.filters = FilterBar()

        self.table = LibraryTable()

        self.details = DetailsPanel()

        layout.addWidget(self.header)

        layout.addWidget(self.search)

        layout.addWidget(self.filters)

        layout.addWidget(self.table, 1)

        layout.addWidget(self.details)

        self.setLayout(layout)

        self.refresh_library()

        self.table.song_selected.connect(
            self.details.update_song
        )

        self.search.searchChanged.connect(
            self.refresh_library
        )

        self.filters.filtersChanged.connect(
            self.refresh_library
        )

    # ==================================================

    def refresh_library(self):

        songs = self.manager.get_library()

        text = self.search.box.text()

        genre = self.filters.genre.currentText()

        decade = self.filters.decade.currentText()

        order = self.filters.order.currentText()

        songs = self.manager.search(text)

        songs = self.manager.filter(
            songs=songs,
            genre=genre,
            decade=decade,
        )

        songs = self.manager.sort(
            songs=songs,
            order=order,
        )

        self.table.load_library(songs)

    # ==================================================

    def statistics(self):

        return self.manager.statistics()