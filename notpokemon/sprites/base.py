from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QPixmap, QColor


class SpriteRenderer:
    GRID_SIZE = 32

    def __init__(self):
        self._pixmap_cache: dict[int, QPixmap] = {}

    def render(self, scale: int = 4) -> QPixmap:
        if scale in self._pixmap_cache:
            return self._pixmap_cache[scale]
        size = self.GRID_SIZE * scale
        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, False)
        self._draw(painter, scale)
        painter.end()
        self._pixmap_cache[scale] = pixmap
        return pixmap

    def render_flipped(self, scale: int = 4) -> QPixmap:
        original = self.render(scale)
        return original.transformed(
            original.trueMatrix(
                original.deviceIndependentSize().toSize().width(),
                original.deviceIndependentSize().toSize().height(),
            ).scale(-1, 1)
        ) if False else self._render_flipped(scale)

    def _render_flipped(self, scale: int) -> QPixmap:
        size = self.GRID_SIZE * scale
        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, False)
        # Flip horizontally
        painter.translate(size, 0)
        painter.scale(-1, 1)
        self._draw(painter, scale)
        painter.end()
        return pixmap

    def _draw(self, painter: QPainter, scale: int):
        raise NotImplementedError

    def _pixel(self, painter: QPainter, x: int, y: int, color: QColor, scale: int):
        painter.fillRect(QRect(x * scale, y * scale, scale, scale), color)

    def _rect(self, painter: QPainter, x: int, y: int, w: int, h: int,
              color: QColor, scale: int):
        painter.fillRect(QRect(x * scale, y * scale, w * scale, h * scale), color)

    def _draw_grid(self, painter: QPainter, scale: int,
                   grid: list[str], palette: dict[str, QColor]):
        for y, row in enumerate(grid):
            for x, char in enumerate(row):
                if char != '.':
                    color = palette.get(char)
                    if color:
                        self._pixel(painter, x, y, color, scale)
