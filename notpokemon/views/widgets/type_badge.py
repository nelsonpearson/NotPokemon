from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor, QFont
from PySide6.QtWidgets import QWidget

from notpokemon.constants import TYPE_COLORS
from notpokemon.models.types import ElementType


class TypeBadge(QWidget):
    def __init__(self, element: ElementType | None = None, parent=None):
        super().__init__(parent)
        self._element = element
        self.setFixedSize(70, 22)

    def set_element(self, element: ElementType):
        self._element = element
        self.update()

    def paintEvent(self, event):
        if self._element is None:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        color = TYPE_COLORS.get(self._element.value, QColor(100, 100, 100))
        painter.setBrush(color.darker(130))
        painter.setPen(color)
        painter.drawRoundedRect(1, 1, self.width() - 2, self.height() - 2, 4, 4)

        painter.setPen(QColor(255, 255, 255))
        font = QFont("monospace", 9, QFont.Weight.Bold)
        painter.setFont(font)
        painter.drawText(
            0, 0, self.width(), self.height(),
            Qt.AlignmentFlag.AlignCenter,
            self._element.value.upper()
        )

        painter.end()
