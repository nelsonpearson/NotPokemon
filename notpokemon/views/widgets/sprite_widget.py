from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, Property, QPoint
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget

from notpokemon.sprites.base import SpriteRenderer


class SpriteWidget(QWidget):
    def __init__(self, renderer: SpriteRenderer | None = None, scale: int = 4,
                 flipped: bool = False, parent=None):
        super().__init__(parent)
        self._renderer = renderer
        self._scale = scale
        self._flipped = flipped
        self._opacity = 1.0
        self._offset = QPoint(0, 0)
        size = 32 * scale
        self.setFixedSize(size, size)

    def _get_opacity(self) -> float:
        return self._opacity

    def _set_opacity(self, value: float):
        self._opacity = value
        self.update()

    opacity = Property(float, _get_opacity, _set_opacity)

    def _get_offset_y(self) -> int:
        return self._offset.y()

    def _set_offset_y(self, value: int):
        self._offset = QPoint(self._offset.x(), value)
        self.update()

    offset_y = Property(int, _get_offset_y, _set_offset_y)

    def _get_offset_x(self) -> int:
        return self._offset.x()

    def _set_offset_x(self, value: int):
        self._offset = QPoint(value, self._offset.y())
        self.update()

    offset_x = Property(int, _get_offset_x, _set_offset_x)

    def set_renderer(self, renderer: SpriteRenderer, flipped: bool = False):
        self._renderer = renderer
        self._flipped = flipped
        self._opacity = 1.0
        self._offset = QPoint(0, 0)
        self.update()

    def paintEvent(self, event):
        if self._renderer is None:
            return

        painter = QPainter(self)
        painter.setOpacity(self._opacity)

        if self._flipped:
            pixmap = self._renderer._render_flipped(self._scale)
        else:
            pixmap = self._renderer.render(self._scale)

        painter.drawPixmap(self._offset, pixmap)
        painter.end()
