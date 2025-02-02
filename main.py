import sys

from PyQt6.QtWidgets import QApplication

from src.front_end.main_window import MainWindow


def main():
    """
    Run the main event loop of the desktop app for recommending similar games.
    """
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
