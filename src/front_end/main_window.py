# external imports
import os
from typing import LiteralString
import numpy as np
import pandas as pd
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QUrl, QStringListModel
from PyQt6.QtGui import QPixmap, QIcon, QMovie, QDesktopServices
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QWidget, QLineEdit, QCompleter
)
from PyQt6 import uic
from functools import partial

# internal imports
from src.back_end.data_processing.helpers.shorten_title_length import shorten_title_length
from src.back_end.placeholders import UI_PATH, ANIMATIONS_PATH, ICON_PATH, NUM_RECOMMENDATIONS
from src.back_end.data_processing.pipeline import preprocess, process
from src.back_end.recommend.recommendation_handler import handle_recommend_action
from src.front_end.loading_window import LoadingScreen


class RecommendationThread(QThread):
    """
    A Separate thread to run recommendation to keep the main window responsive.
    """
    result = pyqtSignal(dict)

    def __init__(
            self, game_title: str, dataset_processed: pd.DataFrame, dataset_preprocessed: pd.DataFrame, parent=None
    ):
        """

        Args:
            game_title: Game title as stands on Steam website
            dataset_processed: dataset with numerical and categorical attributes ready for similarity search
            dataset_preprocessed: dataset without NaNs, trademark symbols, with manual imputations for popular games
        """
        super().__init__(parent)
        self.game_title = game_title
        self.dataset_processed = dataset_processed
        self.dataset_preprocessed = dataset_preprocessed

    def run(self):
        """
        Method that runs when QThread is started. Handles the action to recommend games and emits signal when search for
        all similar games is finished. This signal is caught by MainWindow and it ends loading and shows the result.

        """
        try:
            recommended_titles_urls_thumbnails = handle_recommend_action(
                user_input_text=self.game_title,
                dataset_processed=self.dataset_processed,
                dataset_preprocessed=self.dataset_preprocessed
            )
            self.result.emit(recommended_titles_urls_thumbnails)

        except Exception as e:
            print(f"Error in RecommendationThread: {e}")


class MainWindow(QMainWindow):
    """
    Main window of the Steam game recommendation system.

    This class handles the setup of the UI, event connections, and handles the display of game recommendations.
    """
    def __init__(self):
        """
        Initialize the main window and its UI components
        """
        super().__init__()
        self.init_ui()
        self.showMaximized()

    def load_data(self):
        """
        Get preprocessed dataset and processed dataset

        preprocessed dataset (self.dataset) - remove NaNs, trademark symbols, use manual imputations in place of NaN for
        popular games

        processed dataset (self.dataset_) - prepare dataset for similarity search - impute and parse dates, convert
        dates to numerical values, one-hot encode categorical variables, drop columns, scale numerical columns to
        [0, 1], convert to pandas df

        """
        self.dataset = preprocess()
        self.dataset_ = process(self.dataset)

    def load_ui_elements(self):
        """
        Load UI objects from .ui file, map them to class attributes to control their behavior in python
        """
        self.button_recommend = self.findChild(QPushButton, "button_recommend")
        self.line_editor = self.findChild(QLineEdit, 'line_edit')
        self.label_recommendations = self.findChild(QLabel, 'label_recommendations_field')

        self.titles = [self.findChild(QLabel, f"label_game{i}_title") for i in range(1, NUM_RECOMMENDATIONS+1)]
        self.thumbnails = [self.findChild(QLabel, f"label_game{i}_thumbnail") for i in range(1, NUM_RECOMMENDATIONS+1)]
        self.links = [self.findChild(QPushButton, f"button_game{i}_link") for i in range(1, NUM_RECOMMENDATIONS+1)]

        self.central_widget = self.findChild(QWidget, "centralwidget")
        self.label_loading_movie = self.findChild(QLabel, 'label_loading_movie')

        self.setWindowTitle('What should I play next?')
        self.icon = QIcon(ICON_PATH)
        self.setWindowIcon(self.icon)

    def initialize_objects(self):
        # loading and animations
        self.loading_screen = None
        animation_full_path = self.get_animation_path()
        self.movie = QMovie(animation_full_path)

        # titles, urls, thumbnail paths
        self.recommendation_titles = []
        self.recommendation_urls = []
        self.recommendation_thumbnail_paths = []

    def load_ui_from_ui_file(self):
        """load .ui file that was designed in Qt Designer"""
        uic.loadUi(UI_PATH, self)

    def setup_completer(self):
        """Setup completer that suggests game names to user as he types"""
        # game title suggestions - words to suggest
        words = self.dataset_['title'].tolist()
        # game title suggestions - model
        model = QStringListModel()
        model.setStringList(words)
        # game title suggestions - completer
        completer = QCompleter()
        completer.setModel(model)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.line_editor.setCompleter(completer)
        self.line_editor.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: black;
            }
        """)

    def show_recommendation_data(self):
        """Given recommendation data such as titles, thumbnails and links to games, displays these results on screen"""
        for i in range(NUM_RECOMMENDATIONS):

            # show title
            label_title = self.titles[i]
            shortened_title = shorten_title_length(self.recommendation_titles[i])
            label_title.setText(shortened_title)
            label_title.setStyleSheet(label_title.styleSheet() + "font-size: 16px;")
            label_title.show()

            # show thumbnail
            label_thumbnail = self.thumbnails[i]
            pixmap = QPixmap()
            pixmap.load(self.recommendation_thumbnail_paths[i])
            scaled_pixmap = pixmap.scaled(label_thumbnail.size(), Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation)
            label_thumbnail.setPixmap(scaled_pixmap)
            label_thumbnail.setScaledContents(True)
            label_thumbnail.show()

            # show link to Steam website
            button_link = self.links[i]
            url = self.recommendation_urls[i]
            if url == '':
                full_text = ''
            else:
                full_text = "Steam link"
            button_link.setText(full_text)
            button_link.setCursor(Qt.CursorShape.PointingHandCursor)

            # disconnect previous connections
            try:
                button_link.clicked.disconnect()
            except TypeError:
                pass  # no connections to disconnect

            # connect the new URL to the button
            button_link.clicked.connect(partial(self.open_link, url))

    def open_link(self, url):
        """Open link in web browser on click"""
        QDesktopServices.openUrl(QUrl(url))

    def setup_signals(self):
        """connect button click to function that handles button click"""
        self.button_recommend.clicked.connect(self.handle_button_click)

    def handle_button_click(self):
        """
        Handle button click by showing the loading screen, then read the user input and start game recommendation in a
        separate thread to keep the UI responsive

        """
        # show loading screen
        self.start_loading()

        # prepare inputs for recommendation
        game_title = self.line_editor.text()
        self.recommendation_thread = RecommendationThread(game_title, self.dataset_, self.dataset)
        self.recommendation_thread.result.connect(self.handle_recommendation_result)
        self.recommendation_thread.start()

    def get_animation_path(self) -> LiteralString | str | bytes:
        """Selects a random animation gif from the folder with "best" animations"""
        random_animation_name = np.random.choice(os.listdir(ANIMATIONS_PATH))
        animation_full_path = os.path.join(ANIMATIONS_PATH, random_animation_name)
        return animation_full_path

    def start_loading(self):
        """Show the loading screen."""
        if not self.loading_screen:
            self.loading_screen = LoadingScreen(self)
            self.loading_screen.show()
            QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)

    def stop_loading(self):
        """Close the loading screen when the task is done."""
        if self.loading_screen:
            self.loading_screen.stop_animation()
            self.loading_screen = None  # Reset reference
            QApplication.restoreOverrideCursor()

    def init_ui(self):
        """
        Performs initialization of the user interface. Reads .ui file, loads it and binds its objects to python
        variables, initializes internal objects, sets up completer and the recommendation button clicks.
        """
        self.load_ui_from_ui_file()
        self.load_data()
        self.load_ui_elements()
        self.initialize_objects()
        self.setup_completer()
        self.setup_signals()

    def handle_recommendation_result(self, result):
        """
        Handles the recommended game titles, urls and thumbnail paths that arrived from game recommendation methods.
        E.g. calls a function to show them and stops the loading screen.

        """
        # digest resulting thumbnail
        self.recommendation_titles = result['titles']
        self.recommendation_urls = result['urls']
        self.recommendation_thumbnail_paths = result['thumbnail_paths']

        # show recommendations to user
        self.show_recommendation_data()
        self.stop_loading()
