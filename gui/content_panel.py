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

        # ===========================================
        # CARGAR BIBLIOTECA INICIAL
        # ===========================================

        self.refresh_table()

        # ===========================================
        # CONEXIONES
        # ===========================================

        self.search.searchChanged.connect(
            self.refresh_table
        )

        self.filters.filtersChanged.connect(
            self.refresh_table
        )

    # -------------------------------------------------

    def refresh_table(self):

        songs = self.manager.query(

            text=self.search.box.text(),

            genre=self.filters.genre.currentText(),

            decade=self.filters.decade.currentText(),

            order=self.filters.order.currentText(),

        )

        self.table.load_songs(songs)

    # -------------------------------------------------

    def load_library(self, library):

        self.manager.load_library(library)

        self.refresh_table()