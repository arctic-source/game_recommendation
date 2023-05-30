import sys

from PyQt6.QtWidgets import QApplication

from front_end.app import RecommendationAppWindow


def main():
    app = QApplication([])
    window = RecommendationAppWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()