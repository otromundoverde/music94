from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QMainWindow,
    QSplitter,
)

from gui.navigation_panel import NavigationPanel
from gui.library_table import LibraryTable
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

        splitter.addWidget(NavigationPanel())
        splitter.addWidget(LibraryTable())

        splitter.setSizes([250, 950])

        self.setCentralWidget(splitter)

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