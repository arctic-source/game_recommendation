from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit


def style_button(button: QPushButton) -> None:
    """
    Apply a predefined style to a QPushButton.
    """
    button.setStyleSheet("""
        QPushButton {
            background-color: rgb(7, 7, 7);
            color: rgb(255, 255, 255);
            border: 1px solid rgb(100, 100, 100);
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: rgb(20, 20, 20);
        }
        QPushButton:pressed {
            background-color: rgb(50, 50, 50);
        }
    """)


def style_search_button(button: QPushButton) -> None:
    """
    Apply a predefined style to a search QPushButton.
    """
    button.setStyleSheet("""
        QPushButton {
            color: rgb(255, 255, 255);
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(215, 21, 59, 255), stop:1 rgba(164, 49, 136, 255));
            font: 12pt "Segoe UI";
            background-color: rgb(0, 0, 0);
            background-color: qlineargradient(spread:pad, x1:0.222, y1:0.227273, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(66, 66, 66, 255));
        }
        QPushButton:hover {
            background-color: rgb(20, 20, 20);
        }
        QPushButton:pressed {
            background-color: rgb(50, 50, 50);
        }
    """)


def style_app_title(label: QLabel) -> None:
    """
    Apply a predefined style to a QLabel that stores the title of the app.
    """
    label.setStyleSheet("""
        QLabel {
            color: rgb(200, 200, 200);
            font-size: 14px;
        }
    """)


def style_game_title(label: QLabel) -> None:
    """
    Apply a predefined style to a QLabel that stores a title of a game
    """
    label.setStyleSheet("""
        QLabel {
            color: rgb(255, 255, 255);
            background-color: rgba(25, 25, 25, 50);
        }
    """)


def style_label(label: QLabel) -> None:
    """
    Apply a predefined style to a QLabel.
    """
    label.setStyleSheet("""
        QLabel {
            color: rgb(200, 200, 200);
            font-size: 14px;
        }
    """)


def style_line_edit(line_edit: QLineEdit) -> None:
    """
    Apply a predefined style to a QLineEdit.
    """
    line_edit.setStyleSheet("""
        QLineEdit {
            background-color: rgb(30, 30, 30);
            color: rgb(255, 255, 255);
            border: 1px solid rgb(100, 100, 100);
            border-radius: 5px;
            padding: 5px;
        }
        QLineEdit:focus {
            border: 1px solid rgb(255, 165, 0);
        }
    """)
