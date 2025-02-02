from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import Qt

from src.back_end.placeholders import LOADING_GIF_PATH


class LoadingScreen(QWidget):
    """
    Loading screen that gets shown during the search for similar games and live web scraping for game thumbnails.

    This class handles the setup of the UI, layout, the elements inside the UI and stop of the loading animation.
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        # remove window decorations and set it as modal
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # Optional: Makes it look better

        # get screen size and make full overlay
        screen_geometry = QApplication.primaryScreen().geometry()
        self.setGeometry(screen_geometry)  # cover whole sCreen

        # set semi-transparent background to focus on the fabulous cat loading
        self.setStyleSheet("background-color: rgba(0, 0, 0, 150);")  # Dark overlay

        # centered container for the loading animation
        self.loading_container = QWidget(self)
        self.loading_container.setFixedSize(200, 200)  # Adjust size as needed
        self.loading_container.setStyleSheet("background-color: white; border-radius: 10px;")  # White rounded box

        # center the loading container in the screen
        self.center_loading_container()

        # Layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # QLabel to hold the GIF
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # load GIF
        self.movie = QMovie(LOADING_GIF_PATH)  # Make sure loading.gif exists
        self.label.setMovie(self.movie)
        self.movie.start()

        layout.addWidget(self.label)
        self.setLayout(layout)

    def center_loading_container(self):
        """Centers the loading container in the full-screen overlay."""
        screen_geometry = QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.loading_container.width()) // 2
        y = (screen_geometry.height() - self.loading_container.height()) // 2
        self.loading_container.move(x, y)

    def stop_animation(self):
        """Stop and close the loading screen"""
        self.movie.stop()
        self.close()
