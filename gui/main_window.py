from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QMainWindow,
    QSplitter,
)

from gui.content_panel import ContentPanel
from gui.navigation_panel import NavigationPanel
from gui.status_bar import Music94StatusBar
from gui.tool_bar import Music94ToolBar


class Music94(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Music94")

        self.resize(1200, 700)

        self.create_menu()

        self.setStatusBar(Music94StatusBar())

        self.addToolBar(Music94ToolBar())

        splitter = QSplitter(Qt.Horizontal)

        self.navigation = NavigationPanel()

        self.content = ContentPanel()

        splitter.addWidget(self.navigation)

        splitter.addWidget(self.content)

        splitter.setSizes([220, 980])

        self.setCentralWidget(splitter)

        self.navigation.page_selected.connect(
            self.content.show_page
        )

    def create_menu(self):

        menu = self.menuBar()

        archivo = menu.addMenu("Archivo")

        menu.addMenu("Biblioteca")

        menu.addMenu("Spotify")

        menu.addMenu("Ver")

        menu.addMenu("Herramientas")

        menu.addMenu("Ayuda")

        salir = QAction("Salir", self)

        salir.triggered.connect(self.close)

        archivo.addAction(salir)