from PySide6.QtWidgets import QWidget, QVBoxLayout

from gui.header import Header
from gui.search_bar import SearchBar
from gui.filter_bar import FilterBar
from gui.library_table import LibraryTable


class ContentPanel(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        self.header = Header()

        self.search = SearchBar()

        self.filters = FilterBar()

        self.table = LibraryTable()

        self.search.searchChanged.connect(
            self.update_library
        )

        self.filters.filtersChanged.connect(
            self.update_library
        )

        layout.addWidget(self.header)
        layout.addWidget(self.search)
        layout.addWidget(self.filters)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def update_library(self):

        songs = self.table.library.filter(

            text=self.search.box.text(),

            genre=self.filters.genre.currentText(),

            decade=self.filters.decade.currentText(),

            order=self.filters.order.currentText(),

        )

        self.table.load(songs)

    def show_page(self, page):

        self.header.set_page(page)

        if page == "Biblioteca":

            self.table.show_library()

            self.update_library()

        elif page == "Artistas":

            self.table.show_list(

                "Artistas",

                self.table.library.artists()

            )

        elif page == "Álbumes":

            self.table.show_list(

                "Álbumes",

                self.table.library.albums()

            )

        elif page == "Géneros":

            self.table.show_list(

                "Géneros",

                self.table.library.genres()

            )

        elif page == "Décadas":

            self.table.show_list(

                "Décadas",

                self.table.library.decades()

            )

        elif page == "Favoritos":

            self.table.show_list(

                "Favoritos",

                []

            )