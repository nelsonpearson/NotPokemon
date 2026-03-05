from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QStackedWidget

from notpokemon.constants import WINDOW_WIDTH, WINDOW_HEIGHT, BG_COLOR


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NotPokemon")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet(f"background-color: {BG_COLOR.name()};")

        self._stack = QStackedWidget()
        self.setCentralWidget(self._stack)

    @property
    def stack(self) -> QStackedWidget:
        return self._stack

    def add_screen(self, widget, name: str) -> int:
        index = self._stack.addWidget(widget)
        widget.setObjectName(name)
        return index

    def show_screen(self, index: int):
        self._stack.setCurrentIndex(index)
