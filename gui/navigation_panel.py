from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
)


class NavigationPanel(QWidget):

    page_selected = Signal(str)

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("BIBLIOTECA")

        title.setStyleSheet("""
            font-size:16px;
            font-weight:bold;
            padding:8px;
        """)

        layout.addWidget(title)

        self.menu = QListWidget()

        self.populate()

        self.menu.currentTextChanged.connect(
            self.page_selected.emit
        )

        layout.addWidget(self.menu)

        self.setLayout(layout)

        self.menu.setCurrentRow(1)

    def add_section(self, text):

        item = QListWidgetItem(text)

        item.setFlags(item.flags() & ~item.flags().ItemIsSelectable)

        item.setForeground(self.palette().mid())

        self.menu.addItem(item)

    def add_page(self, text):

        self.menu.addItem("   " + text)

    def populate(self):

        self.add_page("Inicio")

        self.menu.addItem("")

        self.add_section("MÚSICA")

        self.add_page("Canciones")
        self.add_page("Álbumes")
        self.add_page("Artistas")
        self.add_page("Géneros")
        self.add_page("Décadas")

        self.menu.addItem("")

        self.add_section("COLECCIONES")

        self.add_page("Favoritos")
        self.add_page("Playlists")
        self.add_page("Descubrimientos")

        self.menu.addItem("")

        self.add_section("ANÁLISIS")

        self.add_page("Estadísticas")
        self.add_page("BPM")
        self.add_page("Tonalidades")
        self.add_page("Duplicados")

        self.menu.addItem("")

        self.add_section("SPOTIFY")

        self.add_page("Biblioteca Spotify")
        self.add_page("Álbumes Spotify")
        self.add_page("Playlists Spotify")
        self.add_page("Artistas Spotify")

        self.menu.addItem("")

        self.add_section("HERRAMIENTAS")

        self.add_page("Importaciones")
        self.add_page("Exportaciones")
        self.add_page("Registro")