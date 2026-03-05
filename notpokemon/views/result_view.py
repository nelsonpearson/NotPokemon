from PySide6.QtCore import Qt, Signal, QTimer
from PySide6.QtGui import QPainter, QFont, QColor, QLinearGradient
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy,
)


class ResultView(QWidget):
    next_clicked = Signal()
    retry_clicked = Signal()
    quit_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._is_victory = True
        self._is_champion = False
        self._title_label: QLabel | None = None
        self._subtitle_label: QLabel | None = None
        self._next_btn: QPushButton | None = None
        self._retry_btn: QPushButton | None = None
        self._quit_btn: QPushButton | None = None
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(16)

        layout.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Policy.Minimum,
                                         QSizePolicy.Policy.Expanding))

        self._title_label = QLabel("YOU WIN!")
        self._title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._title_label.setStyleSheet(
            "font-family: monospace; font-size: 42px; font-weight: bold; "
            "color: #f39c12; background: transparent;"
        )
        layout.addWidget(self._title_label)

        self._subtitle_label = QLabel("")
        self._subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._subtitle_label.setStyleSheet(
            "font-family: monospace; font-size: 16px; color: #8899aa; background: transparent;"
        )
        layout.addWidget(self._subtitle_label)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum,
                                         QSizePolicy.Policy.Fixed))

        btn_style = """
            QPushButton {{
                background-color: {bg};
                color: #e0e0e0;
                border: 2px solid {border};
                border-radius: 8px;
                font-family: monospace;
                font-size: 14px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {hover};
                color: #ffffff;
            }}
        """

        self._next_btn = QPushButton("NEXT BATTLE")
        self._next_btn.setFixedSize(200, 44)
        self._next_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self._next_btn.setStyleSheet(
            btn_style.format(bg="#2c6b3e", border="#2ecc71", hover="#3d9152")
        )
        self._next_btn.clicked.connect(self.next_clicked.emit)
        layout.addWidget(self._next_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        self._retry_btn = QPushButton("RETRY BATTLE")
        self._retry_btn.setFixedSize(200, 44)
        self._retry_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self._retry_btn.setStyleSheet(
            btn_style.format(bg="#6b2c2c", border="#e74c3c", hover="#913d3d")
        )
        self._retry_btn.clicked.connect(self.retry_clicked.emit)
        layout.addWidget(self._retry_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        self._quit_btn = QPushButton("RETURN TO TITLE")
        self._quit_btn.setFixedSize(200, 44)
        self._quit_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self._quit_btn.setStyleSheet(
            btn_style.format(bg="#2c3e6b", border="#3d5291", hover="#3d5291")
        )
        self._quit_btn.clicked.connect(self.quit_clicked.emit)
        layout.addWidget(self._quit_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addSpacerItem(QSpacerItem(20, 80, QSizePolicy.Policy.Minimum,
                                         QSizePolicy.Policy.Expanding))

    def show_victory(self, is_champion: bool = False):
        self._is_victory = True
        self._is_champion = is_champion

        if is_champion:
            self._title_label.setText("CHAMPION!")
            self._title_label.setStyleSheet(
                "font-family: monospace; font-size: 48px; font-weight: bold; "
                "color: #f1c40f; background: transparent;"
            )
            self._subtitle_label.setText("You defeated all opponents!")
            self._next_btn.setVisible(False)
            self._retry_btn.setVisible(False)
        else:
            self._title_label.setText("YOU WIN!")
            self._title_label.setStyleSheet(
                "font-family: monospace; font-size: 42px; font-weight: bold; "
                "color: #2ecc71; background: transparent;"
            )
            self._subtitle_label.setText("Prepare for the next battle...")
            self._next_btn.setVisible(True)
            self._retry_btn.setVisible(False)

        self._quit_btn.setVisible(True)

    def show_defeat(self):
        self._is_victory = False
        self._is_champion = False

        self._title_label.setText("DEFEATED...")
        self._title_label.setStyleSheet(
            "font-family: monospace; font-size: 42px; font-weight: bold; "
            "color: #e74c3c; background: transparent;"
        )
        self._subtitle_label.setText("Your creature fainted!")
        self._next_btn.setVisible(False)
        self._retry_btn.setVisible(True)
        self._quit_btn.setVisible(True)
