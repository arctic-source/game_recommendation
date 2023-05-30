import os

from PyQt6.QtWidgets import QLineEdit, QWidget, QMainWindow, QPushButton, QLabel, QApplication
from PyQt6.QtGui import QPixmap, QDesktopServices, QMovie, QIcon
from PyQt6.QtCore import QStringListModel, Qt, QUrl, QThread, pyqtSignal
from PyQt6 import uic
import numpy as np

from data_processing.helpers.get_recommendation_titles import get_recommendation_titles
from data_processing.pipeline import preprocess, process
from front_end.suggestion_completer.CustomCompleter import CustomCompleter
from recommend.pipeline import recommend
from steam_webscraping.scrape_game_thumbnail.fetch_game_thumbnail_path import fetch_game_thumbnail_path


class RecommendationThread(QThread):
    result = pyqtSignal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        titles, urls, thumbnail_paths = self.parent().handleRecommendAction(self.parent().line_editor.text())
        self.result.emit((titles, urls, thumbnail_paths))

class RecommendationAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def loadData(self):
        self.dataset = preprocess()
        self.dataset_ = process(self.dataset)
        self.num_recommendations = 5

        self.recommendation_titles = []
        self.recommendation_urls = []
        self.recommendation_thumbnail_paths = []

    def loadUIElements(self):
        self.button_recommend = self.findChild(QPushButton, "button_recommend")
        self.line_editor = self.findChild(QLineEdit, 'line_edit')
        self.label_recommendations = self.findChild(QLabel, 'label_recommendations_field')

        self.titles = [self.findChild(QLabel, f"label_game{i}_title") for i in range(1, 6)]
        self.thumbnails = [self.findChild(QLabel, f"label_game{i}_thumbnail") for i in range(1, 6)]
        self.links = [self.findChild(QPushButton, f"button_game{i}_link") for i in range(1, 6)]

        self.widget_loading = self.findChild(QWidget, f'widget_loading')
        self.widget_loading.setVisible(False)
        self.label_loading_movie = self.findChild(QLabel, f'label_loading_movie')
        animation_full_path = self.getAnimationPath()
        self.movie = QMovie(animation_full_path)
        self.label_loading_movie.setMovie(self.movie)

        self.setWindowTitle('What should I play next?')
        self.icon = QIcon(self.getIconPath())
        self.setWindowIcon(self.icon)


    def loadUIfromUIfile(self):
        uic.loadUi(r"front_end\ui\ui_v11.ui", self)

    def refreshCompleter(self):
        # game title suggestions - words to suggest
        words = get_recommendation_titles(self.dataset_)
        # game title suggestions - model
        model = QStringListModel()
        model.setStringList(words)
        # game title suggestions - completer
        completer = CustomCompleter()
        completer.setModel(model)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.line_editor.setCompleter(completer)

    def cutTitleLength(self, title):
        longest_allowed_title = 34 # characters
        if len(title) >= longest_allowed_title:
            shortened_title = title[:longest_allowed_title] + ' ...'
        else:
            shortened_title = title
        return shortened_title

    def showRecommendationData(self):
        for i in range(self.num_recommendations):

            # show title
            label_title = self.titles[i]
            shortened_title = self.cutTitleLength(self.recommendation_titles[i])
            label_title.setText(shortened_title)
            label_title.setStyleSheet(label_title.styleSheet() + "font-size: 16px;")
            label_title.show()

            # show thumbnail
            label_thumbnail = self.thumbnails[i]
            pixmap = QPixmap()
            pixmap.load(self.recommendation_thumbnail_paths[i])
            label_thumbnail.setPixmap(pixmap)
            label_thumbnail.setScaledContents(True)
            label_thumbnail.show()


            # show link
            button_link = self.links[i]
            url = self.recommendation_urls[i]
            if url == '':
                full_text = ''
            else:
                full_text = "Steam link"
            button_link.setText(full_text)
            button_link.clicked.connect(lambda state, x=url: self.open_link(x))
            button_link.setCursor(Qt.CursorShape.PointingHandCursor)


    def open_link(self, url):
        QDesktopServices.openUrl(QUrl(url))

    def refreshButton(self):
        self.button_recommend.clicked.connect(lambda: self.handleButtonClick())


    def handleButtonClick(self):
        self.startLoading()
        self.recommendation_thread = RecommendationThread(self)
        self.recommendation_thread.result.connect(self.handleRecommendationResult)
        self.recommendation_thread.start()

    def getAnimationPath(self):
        current_path_and_filename = os.path.abspath(__file__)
        current_path = os.path.dirname(current_path_and_filename)
        project_path = os.path.abspath(os.path.join(current_path, '..'))
        animations_folder_path = os.path.join(project_path, 'animations', 'best')
        animation_files = os.listdir(animations_folder_path)
        index = np.random.randint(0, len(animation_files))
        animation_file = animation_files[index]
        animation_full_path = os.path.join(animations_folder_path, animation_file)
        return animation_full_path

    def getIconPath(self):
        current_path_and_filename = os.path.abspath(__file__)
        current_path = os.path.dirname(current_path_and_filename)
        project_path = os.path.abspath(os.path.join(current_path, '..'))
        icon_folder_path = os.path.join(project_path, 'front_end', 'icons')
        icon_file = 'icon.png'
        icon_full_path = os.path.join(icon_folder_path, icon_file)
        return icon_full_path

    def startLoading(self):
        self.widget_loading.setVisible(True)
        self.movie.start()
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)

    def stopLoading(self):
        self.widget_loading.setVisible(False)
        self.movie.stop()
        QApplication.restoreOverrideCursor()

    def initUI(self):

        self.loadUIfromUIfile()
        self.loadData()
        self.loadUIElements()
        self.refreshCompleter()
        self.refreshButton()
        self.handleButtonClick()

    def loadEmptyThumbnail(self):
        current_path_and_filename = os.path.abspath(__file__)
        current_path = os.path.dirname(current_path_and_filename)
        project_path = os.path.abspath(os.path.join(current_path, '..'))
        animations_folder_path = os.path.join(project_path, 'steam_data', 'steam_thumbnails')
        animation_file = 'blank.jpg'
        animation_full_path = os.path.join(animations_folder_path, animation_file)
        return animation_full_path

    def handleRecommendationResult(self, result):
        self.recommendation_titles, self.recommendation_urls, self.recommendation_thumbnail_paths = result
        self.showRecommendationData()
        self.stopLoading()

    def handleRecommendAction(self, user_input_text):
        game_titles = ['', '', '', '', '']
        urls = ['', '', '', '', '']
        thumbnail_paths = [self.loadEmptyThumbnail() for i in range(self.num_recommendations)]

        if user_input_text is None:
            return game_titles, urls, thumbnail_paths
        elif user_input_text == '':
            return game_titles, urls, thumbnail_paths

        # check if desired game exists
        titles_lowercase = self.dataset_['title'].str.lower().tolist()
        user_input_text_lowercase = user_input_text.lower()

        if user_input_text_lowercase not in titles_lowercase:
            return game_titles, urls, thumbnail_paths

        instance = self.dataset_.loc[self.dataset_['title'].str.lower() == user_input_text_lowercase]
        # list of recommended titles
        recommendations_dataframe = recommend(instance=instance,
                                              dataset_processed=self.dataset_,
                                              dataset_preprocessed=self.dataset,
                                              num_recommendations=self.num_recommendations)
        titles = recommendations_dataframe['title'].tolist()

        # urls
        urls = self.dataset.loc[recommendations_dataframe.index]['url'].tolist()

        # game thumbnails
        thumbnail_paths = []
        for url in urls:
            thumbnail_paths.append(fetch_game_thumbnail_path(steam_game_url=url))

        return titles, urls, thumbnail_paths
