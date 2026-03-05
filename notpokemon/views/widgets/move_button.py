from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPainter, QColor, QFont
from PySide6.QtWidgets import QPushButton

from notpokemon.constants import TYPE_COLORS
from notpokemon.models.move import Move, MoveCategory


class MoveButton(QPushButton):
    move_clicked = Signal(int)

    def __init__(self, move_index: int, parent=None):
        super().__init__(parent)
        self._move_index = move_index
        self._move: Move | None = None
        self._type_color = QColor(100, 100, 100)
        self.setFixedSize(170, 60)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.clicked.connect(self._on_clicked)

    def set_move(self, move: Move):
        self._move = move
        self._type_color = TYPE_COLORS.get(move.element.value, QColor(100, 100, 100))
        self.setToolTip(move.description)
        self.update()

    def _on_clicked(self):
        self.move_clicked.emit(self._move_index)

    def paintEvent(self, event):
        if self._move is None:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        w = self.width()
        h = self.height()

        # Background
        bg = self._type_color.darker(180) if not self.isEnabled() else self._type_color.darker(140)
        if self.underMouse() and self.isEnabled():
            bg = self._type_color.darker(110)

        painter.setBrush(bg)
        painter.setPen(self._type_color)
        painter.drawRoundedRect(1, 1, w - 2, h - 2, 6, 6)

        # Type color accent bar at top
        painter.setBrush(self._type_color)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(1, 1, w - 2, 6, 3, 3)
        painter.drawRect(1, 4, w - 2, 3)

        # Move name
        text_color = QColor(255, 255, 255) if self.isEnabled() else QColor(150, 150, 150)
        painter.setPen(text_color)
        font = QFont("monospace", 11, QFont.Weight.Bold)
        painter.setFont(font)
        painter.drawText(8, 18, w - 16, 20, Qt.AlignmentFlag.AlignLeft, self._move.name)

        # Power / category info
        font.setPointSize(9)
        font.setWeight(QFont.Weight.Normal)
        painter.setFont(font)
        painter.setPen(QColor(200, 200, 200) if self.isEnabled() else QColor(120, 120, 120))

        if self._move.category == MoveCategory.PHYSICAL:
            info = f"PWR {self._move.power}  ACC {self._move.accuracy}%"
        elif self._move.category == MoveCategory.HEAL:
            info = f"HEAL {self._move.heal_percent}%"
        else:
            info = "STATUS"
        painter.drawText(8, 36, w - 16, 20, Qt.AlignmentFlag.AlignLeft, info)

        painter.end()
