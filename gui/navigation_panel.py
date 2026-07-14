from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem


class NavigationPanel(QTreeWidget):
    def __init__(self):
        super().__init__()

        self.setHeaderHidden(True)

        biblioteca = QTreeWidgetItem(["Biblioteca"])

        QTreeWidgetItem(biblioteca, ["Canciones"])
        QTreeWidgetItem(biblioteca, ["Artistas"])
        QTreeWidgetItem(biblioteca, ["Álbumes"])
        QTreeWidgetItem(biblioteca, ["Géneros"])
        QTreeWidgetItem(biblioteca, ["Décadas"])
        QTreeWidgetItem(biblioteca, ["Favoritos"])

        self.addTopLevelItem(biblioteca)
        biblioteca.setExpanded(True)
        