from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QMainWindow,
    QSplitter,
)

from controllers.menu_controller import MenuController

from gui.content_panel import ContentPanel
from gui.navigation_panel import NavigationPanel
from gui.status_bar import Music94StatusBar
from gui.tool_bar import Music94ToolBar


class Music94(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music94")
        self.resize(1280, 720)

        # ==========================================================
        # MENÚ
        # ==========================================================

        self.create_menu()

        # ==========================================================
        # STATUS BAR
        # ==========================================================

        self.setStatusBar(Music94StatusBar())

        # ==========================================================
        # TOOLBAR
        # ==========================================================

        self.toolbar = Music94ToolBar()
        self.addToolBar(self.toolbar)

        # ==========================================================
        # PANEL CENTRAL
        # ==========================================================

        splitter = QSplitter(Qt.Horizontal)

        self.navigation = NavigationPanel()
        self.content = ContentPanel()

        splitter.addWidget(self.navigation)
        splitter.addWidget(self.content)

        splitter.setSizes([240, 1040])

        self.setCentralWidget(splitter)

        # ==========================================================
        # CONEXIONES
        # ==========================================================

        self.navigation.page_selected.connect(
            self.content.header.set_page
        )

        self.content.table.song_selected.connect(
            self.content.details.update_song
        )

        # ==========================================================
        # CONTROLLERS
        # ==========================================================

        self.menu_controller = MenuController(self)

    
        

    # ==========================================================
    # IMPORTAR MÚSICA
    # ==========================================================

   
    def create_menu(self):
        menu = self.menuBar()

        archivo = menu.addMenu("Archivo")
        biblioteca = menu.addMenu("Biblioteca")
        spotify = menu.addMenu("Spotify")
        ver = menu.addMenu("Ver")
        herramientas = menu.addMenu("Herramientas")
        ayuda = menu.addMenu("Ayuda")

        # ==========================================================
        # ARCHIVO
        # ==========================================================

        self.action_new_project = QAction("Nuevo proyecto", self)

        self.action_open_library = QAction("Abrir biblioteca...", self)

        self.action_save_library = QAction("Guardar biblioteca", self)

        self.action_save_as = QAction("Guardar como...", self)

        self.action_import_music = QAction("Importar música...", self)

        self.action_import_folder = QAction("Importar carpeta...", self)

        self.action_export_csv = QAction("Exportar CSV", self)

        self.action_export_excel = QAction("Exportar Excel", self)

        self.action_export_json = QAction("Exportar JSON", self)

        self.action_exit = QAction("Salir", self)

        self.action_exit.triggered.connect(self.close)

        archivo.addAction(self.action_new_project)

        archivo.addSeparator()

        archivo.addAction(self.action_open_library)
        archivo.addAction(self.action_save_library)
        archivo.addAction(self.action_save_as)

        archivo.addSeparator()

        archivo.addAction(self.action_import_music)
        archivo.addAction(self.action_import_folder)

        archivo.addSeparator()

        archivo.addAction(self.action_export_csv)
        archivo.addAction(self.action_export_excel)
        archivo.addAction(self.action_export_json)

        archivo.addSeparator()

        archivo.addAction(self.action_exit)

        # ==========================================================
        # BIBLIOTECA
        # ==========================================================

        self.action_update_library = QAction(
            "Actualizar biblioteca",
            self
        )

        self.action_find_duplicates = QAction(
            "Buscar duplicados",
            self
        )

        self.action_reindex = QAction(
            "Reindexar biblioteca",
            self
        )

        self.action_verify = QAction(
            "Verificar archivos",
            self
        )

        self.action_statistics = QAction(
            "Calcular estadísticas",
            self
        )

        self.action_rebuild = QAction(
            "Reconstruir biblioteca",
            self
        )

        biblioteca.addAction(self.action_update_library)
        biblioteca.addSeparator()
        biblioteca.addAction(self.action_find_duplicates)
        biblioteca.addAction(self.action_reindex)
        biblioteca.addAction(self.action_verify)
        biblioteca.addSeparator()
        biblioteca.addAction(self.action_statistics)
        biblioteca.addAction(self.action_rebuild)

        # ==========================================================
        # SPOTIFY
        # ==========================================================

        self.action_spotify_connect = QAction(
            "Conectar cuenta",
            self
        )

        self.action_spotify_disconnect = QAction(
            "Desconectar",
            self
        )

        self.action_spotify_sync = QAction(
            "Sincronizar canciones",
            self
        )

        self.action_import_playlists = QAction(
            "Importar playlists",
            self
        )

        self.action_import_albums = QAction(
            "Importar álbumes",
            self
        )

        self.action_import_artists = QAction(
            "Importar artistas",
            self
        )

        self.action_spotify_refresh = QAction(
            "Actualizar información",
            self
        )

        spotify.addAction(self.action_spotify_connect)
        spotify.addAction(self.action_spotify_disconnect)

        spotify.addSeparator()

        spotify.addAction(self.action_spotify_sync)

        spotify.addSeparator()

        spotify.addAction(self.action_import_playlists)
        spotify.addAction(self.action_import_albums)
        spotify.addAction(self.action_import_artists)

        spotify.addSeparator()

        spotify.addAction(self.action_spotify_refresh)

        # ==========================================================
        # VER
        # ==========================================================

        self.action_view_library = QAction(
            "Biblioteca",
            self
        )

        self.action_view_songs = QAction(
            "Canciones",
            self
        )

        self.action_view_albums = QAction(
            "Álbumes",
            self
        )

        self.action_view_artists = QAction(
            "Artistas",
            self
        )

        self.action_view_genres = QAction(
            "Géneros",
            self
        )

        self.action_view_decades = QAction(
            "Décadas",
            self
        )

        self.action_view_favorites = QAction(
            "Favoritos",
            self
        )

        self.action_view_statistics = QAction(
            "Estadísticas",
            self
        )

        self.action_compact = QAction(
            "Modo compacto",
            self
        )

        self.action_fullscreen = QAction(
            "Pantalla completa",
            self
        )

        ver.addAction(self.action_view_library)
        ver.addAction(self.action_view_songs)
        ver.addAction(self.action_view_albums)
        ver.addAction(self.action_view_artists)
        ver.addAction(self.action_view_genres)
        ver.addAction(self.action_view_decades)
        ver.addAction(self.action_view_favorites)
        ver.addAction(self.action_view_statistics)

        ver.addSeparator()

        ver.addAction(self.action_compact)
        ver.addAction(self.action_fullscreen)

        # ==========================================================
        # HERRAMIENTAS
        # ==========================================================

        self.action_bpm = QAction(
            "Análisis BPM",
            self
        )

        self.action_key = QAction(
            "Análisis tonal",
            self
        )

        self.action_replaygain = QAction(
            "ReplayGain",
            self
        )

        self.action_duplicates = QAction(
            "Detectar duplicados",
            self
        )

        self.action_tags = QAction(
            "Editor de etiquetas",
            self
        )

        self.action_covers = QAction(
            "Gestor de portadas",
            self
        )

        self.action_genres = QAction(
            "Gestor de géneros",
            self
        )

        herramientas.addAction(self.action_bpm)
        herramientas.addAction(self.action_key)
        herramientas.addAction(self.action_replaygain)

        herramientas.addSeparator()

        herramientas.addAction(self.action_duplicates)

        herramientas.addSeparator()

        herramientas.addAction(self.action_tags)
        herramientas.addAction(self.action_covers)
        herramientas.addAction(self.action_genres)

        # ==========================================================
        # AYUDA
        # ==========================================================

        self.action_manual = QAction(
            "Manual",
            self
        )

        self.action_github = QAction(
            "Repositorio GitHub",
            self
        )

        self.action_updates = QAction(
            "Buscar actualizaciones",
            self
        )

        self.action_about = QAction(
            "Acerca de Music94",
            self
        )

        ayuda.addAction(self.action_manual)
        ayuda.addAction(self.action_github)

        ayuda.addSeparator()

        ayuda.addAction(self.action_updates)

        ayuda.addSeparator()

        ayuda.addAction(self.action_about)