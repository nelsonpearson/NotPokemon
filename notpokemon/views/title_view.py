from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPainter, QFont, QColor, QLinearGradient
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy


class TitleView(QWidget):
    start_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addSpacerItem(QSpacerItem(20, 120, QSizePolicy.Policy.Minimum,
                                         QSizePolicy.Policy.Expanding))

        # Title is drawn in paintEvent
        layout.addSpacerItem(QSpacerItem(20, 100, QSizePolicy.Policy.Minimum,
                                         QSizePolicy.Policy.Fixed))

        start_btn = QPushButton("START GAME")
        start_btn.setFixedSize(200, 50)
        start_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        start_btn.setStyleSheet("""
            QPushButton {
                background-color: #2c3e6b;
                color: #e0e0e0;
                border: 2px solid #f39c12;
                border-radius: 8px;
                font-family: monospace;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3d5291;
                color: #ffffff;
            }
            QPushButton:pressed {
                background-color: #1a2544;
            }
        """)
        start_btn.clicked.connect(self.start_clicked.emit)

        layout.addWidget(start_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacerItem(QSpacerItem(20, 80, QSizePolicy.Policy.Minimum,
                                         QSizePolicy.Policy.Expanding))

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw title
        title_font = QFont("monospace", 48, QFont.Weight.Bold)
        painter.setFont(title_font)

        gradient = QLinearGradient(0, 100, 0, 180)
        gradient.setColorAt(0, QColor("#f39c12"))
        gradient.setColorAt(1, QColor("#e74c3c"))

        pen = painter.pen()
        pen.setBrush(gradient)
        pen.setWidth(1)
        painter.setPen(pen)

        painter.drawText(
            0, 80, self.width(), 80,
            Qt.AlignmentFlag.AlignCenter,
            "NOT POKEMON"
        )

        # Subtitle
        sub_font = QFont("monospace", 14)
        painter.setFont(sub_font)
        painter.setPen(QColor("#8899aa"))
        painter.drawText(
            0, 160, self.width(), 30,
            Qt.AlignmentFlag.AlignCenter,
            "A Totally Different Creature Battling Game"
        )

        painter.end()
