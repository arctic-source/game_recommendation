from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QCompleter


class CustomCompleter(QCompleter):
    def popup(self):
        view = super().popup()
        view.setIconSize(QSize(50, 50))  # Customize the size as needed
        return view